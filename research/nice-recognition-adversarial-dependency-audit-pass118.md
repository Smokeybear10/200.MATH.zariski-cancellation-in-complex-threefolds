# Adversarial audit of the nice-slice recognition endpoint

No invalidating gap was found in the portions reconstructed below.
This is a bounded dependency audit of the working
[nice-slice theorem80](nice-slice-recognition-pass80.md), not a new
recognition theorem, a complete reconstruction of every cited result,
or a formal certificate. It checks the endpoint used by
[the quadratic shear117](quadratic-velocity-shear-pass117.md).
The explicit shear and its recognition endpoint remain distinct claims.

## 1. Homogenization and the correct incidence hypothesis

The complete [no-apex proof80](nice-no-apex-quadric-pass80.md) and
[quadric recognition80](nondegenerate-quadric-nice-recognition-pass80.md)
were read through EOF. The rank74, leading76, apex76 and common-top79
arguments were also read, with the following gates reconstructed.

The original slice is essential to exclude a highest adjoint parallel
to the action. The Laurent-parameter restriction and quotient in
[vertical69](vertical-top-exclusion-pass69.md) are genuinely locally
nilpotent, before specialization. Together with the actual inverse
flow, this gives the square-nonzero Jordan type (3,1) and
P outside the image of its Jacobian J. Ordinary rank two alone would
not give the augmented rank three used next.

For the homogenized velocity H=(z^d P(x/z),0), its full Jacobian has
rank three. The slice prevents zeros on z nonzero. At least one
degree-d leading form is nonzero, so the zero set has dimension at
most three. The homogeneous flow identity gives H(H)=0. Consequently
the irreducible three-dimensional image closure W is an actual
component of the zero set. This argument does not classify its other
components and does not need Corollary 6.4 or Lemma 6.1 of de Bondt.

