# Cubic correction and cuspidal repeated fibers

The quadratic-divisor approach now places stronger restrictions on
both remaining stages. At a reduced second-image obstruction point,
flatness forces a genuine cubic element and makes the third image
principal. A full-rank first-order coefficient configuration would
give the entire algebra with an impossible translation-line fiber,
so that configuration is excluded.

After the separate global-equation obstruction vanishes, a smooth
reduced plinth support can still have repeated factors. Contractibility
then forces the quadratic residue on each component to be a pure
odd power of one linear polynomial. The remaining singular residues
are cusps on repeated components, not arbitrary one-branch covers.

Neither deduction resolves the unrestricted cancellation question.
The first retains lower-rank and nonreduced obstruction points.
The second assumes that the global quadratic equation already exists.
The known Russell cubic explains why additional cylinder information,
beyond topology and image-ideal principality, is essential.

## 1. Working question and inherited hypotheses

The working interpretation remains
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
This is the corrected complex-threefold interpretation, not a
professor-confirmed correction of the supplied dimensional typo.
No theorem over arbitrary fields or in arbitrary dimensions is asserted.

In the established independent degree-two branch there is an actual
primitive locally nilpotent derivation \(D\) on \(A\), with
\[
C=\ker D\simeq\mathbb C[U,V],\qquad
D(A)\cap C=pC,\qquad Dr=p,\qquad
F_n=\ker D^{n+1}.
\tag{2}
\]
The invariant inclusion is faithfully flat and factorially closed.
The unknown ring is smooth and factorial, and its complex points
are contractible by (1). Its embedded height-one base localizations
give the complete quadratic divisor models and reconstruct \(A\).
These are hypotheses already established for this branch, not a
universal construction for arbitrary cancellation candidates.

The second image has the form \(I_2=pJ\), where \(p\in J\) and
\(J\) has finite support. At a closed point, \(J\) is proper
exactly when the actual minimal slice becomes scalar in the full
scheme-theoretic fiber. Moreover \(J=C\) is equivalent to an
actual global quadratic equation based on that minimal slice.
The [preceding report](deep-pass-47.md) and its linked proofs
retain these statements and their exact scope.

One additional inherited topological gate is used below: a full
reduced affine-line quotient fiber with nonzero induced translation
lies outside the primitive plinth support. Its proof is an explicit
extension of the published quotient and peripheral-cycle geometry
to the unknown smooth contractible cylinder factor.[^1]

## 2. The local obstruction and its cubic correction

At an obstruction point write
\(R=C_{\mathfrak m}\), \(\mathfrak n=\mathfrak mR\) and
\(\mathcal A=A\otimes_C R\). The exact vector-bundle construction,
after an invariant translation of the local minimal slice, gives
\[
F_2=R\oplus Rz\oplus Rw,\qquad
r=az+bw,\qquad J_R=(a,b).
\tag{3}
\]
The elements \(a,b\) form a regular sequence. The action and conic
equation are
\[
Dz=\epsilon br+B_1,\quad Dw=-\epsilon ar+B_2,\quad
p=aB_1+bB_2,\quad\epsilon\in R^*,
\tag{4}
\]
\[
\epsilon r^2-2B_2z+2B_1w=Q\in R.
\tag{5}
\]
The preceding flat-conic argument gives
\(a,b,B_1,B_2,Q\in\mathfrak n\) and \(p\in\mathfrak nJ_R\).

For the cubic construction assume
\[
B_1,B_2\in J_R.
\tag{6}
\]
This is automatic when the local obstruction scheme is reduced,
so \(J_R=\mathfrak n\). It is an additional hypothesis at a
nonreduced point. Faithful-flat contraction of (5) then gives
\(Q\in J_R\), and invariant coefficients can be chosen with
\[
B_1=ac+bd,\qquad B_2=ae+bf,\qquad Q=aq+bh.
\tag{7}
\]

Define
\[
G=\epsilon rz-2ez+2cw-q,\qquad
H=\epsilon rw-2fz+2dw-h.
\tag{8}
\]
The exact relation is \(aG+bH=0\).
Flatness preserves the regular sequence \(a,b\).
Reduction modulo \(b\) therefore makes \(G\) divisible by \(b\)
inside \(\mathcal A\), not merely in its fraction field.
Cancellation supplies
\[
G=bt,\qquad H=-at,\qquad t\in\mathcal A.
\tag{9}
\]
The products \(rz,rw\) have derivation degree at most three.
Consequently \(D^4t=0\), while direct differentiation gives
\[
D^3t=3\epsilon^2p^2\ne0.
\tag{10}
\]

