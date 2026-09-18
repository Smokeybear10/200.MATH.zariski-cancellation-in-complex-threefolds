# The fourth-image obstruction and the relative-fibration boundary

In the reduced, zero-first-jet sector of the actual degree-two
coordinate-frame problem, the fourth-image ideal is nonprincipal:
\(I_4=p^2\mathfrak n\). The full fourth filtration nevertheless
has an explicit free basis. Its generated algebra has a surface
fiber and cannot equal the actual intrinsic algebra, whose fiber
is a curve. Thus every generating set in this sector needs an
element of intrinsic degree at least five.

A separate applicability result identifies why the polynomial
intrinsic quotient does not close the argument: over that chosen
quotient, the cylinder is an affine-plane fibration exactly when
the primitive plinth is a unit. Nontrivial divisor constant fields
block the fibration premise. This is compatible with an already
polynomial threefold and is not a cancellation counterexample.

The general working question remains
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
This complex-threefold interpretation of the supplied conjecture
has not been confirmed by the professor. The conclusions below are
conditional local results, not a solution of (1) or a historical
novelty claim.

## 1. Actual assumptions and coherent coefficients

Retain the actual independent degree-two frame and its primitive
intrinsic locally nilpotent derivation \(D\). Set
\[
C=\ker D\simeq\mathbb C^{[2]},\quad
R=C_{\mathfrak m},\quad\mathfrak n=\mathfrak mR=(a,b),\quad
\mathcal A=A\otimes_C R,\quad L=\operatorname{Frac}R.
\tag{2}
\]
The actual algebra \(\mathcal A\) is a faithfully flat domain
over the regular local surface ring \(R\), with nonempty
one-dimensional closed fiber. These are inherited actual quotient
conclusions, not properties assumed for an approximate conic.[^1]

Write \(F_i=\ker D^{i+1}\), \(I_i=D^i(F_i)\subset R\).
Assume explicitly that the local second-image obstruction satisfies
\[
JR=\mathfrak n,\qquad B_1,B_2\in\mathfrak n^2.
\tag{3}
\]
Reducedness alone does not imply the second condition. The conditions
hold at actual second-image obstructions lying at ordinary triple
points of the full primitive plinth, by the preceding trace argument.
They do not cover arbitrary reduced rank-one first jets.

The established module, derivative and conic identities are
\[
F_2=R\oplus Rz\oplus Rw,\quad F_3=F_2\oplus Rt,\quad
r=az+bw,\quad Dr=p\ne0,
\]
\[
Dz=\epsilon br+B_1,\qquad Dw=-\epsilon ar+B_2,\qquad
p=aB_1+bB_2,\qquad
\epsilon r^2-2B_2z+2B_1w-Q=0,
\tag{4}
\]
where \(\epsilon\in R^*\). Invariant shifts have made
\(r\in\mathfrak n\mathcal A\). The conic and faithful-flat
contraction give \(Q\in\mathfrak n^2\).
Choose coefficients in \(R\) such that
\[
B_1=a^2c+abd+b^2e,\quad
B_2=a^2f+abg+b^2h,\quad
Q=a^2q_1+abq_2+b^2q_3.
\tag{5}
\]
These nine coefficients need not vanish at the closed point.

Choose the actual cubic construction coherently with (5). It gives
\[
\begin{aligned}
bt&=\epsilon rz-2(af+bg)z+2(ac+bd)w-aq_1-bq_2,\\
-at&=\epsilon rw-2bhz+2bew-bq_3,
\end{aligned}
\qquad D^3t=3\epsilon^2p^2.
\tag{6}
\]
The two actual quartic divisions give \(U,V\in F_4\) with
\[
aU=\epsilon w^2-2hz+2ew-q_3,\qquad
bV=\epsilon z^2-2fz+2cw-q_1,
\]
\[
D^4U=6\epsilon^3ap^2,\qquad
D^4V=6\epsilon^3bp^2.
\tag{7}
\]
Membership in \(\mathcal A\) uses the preserved regular sequences
\((a,b^2)\) and \((b,a^2)\), as proved in the
[actual quartic construction](research/triple-point-quartic-corrections-pass51.md).
The displayed fractions are not sufficient by themselves.

## 2. The fourth image is exactly \(p^2\mathfrak n\)

Substitute \(r=az+bw\) into (6) and then use (7).
Cancellation of the nonzero parameters in the actual domain yields
\[
bU=-t-\epsilon zw,\qquad
aV=t-\epsilon zw+2gz-2dw+q_2.
\]
Subtract to obtain
\[
\boxed{bU-aV=-2t-2gz+2dw-q_2.}
\tag{8}
\]
This lies in \(F_3\), with unit coefficient \(-2\) on its
direct-summand basis vector \(t\).

