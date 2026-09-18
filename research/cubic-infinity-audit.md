# The cubic reduction at infinity

Let

\[
 F=f_3+f_2+f_1+f_0\in\mathbb C[x_0,x_1,x_2,x_3],
 \qquad f_3\ne0,
\]

where \(f_j\) is homogeneous of degree \(j\). If \(F\) is a stable coordinate, then

\[
 \boxed{\operatorname{Sing}V(f_3)\cap V(f_2)\ne\varnothing
 \quad\text{in }\mathbb P^3.}
 \tag{1}
\]

Here and throughout this note, the singular locus means the Jacobian locus
\(V(\partial f_3/\partial x_0,\ldots,\partial f_3/\partial x_3)\) of the
possibly nonreduced hypersurface scheme, not the singular locus of its
reduced support. For example \(f_3=y^3\) has the entire plane \(y=0\)
as its Jacobian locus although that reduced plane is smooth. The same
convention applies to \(f_d\) in the general-degree statement below.

Consequently an invertible linear change of the four affine variables makes

\[
 \boxed{F=uP(v_1,v_2,v_3)+H(v_1,v_2,v_3),
 \qquad \deg P\leq2,\quad\deg H\leq3.}
 \tag{2}
\]

The same conclusions hold for an LND slice, since a slice is a one-stable coordinate. This is a verified reduction lemma. A conclusion that all cubic stable coordinates are coordinates additionally requires the complete treatment of the coefficient cases in (2); this note does not silently assume that treatment.

## 1. What stability supplies

If \(F\) becomes a coordinate after adjoining \(N\) variables, every affine fiber \(X_\lambda=\{F=\lambda\}\) satisfies

\[
 X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}.
\]

Hence every \(X_\lambda\) is smooth and

\[
 \chi_c(X_\lambda)=1.
 \tag{3}
\]

In particular, \(F\) has no critical point. These are the only consequences of stability used in the infinity argument.

## 2. Positive-dimensional singular locus

Write \(S=V(f_3)\subset\mathbb P^3\). If \(\operatorname{Sing}S\) has a positive-dimensional component, it meets the projective hypersurface \(V(f_2)\). Indeed, a positive-dimensional projective variety cannot avoid a hypersurface of positive degree, by the projective dimension theorem. If \(f_2=0\), the assertion is immediate. Thus (1) holds in this case.

It remains to exclude the contrary situation in which \(\operatorname{Sing}S\) is finite, possibly empty, and

\[
 f_2(p)\ne0\quad\text{at every }p\in\operatorname{Sing}S.
 \tag{4}
\]

The finite-singular-locus hypothesis forces \(f_3\) to be reduced. A repeated factor would make all first derivatives vanish on the corresponding projective surface component. It also forces irreducibility: two different positive-degree hypersurface factors in \(\mathbb P^3\) intersect in at least a curve, and their product is singular along that intersection. In particular, the reduced isolated-singularity hypotheses in the formulas below are satisfied.

## 3. Under the contrary assumption, every projective fiber is smooth

In \(\mathbb P^4\), with homogeneous coordinates \([x_0:x_1:x_2:x_3:t]\), put

\[
 Y_\lambda=
 \left\{f_3+t f_2+t^2 f_1+(f_0-\lambda)t^3=0\right\}.
\]

Its affine chart \(t\ne0\) is \(X_\lambda\), which is smooth by (3). On \(t=0\), the defining polynomial's five partial derivatives are

\[
 \left(\frac{\partial f_3}{\partial x_0},
 \ldots,\frac{\partial f_3}{\partial x_3},f_2\right).
 \tag{5}
\]

They do not vanish simultaneously: at a regular point of \(S\), one of the first four is nonzero; at a singular point, (4) makes the last nonzero. Thus every \(Y_\lambda\) is a smooth cubic threefold, and its boundary is the same cubic surface:

\[
 Y_\lambda\cap\{t=0\}=S,\qquad X_\lambda=Y_\lambda\setminus S.
 \tag{6}
\]

