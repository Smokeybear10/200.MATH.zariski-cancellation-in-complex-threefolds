"""Bounded exact tame search. This is not a unittest or an exhaustion proof.

Prints JSON only. Replay a captured attempt count with --replay-attempts N;
that disables the wall-clock cap but preserves the deterministic choices.
"""

import argparse
import hashlib
import json
from pathlib import Path
import random
import time

import sympy as S


def run(batch, replay_attempts=None):
    rng = random.Random(82017 if batch == "initial" else 82018)
    s, a, b, c = S.symbols("s a b c")
    variables = (s, a, b, c)
    P = lambda f: S.Poly(f, *variables)
    seeds = [
        ([s, a, b, c], "identity"),
        ([s, a, b + a*a*s, c + b*b*s], "two-speed"),
        ([b + 2*a*a*c + a**4*s, c + a*a*s, s, a - b*s + c*c], "conic-square"),
        ([b + 2*a*c + a*a*s, c + a*s, s, a - b*s + c*c], "conic-linear"),
    ]
    if batch == "broader":
        for n in (2, 3):
            beta = sum((-1)**j * S.catalan(j) * a**j * b**(j + 1) / 2**j for j in range(n))
            x = beta + a**n*s
            y = S.cancel((x + a*x*x/2 - b) / a**n)
            seeds.append(([a, x, y, c], f"principal-n{n}"))
    pool = [([P(f) for f in frame], label, []) for frame, label in seeds]
    seed_count = len(pool)
    attempts = 3000 if batch == "initial" else 8000
    wall_cap = 45 if batch == "initial" else 35
    if replay_attempts is not None:
        attempts, wall_cap = replay_attempts, None
    config = {
        "batch": batch, "random_seed": 82017 if batch == "initial" else 82018,
        "attempt_limit": attempts, "wall_limit_seconds": wall_cap,
        "maximum_s_degree": 2, "maximum_total_degree": 12 if batch == "initial" else 14,
        "maximum_terms_per_coordinate": 70 if batch == "initial" else 80,
        "maximum_history_length_in_pool": 12 if batch == "initial" else 15,
        "maximum_pool_size": 180 if batch == "initial" else 240,
        "monomial_degree_choices": [1, 2, 2, 3] if batch == "initial" else [1, 2, 2, 3, 3, 4],
        "cancellation_probability_denominator": 4 if batch == "initial" else 2,
        "seed_frames": [{"name": label, "coordinates": list(map(str, frame))} for frame, label in seeds],
    }
    start = time.monotonic()
    counts = dict(attempts=0, accepted=0, rankone=0, nonprincipal=0,
                  membership=0, proper_nonprincipal_membership=0)
    seen, samples, counterexample = set(), [], None
    proper_ideals, nonprincipal_ideals = set(), set()
    while counts["attempts"] < attempts and (wall_cap is None or time.monotonic() - start < wall_cap):
        counts["attempts"] += 1
        frame, label, history = rng.choice(pool)
        target = rng.randrange(4)
        others = [i for i in range(4) if i != target]
        degree = rng.choice(config["monomial_degree_choices"])
        indices = [rng.choice(others) for _ in range(degree)]
        term = P(1)
        for i in indices:
            term *= frame[i]
        change = term if rng.randrange(2) else -term
        if rng.randrange(config["cancellation_probability_denominator"]) == 0:
            candidates = []
            for j in others:
                candidates.append((frame[j], [j]))
                for k in others:
                    if j <= k:
                        candidates.append((frame[j]*frame[k], [j, k]))
                        if batch == "broader":
                            for ell in others:
                                if k <= ell:
                                    candidates.append((frame[j]*frame[k]*frame[ell], [j, k, ell]))
            top_degree = 2 if batch == "initial" else term.degree(s)
            top = S.Poly(term.as_expr(), s).nth(top_degree) if term.degree(s) == top_degree and top_degree >= 2 else None
            if top is not None:
                rng.shuffle(candidates)
                for other, index in candidates:
                    if other.degree(s) != top_degree:
                        continue
                    ratio = S.cancel(top / S.Poly(other.as_expr(), s).nth(top_degree))
                    if ratio.is_Rational and ratio != 0:
                        change = term - P(ratio)*other
                        indices = ("cancel", indices, index, str(ratio))
                        break
        candidate = list(frame)
        candidate[target] += change
        if any(f.degree(s) > 2 or f.total_degree() > config["maximum_total_degree"]
               or len(f.terms()) > config["maximum_terms_per_coordinate"] for f in candidate):
            continue
        if candidate[target] == frame[target]:
            continue
        key = tuple(str(f.as_expr()) for f in candidate)
        if key in seen:
            continue
        seen.add(key)
        counts["accepted"] += 1
        newhistory = history + [(target, indices, str(change.as_expr()))]
        if len(newhistory) <= config["maximum_history_length_in_pool"]:
            pool.append((candidate, label, newhistory))
            if len(pool) > config["maximum_pool_size"]:
                pool.pop(rng.randrange(seed_count, len(pool)))
        bad = [i for i, f in enumerate(candidate) if f.degree(s) == 2]
        if len(bad) != 1:
            continue
        counts["rankone"] += 1
        speeds = [S.Poly(f.as_expr(), s).nth(1) for i, f in enumerate(candidate) if i != bad[0]]
        speeds = [f for f in speeds if f != 0]
        if len(speeds) < 2 or any(not f.free_symbols for f in speeds):
            continue
        gcd = S.gcd_list(speeds)
        primitive = [S.cancel(f/gcd) for f in speeds]
        if any(not f.free_symbols for f in primitive):
            continue
        # Historical key: this counts candidate ideals, before unit-ideal rejection.
        counts["nonprincipal"] += 1
        q = 2*S.Poly(candidate[bad[0]].as_expr(), s).nth(2)
        basis = S.groebner(speeds, a, b, c)
        if basis.reduce(S.Integer(1))[1] == 0:
            continue
        remainder = basis.reduce(q)[1]
        counts["membership"] += 1
        ideal_key = tuple(map(str, basis.polys))
        proper_ideals.add(ideal_key)
        primitive_basis = basis if not gcd.free_symbols else S.groebner(primitive, a, b, c)
        if primitive_basis.reduce(S.Integer(1))[1] != 0:
            counts["proper_nonprincipal_membership"] += 1
            nonprincipal_ideals.add(ideal_key)
        if len(samples) < 3:
            samples.append(dict(seed=label, speeds=list(map(str, speeds)), q=str(q)))
        if remainder != 0:
            counterexample = dict(seed=label, history=newhistory, frame=key,
                                  speeds=list(map(str, speeds)), q=str(q), remainder=str(remainder))
            break
    counts["distinct_proper_ideals"] = len(proper_ideals)
    counts["distinct_nonprincipal_ideals"] = len(nonprincipal_ideals)
    return {
        "config": config, "counts": counts,
        "wall_seconds": round(time.monotonic() - start, 6),
        "stopping_reason": "counterexample" if counterexample else
            ("attempt_limit" if counts["attempts"] == attempts else "wall_limit"),
        "counterexample": counterexample, "sample_proper_checks": samples,
        "python_search_is_unittest": False, "new_unittest_methods": 0,
        "scope": "Finite exact candidate search, not exhaustive and not a universal membership proof.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("batch", choices=("initial", "broader"))
    parser.add_argument("--replay-attempts", type=int)
    args = parser.parse_args()
    record = run(args.batch, args.replay_attempts)
    record["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    record["sympy_version"] = S.__version__
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