Every inherited quadratic divisor model has third image generated
by \(p^2\), up to a unit. Divisibility at every height-one base
prime contracts in the UFD \(R\), giving the upper inclusion
\(I_3R\subseteq p^2R\). Equation (10) attains it. Subtracting the
appropriate invariant multiple of \(t\) from any element of \(F_3\)
now proves
\[
\boxed{I_3R=p^2R,\qquad F_3=F_2\oplus Rt.}
\tag{11}
\]
Thus the third image can be principal even at a point where the
second image is not. No monotone propagation of image-ideal
nonprincipality is assumed.

## 3. A full-rank coefficient configuration gives a contradiction

Differentiating (9), cancelling in the domain, and using (5) gives
\[
\begin{split}
Dt={}&\epsilon Q
+\epsilon\bigl(a(e+2d)+3bf\bigr)z\\
&+\epsilon\bigl(-3ac-b(d+2e)\bigr)w
+2(cf-de).
\end{split}
\tag{12}
\]
Its closed-fiber value is the constant \(2\overline{cf-de}\).
The residue determinant is independent of the representations
in (7), since their differences are regular-sequence syzygies.

Suppose this determinant were nonzero. In \(S=R[Z,W,T]\), use
\(r=aZ+bW\) to form the two relations
\[
I=(bT-G,\ aT+H).
\tag{13}
\]
They map to zero in the actual cubic subalgebra
\(K=R[z,w,t]\). The assertion \(K=S/I\) requires a proof.

At every height-one base prime, at least one of \(a,b\) is a
unit. Eliminating \(T\) yields the already known full conic model.
Thus the generic localization is a domain, and no minimal
component can lie over a height-one base prime.
Over the closed point the two equations become independent
affine-linear equations in \(Z,W\), leaving \(\mathbb C[T]\).
Their common vanishing with \(\mathfrak n\) has height four in
\(S\), so a minimal prime of the two-generated ideal cannot
lie over that point either.

There is therefore one generic minimal prime, of height two.
The two generators form a regular sequence in the regular ring
\(S\). Cohen-Macaulayness excludes embedded associated primes,
and generic reducedness gives the exact domain presentation.
At both the generic and closed points of its fiber line, the
local dimensions are those required by miracle flatness.[^2]
Hence \(K\) is flat over \(R\).

A flat module over a UFD is its embedded intersection of
height-one localizations. Since \(K\subseteq\mathcal A\) and
they agree at all those localizations, \(K=\mathcal A\).
The full fiber is consequently a reduced affine line, and (12)
acts there by a nonzero constant translation. The pointwise
plinth criterion contradicts \(p\in\mathfrak n\).

This proves the precise exclusion
\[
\boxed{cf-de\in\mathfrak n,\qquad
D(F_3)\subseteq\mathfrak nF_3.}
\tag{14}
\]
Under (6), it also says \((B_1,B_2)\ne J_R\), by Nakayama's lemma.
At a reduced obstruction point the first-jet matrix of
\(B_1,B_2\) has rank at most one.

The [complete cubic proof](research/third-image-cubic-gate-pass48.md)
keeps the presentation and flatness steps separate. When the
determinant vanishes, the two-equation candidate can have a larger
fiber; equality with \(\mathcal A\) is not proved. Nor does (14)
say that \(D\) vanishes on the whole quotient fiber.

## 4. The actual image of the exceptional conic plane

At a reduced obstruction point, the parameters in (3) generate
\(\mathfrak n\). Faithful flatness identifies
\[
\mathfrak n^d\mathcal A/\mathfrak n^{d+1}\mathcal A
\simeq
(\mathfrak n^d/\mathfrak n^{d+1})
\otimes_{\mathbb C}\overline{\mathcal A},
\qquad \overline{\mathcal A}=\mathcal A/\mathfrak n\mathcal A.
\tag{15}
\]
Taking the lowest base-adic coefficients of the actual conic relation
therefore gives equations in the full fiber.
Its first-order equations are
\[
-2\bar e\,\bar z+2\bar c\,\bar w-\bar q=0,\qquad
-2\bar f\,\bar z+2\bar d\,\bar w-\bar h=0.
\tag{16}
\]
The affine system must be consistent: otherwise a nonzero scalar
would vanish in the nonzero fiber algebra.

