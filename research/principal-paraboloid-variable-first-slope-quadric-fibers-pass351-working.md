# The centered quadric and its exceptional fibers

Working result: in the actual nonzero-coupling chart264 with
\(k=s\), \(n=B(t)s+f(t)\), and \(b=B'\ne0\), the third surface
is an absolutely irreducible quadric. Its zero centered level forces
the shifted second intrinsic generator to be a constant times a
polynomial square. A nonsquare nonzero centered level also forces
that generator to have even degree, by residue-field degrees.

These are necessary restrictions over the exact coefficient field.
They are not an ambient normalization or recognition theorem. Explicit
formal examples below satisfy whole three-generator return and unit
gradient minors without two-generator ring return. A literal-potential
specialization of one example fails the full scalar calibration.

## 1. Exact actual inputs

Retain the complete actual hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
not just its third polynomial relation:
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\mathrm{initial}}=(X^2Z-Y^2)\text{ is the full initial kernel},\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad O=L[v],\quad Nv=1,\\
K=\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\qquad
L[y,z,w]=L[y,\sigma,\theta]=O,\\
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{1}
\]
Here \(a_0=EX\). Coefficient partials commute and fix \(v\).
Assume
\[
k=s,\qquad n=B s+f,\qquad B,f\in F:=\ker_L\partial_s,
\qquad b=B_t\in F^*.
\tag{2}
\]
In particular neither \(B\) nor \(f\) is assumed rational in \(t\).
There is no assumption on \(\ell_s\) or \(\ell_{ss}\).
The ambient ring \(\mathcal B\) is distinct from the coefficient \(B\).
We focus on \(\sigma\notin L\).

The result of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
retains the full fourth potential and the unit ideal of evaluated
two-gradient minors. In particular its third-gradient consequence is
\[
(H_U,H_P,H_V)O=O.
\tag{3}
\]
The new necessary restrictions here use (3) and whole intrinsic return.
They do not replace the remaining fourth-potential or scalar equations.

## 2. The exact affine reduction over L

Write \(u_1=n_t\), and introduce independent formal variables \(U,P,V\).
In264 the second primitive and the third surface become
\[
\begin{aligned}
w_{\mathrm f}&=\ell-2PU-u_1P-BV,\\
H&=U^2+u_1U+B w_{\mathrm f}
             +\frac{n_{tt}}2P^2+bPV-\ell_tP-\ell_sV.
\end{aligned}
\tag{4}
\]
Define
\[
\begin{gathered}
x=U+u_1/2-BP,\qquad
A_2=n_{tt}/2-B^2,\qquad C=\ell_s+B^2,\\
\bar h=h_0-B\ell+u_1^2/4.
\end{gathered}
\tag{5}
\]
Completing the square in (4), with no coefficient differentiation,
gives
\[
H-h_0=x^2+A_2P^2-\ell_tP+(bP-C)V-\bar h.
\tag{6}
\]
Set
\[
\begin{aligned}
p&=P-C/b,\\
q&=V+(A_2/b)P+A_2C/b^2-\ell_t/b,\\
d&=\bar h-A_2C^2/b^2+\ell_t C/b.
\end{aligned}
\tag{7}
\]
Then exactly
\[
H-h_0=x^2+b p q-d.
\tag{8}
\]
The inverse change is
\(P=p+C/b\),
\(V=q-(A_2/b)P-A_2C/b^2+\ell_t/b\),
\(U=x-u_1/2+BP\). It is affine over \(L\) with determinant one.
Thus, after evaluation on the actual line,
\[
O=L[x,p,q],\qquad p=\sigma-C/b\notin L,
\qquad (x,p,q)O=O.
\tag{9}
\]
The last equality is (3), since the gradient of (8) is
\((2x,bq,bp)\). It is automatic if \(d\ne0\), from (8).

The homogeneous degree-two part \(x^2+bpq\) has rank three over
every field extension of \(L\). A product of two linear forms has
rank at most two. Therefore (8) is absolutely irreducible, including
when \(d=0\). The surface is smooth for \(d\ne0\); for \(d=0\)
its unique geometric singular point is the origin. Equation (9)
means that the actual polynomial line does not meet that point.

