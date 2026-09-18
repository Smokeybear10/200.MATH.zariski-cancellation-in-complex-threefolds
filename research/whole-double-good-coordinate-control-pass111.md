# A whole-double polynomial control with the required degree bounds

A polynomial threefold can have a whole double fiber, collapsed selected
good generators of degree at most two, an actual degree-four coordinate c,
and a hidden degree-two parameter with nonconstant whole residue. The
example below has all these properties for either first normal action.
It nevertheless fails the actual whole-divisor noncollapse hypothesis.
It is therefore an intrinsic control, not a supplied original E-frame.

## 1. A flat polynomial quotient and its full kernel

For an integer e at least one, put
\[
\begin{gathered}
A=\mathbb C[x,y,t],\qquad f=y^2+x^e t,\qquad S=\mathbb C[x,f],\\
N=-x^e\partial_y+2y\partial_t
 =\det\frac{\partial(x,f,\,\cdot\,)}{\partial(x,y,t)},\\
\mathfrak m=(x,f)S,\qquad \mathfrak q=(x,y)A,\qquad
A/\mathfrak mA=\mathbb C[y,t]/(y^2).
\end{gathered}
\tag{1}
\]
Inverting x gives A_x=S_x[y]. This proves algebraic independence of
x,f. The triangular derivation is locally nilpotent: assign weights
zero, one, two to x,y,t. Each term lowers weight. Its coefficient gcd
is one, so it is the primitive canonical polynomial base Jacobian.

The exact monic presentation is
\[
\begin{gathered}
A\simeq S[\mathsf Y,\mathsf T]/
(\mathsf Y^2+x^e\mathsf T-f),\\
A=\bigoplus_{j\ge0}S t^j\ \oplus\ \bigoplus_{j\ge0}S y t^j,
\qquad \ker N=S,\\
\ker N^3=S\oplus Sy\oplus St.
\end{gathered}
\tag{2}
\]
Surjectivity of the presentation is immediate. Its source is free over
S[T] with basis 1,Y and hence x-torsion-free. After inverting x it
maps isomorphically to S_x[y], so its original kernel is zero. The
displayed nonzero free S-module proves faithful flatness.

Here is the full polynomial, rather than bounded-degree, gate for the
last two assertions. Over S_x, the degree-two module has basis 1,y,t.
Suppose a polynomial element has a minimal positive denominator x^k:
x^k a=A0(x,f)+A1(x,f)y+A2(x,f)t. Modulo x, the independent variable
t forces A2(0,y^2)=0; even and odd powers of y then force
A0(0,y^2)=A1(0,y^2)=0. All three coefficients are divisible by x,
contrary to minimality. Thus the degree-two module is exactly (2).
Its invariant elements satisfy -x^e A1+2y A2=0, which forces
A1=A2=0 by independence of 1,y over S. This proves the full kernel.

## 2. Polynomial coordinates with exact good and quartic degrees

Use the following actual coordinate change on this polynomial threefold:
\[
\begin{gathered}
F=x,\qquad G=y+xt,\qquad c=t+G^2,\\
t=c-G^2,\qquad y=G-x(c-G^2),\qquad
A=\mathbb C[F,G,c],\\
\det\frac{\partial(F,G,c)}{\partial(x,y,t)}=1.
\end{gathered}
\tag{3}
\]
The two triangular shears give the inverse in both orders and the
constant determinant. These are coordinates of A, not a constructed
four-coordinate frame for a separate derivation E.

Select A1=y and A2=G as the two good relative elements. If K is the
fraction field of S, then
\[
\begin{gathered}
A=S[A_1,A_2,c],\qquad K[A_1,A_2]=K[y]=A_K,\\
Ny=-x^e,\qquad NG=-x^e+2xy,\qquad
d:=N^2G=-2x^{e+1}\ne0,\qquad N^3G=0,\\
N^4c=6d^2=24x^{2e+2}\ne0,\qquad N^5c=0.
\end{gathered}
\tag{4}
\]
Generation follows already from x,G,c. The generic good pair embeds
the polynomial line, with maximum degree exactly two: its exact
quadratic relation is y squared+x^(e-1)(G-y)-f=0. The fourth
derivative follows from c=t+G squared, N cubed of t equal to zero,
and the Leibniz rule. Thus the higher specified degree of c is not
being removed by renaming that coordinate.

