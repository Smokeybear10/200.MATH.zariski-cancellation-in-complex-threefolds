"""Bounded exploratory exact search, not a unittest or universal certificate.

Apply logged four-step elementary commutators over QQ[u] to the actual129
frame. Each elementary step changes one slot using another slot only, so its
inverse is the negative step and the inverse word is explicit. Filter final
degrees (1,1,2), rank-two good speeds and a primitive mixed-cubic relation;
then solve both correction gates by exact coefficient linear algebra.
Every completed word is checked in both inverse-composition orders before
deduplication. These identities do not enlarge the finite search family.

The wall limit is checked between words. A sparse-term cutoff is reported,
not interpreted as an exclusion theorem. No earlier checker is imported.
"""

import argparse
import itertools
import json
import time

import sympy as sp


a, b, v, u = sp.symbols("a b v u")
g0, g1, g2 = sp.symbols("g0 g1 g2")
BASE = (a, b, v, u)
GOOD = (g0, g1, g2)
SLOTS = ("Y", "Z", "W")


def coefficient_matrix(expressions):
    polynomials = [sp.Poly(value, a, b, v, domain=sp.QQ) for value in expressions]
    monomials = sorted(set().union(*(set(poly.monoms()) for poly in polynomials)))
    return sp.Matrix([[poly.coeff_monomial(monomial) for poly in polynomials]
                      for monomial in monomials])


def span_coefficients(columns, target):
    matrix = coefficient_matrix(columns+[target])
    try:
        solution, parameters = matrix[:, :-1].gauss_jordan_solve(matrix[:, -1])
    except ValueError:
        return None
    if parameters.rows:
        solution = solution.subs({parameter: 0 for parameter in parameters})
    return list(solution)


def step_log(step):
    target, source, power, u_power, sign = step
    return {"target": SLOTS[target], "source": SLOTS[source], "power": power,
            "u_power": u_power, "sign": sign}


