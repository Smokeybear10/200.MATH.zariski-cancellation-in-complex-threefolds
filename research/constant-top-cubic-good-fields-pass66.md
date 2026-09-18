# The good leading fields in the constant-top cubic normal form

The corrected cubic normal form has two independent good leading
fields, not just two independent defects. Their exact common kernel
is the same actual polynomial ring \(k[t,f]\). The corrected
Heisenberg field also has coefficients in the rational curve field
\(k(t)\) when expressed in the defect basis.

These deductions sharpen the remaining actual-partial preservation
question. They do not prove that preservation, that \(t\) is a
coordinate, or recognition of the constant-top cubic sector.

## 1. Actual inputs retained from pass65

Let \(B=k[Q_1,Q_2,X,Y]\), \(k=\mathbb C\), with the genuine coordinate
partials \(T_1,T_2,T_3,T_4\). Retain the hypotheses and permitted
constant normalizations of the
[constant-top cubic reduction](constant-top-cubic-pass65.md):
\[
P=Ex,\quad J=\operatorname{Jac}P,\quad h_2=E^2x,\quad
W_i=[E,T_i],\quad V_j=[E,W_j]\quad(j=3,4),
\]
\[
\mathcal V=[V_3(x)\mid V_4(x)],\qquad
L_0=\begin{pmatrix}0&0&1&0\\0&0&0&1\end{pmatrix},
\]
\[
\begin{aligned}
&E^3x=e_1,\qquad
h_2=(f-F(t),U(t),1,0)^{\mathsf t},\\
&EX=f,\qquad EY=G(t),\qquad Ef=1,\qquad Et=0,\\
&\ker(V_3,V_4)=k[t,f],\qquad
\ker(E,V_3,V_4)=k[t].
\end{aligned}
\tag{1}
\]
Here \(U,G\in k[t]\) are nonconstant. The defects are independent,
and \(E,W_1,W_2,V_3,V_4\) are commuting polynomial LNDs.

The [corrected Heisenberg note](constant-top-cubic-heisenberg-pass65.md)
proves
\[
W_1=-V_3,\qquad N=W_3+\tfrac12T_1,\qquad Nt=Nf=0,
\]
\[
R=N-\tfrac f2V_3\in\operatorname{LND}(B),\qquad
Rt=Rf=0,\qquad [R,E]=[R,V_3]=[R,V_4]=0.
\tag{2}
\]
In particular no nonzero motion of \(t\) by \(N\) remains available.

## 2. An exact identity for the second good field

The actual inverse Jacobian identity can be multiplied in either
order:
\[
\left(I+zJ+\frac{z^2}{2}\operatorname{Jac}h_2\right)
\left(I-zJ+\frac{z^2}{2}\mathcal V L_0\right)=I
\]
and the reverse product is also \(I\). The coefficient of \(z^3\)
in the reverse product gives
\[
J\operatorname{Jac}h_2=\mathcal V L_0J
=\mathcal V\operatorname{Jac}(f,G(t)).
\tag{3}
\]
This uses the full inverse identity, not just the coefficient in
the originally displayed order.

