# Excluding the full Artin image by the actual quartic algebra

In the supplied quadratic frame, an actual collapsed mixed fiber with
nonzero speed normal cannot have full second-degree image
W2=D. The proof allows the residual second-image ideal to be any
maximal-primary complete intersection. It does not assume that this
ideal is the reduced maximal ideal.

The conclusion excludes this branch, not the mixed fiber itself.
The remaining smaller second-degree image, the other fiber sectors,
and the entry from an arbitrary sliced action remain separate questions.

## 1. Actual hypotheses and normalized conic

Let R=S_m, with maximal ideal n, be the regular local invariant
surface in the actual mixed (2,1), L(m) nonzero sector. Write A_R
for the faithfully flat domain and N for its primitive locally
nilpotent derivation with full kernel R. We retain
\[
F_j=\ker(N^{j+1}|A_R)\simeq R^{j+1},\qquad
A_R/\mathfrak nA_R=\mathcal D[c_*],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\qquad
A_R=R[F_4].
\tag{1}
\]
The last equality is an actual generation statement: the two relative
good generators belong to F2 and the specified third generator c*
belongs to F4. The generic fiber is a polynomial line. The finite
freeness of the degree modules does not assert their general fiber
injectivity.[^actual]
Write Ij=N^j(Fj), an ideal of the full kernel R.

Assume, for contradiction, that the image W2 is D. Choose a basis
1,z,w of F2 whose whole-fiber residues form a basis of D. The
induced N kills these residues. The normalized image argument gives
a primitive pair a,b and the following exact data:
\[
\begin{gathered}
F_1=R\oplus Rr,\quad r=az+bw,\quad Nr=P\ne0,\quad
J=(a,b),\quad \sqrt J=\mathfrak n,\quad \gcd(a,b)=1,\\
Nz=\epsilon br+B_1,\qquad Nw=-\epsilon ar+B_2,
\qquad P=aB_1+bB_2,\qquad \epsilon\in R^*,\\
Q=\epsilon r^2-2B_2z+2B_1w\in R,\qquad
B_1,B_2,Q\in J^2.
\end{gathered}
\tag{2}
\]
Here a,b are nonzero nonunits. In particular they form a regular
sequence. For clarity, the two crucial inputs behind (2) are these.

First, the exact quadratic divisor classification says that at every
height-one prime p the image ideals satisfy
ord_p I_j=ceil(j/2) ord_p(P). Degree-one constant divisors instead
have an actual slice and all image ideals are units. The primitive
row (a,b) and I2=epsilon P(a,b) therefore force epsilon to be a
unit. The zero residue matrix of N on F2 then gives a²,b² in n,
so J is proper. Coprimality makes it maximal-primary, not necessarily
equal to n.[^normalized]

Second, the residue-basis purity lemma gives
F2 intersect HA_R = HF2 for every ideal H of R. Since r belongs
to JF2, the conic in (2) puts
Q+2B2z-2B1w in J²A_R intersect F2. Comparing the pure basis
1,z,w proves the stated J² coefficients. This is the point where
the nonreduced ideal J itself, rather than merely its radical, is
essential.[^purity]

## 2. Actual quartics from regular-sequence division

Choose coherent expressions
B1=a²c1+ab d1+b²e1, B2=a²c2+ab d2+b²e2,
and Q=a²q1+ab q2+b²q3, with all coefficients in R. In formal
variables Z,W put
\[
\begin{aligned}
Q_{aa}&=\epsilon Z^2-2c_2Z+2c_1W-q_1,\\
Q_{ab}&=2\epsilon ZW-2d_2Z+2d_1W-q_2,\\
Q_{bb}&=\epsilon W^2-2e_2Z+2e_1W-q_3.
\end{aligned}
\qquad
a^2Q_{aa}(z,w)+abQ_{ab}(z,w)+b^2Q_{bb}(z,w)=0.
\tag{3}
\]
Flatness preserves the regular sequences (a,b²) and (b,a²).
Reducing the last identity modulo a and cancelling b² gives
Qbb(z,w) in aA_R. Reducing modulo b and cancelling a² gives
Qaa(z,w) in bA_R. Thus the following are actual elements, not
fractions merely placed in the generic fiber:
\[
\begin{gathered}
U=Q_{bb}(z,w)/a\in F_4,\qquad
V=Q_{aa}(z,w)/b\in F_4,\qquad
aV+bU+Q_{ab}(z,w)=0,\\
N^3U=-6\epsilon^2P\,Nw,\qquad
N^3V=6\epsilon^2P\,Nz,\\
N^4U=6\epsilon^3aP^2,\qquad
N^4V=6\epsilon^3bP^2,\\
T=-\tfrac12(bU-aV)\in F_3,\qquad
g_T:=N^3T=3\epsilon^2P^2.
\end{gathered}
\tag{4}
\]
These derivatives follow directly from (2). The invariant denominators
do not change degree bounds. For example,
N³(w²)=6Nw N²w and N²w=−epsilon aP, which gives the
first cubic derivative in (4).

