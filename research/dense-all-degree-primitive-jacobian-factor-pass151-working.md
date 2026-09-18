# The all-degree primitive Jacobian factor has a slice off the speed determinant

The global factorization91 does not need constant acceleration.
In every actual dense three-good frame, the selected leading
derivation is the speed determinant times the original polynomial
Jacobian derivation of two intrinsic base coordinates and the slice.
That Jacobian factor is globally primitive and locally nilpotent.
Off the speed determinant, the coefficient derivations preserve the
actual localized base ring. The canonical Taylor peeling and its
second negative coefficient then give local polynomial slices, which
patch to a slice over that whole open base.

This extends the retained constant-acceleration scope and proves
divisor residue triviality off the determinant. No triviality on
its zero divisor, general cancellation, or novelty is asserted.
The primitive plinth and selected content remain distinct objects;
the former's prime support is now contained in the latter's.

## 1. Actual setting and fixed orientation

Retain the actual dense hypotheses139 and the additional intrinsic
quotient theorem used147:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
E^2X=E^2Y=E^2Z=0,\\
a=(EX,EY,EZ)^t\in A^3,\qquad
\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)=2,\\
H(a_1,a_2,a_3)\ne0\quad
\text{for every nonzero homogeneous }H\in\mathbb C[T_1,T_2,T_3],\\
T=\partial_W,\qquad N=[u^2]T|_A\ne0,\qquad
S=\ker_A N=\mathbb C[P,Q],\qquad L=\operatorname{Frac}S.
\end{gathered}
\tag{1}
\]
The retained cofactor and leading-LND arguments give
\(N\in\operatorname{LND}(A)\) and \(N(a_i)=0\), with no bound
on \(\deg_EW\). Extend \(N\) to \(B=A[u]\) by \(Nu=0\).
The actual affine-plane quotient supplies the chosen polynomial
coordinates \(P,Q\) of \(S\). These are explicit inherited
dependencies, not consequences of the field calculation below.[^1]

Use the original volume order \((X,Y,Z,W)\). Define
\[
\Omega=\det[a,a_P,a_Q]\in S,\qquad
\mathcal D(f)=
\det\frac{\partial(P,Q,u,f)}{\partial(X,Y,Z,W)}
\quad(f\in B).
\tag{2}
\]
In particular \(\mathcal D\) is a polynomial derivation of the
original ring \(B\) and kills \(P,Q,u\).
The coefficient derivatives \(a_P,a_Q\) are computed in the
polynomial base ring \(S\), not in a changed ambient coordinate
system.

## 2. The volume and cofactor give the exact factor

Choose an intrinsic rational slice \(v\in\operatorname{Frac}A\)
with \(Nv=1\). The local-slice theorem gives
\(F:=\operatorname{Frac}A=L(v)\). In this field write
\[
dX\wedge dY\wedge dZ\wedge dW
=J\,dP\wedge dQ\wedge du\wedge dv,
\qquad J\in F(u)^*.
\tag{3}
\]
Both sides are nonzero absolute complex differential four-forms.
The original volume is invariant under \(E\): the polynomial
automorphism \(\exp(\lambda E)\) has Jacobian a unit in
\(\mathbb C[\lambda]\), hence a constant, and its value at
\(\lambda=0\) is 1. The coefficient forms \(dP,dQ,dv\)
are fixed by \(E\), as is \(du\). It follows that \(EJ=0\),
so \(J\in F^*\).

Write \((X,Y,Z)^t=c+ua\) with \(c\in A^3\).
In the column order \((P,Q,u,v)\), Cramer's rule for the actual
partial \(T\) gives
\[
T(v)=\frac{\det[c_P+ua_P,\ c_Q+ua_Q,\ a]}{J},\qquad
[u^2]T(v)=\frac{\det[a_P,a_Q,a]}{J}
=\frac{\Omega}{J}=Nv=1.
\tag{4}
\]
The cofactor sign is positive: the deleted row and column are both
the fourth. The cyclic permutation of three determinant columns
is also positive. The degree-two coefficient on \(F\) is the
extension of \(N\), by the quotient rule and the actual degree
bound139. Thus \(J=\Omega\ne0\).