def gate_probe(polynomials):
    degrees = [poly.degree(u) for poly in polynomials]
    if sorted(degrees) != [1, 1, 2]:
        return "profile_rejected", None
    bad_index = degrees.index(2)
    good = [u]+[poly.as_expr() for i, poly in enumerate(polynomials) if i != bad_index]
    bad = polynomials[bad_index].as_expr()
    speeds = [sp.diff(value, u) for value in good]
    if any(sp.diff(value, u) != 0 for value in speeds):
        raise AssertionError("Degree-one filter did not yield invariant speeds")
    f, h = speeds[1:]
    gradient = sp.Matrix([f, h]).jacobian((a, b, v))
    if all(sp.expand(gradient.extract([0, 1], list(pair)).det()) == 0
           for pair in itertools.combinations(range(3), 2)):
        return "rank_rejected", None
    quadratic_forms = [GOOD[i]*GOOD[j] for i in range(3) for j in range(i, 3)]
    speed_sub = dict(zip(GOOD, speeds))
    quadratic_values = [sp.expand(form.subs(speed_sub, simultaneous=True))
                        for form in quadratic_forms]
    q = sp.diff(bad, u, 2)
    if span_coefficients(quadratic_values, q) is not None:
        return "quadratic_span_rejected", None
    cubic_forms = [g0**i*g1**j*g2**(3-i-j)
                   for i in range(4) for j in range(4-i)]
    cubic_values = [sp.expand(form.subs(speed_sub, simultaneous=True))
                    for form in cubic_forms]
    relations = coefficient_matrix([sp.expand(q*value) for value in speeds]
                                   + [-2*value for value in cubic_values]).nullspace()
    relation = next((column for column in relations if any(column[i] != 0 for i in range(3))), None)
    if relation is None:
        return "no_cubic_relation", None
    relation /= next(relation[i] for i in range(3) if relation[i] != 0)
    L = sp.expand(sum(relation[i]*GOOD[i] for i in range(3)))
    F3 = sp.expand(sum(relation[3+i]*form for i, form in enumerate(cubic_forms)))
    if sp.total_degree(sp.gcd(L, F3)) != 0:
        raise AssertionError("Nonquadratic q unexpectedly yielded a nonprimitive relation")
    actual_sub = dict(zip(GOOD, good))
    H = sp.expand(L.subs(actual_sub, simultaneous=True)*bad
                  - F3.subs(actual_sub, simultaneous=True))
    if sp.diff(H, u, 3) != 0:
        raise AssertionError("Mixed relation failed its exact third-derivative identity")
    sigma = sp.diff(H, u, 2)
    correction = span_coefficients([q]+quadratic_values, sigma)
    data = {"good": [str(value) for value in good], "bad": str(bad),
            "speeds": [str(value) for value in speeds], "q": str(q),
            "L": str(L), "F3": str(F3), "sigma": str(sigma)}
    if correction is None:
        return "FIRST_GATE_FAILURE", data
    rho = -correction[0]
    G2 = sp.expand(sum(correction[1+i]*form/2 for i, form in enumerate(quadratic_forms)))
    K = sp.expand(H+rho*bad-G2.subs(actual_sub, simultaneous=True))
    nu = sp.diff(K, u)
    if sp.diff(nu, u) != 0:
        raise AssertionError("Solved first correction did not kill the second derivative")
    second = span_coefficients(speeds, nu)
    if second is None:
        data.update({"rho": str(rho), "G2": str(G2), "nu": str(nu)})
        return "SECOND_GATE_FAILURE", data
    return "both_gates_pass", None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=20.0)
    parser.add_argument("--max-words", type=int, default=192)
    parser.add_argument("--term-cap", type=int, default=4000)
    options = parser.parse_args()
    started = time.monotonic()
    seed = [sp.Poly(value, *BASE, domain=sp.QQ) for value in
            (v+a*u, a-v**3/2+b*u,
             b+3*a*v**2/2+3*a**2*v*u/2+a**3*u**2/2)]
    u_poly = sp.Poly(u, *BASE, domain=sp.QQ)
    quadratic_steps = [(target, source, 2, exponent, 1)
                       for target in range(3) for source in range(3) if target != source
                       for exponent in (0, 1)]
    linear_steps = [(target, source, 1, exponent, 1)
                    for target in range(3) for source in range(3) if target != source
                    for exponent in (0, 1)]
    counts, seen, findings = {}, set(), []
    attempted = 0
    inverse_verified_words = 0
    stopped = "exhausted_family"
    for first, second, sign in itertools.product(quadratic_steps, linear_steps, (1, -1)):
        if first[0] == second[0]:
            continue
        if attempted >= options.max_words or time.monotonic()-started >= options.seconds:
            stopped = "bounded_limit"
            break
        attempted += 1
        second = second[:-1]+(sign,)
        word = [first, second, first[:-1]+(-first[-1],), second[:-1]+(-second[-1],)]
        current = list(seed)
        cutoff = False
        for target, source, power, exponent, coefficient in word:
            current[target] += coefficient*u_poly**exponent*current[source]**power
            if sum(len(poly.terms()) for poly in current) > options.term_cap:
                cutoff = True
                break
        if cutoff:
            counts["sparse_cutoff"] = counts.get("sparse_cutoff", 0)+1
            continue
        restored = list(current)
        for target, source, power, exponent, coefficient in reversed(word):
            restored[target] -= coefficient*u_poly**exponent*restored[source]**power
        if restored != seed:
            raise AssertionError("Inverse after forward word did not restore the seed")
        inverse_first = list(seed)
        for target, source, power, exponent, coefficient in reversed(word):
            inverse_first[target] -= coefficient*u_poly**exponent*inverse_first[source]**power
        for target, source, power, exponent, coefficient in word:
            inverse_first[target] += coefficient*u_poly**exponent*inverse_first[source]**power
        if inverse_first != seed:
            raise AssertionError("Forward after inverse word did not restore the seed")
        inverse_verified_words += 1
        key = tuple(tuple(poly.terms()) for poly in current)
        if key in seen:
            counts["duplicate"] = counts.get("duplicate", 0)+1
            continue
        seen.add(key)
        status, finding = gate_probe(current)
        counts[status] = counts.get(status, 0)+1
        if finding is not None:
            finding["status"] = status
            finding["forward_steps"] = [step_log(step) for step in word]
            finding["inverse_steps"] = [step_log(step[:-1]+(-step[-1],)) for step in reversed(word)]
            finding["inverse_completion"] = "After inverse steps: a=Z-uW+Y^3/2; v=Y-au; b=W-Delta(a,v,u)."
            findings.append(finding)
            stopped = "candidate_found_requires_independent_review"
            break
    print(json.dumps({"scope": "Exact rational elementary-word exploration, not an absence theorem",
                      "attempted_words": attempted, "unique_final_tuples": len(seen),
                      "inverse_verified_words_both_orders": inverse_verified_words,
                      "counts": counts, "stop_reason": stopped,
                      "elapsed_seconds": time.monotonic()-started,
                      "findings": findings}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
