# Lower potentials remove the mixed-conic square-root residual

Status: bounded working necessary conditions for the normalized actual
mixed conic. The complete third and fourth potentials, together with
the retained fourth-degree Jacobian equation, imply
\(G_{hhh}=0\) and \(M(\epsilon-\delta_h)=0\).
The argument never divides by \(M\). Its two branches are distinguished
below; no exclusion of \(M=0\) is assumed or proved in this note.
There is no original-coordinate recognition conclusion.

## 1. Exact inputs and derivative conventions

Assume the normalized actual case-II conic of
[quadratic reduction217](rank-two-mixed-ratio-quadratic-graph-reduction-pass217-working.md),
the [radial-constant calculation218](mixed-conic-radial-constant-leading-ratios-pass218-working.md),
and the [next Jacobian coefficient218](mixed-conic-next-jacobian-constant-pass218-working.md).
The supplied frame and its selected chart satisfy
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(ZW-X^2Y^2),\quad q=t^2/\rho,\quad
R\ne0,\quad [L:\mathbb C(t,\rho)]<\infty,\\
h=t/\rho,\quad \xi=y-h\vartheta,\quad \deg_v\xi=1,\quad
L[y,z,w]=L[v].
\end{gathered}
\tag{1}
\]
Here the four capital-letter generators are actual polynomial
coordinates, the initial kernel is full, and \(u\) is a global slice.
These conditions are retained inputs, not consequences of the algebra
below. The speed \(EX\) need not be an original-ring unit.

For the calculation write \(r=\rho\), \(x=\xi\), and
\[
\mathcal D=h\partial_t+\partial_\rho,\qquad
\partial_h=r\partial_t,\qquad L_0=\ker_L\mathcal D.
\tag{2}
\]
The two derivations commute. A subscript \(r\) in this note means
\(\mathcal D\), which fixes \(h\), whereas a subscript \(h\) fixes \(r\).
The old partial at fixed \(t\) is
\(\partial_\rho=\mathcal D-(h/r)\partial_h\).
Both \(h\) and \(r\) are nonzero elements of the exact field.
No assertion \(L_0=\mathbb C(h)\) or \(L=\mathbb C(h,r)\) is made.

The joint constants of these two derivations are \(\mathbb C\).
Indeed a joint constant is algebraic over \(\mathbb C(h,r)\).
Differentiate its monic minimal polynomial: minimality forces each
coefficient to be constant under both rational partials, hence complex.
Algebraic closedness of \(\mathbb C\) finishes the assertion.
In particular \(\partial_h\) preserves \(L_0\), and its constants there
are precisely \(\mathbb C\).

The two preceding218 notes prove
\[
\begin{gathered}
C\in\mathbb C^*,\quad F,G,\delta\in L_0,\quad
k=C/r+Fr+G,\quad \alpha=r/C,\\
\vartheta=\alpha x^2+bx+c,\qquad
w=dx^2+ex+f,\qquad
d=\alpha\delta,\quad e=b\delta+\epsilon,\\
b=(G_h r+2h\delta r^2)/C,\qquad
M=hF_h-F-2h^2\delta\in L_0,\\
\eta=\epsilon-\delta_h,\qquad
M(2r\mathcal D\eta-\eta)=0.
\end{gathered}
\tag{3}
\]
The coefficients \(c,\epsilon,f,n,\ell,m\) initially lie in \(L\).
No regularity or ambient-coordinate status is assigned to them.
In particular the last equation of (3) alone allows a nonzero
algebraic square-root mode when \(M\ne0\).

## 2. The full raw potentials in the radial variables

