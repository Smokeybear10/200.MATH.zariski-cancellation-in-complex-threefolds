# Actual field return forces a reciprocal rho slope in the nonlinear split graph

**Status: working reciprocal-rigidity proof for graph degrees two through four.**

In the normalized split chart178, suppose \(m_\rho\ne0\) and
the graph \(\vartheta=P(y)\) has degree two, three or four. Then
\[
m_\rho=\frac{d^2}{t+\nu}\qquad\text{for some }\nu\in\mathbb C .
\]
The proof uses the exact field return of the original inverse.
A generic line pencil must have field degree one. Its coefficient
constraint, together with the retained differential equations,
rules out a nonconstant value of \(d^2/m_\rho-t\).

No determinant factor \(Ny\) is dropped. This note proves the
reciprocal form only, not recognition by an original coordinate.

## 1. Retained actual assumptions and nonzero slope

Use the actual normalized chart of
[the coefficient normal form178](split-affine-graph-coefficient-normal-form-pass178-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W),\quad
a=EX\ne0,\quad N=[u^3](\partial_Z|_A),\\
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\quad
y=\gamma v+\eta,\quad \gamma\in L^*,\quad\eta\in L,\\
t=EY/a,\quad \rho=(E^2W/2)/a^2,\quad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty,\quad
\ker_K\partial_t=\mathbb C,\\
r=k_\rho=0,\quad k,n_0,\ell\in K,\quad n=d\rho+n_0,\quad
d\in\mathbb C^*,\qquad 2\le\deg P\le4 .
\end{gathered}
\tag{1}
\]
The initial ideal is the full kernel. The coefficient field is the
exact one, not an assumed rational field. Primes denote the unique
extension of \(\partial_t\) to \(K\).

Put \(A_1=m_\rho\). For degree three or four,178 proves
\(A_1\in K\). For degree two, its literal coefficient formula
gives \(k'''=n_0''=0\), and
\[
h_2:=\ell'-\frac d2k''\ne0,\qquad
[y^2]\vartheta=\frac{h_2}{d^2}.
\]
The third coefficient equation178 is
\(\ell''=(A_1/d)(k''-2\ell'/d)\); hence
\[
A_1=-\frac{d^2\ell''}{2h_2}\in K .
\]
This coefficient-field argument does not require \(A_1\ne0\).
In every degree under consideration, subtracting the explicit
rho primitive gives \(m=A_1\rho+B_0\), with \(B_0\in K\).
The literal projected formulas178 then put \(z,w,\vartheta\)
in \(K(\rho)[y]\). The actual inverse gives
\(\mathbb C(y,z,w)=L(y)\), so
\(L(y)=K(\rho)(y)\). Intersecting with \(L\) yields
\(L=K(\rho)\): a rational expression over \(K(\rho)\) in
the transcendental \(y\) belongs to \(L\) only if coefficient
comparison makes it an element of \(K(\rho)\).
We have therefore established, including in degree two,
\[
m=A_1\rho+B_0,\quad A_1,B_0\in K,\quad
L=K(\rho),\quad
\mathbb C(y,z,w)=L(y)=K(\rho)(y).
\tag{2}
\]
We impose the additional branch condition \(A_1=m_\rho\ne0\).
The element \(\rho\) is transcendental over \(K\), and \(y\)
is transcendental over \(L\). These are actual field equalities
from the original polynomial inverse.

The literal normalized coefficients and differential equations are
\[
\begin{gathered}
w=\frac{A_1}{d}\rho+w_0(y),\quad
w_0(y)=\frac{B_0}{d}-\frac{k'''}{6d}y^3
             -\frac{n_0''}{2d}y^2+\frac{\ell'}d y,\\
\vartheta=\frac{yw-k''y^2/2-n_0'y+\ell}{d},\qquad
z=k'y-y\vartheta+d\rho+n_0-tw,\\
k''''+\frac{4A_1}{d^2}k'''=0,\qquad
n_0'''+\frac{3A_1}{d^2}n_0''=0,\qquad
\ell''=\frac{A_1}{d}\left(k''-\frac{2\ell'}d\right).
\end{gathered}
\tag{3}
\]
Nonlinearity means that at least one of
\(k'''\), \(n_0''\), \(h_2=\ell'-dk''/2\) is nonzero.
Indeed the respective fourth, third and second coefficients
of \(\vartheta\) obtained from (3) are
\(-k'''/(6d^2)\), \(-n_0''/(2d^2)\), and \(h_2/d^2\).

## 2. An exact pencil over the coefficient curve

Put
\[
T=\frac{d^2}{A_1}\in K^*,\qquad h=T-t,\qquad
z_*=z+\frac{y^2}{d}w .
\tag{4}
\]
The transformation \((y,z,w)\mapsto(y,z_*,w)\) is a polynomial
change in the projected three-ring, with inverse
\(z=z_*-y^2w/d\). It is not asserted to be an original
four-coordinate change.

Eliminate \(\rho\) from (3), using
\(d\rho=T(w-w_0)\). The exact result is
\[
\begin{gathered}
z_*=h\,w+g(y),\qquad
g(y)=g_3y^3+g_2y^2+g_1y+g_0\in K[y],\\
g_3=\frac{3k''+Tk'''}{6d},\qquad
g_2=\frac{2n_0'+Tn_0''}{2d},\\
g_1=k'-\frac{\ell}{d}-\frac{T\ell'}d,\qquad
g_0=n_0-\frac{TB_0}d .
\end{gathered}
\tag{5}
\]
For verification, substitute the first potential for \(\vartheta\)
in the formula for \(z\). The remaining cubic, quadratic and
linear terms before subtracting \(Tw_0\) are
\(k''y^3/(2d)+n_0'y^2/d+(k'-\ell/d)y+n_0\).
This gives every coefficient in (5).

