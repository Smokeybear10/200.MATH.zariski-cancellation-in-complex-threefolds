# The isolated nodal component cannot have a simple plinth factor

The compatible action on the fixed pinched surface is still not realized in
affine three-space or excluded for all plinth multiplicities. There is a new
all-later-modification obstruction: **its nodal component must occur in the
primitive plinth with multiplicity at least two.** More precisely, the first
quadratic relation of any minimal local slice can never consume its entire
plinth exponent. This does not assume that the unknown ambient ring has a
one-step presentation.

## 1. The unchanged conditional problem

Use the surface and gluing of [pass 33](nodal-plinth-realization-pass33.md):
\[
B_0=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),\qquad d=u^4-1,
\]
\[
R=B_0\times_{\mathbb C[t]^6}\mathbb C[t]^3,\qquad D=u\delta_0.
\tag{1}
\]
The three paired normalization values remain
\((1,i),(1,-i),(-1,i)\), with the original branch labels and scaled
parameters. Set
\[
s=u^2,\qquad S=\mathbb C+d\mathbb C[s],\qquad
T=\ker D=\mathbb C+d\mathbb C[u].
\tag{2}
\]
Thus \(d=s^2-1\) in the normalization of \(S\), and
\[
S\simeq\mathbb C[d,v]/(v^2-d^2(d+1)),\quad v=ds,
\qquad T=S\oplus du\mathbb C[s].
\tag{3}
\]

Assume an actual primitive LND \(E\) on
\(W=\mathbb C[X,Y,Z]\), a prime invariant \(F\), and an identification
\(W/(F)=R\) under which \(\overline E=D\). Let
\(C=\ker E\simeq\mathbb C^{[2]}\). The preceding residue theorem forces
the image \(C/(F)=S\), not the larger restricted kernel \(T\).
Let \(\mathfrak m\subset C\) be the maximal ideal of its node. In particular
\(F\in\mathfrak m^2\).

The full plinth is principal, and the [isolation theorem](odd-realization-pass34.md)
gives
\[
\operatorname{pl}(E)=F^k\beta C,\qquad k\ge1,
\qquad \beta=\kappa+FQ,\quad \kappa\in\mathbb C^*,\ Q\in C.
\tag{4}
\]
Its proof excludes every other plinth component from the entire prescribed
surface. It does not exclude additional disjoint components.

Choose a minimal local slice, meaning \(E(r)=F^k\beta\). Subtracting an
invariant, the [exact first-center theorem](nodal-plinth-realization-pass33.md)
gives
\[
\overline r=du\,b(s),\quad 0\ne b\in\mathbb C[s],
\qquad \overline r^{\,2}=d^2s b(s)^2\in S.
\tag{5}
\]
Every invariant lift \(K\in C\) of the last expression lies in
\(\mathfrak m^2\). The quadratic minimal polynomial of \(\overline r\)
over \(\operatorname{Frac}S=\mathbb C(s)\) is
\(Z^2-d^2s b(s)^2\), since \(s\) is not a rational square.
These facts apply to every minimal slice after its trace subtraction, with
no assumption that \(b\) is constant or nonvanishing at the node branches.

## 2. Removing the other plinth factors without removing the node

Put \(\widetilde C=C[\beta^{-1}]\) and
\(\widetilde W=W[\beta^{-1}]\). Then
\[
\widetilde W/F\widetilde W=R,\qquad
\widetilde C/F\widetilde C=S,\qquad
\operatorname{pl}(E|_{\widetilde W})=F^k\widetilde C.
\tag{6}
\]
The last equality is up to the unit \(\beta\). Localization commutes with
the invariant kernel and with the image-kernel intersection, since its
denominators are invariant. The local-slice theorem gives the actual
inclusion
\[
\widetilde W\subset\widetilde C[F^{-1}][r],\qquad
\widetilde W[F^{-1}]=\widetilde C[F^{-1}][r].
\tag{7}
\]
The localized threefold is smooth and factorial. It is not asserted to be
affine three-space or contractible. No theorem requiring those stronger
properties is reapplied after this localization.

Even all infinitesimal neighborhoods of the prescribed surface are unchanged:
for each \(N\ge1\), \(\beta\) is already a unit modulo \(F^N\), with inverse
\[
\kappa^{-1}\sum_{j=0}^{N-1}(-FQ/\kappa)^j.
\tag{8}
\]
Consequently \(W/(F^N)\to\widetilde W/(F^N)\) is an isomorphism.
This is an exact neighborhood reduction, not an algebraization theorem.