All coefficient partials in the universal potentials are taken before
the formal substitution \(U=x+hV\). After that substitution the first
and second potentials are
\[
\sigma=h^2\vartheta+2hx+k,\qquad
z=-h^2w+x^2/r+k_t x+(\mathcal Dk)\vartheta+n.
\tag{4}
\]
The third and fourth potentials from the freshly read
[full mixed-ratio reduction217](rank-two-mixed-ratio-projection-reduction-pass217-working.md)
take the following forms in independent formal \(x,V,W_0\):
\[
\begin{gathered}
\mathcal R=-2hx/r+R_0,\qquad R_0=k_\rho
 =F-hF_h-hG_h/r-C/r^2,\\
\mathcal Rw+S(x,\vartheta)-\ell=0,\qquad
\mathcal K(x,\vartheta,w)=0,\\
S(x,V)=CV^2/r^3-x^2V/r^2-G_hxV/r^2
       +k_{tt}x^2/2+n_rV+n_hx/r,\\
\mathcal K(x,V,W_0)=h^2W_0^2/r+\mathfrak c(x,V)W_0+Q(x,V),\\
\mathfrak c(x,V)=-x^2/r^2+2hxV/r^2
       +k_{t\rho}x+(\mathcal Dk_\rho)V+n_r-hn_h/r .
\end{gathered}
\tag{5}
\]
The symbol \(\mathfrak c\) is a formal fourth-potential coefficient,
not the constant \(c\) of the quadratic graph.
For completeness all terms of \(Q\), including the unused lower ones,
are
\[
\begin{aligned}
Q(x,V)={}&x^2V^2/r^3-CV^3/r^4+G_hxV^2/r^3\\
 &+\left(-F_{hh}/(2r^2)-G_{hh}/r^3\right)x^2V
   +\left(F_{hhh}/r^2+G_{hhh}/r^3\right)x^3/6\\
 &+n_{rr}V^2/2+(n_{rh}/r-n_h/r^2)xV+n_{hh}x^2/(2r^2)\\
 &-\ell_hx/r-\ell_rV-m.
\end{aligned}
\tag{6}
\]
For example the required old and new derivative conversions are
\[
\begin{gathered}
k_t=F_h+G_h/r,\quad k_{tt}=F_{hh}/r+G_{hh}/r^2,\\
k_{t\rho}=-hF_{hh}/r-(G_h+hG_{hh})/r^2,\qquad
\mathcal Dk_\rho=hG_h/r^2+2C/r^3,\\
\mathcal Dk_t=-G_h/r^2,\quad
\mathcal D^2k_t=2G_h/r^3,\quad \mathcal D^3k=-6C/r^4,\\
\mathcal Dk_{tt}=-F_{hh}/r^2-2G_{hh}/r^3,\quad
k_{ttt}=F_{hhh}/r^2+G_{hhh}/r^3 .
\end{gathered}
\tag{7}
\]
Thus (5)--(6) follow either by substituting in the full universal
potentials or by expanding their coefficient Taylor polynomials using
(7). In particular the \(h^2w^2/r\) term has not been discarded.

## 3. Literal coefficient identities before integration

Substitute \(V=\alpha x^2+bx+c\) and \(W_0=dx^2+ex+f\).
The degree-four and degree-three coefficients of the third potential
are identically zero by (3). Its next two coefficients are exactly
\[
\begin{aligned}
0=[x^2](\mathcal Rw+S-\ell)
 ={}&-2he/r+R_0d+Cb^2/r^3+c/r^2\\
 &-G_hb/r^2+k_{tt}/2+\alpha n_r,\\
0=[x](\mathcal Rw+S-\ell)
 ={}&R_0e-2hf/r+(2Cb/r^3-G_h/r^2)c+bn_r+n_h/r.
\end{aligned}
\tag{8}
\]
The constant coefficient is retained as
\(\ell=R_0f+Cc^2/r^3+n_rc\).
It will not be necessary to solve the lower fourth-potential
coefficients in order to obtain the restrictions below.

Here are also the complete fourth-degree and third-degree
coefficients of the fourth potential before any substitution for
\(n,c,f\). This records explicitly every contribution used.
Set
\[
\begin{gathered}
j_3=2h\alpha/r^2,\qquad
j_2=-1/r^2+2hb/r^2+(\mathcal Dk_\rho)\alpha,\\
j_1=2hc/r^2+k_{t\rho}+(\mathcal Dk_\rho)b,\qquad
j_0=(\mathcal Dk_\rho)c+n_r-hn_h/r,\\
L_2=-F_{hh}/(2r^2)-G_{hh}/r^3,\qquad
L_3=F_{hhh}/(6r^2)+G_{hhh}/(6r^3).
\end{gathered}
\tag{9}
\]
Thus \(\mathfrak c(x,\vartheta)=j_3x^3+j_2x^2+j_1x+j_0\).
The coefficients of \(x^6,x^5\) in \(\mathcal K(x,\vartheta,w)\)
vanish identically by (3), without any lower-potential restriction.
The complete next two coefficients are
\[
\begin{aligned}
K_4={}&h^2d^2/r+j_3e+j_2d+(b^2+2\alpha c)/r^3\\
 &-3C(\alpha^2c+\alpha b^2)/r^4
   +2G_h\alpha b/r^3+L_2\alpha+n_{rr}\alpha^2/2,\\
K_3={}&2h^2de/r+j_3f+j_2e+j_1d+2bc/r^3\\
 &-C(b^3+6\alpha bc)/r^4+G_h(b^2+2\alpha c)/r^3\\
 &+L_2b+L_3+n_{rr}\alpha b+(n_{rh}/r-n_h/r^2)\alpha .
\end{aligned}
\tag{10}
\]
Both \(K_4\) and \(K_3\) must be zero. The terms containing
\(\ell,m,n_{hh}\) in (6) have degree at most two after substitution,
so their absence from (10) is justified by degree, not by a
specialization of those functions.

