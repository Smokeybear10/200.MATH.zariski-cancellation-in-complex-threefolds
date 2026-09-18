# Rank-one speed controls, pass82

This is a finite-control and provenance note, not a proof certificate. The
standalone [checker](rank_one_speed_checks_pass82.py) has four `unittest`
methods and imports only `unittest` and SymPy. It does not import the solver,
research proof scripts, or earlier checkers. All computations are exact.

The written results being controlled are the
[divisorial ideal theorem](rank-one-acceleration-divisorial-ideal-pass82.md),
the [whole quotient description](rank-one-speed-quotient-pass82.md), and the
[ambient nilpotence bound](rank-one-ambient-nilpotence-bound-pass82.md).
The author independently read each complete saved proof through EOF. This
does not claim a fresh read of any external source paper.

## 1. Actual proper nonprincipal speed ideal

Starting in the genuine polynomial coordinates `(s,a,b,c)` with `E = d/ds`,
put `X = b + a^2 s`, `Y = c + b^2 s`, and take the new coordinates
`(A,X,Y,Z) = (a,X,Y,s+XY)`. The inverse uses
`sigma = Z-XY`, `B0 = X-A^2 sigma` and is
`(s,a,b,c) = (sigma,A,B0,Y-B0^2 sigma)`.

The method checks both inverse orders, the transported derivation, the
supplied slice, all first accelerations and their next iterates. The velocity
and acceleration in this actual frame are

```text
E(A,X,Y,Z)  = (0,A^2,B0^2,1+A^2 Y+B0^2 X),
E^2(A,X,Y,Z) = (0,0,0,2 A^2 B0^2).
```

Both Groebner containments give the exact ideal equality
`(A^2,B0^2) = (A^2,X^2)` in the actual four-variable ring. This ideal is
proper. Its generators have gcd one, so it is not principal. The tests
also check stability under the original partial `d/dZ`, that the bad speed
is one modulo the ideal, and that the primitive good divergence
`2 A^2 X B0` is the negative bad-speed derivative and belongs to the ideal.
This actual nonprincipal example has `q` in the ideal. It proves no
universal membership assertion.

## 2. Retained principal boundary

With `Delta = a^2 + sb`, the second actual map is
`(Y,B,C,Z) = (a+b Delta,b,c,s-2a Delta-b Delta^2)`. Its inverse uses
`Delta = Y^2+ZB` and is
`(s,a,b,c) = (Z+2Y Delta-B Delta^2,Y-B Delta,B,C)`.

Both inverse orders and the transported derivation are checked. Here the
good gcd is `g = B^2`, the bad speed is `1-2BY`, and `q = -2B^3`.
The method checks `Eg = (d/dZ)g = 0`, the exact quotient identity for
`q/g`, and `q in (g)` but `q not in (g^2)`. This is the retained principal
Nagata mechanism, not a new family or a nonprincipal counterexample.

## 3. Whole nonreduced quotient controls

For each `N = 2,...,6`, all reductions are modulo `epsilon^N`. The map
`z = s + epsilon s^2/2` has its finite Catalan inverse checked in both
orders. For `D = b(z) d/dz`, where `b(z) = 1+epsilon s(z)`, the method
checks an explicit inverse of the unit `b`, `D(s(z))=1`, `D^2z=epsilon`
and `D^3z=0`. It also checks that the relative divergence is nonzero and
that the nilpotence order of the acceleration is exactly `N`.

These are genuine quotient-ring derivations, conjugate to `d/ds` in that
quotient. They are not polynomial-coordinate actions on ambient `C^4`.
For `N >= 5`, the nonzero fourth power explicitly violates the separate
ambient `q^4 in I` theorem, so those controls cannot be its full speed
quotients. No actual ambient lift is asserted for `N = 2,3,4` either.
In particular, the tests do not remove the relative two-variable and
zero-divergence hypotheses of any external theorem.

## 4. Formal full ambient determinant control

The fourth method keeps a generic three-by-three block, the whole lower
row, and the last diagonal entry `1+td`. It checks the exact four-by-four
determinant factorization and each coefficient of
`(1+td)(1+e1 t+e2 t^2+e3 t^3)`. Substituting
`(e1,e2,e3)=(-d,d^2,-d^3)` leaves `1-d^4 t^4`.

A separate formal companion table retains an arbitrary lower row. Its
characteristic polynomial is `lambda^4-d^4` and its fourth power is
`d^4` times the identity, hence zero modulo `d^4`. This verifies finite
algebra used in the written argument. It is not an integrable velocity
Jacobian, a realized action, or a sharpness example for the exponent.

## 5. Runs, search separation and limits

The first author run of the final four-method checker passed in **0.277
seconds**, exit zero, tool output chunk `6fa0a4`. The complete checker
was then read through EOF. Its SHA256 is

```text
4e05c14b45bc1a8bbcba46fdb7df50fed205672858525ad4d63ad9a5aee19a5c
```

The [print-only targeted runner](run_targeted_pass82.py) executes exactly
this one suite with four expected methods, retains its full stdout and
hash, and checks that its recorded inputs have not changed during the run.
Root owns the separate canonical capture. This note does not report that
capture before it occurs. Repeated executions and the five quotient
subtests are not additional methods.

The [bounded search record](rank-one-speed-search-scope-pass82.md) is
separate. Its initial and single broader batches found no counterexample.
They contribute **zero unittest methods** and are not executed by the
targeted runner. Their search counters, duplicates and between-attempt
time cutoff are documented in that record, not merged into this count.

No new full regression is claimed here. The last preserved full run is
pass75, with 146 suites and 1047 methods. These finite checks neither
prove arbitrary acceleration-ideal membership nor resolve general
cancellation. They do not alter the central registry or any frozen file.