The preceding full divisor calculation and quartic construction gave
\(p^2\mathfrak n\subset I_4\subset p^2R\).
The quotient ideal \(p^{-2}I_4\) contains the maximal ideal, so
the only alternatives were \(p^2\mathfrak n\) and \(p^2R\).
Suppose the latter holds. Choose \(Y\in F_4\) normalized so that
\(D^4Y=6\epsilon^3p^2\). Then \(U-aY,V-bY\in F_3\), giving
\[
bU-aV=b(U-aY)-a(V-bY)\in\mathfrak nF_3.
\tag{9}
\]
But \(F_3=F_2\oplus Rt\) makes the coefficient of \(t\) in
every element of \(\mathfrak nF_3\) lie in \(\mathfrak n\).
Equation (8) contradicts this. Therefore
\[
\boxed{I_4=p^2\mathfrak n.}
\tag{10}
\]
No freeness assumption on \(F_4\) was used to exclude the
principal alternative.

For every \(x\in F_4\), its fourth derivative can now be matched
by an \(R\)-linear combination of \(U,V\), leaving an \(F_3\)
remainder. Equation (8) eliminates that remainder's \(t\)-term,
so \(F_4=F_2+RU+RV\). To prove directness, an \(F_2\)-valued
relation \(\alpha U+\beta V\) has
\(a\alpha+b\beta=0\) after applying \(D^4\).
Coprimality of the parameters gives \(\alpha=bk,\beta=-ak\).
Equation (8) and the direct cubic basis force \(k=0\). Hence
\[
\boxed{F_4=R\oplus Rz\oplus Rw\oplus RU\oplus RV.}
\tag{11}
\]
This identifies the entire fourth filtration, not merely five
independent elements of it. The
[full fourth-image proof](research/fourth-image-boundary-pass52.md)
records the coherent choices and the exact generic determinant control.

## 3. Presentation of the entire quartic algebra

Define polynomials over \(R\):
\[
\begin{aligned}
Q_{aa}&=\epsilon Z^2-2fZ+2cW-q_1,\\
Q_{ab}&=2\epsilon ZW-2gZ+2dW-q_2,\\
Q_{bb}&=\epsilon W^2-2hZ+2eW-q_3.
\end{aligned}
\tag{12}
\]
The conic in (4) is
\(a^2Q_{aa}(z,w)+abQ_{ab}(z,w)+b^2Q_{bb}(z,w)=0\).
Equation (7) and cancellation of \(ab\) give
\(aV+bU+Q_{ab}(z,w)=0\).
For \(S=R[Z,W,\mathsf U,\mathsf V]\), put
\[
J_4=(b\mathsf V-Q_{aa},\
a\mathsf V+b\mathsf U+Q_{ab},\
a\mathsf U-Q_{bb}).
\tag{13}
\]
There is an actual surjection
\(S/J_4\to K_4:=R[z,w,U,V]=R[F_4]\).
The point requiring proof is that these are all the relations.

After inverting \(a\), eliminate
\(\mathsf U=Q_{bb}/a\) and
\(\mathsf V=-(bQ_{bb}+aQ_{ab})/a^2\).
The remaining equation is the full conic times a nonzero scalar.
The same holds after inverting \(b\). At every height-one
base prime one parameter is a unit, so the inherited full
divisor theorem gives
\[
(S/J_4)_{(\pi)}=\mathcal A_{(\pi)},\qquad
(S/J_4)_L=L[r].
\tag{14}
\]
In particular the generic prime has height three in the four-variable
polynomial ring over \(L\).

Set
\[
S_0=\mathbb C[Z,W]/
(\bar Q_{aa},\bar Q_{ab},\bar Q_{bb}).
\tag{15}
\]
The leading terms in its equations are unit multiples of
\(Z^2,ZW,W^2\). Successive reduction of quadratic monomials
shows that \(1,Z,W\) span \(S_0\).
It is nonzero, since its equations hold in the nonempty actual fiber.
Thus
\[
1\le\dim_{\mathbb C}S_0\le3,\qquad
S/(J_4+\mathfrak nS)=S_0[\mathsf U,\mathsf V].
\tag{16}
\]
All primes above the closed base point containing \(J_4\)
have height at least four. Nilpotents are retained.

