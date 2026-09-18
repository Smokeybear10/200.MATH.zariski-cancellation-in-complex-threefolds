# Original-kernel recognition for the terminal rank-drop quintic

The terminal rank-drop quintic is recognized by using its good
fixed-base partial, rather than trying to turn the bad output
partial into a good one. A linear relation for the nice symmetry
splits according to the surviving coordinate's constant normalized
acceleration. In both cases actual polynomial shears give a rational
two-direction field. Its parallel coefficient is then constrained
by a separate elementary commutator lemma; its radial alternative
already forces an actual invariant coordinate plane.

This is a conditional original-ring theorem. It does not recognize
the independent joint-rank-three moving sectors or provide a
coordinate frame for arbitrary sliced actions.

## 1. Precise original-ring and normalized hypotheses

Let
\[
B=k[a,b,z,w],\quad k=\mathbb C,\quad
E\in\operatorname{LND}_k(B),\quad E(s_*)=1,
\quad 0\ne g\in\ker E,\quad\delta=E/g.
\tag{1}
\]
All displayed generators are actual polynomial coordinates.
Suppose the rational derivation
\[
S=\partial_z+\beta\partial_b+\kappa\partial_a
\]
satisfies
\[
[\delta,S]=0,\quad Sg=S\beta=S\kappa=Sw=0,
\quad\delta\beta=\frac13,\quad\delta\kappa=\frac\beta2,
\quad\delta^2w=\lambda\in k.
\tag{2}
\]
Assume \(g^NS\) is polynomial on \(B\) for some integer
\(N\ge0\). Put \(D=\operatorname{ad}_\delta^2\partial_b\),
and require
\[
D\ne0,\qquad [\delta,\partial_a]=-2D,\qquad
\operatorname{ad}_\delta^2\partial_a=0,
\qquad\operatorname{ad}_E^2\partial_a=0.
\tag{3}
\]
The original and normalized good-partial hypotheses are explicitly
separate. No assertion that \(\delta\) or the coordinate partials
are LNDs of the unlocalized original ring is made.

**Theorem.** Under (1)--(3), \(E\) fixes an actual ambient
coordinate of \(B\), and
\[
\boxed{\ker E\simeq\mathbb C^{[3]}.}
\tag{4}
\]
The terminal independent moving-quintic rank-drop case satisfies
these hypotheses. The [third full-image lemma](quintic-rank-drop-third-image-pass72.md)
gives \(\delta^2w\in k\). The actual constant shear and
[polynomial-clearing proof](quintic-rank-drop-polynomial-symmetry-pass72.md)
give (2), the original good partial, and the explicit choice
\(N=4\). The normalized top identity is
\(J_\delta c=2\widetilde V_X\), so
\([\delta,\partial_a]=-2\widetilde V_X\).
The changed \(b\)-partial differs from the constant direction
\(T_e\) only by a constant good direction. Thus its normalized
second adjoint is still \(D=\widetilde V_X\ne0\), and (3)
holds. The zero normalized-defect branch was already handled
in [the rank-drop bridge](independent-higher-rank-drop-pass72.md).

## 2. The exact linear relation and the two-direction endpoints

Since \(Sg=0\), the polynomial derivation \(T=g^NS\)
has all its polynomial coefficients fixed by itself. It is a
nonzero nice LND and fixes \(w\). Apply the established
three-variable linear-invariant theorem to \(T\) over
\(k(w)\), not to \(E\) over that field.[^nice]
Clearing denominators and canceling the common nonzero factor
\(g^N\) gives
\[
A(w)\kappa+B_0(w)\beta+C(w)=0,
\quad A,B_0,C\in k[W],\quad(A,B_0,C)\ne(0,0,0).
\tag{5}
\]
Only this linear-relation conclusion of the source is used.
Set
\[
h=\kappa-\frac34\beta^2,
\qquad \delta h=Sh=0,
\qquad F=\ker(\delta:\operatorname{Frac}B\to\operatorname{Frac}B).
\tag{6}
\]
The rational function \(\beta\) is transcendental over \(F\):
differentiating a minimal polynomial over the constant field
would contradict \(\delta\beta=1/3\) in characteristic zero.

