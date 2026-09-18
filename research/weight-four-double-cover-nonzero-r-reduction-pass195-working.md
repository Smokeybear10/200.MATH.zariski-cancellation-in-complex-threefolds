# Algebraic leading ratios exclude the pure-quartic branch

Status: bounded working proof. In the actual nonzero-R chart with
q independent of rho, the pure-quartic alternative forces q to be a
rational function of t. Consequently the two repeated-root double-cover
initial forms below leave only the two square-completion alternatives
when R is nonzero. Neither alternative is recognized or excluded here.
This does not prove cancellation or arbitrary coordinate entry.

## 1. Actual hypotheses and the two applications

Retain the supplied actual globally sliced setup and exact coefficient
chart of [universal184](weight-four-universal-chart-potentials-pass184-working.md).
Thus
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
a_E=EX\in L^*,\quad t=EY/a_E,\quad
q=(E^2Z/2)/a_E^2,\quad \rho=(E^2W/2)/a_E^2,\\
[L:\mathbb C(t,\rho)]<\infty,\quad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty,\quad
\ker_K\partial_t=\mathbb C,\\
Y=y+tX,\quad Z=z+(q'y+k)X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\quad \mathbb C(y,z,w)=L(v),\quad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a_E^3 .
\end{gathered}
\tag{1}
\]
Here \(q\in K\), the two ratios \(t,\rho\) are independent, primes
differentiate \(t\), and coefficient partials commute. The determinant
holds for all \(X\). Its nonzero coefficient is not an original-ring
unit assertion.