A minimal prime of a three-generated ideal has height at most three,
so none lies over the closed base point. Equation (14) excludes
minimal primes over height-one base points, since those localizations
are domains in which the base prime is nonzero. There is therefore
only the generic height-three prime.

Locally along \(V(J_4)\), the three equations have codimension three
in a regular local ring, so they form a regular sequence. The quotient
is Cohen-Macaulay and has no embedded associated primes.[^2]
Its unique associated prime is the generic one, which avoids every
nonzero base element. Consequently \(S/J_4\hookrightarrow(S/J_4)_L\).
The actual map to \(\mathcal A\) is generically injective, so it
is injective everywhere. This proves
\[
\boxed{K_4=S/J_4,\qquad
J_4=J_4:(R\setminus\{0\})^\infty.}
\tag{17}
\]
No flatness of \(K_4\) has been presumed, and no vertical component
has been removed by declaration.

Reducing this exact presentation gives
\[
\boxed{K_4/\mathfrak nK_4=S_0[\mathsf U,\mathsf V].}
\tag{18}
\]
This is finite free of rank \(\dim_{\mathbb C}S_0\) over a
polynomial plane and has dimension two. Since the actual closed
fiber has dimension one,
\[
\boxed{R[F_4]\ne\mathcal A.}
\tag{19}
\]
Every generating set of \(\mathcal A\) over \(R\) must contain
an element of intrinsic degree at least five.

The finite algebra \(S_0\) is the full quotient in (15), not
necessarily its image in the actual fiber. The actual map can
kill further classes. The result describes the quartic subalgebra's
surface fiber, not a union of planes inside the actual curve.
The [complete presentation proof](research/quartic-fiber-gate-pass52.md)
states these scheme-theoretic distinctions explicitly.

## 4. Why the polynomial quotient does not finish cancellation

Return to the actual global inclusion
\(C=\ker D\subset A\subset B=A[s_*]\).
An affine-plane fibration over \(C\) must have polynomial-plane
fibers over every prime, not merely a polynomial generic fiber.
This premise is part of the published affine-fibration and
residual-rank theorems. Their slice conclusions do not manufacture
the premise.[^3]

For a prime \(\pi\in C\), write
\(\kappa=\operatorname{Frac}(C/\pi C)\).
The full actual divisor argument gives
\[
A\otimes_C\kappa=F_\pi[t],\qquad
B\otimes_C\kappa=F_\pi[t,s_*],\qquad
[F_\pi:\kappa]=1\ \Longleftrightarrow\ \pi\nmid p.
\tag{20}
\]
Here \(F_\pi/\kappa\) is finite. In the still-unrecognized
degree-two branch its degree is two whenever \(\pi\mid p\).

The support equivalence in (20) follows from the primitive minimal
slice, not an assumed fibration theorem. If \(p\) is a unit at
\(\pi\), the local slice gives a polynomial line there. Conversely,
if \(\pi\mid p\) and \(F_\pi=\kappa\), the residue of \(r\)
is constant. Lift it to \(c\in C_{(\pi)}\); then the actual
element \((r-c)/\pi\) has derivative \(p/\pi\), contrary to
minimality of the localized primitive plinth.

It follows that
\[
\boxed{B\text{ is an }\mathbb A^2\text{-fibration over }C
\quad\Longleftrightarrow\quad p\in C^*.}
\tag{21}
\]
The unit case has the actual slice \(r/p\), giving
\(A=C[r/p]\) and \(B=C[r/p,s_*]\).
For nonunit \(p\), choose a prime divisor. The corresponding
fiber contains a proper finite algebraic extension of \(\kappa\).
In \(\kappa[U,V]\), every element algebraic over \(\kappa\)
is constant: powers of a nonconstant polynomial have distinct
leading degrees. The two rings cannot be isomorphic as
\(\kappa\)-algebras.

In the quadratic branch, separability gives the sharper distinction
\[
(B\otimes_C\kappa)\otimes_\kappa\bar\kappa
\simeq\bar\kappa[t,s_*]\times\bar\kappa[t,s_*].
\tag{22}
\]
There are two geometric planes, not one. Faithful flatness and
smoothness of the total space do not change this residue field.