## 3. A denominator-saturation lemma

**Lemma.** Let \(A\subset B\subset A[f^{-1}]\) be domains, with
\(0\ne f\in A\). If the natural map \(A/fA\to B/fB\) is injective,
then \(A=B\).

Indeed injection means \(A\cap fB=fA\). For \(b\in B\), take the
least nonnegative \(n\) such that \(f^nb\in A\). If \(n>0\), then
\(f^nb\in A\cap fB\), so \(f^nb=fa\) for some \(a\in A\).
Domain cancellation gives \(f^{n-1}b=a\), contrary to minimality.
Hence every \(b\) is in \(A\).

No normality, factoriality, finite morphism, or properness hypothesis is
needed. In particular the lemma does not presume that later modification
centers are monogenic or supported at generic points of the divisor.

## 4. The all-tower exhaustion obstruction

**Theorem.** Under Section 1's actual-realization assumptions, for every
invariant lift \(K\) in (5), the exact ambient divisibility order satisfies
\[
\boxed{1\le v_F(r^2-K)<k.}
\tag{9}
\]
In particular
\[
\boxed{k\ge2.}
\tag{10}
\]

Here \(v_F\) is the exponent of the prime \(F\) in the polynomial ring
\(W\), equivalently in \(\widetilde W\). It is finite: otherwise
\(r^2=K\), contradicted by differentiation. Write it as \(\ell\).
At least one \(F\) divides the expression by (5). Differentiation gives
\[
E(r^2-K)=2rF^k\beta.
\tag{11}
\]
If \(r^2-K=F^\ell a\), then \(F^\ell E(a)=2rF^k\beta\).
Since \(F\nmid r\beta\), this proves \(\ell\le k\).

Suppose \(\ell=k\), and form the actual intermediate subring
\[
H=\widetilde C[r,a],\qquad a=(r^2-K)/F^k.
\tag{12}
\]
Its exact presentation, using independent symbols \(R_0,A_0\), is
\[
H\simeq
\widetilde C[R_0,A_0]/(F^kA_0-R_0^2+K).
\tag{13}
\]
For clarity, \(r\) is transcendental over \(C\), as follows by applying
\(E\) to a minimal polynomial relation. The coefficient \(F^k\) and
the polynomial \(R_0^2-K\) are coprime in the UFD
\(\widetilde C[R_0]\): reduction modulo \(F\) of the latter is monic
and nonzero. The linear relation in \(A_0\) is primitive and irreducible,
so its kernel on substitution in the fraction field is precisely the
principal ideal displayed in (13).

Reduction of that presentation yields
\[
H/FH\simeq
\bigl(S[R_0]/(R_0^2-d^2s b(s)^2)\bigr)[A_0].
\tag{14}
\]
This is a domain. In particular the doubled scheme fiber at the node
does **not** make the entire ring (14) nonreduced: irreducibility over
\(\mathbb C(s)\), followed by monic division, proves that its coefficient
ring embeds in \(\mathbb C(u)\) by \(R_0\mapsto\overline r\).

The actual restricted derivation obeys
\[
D(\overline a)=2\kappa\overline r\ne0.
\tag{15}
\]
The field \(L=\operatorname{Frac}(S[\overline r])=\mathbb C(u)\)
is killed by \(D\). Thus \(\overline a\) is transcendental over
\(L\): if it were algebraic, differentiating its separable minimal
polynomial in characteristic zero would give \(D(\overline a)=0\).
Consequently the natural map of (14) into \(R\) is injective.
Equivalently,
\[
H\cap F\widetilde W=FH.
\tag{16}
\]

Since (7) gives
\(H\subset\widetilde W\subset H[F^{-1}]\), the saturation lemma
forces \(H=\widetilde W\). This controls **every** later intermediate
subring simultaneously, not just a selected continuation of (12).

But (13) is singular at every point over the node with
\(R_0=0\), \(A_0\) arbitrary. The partial derivatives of its equation
all vanish there: \(F,K\in\mathfrak m^2\), the \(R_0\)-derivative
is \(-2R_0\), and its \(A_0\)-derivative is \(F^k\).
The factor \(\beta\) equals \(\kappa\) at the node, so these points
were not removed. The relation defines an irreducible threefold
hypersurface, and the Jacobian criterion therefore makes them genuine
singular points. This contradicts the smoothness of \(\widetilde W\).
Thus \(\ell=k\) is impossible and (9) follows.