Both selected good elements vanish on the reduced component q. The
exact ideals and induced action are
\[
\begin{gathered}
\mathfrak q=(F,G),\qquad \mathfrak mA=(F,G^2),\qquad
A/\mathfrak mA=\mathbb C[c,\epsilon]/(\epsilon^2),\quad
\epsilon=\bar G,\\
\bar y=\epsilon,\qquad \bar t=\bar c,\qquad
\bar N=2\epsilon\partial_c,\qquad \bar NG=0,\\
e=1:\ N\mathfrak q\not\subset\mathfrak q^2,
\qquad e\ge2:\ N\mathfrak q\subset\mathfrak q^2.
\end{gathered}
\tag{5}
\]
The ideal equalities follow from G-y=xt and G squared-y squared
divisible by x. On the whole fiber, t=c and N(G)=0, so N(c)=2G.
For the final line use the generators x,y of q: Nx=0 and Ny=-x^e.
The degree-two hidden parameter t therefore exists in both normal
branches, with Nt=2y having a nonzero square-zero whole residue.

## 3. Precisely what does not transfer from the mixed proof

By (2) and (5), the degree-two module has independent whole residues
\[
\overline{\ker N^3}
 =\mathbb C\{1,\epsilon,c\},\qquad
\bar G^2=0,\qquad t=c-G^2\in\ker N^3.
\tag{6}
\]
Thus 1,G,G squared is not a residue-independent piece. Its third
element has zero residue. Also the degree-two image is not contained
in the constant Artin algebra C[epsilon]/epsilon squared: it contains c.
The actual mixed-image restriction104 and the sharp coefficient
extraction108 cannot be applied to this whole-double example.

This failure does not invalidate the one-element contraction from110.
Nc still has nonzero whole residue 2epsilon, so residue-basis purity
would apply to R Nc over the local invariant base R=S_m. What is missing
is the mixed-specific pure three-element piece and the sharp ideal
that produced the divided quartic and its derivative containment.
No prescribed mixed conic coefficients are asserted for (1).

## 4. A definite violation of the actual divisor hypothesis

The model is not merely missing a checked original inverse. The
specified good pair fails the actual whole-divisor noncollapse gate
in [divisor91](nonconical-residue-degree-bound-pass91.md), equation (2).
Take the invariant prime p=x, put D=S_(x), and k=C(f). Then
\[
\begin{gathered}
A_D/xA_D=\mathbb C(y)[t],\qquad f=y^2,\qquad
[\mathbb C(y):\mathbb C(f)]=2,\\
\overline N=2y\partial_t\ne0,\qquad
\bar A_1=\bar A_2=y,\qquad
\operatorname{trdeg}_{k}k[\bar A_1,\bar A_2]=0.
\end{gathered}
\tag{7}
\]
To identify the ring, localize C[y,t] by every nonzero polynomial in
y squared. This gives C(y)[t]: for a nonzero polynomial g(y), the
product g(y)g(-y) is a nonzero polynomial in y squared and supplies
an inverse for g. The quadratic degree is exact because the
independent variable f is not a square in C(f), so Y squared-f is
irreducible. The algebraic constant field of C(y)(t) over C(f) is
exactly C(y), since C(y) is relatively algebraically closed in its
purely transcendental extension C(y)(t). Indeed any nonconstant
rational function of t makes t algebraic over the field it generates;
if that function were algebraic over C(y), t would be algebraic too,
contrary to its transcendence.

Actual divisor91 requires transcendence degree one for the algebra
generated by the selected good residues. In (7) both belong to the
constant field, while the hidden parameter t survives. Consequently
this intrinsic family cannot realize that actual frame with these
selected good generators identified. Replacing a selected good
generator by t would change the data being tested and would also
make the closed component noncollapsed for that selection.

## Scope and finite verification

This note supplies a new polynomial-coordinate control and an exact
failed actual hypothesis. Its underlying conic and saturation method
are the retained intrinsic models of
[cyclic103](noncollapsed-cyclic-degree-module-pass103.md) and
[hidden-parameter104](quadratic-catalan-hidden-parameter-pass104.md).
The new simultaneous coordinate and degree choices are (3)--(5).
No new actual-frame existence theorem or universal hidden-parameter
theorem is proved, and no frozen file through110 is changed.

The [standalone finite checker](whole_double_coordinate_checks_pass111.py)
uses one method with e=1 through4. It checks both polynomial inverse
orders, the coordinate Jacobian, derivative degrees, exact quotient
and divisor substitutions, and finite residue independence. These
instances do not prove flatness, the all-polynomial saturation,
the full kernel, or a universal geometric classification.

The first assertion-bearing author command was
`/opt/anaconda3/bin/python research/whole_double_coordinate_checks_pass111.py`.
Its one method passed in 0.069 unittest seconds, exit zero, with
complete output 192ea4 and tool wall time 0.327367333 seconds.
No retained test was rerun for this author check.