We will repeatedly use two precise consequences of the complete
[rational two-direction proof](rational-two-direction-recognition-pass69.md).
For an actual coordinate frame \((A_0,w,b_0,z)\) and a field
\(S=\partial_z+v\partial_{b_0}\) with \(Sv=0\), its
direct rational Burgers classification says
\[
v\in k(A_0,w)\quad\hbox{or}\quad
v=\frac{b_0+P}{z+Q},\qquad P,Q\in k(A_0,w).
\tag{7}
\]
In the radial alternative, the polynomial kernel of \(S\)
is exactly \(k[A_0,w]\). Since \([E,S]=0\), the original
polynomial \(E\) preserves this actual plane. Rentschler's
theorem, followed by the original invariant-coordinate
regular-kernel endpoint, proves (4). This is Section 5 of that
proof and does not require the output partial to be good.
Original commutation follows already from (1)--(2):
\([E,S]=[g\delta,S]=0\).

In the parallel alternative we use the
[fixed-good-base coefficient lemma](fixed-good-base-coefficient-pass72.md).
It applies to the normalized rational derivation, genuine
coordinate partials, and the nonzero normalized defect. Its
conclusion is only that \(v\in k(w)\); it does not itself
assert original-kernel recognition. Each application below
checks its exact normalized adjoint identities.

## 3. Zero acceleration first forces constant normalized speed

Assume \(\lambda=0\), and put \(\rho=\delta w\in F\).
If \(\rho=0\), the original action fixes the actual coordinate
\(w\), proving (4) by the inherited regular-kernel endpoint.[^regular]
Assume \(\rho\ne0\).
The exact normalized flow on the three functions in (5) is
\[
w\mapsto w+t\rho,\qquad
\beta\mapsto\beta+t/3,\qquad
\kappa\mapsto\kappa+t\beta/2+t^2/12.
\tag{8}
\]
This may be read in the rational formal exponential: all three
displayed series terminate, so applying it to (5) gives a
polynomial identity in \(t\).

Let \(d=\max\{\deg A+2,\deg B_0+1,\deg C\}\), omitting
zero coefficients. Let \(A_*,B_*,C_*\) be the corresponding
leading coefficients when their weighted degree is \(d\),
and zero otherwise. At least one is nonzero. Comparing the
coefficient of \(t^d\) and dividing by \(\rho^{d-2}\)
in the fraction field gives
\[
A_*/12+(B_*/3)\rho+C_*\rho^2=0.
\tag{9}
\]
Summands with zero starred coefficients are absent before
division. Negative exponents in the dividing element for
\(d=0,1\) are legitimate field inverses. For \(d=0\),
only a nonzero constant \(C\) could occur and would already
contradict (5). For \(d=1\) the same displayed identity is
valid with \(A_*=0\).
The polynomial in (9) is nonzero, since its monomials are
distinct. Algebraic closedness therefore proves
\[
\rho\in k^*.
\tag{10}
\]
Set \(f=w/(3\rho)\) and \(u=\beta-f\). Then
\(\delta u=Su=0\). The element \(w\) is transcendental
over \(F\), by \(\delta w=\rho\ne0\).

### The linear coefficient branch

