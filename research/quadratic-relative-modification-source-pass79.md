# What the relative quadratic equation does not imply by itself

The actual equation derived in pass79 lies in a family that already
contains the Russell cubic. Consequently the equation, smoothness,
factoriality, contractibility and a flat plane quotient are not an
absolute recognition theorem. The cylinder hypothesis must not be
silently assigned to that example.

This source boundary is separate from the stronger original-partial
cofactor argument. That argument retains information which an
arbitrary relative quadratic equation does not have.

## 1. The equation-level question

Consider
\[
S=\mathbb C[u,v],\qquad
A=S[Y,Z]/(F),\qquad
F=aZ+bY^2+cY+d,\qquad
a,b,c,d\in S,\quad a\ne0.
\tag{1}
\]
The proposed absolute question additionally assumes that A is smooth,
factorial and contractible, that \(A[s]\simeq_{\mathbb C}\mathbb C^{[4]}\),
and that a primitive nonzero S-LND has kernel S with faithfully flat
nonempty curve fibers.

The [earlier source note](relative-hypersurface-source-gates-pass79.md)
already separates an S-retraction and geometric divisor integrality
from these assumptions. Neither relative condition is necessary for
an absolute polynomial three-ring, as its Weitzenbock control shows.
The present note therefore does not reuse either condition as an
unproved consequence.

## 2. A quadratic modification boundary with an actual plane quotient

The Russell cubic has the presentation
\[
R=\mathbb C[u,v,Y,Z]/(u^2Z+Y^2+v^3+u),\qquad S=\mathbb C[u,v].
\tag{2}
\]
It is a smooth contractible threefold not isomorphic to affine
three-space.[^russell] The following checks identify exactly how
much of (1)'s extra structure it possesses.

The relation is irreducible: it is primitive and linear in Z over
\(\mathbb C[u,v,Y]\). Its u and Z partials cannot vanish
simultaneously on the hypersurface, since the latter is \(u^2\)
and the former is \(2uZ+1\). Thus smoothness also follows directly.
The element u is prime because
\(R/uR=\mathbb C[v,Y,Z]/(Y^2+v^3)\) is a domain.
Moreover \(R_u=\mathbb C[u,u^{-1},v,Y]\) is a UFD.
The prime-localization criterion for factoriality therefore gives
that R is a UFD; R is Noetherian, so the required factorization
existence holds.[^nagata]

Define
\[
D=u^2\partial_Y-2Y\partial_Z,\qquad
Du=Dv=0,\qquad
DY=u^2,\quad DZ=-2Y,\quad D^2Z=-2u^2,\quad D^3Z=0.
\tag{3}
\]
This is a nonzero LND on R. It is primitive, since u is prime and
does not divide Y. After inverting u its kernel is
\(\mathbb C[u,u^{-1},v]\). The intersection of that ring with R
is S: if a numerator in S acquires a power of u as a divisor in R,
reduction modulo u, using the injectivity of
\(\mathbb C[v]\to R/uR\), removes that power already in S.
Induction on the denominator exponent proves the assertion.
Hence \(\ker D=S\).

The relation is monic in Y, so R is free of rank two over S[Z]
and consequently faithfully flat over S. Every closed fiber is
a nonempty curve. For \(u_0\ne0\), Z can be eliminated. For
\(u_0=0\), the fiber is
\(\mathbb C[Y,Z]/(Y^2+v_0^3)\), including its nilpotents when
\(v_0=0\).

Nothing here establishes \(R[s]\simeq\mathbb C^{[4]}\).
The January 2025 Dubouloz--Ghosh primary paper explicitly retains
the affine-space status of the corresponding cylinders as a
potential cancellation-counterexample question.[^cylinder]
Thus (2) is not a counterexample to the full cylinder hypothesis.
It is a concrete warning that recognition from the quadratic form
plus the other listed geometric assumptions would require a
substantial additional argument. The preserved nice action and
original good partial have not been supplied on this model.

## 3. An exact primary recognition criterion and its extra premises

