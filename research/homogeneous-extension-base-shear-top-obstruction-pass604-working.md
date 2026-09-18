# Fixed-base top obstructions and the global-minimum boundary

Date: 2026-09-17

Status: bounded working proof. Independent saved-source review is required
before canonical acceptance.

## 1. What is decided

For a homogeneous triangular extension whose last coordinate has
LND-degree at least two, an arbitrary polynomial shear fixing the
original three-ring lowers that degree if and only if a single
homogeneous component of the shear does so.
Thus a homogeneous top obstruction can rule out every fixed-base
automorphism, not just the homogeneous shears originally tested.

This local conclusion does not prove that the displayed four-coordinate
frame globally minimizes degree. A polynomial automorphism that changes
the three-ring is outside the fixed-base test. If a separate whole
rectification is supplied, the unrestricted minimum of the coordinate
degree sum is one and the all-positive minimum is four, irrespective of
the fixed-base obstruction.

The note proves both statements, formulates the exact obstruction space,
and checks the replica family motivating the distinction. It does not
claim a general entry theorem, cancellation, or novelty.

## 2. The exact fixed-base test

Let

\[
R=\mathbb C[x,y,z],\qquad
0\ne H\in\operatorname{LND}_{\mathbb C}(R),\qquad
B=R[t],\qquad E=H+(1+\psi)\partial_t.
\tag{1}
\]

No slice is required in this section. The triangular derivation \(E\)
is locally nilpotent, since the derivative sequence of each displayed
generator terminates. For nonzero polynomials, degree means LND-degree;
the zero polynomial has degree \(-\infty\).

If \(1+\psi=0\), then \(t\) is invariant and its degree zero cannot be
strictly lowered by a polynomial coordinate replacement. Otherwise put
\(m=\deg_Et\geq1\). For every \(P\in R\), the entire derivative identities
are

\[
E^jt=H^{j-1}(1+\psi)\quad(j\geq1),\qquad E^jP=H^jP.
\tag{2}
\]

Consequently

\[
\deg_E(t-P)<m
\quad\Longleftrightarrow\quad
H^mP=H^{m-1}(1+\psi).
\tag{3}
\]

There is no extra hidden bound on \(P\) in this equivalence. Applying
\(H\) to the equality automatically gives \(H^{m+1}P=0\).

When \(m\geq2\), one has \(\deg_H\psi=m-1\), and (3) becomes

\[
H^mP=H^{m-1}\psi
\quad\Longleftrightarrow\quad
\deg_H(\psi-HP)<m-1.
\tag{4}
\]

When \(m=1\), the correct condition is instead

\[
HP=1+\psi.
\tag{5}
\]

The constant term in (5) cannot be omitted. A successful replacement
then has degree zero, so it is a descent for unrestricted frames but
not itself an all-positive frame.

Every \(R\)-automorphism of \(R[t]\) is of the form
\(t\mapsto\lambda t+P\), with \(\lambda\in\mathbb C^*\) and \(P\in R\).
Indeed degrees in \(t\) multiply under mutually inverse substitutions
over the domain \(R\), forcing degree one; the linear coefficient is
an \(R\)-unit, hence complex. Scaling by \(\lambda\) does not affect
LND-degree. Thus (3) tests all automorphisms fixing this base pointwise.

## 3. Homogeneous projection and the precise top quotient

Assume now that \(H\) is ordinary homogeneous of derivation degree
\(D\), and write \(R_j\) for the ordinary degree-\(j\) space, with
\(R_j=0\) for \(j<0\). Nonzero polynomial derivations of this kind have
\(D\geq-1\), but no positivity assumption on \(D\) is needed below.
Suppose

\[
\psi\in R_\ell,\qquad \deg_H\psi=m-1\geq1,\qquad q=\ell-D.
\tag{6}
\]

Decompose an arbitrary \(P=\sum_jP_j\) into ordinary homogeneous
components. The nonzero right side of (4) has ordinary degree
\(\ell+(m-1)D\), whereas \(H^mP_j\), if nonzero, has degree \(j+mD\).
Distinct \(j\)'s give distinct ordinary degrees. Hence (4) forces

\[
H^mP_q=H^{m-1}\psi,\qquad H^mP_j=0\quad(j\ne q).
\tag{7}
\]

Conversely a solution \(P_q\in R_q\) is already a solution in \(R\).
We have proved the full equivalence

\[
\begin{split}
&\exists P\in R:\ \deg_E(t-P)<m\\
&\qquad\Longleftrightarrow
\exists P_q\in R_{\ell-D}:\ \deg_H(\psi-HP_q)<m-1.
\end{split}
\tag{8}
\]

In particular, when \(q<0\) or \(q=0\), no such descent is possible:
there is no negative-degree component, and \(H\) kills constants.
For \(q\geq1\), (8) makes no automatic surjectivity assertion.

Here is the exact finite-dimensional obstruction in the fixed grading.
Set \(k=m-1\) and \(\mathcal F_j=\ker H^{j+1}\). Then