If the coefficient matrix has rank one, the image of the two
functions is confined to an affine line. This says only that
\(\mathbb C[\bar z,\bar w]\) is a quotient of a polynomial line.
It does not describe the whole fiber.

If the rank is zero, (16) also kills the first-order part of \(Q\).
All conic coefficients then belong to \(\mathfrak n^2\), allowing
(15) to be applied in degree two. The three coefficients of
\(a^2,ab,b^2\) express
\(\bar z^2,\bar z\bar w,\bar w^2\) as affine-linear combinations
of \(1,\bar z,\bar w\). Repeated monomial reduction proves
\[
\boxed{\dim_{\mathbb C}\mathbb C[\bar z,\bar w]\le3.}
\tag{17}
\]
Nilpotents are retained. This is a finite-dimensional image
subalgebra, not a dimension bound for the full fiber.
In this case \(p\in\mathfrak n^3\) as well.

The [initial-conic proof](research/initial-conic-fiber-pass48.md)
explains why higher homogeneous coefficients cannot be imposed
merely because lower equations vanish after residue evaluation.
The changing lifts of \(z,w\) can contribute at higher orders.

## 5. Repeated smooth support after the global equation exists

Now make the separate global assumptions \(J=C\) and smooth
reduced support of \(p\). The components are disjoint embedded
affine lines. The plane embedding theorem and the fact that a
nowhere-zero function on an affine line is constant put them in
parallel coordinate positions.[^3] Multiplicities are allowed:
\[
C=\mathbb C[u,v],\qquad
p=P(u)=\prod_i(u-a_i)^{n_i},\qquad n_i\ge1.
\tag{18}
\]
Completing the square in the actual global presentation gives
\[
A=\mathbb C[u,v,r,Y]/(P(u)Y-r^2-d(u,v)),\qquad
Dr=P,\quad DY=2r.
\tag{19}
\]
Smooth support without \(J=C\) does not supply (19).

Let \(d_i(v)=d(a_i,v)\). Factorial closure makes
\(C_i=\{r^2+d_i(v)=0\}\) integral. The full quadratic residue
extension and normalized one-finite-branch cover imply
\[
d_i(v)=c_i(v-b_i)h_i(v)^2,\qquad c_i\ne0.
\tag{20}
\]
The additional assertion is that \(h_i\) has no root away
from \(b_i\).

Indeed the actual open part of \(X=\operatorname{Spec}A\) is
\((\mathbb A^1\setminus\{a_i\})\times\mathbb A^2\).
Its closed complement is the disjoint union
\(\coprod_i C_i\times\mathbb A^1\), with the actual singular
curves \(C_i\). Poincare duality, contractibility, Kunneth and
the compactly supported closed/open sequence give
\[
H_c^1(C_i;\mathbb Q)=0
\quad\text{for every }i.
\tag{21}
\]
No generic smooth fiber has been substituted for a singular one.

Choose \(\gamma_i^2=-c_i\). The finite birational normalization is
\[
v=b_i+w^2,\qquad
r=\gamma_i w\,h_i(b_i+w^2).
\tag{22}
\]
Each distinct root of \(h_i\) away from \(b_i\) identifies two
normalization points. At \(b_i\) there is only one preimage.
The constant-sheaf normalization sequence, whose skyscraper
quotient has dimension equal to the number of branches minus one,
therefore computes \(H_c^1(C_i)\) as precisely the number of these
off-branch roots. Equation (21) excludes all of them. Hence
\[
\boxed{d_i(v)=c_i(v-b_i)^{2k_i+1},\qquad k_i\ge0.}
\tag{23}
\]

