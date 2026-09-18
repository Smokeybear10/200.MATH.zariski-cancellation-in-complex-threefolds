"""Bounded exact exploration of actual four-slot elementary commutators.

Three inverse-verified seeds are used: the successful nonprimitive132 frame,
a quadratic translation frame, and the retained77 nilpotent frame followed by
a quadratic bad shear. None is claimed to be a new or primitive example.
Unlike search131, no original slot is held fixed. Quadratic monomials may use
two distinct slots, and intermediate degree-profile loss is permitted.

Each completed word is checked in BOTH inverse orders before deduplication or
profile filtering. All coefficients and correction systems are over QQ. A
finite negative result is not an absence theorem. No solver/checker internals
are imported, no files are written, and no package installation is performed.
"""

import argparse
import itertools
import json
import signal
import time

import sympy as sp


a, b, v, u = sp.symbols("a b v u")
X, Y, Z, W = sp.symbols("X Y Z W")
g0, g1, g2 = sp.symbols("g0 g1 g2")
BASE, ORIGINAL, GOOD = (a, b, v, u), (X, Y, Z, W), (g0, g1, g2)
SLOTS = ("X", "Y", "Z", "W")


class TimeBound(Exception):
    pass


class TermBound(Exception):
    pass


def polynomial(value):
    return sp.Poly(value, *BASE, domain=sp.QQ)


def coefficient_matrix(expressions):
    polys = [sp.Poly(value, a, b, v, domain=sp.QQ) for value in expressions]
    monomials = sorted(set().union(*(set(poly.monoms()) for poly in polys)))
    return sp.Matrix([[poly.coeff_monomial(monomial) for poly in polys]
                      for monomial in monomials])


def solve_span(columns, target):
    matrix = coefficient_matrix(columns+[target])
    try:
        solution, parameters = matrix[:, :-1].gauss_jordan_solve(matrix[:, -1])
    except ValueError:
        return None
    if parameters.rows:
        solution = solution.subs({entry: 0 for entry in parameters})
    return list(solution)


def seeds():
    half = sp.Rational(1, 2)
    first = [u, v+a*u, a+b*(v+a*u), b+half*u**2]
    first_b = W-half*X**2
    first_a = Z-first_b*Y
    second = [u, a, b, v+half*u**2]
    h = b-a**2
    old_x, old_y, old_z = a+u*h, b+u*(v+2*a*h), v-u*h**2
    third = [old_x, old_y, old_z, u+half*old_x**2]
    third_u = W-half*X**2
    third_h = Y-X**2-third_u*Z
    third_a = X-third_u*third_h
    entries = [
        ("nonprimitive132", first, [first_a, first_b, Y-first_a*X, X]),
        ("quadratic_translation", second, [Y, Z, W-half*X**2, X]),
        ("retained77_quadratic_bad_shear", third,
         [third_a, third_h+third_a**2, Z+third_u*third_h**2, third_u]),
    ]
    result = []
    for name, frame, inverse in entries:
        forward_sub, inverse_sub = dict(zip(ORIGINAL, frame)), dict(zip(BASE, inverse))
        if any(sp.expand(value.subs(forward_sub, simultaneous=True)-expected) != 0
               for value, expected in zip(inverse, BASE)):
            raise AssertionError((name, "seed inverse after forward"))
        if any(sp.expand(value.subs(inverse_sub, simultaneous=True)-expected) != 0
               for value, expected in zip(frame, ORIGINAL)):
            raise AssertionError((name, "seed forward after inverse"))
        result.append({"name": name, "frame": [polynomial(value) for value in frame],
                       "inverse": [str(value) for value in inverse]})
    return result


def negate(step):
    target, powers, coefficient = step
    return target, powers, -coefficient


def describe(step):
    target, powers, coefficient = step
    return {"target": SLOTS[target], "source_exponents_XYZW": list(powers),
            "coefficient": coefficient}


def apply_word(start, word, term_cap):
    current = list(start)
    for target, powers, coefficient in word:
        # Conservative pre-expansion cap. It can reject a word whose terms
        # would later cancel, so every such rejection is reported as a cutoff.
        bound = 1
        for value, exponent in zip(current, powers):
            if exponent:
                bound *= len(value.terms())**exponent
        if bound+len(current[target].terms()) > term_cap:
            raise TermBound()
        increment = polynomial(1)
        for value, exponent in zip(current, powers):
            if exponent:
                increment *= value**exponent
        current[target] += coefficient*increment
        if sum(len(value.terms()) for value in current) > term_cap:
            raise TermBound()
    return current