The height-one formulas imply I3 is contained in P²R: membership
in every height-one localization contracts in the UFD R. The actual
T in (4) gives the reverse inclusion. Hence I3=P²R, and
F3=F2 direct-sum RT. This derives the cubic generator without the
older normalized-cover cubic argument.

## 3. The quartics are a full basis, also for nonreduced J

The independent residues of 1,z,w remain independent in F4/nF4,
so they extend to a basis of F4. Let M=F4/F2 be the resulting
free rank-two module. In a basis of M write the class of T as
t=(c0,d0)^t. The quotient M/Rt=F4/F3=I4 is torsion-free,
so c0,d0 are coprime. The nonzero N4 row on M annihilates t;
coprimality in the UFD makes it h(d0,−c0), with h in R.
At every height-one prime I4 has valuation 2 ord(P). Therefore
h/g_T is a unit theta of R. This uses all local degree modules,
not only the derivative of the specified c*.

Let X be the matrix whose columns are the classes of U,V in M.
Equation (4) gives
\[
\theta(d_0,-c_0)X=2\epsilon(a,b),\qquad
X\binom b{-a}=-2\binom{c_0}{d_0},\qquad
\det X=\frac{4\epsilon}{\theta}\in R^*.
\tag{5}
\]
To check the last equality including its sign, set
J0=((0,1),(-1,0)), ell=(d0,−c0), and
zeta=2epsilon/theta. Then ell X=zeta(a,b). Multiplying
X J0 X^t ell^t in the two ways given by the first two identities
gives −det(X)t=−2zeta t. Since R is a domain and t is nonzero,
the displayed determinant follows.

Consequently F4=F2 direct-sum RU direct-sum RV. In particular
the actual quartic subalgebra is K4=R[z,w,U,V], and its fourth
image is P²J. No step in this basis argument replaces J by n.

## 4. The presentation has no hidden base torsion

Set Sscr=R[Z,W,Uscr,Vscr] and
\[
\mathscr I=(b\mathsf V-Q_{aa},\quad
 a\mathsf V+b\mathsf U+Q_{ab},\quad
 a\mathsf U-Q_{bb})\subset\mathscr S.
\tag{6}
\]
There is a natural surjection Sscr/Iscr onto K4. We prove it is
an isomorphism before drawing a conclusion from its raw closed fiber.

The conic polynomial
f=epsilon(aZ+bW)²−2B2 Z+2B1 W−Q is primitive over R:
its leading coefficients epsilon a², 2epsilon ab, epsilon b²
have no common prime divisor. Over K=Frac(R), use r=aZ+bW
and a complementary linear coordinate. The conic is linear in
the complementary coordinate with nonzero coefficient proportional
to P. It is irreducible and defines K[r]. Gauss's lemma therefore
makes R[Z,W]/(f) a domain, and generic injectivity proves that
this is exactly R[z,w].

After inverting a, the three relations (6) eliminate Uscr and
Vscr, leaving f. The same assertion holds after inverting b.
For every height-one prime p of R at least one of a,b is a unit
in R_p. The exact divisor classification, or the degree-one slice,
gives A_(p)=R_p[F2]. Thus (Sscr/Iscr)_(p) is the actual domain
A_(p). In particular it has no vertical minimal prime over p.

At the closed point define
S0=C[Z,W]/(Qaa_bar,Qab_bar,Qbb_bar). Their leading quadratics
are epsilon_bar Z², 2epsilon_bar ZW, epsilon_bar W². Reduction
of total degree shows that 1,Z,W span S0. The actual residues
zbar,wbar satisfy these equations and give a surjection S0 onto
D, whose dimension is three. Since 1,zbar,wbar are independent,
S0 is exactly D. Hence the raw closed fiber of (6) is
D[Uscr,Vscr], of dimension two.

Every minimal prime of the three-generated ideal Iscr has height
at most three. None contracts to n: a prime containing Iscr+n
has height at least four. Indeed its image in C[Z,W,Uscr,Vscr]
has height at least two by the raw fiber computation, and the
polynomial-fiber height formula over the closed base point adds
height(n)=2. None contracts to a height-one base prime by
the preceding actual localization. All minimal primes therefore
contract to zero. The generic quotient is the single polynomial
line K[r], so Iscr has a unique minimal prime, of height three.