The normalized top equation is \(Je_1=V_3(x)\). Expanding (3)
using (1), and comparing the independent one-forms \(df,dt\), yields
\[
-F'(t)V_3(x)+U'(t)Je_2=G'(t)V_4(x).
\]
Since \(Je_2=-W_2(x)\), this is the polynomial field identity
\[
\boxed{U'(t)W_2+F'(t)V_3+G'(t)V_4=0.}
\tag{4}
\]
The comparison is valid because \(t,f\) are algebraically independent
actual polynomials in characteristic zero.

Neither \(U'\) nor \(G'\) is zero. Thus over \(\operatorname{Frac}B\),
\[
W_1=-V_3,\qquad
W_2=-\frac{F'}{U'}V_3-\frac{G'}{U'}V_4
\tag{5}
\]
is an invertible change of basis between the two pairs. In particular
\[
\operatorname{rank}(W_1,W_2)=2,\qquad
\ker(W_1,W_2)=k[t,f],\qquad
\ker(E,W_1,W_2)=k[t].
\tag{6}
\]
The kernel equalities are actual ring equalities: (5) gives
equivalence of annihilation for each polynomial, despite its
rational coefficients.

Equation (4) retains the full polynomials \(U',F',G'\).
It does not imply that either quotient in (5) is polynomial or that
the two fields stay independent after restriction to every fiber
of \(t\).

## 3. The corrected field has rational curve coefficients

The forms \(dt,df\) are independent. The space of rational
derivations annihilating both has dimension two; \(V_3,V_4\) form a
basis of it. Therefore there are unique
\(\alpha,\beta\in\operatorname{Frac}B\) with
\[
R=\alpha V_3+\beta V_4.
\tag{7}
\]
For each \(D\in\{E,V_3,V_4\}\), commutation in (2) and independence
give
\[
D\alpha=D\beta=0.
\]

Here the rational joint kernel equals the fraction field of the
actual joint kernel. To verify this directly, write a nonzero
joint rational invariant as \(p/q\), with coprime \(p,q\in B\).
For every one of the three LNDs,
\[
(Dp)q=p(Dq).
\]
The UFD property makes \(p\mid Dp\) and \(q\mid Dq\). For an LND
on a characteristic-zero domain, a nonzero polynomial dividing
its derivative has derivative zero: the usual LND degree drops
by one under a nonzero derivative and is additive on products.
Thus \(Dp=Dq=0\) for each field. Equation (1) puts both \(p,q\)
in \(k[t]\).

Consequently
\[
\boxed{\alpha,\beta\in k(t),\qquad
W_3=-\frac12T_1+
       \left(\frac f2+\alpha(t)\right)V_3+\beta(t)V_4.}
\tag{8}
\]
This strengthens the generic dependence recorded in pass65.
It proves neither \(\alpha,\beta\in k[t]\) nor their vanishing.
The polynomiality of the entire field \(R\) does not separately
remove the denominators of its coefficients in a possibly
nonprimitive two-field basis.

## 4. The actual-partial preservation gate

There is a precise sufficient recognition condition:
if one nonzero constant good direction
\[
T=c_1T_1+c_2T_2,\qquad (c_1,c_2)\ne(0,0)
\]
preserves the actual ring \(k[t,f]\), then the original kernel
\(\ker E\) is a polynomial three-ring.

Indeed \(Tt\in k[t,f]\). On the other hand
\[
E(Tt)=[E,T]t=0
\]
because both good tops kill \(t\). The kernel of \(E=\partial_f\)
on \(k[t,f]\) is \(k[t]\), so \(Tt\in k[t]\).
The actual constant partial \(T\) is an LND and now preserves this
one-variable ring. Therefore \(Tt\) is a complex constant.

If that constant is nonzero, completing \(T\) to a constant
coordinate frame shows that \(t\) is affine-linear with nonzero
coefficient in its corresponding coordinate. Hence \(t\) itself is
an ambient coordinate fixed by \(E\). The fixed-coordinate
recognition endpoint already used in pass65 applies with the
original slice.

If the constant is zero, \(t\) omits a genuine constant direction.
The three independent commuting LNDs \(E,W_1,W_2\), with joint
kernel \(k[t]\), satisfy the
[omitted-coordinate criterion](commuting-coordinate-descent-pass43.md).
The same recognition conclusion follows. These are applications
of the existing recognition theorems, not new source claims.

The premise has not been deduced here. What is automatic is only
\[
E(T_i t)=E(T_i f)=0\qquad(i=1,2),
\tag{9}
\]
because \(W_i\) annihilates \(t,f\). This places these derivatives
in \(\ker E\), not in \(k[t,f]\). To infer preservation one would
still have to prove their annihilation by both defect fields.
Equations (4) and (8) do not supply that missing condition by
themselves.

## 5. Scope and verification

This note was deduplicated against the two cited pass65 cubic
notes. Those notes establish the exact common kernel and the
corrected zero-motion LND, but do not contain (4), (6), or the
curve-field coefficient conclusion (8). The new deductions use
the full actual inverse-Jacobian equation and the polynomial UFD
in which the actual fields act.

No preceding-layer generator is promoted to an ambient coordinate,
no rational field coefficient is promoted to a polynomial, and
no auxiliary correction is promoted to a coordinate partial.
The remaining preservation premise in Section 4 is explicit.

The derivation of (8), including the reduced-fraction LND argument,
was independently reconstructed by Jet before saving this note.
No new numerical suite or shared metadata change is attached to
these all-instance identities. Frozen pass65 files are unchanged.

