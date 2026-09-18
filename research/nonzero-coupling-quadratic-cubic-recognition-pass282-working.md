# Recognition of the supplied nonzero-coupling quadratic-cubic chart

Every actual frame satisfying the nonzero-coupling hypotheses of263
is recognized by the retained proofs and the elementary degree-lowering
argument below. A nonzero quartic top is covered by the two genuine
quartic endpoints and the selected-conic exclusion. With zero quartic
top, either the first projection is constant or an actual monic shear
lowers the cubic coordinate to time degree at most two.

This is a chart-level working theorem, not recognition of every1123
frame or a proof of unrestricted cancellation.

## 1. Exact supplied hypotheses

Retain all actual entry assumptions of
[263](two-affine-quadratic-cubic-whole-plane-cofactor-pass263-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\quad
\deg_E(X,Y,Z,W)=(1,1,2,3),\\
\operatorname{ht}I_{\rm initial}=2,\qquad
\operatorname{shift}(\partial_Z)=3,\qquad
m=k_\lambda\ne0,\quad q'''\ne0.
\end{gathered}
\tag{1}
\]
The ideal is the full weighted initial kernel and the selected partial
is literal. All exact field and actual return hypotheses of258/263
are retained, including \(K=\mathbb C(y,z,w)=L(v)\) and
\(L[y,\psi]=L[v]\). They are not replaced by a formal unit determinant.

By263, \(m_\lambda=0\). With \(F=\ker_L\partial_\lambda\), its
exact field construction gives
\[
[F:\mathbb C(t)]<\infty,\qquad
\ker(\partial_t|_F)=\mathbb C,\qquad q,r,m\in F,\quad m\ne0.
\tag{2}
\]
Primes below refer to the extended t-derivative on \(F\).
Set
\[
e=1/m,\qquad
M=m''/2-(m')^2/m,\qquad
a_4=(q''''-mr''''-4q'''m'/m)/24.
\tag{3}
\]
The whole-plane polynomial \(\mathcal H\) has degree at most four.
For the selected irreducible relation \(G\),263 proves
\[
\mathcal H=\eta G+G^2R_0,\qquad \eta\in L^*,
\qquad G_g=c_0\Lambda^g,\quad g=\deg G.
\tag{4}
\]
Its quartic part and, when that vanishes, cubic part are exactly
\[
\mathcal H_4=a_4U^4,\qquad
\mathcal H_3=U^2(MV+c_3U)\quad\text{if }a_4=0.
\tag{5}
\]
There are no \(UV^2\) or \(V^3\) terms in the literal coefficient
table after \(m_\lambda=0\). This absence is needed in (5).

The working conclusion, subject to the retained proof inputs, is
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{6}
\]

## 2. A nonzero quartic top has no remaining selected component

Assume \(a_4\ne0\). Since \(G\) divides \(\mathcal H\), its degree
lies between one and four and its pure top divides \(U^4\).

If \(g=1\), its direction is \(U\), so \(y\in L\).
The actual commuting-derivation endpoint of263 Section4 recognizes
this case. It constructs an invariant ambient coordinate; no
projected constant is simply promoted to one.

If \(g=2\), a constant y would already give a linear full plane
relation by whole-line generation. Thus y is nonconstant, and all
hypotheses of
[the selected-conic exclusion279](quadratic-cubic-selected-conic-square-obstruction-pass279-working.md)
hold. That configuration is impossible.

If \(g=3\), the square-cofactor term in (4) would have degree at
least six if nonzero. It therefore vanishes, forcing
\(\deg\mathcal H=3\), a contradiction.

For \(g=4\), (4) gives \(\mathcal H=\eta G\). The full coefficient
table bounds the V-degree by two. The exact whole-line alternatives
proved in263 are the affine-first quartic graph and the
quadratic-first quartic component. The former is recognized by
[267](quadratic-cubic-quartic-graph-polynomial-entry-pass267-working.md);
the latter by
[276](quadratic-first-quartic-actual-coordinate-recognition-pass276-working.md).
These endpoints use the actual hypotheses in (1), not an arbitrary
quartic plane curve.

This accounts for every selected degree when \(a_4\ne0\).

## 3. A nonzero mixed cubic top forces a constant first projection

Now let \(a_4=0\), but suppose \(M\ne0\). Formula (5) makes
\(\mathcal H\) exactly cubic, with two distinct linear factors
in its top, of multiplicities two and one.

If \(g=3\), (4) again has \(R_0=0\), and its top would be a
pure cube, contrary to (5). If \(g=2\), \(R_0=0\) since the
square term has degree at least four; then
\(\deg\mathcal H=2\), again a contradiction.
The only possibility is \(g=1\). Now the top of \(G^2R_0\)
supplies the cubic part, so \(\Lambda^2\) divides (5).
Its only repeated line is \(U\). Hence \(y\in L\).