Ghosh--Gupta--Pal, Theorem 4.8, treats the univariate-denominator
family, including
\[
R_G=\mathbb C[x,L,R_1,R_2]/
       \bigl(\alpha(x)L-G(x,R_1,R_2)\bigr),
\qquad \deg\alpha\ge2,
\tag{4}
\]
assumed to be a domain. Its equivalent conditions include
\[
\begin{aligned}
R_G\simeq\mathbb C^{[3]}
&\Longleftrightarrow
\bigl[R_G^{[n]}\simeq\mathbb C^{[n+3]}
 \text{ for some }n>0,\ \operatorname{ML}(R_G)=\mathbb C\bigr]\\
&\Longleftrightarrow
\bigl[R_G^{[n]}\simeq\mathbb C^{[n+3]}
 \text{ for some }n>0,\ \operatorname{DK}(R_G)=R_G\bigr].
\end{aligned}
\tag{5}
\]
It also requires, equivalently, that every root specialization
\(G(\lambda,R_1,R_2)\) be a plane coordinate.[^ggp]

The invariants in (5) belong to the unstabilized algebra.
Knowing their values on its cylinder does not establish these
conditions. Nor does a general coefficient \(a(u,v)\) in (1)
become univariate by renaming variables. An actual allowable
coordinate change and the missing unstabilized condition would
need proof before this criterion could be applied.

## 4. Why the original-partial endpoint is different

The [actual quadratic-generation proof](relative-quadratic-generation-pass79.md)
retains the original global LND \(T=\partial_w\), not merely (1).
Its exact cofactors show that T(a) belongs to aB. The LND degree
argument forces T(a)=0. Since \(a\in S\subset\ker E\), the
retained nonlinear-branch
[invariant-omission theorem](nice-good-direction-invariant-omission-pass76.md)
then forces \(a\in\mathbb C^*\). Eliminating Z is therefore
justified using the original frame.

This explains why the separately proved
[recognition endpoint](nice-good-direction-recognition-pass79.md) is not an
application of (5), a claim about all quadratic modifications, or
an assertion that the Russell cylinder has been classified. The
omission theorem is conditional on the supplied good direction
and the precise nonlinear velocity-cone branch.

## 5. Reading scope

The earlier quadratic-slice, cubic-postproof and cylinder source
notes were inspected for deduplication. The jointly affine-linear
hyperplane theorems and restricted residual-coordinate criteria
recorded there are not promoted to a theorem about (1).
The already excluded withdrawn arXiv:1502.01849v2 is not used.

This note records selected primary statements and their exact
applicability limits, together with the explicit algebra in
Section 2. No complete literature-exhaustion, new numerical test,
novelty, human expert verification or formal verification is
claimed. Files through pass78 and shared metadata are unchanged.

[^russell]: Adrien Dubouloz, Lucy Moser-Jauslin and Pierre-Marie Poloni,
[*Inequivalent embeddings of the Koras--Russell cubic threefold*](https://arxiv.org/pdf/0903.4278),
abstract and introduction, printed pp. 1--2. These passages were
freshly read for the smooth, contractible, non-affine-three-space
statement; the original topological and Makar-Limanov proofs cited
there were not freshly reconstructed. The quotient, derivation,
kernel and flatness checks are supplied above.

[^nagata]: The Stacks Project, [Lemma 10.120.7, tag 0AFU](https://stacks.math.columbia.edu/tag/0AFU),
Nagata's criterion for factoriality. Its complete displayed
statement and proof were freshly read; it is used with the
multiplicative set generated by the prime element u.

[^cylinder]: Adrien Dubouloz and Parnashree Ghosh,
[*Algebraic families of higher dimensional \(\mathbb A^1\)-contractible
affine varieties non-isomorphic to affine spaces*](https://arxiv.org/pdf/2501.09613),
v1, 16 January 2025, introduction, printed p. 1.
The displayed cylinder-status discussion was freshly read.
The retained [cylinder note](cylinder-route.md) records the exact
family and its Russell specialization. This is a dated primary
statement, not a claim of exhaustive later literature coverage.

[^ggp]: Parnashree Ghosh, Neena Gupta and Ananya Pal,
[*On the family of affine threefolds \(a(x)y=F(x,z,t)\)*](https://arxiv.org/pdf/2403.17397),
v2, 3 August 2024, Theorem 4.8, printed p. 16.
The complete displayed theorem and proof, Corollary 4.2 and its
proof, and Lemmas 4.3--4.5 and their displayed proofs were freshly
read. The proof explicitly retains the ML/DK premise through
Corollary 4.2; the longer invoked Theorem 4.1 and all external
dependencies were not newly audited in full. This is a primary
preprint, with no journal-publication claim made here.
