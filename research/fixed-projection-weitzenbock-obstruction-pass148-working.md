# A Weitzenbock quotient placement cannot complete the two projected goods

Fix the projected coordinate placement \(A=\mathbb C[p,y,z]\)
with quotient functions \(p\) and \(q=pz-H(y)\), where
\(\deg H\ge2\). No two algebraically independent rational speeds
in \(\mathbb C(p,q)\) can complete
\(X,\ y+Xf(p,q),\ z+Xg(p,q)\) to an actual coordinate chart
after localization by invariant denominators. The two projected-good
gradients necessarily become dependent at a point of that localization.

This is an obstruction for this fixed placement of the two projected
goods. It does not classify other embeddings of the same quotient
ring, arbitrary changes of projected coordinates, or actual divisor
constant fields. In particular it does not prove that those fields
are always trivial.

## 1. Precise localized statement

Let \(H\in\mathbb C[y]\) have degree \(d\ge2\), and put
\[
\begin{gathered}
A=\mathbb C[p,y,z],\qquad q=pz-H(y),\qquad
S=\mathbb C[p,q],\qquad K=\mathbb C(p,q),\\
f,g\in K,\qquad
J=f_p g_q-f_q g_p\ne0,\\
R=A[c(p,q)^{-1}],\qquad 0\ne c\in S,\qquad f,g\in R,\\
Y=y+Xf(p,q),\qquad Z=z+Xg(p,q)\quad\text{in }R[X].
\end{gathered}
\tag{1}
\]
The polynomial \(c\) may be any common denominator enlarged by
any further nonzero invariant factor. There is no requirement that
\(p\) remain uninverted. In characteristic zero, independence of
\(f,g\) over \(\mathbb C\) is equivalent to the nonvanishing
of \(J\), since \(K\) has separating transcendence basis \(p,q\).

**Claim.** The \(2\times2\) minors of the two rows
\(d_{p,y,z}Y,d_{p,y,z}Z\), with \(X\) held fixed, generate a
proper ideal of \(R[X]\). Consequently there is no
\(W\in R[X]\) such that
\[
\det\frac{\partial(Y,Z,W)}{\partial(p,y,z)}
\quad\text{is a unit of }R[X].
\tag{2}
\]
Every actual localized coordinate completion would have such a unit
determinant: the original coordinate differentials are a basis,
and localization preserves this property. This uses only a necessary
condition, never the converse of the Jacobian condition.