\[
\mathcal T_{\ell,k}(H)=
\frac{R_\ell\cap\mathcal F_k}
 {H(R_{\ell-D}\cap\mathcal F_{k+1})
       +(R_\ell\cap\mathcal F_{k-1})}.
\tag{9}
\]

The denominator is a subspace of the numerator. The class of \(\psi\)
in (9) vanishes exactly when (8) holds. The restriction
\(P_q\in\mathcal F_{k+1}\) is essential in this general definition:
without it, \(H(R_{\ell-D})\) need not lie in \(\mathcal F_k\).
Any solution of (4) automatically satisfies that restriction.

For completeness, the degree-one boundary also has a homogeneous
description. If \(m=1\), \(H\psi=0\), and \(0\ne\psi\in R_\ell\) with
\(\ell>0\), (5) is equivalent to the two separate conditions

\[
HP_{-D}=1,\qquad HP_{\ell-D}=\psi.
\tag{10}
\]

All other homogeneous components have zero \(H\)-image. If instead
\(\psi=\lambda\in\mathbb C\), with \(\lambda\ne-1\), the single
condition is \(HP_{-D}=1+\lambda\). This includes \(\psi=0\).
For \(D\geq0\), a nonzero constant is not in \(H(R)\): projection
to degree zero would require a negative-degree polynomial, or a
constant killed by \(H\). Thus (5) has no solution in that case.
The invariant case \(\psi=-1\) was already separated before (3).

## 4. The replica obstruction is complete for its fixed base

Take \(n,q\geq1\) and the original DG family

\[
\begin{gathered}
f=xz-y^2,\quad r=x^{2n+1}+yf^n,\quad
g=\frac{f^{2n+1}+r^2}{x},\\
H_0=\det J(f,g,\,\cdot\,),\quad
M=4n+1,\quad N=8n+2,\quad s=M+1,\\
a=f^s,\qquad c=fg^2,\qquad
H=aH_0,\qquad \psi=cH_0(z^q).
\end{gathered}
\tag{11}
\]

The quotient \(g\) is a whole polynomial:
\(g=zf^{2n}+2x^{2n}yf^n+x^{4n+1}\).
The explicit identities
\[
H_0f=H_0g=0,\qquad H_0r=-f^ng,\qquad
R_{fg}=\mathbb C[f^{\pm1},g^{\pm1},r]
\tag{12}
\]
give the exact degrees
\[
\deg_{H_0}(x,y,z)=(2,4n+2,N).
\tag{13}
\]
For example the inverse formulas are
\(x=(f^{2n+1}+r^2)/g\), \(y=(r-x^{2n+1})/f^n\), and
\(z=(g-2x^{2n}r+x^{4n+1})/f^{2n}\), so these are degrees in the
independent rational variable \(r\). These whole computations also
appear in [pass 601](homogeneous-dg-top-degree-removal-pass601-working.md).

Both \(a,c\) are \(H_0\)-invariant, and their ordinary degrees are
equal to \(2s=8n+4\). Multiplying an LND by a nonzero invariant does
not change its degree function, since \(H^j=a^jH_0^j\). Thus

\[
D=12n+4,\qquad \ell=q+D,\qquad
\deg_H\psi=qN-1,\qquad m=\deg_Et=qN.
\tag{14}
\]

Only \(z\) among \(x,y,z\) has degree \(N\). Hence any \(P_q\in R_q\)
has, for some scalar \(\lambda\in\mathbb C\),

\[
H_0^{qN}P_q=\lambda H_0^{qN}(z^q),\qquad
H_0^{qN}(z^q)\ne0.
\tag{15}
\]

Indeed every other degree-\(q\) monomial has strictly smaller
\(H_0\)-degree, so it contributes zero to this derivative. Condition
(7) would now give

\[
a^{qN}\lambda H_0^{qN}(z^q)
=a^{qN-1}cH_0^{qN}(z^q),
\quad\hbox{hence}\quad a\lambda=c.
\tag{16}
\]

This is impossible: \(f,g\) are algebraically independent by (12),
and \(fg^2\) is not a complex multiple of \(f^s\). All cancelled
factors in (16) are nonzero in the domain.

Therefore no \(P\in R\), of any ordinary degree, strictly lowers
\(\deg_Et\) while fixing the displayed base. This strengthens the
homogeneous no-shear computation by (8), and includes \(q=1,n=1\).
It does not prohibit changing the base three-ring, and does not
by itself prove or disprove the existence of a slice or rectification.
Any whole rectification supplied separately is subject to the next
section, not contradicted by (16).

In particular, the DG theorem in601 and this replica calculation
have different derivations. The former uses \(H_0\), while the
latter uses its nonconstant invariant multiple \(aH_0\).
Neither the full triangular form nor a supplied slice permits
silently dividing \(H\) by \(a\) inside the original extension.

## 5. The full initial test for a single coordinate