## 4. Exact formulas for the graph constant and \(n\)

The first equation in (8) and \(\alpha=r/C\) give
\[
\begin{aligned}
n_r={}&\delta(hF_h-F)+h\delta G_h/r
       +2Ch\epsilon/r^2\\
 &+(C\delta-CF_{hh}/2)/r^2
       -(Cc+CG_{hh}/2)/r^3 .
\end{aligned}
\tag{11}
\]
In \(K_4\), replace \(n_{rr}\) by the radial derivative of (11).
Using (3), (7), and (9), the full expression (10) simplifies to
\[
K_4=
\frac{4Chr^2\epsilon_r-2Cr c_r+2Cc-CG_{hh}
      +4h^2r^3\delta^2+2hr^2\delta G_h}{4C^2r^2}.
\tag{12}
\]
Here \(Ch\) means the product \(C\cdot h\); \(C_h=0\).
Equivalently, \(K_4=0\) says
\[
rc_r-c=2hr^2\epsilon_r-G_{hh}/2
       +2h^2\delta^2r^3/C+h\delta G_hr^2/C .
\tag{13}
\]
One can integrate this identity inside \(L\) without solving an
equation in a presumed rational function field. Directly differentiate
\(c/r-2h\epsilon-G_{hh}/(2r)
-h^2\delta^2r^2/C-h\delta G_hr/C\).
Equation (13) makes its radial derivative zero. Therefore
\[
\boxed{c=2hr\epsilon+G_{hh}/2+h^2\delta^2r^3/C
                  +h\delta G_hr^2/C+c_0r,\qquad c_0\in L_0.}
\tag{14}
\]
Substituting this exact expression into (11) cancels the
\(\epsilon\) terms and the \(r^{-1}\) terms. Put
\[
A_0=\delta(hF_h-F)-h^2\delta^2,\qquad
B_0=\delta-F_{hh}/2-c_0,\qquad A_0,B_0\in L_0.
\tag{15}
\]
Then \(n_r=A_0+CB_0/r^2-CG_{hh}/r^3\).
Differentiating the difference with an explicit primitive gives
\[
\boxed{n=A_0r-CB_0/r+CG_{hh}/(2r^2)+n_0,\qquad n_0\in L_0.}
\tag{16}
\]
The constants \(c_0,n_0\) are actual elements of the retained
radial constant field, not assumed rational functions of \(h\).

The second equation in (8) now gives the complete remaining
coefficient \(f\) in compact form:
\[
\boxed{f=\frac r{2h}
\left\{R_0(b\delta+\epsilon)
 +(2Cb/r^3-G_h/r^2)c+bn_r+n_h/r\right\}.}
\tag{17}
\]
All symbols on the right are the explicit functions in
(3), (14), and (16), or their indicated exact derivatives.
Thus (17) is a formula for \(f\), not an additional differential
equation left to solve. It avoids an unnecessary expansion of the
derivatives of (16). Division by \(h\) occurs only in the coefficient
field, where \(h=t/r\ne0\); it is not an ambient polynomial operation.

## 5. The full cubic coefficient and the two radial weights