Set \(F=\mathbb C(y)\) and \(M=K(y)\) for the next two sections.
The element \(w\) is transcendental over \(M\), since it is
affine with nonzero slope \(A_1/d\) in the variable \(\rho\).
Equation (2) now gives the exact pencil equality
\[
F(w,z_*)=M(w).
\tag{6}
\]
This is stronger than a nonzero formal Jacobian.

## 3. The elementary pencil-degree argument

We reproduce the algebraic lemma used in
[the actual pencil proof166, Section 3](cusp-quartic-actual-field-recognition-pass166-working.md).
Let \(F\) be any field, let \(M=F(f,g)\) have transcendence
degree one over \(F\), and suppose \(f\) is transcendental over
\(F\). If \(W\) is transcendental over \(M\), then
\[
[M(W):F(W,fW+g)]=\deg R,
\tag{7}
\]
where \(R(S,V)\) is an irreducible generator of the full
relation ideal of \((f,g)\) in \(F[S,V]\), and the right
side is total degree. In particular equality of the two fields
forces \(g\in F+Ff\).

Here is the proof without a rationality assumption on \(M\).
The relation ideal has height one and hence has the stated
irreducible generator. The two elements \(W,Z=fW+g\) are
algebraically independent over \(F\). If a polynomial relation
of total degree \(e\) vanished, its leading coefficient after
substitution would be the nonzero polynomial \(Q_e(1,f)\)
multiplying \(W^e\), impossible because \(f\) is transcendental.

The polynomial \(R(S,V)\) remains irreducible after adjoining
\(W\). The substitution \(V\mapsto Z-WS\) is a polynomial
variable change, so \(R(S,Z-WS)\) is irreducible in
\(F[W,Z,S]\). Its degree in \(S\) is exactly \(\deg R=e\):
the coefficient of \(S^e\) is \(R_e(1,-W)\ne0\).
Gauss's lemma makes this the irreducible polynomial of \(f\)
over \(F(W,Z)\), up to a field unit. Since \(g=Z-fW\),
adjoining \(f\) gives all of \(M(W)\). This proves (7).
If \(e=1\), the coefficient of \(V\) in \(R\) cannot be zero,
since that would make \(f\) algebraic over \(F\). Solving the
linear relation gives the final assertion.

## 4. A nonconstant pencil slope contradicts graph degree

Suppose \(h\notin\mathbb C\). Since \(K/\mathbb C\) has
transcendence degree one and \(\mathbb C\) is algebraically closed,
\(h\) is transcendental over \(\mathbb C\). It remains
transcendental over \(F=\mathbb C(y)\), because \(y\) is
transcendental over \(K\).