There is an analogous exact criterion without homogeneity or a stable
base. Let \((X_1,\ldots,X_4)\) be any actual polynomial frame for
a nonzero LND \(E\), and let
\[
R_i=\mathbb C[X_1,\ldots,\widehat{X_i},\ldots,X_4],
\qquad d_i=\deg_EX_i>0.
\tag{17}
\]
Filter both \(B\) and \(R_i\) by their actual \(E\)-degree. Inclusion
induces an injective map of their associated graded rings. Then

\[
\exists P\in R_i:\ \deg_E(X_i-P)<d_i
\quad\Longleftrightarrow\quad
\operatorname{in}_E(X_i)\in
\operatorname{image}\bigl(\operatorname{gr}_{d_i}R_i
                          \longrightarrow\operatorname{gr}_{d_i}B\bigr).
\tag{18}
\]

Both implications just lift the equality of degree-\(d_i\) classes.
Every replacement \(X_i\mapsto X_i-P\) is an actual polynomial
automorphism fixing the other three coordinates. The criterion
uses the full associated graded algebra of \(R_i\), including
initials revealed by cancellation inside its polynomials. It is
not enough to test the algebra generated only by the three
displayed coordinate initials.

Global minimality of the unrestricted degree sum forces failure
of (18) at every positive-degree coordinate. Conversely, failure
for one coordinate, or for one fixed base as in (16), does not
assert global minimality. A degree-zero replacement is permitted
in this unrestricted statement; if only all-positive frames are
allowed, that particular replacement leaves the allowed class.

## 6. What whole rectification implies about minima

Assume now \(Eu=1\) for some polynomial \(u\). Define the unrestricted
minimum
\[
\mu(E)=\min_{\text{actual frames }(X_1,\ldots,X_4)}
           \sum_{i=1}^4\deg_EX_i.
\tag{19}
\]
It exists as a minimum of a nonempty subset of nonnegative integers.
It is at least one, since a nonzero derivation cannot kill a full
generating frame. The elementary equivalence is

\[
\mu(E)=1
\quad\Longleftrightarrow\quad
E\ \hbox{is polynomially conjugate to }\partial_u
\quad\Longleftrightarrow\quad \ker E\simeq\mathbb C^{[3]}.
\tag{20}
\]

For the forward implication, a minimizing frame has three invariant
coordinates \(Y_1,Y_2,Y_3\) and one degree-one coordinate \(T\).
Write \(ET=b\). The identity \(E^2T=0\), together with
\(E=b\partial_T\), implies \(\partial_Tb=0\) in the domain.
Then \(1=Eu=b\,\partial_Tu\) forces \(b\in\mathbb C^*\), giving
the displayed conjugacy after scaling \(T\). Conversely a whole
rectification gives an actual frame with degrees \((0,0,0,1)\).
The kernel equivalence also follows directly from the slice
identity \(B=(\ker E)[u]\).

All-positive actual frames exist: starting with any frame, choose
one coordinate of positive \(E\)-degree and add it to each invariant
coordinate, keeping the other coordinates unchanged. These are
invertible shears. Consequently the all-positive minimum \(\mu_+(E)\)
is defined and is at least four.

If a whole rectification has been supplied, an invariant-coordinate
frame \((Y_1,Y_2,Y_3,u)\) gives the actual positive frame
\((Y_1+u,Y_2+u,Y_3+u,u)\), with every degree equal to one. Hence

\[
\text{whole rectification supplied}
\quad\Longrightarrow\quad
\mu(E)=1,\qquad\mu_+(E)=4.
\tag{21}
\]

No converse from \(\mu_+(E)=4\) is asserted here. Nor does a
displayed positive frame of larger degree certify either minimum.
For (11), the displayed frame and its uniform base-linear variant
have profiles
\[
(2,4n+2,N,qN),\qquad(N,N,N,qN),
\tag{22}
\]
both with sums larger than four. If that extension is separately
rectified by a whole polynomial map, (21) proves that these frames
are not globally degree-minimizing, despite their complete fixed-base
obstruction. This conclusion is conditional on that supplied map;
no unfinished rectification source is a proof input to this note.

## 7. The exact missing bridge

To invoke a top-removal theorem against a globally minimizing
frame, an argument must place that actual minimizing frame in
the theorem's hypotheses. For the DG statement601, these include
an actual \(E\)-stable polynomial omission ring, the specific
unmultiplied derivation \(H_0\) on it, ordinary homogeneity of the
extension coefficient, and the stated degree relation. None is
supplied just by choosing a degree minimum.

More generally, one needs a vanishing statement for the actual
class (9), or the full membership in (18), in an allowed minimizing
frame. The replica calculation proves that this vanishing cannot
be inferred from the homogeneous extension formula alone. A
separate rectification may bypass the obstruction by moving the
base rather than killing that class.

Thus the example is a boundary for a fixed-base reduction rule,
not a counterexample to a theorem restricted to globally minimizing
frames. It also does not establish such a theorem. The unresolved
step is actual entry with degree control, not the distinction
between homogeneous and arbitrary fixed-base shears, which (8)
settles exactly.

No canonical file was edited and no saved checker was executed,
imported, or compiled in preparing this proof.
