# Finite return-map and failed-lift controls

The standalone [checker](rank_one_return_checks_pass83.py) has three
`unittest` methods, using only `unittest` and SymPy. It imports no
solver, proof script or previous checker. These finite calculations
do not prove an arbitrary action theorem or certify a cited source.

The mathematical inputs are the actual
[return-map and integral-closure proof](rank-one-return-map-integral-closure-pass83.md)
and the [cubic socle characterization](rank-one-cubic-acceleration-socle-pass83.md).
The checker author independently reconstructed both complete saved
notes through EOF, including the revised monic Taylor equation and
third-Veronese paragraph in the return proof. Their universal claims
remain written proofs, separate from these finite examples.

## 1. A genuine two-speed action and its rational return

Start with actual coordinates `(s,a,b,c)` and `E = d/ds`. Put

```text
X = b + as,  Y = c + bs,  (A,X,Y,Z) = (a,X,Y,s+XY).
sigma = Z-XY,  B0 = X-A sigma.
(s,a,b,c) = (sigma,A,B0,Y-B0 sigma).
```

The method checks both polynomial inverse orders, the transported
derivation, the original slice and every coordinate acceleration.
The only nonzero acceleration is `2 A B0` in the fourth coordinate,
and its next derivative vanishes. This is an actual sliced LND in
the required rank-one quadratic frame, built by elementary polynomial
coordinate changes. It is a retained two-speed construction, not a
new family or a cancellation counterexample.

On the actual hyperplane `Z=0`, with `r=1+AY`, the data are
`f=(0,A,Xr)`, `b0=r(1+X^2)` and `q0=2AXr`. The full speed ideal
there is `(A,Xr)=(A,X)`, since `Xr-X=AXY`. The rational return fixes
`A`, sends `X` to `-1/X`, and sends `r` to `-X^2 r`. The test checks
its twofold composition, the invariant speed and acceleration,
the sign reversal of `b0`, and return of the last coordinate to zero.

The total spatial degree of `b0` is four. Simultaneous substitution
in `b0(u+t f(u))` freezes `f` at the original point. Its Taylor
coefficients give the exact monic equation in the written proof,
with a nonzero third frozen derivative. Each kth coefficient is
checked in `(A,X)^k` by exact Groebner reduction. This is not the
iterated variable-coefficient derivation `sum f_i d/du_i`.

The return has a pole at `X=0`, even though this actual example has
`q0` in its speed ideal. Thus the regular-return sufficient criterion
is not a necessary condition for membership.

## 2. A polynomial jet that is not an actual action

Root supplied the following three-polynomial jet, with nonzero
parameter `e` and arbitrary parameter `h`:

```text
f = (y,z,e^3 x^4/4 + e xz + h y^2 - e^2 x^2 y),
q0 = -ex,  b0 = 1.
```

Exact computations take place over the rational function field
`Q(e,h)`, so `e` is invertible. The speed ideal is exactly
`(y,z,x^4)`. The matrix used in the tests is the actual derivative
matrix of this polynomial triple, not a freely prescribed matrix.
The method checks the quotient flow-determinant coefficients,
the full four-by-four characteristic polynomial and fourth power
modulo the ideal, the signed cubic Jacobian identity, and the
nonzero socle class annihilated by `x,y,z`.

These conditions do not supply a sliced action. For the attempted
four-coordinate map

```text
(x+sy, y+sz, z+s f3, s-ex s^2/2),
```

the method computes the full Jacobian determinant, not only its
quotient. The coefficients of its determinant minus one are zero
in degrees zero and one, followed by

```text
s^2:  y(e-4h)/2,
s^3: -e(3exy-4hxy-z)/2,
s^4: -e(7e^3x^4-16e^2x^2y+8exz+4hy^2)/8.
```

There are no higher coefficients. Making the second coefficient
zero by `h=e/4` leaves a nonzero `z` coefficient `e/2` in the third.
Thus this attempted map is not a polynomial automorphism for any
nonzero `e`. Independently, its constant nonzero `b0` cannot satisfy
the actual return sign identity when `q0` is nonzero. The latter is
a written obstruction from the actual flow, not a fabricated action
on this jet. No ambient sharpness example is obtained.

## 3. Integrality versus ideal membership

In `Q[x,y,z]`, take `J=(x^2,y^2)` and `q=xy`. The method checks
that `q` has nonzero remainder modulo `J` but satisfies the monic
equation `tau^2-x^2 y^2=0` at `tau=q`, whose constant coefficient
lies in `J^2`. This elementary example distinguishes ideal
integrality from membership; no action realizes these data here.

The same method checks one weighted monomial valuation for the
preceding failed jet: `v(x)=1`, `v(y)=v(z)=4`, and the coefficient
field has value zero. It gives `v((f))=4` but `v(q0)=1`. The ordinary
necessary valuation inequality for any monic ideal-integrality
equation therefore excludes integrality for that jet. The tests
compute only these finite weights, not the general valuative
criterion or a classification of all jets.

## 4. Source and execution provenance

The checker author's new source reads for the two proof audits were
the complete displayed Stacks 00H3 and 090P proofs, the full
characteristic-zero field statement of Hickel's Theorem 1.1 on
printed page 2, and the visually read Lipman--Sathaye printed
page 199, including Theorem 1 and its deduction from Theorem 1-prime.
This does not claim a complete Hickel proof read, the Stacks
valuation-existence dependency, or the later core proofs in
Lipman--Sathaye. Those source gates are not verified by this suite.

The first run passed **three methods in 0.154 seconds**, exit zero,
with complete tool output chunk `c71160`. The entire saved checker
was then read through EOF. Its SHA256 is

```text
1ef8779766686d8c324ca8074aa47814e5d04e62af2e2f1cf344af0297fb0639
```

The subsequent [print-only targeted runner](run_targeted_pass83.py)
executes only this one suite with three expected methods and preserves
the full output and its hash. The checker author did not execute that
runner or create a canonical capture, new search or full regression.
Root owns later integration and canonical capture. Repeated runs do
not add methods. All pass82
and earlier artifacts remain unchanged. The controls assert no
unrestricted coordinate reduction, new recognized family, historical
novelty or general cancellation result.