If \(A=0\), then \(B_0\ne0\), and (5) gives
\(\beta\in k(w)\). Integration of \(\rho\beta'=1/3\)
in the rational one-variable field gives
\[
\beta=f+u_1,\quad u_1\in k,\qquad
P(w)=\frac{w^2}{12\rho^2}+\frac{u_1w}{2\rho},
\quad\delta P=\beta/2.
\tag{11}
\]
Make the actual polynomial shears
\(b'=b-\beta(w)z\), \(a'=a-P(w)z\), fixing \(w,z\).
Their inverses add the same corrections. In these coordinates
\(S=\partial_z+(\kappa-P)\partial_{a'}\), with
\(\delta(\kappa-P)=S(\kappa-P)=0\).
The genuine \(\partial_{a'}=\partial_a\) is good for
the original \(E\). The full rational two-direction theorem
therefore proves (4), using the unchanged original slice.

### The quadratic coefficient branch

If \(A\ne0\), expand (5) using \(\beta=u+f\).
Comparing any coefficient of \(w\) for which \(A\) has
a nonzero complex coefficient gives complex \(\alpha,\gamma\)
with
\[
\frac34u^2+h=\alpha u+\gamma,
\quad\kappa=L(w)\beta+R(w),
\quad L=\frac32f+\alpha,
\quad R=-\frac34f^2-\alpha f+\gamma.
\tag{12}
\]
The comparison is valid over \(F\) because \(u,h\in F\)
and \(w\) is transcendental over it. It does not assume
that \(u\) or \(h\) is complex constant.

The actual polynomial coordinate change and its inverse are
\[
b'=b-fz,\qquad a'=a-Lb-Rz,
\]
\[
b=b'+fz,\qquad a=a'+Lb'+(Lf+R)z,
\tag{13}
\]
with \(w,z\) fixed. It gives \(S=\partial_z+u\partial_{b'}\)
with fixed actual base plane \((a',w)\). The actual partials
and normalized defects satisfy
\[
\partial_{a'}=\partial_a,\qquad
\partial_{b'}=\partial_b+L\partial_a,\qquad
\delta L=1/2,\quad\delta^2L=0,
\]
\[
D':=\operatorname{ad}_\delta^2\partial_{b'}=-D\ne0,
\qquad [\delta,\partial_{a'}]=2D',\qquad
\operatorname{ad}_\delta^2\partial_{a'}=0.
\tag{14}
\]
The value \(D'=-D\), rather than zero, is essential. Indeed,
the adjoint product rule gives \(D'=D+2(1/2)(-2D)=-D\).
We do not apply the good-output theorem to \(\partial_{b'}\).

Apply (7). The radial case is recognized as described there.
In the parallel case the fixed-good-base lemma applies to
\(a',w,b',z\), coefficient \(u\), and (14), with its
proportionality factor equal to two. It proves \(u\in k(w)\).
Since \(\delta u=0\) and \(\delta w=\rho\in k^*\),
one has \(u\in k\). The additional actual constant shear
\(b''=b'-uz\) now makes \(S=\partial_z\), while
\(\partial_{a'}=\partial_a\) remains original-good.
The rational two-direction theorem with coefficient zero
and good output \(a'\) proves (4).
This finishes the zero-acceleration case.

## 4. Nonzero acceleration classifies the coefficient relation

Assume \(\lambda\ne0\). Define
\[
v=\delta w-3\lambda\beta,\qquad
u=w-\frac{9\lambda}{2}\beta^2-3v\beta.
\tag{15}
\]
Direct differentiation gives \(u,v\in F\), and
\[
w=\frac{9\lambda}{2}\beta^2+3v\beta+u,
\qquad
\kappa=\frac{w}{6\lambda}-\frac{v}{2\lambda}\beta
                    +h-\frac{u}{6\lambda}.
\tag{16}
\]
The functions \(1,\beta\) are linearly independent over
\(F(w)\). To see this, \(\beta\) is transcendental over
\(F\), hence so is \(w\) by its genuine quadratic expression.
If \(\beta\in F(w)\), then
\[
(9\lambda\beta+3v)^2
 =18\lambda w+9v^2-18\lambda u
\tag{17}
\]
would express a nonconstant linear polynomial in \(w\) as
a square in \(F(w)\). Its simple-root valuation is odd,
whereas a rational square has even valuations. This is impossible.
No assertion that the whole original fraction field equals
\(F(\beta)\) is required.

Substitute (16) into (5) and compare the coefficients of
\(1,\beta\) over \(F(w)\). One has \(A\ne0\), since
otherwise independence would force \(B_0=C=0\). Moreover
\[
\frac{B_0(w)}{A(w)}=\frac{v}{2\lambda},\qquad
h-\frac{u}{6\lambda}=-\frac{C(w)}{A(w)}-\frac{w}{6\lambda}.
\tag{18}
\]
Both sides in each equation belong to \(F\cap k(w)\).
This intersection is \(k\): for a rational \(r(w)\),
\(\delta r=r'(w)\delta w\); here \(\delta w\ne0\)
because \(\delta^2w=\lambda\ne0\). The constants of
ordinary differentiation on \(k(w)\) are \(k\).
Thus there are complex constants \(k_0,j_0\) such that
\[
\kappa=\frac{w}{6\lambda}-k_0\beta+j_0,
\qquad \delta w=3\lambda\beta+2\lambda k_0.
\tag{19}
\]

## 5. Nonzero acceleration: radial recognition or parallel impossibility

Put \(C_0(w)=w/(6\lambda)+j_0\). Make the actual
polynomial shear
\[
a'=a+k_0b-C_0(w)z,
\qquad a=a'-k_0b+C_0(w)z,
\tag{20}
\]
fixing \(b,z,w\). Equation (19) gives
\(S=\partial_z+\beta\partial_{b'}\), with \(b'=b\)
as a coordinate function and fixed base \((a',w)\).
The genuine partial holding \(a'\) fixed is
\[
\partial_{a'}=\partial_a,\qquad
\partial_{b'}=\partial_b-k_0\partial_a,
\qquad D':=\operatorname{ad}_\delta^2\partial_{b'}=D\ne0,
\quad [\delta,\partial_{a'}]=-2D'.
\tag{21}
\]
The normalized good-partial bound on \(\partial_{a'}\)
is unchanged. Distinguishing a coordinate function from its
new coordinate partial is necessary for (21).

Again apply (7). Its radial case supplies original recognition.
In the parallel case \(\beta\in k(a',w)\), so the
fixed-good-base lemma, with factor minus two and
\(\delta\beta=1/3\), implies \(\beta\in k(w)\).
Its ordinary derivative is nonzero, and therefore
\[
r(w):=\delta w=\frac{1}{3\beta'(w)}\in k(w).
\]
Now \(\delta^2w=\lambda\) gives \(r r'=\lambda\),
so
\[
r(w)^2=2\lambda w+c_0,\qquad c_0\in k.
\tag{22}
\]
The same odd simple-root valuation excludes (22) when
\(\lambda\ne0\). This parallel subcase is impossible.
The radial alternative is recognized, so (4) follows in
the nonzero-acceleration case as well.

## 6. What changed and what has not been claimed

The old direct quintic shear did not create a good bad-output
partial. That failure remains valid. The proof instead retains
the good fixed-base partial and uses its normalized commutator
with the nonzero output defect. All applications of original
recognition occur only after checking original-coordinate and
original-slice hypotheses, or through the independent radial
plane-preservation argument.

The external linear-invariant gate is the same precise source
used in pass71. The good-fixed-base lemma is proved directly
in the rational derivation algebra. No new binary-invariant
source or dimension-three preslice theorem is needed.
No slice is transferred to the polynomial replica of \(S\).

This is a complete written conditional deduction. Independent
review and finite checks must be recorded separately after they
occur. It does not claim historical novelty, human expert review,
formal proof-assistant verification, entire-frame recognition,
or unrestricted cancellation. Frozen pass71 and earlier files
remain unchanged.

## Sources

[^nice]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), arXiv:1701.03635v1, Theorem 3.1(i), PDF p. 5. It states Wang's nonzero linear-invariant theorem over every characteristic-zero field, without the irreducibility premise of its separate part (iii). The exact statement was read directly. The [pass71 source audit](nice-linear-invariant-source-pass71.md) records the inaccessible original Wang proof, the accessible de Bondt proof route, and finite-coefficient-field descent. No fresh complete Wang-proof read is claimed.

[^regular]: The original invariant-coordinate endpoint is Bhatwadekar--Gupta--Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5. The original slice gives regularity of the original kernel. The exact source gates, including Rentschler's theorem for the radial actual plane, are retained in [rational69](rational-two-direction-recognition-pass69.md), Section 5, and [the one-good-output proof](three-output-cubic-closure-pass41.md), Section 1. No fresh reconstruction of all their historical dependencies is claimed.