Equation (3) also gives \(\mathcal Dv=1/J\). Since both
\(N\) and \(\Omega\mathcal D\) kill \(P,Q,u\) and take
value 1 on \(v\), they agree on the rational function field
\(\mathbb C(P,Q,u,v)\), and hence on \(B\):
\[
\boxed{\ N=\Omega\mathcal D\text{ on }B,\qquad
\mathcal D\in\operatorname{LND}(B),\qquad
[E,\mathcal D]=0,\qquad
\ker_A\mathcal D=S.\ }
\tag{5}
\]
Here the extension of \(N\) kills \(u\). The LND assertion is
global: \(\mathcal D\Omega=0\), so
\(N^j f=\Omega^j\mathcal D^j f\); since \(N\) is locally
nilpotent and \(B\) is a domain, \(\mathcal D\) is locally
nilpotent on all of \(B\), without inverting \(\Omega\).
Also \([E,N]=0\) and \(E\Omega=0\), so the commutator
in (5) vanishes. The kernel assertion follows from the same
factorization on \(A\).

## 3. The polynomial Jacobian factor is primitive

The conormal proof91 applies unchanged; it is reproduced here to
make the all-degree scope explicit.[^2] Let \(g\) be the gcd
in the UFD \(B\) of the nonzero coefficient entries of
\(\mathcal D\), and write \(\mathcal D=gD_0\), with the
coefficient gcd of \(D_0\) equal to 1.
Since \(\mathcal Dg\in gB\), LND self-divisibility gives
\(\mathcal Dg=0\). The identity \([E,\mathcal D]=0\) gives
\(E(g)D_0+g[E,D_0]=0\). Taking valuations at each irreducible
factor of \(g\), and using the coefficient gcd of \(D_0\),
gives \(g\mid E(g)\). Self-divisibility for \(E\) then gives
\(Eg=0\). Consequently \(g\in S\).

Suppose a prime \(p\in S\) divides \(g\). Factorial closure
makes \(p\) prime in \(A\) and \(B\). Choose \(\ell=P\)
or \(Q\) so that
\[
dp\wedge d\ell=\epsilon\,dP\wedge dQ,\qquad
\epsilon\in S\setminus(p).
\tag{6}
\]
At least one base partial of the irreducible \(p\) is nonzero
modulo \(p\) in characteristic zero, giving such a choice.
The residue of \(\ell\) is transcendental over \(\mathbb C\)
in \(\operatorname{Frac}(S/(p))\). Otherwise it is constant,
so \(p\) is a multiple of \(\ell-\alpha\), incompatible
with (6).

Put \(K_p=\operatorname{Frac}(B/pB)\).
The injection \(S/(p)\hookrightarrow A/pA\), together with
\(B/pB=(A/pA)[u]\), makes the residues of \(\ell,u\)
algebraically independent. Their differentials in
\(\Omega_{K_p/\mathbb C}\) are independent.
In the ambient conormal sequence at this generic point, the
kernel is \(K_p\,dp\), and \(dp\ne0\): an irreducible
nonconstant polynomial in characteristic zero cannot divide
all its own original partial derivatives.
Thus \(dp,d\ell,du\) are independent before the conormal
quotient. By (6), \(dP,dQ,du\) are independent there as well.
This contradicts divisibility by \(p\) of every three-by-three
minor defining \(\mathcal D\).

Therefore \(g\in\mathbb C^*\). The restriction to \(A\)
is primitive too: any prime dividing all values on \(A\)
would divide all values on \(A[u]\), since \(\mathcal Du=0\).
It follows that \(\Omega\), up to a complex unit, is exactly
the global invariant content of \(N\), not just one known
factor of that content.

