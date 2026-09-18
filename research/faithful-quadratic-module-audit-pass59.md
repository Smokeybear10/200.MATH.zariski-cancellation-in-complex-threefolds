# The fixed-pair quadratic classification and its source scope

The complete [quadratic-module proof](faithful-quadratic-module-pass59.md)
and its one-method checker reconstruct cleanly. The classification
covers every actual quadratic in the specified generic pair, not
only invertible changes of two previously chosen generators.
The independent checker run passed one method in 0.036 seconds,
exit zero. No mathematical correction is requested.

The underlying modification is standard. The exact coefficient
calculation and its combination with necessary actual-frame
identities are the specific results checked here. Neither this
calculation nor the bounded source comparison certifies historical
novelty or a cancellation theorem.

## 1. Independent membership reconstruction

Keep
\[
R=\mathbb C[a,v]_{(a,v-1)},\quad L=\mathbb C(a,v),\quad
\mathcal B=\bigl(R[z]\oplus tR[z]\bigr)[s],\quad t^2=v+az,
\]
\[
X=as+tz,\quad T=t,\quad q=ts+z^2,\quad Y=vX+T.
\]
The monic decomposition is an actual direct sum, and \(v\) is a
unit while \(a\) is not.

Independently write a generic quadratic as
\[
F=\alpha X^2+\beta XT+\gamma T^2+\delta X+\epsilon T+\zeta,
\qquad \alpha,\beta,\gamma,\delta,\epsilon,\zeta\in L.
\]
Expansion in the actual \(s\)-polynomial and monic \(1,t\) basis
gives the exact membership conditions
\[
\alpha,\delta,\epsilon\in R,\qquad
a\beta\in R,\qquad a\gamma+v\beta\in R,\qquad
\zeta+v\gamma\in R.
\tag{1}
\]
For necessity, the \(s\)-coefficient first gives \(a\alpha,a\beta\in R\).
The even constant coefficient gives \(v\alpha+a\beta\in R\);
the unit \(v\) then forces \(\alpha\in R\). The odd constant
coefficient supplies \(\delta,\epsilon\in R\), and the remaining
even coefficients give (1).

Conversely (1) gives the actual expression
\[
F=\alpha X^2+\delta X+\epsilon T+(\zeta+v\gamma)
 +(a\gamma+v\beta)z+(a\beta)q.
\tag{2}
\]
Comparing the generic \(XT\) coefficient, then the \(T^2\)
coefficient, then the remaining monomials proves independence.
Thus the full free rank-six module is exactly
\[
\mathcal B\cap L[X,T]_{\le2}
=R\oplus RT\oplus RX\oplus RX^2\oplus Rz\oplus Rq.
\tag{3}
\]
All rational coefficients are covered. No bounded coefficient
search or premature coefficient-regularity assumption is used.

## 2. The actual compatibility gate

The necessary good-column equations are those of the actual
[generic-pair theorem](generic-bad-pair-pass44.md), whose Schur
complement, Euler, Hessian and linear-gradient derivation was
reread. They use genuine coordinate partials, not just a graph.

For \(f_1=a,f_2=av\), the Euler field is \(a\partial_a\) at
fixed \(v\). The acceleration is \(h=2a^2\alpha\), so its
Euler equation gives
\[
\alpha\in S:=\mathbb C(v)\cap R=\mathbb C[v]_{(v-1)}.
\]
The Hessian specifies the quadratic part as
\[
\alpha X^2+\alpha'XT+\frac{\alpha''}{2}T^2.
\]
In the author's module coefficients this requires exactly
\[
b=a\alpha',\qquad c=v\alpha'+\frac a2\alpha''.
\tag{4}
\]
The constant term must also be retained: substituting (4) into
\(cz+bq\) leaves the regular constant correction
\(-v\alpha''/2\). Each individually compatible quadratic
therefore already belongs to \(R[X,T]\).