There is no assumption here that a smooth affine fiber automatically has a smooth closure. Equation (5) is the explicit verification of that extra property under (4).

## 4. Euler characteristics and the Milnor-number bound

For a smooth degree-three hypersurface of complex dimension \(n\), the total Chern class is

\[
 c(TY)=\frac{(1+h)^{n+2}}{1+3h},\qquad \int_Y h^n=3.
\]

Consequently the smooth cubic threefold has

\[
 \chi(Y_\lambda)
 =3[h^3]\frac{(1+h)^5}{1+3h}
 =3(10-30+45-27)=-6,
 \tag{7}
\]

whereas a smooth cubic surface has

\[
 \chi(S_{\mathrm{sm}})
 =3[h^2]\frac{(1+h)^4}{1+3h}
 =3(6-12+9)=9.
 \tag{8}
\]

Let \(\mu_p\) be the ordinary local Milnor number of the isolated surface singularity at \(p\), and let \(\mu=\sum_p\mu_p\). The isolated-singularity smoothing formula gives

\[
 \chi(S)=9-\mu.
 \tag{9}
\]

The sign is important. A complex two-dimensional isolated hypersurface singularity has Milnor fiber with Euler characteristic \(1+\mu_p\). Smoothing replaces a contractible local singular piece, of Euler characteristic one, by that Milnor fiber, increasing the Euler characteristic by \(\mu_p\). The precise global formula is recorded in Maxim–Păunescu–Tibăr, Remark 3.2, equation (3.11), with \(n=2,d=3\).[^1]

For a degree-\(d\) projective hypersurface in \(\mathbb P^n\) with isolated singularities, the polar-degree formula is

\[
 \deg\operatorname{grad}(f)
 =(d-1)^n-\sum_p\mu_p.
\]

Taking \(d=n=3\), nonnegativity of the polar degree gives

\[
 \mu\leq8.
 \tag{10}
\]

This is exactly the formula stated at the start of Huh's paper.[^2] The gradient map need not be dominant: its polar degree is then zero. In particular, cones are permitted, and can attain \(\mu=8\). The argument does not apply Huh's separate, stronger theorem with its cone exception.

Combining (6)–(10) and additivity gives

\[
 \chi_c(X_\lambda)
 =\chi(Y_\lambda)-\chi(S)
 =-6-(9-\mu)
 =-15+\mu\leq-7.
 \tag{11}
\]

This contradicts (3), proving (1). The case \(\operatorname{Sing}S=\varnothing\) is included by taking \(\mu=0\).

## 5. A point in the intersection makes the cubic linear in one variable

Choose a nonzero representative of the point supplied by (1) as one vector of a basis of \(\mathbb C^4\). Let \(u\) be the coordinate in that direction and \(v=(v_1,v_2,v_3)\) the complementary coordinates. Write

\[
 \begin{aligned}
 f_3&=A u^3+u^2L(v)+uQ(v)+C(v),\\
 f_2&=B u^2+uM(v)+N(v),\\
 f_1&=a u+\ell(v).
 \end{aligned}
\]

Here \(L,M,\ell\) are linear, \(Q,N\) quadratic, and \(C\) cubic. The vanishing of all first derivatives of \(f_3\) at \([1:0:0:0]\) gives \(A=0\) and \(L=0\). The additional condition \(f_2(p)=0\) gives \(B=0\). Thus

\[
 F=u\bigl(Q(v)+M(v)+a\bigr)
   +C(v)+N(v)+\ell(v)+f_0,
\]

which is (2). The coefficient \(P\) may be zero, constant, linear, or quadratic. This is an actual linear change of affine variables, with no degree increase and no appeal to a conjectural polynomial degree reduction.

For completeness, degrees below three pose no corresponding difficulty: a nonconstant quadratic polynomial without critical points has a nonzero constant derivative along some vector in the radical of its quadratic form. In coordinates along that vector it is linear with nonzero constant coefficient, hence a coordinate. The same conclusion for a linear polynomial is immediate.