The invariant ring in (1) is the standard triangular-LND quotient.
Indeed \(\delta=p\partial_y+H'(y)\partial_z\) kills \(p,q\).
After inverting \(p\), one has \(A_p=S_p[y]\) and
\(\delta=p\partial_y\). Thus its localized kernel is \(S_p\).
To contract back to \(A\), a reduced expression
\(p^{-m}F(p,q)\), \(m>0\), could be polynomial only if
\(F(0,-H(y))=0\). Since \(H\) is nonconstant, the map
\(\mathbb C[q]\to\mathbb C[y]\) given by \(q\mapsto-H(y)\)
is injective. This contradicts the reduced choice of \(F\), and
proves \(\ker_A\delta=S\). This kernel description alone does
not provide the coordinate completion excluded by (2).

## 2. An explicit critical point over the generic coefficient field

Work temporarily over \(K\). Because \(p\ne0\) there, write
\(z=(q+H(y))/p\) and use \((p,q,y)\) instead of \((p,y,z)\)
for computing the differentials. The determinant of this coordinate
change is \(-p\), so it preserves row rank. The two rows become
\[
\begin{pmatrix}
Xf_p & Xf_q & 1\\
-(q+H)/p^2+Xg_p & 1/p+Xg_q & H'/p
\end{pmatrix}.
\tag{3}
\]
Here the partial derivatives of \(f,g\) hold the other coefficient
variable fixed. Define two polynomials in an independent variable
\(T\) over \(K\):
\[
\begin{gathered}
D(T)=p g_q-H'(T)f_q,\\
F_*(T)=(q+H(T))D(T)+p^2g_p-pH'(T)f_p.
\end{gathered}
\tag{4}
\]

If \(f_q=0\), then \(J=f_p g_q\ne0\). Thus
\(D=p g_q\) is a nonzero constant, and \(F_*\) has degree
\(d\): its leading term comes from \(p g_qH\), while the
\(H'\) term has smaller degree.

If \(f_q\ne0\), then \(F_*\) has degree \(2d-1\), with
leading term from \(-f_q HH'\). Moreover the exact identity
\[
f_qF_*-
\bigl(f_q(q+H)+pf_p\bigr)D=-p^2J
\tag{5}
\]
shows that \(F_*\) and \(D\) have no common root. No assumption
on zeros or ramification of \(H'\) is required.

In both cases, choose a root \(r\) of the nonconstant \(F_*\)
in an algebraic closure \(\overline K\). Then \(D(r)\ne0\).
Set
\[
y=r,\qquad z=\frac{q+H(r)}p,\qquad X=-\frac1{D(r)}.
\tag{6}
\]
Subtract \(H'(r)/p\) times the first row of (3) from its second.
The last entry is zero. The middle entry is
\((1+XD(r))/p=0\), and the first entry is
\(-F_*(r)/(p^2D(r))=0\). Thus all two-by-two minors vanish.

## 3. Why invariant localization cannot remove the obstruction

The prescription (6), together with the unchanged transcendental
coefficient \(p\), defines a \(\mathbb C\)-algebra homomorphism
\(R[X]\to\overline K\). Its image of \(pz-H(y)\) is exactly
the coefficient variable \(q\). Therefore every nonzero invariant
denominator \(c(p,q)\) has nonzero image. The homomorphism is
defined on every localization in (1), including any additional
invariant denominators one chooses.

Its kernel contains all the minors. It cannot contain one, so the
minor ideal is proper. Expanding a three-by-three determinant along
the third row puts every determinant in (2) in that ideal, proving
the claim. A point over \(\overline K\) suffices to prove the ideal
proper; no assertion that the displayed transcendental point is a
complex closed point is needed.

The proof allows all rational \(f,g\) whose denominators are
inverted. It does not allow an additional denominator depending on
\(X\) or on a noninvariant coordinate merely to delete the critical
point. Such a localization is not the selected-speed localization
of the asserted actual chart.

## 4. Relation to an actual dense chart and its limits

In the actual fixed-\(X\) chart139, one has
\(A_s=\mathbb C[y,z,w_0]_{s_0}\),
\(Y=y+\tau X\), \(Z=z+\rho X\), and an actual \(W\)
completing them.[^1] If this specific projected-coordinate placement
has \(p=w_0\), \(q=pz-H(y)\), coefficient field \(K\), and
\(\tau=f(p,q),\rho=g(p,q)\) independent, it satisfies (1)
after inverting a common invariant denominator, including the
selected speed. Equation (2) then rules it out. No original
global slice coordinate is assumed here; it is the relative
fixed-\(X\) presentation that is used.

The leading cofactor is consistent with the proposed quotient but
does not remedy this obstruction. In the order \((p,y,z)\),
\[
\operatorname{Jac}(f,g,\,\cdot\,)
=J\operatorname{Jac}(p,q,\,\cdot\,)
=-J\bigl(p\partial_y+H'\partial_z\bigr).
\tag{7}
\]
It is an invariant multiple of a triangular LND. Thus prescribing
a suitable generic leading derivation and quotient does not ensure
that the lower coefficients form an actual coordinate partial.

The special choice \(f=p,g=q,H(y)=y^2\) has a unit selected
speed row \((1,p,q)\) and dense homogeneous speed cone. Its
critical equations are \(X=-1/p\), \(z=2y/p\), and
\(q=2y-y^2\). Hence even these speed conditions do not replace
coordinate completion. This is an excluded ansatz, not an actual
dense-frame counterexample or a cancellation counterexample.

Constant-linear reorientations of the projected coordinates,
other polynomial embeddings of \(S\) in a three-ring, and general
nontrivial divisor constant fields are not excluded by this note.

## Sources and verification scope

1. [The actual dense Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--2. The fixed-\(X\) localization and actual Jacobian
   necessity used only for the application in Section 4.
2. [Divisor residue bounds147](dense-all-degree-divisor-residue-bound-pass147-working.md),
   Sections 2--4. Motivation for examining triangular quotients
   with possible nontrivial residue constants; the present critical-point
   argument does not depend on that bound.

The argument is an elementary localized Jacobian obstruction.
It invokes no new external classification theorem and makes no
historical novelty claim. Finite symbolic controls, when executed,
check specified coefficient identities rather than the universal
existence-of-a-root argument or all coordinate placements.

[^1]: Source 1. An actual completion forces a unit determinant;
    no implication from unit determinant to an inverse is used.
