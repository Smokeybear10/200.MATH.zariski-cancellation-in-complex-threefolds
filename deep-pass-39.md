# Coordinate reduction at the next cancellation boundary

The general complex threefold cancellation problem remains unresolved.
The results below settle a specified low-flow-degree case, isolate a
genuine obstruction to extending a highest-coefficient argument, and
give an exact test for coordinate reduction within a supplied family.
None proves that a suitable coordinate frame exists for every cylinder.

One correction to the earlier record is essential. The whole-frame
criterion in pass 38 is weaker than the already established
[height-eight theorem](research/height-eight-algebra-pass.md). The
[height-nine theorem](deep-pass-13.md) goes further still. The newer
frame argument is an alternate proof, not an improvement in that
threshold. The separate fixed-model integrability classification from
pass 38 is unaffected.

## 1. The question and the exact conditional result

The working question is
\[
A[s]\simeq\mathbb C[x_1,x_2,x_3,x_4]
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
Here the isomorphism is as complex algebras. The original email's
conclusion in dimension one has a dimensional mismatch when its
parameter exceeds one. Equation (1) is the working corrected
specialization, not a field and dimension confirmed by the professor.

Put \(B=A[s]\) and \(E=\partial_s\). In any genuine polynomial
coordinate system \(x\) on \(B\), write \(T_i=\partial_{x_i}\).
A locally nilpotent derivation, abbreviated LND, has a terminating
iterate on each polynomial. Its exponential \(\exp(tE)\) is therefore
an actual polynomial flow. A slice is a polynomial with derivative one;
the given \(s\) is a slice.

**Conditional low-flow-degree theorem.** Suppose that, in one such
coordinate frame,
\[
[E,[E,T_i]]=0\quad(i=1,2,3),\qquad
(\operatorname{ad}E)^4T_4=0,\qquad E^5(x_i)=0\quad(1\le i\le4).
\tag{2}
\]
Then \(A\simeq\mathbb C^{[3]}\).

The final condition in (2) concerns the four coordinate generators,
not every polynomial. It means that each coordinate of the flow has
degree at most four in time. It does not bound the ordinary degree
of the coefficients of \(E\). The first two conditions constrain
the interaction of \(E\) with the chosen coordinate directions.
They have not been proved achievable for arbitrary \(E\) with a slice.

The full proof is in the
[one-cubic-partial note](research/whole-frame-recognition-pass39.md).
It includes constant and nonconstant highest coefficients, the
low-degree edge cases, and explicit inverse maps for the new shears.
Sections 3 and 4 below give the decisive argument and identify the
precise cases not covered.

## 2. Which coordinate profiles are actually unclosed

Two degree notions must be kept separate. The adjoint height of a
nonzero coordinate partial is
\[
h_E(T)=\max\{j:(\operatorname{ad}E)^jT\ne0\}.
\tag{3}
\]
It is finite because conjugation by the polynomial flow is polynomial
in time. The older slice-filtration degree \(q_i\) measures the largest
shift in \(s\)-degree caused by \(T_i\); its total height is
\(H=\sum_i(q_i+1)\). In an adapted frame on a polynomial quotient,
all adjoint heights are zero, while \(H=3\). The direction \(E\)
has filtration shift minus one.

The existing proofs close every supplied frame with \(H\le9\).
After the negative-shift, double-zero, and zero/one cases are removed,
the first profiles not closed by that threshold are

| Slice-filtration profile | Result established here | Remaining limitation |
| --- | --- | --- |
| \((0,2,2,2)\) | No new general recognition theorem | The entire profile remains unclosed |
| \((1,1,1,3)\) | Recognition under the corresponding adjoint bounds and flow degree at most four | Two highest-degree configurations remain |
| \((1,1,2,2)\) | Exact highest-rank dichotomy when the two quadratic defects are independent | No general recognition theorem for the profile |

This list constrains a hypothetical counterexample; it does not
construct one. Nor does well-ordering of the possible heights give a
coordinate change that lowers a nonminimal frame. That missing
reduction argument cannot be replaced by choosing a minimum.

## 3. A six-dimensional matrix for one cubic partial

Assume the two commutator bounds in (2). If
\((\operatorname{ad}E)^3T_4=0\), the older height-nine argument
already applies. Otherwise define
\[
P=E(x),\quad J=\operatorname{Jac}P,\quad
u=((\operatorname{ad}E)^2T_4)(x),\quad
v=((\operatorname{ad}E)^3T_4)(x)\ne0.
\tag{4}
\]
The coefficient matrix of the actual conjugated partials is
\[
C(t)=I-tJ+\frac{t^2}{2}u e_4^{\mathsf t}
             +\frac{t^3}{6}v e_4^{\mathsf t},
\qquad \operatorname{Jac}(\exp(tE)x)C(t)=I.
\tag{5}
\]
Thus \(C(t)\) is an inverse-flow Jacobian, not an arbitrary
matrix pencil with determinant one.

Introduce
\[
M=\begin{pmatrix}
J&-u/2&-v/6\\
e_4^{\mathsf t}&0&0\\
0&1&0
\end{pmatrix}.
\tag{6}
\]
Schur elimination gives \(\det(I-tM)=\det C(t)=1\), hence
\(M^6=0\). The upper-left block of \(M^r\) equals
\(\operatorname{Jac}(E^r x)/r!\). In particular \(E^6x\)
is constant and \(E^7x=0\). The full commutator class has flow
degree at most six before the extra low-degree hypothesis is imposed.

The left and right kernels of \(M\) contain no nonzero row or
vector supported only on its last two positions. Consequently a
rank-one last nonzero power cannot disappear when its upper-left
block is taken. Descending through the possible nilpotent Jordan
blocks shows that a nonconstant highest coefficient \(h=E^m x\),
for \(m\ge3\), has Jacobian rank one, with \(m\in\{3,4,5\}\).

Comparing the top powers in \(C(t)P(\exp(tE)x)=P\) and (5) yields
\[
(h)_4=0,\quad (E^{m-1}x)_4=0,\quad
l=(E^{m-2}x)_4,\quad E(l)=0,
\]
\[
Jh=\frac{(m-1)(m-2)}6\,lv,\qquad
J\operatorname{Jac}h=\frac{m(m-1)}6\,v\operatorname{Jac}l.
\tag{7}
\]
For flow degree at most two, the same comparison gives \(E(x_4)=0\).
An actual invariant ambient coordinate, together with the regular
kernel furnished by the slice, is sufficient for polynomiality by
the fixed-coordinate regular-kernel theorem.[^1]

## 4. The polynomial curve and the actual repairs

For nonconstant \(h\), the joint map \((h,l)\) has Jacobian
rank one by (7). A polynomial curve-factorization theorem gives
a polynomial \(a\in B\) with \(h=H(a)\), \(l=L(a)\), and
\(E(a)=0\). It does not assert that \(a\) is a coordinate.[^2]
The useful corrected vector is
\[
w=(m-2)LH'-mL'H.
\tag{8}
\]
Equation (7) implies \(Jw=0\). Its vector field commutes with
\(E\), kills \(a\), and therefore kills its own coefficients.
If nonzero, it is a nice LND with coefficient Jacobian rank at
most one.

A nonzero constant \(w\) supplies a constant commuting translation
and reduces directly to the earlier single-partial argument.
For nonconstant \(w\), the established nonhomogeneous rank-one
quasi-translation theorem supplies a linear normal form.[^3]
In the two-output case,
the proof divides a univariate invariant gcd and uses a genuine
univariate Bézout identity to obtain a coordinate slice for the
corrected field. The three-dimensional space of good constant
directions intersects its output plane. A surviving direction
induces the earlier single-partial criterion on its polynomial
three-variable kernel. That criterion uses the planar and
commuting-three-variable LND theorems with their original
hypotheses.[^4] The outcome is an invariant ambient coordinate
for \(E\), so the regular-kernel theorem applies again.

This step cannot be replaced by the claim that every highest
coefficient vector is nice. Section 5 gives an explicit counterexample
to that claim in the adjacent profile.

The remaining nonconstant case has \(L\ne0\) and \(w=0\).
Factoring the one-variable polynomials gives, with
\(e=\gcd(m,m-2)\),
\[
h=cg^{m/e},\qquad l=\lambda g^{(m-2)/e},\qquad
c_4=0,\quad \lambda\in\mathbb C^*,\quad E(g)=0.
\tag{9}
\]
For \(m=3\), the actual repair is
\[
y=x-\frac{c}{6\lambda^3}x_4^3.
\tag{10}
\]
Its inverse has a plus sign, since it leaves \(x_4\) unchanged.
The first three partials do not change. If \(A=c\cdot\partial\),
the fourth becomes \(T_4+x_4^2A/(2\lambda^3)\).
The iterated-bracket product rule and (7) make its third
commutator vanish identically, including at \(g=0\). The
repaired frame satisfies the older mixed theorem.

For \(m=4\), the corresponding repair is
\[
y=x-\frac{c}{6\lambda^2}x_4^2,\qquad
T'_4=T_4+\frac{x_4}{3\lambda^2}A.
\tag{11}
\]
Its third commutator also vanishes. A constant highest vector
is handled by a constant commuting direction when \(l=0\),
an actual coordinate slice when \(m=3\) and \(l\ne0\), and
the same quadratic repair when \(m=4\) and \(l\ne0\).
This completes every case in the stated low-degree theorem.

For this one-cubic-partial argument, the unresolved highest
configurations are precisely
\[
\begin{array}{ll}
m=5:& h_5=cg^5,\quad (h_3)_4=\lambda g^3,\\
m=6:& h_6=c\ne0,\quad (h_4)_4=\lambda\ne0.
\end{array}
\tag{12}
\]
In the first line \(g\) is invariant and nonzero, possibly
constant. In the second the displayed coefficients are constant.
These are necessary remaining descriptions, not actual
nonpolynomial examples or complete normal forms for \(E\).

## 5. Two quadratic defects: a real obstruction to the rank-one route

Now assume adjoint heights at most \((1,1,2,2)\). Let
\(\mathcal V\) have columns
\(((\operatorname{ad}E)^2T_3)(x)\) and
\(((\operatorname{ad}E)^2T_4)(x)\), assumed independent over
\(\operatorname{Frac}B\), and let \(L_0\) select the last two
coordinates. The companion becomes
\[
\mathcal M=\begin{pmatrix}J&-\mathcal V/2\\L_0&0\end{pmatrix},
\qquad \mathcal M^6=0.
\tag{13}
\]
Both its left and right kernels avoid the auxiliary plane.
If \(\mathcal M N=N\mathcal M=0\), deleting the auxiliary
columns preserves row rank, and deleting the auxiliary rows
preserves image rank. Thus the upper-left block of \(N\)
has exactly the rank of \(N\), without a rank-one restriction.

For flow degree \(m\ge3\), this gives
\(\operatorname{rank}\operatorname{Jac}(E^m x)\le1\).
For \(m=2\), however, the answer is exactly two. Indeed
\(\mathcal M^3=0\) and \(\operatorname{rank}\mathcal M\ge4\);
its Jordan type must be \((3,3)\). Its squared upper-left
block consequently has rank two. Degree one is impossible
under the independent-defects hypothesis.

This alternative occurs in an actual sliced polynomial cylinder.
In physical coordinates \((a,b,c,d)\), set
\[
u=b-a^2/2,\quad v=d-c^2/2,\quad g=uv-1,
\quad E=u\partial_a+au\partial_b+g\partial_c+cg\partial_d.
\tag{14}
\]
The intermediate coordinates \((u,v,a,c)\) make
\(E=u\partial_a+g\partial_c\), proving local nilpotence.
The slice and invariant
\[
s=va-c,\qquad r=ga-uc
\tag{15}
\]
satisfy \(E(s)=1\), \(E(r)=0\). There are explicit inverse maps
\[
a=us-r,\quad c=gs-vr,\quad
b=u+(us-r)^2/2,\quad d=v+(gs-vr)^2/2.
\tag{16}
\]
Hence \(\ker E=\mathbb C[u,v,r]\). In the frame \((b,d,a,c)\),
both the adjoint and slice-filtration profiles are exactly
\((1,1,2,2)\); nonzero values on the invariant \(r\) certify
that these are attained degrees, not merely upper bounds.

Here \(E^2x=(u^2,g^2,0,0)\) has Jacobian rank two. Its
associated highest vector field \(U=u^2\partial_b+g^2\partial_d\)
satisfies
\[
U^n(u)=n!u^{n+1}\ne0,\qquad
u^2v^2(1-2g)+g^2(3+2g)=1.
\tag{17}
\]
It is not an LND even though its coefficients generate the unit
ideal. Passing to a primitive vector therefore does not repair it.
The original \(E\) has a slice throughout.

This is a counterexample to automatic highest-vector recognition,
not to cancellation. The quotient and a better frame are explicitly
polynomial. The complete
[two-defect proof](research/two-quadratic-defects-pass39.md)
also records the general top-factor identities and the precise
independence assumption.

## 6. Exact reduction inside a supplied coordinate family

Let \(\Phi_{\mathbf t}\) be a supplied automorphism of
\(B[\mathbf t]\) fixing the parameter ring, with a polynomial
inverse and \(\Phi_{\mathbf0}=\mathrm{id}\). Keep \(E\) fixed.
The partials of the actual new coordinates
\(y_i=\Phi_{\mathbf t}(x_i)\) are
\(U_i=\Phi_{\mathbf t}T_i\Phi_{\mathbf t}^{-1}\).

For a target profile \(\mathbf r\), expand
\(((\operatorname{ad}E)^{r_i+1}U_i)(x_j)\) in the ambient
monomials. If \(I_{\mathbf r}\) is the ideal generated by
all parameter coefficients, then
\[
\{\mathbf t:h_E(U_i)\le r_i\text{ for all }i\}
=V(I_{\mathbf r}).
\tag{18}
\]
This is necessary and sufficient because a derivation is zero
exactly when it kills all polynomial generators. In one parameter,
success for a target that fails initially can occur only at finitely
many exceptional values. A generic parameter choice will miss it.
Several parameters can instead give a positive-dimensional success
set. Effective computation requires coefficients in an effective
exact field; arbitrary unencoded complex constants are not an
algorithmic zero-testing input.

For an elementary shear \(y_j=x_j+P(x_{\ne j})\) of bounded
degree, the other partials are
\(U_i=T_i-(T_iP)T_j\). The target equations are affine-linear
in the unknown coefficients of the single polynomial \(P\).
They decide every shear in that finite ansatz, including the
simultaneous integrability of the rows. Failure at a chosen degree
does not prove failure at all degrees, and no universal search
bound is established.

There is nevertheless an all-degree obstruction for one explicit
family. Take \(E=\partial_s\) on \(\mathbb C[a,b,c,s]\) and
\[
x=a+s^N,\qquad y=s+x^M,\qquad N,M\ge2.
\tag{19}
\]
The exact profile of \((x,y,b,c)\) is
\((NM-1,N-1,0,0)\). Every nonconstant shear
\(x'=x+P(y)\), with \(\deg P=k\), changes it to
\((NM-1,NMk-1,0,0)\). Thus that entire direction strictly
raises the sum of the heights, at every positive degree.
The proof is a noncancellation of leading coefficients, not a grid.

The transverse family \(y'=y-tx^M\) lowers the profile only at
\(t=1\). It then gives \((x,s,b,c)\), after which
\(x\mapsto x-s^N\) reaches the adapted frame. This exhibits
both a completely ineffective family and the exact exceptional
value of an effective family on the same actual cylinder.

An automorphism preserving \(A\) setwise cannot lower any adjoint
height: it sends \(s\) to \(us+h\), with \(u\in\mathbb C^*\)
and \(h\in A\), and merely rescales \(E\) under conjugation.
A successful reduction must move the chosen kernel subalgebra
inside \(B\). This necessary condition does not construct a move.
The complete arguments are in the
[coordinate-family note](research/coordinate-reduction-pass39.md).

## 7. Verification, prior work, and the remaining obligation

The new finite exact checkers test polynomial inverse maps,
commutators, matrix identities, coefficient ideals, and displayed
negative controls. They do not certify the universal quantifiers
in the written proofs or the cited classification theorems.
The [current regression record](verification-pass-39.json) reports
the actual executed suite results. Full proof-assistant verification,
human expert review, and novelty verification remain absent.

The recognition arguments retain the published inputs' exact scope.
A polynomial parameter is not automatically a coordinate; a
three-variable theorem is not a four-variable classification;
homogenization introduces an additional invariant that can be the
only one supplied by a theorem. The
[literature comparison](research/literature-scope-pass39.md)
records those distinctions and the earlier-result reconciliation.
The bounded literature search does not establish originality or
exclude all later prior work.

The next focused mathematical obligation is to resolve one of the
two configurations in (12), or to obtain a genuine coordinate
repair for another height-ten profile. Even closing all three
profiles would not solve (1) without an argument forcing a bounded
frame or a decreasing move. The exact family criterion in (18)
checks a proposed move but does not supply that existence theorem.

## Sources

1. S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande.
   [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1),
   2015 preprint, Theorem 3.5. Used only after obtaining an actual
   fixed ambient coordinate and a regular kernel.
2. Michiel de Bondt.
   [*Rational maps H for which K(tH) has transcendence degree 2 over K*](https://arxiv.org/pdf/1501.06046),
   Corollary 3.2 and Lemma 3.3, PDF pages 20–21. Supplies a
   polynomial parameter for the transcendence-degree-one algebra,
   not a coordinate theorem.
3. Michiel de Bondt.
   [*Quasi-translations and singular Hessians*](https://arxiv.org/pdf/1501.05168),
   Theorem 5.5, PDF page 19;
   [published version](https://doi.org/10.4064/cm6915-3-2017),
   *Colloquium Mathematicum* 152 (2018), 175–198.
   The nonhomogeneous rank-one statement is the relevant input.
4. Nikhilesh Dasgupta and Sergey Gaifullin.
   [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510),
   Theorem 2.7 and Proposition 2.14. These explicitly recall the
   planar triangularization and commuting-three-variable results
   used by the earlier single-partial lemma.

[^1]: Bhatwadekar, Gupta and Lokhande, [Theorem 3.5](https://arxiv.org/html/1501.01438v1). The slice makes the kernel regular, but the invariant ambient coordinate is a separate required input.
[^2]: De Bondt, [Corollary 3.2 and Lemma 3.3](https://arxiv.org/pdf/1501.06046). Both the highest vector and the preceding selected coefficient must belong to the same transcendence-degree-one algebra.
[^3]: De Bondt, [Theorem 5.5](https://arxiv.org/pdf/1501.05168). Its rank-one normal form applies to the corrected nice vector, not automatically to the original highest vector.
[^4]: Dasgupta and Gaifullin, [Theorem 2.7 and Proposition 2.14](https://arxiv.org/pdf/2306.00510); the complete local deduction is in the [single-partial proof](research/height-seven-audit.md).