All transformations (5),(7) concern formal and intrinsic coordinates
over \(L\). They are not transformations of actual \(X,Y,Z,W\).
Their coefficients need not be complex and may have nonzero
coefficient derivatives.

## 3. Zero centered level: exact square factorization

Suppose \(d=0\). Since \(p\notin L\), neither \(q\) nor \(x\)
can be zero: otherwise (8),(9) would force \(p\) to be a unit.
Every common irreducible divisor of \(p,q\) divides \(x\) by
\(x^2=-bpq\), contradicting (9). Consequently
\[
\gcd(p,q)=1.
\tag{10}
\]
Unique factorization in \(L[v]\) now shows that every irreducible
factor of either \(p\) or \(q\) has even multiplicity. Absorbing
constant factors into one of the square roots gives the exact form
\[
\boxed{
p=\lambda r^2,\qquad x=\lambda r s_1,\qquad
q=-\frac{\lambda}{b}s_1^2,
\quad \lambda\in L^*,\quad r,s_1\in L[v],\quad \gcd(r,s_1)=1.
}
\tag{11}
\]
No square root of a coefficient of \(L\) has been adjoined.
For example, first take \(p=\lambda r^2\); the factorization of
\(x\) then defines \(s_1=x/(\lambda r)\), and (8) gives the
displayed value of \(q\).

Whole intrinsic return is equivalently
\[
L[r^2,rs_1,s_1^2]=L[v],
\qquad\text{and hence }L[r,s_1]=L[v].
\tag{12}
\]
In particular
\[
\deg_v\sigma=\deg_vp=2\deg_vr\text{ is positive and even}.
\tag{13}
\]
At every geometric zero of \(p\), one has \(x=0\), \(q\ne0\),
and \(p_v=0\). The equality \(O=L[x,p,q]\), differentiated in
\(v\), gives \((x_v,p_v,q_v)O=O\). Thus at such a zero at least
one of \(x_v,q_v\) is nonzero. This does not require \(q_v\ne0\):
the projected plane can be ramified there while the full line is
immersed.

## 4. Nonzero level and exceptional residue fields

Suppose \(d\ne0\). At a geometric zero of \(p\), equation (8)
gives \(x^2=d\), so \(x\ne0\). Differentiation in \(v\) gives
\[
2x x_v+b(p_vq+pq_v)=0.
\tag{14}
\]
Together with the differentiated whole return, this implies
\[
\gcd(p,p_v,q_v)=1.
\tag{15}
\]
Indeed a common geometric zero would also have \(x_v=0\) by (14).
This is an immersion restriction at the exceptional fiber, not a
claim that the projected plane is smooth everywhere.

There is also a restriction over the exact field, before taking its
algebraic closure. If \(d\) is not a square in \(L\), each
irreducible divisor \(\pi\) of \(p\) has even degree. In the finite
field \(L[v]/(\pi)\), the residue of \(x\) is a square root of
\(d\). Hence this field contains the quadratic extension
\(L(\sqrt d)\), and its degree over \(L\) is even. Therefore
\[
d\notin L^{*2}\quad\Longrightarrow\quad\deg_v\sigma\text{ is even}.
\tag{16}
\]
The same statement applies to nonconstant \(q\).
Combining (13),(16), odd degree of the nonconstant \(\sigma\)
requires \(d\in L^{*2}\). In particular an affine \(\sigma\)
requires a nonzero square centered level. This is not a claim that
the square root is complex or an ambient polynomial.

## 5. Formal families delimit the force of these restrictions

This section drops the actual chart hypotheses. Work over any
characteristic-zero field \(L\), take \(b\in L^*\), \(d\in L\),
and a nonzero polynomial \(f_0(p)\in L[p]\). Define
\[
\begin{aligned}
p&=v^2-d,\\
x&=v+b p f_0(p),\\
q&=-1/b-2v f_0(p)-b p f_0(p)^2.
\end{aligned}
\tag{17}
\]
Then \(x^2+bpq=d\) and \(v=x-bpf_0(p)\), so the whole line
is generated by \(x,p,q\). Its surface gradient is a unit ideal,
also when \(d=0\): if \(p=x=0\), then \(v=0\) and \(q=-1/b\).