## 4. Local content is the speed-ratio Jacobian order

At an arbitrary prime \(p\in S\), choose a good speed
\(s=a_i\notin(p)\), using the all-degree gcd theorem134.
Permuting the goods only changes determinant orientation by a
constant sign. Write the reordered row as \((s,t,b)\), and
put \(\tau=t/s,\rho=b/s\). Then
\[
\Omega=\pm s^3
\det\frac{\partial(\tau,\rho)}{\partial(P,Q)},\qquad
c_p:=\min_{f\in A,\,Nf\ne0}\operatorname{ord}_{pA}(Nf)
=\operatorname{ord}_p\Omega
=\operatorname{ord}_p
\det\frac{\partial(\tau,\rho)}{\partial(P,Q)}.
\tag{7}
\]
The determinant formula follows by removing the derivatives of
\(s\) from the second and third columns of
\(\det[a,a_P,a_Q]\). Primitivity of \(\mathcal D|_A\)
proves the content equality. The final equality uses that \(s\)
is a unit in \(S_{(p)}\).

Thus the content removed in147 is precisely the vanishing order
of the speed-ratio Jacobian. This is a differential critical
divisor for the generically finite speed-ratio map. It is not
the different finite cover given by the full divisor residue
constants, and no assertion that the speed-ratio map is finite
on the whole selected chart is needed.

## 5. The Taylor coefficients are regular off the speed determinant

Fix one selected speed \(s\), put \(\tau=t/s,\rho=b/s\), and
write
\[
R=S[(\Omega s)^{-1}],\qquad A_R=A\otimes_S R,\qquad
\partial_\tau(R)\subset R,\qquad \partial_\rho(R)\subset R.
\tag{8}
\]
The last assertions follow from (7), not from a claim that an
arbitrary finite coefficient-field extension is unramified.
Indeed \(\tau,\rho\in R\), their ordinary \(P,Q\) derivatives
belong to \(R\), and their two-by-two Jacobian determinant is
a unit. Inverting that matrix gives the values of
\(\partial_\tau,\partial_\rho\) on \(P,Q\) in \(R\).
The reciprocal rule then proves preservation of the localization.
These are exactly the coefficient derivations on \(L\) used139,
by uniqueness of extension through its finite separable extension
of \(\mathbb C(\tau,\rho)\).