The same actual endpoint263 Section4 recognizes this case.
In particular no cubic or conic component is left over when
\(M\ne0\) and \(a_4=0\).

## 4. The last coefficient case has an actual degree-lowering shear

It remains to consider
\[
a_4=M=0.
\tag{7}
\]
The derivative identity \(e''=-2e^2M\) and the exact constants
in (2) give
\[
e=\alpha t+\beta,\qquad \alpha,\beta\in\mathbb C.
\tag{8}
\]
The two constants are not both zero, since \(e\ne0\).
Put \(R=r-eq\). Using \(e''=0\), direct differentiation and (3) give
\[
R''''=r''''-eq''''-4e'q'''=-24e\,a_4=0.
\tag{9}
\]
Repeated exact integration in \(F\) gives
\[
R=r_0+r_1t+r_2t^2+r_3t^3,\qquad r_i\in\mathbb C.
\tag{10}
\]
This does not assume \(F=\mathbb C(t)\).

Define a homogeneous complex cubic
\[
P_R(X,Y)=r_0X^3+r_1X^2Y+r_2XY^2+r_3Y^3,
\tag{11}
\]
and the actual monic-in-W shear
\[
\boxed{W_*=W-(\alpha Y+\beta X)Z-P_R(X,Y).}
\tag{12}
\]
Its polynomial inverse fixes \(X,Y,Z\) and sends
\(W_*\) to \(W_*+(\alpha Y+\beta X)Z+P_R(X,Y)\).
Both compositions are the identity.

To check its E-degree, use the literal fixed-X expansions from258:
\[
Y=y+tX,\quad Z=z+(q'y+k)X+qX^2,\quad
W=w+\theta X+(r'y+\lambda)X^2+rX^3.
\tag{13}
\]
Their coefficients belong to \(K=\operatorname{Frac}A\), which E
annihilates; \(EX\ne0\). Every term in (12) has degree at most
three in X. Its cubic coefficient is
\[
r-(\alpha t+\beta)q-P_R(1,t)=r-eq-R=0.
\tag{14}
\]
Thus \(E^3W_*=0\), or \(\deg_EW_*\le2\).
No condition on \(n_\lambda\), \(\ell\), the selected degree of G,
or polynomiality of other coefficient functions was used.

The actual coordinates \(X,Y,Z\) retain degrees \(1,1,2\).
There are three exhaustive endpoints:

- If \(\deg_EW_*=0\), this is an invariant actual coordinate.
  Regularity from \(A[u]=B\) permits BGL Theorem3.5.
- If \(\deg_EW_*=1\), the actual frame \((X,Y,W_*,Z)\) has three
  coordinates annihilated by \(E^2\). The completely reread
  [three-good theorem156](three-good-all-degree-recognition-pass156-working.md)
  applies.
- If \(\deg_EW_*=2\), the actual frame has exact degrees1122.
  The completely reread
  [recognition synthesis257](full-exact1122-recognition-synthesis-pass257-working.md)
  applies, without any assumption on its new initial ideal.

Each yields (6). The coordinate \(W_*\) is nonconstant, so its
time degree is a nonnegative integer; there is no missing negative
or identically zero case.

## 5. Composition and exact remaining boundary

The split \(a_4\ne0\), \(a_4=0,M\ne0\), and \(a_4=M=0\)
is exhaustive in the exact coefficient field. Sections2--4 therefore
recognize the entire supplied nonzero-coupling chart (1).
This removes the lower-degree selected components as well as the
genuine quartics within that chart.

The conclusion does not recognize every height-two1123 frame:
smaller selected shifts and charts without the actual258 entry
are not included. Nor does it supply the missing arbitrary-coordinate
reduction. The zero-coupling and \(q'''=0\) arguments in earlier notes
are separate inputs, not silently built into (1).

The new part is the cubic multiplicity split and the actual shear
(12). The endpoints263,267,276,279,156 and257 retain their explicit
working dependencies; this synthesis is not a recursive formal audit
of those historical proofs. The primary invariant-coordinate endpoint
is [Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/pdf/1501.01438).
Its hypotheses were freshly checked in the preceding continuation.

Root completely read the named new endpoint proofs and reread the full
156 and257 syntheses before this composition. The new derivative and
leading-coefficient identities are elementary algebra, not a numerical
test of a conjecture. No saved checker is rerun, imported or compiled
by this proof. No historical novelty, human peer review, proof-assistant
certification, or unrestricted solution is claimed.