The exact projected ring and its conductor in \(L[v]\) are
\[
\begin{aligned}
L[p,q]&=L[p,vf_0(p)]
       =L[p]\oplus v f_0(p)L[p],\\
\operatorname{Frac}L[p,q]&=L(v),\qquad
\operatorname{cond}_{L[v]}L[p,q]=f_0(p)L[v].
\end{aligned}
\tag{18}
\]
Here \(L[v]=L[p]\oplus vL[p]\), since \(v^2=p+d\).
For the conductor, an element \(a(p)+vf_0(p)c(p)\) stays in
the displayed subring after multiplication by \(v\) exactly when
\(f_0\mid a\). Thus a nonconstant \(f_0\) gives genuine
birational field return but not two-generator ring return.

Even an abstract second relation with unit gradient minors does not
repair this ring boundary. Set
\[
Q_{\mathrm{aux}}=q+1/b+2x f_0(p)-bp f_0(p)^2.
\tag{19}
\]
The polynomial automorphism
\[
x_1=x-bpf_0(p),\qquad p_1=p,\qquad
q_1=q+2xf_0(p)-bp f_0(p)^2
\tag{20}
\]
has inverse
\(x=x_1+bp_1f_0(p_1)\),
\(q=q_1-2x_1f_0(p_1)-bp_1f_0(p_1)^2\).
Its Jacobian is one and it preserves \(x^2+bpq\).
In these coordinates the two relations are
\(x_1^2+bp_1q_1-d=0\), \(q_1+1/b=0\), whose evaluated
gradient minors include \(bq_1=-1\). The minors remain a unit
ideal after (20).

For \(f_0=p^j\), \(j\ge1\), the degrees in (17) are
\[
(\deg_vp,\deg_vx,\deg_vq)=(2,2j+2,4j+2).
\tag{21}
\]
Thus third-gradient and whole-line conditions alone give no uniform
bound on the other two degrees. Already \(j=1\) has degrees
\((2,4,6)\), an auxiliary relation of total degree three, and
unit two-gradient minors, but a nontrivial projected conductor.
The polynomial \(Q_{\mathrm{aux}}\) is not asserted to be296's
coefficient-corrected fourth potential.

## 6. A literal-potential control fails the full determinant

The distinction can be checked within the first three literal
potential identities, still without claiming an actual polynomial
slice frame. Over \(L=\mathbb C(t,s)\), set
\[
k=s,\quad n=ts,\quad \ell=-t^2s,\quad
h_0=-t^3s-s^2/4,
\tag{22}
\]
and take (17) with \(b=1,d=0,f_0=p\). Thus
\(p=v^2\), \(x=v+v^4\), \(q=-1-2v^3-v^6\).
Recover the original intrinsic symbols by
\[
\sigma=p,\qquad \theta=q+t^2p-2ts,\qquad
y=x-s/2+tp,
\tag{23}
\]
and define \(z,w,Y,Z,W\) from the literal264 first two potentials
and actual-map formulas. The third potential is exactly \(h_0\),
and the whole intrinsic three-generator ring is \(L[v]\).
Nevertheless direct differentiation gives
\[
\left.\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}\right|_{v=0}
=t-X.
\tag{24}
\]
It therefore fails the required full scalar calibration (1), already
in its coefficient of \(X\). Neither strong complex-field return
nor an actual coordinate frame is claimed for this control. It is
not a cancellation counterexample.

## 7. Scope

The new actual conclusions are the affine quadric reduction (7),
the exact square factorization and even-degree condition at zero
level, and the nonsquare-level residue-degree restriction. The
exceptional-fiber immersion conditions retain the full intrinsic
line rather than assuming its plane projection is normal.

The formal families show why these necessary conclusions alone do
not yield recognition or projected ring return. They do not satisfy
all actual hypotheses, and (24) records a specific failed calibration.
No assertion is made about the existence of an actual frame in any
remaining degree pattern. This note does not duplicate a separate
fourth-potential exclusion of degree-two projected function fields.

The complete264 and296 sources were freshly read. Fresh unsaved
symbolic calculations checked the affine reduction, both orders of
(20), its Jacobian, the family identities, the literal third level,
and (24). The coefficient-field and UFD arguments above are written
algebraic arguments, not consequences of finitely many numerical examples.
No saved checker was executed, imported, compiled, or rerun by this
author. No earlier source or canonical index was changed.