The actual fixed-\(X\) chart139 gives
\(A_R=R[y,z,w_0]\), \(Y=y+\tau X\), \(Z=z+\rho X\),
and \(W=\sum_{j=0}^m w_jX^j\), with \(w_j\in A_R\).
Its selected leading derivation is
\(N'=N/s^2\in\operatorname{LND}(A_R)\), with kernel \(R\).
The intersection \(A_R\cap L=R\) follows either from this
kernel assertion or directly by clearing invariant denominators
and applying \(N\).

For a coefficient \(f\in L\), use the homogeneous Taylor notation
\[
H_d(f;U,V)=\sum_{i+j=d}
\frac{\partial_\tau^i\partial_\rho^j f}{i!j!}U^iV^j,
\qquad
w_j=f_j+\sum_{k=j+1}^m H_{k-j}(f_k;y,z).
\tag{9}
\]
The exact chart139 supplies \(f_j\in L\) and the second identity.
Descending induction proves \(f_m,\ldots,f_0\in R\).
For the first step \(f_m=w_m\in A_R\cap L=R\).
If the higher coefficients lie in \(R\), (8) puts all their
Taylor polynomials in \(R[U,V]\). The difference defining
\(f_j\) in (9) belongs to \(A_R\), and also belongs to
\(L\); thus it lies in \(R\).

The first two exact negative-tail identities139 are
\[
\begin{gathered}
f_{-1}=-\sum_{j=0}^m H_{j+1}(f_j;y,z)\in L,\\
f_{-1}\in A_R\cap L=R,\qquad
\Psi(U,V)=-\sum_{j=0}^m H_{j+2}(f_j;U,V)
-H_1(f_{-1};U,V)\in R[U,V],\\
N'\bigl(\Psi(y,z)\bigr)=1,\qquad
A_R=R[\Psi(y,z)],\qquad
\mathcal D\left(\frac{\Omega}{s^2}\Psi(y,z)\right)=1.
\end{gathered}
\tag{10}
\]
The sign of the correction is negative: the first tail is
corrected by subtracting the full term
\(X^{-1}\Theta(f_{-1})\). Its new \(X^{-2}\) coefficient
is \(\Psi(y,z)\); applying the degree-two top of \(T\)
gives value 1. These are the exact tail identities, not an
assertion that the uncorrected second coefficient is a slice.[^5]
Regularity follows from (8)--(9), including that of \(f_{-1}\).
The slice theorem for \(N'\) gives the ring equality in (10).
Finally \(N'=(\Omega/s^2)\mathcal D\), and the scaling factor
is an invariant unit, proving the last identity.
There is also an \(N\)-slice \(\Psi(y,z)/s^2\) on this same
chart. Thus the off-determinant polynomial recognition mechanism
does not depend on the separate primitivity proof in Section 3.

This proof includes \(m=0\), since the chart and negative-tail
identities include that case. It uses no primitivity or plane-
coordinate assertion for the first-tail polynomial, and in
particular does not require the later factor theorem145.
The localized original \(T\) is not declared locally nilpotent.

## 6. The local slices patch over the whole determinant open set

Let \(S_\Omega=S[\Omega^{-1}]\) and \(A_\Omega=A[\Omega^{-1}]\).
Expansion of the determinant \(\Omega\) in its first column
gives \(\Omega\in(a_1,a_2,a_3)S\). Thus
\((a_1,a_2,a_3)S_\Omega=S_\Omega\), and the three selected-speed
charts cover \(\operatorname{Spec}S_\Omega\).
Apply (10) in each chart, permitting the harmless orientation sign
in (7). Use the \(N\)-slices \(r_i=\Psi_i/a_i^2\)
in \(A_\Omega[a_i^{-1}]\), with the same intrinsic \(N\)
in every selected chart.

Choose positive integers \(n_i\) so that
\(b_i=a_i^{n_i}r_i\in A_\Omega\). Their derivatives are
\(N b_i=a_i^{n_i}\).
The powers \(a_i^{n_i}\) still generate the unit ideal in
\(S_\Omega\), since the radical of their ideal is the unit
ideal. Choose \(c_i\in S_\Omega\) with
\(\sum_i c_i a_i^{n_i}=1\). Then
\[
\begin{gathered}
r_N=\sum_i c_i b_i\in A_\Omega,\qquad Nr_N=1,\qquad
A_\Omega=S_\Omega[r_N],\\
r=\Omega r_N,\qquad \mathcal D r=1,\qquad
\boxed{\ A_\Omega=S_\Omega[r].\ }
\end{gathered}
\tag{11}
\]
This patches actual slices using invariant coefficients. It does
not merely patch nonvanishing vector fields, nor require a
cohomological triviality assertion. If a local slice already has
no speed denominator, the same construction or that slice alone
applies. The first line of (11) needs only the actual chart139,
the corrected negative-tail identity, and the derivative stability
(8); it does not use the primitive factor theorem. The second
line uses \(N=\Omega\mathcal D\) and the invariant unit
\(\Omega\) to recover the primitive-action statement.

In particular \(\mathcal D\) is fixed-point-free on
\(A_\Omega\), and for every prime \(p\nmid\Omega\) the full
fiber is \(k_p[\bar r]\), so \(\ell_p=k_p\). By the retained
principal-plinth support theorem27, every prime factor of the
primitive plinth lies in \(V(\Omega)\). Equivalently, clearing
the denominator of \(r\) in (11) gives \(b\in A\) and an
integer \(n\ge0\) with \(\mathcal D b=\Omega^n\).
If \(\Omega\) is a complex unit, (11) is a global polynomial
recognition \(A=S[r]\simeq\mathbb C^{[3]}\).
No assertion that \(\Omega\) must be a unit is made.

## 7. The determinant-zero divisor remains open

At every prime \(p\in S\), the restriction of
\(\mathcal D\) to the full generic divisor fiber is nonzero.
By147 that fiber is \(\ell_p[\xi]\), and this derivation is
a nonzero constant multiple of \(\partial_\xi\).
It has no fixed points on that full fiber, regardless of whether
\(\ell_p\) equals the base residue field. The generic fiber
has the same property. As in91, any fixed locus of
\(\mathcal D|_A\) therefore lies over finitely many closed
points of \(\operatorname{Spec}S\). Equation (11) now places
those points inside \(V(\Omega)\), but does not exclude them.

The constant-acceleration argument90 proves freeness on
\(A_\Omega\) using an actual two-generator relative presentation,
a quadratic potential, and a conormal determinant. The all-degree
slice conclusion (11) uses a different additional step: preservation
of the localized coefficient ring by both Taylor partials, followed
by the corrected second-tail identity. It does not simply promote
the field equality \(L[y,z]=L[v]\) to a ring equality.[^3]

Even fixed-point-freeness on an invariant localization is weaker
than existence of a slice there, and does not alone force the
full divisor constants to be trivial. The localized ordinary
Weitzenbock control discussed90 is smooth and has a free action
while retaining a quadratic divisor constant extension. It is
not an actual dense selected frame.[^3]

The primitive plinth of \(\mathcal D|_A\), rather than the
content \(\Omega\), detects nontrivial \(\ell_p/k_p\) by
the retained principal-plinth support theorem27. The support
containment just proved does not identify their multiplicities
or make either divisor disappear. The remaining selected-divisor
problem is now concentrated on \(\Omega=0\); arbitrary coordinate
entry remains a separate gap150.[^4] The [companion finite checks](off_omega_tail_slice_controls_pass151.py)
illustrate exact formulas; the arbitrary-ring conclusions are
the written arguments above. No novelty claim or unrestricted
cancellation conclusion is made.

## Sources

1. [Dense chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--3, including the inherited all-degree cofactor132
   and leading-LND125 inputs; [global residue bound147](dense-all-degree-divisor-residue-bound-pass147-working.md),
   Sections 1--3, for the separate intrinsic quotient, UFD,
   generic fiber, and every-divisor speed selection dependencies.
2. [Global primitive Jacobian factor91](nonconical-global-jacobian-field-pass91.md),
   Sections 1--4. Its volume orientation, global transfer,
   conormal primitivity proof, and finite base support of fixed
   points were fully reread. The constant-acceleration hypothesis
   is not used in the proofs reproduced here.
3. [Open free field90](nonconical-open-free-derivation-pass90.md),
   Sections 1--5. Its extra actual quadratic presentation,
   unit-value-ideal calculation, and the distinction between
   freeness, a slice, and residue constants were fully reread.
4. [Primitive plinth and boundary fields27](intrinsic-plinth-boundary-pass27.md),
   Sections 2--4; [selected-divisor and entry gaps150](selected-divisor-and-entry-gaps-pass150-working.md),
   Sections 2--5. Their open sufficient residue-field assertion
   remains unproved on the determinant-zero divisor.
5. [Exact negative-tail relations139](dense-negative-tail-relations-pass139-working.md),
   Sections 1--3, especially equations (5)--(7). The corrected
   second coefficient has intrinsic derivative 1. The displayed
   proof was fully reread before applying the new regularity
   argument (8)--(10).

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
[^4]: Source 4.
[^5]: Source 5.
