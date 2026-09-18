# The degree-two residual has one intrinsic leading direction

In the two-quadratic profile with independent defects and coordinate
flow degree two, all highest commuting fields, including the original
action, span exactly one two-dimensional tangent plane over the fraction
field. After passing to the original slice quotient, their restrictions
have rank exactly one. This is a statement about the displayed leading
fields, not about every additive action of the quotient.

There is also a recognition criterion: if the two bad-coordinate speeds
have Jacobian rank at most one, the original kernel is polynomial. A
remaining degree-two instance must therefore have two algebraically
independent bad-coordinate speeds.

## 1. Exact assumptions and the earlier rank calculation

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be an LND,
and let \(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2T_i=0\quad(i=1,2),\qquad
\operatorname{ad}_E^3T_i=0\quad(i=3,4),
\quad E^3x=0,\quad h:=E^2x\ne0.
\tag{1}
\]
Write \(P=Ex\), \(J=\operatorname{Jac}P\),
\(W_i=[E,T_i]\), \(V_i=[E,[E,T_i]]\) for \(i=3,4\),
and suppose
\[
\mathcal V=[V_3(x)\mid V_4(x)]\quad\text{has rank two over }
K=\operatorname{Frac}B.
\tag{2}
\]
The selector \(L_0\) retains the third and fourth components.
The complete [earlier companion argument](two-quadratic-defects-pass39.md)
gives
\[
\operatorname{rank}_K\operatorname{Jac}h=2.
\tag{3}
\]
Specifically its six-dimensional matrix has cube zero and rank four,
hence Jordan type \((3,3)\). The rank-preserving block lemma identifies
the rank of its square with that of \(\operatorname{Jac}h\).
This source is an already proved conditional calculation, not a rank
claim for a hypothetical arbitrary matrix pencil.

## 2. Actual conjugated columns identify the common tangent plane

The actual flow is
\(F_t=x+tP+t^2h/2\). Its inverse-Jacobian matrix is
\[
C(t)=I-tJ+\frac{t^2}{2}\mathcal V L_0.
\tag{4}
\]
The coefficient of \(t^3\) in
\(C(t)P(F_t)=P\), using \(P(F_t)=P+th\), gives
\(\mathcal V L_0h=0\). Injectivity in (2) implies
\[
h_3=h_4=0,
\qquad f:=Ex_3\in\ker E,
\qquad g:=Ex_4\in\ker E.
\tag{5}
\]

The good conjugated columns are \(T_i+tW_i\). Acting on \(F_t\),
their coefficient of \(t^3\) gives \(W_i(h)=0\), for \(i=1,2\).
The bad columns are \(T_i+tW_i+t^2V_i/2\); their coefficient of
\(t^4\) gives \(V_i(h)=0\), for \(i=3,4\). Also \(E(h)=0\).
Together with (2)--(3), this proves
\[
\operatorname{span}_K\{E,W_1,W_2,V_3,V_4\}
=\operatorname{span}_K\{V_3,V_4\}
=\ker_K\operatorname{Jac}h,
\quad\dim_K=2.
\tag{6}
\]
All fields in the displayed list are commuting LNDs, with a zero
\(W_i\) allowed. This does not include the middle bad fields
\(W_3,W_4\).

Apply the same conjugated columns just to
\(F_{t,3}=x_3+tf\) and \(F_{t,4}=x_4+tg\). The good columns'
coefficients of \(t^2\) and bad columns' coefficients of \(t^3\)
give
\[
W_1(f)=W_2(f)=V_3(f)=V_4(f)=0,
\qquad
W_1(g)=W_2(g)=V_3(g)=V_4(g)=0.
\tag{7}
\]
These are genuine global polynomial identities, including points where
the displayed generic ranks drop.

## 3. Exactly one leading direction remains on the slice quotient

Now suppose \(E(s_*)=1\), and put \(A=\ker E\). The slice gives
\(B=A[s_*]\). Every field in (6) centralizes \(E\), so restricts
to a derivation on \(A\). A derivation of \(\operatorname{Frac}(A)(s_*)\)
annihilating \(\operatorname{Frac}(A)\) is a rational multiple of
\(\partial_{s_*}=E\). Thus the kernel of restriction, on the span
in (6), is precisely its one-dimensional \(KE\) subspace.