The applications have entire weighted initial kernel respectively
\[
(F_1)=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad
(F_2)=(\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)).
\tag{2}
\]
Their leading ratios satisfy \(q^2=t\) and \(q^2=t(1-t)\).
In both cases \(q\notin\mathbb C(t)\). For example the valuation at
\(t=0\) of either right side is odd, whereas a rational square has
even valuation. Also \(q'''\ne0\); otherwise successive integration
using the exact constants of \(K\) would make \(q\) quadratic over
\(\mathbb C\).

## 2. The rationality lemma for a pure-quartic actual branch

For this section \(q\) may be any element of the finite field \(K\).
Assume that the actual branch has
\[
\begin{gathered}
R=k_\rho=r=(\alpha t+\beta)^{-1},\quad
\alpha,\beta\in\mathbb C,\quad(\alpha,\beta)\ne(0,0),\\
k=r\rho+k_0,\quad n=c r^2\rho+n_0,\quad
c\in\mathbb C,\quad k_0,n_0\in K,\\
y=\Gamma v+\eta,\quad \Gamma\in L^*,\quad\eta\in L,\qquad
\mathcal H=\omega(V-P_4(U)),\quad
\omega\in L^*,\quad \deg P_4=4 .
\end{gathered}
\tag{3}
\]
The eliminant and potentials are the literal universal-chart ones.
These assumptions are precisely the pure-quartic coefficient gates,
not assumptions imposed on a square-completion branch.

Write \(\chi=\alpha t+\beta\), \(Q=q''/2\), \(d=q'''/6\), and
\[
\begin{gathered}
D=\chi d'/4+\alpha d,\quad
F_3=\chi k_0'''/6+\alpha k_0''/2-cd,\quad
F_2=\chi n_0''/2+\alpha n_0'-c k_0''/2,\\
F(U)=DU^4+F_3U^3+F_2U^2,\qquad
p(U)=(-\chi d-\alpha Q)U^3
 +(cQ-\chi k_0''/2-\alpha k_0')U^2\\
\hspace{35mm} +(ck_0'-\chi n_0'-\alpha n_0)U .
\end{gathered}
\tag{4}
\]
Then \(p_t=-F_U\). The coefficient of \(U^4\) in \(\mathcal H\)
is \(r^2D\), so (3) gives \(D\ne0\).

For clarity, the general-q elimination in
[pure-quartic193](weight-four-split-pure-quartic-coordinate-recognition-pass193-working.md),
Section 2, has no dependence on its later specialization
\(q=-t^3-t^{-1}\). It gives
\[
h=\chi\ell+c^2r^2\rho+cn_0,\quad
w=(\alpha y-c)z+p(y)+h,\quad
h_\rho=-\omega/r^2\ne0 .
\tag{5}
\]
Use the exact coefficient partials fixing \(h\):
\[
\partial_h=h_\rho^{-1}\partial_\rho,\qquad
\partial_t^h=\partial_t^{\rm old}
   -(h_t^{\rm old}/h_\rho)\partial_\rho .
\tag{6}
\]
They commute, and \(\ker_L\partial_h=K\). From now on \(t\)-partials
in \(L\) mean \(\partial_t^h\); primes in \(K\) are unchanged.
No equality \(L=K(h)\) is needed.

The same literal elimination gives
\[
z=r\rho_hF(y)+Qy^2+(r\rho+k_0)_t y+z_0,\qquad
\bigl(\partial_t^h+F_U(y)\partial_h\bigr)z
  =-\frac{a_E^3\rho_h}{\Gamma}\in L^* ,
\tag{7}
\]
where \(z_0\in L\). The right side is independent of \(y\), but
may depend on \(h\). The factor \(\Gamma\) has not been dropped.

The coefficient of \(y^7\) in (7) is \(4rD^2\rho_{hh}\).
Thus
\(\rho=\lambda h+\kappa\), with \(\lambda,\kappa\in K\) and
\(\lambda\ne0\). Put \(T=r\lambda\ne0\) and
\(u_0=(r\kappa+k_0)'\). Equation (7) becomes
\[
z=TF(y)+Qy^2+(T'h+u_0)y+z_0 .
\tag{8}
\]
Comparing the coefficients of \(y^4,y^3,y\), in that order, gives
\[
\begin{gathered}
5DT'+D'T=0,\\
(z_0)_h=b=-(TF_3'+4T'F_3)/(4D)\in K,\qquad
z_0=bh+g_0,\quad g_0\in K,\\
T''h+u_0'+2F_2b=0 .
\end{gathered}
\tag{9}
\]
Since \(h\) is transcendental over \(K\), \(T''=0\).
The constants of \(K\) give \(T=A t+B\), with \(A,B\in\mathbb C\)
not both zero. The first equation of (9) now implies
\[
(DT^5)'=0,\qquad DT^5=C_0\in\mathbb C^*,\qquad
D\in\mathbb C(t)^* .
\tag{10}
\]

We finish with a differential-field argument valid for every algebraic
\(q\), not just the two quadratic extensions in (2).
Let
\(\overline q=\operatorname{Tr}_{K/\mathbb C(t)}(q)/[K:\mathbb C(t)]\)
and \(\widetilde q=q-\overline q\).
Trace commutes with the derivative: in a finite normal closure it is a
sum over embeddings, each of which commutes with the uniquely extended
derivation in characteristic zero. Therefore (4) and (10) imply
\[
\chi\,\widetilde q''''+4\alpha\,\widetilde q'''=0 .
\tag{11}
\]
If \(\alpha=0\), then \(\beta\ne0\), so \(\widetilde q''''=0\).
Successive primitive subtractions give
\(\widetilde q\in\mathbb C[t]\) of degree at most three.

If \(\alpha\ne0\), equation (11) is
\((\chi^4\widetilde q''')'=0\).
Hence \(\widetilde q'''=c_0\chi^{-4}\), \(c_0\in\mathbb C\).
Since
\[
\left(-\frac{c_0}{6\alpha^3\chi}\right)'''=c_0\chi^{-4},
\tag{12}
\]
successive primitive subtractions give
\(\widetilde q=-c_0/(6\alpha^3\chi)+P_2(t)\), with
\(P_2\in\mathbb C[t]\) of degree at most two.
Thus in either case \(\widetilde q\in\mathbb C(t)\), and consequently
\(q=\overline q+\widetilde q\in\mathbb C(t)\).

This proves the pure-quartic rationality lemma. Notice that it used the
actual scalar determinant, not just the polynomial eliminant equations.
It did not use an ansatz restricting \(q\) to rational functions.

## 3. Constant projection and the quartic top in the applications

Now impose one of (2) and assume \(R=k_\rho\ne0\).
The actual constant-projection derivation argument in
[three-alternative193](weight-four-split-nonzero-r-three-alternatives-pass193-working.md),
Section 2, applies with the following stronger multiplier obstruction:
\[
l(t)\in\mathbb C[t]\setminus\{0\}
\quad\Longrightarrow\quad l(t)q\notin\mathbb C(t).
\tag{13}
\]
Indeed the opposite assertion would give \(q\in\mathbb C(t)\).