## 6. Audit conclusions and limits

No gap was found in the stated stable-coordinate reduction. The essential hypotheses and checks are:

- The affine fibers must be smooth and have Euler characteristic one. Smoothness alone is not being substituted for stability in the proof presented here.
- Positive-dimensional singular loci are handled before applying the isolated-singularity formulas.
- Reducedness, the smoothing sign, and the possibility of polar degree zero are all accounted for.
- The boundary is a surface in \(\mathbb P^3\), while the compactified fiber is a threefold in \(\mathbb P^4\); the two Euler calculations use different dimensions.
- The final conclusion is the explicit linear-in-one-variable form (2). A global cubic classification additionally depends on the separately verified quadratic-coefficient branches.

The Chern coefficients in (7) and (8), and the arithmetic in (11), were checked independently by exact symbolic expansion. The geometric argument is a cited written proof, not a proof-assistant certificate or a claim of novelty.

## 7. The same necessary reduction in every higher degree

The argument also proves a limited higher-degree statement. Let \(F\)
be a stable coordinate of total degree \(d\ge3\) in four complex
variables, with leading pieces \(f_d,f_{d-1}\). Then

\[
 \operatorname{Sing}V(f_d)\cap V(f_{d-1})\ne\varnothing
 \quad\text{in }\mathbb P^3.
 \tag{12}
\]

Indeed, absence of an intersection again forces the singular locus
of the reduced boundary to be finite and makes each compactified
fiber smooth. For smooth degree-\(d\) hypersurfaces of dimensions
three and two, their Euler characteristics satisfy

\[
 E_3(d)-E_2(d)=1-(d-1)^4.
\]

The isolated surface-singularity correction and the polar-degree
identity used above therefore give

\[
 \begin{aligned}
 \chi_c(X_\lambda)
 &=1-(d-1)^4+\sum_p\mu_p\\
 &\le1-(d-1)^4+(d-1)^3\\
 &=1-(d-1)^3(d-2)<1.
 \end{aligned}
\]

This contradicts stability and proves (12). The same projective
dimension argument covers positive-dimensional singular loci.

Choosing a point in (12) as the \(u\)-direction removes \(u^d\)
and \(u^{d-1}v_i\) from \(f_d\), and \(u^{d-1}\) from
\(f_{d-1}\). Hence

\[
 \deg_u F\le d-2.
 \tag{13}
\]

For \(d=4\), this yields exactly

\[
 F=A(v)u^2+B(v)u+C(v),\qquad
 \deg A\le2,\quad\deg B\le3,\quad\deg C\le4.
 \tag{14}
\]

The general Euler subtraction and the coefficient elimination were
reconstructed in a separate model check. This is a necessary normal
form, not a quartic classification. It reduces the degree in one
chosen variable, not the total degree, and gives no induction down
to the cubic theorem. The restriction \(d\ge3\) is essential:
the strict inequality disappears for \(d=2\).

## Sources

[^1]: Laurenţiu G. Maxim, Laurenţiu Păunescu, and Mihai Tibăr, [“Vanishing cohomology and Betti bounds for complex projective hypersurfaces”](https://www.numdam.org/item/10.5802/aif.3486.pdf), *Annales de l'Institut Fourier* **72** (2022), 1705–1731. Remark 3.2 and equation (3.11), printed p. 1720, give the reduced isolated-singularity Euler formula; equation (1.3), p. 1706, also records the smooth hypersurface Euler formula.

[^2]: June Huh, [“Milnor numbers of projective hypersurfaces with isolated singularities”](https://arxiv.org/pdf/1210.2690), arXiv:1210.2690v2, p. 1; published in *Duke Mathematical Journal* **163** (2014), 1525–1548, [DOI 10.1215/00127094-2713700](https://doi.org/10.1215/00127094-2713700). Used for the polar-degree identity and its nonnegative-degree bound, not for the stronger theorem excluding cones.