This failure can occur even in a polynomial threefold. For
\[
A_0=\mathbb C[x,y,z],\quad
D_0=x\partial_y+2y\partial_z,\quad
C_0=\mathbb C[x,h],\quad h=xz-y^2,
\tag{23}
\]
the kernel is \(C_0\). Inverting \(x\) proves the kernel assertion
generically; a smallest possible \(x\)-pole is excluded by evaluating
at \(x=0\), where a nonzero polynomial in \(h\) remains nonzero
after \(h\mapsto-y^2\).
Over the generic divisor \(x=0\),
\[
A_0[s_*]\otimes_{C_0}\mathbb C(h)
=\mathbb C(h)(\sqrt{-h})[z,s_*].
\tag{24}
\]
The odd valuation at \(h=0\) makes \(-h\) nonsquare.
Thus nonunit plinth for a chosen action is compatible with
polynomiality of \(A\). It cannot be treated as a cancellation
counterexample or a reason to demand that every action have a slice.

## 5. Remaining implications

The exact local obstruction is narrower than the full supplied
profile \((1,1,2,2)\). Other branches of that profile remain,
as does the passage from an arbitrary sliced derivation to any
recognized actual frame. The established all-profile recognition
threshold \(H\le9\), and the separately treated height-ten profiles,
do not prove a universal bound on the minimum height.

Completing the full \((1,1,2,2)\) profile and then proving
\(H_{\min}\le10\) for every sliced derivation would imply (1).
Both premises remain unproved. Existence of a minimum by
well-ordering does not bound it, and a positive coefficient search
does not prove termination.

An alternative sufficient target is one actual invariant ambient
coordinate of \(B\). The regular-kernel recognition theorem would
then apply over that coordinate's polynomial base.[^4]
A generator of the abstract quotient \(C\) is not automatically
such a coordinate. The
[full applicability audit](research/universal-frame-reduction-audit-pass52.md)
separates these implications and the failed relative-fibration shortcut.

## 6. Verification and scope

The [captured expanded regression](verification-pass-52.json)
passed 993 methods in 122 suites, including four new methods in two
suites. The recorded run spans 20:42:01-20:43:34 UTC on
13 September 2026. The two new checkers verify the coherent quartic
syzygy, its generic basis determinant, divisor eliminations, and
saturation in specified coefficient models.

The bounded models include reduced length-one and nonreduced
length-three algebras \(S_0\). They are not constructions of
actual unresolved-cylinder obstruction points. Finite tests do not
prove the universal flatness, complete-intersection or generation
arguments.

The [working proof audit](research/proof-audits-pass52-working.md)
records independent AI reconstructions and observed reruns.
These are not human expert review, proof-assistant verification,
or historical novelty certification.

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass52.py
/opt/anaconda3/bin/python research/fourth_image_boundary_checks_pass52.py
/opt/anaconda3/bin/python research/quartic_fiber_gate_checks_pass52.py
/opt/anaconda3/bin/python research/consistency_checks_pass52.py
~~~

No degree-five generation or general cancellation conclusion has
been established in this report. New quintic investigations are
separate from the stated checkpoint. There has been no public
posting, submission or external contact.

## Sources

[^1]: [The actual quotient audit](research/intrinsic-quotient-foundation-audit-pass51.md) and [the preceding local synthesis](deep-pass-51.md). Their published quotient input is Kaliman and Saveliev, [C+-actions on contractible threefolds](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Michigan Mathematical Journal 52 (2004), 619-625; the flatness input is [Stacks 00R4](https://stacks.math.columbia.edu/tag/00R4). The special frame remains an extra actual hypothesis.

[^2]: The Stacks Project, [regular sequences in Cohen-Macaulay local rings, 02JN](https://stacks.math.columbia.edu/tag/02JN), [the supporting module proposition, 00N6](https://stacks.math.columbia.edu/tag/00N6), and [absence of embedded associated primes, 0BUS](https://stacks.math.columbia.edu/tag/0BUS). These standard results support the local complete-intersection step after its codimension hypotheses have been proved.

[^3]: Babu, Das and Lokhande, [Rank and rigidity of locally nilpotent derivations of affine fibrations](https://arxiv.org/pdf/2210.10285v1), Definition 3.1, Remark 3.10 and Corollary 3.11; the arXiv version was deposited in 2022 after the 2021 Communications in Algebra publication. Babu and Das, [Structure of A2-fibrations having fixed point free locally nilpotent derivations](https://arxiv.org/pdf/2001.07632v5), Theorem 4.4, Journal of Pure and Applied Algebra 225 (2021), 106763. The first source's relative-dimension-three result does not automatically apply to the relative-dimension-four cylinder over \(\mathbb C\).

[^4]: Bhatwadekar, Gupta and Lokhande, [Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]](https://arxiv.org/html/1501.01438v1), Theorem 3.5. It requires a nonzero characteristic-zero derivation fixing an actual ambient variable and a regular kernel. It does not recognize arbitrary invariant quotient generators as ambient variables.