Substitute (14), (16), and (17) in the complete expression for \(K_3\)
in (10). Define
\[
U_0=c_0-G_h^2/(4C)\in L_0,\qquad
A_*=\frac{F_{hhh}}3+(U_0)_h-\delta_h\in L_0.
\tag{18}
\]
The result, retaining arbitrary \(\epsilon\), is
\[
\boxed{K_3=-\frac{M(\epsilon-\delta_h)}C
                 -\frac{A_*}{r^2}-\frac{5G_{hhh}}{6r^3}.}
\tag{19}
\]
For a direct coefficient check, multiplying the negative of (19)
by \(6Cr^3\), before using the definition of \(A_*\), gives
\[
\begin{aligned}
{}&6r^3M(\epsilon-\delta_h)
  +2CrF_{hhh}+6Cr(c_0)_h-6Cr\delta_h\\
&\hspace{28mm}+5CG_{hhh}-3rG_hG_{hh}.
\end{aligned}
\tag{20}
\]
This is also obtained by substituting into the explicit convolution
formula (10). In particular the derivatives of \(n_0\) occurring in
(17) cancel from this coefficient; no restriction on \(n_0\) was
used for that cancellation.

Since \(K_3=0\), equations (18)--(19) give
\[
M\eta=-CA_*/r^2-5CG_{hhh}/(6r^3).
\tag{21}
\]
The last retained Jacobian equation in (3) is
\((2r\mathcal D-1)(M\eta)=0\), because \(M\in L_0\).
Apply this operator to (21), noting that \(C,A_*,G_{hhh}\)
are radial constants. The two distinct radial powers give
\[
0=5CA_*/r^2+35CG_{hhh}/(6r^3),\qquad
A_*r+7G_{hhh}/6=0 .
\tag{22}
\]
Radial differentiation of the last equality yields \(A_*=0\).
Substitution then yields \(G_{hhh}=0\), and (21) gives \(M\eta=0\).
This step uses \(\mathcal Dr=1\), not a rationality assumption or
a choice of a branch of a square root. No division by \(M\) occurs.

## 6. Consequences, both branches, and scope

The proved restrictions are
\[
\boxed{
G_{hhh}=0,\qquad
\frac{F_{hhh}}3+
  \left(c_0-\frac{G_h^2}{4C}\right)_h-\delta_h=0,\qquad
M(\epsilon-\delta_h)=0.}
\tag{23}
\]
The first two may be integrated in \(L_0\) using its exact
\(\partial_h\)-constant field \(\mathbb C\):
\[
\begin{gathered}
G=g_2h^2+g_1h+g_0,\qquad g_0,g_1,g_2\in\mathbb C,\\
c_0=\delta-F_{hh}/3+G_h^2/(4C)+\gamma,\qquad
\gamma\in\mathbb C .
\end{gathered}
\tag{24}
\]
For example \(G_{hh}/2\) is first a joint constant, and subtracting
its quadratic term reduces the assertion successively to linear
and constant terms. Thus (24) does not identify all of \(L_0\)
with a rational function field.

If \(M\ne0\), (23) forces \(\epsilon=\delta_h\).
The possible nonzero square-root residual from the preceding218
Jacobian note is therefore removed by the full lower potentials.
It is not removed by claiming that such a mode cannot belong to a
finite algebraic extension.

If \(M=0\), the same proof still gives (24) and the exact formulas
(14), (16), and (17). These equations put no further restriction
on \(\epsilon\). In this branch \(F,\delta\) also obey the defining
identity \(hF_h-F=2h^2\delta\), but no exclusion of this branch is
asserted here. An independent later use of the full determinant
may strengthen this conclusion; it is not an input to this note.

The remaining coefficients of the fourth potential, the lower
Jacobian coefficients, and the original-ring coordinate question
have not been solved here. In particular no arbitrary function of
\(h\) has been removed by an ambient shear. The formulas are
necessary identities inside the selected exact coefficient field,
not a construction of an actual frame from formal coefficients.

The two stable218 inputs and the full mixed-ratio potential source217
were freshly read through EOF. New unsaved inline algebra first
reconstructed (5)--(7) directly from \(q=t^2/\rho\), then checked
each coefficient in (8), (10), (12), and (19), including the
identically vanishing higher coefficients. These are finite
arithmetic checks, not proofs of the actual-chart or field gates.
No saved checker was executed, imported, or compiled, and no217
source, earlier source, index, JSON, or verification packet was
changed. This note makes no arbitrary-entry, unrestricted
cancellation, global-minimum, certification, or novelty claim.