Before applying (7), the full coefficient field must be checked.
The inclusions
\[
F(w,z_*)\subseteq F(h,g)(w)\subseteq M(w)
\]
are equalities by (5)--(6). Intersecting with \(M\) gives
\(M=F(h,g)\). Indeed, for any subfield \(M_0\subset M\)
and a variable \(w\) transcendental over \(M\),
\(M_0(w)\cap M=M_0\): write a rational expression in \(w\)
and compare one nonzero coefficient after clearing its denominator.
Thus every premise of (7) holds with \(f=h\), not just for
a proper coefficient subfield.

The degree in (7) is one by (6), and consequently
\[
g(y)\in\mathbb C(y)+h\mathbb C(y),\qquad
g_i\in\mathbb C+\mathbb C h\quad(0\le i\le3).
\tag{8}
\]
For the coefficient assertion, take a finite complex basis for
the span of \(1,h,g_0,g_1,g_2,g_3\), beginning with \(1,h\).
It stays independent over \(\mathbb C(y)\): clearing a common
denominator and comparing powers of the transcendental \(y\)
proves this. Expressing (8) in that basis makes all components
outside the span of \(1,h\) zero. No rational parametrization
of \(K\) has been used.

The ODEs in (3), together with \(T=d^2/A_1\), give
\[
g_3'=\frac{h'k'''}{6d},\qquad
g_2'=\frac{h'n_0''}{2d},\qquad
g_1'=-\frac{h'\ell'}d .
\tag{9}
\]
For example, the numerator of \(6dg_3'\) is
\((3+T')k'''+Tk''''=(T'-1)k'''=h'k'''\).
The quadratic identity uses
\(Tn_0'''=-3n_0''\); the linear identity uses
\(T\ell''=dk''-2\ell'\).

Under the supposition \(h\notin\mathbb C\), the exact constant
field gives \(h'\ne0\). Write \(g_i=u_i+v_ih\) for
\(i=1,2,3\), with all six coefficients complex, as permitted by (8).
Differentiation and (9) force
\[
k'''=6dv_3\in\mathbb C,\qquad
n_0''=2dv_2\in\mathbb C,\qquad
\ell'=-dv_1\in\mathbb C .
\tag{10}
\]
Their derivatives vanish. The first two ODEs in (3) now imply
\(4A_1k'''/d^2=0\) and \(3A_1n_0''/d^2=0\).
Since \(A_1d\ne0\), both \(k'''\) and \(n_0''\) are zero.
Also \(\ell''=0\), so the third ODE in (3) gives
\(\ell'=dk''/2\), or \(h_2=0\).
All three positive-degree candidates from the observation
after (3) vanish. Thus \(\deg P\le1\), contradicting (1).

It follows that \(h\in\mathbb C\). With the precise sign
convention in (4), write \(h=\nu\), so
\[
T=t+\nu,\qquad
A_1=m_\rho=\frac{d^2}{t+\nu},\qquad \nu\in\mathbb C .
\tag{11}
\]
The denominator is nonzero because \(t\) is transcendental.
In particular \(A_1'+A_1^2/d^2=0\), now as a proved
consequence of actual field return.

## 5. Determinant calibration and the boundary of the result

The scalar equation retained from178 is still
\[
-\left(A_1'+\frac{A_1^2}{d^2}\right)\rho
-B_0'+\frac{A_1}{d}\left(n_0'-\frac{B_0}d\right)
=-\frac{a^3}{Ny}\ne0 .
\tag{12}
\]
Equation (11) cancels its rho coefficient by the preceding
pencil proof. It was not obtained by treating the right side
as a rational cube, replacing \(Ny\) by one, or assuming
\(a\) is a global unit. None of those shortcuts is justified
by the affine-parameter conclusion177 alone.

This proof is restricted to \(A_1\ne0\) and graph degrees two
through four in the normalized actual split chart. It does not
produce an original invariant coordinate, normalize \(t+\nu\)
by an unproved original reframe, or recognize this branch.
Those are separate steps. The \(A_1=0\) construction179 is
the complementary slope case. The older degree-two shear178
remains valid, but is not needed by this reciprocal argument.

This revision extends the original degree-three/four statement
by the explicit degree-two coefficient-field gate and the
\(g_1'\) comparison. It does not change the determinant
calibration or any original-coordinate formula.

The exact pencil lemma was freshly read in166 and is reproduced
here. The actual field and ODE inputs are the fully read178
proof. No new external theorem, checker execution, prior-file
edit, packet update, human expert certification, historical
novelty claim, or proof-assistant verification is involved.
