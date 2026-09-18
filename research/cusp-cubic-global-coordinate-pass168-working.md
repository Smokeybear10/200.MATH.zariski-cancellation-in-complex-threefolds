# An actual invariant coordinate for every cubic graph cusp chart

Status: working proof pending independent review of this saved artifact.
Under the retained actual cusp hypotheses and a fixed-axis cubic graph,
the projected coordinate constructed in167 extends to a polynomial
coordinate of the original four-ring. The extension is an explicit
cubic correction, with a two-sided polynomial inverse. This recognizes
this subcase, not unrestricted cancellation.

## 1. Assumptions and the exact coefficient data

Retain all hypotheses of
[the cubic field-forcing theorem167](cusp-cubic-field-forcing-pass167-working.md):
\(B=A[u]=\mathbb C[X,Y,Z,W]\), \(E=\partial_u\), exact time
degrees \((1,1,2,2)\), full weighted initial kernel \((XZ-Y^3)\),
and the actual projected graph \(\vartheta=P(y)\) of degree three.
In particular the actual chart is
\[
\begin{gathered}
Y=y+tX,\quad
Z=z+(3t^2y+k)X+t^3X^2,\quad
W=w+P(y)X+\rho X^2,\\
z=3ty^2+k_0'y+rP(y)+n,\qquad
rw=\ell-y^3-k_0''y^2/2-n_0'y-sP(y).
\end{gathered}
\tag{1}
\]
Here \(t\) denotes the \(\tau\) of167, and a prime is its extended
coefficient derivative on \(K=\ker_L\partial_\rho\).
The exact results of167 give constants
\(r,C_3\in\mathbb C^*\), \(s,\alpha,\beta,h\in\mathbb C\), with
\((\alpha,\beta)\ne(0,0)\), and
\[
\begin{gathered}
\chi=\alpha t+\beta,\quad \lambda=1/\chi,\quad
k=r\rho+k_0,\quad n=s\rho+n_0,\quad
\ell=(-1/\chi-s^2/r)\rho+\ell_0,\\
P=p_3U^3+p_2U^2+p_1U+p_0,\quad
p_3=C_3/\chi^3,\quad k_0'''=6s/r-6C_3/\chi^4,\\
p_2=\chi(s k_0''/(2r)-n_0''/2),\quad
p_1=(\alpha/\chi)\rho+b_1,\quad
b_1=\chi(s n_0'/r+\ell_0'),\\
p_0=e\rho+d_0,\quad e+s/r=h/\chi,\qquad
k_0,n_0,\ell_0,d_0\in K,\quad \ker_K\partial_t=\mathbb C .
\end{gathered}
\tag{2}
\]
The proof that \(h\) is complex uses the actual field equality and
the pencil-degree lemma. It is not an assumption about formal data.
No normalization dividing by \(\alpha\) is made here.

Write \(w_*=w+(s/r^2)z\). The projected coordinate theorem167 says
\[
z+r^2(\alpha y+h)w_*=P_*(y)+g_0,\qquad
P_*\in\mathbb C[y],\quad P_*(0)=0,\quad
g_0=(1+sh)n_0+rd_0+rh\ell_0\in K .
\tag{3}
\]
Moreover \([y^4]P_*=-r\alpha\), and \(K=\mathbb C(g_0)\).
The rationality conclusion is not needed for the correction argument;
the exact constant field and (3) are sufficient.

## 2. An elementary descent calculation

Introduce coefficient functions, distinct from the graph coefficients
\(b_1,d_0\):
\[
\mathsf b=st^3-rk_0,\qquad
\mathsf c=sk_0-rn_0,\qquad
\mathsf d=r\ell_0+sn_0 .
\tag{4}
\]
Their useful exact identities are
\[
\mathsf b'''=6rC_3/\chi^4,\qquad
\chi\mathsf c''=2rp_2,\qquad
\chi\mathsf d'=rb_1 .
\tag{5}
\]
Set \(F=XZ-Y^3\), \(\mathcal L=\beta X+\alpha Y+h\), and define
an actual polynomial
\[
I_*=Z+\mathcal L(r^2W+sZ-rF)\in B .
\tag{6}
\]
The inner expression has the following literal chart expansion:
\[
r^2W+sZ-rF
=-\frac{r\rho}{\chi}+\frac{\mathsf b''}{2}y^2
 +\mathsf c'y+\mathsf d
 +(\mathsf b'y+\mathsf c)X+\mathsf bX^2 .
\tag{7}
\]
For example its \(X\) coefficient is
\((3st^2-rk_0')y+sk_0-rn_0\), and its \(X^2\)
coefficient is \(st^3-rk_0\). Its constant coefficient follows
by substituting both equations for \(z,w\) in (1). This checks
the mixed terms without imposing the graph equation on independent
variables prematurely.

By (3), the constant coefficient of \(I_*\) is
\(g_0+q_3y^3+q_2y^2+q_1y\), with \(q_i\in\mathbb C\).
Indeed it is \(g_0+P_*(y)+r(\alpha y+h)y^3\), whose fourth
degree term cancels. Explicitly
\[
\begin{gathered}
q_3=rC_3/\chi^3+\alpha\mathsf b''/2,\\
q_2=3t+rp_2+h\mathsf b''/2+\alpha\mathsf c',\\
q_1=k_0'+rb_1+h\mathsf c'+\alpha\mathsf d .
\end{gathered}
\tag{8}
\]
Define six more coefficient functions
\[
\begin{array}{lll}
A_2=\alpha\mathsf b'+\chi\mathsf b''/2,&
A_1=3t^2+h\mathsf b'+\alpha\mathsf c+\chi\mathsf c',&
A_0=k_0+h\mathsf c+\chi\mathsf d,\\
B_1=\alpha\mathsf b+\chi\mathsf b',&
B_0=t^3+h\mathsf b+\chi\mathsf c,&
C_0=\chi\mathsf b .
\end{array}
\tag{9}
\]
Collecting (6)--(7), including cancellation of every \(\rho\)
coefficient, gives
\[
I_*=g_0+\mathcal Q(X,y),\qquad
\mathcal Q=q_3y^3+q_2y^2+q_1y
 +X(A_2y^2+A_1y+A_0)+X^2(B_1y+B_0)+X^3C_0 .
\tag{10}
\]
In particular the term \(\chi\mathsf b''/2\) belongs in
the coefficient of \(Xy^2\), not \(Xy\).

Equations (5), (8), and (9) give the six recurrences
\[
A_2'=3q_3,\quad A_1'=2q_2,\quad A_0'=q_1,\qquad
B_1'=2A_2,\quad B_0'=A_1,\quad C_0'=B_1 .
\tag{11}
\]
For the first, differentiating \(A_2\) gives
\(3\alpha\mathsf b''/2+\chi\mathsf b'''/2=3q_3\).
For the next two, use respectively
\(\chi\mathsf c''=2rp_2\) and \(\chi\mathsf d'=rb_1\).
The last three follow directly by differentiation.
As the \(q_i\) are constant, these recurrences prove the polynomial
identity
\[
(\partial_t-X\partial_y)\mathcal Q(X,y)=0 .
\tag{12}
\]
Now substitute \(y=Y-tX\), holding \(X,Y\) fixed. By the chain
rule every coefficient of
\(Q(X,Y):=\mathcal Q(X,Y-tX)\in K[X,Y]\) has derivative zero.
The constant field in (2) therefore proves
\(Q\in\mathbb C[X,Y]\), of total degree at most three.
This is coefficientwise descent, not an integration assumption on
algebraic functions and not an assertion that a localized unit is
a global unit.

For an explicit coefficient formula, put
\[
\begin{aligned}
Q={}&q_3Y^3+q_2Y^2+q_1Y\\
&+X\bigl((A_2-3tq_3)Y^2+(A_1-2tq_2)Y+A_0-tq_1\bigr)\\
&+X^2\bigl((B_1-2tA_2+3t^2q_3)Y+B_0-tA_1+t^2q_2\bigr)\\
&+X^3(C_0-tB_1+t^2A_2-t^3q_3).
\end{aligned}
\tag{13}
\]
Every displayed coefficient is an element of \(\mathbb C\) by
(11). Thus \(t\) in this specification is not an original-ring
denominator or an extra variable in the resulting polynomial.

## 3. The global coordinate and recognition

Set \(I=I_*-Q(X,Y)\). This is an actual polynomial in \(B\).
Equation (10) gives the equality \(I=g_0\) in the actual fraction
field. Since \(g_0\in L\subset\operatorname{Frac}A\), one has
\(EI=0\); because \(B\) is a domain, this equality holds in \(B\).
It follows that \(I\in A\cap L=S\). Nothing was divided by the
speed \(a=EX\) in constructing \(I\).

There is an explicit inverse on the whole four-ring. Put
\[
\begin{gathered}
J=W+(s/r^2-X/r)Z,\\
I=Z+r^2\mathcal L J+r\mathcal L Y^3-Q(X,Y),\\
Z=I-r^2\mathcal L J-r\mathcal L Y^3+Q(X,Y),\qquad
W=J-(s/r^2-X/r)Z .
\end{gathered}
\tag{14}
\]
The only denominators are nonzero complex constants. With \(X,Y\)
unchanged, substitution verifies both composition orders. Hence
\(B=\mathbb C[X,Y,I,J]\), and \(I\) is a nonconstant polynomial
coordinate, not merely a rational coordinate.

For recognition, apply Bhatwadekar--Gupta--Lokhande's
[Theorem 3.5](https://arxiv.org/html/1501.01438v1).
Its hypotheses are satisfied: \(E\ne0\) is locally nilpotent and
\(\mathbb C[I]\)-linear on the polynomial three-ring over
\(\mathbb C[I]\) in (14). Also \(A\simeq B/(u)\) is regular,
since \(Eu=1\) makes the hypersurface \(u=0\) smooth. The theorem
therefore gives \(A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}\).
This invokes that external theorem, whose statement and displayed
proof were freshly read. It is not a new proof of its dependencies.

The argument treats \(\alpha=0\) and \(\alpha\ne0\) together,
without evaluating at a possibly forbidden point of \(K\).
The invariant has original weight at most four. No minimal-weight
claim is needed.

## 4. A nonvacuous actual cubic example

Take independent polynomial coordinates \(x,y,t,\rho\), and
\(E=\partial_x\). Define
\[
\begin{gathered}
X=x,\quad Y=y+tx,\\
Z=y^3+t+(3t^2y+\rho-t^3)x+t^3x^2,\\
W=-\rho-(y-t)^3+\bigl((y-t)^3+t\bigr)x+\rho x^2 .
\end{gathered}
\tag{15}
\]
These have exact \(E\)-degrees \((1,1,2,2)\). Their leading
coefficients are \(1,t,t^3,\rho\), so the full initial kernel
is precisely \((XZ-Y^3)\): on inverting the first leading
variable, the remaining three independent parameters are
that variable, \(t\), and \(\rho\), and the displayed prime
hypersurface has the same dimension.

Here \(r=1,s=0,\chi=1,C_3=1,h=0\),
\(k_0=-t^3,n_0=\ell_0=t^3,d_0=t-t^3\).
The graph is \(P(y)=(y-t)^3+t\), and the construction gives
\(Q=Y^3\) and
\[
I=(1-X^2)Z+XW+(X-1)Y^3=t,\qquad J=W-XZ .
\tag{16}
\]
This is also an actual inverse check, not just a formal determinant
example. Define
\[
\Gamma(x,y,t)=-(y-t)^3-t(3y^2-3ty+t^2)x
 +(t^3-3t^2y)x^2-t^3x^3 .
\]
Then \(J=-\rho+\Gamma(x,y,t)\). Recover
\(x=X,\ t=I,\ y=Y-XI,\ \rho=\Gamma(X,Y-XI,I)-J\).
Together with (14) and (16), these are polynomial inverses in
both directions. The example confirms that the cubic branch
need not be empty; it is not a cancellation counterexample.

## Scope and correction history

This proves recognition for the cubic graph branch, subject to
the retained actual hypotheses and proof dependencies159,166,167.
Together with166 it handles cubic and quartic graphs in that
fixed cusp chart. It does not handle every lower graph degree,
the \(r=0\) branches, other weighted initial configurations, or
the unrestricted coordinate-entry problem. The full cancellation
target remains unsolved.

During derivation, an initial coefficient collection omitted
\(\chi\mathsf b''/2\) from \(A_2\), producing a spurious
obstruction to (6). Correctly collecting (7) repairs it, as
(9)--(12) show. That discarded obstruction is not a result and
is not evidence against the template.

Independent AI reviews and bounded exact controls do not constitute
proof-assistant certification, expert review, or novelty clearance.
No previous frozen artifact is changed by this note.