The exact published input is de Bondt's Definition 3.7 and
Theorem 3.8(i): a homogeneous complex quasi-translation of Jacobian
rank between 2 and (n+1)/2 has intersecting GN-planes through any
two points of its image closure. GN-planes are two-dimensional
linear subspaces of its zero set. Here n=5 and the rank is 3.
[Primary statement and proof](https://arxiv.org/html/1501.04845v3#S3).

Removing W's intersections with all other components leaves a dense
conical open. A plane through one of its points belongs to W because
an irreducible plane in a finite union of components lies in one of
them. Thus projectivization really gives lines on the selected surface,
not on an unspecified component. The extra component restriction is
also discussed in the source's Remark 3.11.

The source's generic independent-pair proof already suffices: if its
nonzero common direction is proportional to one selected point, the
plane spanned by the two selected points serves for both. Extension
to nongeneric pairs is unnecessary for this application. In particular
the argument never invokes a five-variable theorem requiring absence
of all linear invariants; the homogenizing coordinate is invariant.

## 2. The projective step does not assume a smooth surface

The apex76 row-space proof identifies constant good directions with
translation-apex directions. Hence in the no-good branch the
irreducible projective surface X in P3 is neither a plane nor a cone.
This uses density of the cone over P's image, not dominance of P onto
that three-dimensional cone.

The elementary incidence lemma in no-apex80 survives the following
challenges. Infinitely many lines through one point would form a
positive-dimensional projective family whose closed union is X,
making X a cone. Thus the point fibers of every line-family incidence
are finite. Each positive-dimensional component of the line space is
a curve and covers X. If its generic incidence degree exceeded one,
the off-diagonal incidence would dominate the product of that curve
with itself. Closedness of line intersection would make every pair
intersect, forcing a plane or cone. Characteristic zero is used to
count distinct points after restricting to a generic open.

One family cannot supply the required intersecting lines through
general pairs. Two distinct covering families meet pairwise across
the families by the same dimension argument. Three pairwise skew
lines in one family exist because its intersection relation is a
proper closed subset of the product. Lines meeting all three lie on
the explicit smooth determinant quadric. The second family covers X,
so X is that quadric. No initial normality or smoothness of X, no
classification of singular ruled surfaces, and no use of recognition
itself enters this reasoning.

## 3. The quadric-to-kernel step uses actual generation

The common highest field is an actual polynomial LND obtained by
primitive division of the highest adjoint columns. Their coefficient
invariance and Jacobian annihilation are both needed for commutation.
Its intrinsic restriction is nonzero because a zero restriction would
make it rationally parallel to the original action.

Once the intrinsic plane and faithful flatness are supplied, the
slice contracts the velocity unit ideal to that plane. The Segre
factorization then uses actual Bezout identities, not gcd one in place
of a unit ideal. Its determinant-one matrix supplies the exact
relative hypersurface presentation and original-coordinate recovery.

The five-by-five generation determinant is a unit modulo the relation.
This does not infer coordinates from a nonzero Jacobian. The four
original differentials form a basis of the quotient differential
module; the conormal map is injective because a partial derivative
of the irreducible relation is nonzero modulo it and the quotient is
a domain. These five lifted vectors are a basis, so their determinant
is a unit of the actual polynomial four-ring, hence a complex constant.

The slice coefficient gives the affine saddle derivation in quadric80.
Its linear part is invertible over the base fraction field. After an
affine translation, irreducible eigenpolynomials are affine lines or
polynomials in the product of the two eigen-coordinates. The latter
case would give either reducibility or a nonconstant unit in the
actual generic polynomial line. Thus the relation is affine-linear.
Nonempty curve fibers then make its coefficient pair unimodular over
the whole plane. This last global step is not descent of a generic
coordinate by itself.

## 4. The other branches and the external boundaries

The complete good-direction79, omission76, binary descent77,
conormal77, normal-syzygy78, Wronskian78, relative hypersurface78 and
relative quadratic79 notes were read. Their supplied-good route keeps
its actual partial, common invariant plane and polynomial reconstruction.
Its final coefficient self-divisibility uses that original partial's
local nilpotence, not a rationally altered derivation.

The separate source input is de Bondt's Theorem 5.1(iv), under component
gcd one, independence of the fifth output, and no two independent
linear invariants. Its invariant-omission conclusion applies here with
exactly the homogenizing linear invariant. The whole displayed theorem
proof was freshly read, including both cases of (iv).
[Primary text](https://arxiv.org/html/1501.04845v3#S5).
The cone product verifies output independence; it is not inferred
merely from an ordinary Jacobian rank.

The homogeneous binary-parameter input was checked in the retained
primary thesis text, Theorem 4.3.1 and its full displayed proof, printed
pages 87--89. The application is over C and needs coprime equal-degree
homogeneous parameters, not the optional irreducibility refinement.
The rational Luroth input was read as a statement, not re-proved from
Igusa. The original PDF endpoint was unavailable on this new access
attempt; the previously retained PDF extraction was used.
[Original thesis URL](https://webdoc.ubn.ru.nl/mono/b/bondt_m_de/homokema.pdf).

The intrinsic quotient theorem uses Kaliman--Saveliev, Lemma 2.1,
Theorem 2.7 and Corollary 2.8(2). They concern a smooth contractible
affine threefold with a nontrivial additive action, not an already
polynomial threefold. The cylinder supplies smoothness, contractibility
and domination by an affine three-plane. The nonempty curve fibers
and regular target give faithful flatness by miracle flatness.
The selected statements and displayed proofs of 2.7 and 2.8 were
freshly read. Their deeper topology and surface-classification inputs,
including Taubes, were not reconstructed here.
[Author-hosted primary paper](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf).

The separately retained all-double-adjoint recognition theorem and
the original-slice/invariant-coordinate endpoint in the linear-cone
case were not re-audited through their entire dependency trees in this
turn. Neither the original Igusa proof nor every algebraic-geometry
reference in de Bondt was re-read. These are explicit audit boundaries,
not newly detected defects. The primary proofs read here do not turn
the whole working theorem80 into a published theorem.

## 5. Evidence and verdict

Full core saved-file reads: 9af748, 9e3983, 9324b6; good-direction
and binary-chain reads: a00c98, 43eca7, 7bfd3f, a06b04. The remaining
rank74 and relative-quadratic79 tails were read in 43eca7. Primary
de Bondt 3.1--3.4, 3.7 and 3.8 were read in 6b2a84 and checked
against HTML; 5.1 in 43eca7; thesis 4.3.1 in 557de6.
Kaliman--Saveliev selected reads are recorded separately above.

No dimension, component, actual-generation or circularity defect was
found in the reconstructed routes. That supports retaining117's
recognition endpoint with its existing working-theorem qualification.
It does not certify the full dependency tree, establish historical
novelty, resolve the cubic relative branch, or produce a nice frame
for an arbitrary sliced action. No test was executed and no file
through117 was modified in this audit.