## 5. The remaining realization gap is not removed

For \(k=1\), every first relation has \(\ell=1=k\), so Section 4 rules
out the entire realization, regardless of any proposed later centers.
For \(k\ge2\), however, the theorem allows \(1\le\ell<k\).
Then
\[
E\big((r^2-K)/F^\ell\big)=2rF^{k-\ell}\beta,
\tag{17}
\]
and its residue is invariant. It need not be transcendental over
\(\mathbb C(u)\). The injectivity used in (14)-(16) is consequently
not available at that stage.

There is no automatic way to choose a better \(K\) to force
\(\ell=k\). Already at the next step one would have to lift an
invariant of the restricted surface from \(T\) back to \(S\), whereas
\(T/S=du\mathbb C[s]\ne0\). The known rank-one nonfree lifting defect
is exactly a reason that this proposed correction cannot be assumed.

A remaining realization must therefore have \(k\ge2\), all minimal
quadratic lifts must have order strictly below \(k\), and subsequent
centers must repair the nodal fiber while respecting this failure of
initial residue injection. Neither existence nor impossibility of such
a tower is proved here. The still more general all-noninvariant
three-generator embedding question is likewise untouched.

## 6. What the primary literature does and does not supply

- [Kaliman's Seattle survey](https://www.math.miami.edu/~kaliman/library/seattle.paper.pdf),
  Section 10, Theorem 10.1 and Remarks 10.2-10.4, was read directly.
  The theorem gives affine-line normalization for each minimal exceptional
  curve component. Remark 10.2 expresses a suspicion of contractibility,
  not a theorem. Its literal whole-curve wording must not be imported as
  a connectedness theorem: even primitive rank-two actions can have
  disconnected plinth support. For example
  \(p(x)\partial_y+2y\partial_z\), with \(p=1-x^2\), has kernel
  \(\mathbb C[x,pz-y^2]\) and full plinth \((p)\), two disjoint lines.
  One can recover the full plinth by the local-slice formula and odd/even
  pole cancellation at the two simple roots of \(p\). This is an old
  triangular control, not a new claim. The componentwise suspicion is
  relevant because a nodal affine polynomial curve is not contractible.
  This audit does not establish the current status of every later
  formulation of that question. Remark 10.4's simple smooth-center tower
  applies when the exceptional curve is a line or disjoint lines, not
  to the present node.

- [Masuda, *Faithfully flat quotient morphisms by Ga-actions on factorial
  affine varieties*](https://arxiv.org/html/2512.06687), Section 3,
  its modification construction, Lemmas 3.3-3.4 and Theorems 3.5-3.6,
  supplies actual finite towers. The global polynomial recursive form
  following Lemma 3.4 has additional factoriality assumptions on the
  residue base and intermediate center rings. Our residue base \(S\) is
  nonnormal and nonfactorial. The trivial-bundle criterion requires the
  finite exceptional invariant map to be birational; ours has degree
  two. Neither conclusion settles the node. No all-tower smoothness
  assertion is inferred from this source.

- [Masuda, *Factorial affine Ga-varieties with principal plinth
  ideals*](https://arxiv.org/html/2312.05455), Theorems 3.8-3.9 and the
  recursive construction leading to them, gives a description after
  inverting an additional invariant \(c\notin(F)\). Such a \(c\) can
  still vanish at the node. The isolation identity \(\beta=\kappa+FQ\)
  removes the other plinth factors everywhere on \(R\), but it does
  not turn every auxiliary \(c\) into a unit at the node.

These are exact source boundaries, not novelty evidence from absence of
search hits. No connectedness or componentwise contractibility theorem
with the required nodal scope was obtained from these sources.

## 7. Verification boundary

The companion [exact control suite](isolated_node_checks_pass35.py)
uses only `unittest` and SymPy. Its five methods check finite polynomial
controls for the lifted nodal norm and singular locus, the derivative
orders, the crucial positive-order residual derivative, the failure of
denominator saturation when the residue map is not injective, and the
finite geometric-series inverse in (8).

Those controls do not quantify over an unknown ambient polynomial
\(F\), every minimal slice, or every possible tower. Those quantifiers
belong to the written proofs, especially the elementary saturation lemma.
Independent AI reconstruction is not expert review or Lean verification.
No novelty or cancellation claim is made.
