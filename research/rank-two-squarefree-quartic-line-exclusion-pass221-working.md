# A squarefree binary quartic cannot occur in the supplied frame

Status: working nonrealizability theorem for an actual supplied
exact1122 frame with full initial kernel \(ZW-F_4(X,Y)\), where
\(F_4\) is squarefree. The projected line forced by220 is incompatible
with the actual auxiliary locally nilpotent derivation.
No arbitrary frame-entry or unrestricted cancellation claim is made.

The decisive comparison occurs over \(\mathbb C(X)\), but it is a
contradiction for an actual derivation on the original polynomial ring.
No coordinate over the coefficient field \(L\) is lifted to that ring.

## 1. Actual assumptions and the selected pair

Assume the full hypotheses of
[general quartic220](rank-two-binary-quartic-leading-sextic-pass220-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(aT,bT,e_0T^2,h_0T^2)\bigr)
 =(\mathsf Z\mathsf W-F_4(\mathsf X,\mathsf Y)).
\end{gathered}
\tag{1}
\]
The symbol \(T\) in this display is independent. The polynomial
\(F_4\) is a nonzero complex homogeneous binary quartic with four
distinct projective roots. The equality is the entire initial ideal,
not merely one vanishing relation.

The actual chart of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
uses the literal quadratic pivot \(\partial_Z\) and gives
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A)\in\operatorname{LND}(A),\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=e_0/a^2=F_4(1,t)/\rho,\quad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\vartheta,\sigma\in L[v],\qquad L[y,z,w]=L[v].
\end{gathered}
\tag{2}
\]
In particular \(t,\rho\) are algebraically independent, \(Na=0\),
and \(X\) is transcendental over \(L(v)\). The derivation \(N\) is
extended to \(B=A[u]\) by \(Nu=0\).

[Zero return221](rank-two-nonsquare-quartic-zero-return-exclusion-pass221-working.md)
proves that \(R=0\) would force \(F_4\) to be a binary-quadratic
square. Hence \(R\ne0\) here. The actual birational return and
leading-sextic factorization in220 then give
\[
L[y,\vartheta]=L[v],\qquad
\max(\deg_v y,\deg_v\vartheta)=1.
\tag{3}
\]
If \(F_4=\prod_{i=1}^4\ell_i(X,Y)\), write
\(\ell_i(t)=\ell_i(1,t)\). The homogeneous part of the selected
plane-line equation is one of the six factors
\[
\ell_i(t)\ell_j(t)V
 -\rho\bigl(\ell_i'(t)\ell_j(t)+\ell_i(t)\ell_j'(t)\bigr)U,
\qquad i<j.
\tag{4}
\]
The root forms in the chosen pair are linearly independent over
\(\mathbb C\). We next normalize this pair by an actual coordinate
change, keeping track of its projected line.

## 2. Actual transport of the pair direction

Write the chosen root forms as
\[
X'=\alpha X+\beta Y,\qquad Y'=\gamma X+\delta Y,\qquad
d=\alpha\delta-\beta\gamma\ne0,
\quad l=\alpha+\beta t,\quad m=\gamma+\delta t.
\tag{5}
\]
Keep \(Z,W\) unchanged. This is a polynomial automorphism with the
literal inverse
\[
X=(\delta X'-\beta Y')/d,\qquad
Y=(-\gamma X'+\alpha Y')/d.
\tag{6}
\]
Its good-coordinate speeds are \(al,am\), both nonzero because
\(t\) is transcendental. Thus their exact \(E\)-degrees remain one;
the quadratic coordinates retain degree two. The full initial
ideal transforms by this same constant linear automorphism.