At a cusp with \(k_i>0\), the only possibly nonzero derivative
of the total defining equation over \(u=a_i,v=b_i,r=0\) is
\(P'(a_i)Y-d_u(a_i,b_i)\).
If \(n_i=1\), a choice of \(Y\) would make the total space singular.
If \(n_i\ge2\), smoothness instead forces
\[
k_i>0\quad\Longrightarrow\quad
n_i\ge2,\qquad d_u(a_i,b_i)\ne0.
\tag{24}
\]
The two exponents measure different features and need not agree.

If every \(k_i=0\), each root specialization is a plane coordinate.
Maubach's published repeated-root sufficiency theorem then makes
the defining polynomial a coordinate over \(\mathbb C[u]\),
recognizing \(A\) as a polynomial three-ring.[^4]
The [complete repeated-support proof](research/repeated-smooth-support-pass48.md)
therefore leaves only genuine cuspidal thickenings in this
conditional equation branch.

## 6. Why further image principality does not remove the cusps

Once (19) exists, the monic relation provides the actual \(C\)-basis
\(\{Y^j,rY^j:j\ge0\}\). Its members have distinct generic \(r\)-degrees.
The degree-\(n\) member has leading coefficient
\(P^{-\lfloor n/2\rfloor}\), so
\[
\boxed{I_n=P^{\lceil n/2\rceil}C\qquad(n\ge0).}
\tag{25}
\]
This is an all-degree basis argument, not a finite pattern.
Principality of every higher image adds no condition after \(J=C\).

The inherited Russell cubic has the presentation
\[
A_{\rm KR}=
\mathbb C[x,v,r,Y]/(x^2Y-r^2-x-v^3),\qquad
D=x^2\partial_r+2r\partial_Y.
\tag{26}
\]
It is smooth, factorial and contractible, with primitive plinth
\(x^2\mathbb C[x,v]\), faithful-flat polynomial kernel, \(J=C\),
the complete quadratic divisor model and every image ideal
principal. Its residue is the cusp \(r^2+v^3=0\), with
normalization \(v=-w^2,r=w^3\).
Nevertheless its known Makar-Limanov invariant is
\(\mathbb C[x]\), so it is not affine three-space.[^5]

This is a counterexample only to the weaker collection of hypotheses.
No isomorphism \(A_{\rm KR}[s]\simeq\mathbb C^{[4]}\) is asserted,
and no realization of the original unresolved coordinate frame
is supplied. The example prevents replacing the actual cylinder
assumption by contractibility and higher-image freeness alone.

## 7. Remaining obligations

At second-image basepoints, rank-one and rank-zero jets remain.
Nonreduced local obstruction schemes can also fail the coefficient
premise \(B_1,B_2\in J_R\), so the cubic construction is not yet
available there. The image of a low-degree subalgebra is not the
whole fiber without a generation proof.

When \(J=C\) and the reduced support is smooth, genuine cuspidal
thickenings remain. Their exclusion or recognition must use
information beyond the weaker properties realized by the Russell
cubic. Singular reduced plinth support is a separate case.

The genuinely moving branches of the supplied \((1,1,2,2)\)
profile and a universal actual-frame reduction remain unresolved.
The original scope of (1) is unchanged. No historical novelty,
human expert approval or proof-assistant certification is claimed.

## Sources

[^1]: Shulim Kaliman, [*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), final 2004 author version, Lemma 2.2 and Proposition 3.2. The intrinsic pointwise deduction is proved in the linked earlier notes; normalization-surjectivity is not inserted as an unstated source conclusion.
[^2]: Stacks Project, [10.104.2, tag 02JN](https://stacks.math.columbia.edu/tag/02JN), [10.103.7, tag 0BUS](https://stacks.math.columbia.edu/tag/0BUS), and [10.128.1, tag 00R4](https://stacks.math.columbia.edu/tag/00R4). Regular-sequence quotients, absence of embedded associated primes and the exact local miracle-flatness criterion.
[^3]: Angelo Vistoli, [*On the minimal normal compactification of a polynomial in two variables*](https://arxiv.org/pdf/math/9904035v3), 2 August 1999, p. 2 and supporting Theorem 1 on pp. 3–4. Complex Suzuki–Abhyankar–Moh embedding statement and proof.
[^4]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), author manuscript dated 5 October 2001, Theorem 4.5 and its proof, p. 6; published in *Journal of Pure and Applied Algebra* 179 (2003), 159–168. Only the unconditional repeated-root sufficiency is used.
[^5]: Adrien Dubouloz, [*The cylinder over the Koras–Russell cubic threefold has a trivial Makar-Limanov invariant*](https://arxiv.org/pdf/0807.4085), Introduction, PDF p. 1; *Transformation Groups* 14 (2009), 531–539. The example's topology and nonpolynomiality are inherited published facts; its cylinder invariant does not give a polynomial-cylinder isomorphism.