For the linear part the homogeneous potential is \(k=a\delta\).
Its Euler equation gives \(\delta\in S\), and its gradient
forces \(\epsilon=\delta'\). This reconstructs
\[
\alpha(v)X^2+\alpha'(v)XT+\frac{\alpha''(v)}2T^2
 +\delta(v)X+\delta'(v)T+\ell(a,v),
\quad \alpha,\delta\in S,\ \ell\in R.
\tag{5}
\]
The converse checks precisely the stated graph identities,
not an ambient coordinate system or every full-frame equation.
Zero quadratic and linear cases are included without division
by their coefficients.

Since \(z=(T^2-v)/a\notin R[X,T]\), any collection of such
functions with the fixed bad pair generates a proper
subalgebra of \(\mathcal B\). No invertible good-generator
matrix is assumed. Indeed \(vz+aq=XT\) already gives
\(\mathcal B=R[X,T,q]\): module generation and algebra
generation are different questions here.

## 3. Exact relation to standard affine modifications

Put \(S_0=R[X,T]\) and \(N=aXT-v(T^2-v)\). Directly,
\[
\mathcal B=S_0[q]=S_0[N/a^2]=S_0[(a^2,N)/a^2].
\tag{6}
\]
This is a principal affine modification in the established
terminology, after invariant localization.[^kz][^freud]
Its polynomial presentation is
\[
\mathcal B\simeq S_0[Q]/(a^2Q-N).
\tag{7}
\]
For an elementary exactness check, \(S_0\) is a UFD and
\(N\bmod a=-v(T^2-v)\ne0\). Thus \(a^2,N\) are coprime.
The linear polynomial in \(Q\) is primitive and irreducible,
hence prime; localization at \(a\) identifies its quotient
with the displayed fraction subring.

The construction in (6)–(7) is standard modification algebra.
Formula (3) is an explicit finite-degree coefficient computation
for it. The cited general statements do not print this particular
module or impose the actual-frame differential constraints.

The relevant saturation condition cannot be suppressed:
\[
T^2-v=az\in a\mathcal B\cap S_0,\qquad T^2-v\notin aS_0.
\tag{8}
\]
Thus the smaller bad-coordinate algebra fails the usual
generating-principle saturation premise. It also does not
contain the entire \(E\)-invariant ring, since \(z\) is absent.

Freudenburg's degree-module algorithm concerns
\(\ker D^{n+1}\) for a specified LND, not automatically the
total-degree intersection (3). All \(z^m\) are \(E\)-invariant,
while their generic total degrees are \(2m\). The source theorem
therefore does not itself identify this rank-six module or solve
the actual-coordinate compatibility question.[^freud]

This comparison is restricted to the already cited modification
and degree-module route. It is not an exhaustive literature
search or an inference of novelty from absent search results.

## 4. Verification and limits

The complete saved proof, including all 24 tagged equations,
and the complete checker were read. The checker imports only
unittest and SymPy, not project solvers. Its independent run
with /opt/anaconda3/bin/python passed one method in
0.036 seconds, exit zero.

That method checks the complete monic expansion, coefficient
extraction, reconstruction and nonzero basis determinant
\(1/a^2\). Universal membership and non-generation are proved
by the written arguments, not inferred from finite sampling.
No full regression was run in this audit.

Only the fixed bad pair and generic quadratic class in the
specified faithful model are classified. Different bad pairs,
higher generic degrees, unrestricted actual-frame reduction
and complex-threefold cancellation remain outside the result.
No file from pass58 or earlier or shared metadata was edited.

## Sources

[^kz]: Shulim Kaliman and Mikhail Zaidenberg,
  [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076v1),
  arXiv:math/9801076v1, 16 January 1998, Definition 1.1,
  Proposition 1.1 and Example 1.6. The construction, complete
  proposition statement and its displayed proof were read
  directly. Part (c) credits E. D. Davis and refers elsewhere
  for its proof; no new reading of those original references
  is claimed. The [author-university publication record](https://scholarship.miami.edu/esploro/outputs/journalArticle/Affine-modifications-and-affine-hypersurfaces-with/991031577249602976)
  identifies *Transformation Groups* 4 (1999), 53–95. A new
  line-by-line journal-version comparison is not claimed.
[^freud]: Gene Freudenburg,
  [*Canonical factorization of the quotient morphism for an affine Ga-variety*](https://arxiv.org/pdf/1602.08786v3),
  arXiv:1602.08786v3, Proposition 2.1 with its full proof,
  Definitions 3.1 and 3.4, Lemma 3.5 with proof, and Section 4
  through Theorem 4.4 and its complete proof. These selected
  primary passages were directly reread. The general
  saturation/modification route was already recorded in
  [pass21](universal-bridge-pass21.md), and its degree-module
  applicability boundary in
  [pass58](coordinate-slice-degree-scope-pass58.md).