In each localization of the regular ring Sscr at a prime containing
Iscr, its three generators cut out codimension three. They form
a regular sequence; the quotient is Cohen–Macaulay and has no
embedded associated primes.[^cm] Its sole associated prime is
therefore the horizontal minimal prime. Every nonzero element of
R is a nonzerodivisor on Sscr/Iscr. The quotient injects into its
generic localization, where the map to K4 is an isomorphism.
This proves the exact presentation and fiber:
\[
K_4\simeq\mathscr S/\mathscr I,\qquad
K_4/\mathfrak nK_4\simeq
\mathcal D[\mathsf U,\mathsf V],\qquad
\dim(K_4/\mathfrak nK_4)=2.
\tag{7}
\]

## 5. Contradiction and exact scope

By (1), A_R=R[F4]=K4. But its actual whole fiber is D[c*],
of dimension one, contrary to (7). Thus W2 cannot be D in
the actual mixed sector under consideration. Since the retained
second-image dichotomy gives dimensions two or three, its dimension
must be two here.[^image]

This repairs the precise reducedness gate in the older quartic
argument52. Its regular-sequence divisions and presentation proof
work for arbitrary maximal-primary J once purity supplies the
actual J² coefficients and (5) supplies a full quartic basis.
We do not import the old ordinary-triple hypothesis, normalized
trace estimates, or a conclusion J=n. The base ideals need not
define reduced schemes. No general cancellation or recognition
theorem follows from this branch exclusion alone.

The dependency is narrower than the full-Artin matrix argument106.
The present proof does not assume that I4 is nonprincipal or that
I3 is principal. The actual T proves I3=P² directly, and the
height-one row valuations prove theta is a unit. From the normalized
note107 it uses the conic normalization and purity application in
Sections 2 and 4, together with the independent divisor gates.

## Proof and source scope

The author reconstructed the complete retained quartic-fiber52,
quartic-corrections51, cubic-generation51, second-image47,
third-image48, and fourth-image-boundary52 notes. Only the algebraic
presentation mechanism from these notes is reused here. The direct
cubic T and matrix (5) replace the older cubic and reduced-point
gates. Root and General independently reconstructed the outline;
saved-file reviews are separate. These AI reviews are neither human
expert certification nor formal verification, and no novelty claim
is made.

[^actual]: [Degree-module102](quadratic-degree-module-fiber-rigidity-pass102.md), the finite-free degree-module proof; [whole fiber99](quadratic-whole-plane-fiber-pass99.md); and [mixed degree-module image104](mixed-degree-module-artin-image-pass104.md). The actual finite generating set and its explicit F2/F4 bounds are recorded in [third-degree image105](mixed-third-degree-image-pass105.md), in the paragraph beginning “The actual finite generating set A=S[A1,A2,c]”. The supplied relative generators originate in [quadratic cubic-relation90](nonconical-cubic-relation-pass90.md).

[^normalized]: [Normalized image ideals107](mixed-normalized-image-ideals-pass107.md), Sections 2 and 4; [quadratic constant divisor107](quadratic-constant-divisor-filtration-pass107.md); [independent divisor gates107](quadratic-divisor-normal-form-gates-pass107.md); and [degree-one slice105](mixed-cubic-rank-defect-pass105.md), Section 2. The all-height-one quadratic hypotheses use the actual divisor91 and admissible-boundary106 gates recorded in those notes.

[^purity]: [Residue-basis purity107](residue-basis-purity-pass107.md), using the Stacks Project's [Lazard theorem, tag 058G](https://stacks.math.columbia.edu/tag/058G) and [finite-factorization proof, tag 058C](https://stacks.math.columbia.edu/tag/058C). The author freshly read the complete selected statements and displayed proofs on September 14, 2026, not all their deeper flatness dependencies.

[^cm]: Stacks Project, [regular sequence from the expected dimension, tag 02JN](https://stacks.math.columbia.edu/tag/02JN), its [displayed local proof, tag 00N6](https://stacks.math.columbia.edu/tag/00N6), and [no embedded associated primes for a Cohen–Macaulay module, tag 0BUS](https://stacks.math.columbia.edu/tag/0BUS). The complete selected statements and displayed proofs were freshly read, not all deeper dependencies. The older exact presentation and contradiction are [quartic fiber52](quartic-fiber-gate-pass52.md), Sections 3–4.

[^image]: [Mixed degree-module image104](mixed-degree-module-artin-image-pass104.md), the actual dimension-two/dimension-three dichotomy, together with the actual mixed hypotheses of (1).
