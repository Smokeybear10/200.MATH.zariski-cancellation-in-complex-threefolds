# Recognition of every nonlinear graph in the supplied actual split chart

**Status: synthesis of the explicitly retained working proofs178--182.**

Every graph of degree two, three or four arising in the supplied actual
split chart175--177 has polynomial invariant ring. In every one of
these degrees, the vanishing or nonvanishing of \(m_\rho\) gives
two explicit invariant-coordinate constructions.

This is a recognition theorem for the stated subfamily, not for all
split graphs or unrestricted coordinate entry. It inherits the working
proofs and external endpoints identified below.

## 1. Actual hypotheses and the graph under consideration

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\qquad Eu=1,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W).
\end{gathered}
\tag{1}
\]
Here \(X,Y,Z,W\) are actual polynomial coordinates, and the ideal
is the full kernel of the map defined by their leading forms with
weights \((1,1,2,2)\). It is not merely one vanishing leading relation.

Use the selected original \(\partial_Z\), fixing \(X,Y,W\), and
\[
a=EX,\quad N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\quad
t=EY/a,\quad \rho=(E^2W/2)/a^2 .
\]
The actual chart175 supplies the nonzero \(N\), the independent ratios,
the finite separable field \(L/\mathbb C(t,\rho)\), and the projected
coordinates \(y,z,w,\vartheta\) with actual field return
\(\mathbb C(y,z,w)=L(v)\).
The completed plane proof175, constant-projection exclusion176 and
quadratic-projection exclusion177 give
\[
L[y]=L[v],\qquad y=\gamma v+\eta,\quad
\gamma\in L^*,\quad\eta\in L,\qquad
\vartheta=P(y),\quad P\in L[U],\quad\deg P\le4 .
\tag{2}
\]
The additional scope condition of this synthesis is
\(2\le\deg P\le4\).

The conclusion under these retained actual hypotheses is
\[
A\simeq\mathbb C^{[3]} .
\tag{3}
\]

## 2. The exhaustive nonlinear case split

The coefficient proof178 shows that every graph in this range has a
pure literal eliminant and admits actual constant-good translations
normalizing
\[
r=k_\rho=0,\qquad n=d\rho+n_0,\quad
k,n_0,\ell\in K:=\ker_L\partial_\rho,\qquad d\in\mathbb C^* .
\tag{4}
\]
Its translation formulas, inverse maps and coefficient-partial changes
are explicit. They preserve the original slice and graph degree.

Set \(A_1:=m_\rho\). For degrees three and four, Section 5 of178
proves \(A_1\in K\). The revised coefficient-field gate180 also
handles degree two: its nonzero quadratic coefficient is
\(h_2/d^2\), where \(h_2=\ell'-dk''/2\), and the third
coefficient ODE gives \(A_1=-d^2\ell''/(2h_2)\in K\).
In all three degrees an explicit rho primitive and actual field
return give \(m=A_1\rho+B_0\), \(B_0\in K\), and \(L=K(\rho)\).
There are exactly two alternatives in this field.

When \(A_1=0\), the construction179 returns the literal coefficient
\(m\) as an actual invariant polynomial \(I\). It supplies a companion
\(J\) with \(B=\mathbb C[X,Y,I,J]\), verified by both polynomial
inverse orders. The global slice gives regularity of \(A\), and the
stated Bhatwadekar--Gupta--Lokhande Theorem 3.5 endpoint gives (3).

When \(A_1\ne0\), the exact field-pencil proof180 forces
\(A_1=d^2/(t+\nu)\) for \(\nu\in\mathbb C\).
Its degree-two extension uses the linear coefficient \(g_1'\)
as well as the two higher coefficients in the pencil contradiction.
The construction182 normalizes the reciprocal expression by an
actual linear change preserving \(XZ+YW\). Its explicit invariant
coordinate and companion again have both polynomial inverse orders.
The same regular-kernel theorem gives (3).

These two slope cases exhaust degrees two through four.
The zero-slope construction does not assume the reciprocal
condition used in the nonzero-slope case.
The older degree-two shear178 remains valid, but this synthesis
no longer needs its three-good recognition156 endpoint.

## 3. Why the generic and original conclusions are different

The parameter \(y\) in (2) need not be an original coordinate.
Its slope \(\gamma=Ny\) may be nonconstant. The determinant in the
\(y\)-parameter is \(-a^3/(Ny)\), not generally \(-a^3\).
The reciprocal proof180 uses actual field return and a full
pencil-degree calculation; it does not omit this factor or treat
the determinant as a rational cube.

The integral conclusions come later from the explicit invariant
coordinates and polynomial companions in179 and182, in all three
degrees. Their formulas allow coefficients to vanish; in the
reciprocal degree-two case its two highest Laurent coefficients
are zero while the remaining quadratic coefficient is nonzero.
The regular-kernel endpoint
is applied only after an ambient invariant coordinate has been proved.
No division by the possibly nonunit original speed \(a\) occurs in
those coordinate inverses.

## 4. Sources and remaining scope

The source proofs used here were read as saved artifacts:

- [Actual split chart175](split-cubic-generic-chart-pass175-working.md), [whole-plane completion175](split-projection-exceptional-cone-pass175-working.md), [constant projection176](split-constant-projection-exclusion-pass176-working.md), [selected component176](split-cubic-simple-selected-component-pass176-working.md), and [affine projection177](split-quadratic-projection-exclusion-pass177-working.md) supply the actual setup and (2).
- [Coefficient normal form178](split-affine-graph-coefficient-normal-form-pass178-working.md) supplies (4), the coefficient equations and the higher-degree field return. Its separate degree-two shear and recognition156 endpoint are not used in this revised synthesis.
- [Zero-slope coordinate179](split-rho-constant-potential-coordinate-pass179-working.md) supplies the first coordinate construction in every degree under consideration.
- [Reciprocal rigidity180](split-nonzero-rho-slope-reciprocal-rigidity-pass180-working.md) and [reciprocal coordinate182](split-reciprocal-slope-invariant-coordinate-pass182-working.md) supply the second.
- The nonlinear recognition uses the exact regular-kernel statement of [Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1), as checked and applied in179 and182. This synthesis imports no additional external theorem and does not recursively audit that theorem's prerequisites.

Graphs of degree zero or one are not resolved by this synthesis.
Other weighted initial ideals, lower initial rank, and unrestricted
coordinate entry are separate questions. No universal bound on the
minimum total E-time degree is asserted.

This unfrozen revision replaces the former degree-two dependency
on156 by the explicit180 extension and the same invariant-coordinate
endpoints179/182. No checker was executed or imported, and no
frozen source, packet or live index was changed. The statement is a
combination of retained working proofs, not historical novelty
clearance, human expert certification, proof-assistant verification,
or a proof of unrestricted cancellation.