def probe(frame):
    degrees = [value.degree(u) for value in frame]
    if sorted(degrees) != [1, 1, 1, 2]:
        return "profile_rejected", None
    bad_slot = degrees.index(2)
    good = [value.as_expr() for index, value in enumerate(frame) if index != bad_slot]
    bad = frame[bad_slot].as_expr()
    speeds = [sp.diff(value, u) for value in good]
    gradient = sp.Matrix(speeds).jacobian((a, b, v))
    if sp.expand(gradient.det()) != 0:
        raise AssertionError("An actual three-good frame unexpectedly had speed rank three")
    if not any(sp.expand(gradient.extract(rows, cols).det()) != 0
               for rows in itertools.combinations(range(3), 2)
               for cols in itertools.combinations(range(3), 2)):
        return "rank_rejected", None
    cone = sp.Matrix.hstack(sp.Matrix(speeds), gradient)
    if not any(sp.expand(cone[:, list(cols)].det()) != 0
               for cols in itertools.combinations(range(4), 3)):
        return "density_rejected", None
    quadratic_forms = [GOOD[i]*GOOD[j] for i in range(3) for j in range(i, 3)]
    cubic_forms = [g0**i*g1**j*g2**(3-i-j)
                   for i in range(4) for j in range(4-i)]
    speed_sub, actual_sub = dict(zip(GOOD, speeds)), dict(zip(GOOD, good))
    evaluate = lambda forms: [sp.expand(form.subs(speed_sub, simultaneous=True)) for form in forms]
    quadratics, cubics = evaluate(quadratic_forms), evaluate(cubic_forms)
    q = sp.diff(bad, u, 2)
    if solve_span(quadratics, q) is not None:
        # Density makes evaluation injective on homogeneous polynomials.
        # Here every relation must have F3=L*G2, hence cannot be primitive.
        return "quadratic_span_rejected", None
    relations = coefficient_matrix([sp.expand(q*speed) for speed in speeds]
                                   + [-2*value for value in cubics]).nullspace()
    if not relations:
        # The written dichotomy133 now forces a primitive cubic relation here.
        # Such an endpoint would challenge that proof or this implementation,
        # not be an ordinary rejected sample or a cancellation counterexample.
        raise AssertionError("Actual dense nonquadratic endpoint contradicts leading dichotomy133")
    # Two independent leading relations would force a homogeneous relation
    # of degree four or make q quadratic. Both were excluded above.
    if len(relations) != 1 or not any(relations[0][i] for i in range(3)):
        raise AssertionError("Unexpected leading-relation dimension under dense primitive filtering")
    relation = relations[0]
    relation /= next(relation[i] for i in range(3) if relation[i] != 0)
    L = sp.expand(sum(relation[i]*GOOD[i] for i in range(3)))
    F3 = sp.expand(sum(relation[3+i]*form for i, form in enumerate(cubic_forms)))
    if sp.total_degree(sp.gcd(L, F3)) != 0:
        raise AssertionError("Nonprimitive relation survived exact nonquadratic/density filtering")
    H = sp.expand(L.subs(actual_sub, simultaneous=True)*bad
                  - F3.subs(actual_sub, simultaneous=True))
    if sp.expand(sp.diff(H, u, 3)) != 0:
        raise AssertionError("Leading relation did not cancel the third derivative")
    sigma = sp.diff(H, u, 2)
    data = {"good_slots": [SLOTS[i] for i in range(4) if i != bad_slot],
            "bad_slot": SLOTS[bad_slot], "good": list(map(str, good)), "bad": str(bad),
            "speeds": list(map(str, speeds)), "q": str(q), "L": str(L), "F3": str(F3),
            "leading_speed": str(sp.expand(L.subs(speed_sub, simultaneous=True))),
            "sigma": str(sigma)}
    first = solve_span([q]+quadratics, sigma)
    if first is None:
        return "FIRST_GATE_FAILURE", data
    rho = -first[0]
    G2 = sp.expand(sum(first[i+1]*form/2 for i, form in enumerate(quadratic_forms)))
    corrected = sp.expand(H+rho*bad-G2.subs(actual_sub, simultaneous=True))
    nu = sp.diff(corrected, u)
    if sp.expand(sp.diff(nu, u)) != 0:
        raise AssertionError("First correction did not lower the actual E-degree")
    data.update(rho=str(rho), G2=str(G2), nu=str(nu))
    second = solve_span(speeds, nu)
    if second is None:
        return "SECOND_GATE_FAILURE", data
    G1 = sp.expand(sum(value*form for value, form in zip(second, GOOD)))
    invariant = sp.expand(corrected-G1.subs(actual_sub, simultaneous=True))
    if sp.diff(invariant, u) != 0:
        raise AssertionError("Second correction did not yield an invariant")
    data.update(G1=str(G1), invariant=str(invariant))
    return "both_gates_pass", data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=25.0)
    parser.add_argument("--max-words", type=int, default=1296)
    parser.add_argument("--term-cap", type=int, default=1800)
    options = parser.parse_args()
    if not 0 < options.seconds <= 30 or options.max_words < 1 or options.term_cap < 1:
        parser.error("Require 0 < seconds <= 30 and positive word/term bounds")
    started = time.monotonic()
    counts, per_seed, seen, findings, samples = {}, {}, set(), [], []
    attempted = verified = changed_X = 0
    current_active = False
    stop, current_seed, family, seed_data = "exhausted_family", None, [], []

    def count(status):
        nonlocal current_active
        counts[status] = counts.get(status, 0)+1
        local = per_seed.setdefault(current_seed, {})
        local[status] = local.get(status, 0)+1
        current_active = False

    def timeout_handler(signum, stack):
        raise TimeBound()

    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, options.seconds)
    try:
        seed_data = seeds()
        quadratic, linear = [], []
        for target in range(4):
            others = [i for i in range(4) if i != target]
            for sources in itertools.combinations_with_replacement(others, 2):
                powers = tuple(sources.count(i) for i in range(4))
                quadratic.append((target, powers, 1))
            for source in others:
                linear.append((target, tuple(int(i == source) for i in range(4)), 1))
        family = [(first, (second[0], second[1], sign), seed)
                  for first, second, sign, seed in itertools.product(
                      quadratic, linear, (1, -1), seed_data) if first[0] != second[0]]
        assert len(family) == 1296
        for first, second, seed in family:
            if attempted >= options.max_words:
                stop = "word_limit"
                break
            attempted += 1
            current_seed = seed["name"]
            current_active = True
            word = [first, second, negate(first), negate(second)]
            if first[0] == 0 or second[0] == 0:
                changed_X += 1
            inverse_word = [negate(step) for step in reversed(word)]
            try:
                endpoint = apply_word(seed["frame"], word, options.term_cap)
            except TermBound:
                count("forward_sparse_cutoff")
                continue
            try:
                restored = apply_word(endpoint, inverse_word, options.term_cap)
                inverse_first = apply_word(seed["frame"], inverse_word, options.term_cap)
                restored_reverse = apply_word(inverse_first, word, options.term_cap)
            except TermBound:
                count("inverse_sparse_cutoff")
                continue
            if restored != seed["frame"] or restored_reverse != seed["frame"]:
                raise AssertionError("A logged elementary inverse word failed")
            verified += 1
            key = tuple(tuple(value.terms()) for value in endpoint)
            if key in seen:
                count("duplicate")
                continue
            seen.add(key)
            status, data = probe(endpoint)
            count(status)
            if data is not None:
                data.update(seed=current_seed, word_index=attempted,
                            forward_steps=[describe(step) for step in word],
                            inverse_steps=[describe(step) for step in inverse_word],
                            seed_inverse_after_inverse_word=seed["inverse"])
                if status.endswith("FAILURE"):
                    findings.append(data)
                    stop = "candidate_found_requires_independent_review"
                    break
                if len(samples) < 3:
                    samples.append(data)
    except TimeBound:
        stop = "time_limit"
        if current_active:
            count("interrupted_word")
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old_handler)
    print(json.dumps({
        "scope": "Finite exact exploration, not an absence theorem or actual-frame entry theorem",
        "family": "All four-slot quadratic/linear commutators with distinct targets; 3 actual seeds",
        "configured_seconds": options.seconds, "term_cap": options.term_cap,
        "max_words": options.max_words, "full_deterministic_family_words": len(family),
        "seed_inverse_orders_verified": [seed["name"] for seed in seed_data],
        "attempted_words": attempted, "attempted_words_changing_X": changed_X,
        "inverse_verified_words_both_orders": verified, "unique_final_tuples": len(seen),
        "counts": counts, "per_seed_counts": per_seed, "stop_reason": stop,
        "elapsed_seconds": time.monotonic()-started, "findings": findings,
        "successful_samples_at_most_three": samples,
        "cutoff_scope": "Term bounds include conservative pre-expansion estimates and inverse paths",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