Here are the statement-level substitutions in that argument.
If \(y\in L\), the actual primitive commuting LND \(D_0\) fixing \(X,Y\)
has \(D_0Z=B_0(X,Y)\ne0\) and
\(D_0W=2cB_0Z+C_0(X,Y)\), where \(\deg B_0\le1\).
The leading coefficient of \(E^2(D_0W)=0\), if \(c\ne0\), would
make a nonzero affine multiplier of \(q\) a polynomial.
Equation (13) excludes it. Thus \(c=0\), \(C_0\) is affine or zero,
and the actual contracted kernel is
\(\mathbb C[X,Y,F_0]\), \(F_0=B_0W-C_0Z\).
The contraction follows by the explicit slice inverse or least
denominator argument in193, with no change involving \(q\).

Wang's two-coordinate theorem now supplies either an invariant
nonzero linear combination of \(X,Y\), contrary to nonconstant \(t\),
or an invariant \(c_1F_0+H(X,Y)\), \(c_1\in\mathbb C^*\).
If \(B_0\) is nonconstant, its leading coefficient multiplies the
independent ratio \(\rho\), preventing cancellation.
If \(B_0\) is constant and \(C_0\) nonconstant, (13) prevents the
required polynomial cancellation of its affine multiplier of \(q\).
If both are constant, the nonzero \(B_0\rho\) term prevents cancellation.
This exhausts the affine pair and proves \(y\notin L\).
The same two published inputs are used as in193:
[Dasgupta--Gupta, Lemma 2.3(i) and Theorem 4.1](https://arxiv.org/pdf/1701.03635v1).
Their hypotheses concern actual irreducible LNDs, not arbitrary
coefficient derivations.

The general-q [rigidity188](weight-four-absent-variable-nonzero-r-rigidity-pass188-working.md)
therefore gives \(R_\rho=0\), the entire plane ring
\(L[y,\vartheta]=L[v]\), and a unit evaluated cofactor.
With \(d=q'''/6\), put
\[
C_4=Rd'/4-R'd,\qquad \Delta=RR''/2-(R')^2 .
\tag{14}
\]
If \(C_4=0\), the general differentiation identity is
\[
\Delta=\frac{R^2}{32}
  \frac{4dd''-5(d')^2}{d^2},\qquad
\frac{4dd''-5(d')^2}{d^2}=
\begin{cases}
15/(4t^2),&q^2=t,\\
5(4t-3)(4t-1)/(4t^2(t-1)^2(2t-1)^2),&q^2=t(1-t).
\end{cases}
\tag{15}
\]
Both are nonzero elements of \(\mathbb C(t)\); vanishing at individual
values of \(t\) is not vanishing as a coefficient-field element.
The eliminant would then have cubic top
\(U^2(C_3U+\Delta V)\) with two distinct linear factors.
The one-point-at-infinity and unit-cofactor degree argument of193,
Section 3, excludes degree three, two, and one selected components
in turn, the last because it would make \(y\) constant. Thus \(C_4\ne0\).

The resulting quartic degree/cofactor classification is exactly
\[
\begin{array}{ll}
\text{pure quartic:}&\mathcal H=\omega(V-P_4(U)),\\
\text{quadratic graph:}&
\mathcal H=\omega(V-P_2(U))+A_2(V-P_2(U))^2,\\
\text{quadratic projection:}&
\mathcal H=A_2((V-P_2(U))^2-a_2U-b_2).
\end{array}
\tag{16}
\]
Here the subscripts on \(P_i\) give exact degree, and the necessary
nonzero coefficients are as in193. The argument uses only the
quartic top, entire affine-line ring, and unit evaluated cofactor.
The pure-quartic coefficient comparison gives exactly (3), so
Section 2 excludes it because \(q\notin\mathbb C(t)\).

## 4. Exact remaining question

Under either full initial kernel in (2), every actual nonzero-R
configuration must therefore be one of the two square-completion
alternatives in (16). After completing the square they have
\(\mathcal H=A_2(V-P_2)^2+B_1U+B_0\), with \(B_1=0\) in the
quadratic-graph case and \(B_1\ne0\) in the quadratic-projection case.

The first and second differential gates from193--194 must not be
imported with the split value \(d=t^{-4}-1\).
For \(q^2=t\), preliminary exact calculations give simultaneous
solutions \(f=t^{1/2}\) and \(f=t^{-1/2}\) to those general-d gates.
Their actual-chart realization is a separate question. This note
uses neither their existence nor their sufficiency.

The zero-R branches, the two remaining square alternatives, original
coordinate return, and arbitrary entry are outside this proof.
No external contact, public claim, human expert review, Lean
certification, or historical novelty clearance has occurred.