The literal pivot \(\partial_Z\) is unchanged, so its selected
coefficient \(N\), and consequently \(L\), are unchanged. The new
ratios and the projection at \(X'=0\) satisfy
\[
\begin{gathered}
t'=m/l,\qquad \rho'=\rho/l^2,\qquad q'=q/l^2,\\
y'=d\,y/l,\qquad
\vartheta'=\vartheta/l-2\rho\beta y/l^2,\\
w'=w-\beta y\vartheta/l+\rho\beta^2y^2/l^2.
\end{gathered}
\tag{7}
\]
For example \(X=(X'-\beta y)/l\) in the old chart gives these
formulas by substitution. The two by two linear transformation of
\((y,\vartheta)\) in (7) has determinant \(d/l^2\ne0\).
The new projected pair therefore still generates \(L[v]\).
The ratios \(t',\rho'\) are algebraically independent and generate
the same rational field as \(t,\rho\).

Most importantly, the selected pair factor transforms exactly as
\[
y'-\frac{t'}{\rho'}\vartheta'
=-\frac{lm\vartheta-\rho(\beta m+\delta l)y}{\rho l}.
\tag{8}
\]
The numerator is a scalar in \(L\) by the affine line relation (4).
After renaming the new coordinates and ratios, we consequently have
\[
F_4(X,Y)=XY(\alpha_0Y^2+\beta_0XY+\gamma_0X^2),\qquad
q=\frac{\alpha_0t^3+\beta_0t^2+\gamma_0t}{\rho},\qquad
y=h\vartheta+\nu,\quad h=t/\rho,\quad \nu\in L.
\tag{9}
\]
Here \(\alpha_0,\gamma_0\in\mathbb C^*\) because the other two
roots are distinct from the chosen axes. Squarefreeness also gives
\(\beta_0^2-4\alpha_0\gamma_0\ne0\), although that last inequality
is not used in the normalized-line argument below.
Equation (8) and (3) imply \(\deg_v\vartheta=1\): if it were
constant, so would \(y\).

This normalization has not replaced \(h\) by a complex constant.
It remains transcendental over \(\mathbb C\).

## 3. Literal potential coefficients and auxiliary degrees

For coefficient derivatives on \(L\), use the notation
\[
H_j(c;U,V)=\sum_{i=0}^j
\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{10}
\]
The actual first three potentials in184 give, for \(k,n,\ell\in L\),
\[
\begin{gathered}
\sigma=q_ty+q_\rho\vartheta+k,\\
z=q_\rho w+H_2(q;y,\vartheta)+k_ty+k_\rho\vartheta+n,\\
Rw+H_3(q;y,\vartheta)+H_2(k;y,\vartheta)
       +H_1(n;y,\vartheta)=\ell,\\
R=q_{t\rho}y+q_{\rho\rho}\vartheta+k_\rho .
\end{gathered}
\tag{11}
\]
All coefficient derivatives are taken before evaluating \(U=y,V=\vartheta\).

Put \(\mathcal D=h\partial_t+\partial_\rho\) on \(L\). Since
\(\mathcal D h=0\), one has
\(\mathcal D^j q=j!H_j(q;h,1)\). Directly,
\[
\begin{gathered}
q=\alpha_0h^3\rho^2+\beta_0h^2\rho+\gamma_0h,\\
\mathcal Dq=2\alpha_0h^3\rho+\beta_0h^2,\qquad
\mathcal D^2q=2\alpha_0h^3,\qquad \mathcal D^3q=0,\\
[V]\,\mathcal R(hV+\nu,V)
=h q_{t\rho}+q_{\rho\rho}
=\frac{t(\gamma_0-\alpha_0t^2)}{\rho^3}\ne0 .
\end{gathered}
\tag{12}
\]
The last nonvanishing follows from the transcendence of \(t\).
In particular the normalized chart has nonzero, degree-one return.

Solving the third potential in (11) for \(Rw\) gives a right side
of degree at most two in \(\vartheta\): its possible cubic coefficient is
\(H_3(q;h,1)=0\), and the other terms already have degree at most
two. Since \(R\) has degree one and \(w\in L[\vartheta]\),
\(\deg_\vartheta w\le1\). The second potential then yields
\[
\begin{gathered}
w=\lambda\vartheta+\omega,\qquad
z=\alpha_0h^3\vartheta^2+\kappa\vartheta+\zeta,\\
\sigma=(2\alpha_0h^3\rho+\beta_0h^2)\vartheta+q_t\nu+k,
\qquad \lambda,\omega,\kappa,\zeta\in L .
\end{gathered}
\tag{13}
\]
The nonzero quadratic coefficient of \(z\) is exactly
\(H_2(q;h,1)=\alpha_0h^3\); it has not been obtained by a
coefficient-field coordinate change.

Now form the actual polynomial derivation
\[
\mathcal P=aN-(NX)E,\qquad \mathcal PX=0,\qquad
\tau=aN\vartheta\in L^*.
\tag{14}
\]
It is a locally nilpotent derivation of \(B\). Indeed on
\(B_a=A_a[X]\) it is \(aN\) on \(A_a\) and fixes \(X\).
Here \(Na=0\), so this localized derivation is locally nilpotent.
Because the displayed expression in (14) preserves \(B\), local
nilpotence on that localization implies local nilpotence on \(B\).
It fixes \(L\) and acts on the chart as \(\tau\partial_\vartheta\).
Equations (2) and (13) give the actual coordinate columns
\[
\begin{aligned}
\mathcal PY&=\tau h,&
\mathcal PW&=\tau(X+\lambda),\\
\mathcal PZ&=\tau\{2\alpha_0h^3\vartheta+\kappa+
                    (2\alpha_0h^3\rho+\beta_0h^2)X\},\\
\mathcal P^2Z&=2\alpha_0h^3\tau^2\ne0,&
\mathcal P^2Y&=\mathcal P^2W=\mathcal P^3Z=0 .
\end{aligned}
\tag{15}
\]
Thus the exact auxiliary coordinate degrees are \((0,1,2,1)\).
The products in (15) are actual polynomials. No assertion is made
that \(h,\lambda,\tau\) separately belong to \(B\).

## 4. The exact Wang hypotheses

Let \(\Delta\) be a greatest common divisor in the UFD \(B\) of the
components of \(\mathcal P\), and put \(D=\mathcal P/\Delta\).
This is an actual polynomial derivation. Also
\(\mathcal P\Delta=\Delta D\Delta\) forces \(\mathcal P\Delta=0\):
otherwise the \(\mathcal P\)-degree of its left side is
\(\deg_{\mathcal P}\Delta-1\), while that of its right side is at
least \(\deg_{\mathcal P}\Delta\). Thus \(D\Delta=0\), and
\(D^nf=\mathcal P^nf/\Delta^n\). It follows that \(D\) is a
primitive locally nilpotent derivation with the same auxiliary
coordinate degrees as (15).

Localize at the nonzero polynomials of \(\mathbb C[X]\) and write
\(K=\mathbb C(X)\). Then
\[
D\in\operatorname{LND}_K K[Y,Z,W],\qquad
D\text{ is irreducible},\quad
D^2Y=D^2W=0,\quad D^2Z\ne0,\quad D^3Z=0 .
\tag{16}
\]
Irreducibility is preserved: a common nonunit factor after
localization would, by Gauss factorization, give a common
nonunit polynomial factor of the original components not in
\(\mathbb C[X]\), contrary to their gcd one.
No \(E\)-invariance of \(\Delta\) is required.

Use the two alternatives in
[Dasgupta--Gupta, Theorem4.1](https://arxiv.org/html/1701.03635v1#S4.Thm1),
their explicit restatement of Wang's result over a characteristic-zero
field. In the present notation the first alternative fixes a
nonzero \(K\)-linear form in \(Y,W\). The second supplies a
\(D\)-invariant coordinate \(V_0\) while retaining \(Y,W\) as the
other two coordinates of \(K[Y,Z,W]\).
We use this exact statement, not a conclusion about descent of
its coordinate system to \(\mathbb C[X,Y,Z,W]\).

The ratio of the two nonzero good components is
\[
\frac{DW}{DY}=\frac{X+\lambda}{h}.
\tag{17}
\]
It is transcendental over \(K\). For an elementary proof, divide
it by \(X\) and suppose that
\(\sum_j p_j(X)((X+\lambda)/(hX))^j=0\), with
\(p_j\in\mathbb C[X]\) not all zero. At the highest degree of
the \(p_j\), the Laurent expansion at \(X=\infty\) gives a
nonzero complex polynomial in \(1/h\). This cannot vanish,
because \(h\) is transcendental over \(\mathbb C\).
All elements of \(L\), including \(h,\lambda\), are independent
of the indeterminate \(X\) in this comparison.

Thus the first Wang alternative is impossible. In the second,
retaining \(Y,W\) implies that the coordinate \(V_0\), as a
coordinate in the one-variable polynomial ring
\(K[Y,W][Z]\), has form \(uZ+Q(Y,W)\), with \(u\in K^*\).
Indeed the degrees in \(Z\) of its two inverse polynomial
expressions multiply to one, and their linear coefficients are
units of \(K[Y,W]\), hence elements of \(K^*\).
After scaling, take \(V_0=Z+Q(Y,W)\).

If \(Q_j\) is a nonzero homogeneous polynomial of degree \(j\)
over \(K\), then \(Q_j(DY,DW)\ne0\) by (17). Since both good
components are killed by \(D\), the highest derivative of
\(Q_j(Y,W)\) is \(j!Q_j(DY,DW)\). It follows that the
\(D\)-degree of a nonconstant polynomial in \(Y,W\) equals its
ordinary total degree. The equality \(D(Z+Q)=0\), together with
the exact \(D\)-degree two of \(Z\), therefore forces
\[
\deg Q=2,\qquad Q_2=A_2(X)Y^2+B_2(X)YW+C_2(X)W^2,
\quad A_2,B_2,C_2\in\mathbb C(X).
\tag{18}
\]

## 5. The Laurent contradiction

Use the invariant identity \(D^2(Z+Q)=0\) and divide in the
fraction field by \(2(\tau/\Delta)^2\). Equations (15) and (18)
give the exact necessary identity
\[
\alpha_0h^3+A_2(X)h^2+B_2(X)h(X+\lambda)
                  +C_2(X)(X+\lambda)^2=0 .
\tag{19}
\]
This division is only an equality in a field. It does not assert
that the displayed denominator is a polynomial-ring unit.

For a nonzero rational function over \(\mathbb C\), let its
order at infinity here mean the exponent of its leading Laurent
power of \(X\); give zero the value \(-\infty\). Put
\[
m=\max\{\deg_\infty A_2,\ \deg_\infty B_2+1,\
                              \deg_\infty C_2+2\}.
\tag{20}
\]
If \(m>0\), the coefficient of \(X^m\) in (19) is a complex
linear combination of \(h^2,h,1\), with at least one nonzero
coefficient. Indeed the contributions containing \(\lambda\)
are one or two powers lower than the corresponding leading
terms. The transcendence of \(h\) makes this impossible.

Hence each of the adjusted orders in (20) is at most zero.
Taking the constant Laurent coefficient in (19) now gives
\[
\alpha_0h^3+a_2h^2+b_2h+c_2=0,\qquad a_2,b_2,c_2\in\mathbb C .
\tag{21}
\]
This is impossible because \(\alpha_0\ne0\) and \(h\) is
transcendental. This also covers the case when all three
adjusted orders are negative.

Both Wang alternatives have been excluded for the actual
primitive derivation (16). Therefore the normalized line in
(9) cannot occur.

## 6. Conclusion and scope

The actual constant linear transformation (5)--(8) carries any
selected pair line of a squarefree \(F_4\) to the excluded line.
The zero-return exclusion221 and leading-sextic theorem220 cover
the two prior gates. Consequently
\[
\boxed{\text{There is no supplied actual exact1122 frame with full
initial kernel }ZW-F_4(X,Y)\text{ and squarefree }F_4.}
\tag{22}
\]
This is a nonrealizability statement for the specified full initial
kernel. It is not a procedure entering such a frame from an arbitrary
sliced action. It asserts no result for the other root partitions,
height-two initial ideals, arbitrary global degree minima, or
unrestricted complex-threefold cancellation.

The proof does not assume \(L=\mathbb C(t,\rho)\), does not make
\(h\) complex, and never treats a generic-field coordinate as an
original coordinate. It also does not presume that the speed \(a\)
is a unit of the original ring.

The universal184 potentials, the complete220 factorization source,
the complete zero-return221 source, and the exact primary
Theorem4.1 statement were read before use. New unsaved symbolic
identities independently checked the cubic and quadratic directional
coefficients, the return coefficient, and the actual pair transport.
No saved checker was executed for this derivation. These written
arguments and finite controls are not human expert review,
proof-assistant certification, or historical novelty clearance.
No frozen source, index, packet, submission or external communication
was changed by this note.