Consequently
\[
\operatorname{rank}_{\operatorname{Frac}A}
\operatorname{span}\{W_1|_A,W_2|_A,V_3|_A,V_4|_A\}=1.
\tag{8}
\]
Rank is unchanged by the field extension
\(\operatorname{Frac}A\subset K\); this follows by testing minors
of the fields' values on a finite set of algebra generators of \(A\).
The rank is not zero, because two independent \(V_i\) cannot both
be rational multiples of \(E\).

In particular all nonzero fields in (8) have the same kernel in \(A\),
and (5)--(7) place \(f,g,h_1,h_2\) in it. This does not prove that
every intrinsic LND of \(A\) has that kernel. No conclusion about the
global Makar-Limanov invariant or total intrinsic LND rank is drawn.

## 4. Low rank of the bad speeds produces an ambient coordinate

Put \(F=(f,g)^{\mathsf t}\). Because \(EF=0\), differentiation
gives
\[
E(\operatorname{Jac}F)=-(\operatorname{Jac}F)J.
\]
The bad components of \(V_i\) can therefore be computed exactly:
\[
L_0\mathcal V
=2(\operatorname{Jac}F)J_{\{3,4\}},
\tag{9}
\]
where \(J_{\{3,4\}}\) denotes the last two columns of \(J\).
Equivalently, the unrestricted bracket identity has the additional
term \(-\operatorname{Jac}(EF)_{\{3,4\}}\), which vanishes here.

Equation (6) puts \(E\) in the span of the two \(V_i\). Projection
to the bad components and (9) yield the important image condition
\[
F\in\operatorname{im}_K(L_0\mathcal V)
\subseteq\operatorname{im}_K\operatorname{Jac}F.
\tag{10}
\]
It is stronger than a Jacobian rank bound by itself.

If \(\operatorname{rank}\operatorname{Jac}F=0\), (10) gives
\(F=0\), so both \(x_3,x_4\) are invariant ambient coordinates.
If that rank is one and \(F\ne0\), its image is the line \(KF\).
Every differential column of \(F\) is therefore proportional to
\(F\), so
\[
f\,dg-g\,df=0.
\tag{11}
\]
If \(f\ne0\), the rational function \(g/f\) is killed by all
four ordinary partials and is a complex constant \(c\). Then
\(x_4-cx_3\) is an invariant ambient linear coordinate. If
\(f=0\), use \(x_3\) directly.

Under the original slice hypothesis, \(A\) is regular. The invariant
ambient coordinate just obtained supplies the other hypothesis of the
regular-kernel theorem, hence
\[
\operatorname{rank}\operatorname{Jac}(Ex_3,Ex_4)\le1
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{12}
\]
The theorem is used on the original four-variable action, not on an
auxiliary kernel.[^regular]

## 5. What the remaining branch must retain

Any instance left by this degree-two argument has both
\(\operatorname{rank}\operatorname{Jac}h=2\) and
\(\operatorname{rank}\operatorname{Jac}(f,g)=2\), while its displayed
intrinsic leading fields have rank one. Thus a strategy based only on
increasing the number of independent leading fields cannot close this
branch without changing the frame or using lower coefficients.

The already verified unimodular-pair examples realize the rank-two
speed case with polynomial quotients. Their leading coefficient ideals
may have nonempty simultaneous fixed loci even after removal of a gcd.
Those negative controls remain valid; (8) does not supply a free action
or a primitive intrinsic slice.

If the two defects have rank one instead, (6) is unavailable. The
[actual dependent-defect control](dependent-quadratic-defects-pass42.md)
has \(f,g=f^2+1\) with rank-one Jacobian but no constant projective
direction. It violates the image premise in (10), not (12). The
rank-two-defect hypothesis cannot silently be omitted.

The [standalone checker](two_quadratic_degree_two_checks_pass42.py)
checks actual-frame annihilations and ranks, the bracket identity,
slice-quotient restrictions, and positive/negative image controls.
The universal proof consists of the coefficient comparisons and
linear-algebra deductions above. Finite tests do not replace it.

[^regular]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and its proof, PDF p. 11. A nonzero LND fixing an actual ambient coordinate has polynomial kernel over that coordinate when its original kernel is regular. Here regularity follows from the original polynomial slice.
