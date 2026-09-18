# Nonzero distinct-root residues leave only a projected line

This is a bounded actual-chart reduction for a supplied full rank-one
quartic kernel. For \(Z^2-XYW+aX^4+bY^4\), the universal eliminant has an
explicit nonzero sextic with completely split leading part over the
exact coefficient field. If \((a,b)\ne(0,0)\), every leading line has
multiplicity at most two. The actual cofactor identity then excludes all
projected conics in the nonzero-return branch. It leaves a coefficient-field
line, not an ambient invariant coordinate or a realizability assertion.

## 1. Actual hypotheses and the literal pivot

Let \(a,b\in\mathbb C\) be fixed residue parameters. They are not the
leading speeds of the original coordinates. Assume an actual globally
sliced polynomial four-ring and its entire initial kernel:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a_0=EX,\quad b_0=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(a_0T,b_0T,e_0T^2,h_0T^2)\bigr)
 =(\mathsf Z^2-\mathsf X\mathsf Y\mathsf W
                    +a\mathsf X^4+b\mathsf Y^4).
\end{gathered}                                                    \tag{1}
\]
The coordinates are actual polynomial generators and \(T\) is independent.
No minimality assumption on the frame is made.

The literal \(Z\) pivot of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
gives
\[
\begin{gathered}
N=[u^3]\partial_Z|_A\ne0,\quad L=\operatorname{Frac}(\ker_A N),
\quad A_L=L[v],\quad Nv=1,\\
t=b_0/a_0,\quad \rho=h_0/a_0^2,\quad q=e_0/a_0^2,\quad
q^2=t\rho-a-bt^4,\quad [L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2,\\
y,z,w,\sigma,\theta\in L[v],\quad L[y,z,w]=L[v],\quad
J_0=-a_0^3\in L^* .
\end{gathered}                                                    \tag{2}
\]
Here \(t,\rho\) are algebraically independent. The two partials extend
uniquely and commute on the finite separable field \(L\), and fix \(v\).
In particular \(q,t,\rho\ne0\) as field elements. The algebraic relation
for \(q\) does not assume \(L\) rational or choose an analytic branch.

For \(c\in L\), write
\[
H_j(c;U,V)=\sum_{i=0}^j
\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{3}
\]
Formal \(U,V\) are fixed by coefficient derivatives. Retain all lower
potentials \(k,n,\ell,m\in L\), and set
\[
\begin{gathered}
f=H_2(q)+H_1(k)+n,\quad \mathcal R=f_V,\quad c=f_\rho,\\
S=H_3(q)+H_2(k)+H_1(n),\quad T_0=\ell-S,\\
Q=H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\mathcal H=\frac{q_{\rho\rho}}2T_0^2+
                    \mathcal R cT_0+\mathcal R^2Q .
\end{gathered}                                                    \tag{4}
\]
The universal actual identities are
\[
z=q_\rho w+f(y,\theta),\quad
Rw=T_0(y,\theta),\quad
\frac{q_{\rho\rho}}2w^2+c(y,\theta)w+Q(y,\theta)=0,\quad
R=\mathcal R(y,\theta).
\tag{5}
\]
Thus \(\mathcal H(y,\theta)=0\). Lower potentials are not discarded.
The degree of \(\mathcal H\) is at most six.

## 2. Exact leading sextic from the quadratic-field Taylor expansion

The coefficient derivatives satisfy
\[
q_t=\frac{\rho-4bt^3}{2q},\quad q_\rho=\frac t{2q},\quad
q_{\rho\rho}=-\frac{t^2}{4q^3}\ne0 .
\tag{6}
\]
To calculate all required Taylor terms at once, let
\[
\begin{aligned}
D_1&=(\rho-4bt^3)U+tV,&D_2&=UV-6bt^2U^2,\\
D_3&=-4btU^3,&D_4&=-bU^4 .
\end{aligned}                                                    \tag{7}
\]
Then the exact formal identity for
\(q(t+\varepsilon U,\rho+\varepsilon V)^2\) is
\(q^2+\sum_{j=1}^4D_j\varepsilon^j\).
The formal square root with constant term \(q\) is unique since
\(2q\ne0\). Expanding it gives
\[
\begin{aligned}
H_2(q)&=\frac{D_2}{2q}-\frac{D_1^2}{8q^3},\\
H_3(q)&=\frac{D_3}{2q}-\frac{D_1D_2}{4q^3}
                              +\frac{D_1^3}{16q^5},\\
H_4(q)&=\frac{D_4}{2q}-\frac{2D_1D_3+D_2^2}{8q^3}
                +\frac{3D_1^2D_2}{16q^5}-\frac{5D_1^4}{128q^7},\\
R_1:=\partial_VH_2(q)&=\frac U{2q}-\frac{tD_1}{4q^3},\\
C_2:=(H_2(q))_\rho&=-\frac{tD_2}{4q^3}-\frac{D_1U}{4q^3}
                                      +\frac{3tD_1^2}{16q^5}.
\end{aligned}                                                    \tag{8}
\]
The \(\rho\)-derivative in \(C_2\) differentiates the coefficients
before evaluation. It is not a formal \(V\)-derivative.

Only these terms contribute to total degree six in (4):
\[
\mathcal H_6=-\frac{t^2}{8q^3}H_3(q)^2
                      -R_1C_2H_3(q)+R_1^2H_4(q).
\tag{9}
\]
Substitute \(\rho=(q^2+a+bt^4)/t\) and define the linear form
\[
Z_0=t^2V+(a-3bt^4-q^2)U .
\tag{10}
\]
Straight expansion of (8),(9) yields the short identity
\[
\boxed{\mathcal H_6=-\frac{U^2}{512q^9t^4}
 \left[Z_0^4+8q^2(a+bt^4)U^2Z_0^2
                    +16q^4(a-bt^4)^2U^4\right].}
\tag{11}
\]
For a check of the coefficient simplification, the bracket is a depressed
quartic in \(Z_0\): its coefficients of \(Z_0^3,Z_0\) are zero, and
its remaining coefficients are exactly those displayed. The coefficient
of \(U^2V^4\) in the full sextic is
\(-t^4/(512q^9)\ne0\). Consequently \(\deg\mathcal H=6\) for all
residue parameters, independently of the lower potentials.

Choose square roots \(\alpha^2=a,\beta^2=b\) in \(\mathbb C\). The
bracket factors in the existing field \(L\):
\[
\boxed{\mathcal H_6=
 -\frac{U^2}{512q^9t^4}
 \prod_{\epsilon,\delta\in\{1,-1\}}
 \left[Z_0+2\mathrm i q(\epsilon\alpha+\delta\beta t^2)U\right].}
\tag{12}
\]
Indeed pairing opposite signs gives
\((Z_0^2+4q^2(\alpha+\beta t^2)^2U^2)
 (Z_0^2+4q^2(\alpha-\beta t^2)^2U^2)\), which expands to (11).
No extension of \(L\) is needed to split these lines.

## 3. All parameter degenerations in the coefficient field

Each bracketed line in (12) has \(V\)-coefficient \(t^2\ne0\), so none
is proportional to \(U\). Equality of two such lines requires
\((\epsilon-\epsilon')\alpha+
(\delta-\delta')\beta t^2=0\).
Since \(t\) is transcendental over \(\mathbb C\), this gives exactly
the following multiplicity list:
\[
\begin{array}{c|c|c}
\text{residue parameters}&\text{distinct leading lines}
                                      &\text{multiplicities}\\ \hline
a=b=0&U,\ \rho U-tV&(2,4)\\
a\ne0,\ b=0&U,\ Z_0+2\mathrm i q\alpha U,\
                       Z_0-2\mathrm i q\alpha U&(2,2,2)\\
a=0,\ b\ne0&U,\ Z_0+2\mathrm i q\beta t^2U,\
                       Z_0-2\mathrm i q\beta t^2U&(2,2,2)\\
ab\ne0&U,\ \text{the four lines in (12)}&(2,1,1,1,1).
\end{array}                                                      \tag{13}
\]
In the first row \(q^2=t\rho\) and (11) becomes exactly
\(-U^2(\rho U-tV)^4/(512q^9)\), as in
[pass227](rank-one-product-radical-sextic-pruning-pass227-working.md).
Special values in a numerical fiber, such as \(a=bt^4\), are not
identities in the coefficient field when \(ab\ne0\).

## 4. Actual return and the universal cofactor divisor

From now on assume \(R\ne0\) in \(L[v]\). Put
\(\mathcal C=L[y,\theta]\), \(\mathcal O=L[v]\).
Equation (5), the nonzero coefficient in (6), and the whole-line
equality in (2) give
\[
\mathcal O=\mathcal C[w]=\mathcal C+\mathcal Cw,\qquad
R\mathcal O\subset\mathcal C,\qquad
\operatorname{Frac}\mathcal C=L(v).
\tag{14}
\]
The fourth potential, divided by \(q_{\rho\rho}/2\), reduces every
power of \(w\) to a linear expression. The equality of fraction fields
then follows from \(Rw\in\mathcal C\) and \(R\ne0\). Neither normality
of \(\mathcal C\) nor equality with \(\mathcal O\) is assumed.

Let \(G\) be the irreducible generator of the height-one evaluation
kernel \(L[U,V]\to L[v]\). The general-\(q\) calculation in
[cofactor222](rank-two-saturated-pair-cofactor-exclusion-pass222-working.md),
also rebuilt in pass227, applies literally here. For precision, put
\[
\begin{gathered}
B_1=f_t(y,\theta)+q_{t\rho}w,\quad
C_1=f_\rho(y,\theta)+q_{\rho\rho}w,\\
\Lambda_i=\ell_i-S_i(y,\theta)-\mathcal R_i(y,\theta)w,\quad i=t,\rho,\\
D_U=R(y_v\theta_\rho-y_\rho\theta_v)+C_1y_v,\quad
D_V=R(y_t\theta_v-y_v\theta_t)-B_1y_v .
\end{gathered}                                                    \tag{15}
\]
The derivatives in \(\Lambda_i\) precede evaluation. Formal
differentiation of (4), followed by (5), and the calibrated wedge give
\[
\begin{gathered}
\mathcal H_U(y,\theta)=-R(C_1B_1+R\Lambda_t),\quad
\mathcal H_V(y,\theta)=-R(C_1^2+R\Lambda_\rho),\\
Rw_v=-B_1y_v-C_1\theta_v,\quad
R^3J_0=D_U\mathcal H_U(y,\theta)+D_V\mathcal H_V(y,\theta),\\
\mathcal H=GQ_1,\qquad
0\ne q_1:=Q_1(y,\theta)\mid R^3\quad\text{in }L[v].
\end{gathered}                                                    \tag{16}
\]
In particular \(G\) occurs simply in \(\mathcal H\); otherwise both
evaluated gradients would vanish, contradicting \(R^3J_0\ne0\).
After cancellation of \(q_1\), the last divisibility follows since
\(J_0\) is a unit of \(L\). These identities are valid for arbitrary
universal \(q\), not only the rational rank-two ratios used elsewhere.
The stronger root bounds of pass225 or pass231 are not needed here.

## 5. Pure top over the exact field and exclusion of projected conics

Here is the precise plane-degree input, without a geometric splitting
assumption. Make a linear change of the two generators over \(L\) so
their degrees are \(i<d\), cancelling equal leading degrees if necessary.
If the smaller generator is constant, birationality in (14) forces
\(d=1\). Otherwise write the new generators as \(r(v),p(v)\) with
degrees \(i,d\). The module \(L[v]\) is free of rank \(d\) over \(L[p]\).
The characteristic polynomial of multiplication by \(r\) is its minimal
polynomial, since \(L(p,r)=L(v)\).

Its coefficient of first-variable degree \(d-j\) has second-variable
degree at most \(\lfloor ij/d\rfloor<j\). To see this bound, extend
temporarily to an algebraic closure of \(L\) and put the second variable
equal to \(z^{-d}\). The \(d\) roots of \(p(v)=z^{-d}\) have the form
\(\lambda z^{-1}+O(1)\), with the distinct leading roots supplied by
the leading coefficient of \(p\). They exist by coefficient recursion,
since these leading roots are simple in characteristic zero. Each
value of \(r\) has pole order at most \(i\); its \(j\)-th elementary
symmetric function has pole order at most \(ij\). Because this symmetric
function is a polynomial in the second variable over \(L\), the asserted
integer degree bound follows. The characteristic polynomial therefore
has pure top equal to the first variable to power \(d\).

Returning to the original formal variables proves
\[
g:=\deg G=\max(\deg_vy,\deg_v\theta),\qquad
G_g=c_0\,\lambda(U,V)^g,\quad c_0\in L^*,
\tag{17}
\]
where \(\lambda\) is a linear form over \(L\). This is a coefficient-field
change only. Since \(G\mid\mathcal H\), its line is one of (13) and
\(g\) is at most that line's multiplicity.

Suppose \((a,b)\ne(0,0)\). By (13), \(g\le2\). If \(g=2\), its selected
line has multiplicity exactly two. The degree-four part of \(Q_1\)
is therefore \(\mathcal H_6/(c_0\lambda^2)\), and has no factor
\(\lambda\). Let \((y_2,\theta_2)\ne(0,0)\) be the degree-two leading
vector of the actual parametrization. Equation (17) gives
\(\lambda(y_2,\theta_2)=0\), whereas every other line in (13) is nonzero
on that vector. Consequently
\[
\deg_vq_1=8,\qquad \deg_vR\le2,\qquad
8=\deg_vq_1\le3\deg_vR\le6,
\tag{18}
\]
a contradiction. The degree eight is exact: lower total-degree terms of
\(Q_1\) evaluate to degree at most six and cannot cancel its leading term.
The bound on \(R\) holds because \(\mathcal R=R_1+k_\rho\) is affine
in \(U,V\).

Thus \(g=1\). Equation (17), or direct birationality of a polynomial
parametrization of a line, now gives
\(\max(\deg_vy,\deg_v\theta)=1\) and \(\mathcal C=L[v]\).
This equality is proved only at this endpoint.

There is a useful further precision when \(ab\ne0\). A line in one of
the four simple directions would likewise have evaluated cofactor
degree five, while \(\deg R^3\le3\), contradicting (16). Hence its
selected top must be \(U\). In this case \(G\) is a nonzero scalar
multiple of \(U-y_0\), so \(y\in L\) and \(\theta\) is affine
nonconstant. If exactly one residue is nonzero, the three
multiplicity-two directions of (13) remain possible at this stage.

## 6. Scope and verification boundary

The result is conditional on the complete actual hypotheses (1) and
on \(R\ne0\). It says that every nonzero-residue distinct-root model
has only an affine projected pair in that branch. It neither treats
\(R=0\) nor excludes or recognizes the surviving actual lines. The
case \(a=b=0\) is included in the sextic calculation but is not covered
by the multiplicity-at-most-two argument.

No \(L\)-linear operation in the plane-degree proof is claimed to
preserve an original pivot or to lift to an ambient coordinate change.
No original-ring unit conclusion is drawn from a coefficient in \(L^*\).
The actual universal chart, whole-line equality, and nonzero calibrated
Jacobian are the essential inputs beyond the formal leading relation.

The Taylor coefficients were checked both by expansion of the quadratic
relation and by repeated extended differentiation. The complete sextic
bracket and its four linear factors were independently reconstructed
by fresh unsaved symbolic arithmetic. No saved checker was executed,
imported, or compiled; no earlier source, index, or packet was changed.
This is not a claim about arbitrary initial kernels, unrestricted
cancellation, actual existence, historical novelty, or human review.
