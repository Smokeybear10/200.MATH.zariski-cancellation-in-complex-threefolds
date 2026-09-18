# Dependent quadratic defects: constant reduction and a genuine rational obstruction

For a supplied two-quadratic frame, a constant relation between the two
defects reduces to an already recognized frame. A relation only over
the fraction field need not do so. The distinction persists for a
genuine sliced polynomial action: the natural polynomial syzygy can
have nonzero divergence and therefore fail even to be locally nilpotent.
This does not obstruct a nonlinear coordinate change or cancellation.

## 1. What rank at most one actually gives

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be an LND,
and write \(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Put \(V_i=\operatorname{ad}_E^2T_i\) for \(i=3,4\).
These are commuting LNDs and commute with \(E\), by the actual
conjugated-coordinate argument in
[pass 39, Section 1](two-quadratic-defects-pass39.md).

Suppose their fraction-field rank is one. There is a primitive
polynomial LND \(D\) and polynomials \(a,b\), not both zero, such that
\[
V_3=aD,\qquad V_4=bD,
\qquad a,b\in\ker E\cap\ker D,
\quad [E,D]=0.
\tag{2}
\]
Here primitive means that the coefficients of \(D\) have polynomial
gcd one. It does not mean their ideal is the unit ideal.

To prove (2), choose a nonzero defect and divide its coefficient vector
by its gcd. Every irreducible factor of that gcd is invariant: its
derivative is divisible by the same factor, which for an LND forces
that derivative to vanish. Thus division gives an LND \(D\).
Fraction-field proportionality and primitivity make the other
multiplier polynomial, by comparing valuations at each irreducible.
The same divisibility argument applied to that defect shows that its
multiplier is \(D\)-invariant. Finally
\([E,aD]=0\), primitivity, and valuations imply \(a\mid E(a)\).
Local nilpotence of \(E\) gives \(E(a)=0\), hence \([E,D]=0\).
The other multiplier is also \(E\)-invariant. If the first chosen
defect was zero, interchange the two labels.

The polynomial combination
\[
bT_3-aT_4
\tag{3}
\]
therefore has second iterated \(E\)-adjoint zero. Formula (3) alone
does not say it is a coordinate partial or an LND.

## 2. Exactly when constant recombination works

On the four-dimensional complex space of constant partials, the map
\(T\mapsto\operatorname{ad}_E^2T\) has image
\(\operatorname{span}_{\mathbb C}\{V_3,V_4\}\). Hence its kernel has
dimension
\[
4-\dim_{\mathbb C}\operatorname{span}_{\mathbb C}\{V_3,V_4\}.
\tag{4}
\]
If the defects have a nontrivial constant relation, a constant linear
change of \((x_3,x_4)\) makes one more partial good. The remaining
partial still has third iterated adjoint zero. With a slice for \(E\),
this is the already closed mixed profile \((1,1,1,2)\), and its kernel
is polynomial. If both defects vanish, all four partials are good.
These use the previously proved mixed/whole-frame recognition results,
not a new classification theorem.

Conversely, if \(V_3,V_4\) are complex-linearly independent, (4) is two.
No constant \(\mathrm{GL}_4(\mathbb C)\) change can supply three good
partials. Their fraction-field rank being one does not change (4).

## 3. A sliced full-frame realization of the distinction

Start with independent polynomial coordinates \((u,v,A,C)\) and put
\[
f=u+v,\qquad q=f^2+1,\qquad
E=f\partial_A+q\partial_C.
\tag{5}
\]
Thus \(E\) is an LND fixing \(u,v\). Define
\[
s=C-fA,\qquad r=qA-fC.
\]
Since \(q-f^2=1\), these have the actual inverse
\[
A=r+fs,\qquad C=fr+qs,
\quad E(s)=1,\quad E(r)=0,
\quad\ker E=\mathbb C[u,v,r].
\tag{6}
\]
This is an explicit polynomial cylinder, not an abstract field model.

Use the actual ambient frame
\[
(x_1,x_2,x_3,x_4)=(B_0,D_0,A,C),
\quad B_0=u+A^2/2,\quad D_0=v+C^2/2.
\tag{7}
\]
Its partials, in the original polynomial coordinates, are
\[
T_1=\partial_u,\quad T_2=\partial_v,\quad
T_3=\partial_A-A\partial_u,\quad
T_4=\partial_C-C\partial_v.
\tag{8}
\]
Writing \(H=\partial_A+2f\partial_C\), direct brackets give
\[
[E,T_1]=[E,T_2]=-H,\quad
V_3=2fH,\quad V_4=2qH,
\quad [E,H]=0.
\tag{9}
\]
Every displayed leading field is nonzero, so the exact adjoint profile
is \((1,1,2,2)\). The two defects have fraction-field rank one. They
have no nonzero constant relation: if \(\alpha f+\beta(f^2+1)=0\)
with complex constants, comparison of the quadratic and linear terms
in the independent coordinate \(f\) gives \(\alpha=\beta=0\).
By (4), no constant ambient frame change produces a third good partial.

The action has flow degree two in (7):
\[
E^2x=(f^2,q^2,0,0),\qquad E^3x=0.
\tag{10}
\]
Its highest Jacobian has rank one, consistently with the defect rank
being one. The rank-two hypothesis of the pass-39 companion theorem
does not hold here.

## 4. The natural invariant-coefficient syzygy is not a partial

The polynomial field
\[
Y=qT_3-fT_4
\tag{11}
\]
has \(\operatorname{ad}_E^2Y=0\), because \(f,q\) are
\(E\)-invariant. Its coefficients in the physical frame (7) are
\((0,0,q,-f)\), with gcd one and even unit coefficient ideal.
Nevertheless its divergence in that actual polynomial coordinate
volume is
\[
\operatorname{div}Y
=\partial_A q-\partial_C f
=C-2fA\ne0,
\tag{12}
\]
where the derivatives hold \(B_0,D_0\) fixed, so
\(f=B_0+D_0-(A^2+C^2)/2\).

Every polynomial LND has zero divergence: its polynomial exponential
has polynomial inverse, so the Jacobian is a unit in \(B[t]\), hence
a nonzero constant; at \(t=0\) it is one, and differentiating gives
zero divergence. Thus \(Y\) is not an LND and cannot be a member of
any actual polynomial coordinate-partial frame. Adding only constant
good partials does not fix its divergence.

This excludes the uncorrected invariant-coefficient syzygy as a
coordinate construction. It does not exclude further nonlinear
corrections. Indeed (6) already exhibits successful nonlinear
coordinates for this very action.

## Verification boundary

The new standalone checker is
[dependent_quadratic_defects_checks_pass42.py](dependent_quadratic_defects_checks_pass42.py).
It reconstructs exact inverses, all frame brackets, constant-relation
coefficients, flow rank, and divergence. Finite controls do not replace
the general primitive-division argument or recognition inputs.
Its first run passed all five methods in 0.221 seconds, with no
assertion failure or intervening formula correction.
No general height-ten theorem, novelty, human expert review, or full
cancellation solution is claimed.
