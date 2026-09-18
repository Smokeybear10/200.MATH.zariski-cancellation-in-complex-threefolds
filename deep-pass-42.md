# Quadratic-frame recognition and the remaining two-defect problem

A locally nilpotent derivation of the complex polynomial three-ring
fixes a polynomial coordinate if its third iterated adjoint annihilates
each partial of a supplied polynomial coordinate frame. This theorem
does not require a slice. It closes the four-variable cancellation
case with one commuting coordinate direction and three quadratic
adjoint columns, provided the original four-variable action has a slice.

The remaining two-quadratic-column case has stronger reductions. At
flow degree two, its independent leading fields span a single tangent
plane, and their restrictions to the slice quotient have rank one.
At higher degree, a full companion-matrix image calculation forces an
exact common power law. A rational normalization has an exact rank
dichotomy, but neither that normalization nor its rank calculation
supplies global polynomial coordinates.

The general complex threefold cancellation conjecture is not proved.
The results here have explicit additional frame hypotheses. No claim
of novelty, human expert review, or proof-assistant verification is made.

## 1. The cancellation target and recognition criteria

The working question is
\[
A[s_*]\simeq\mathbb C[x_1,x_2,x_3,x_4]
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
An isomorphism on the left transports \(\partial_{s_*}\) to a
locally nilpotent derivation \(E\) of the actual polynomial ring
\(B=\mathbb C[x_1,x_2,x_3,x_4]\). It has a polynomial slice,
\(E(s_*)=1\), and kernel \(A\). Conversely, the slice theorem
recovers this cylinder presentation from a sliced LND.[^1]

An ambient coordinate means an element belonging to some polynomial
coordinate system of the original ring. It means more than being
nonconstant, algebraically independent of another element, or having
nonzero differential. If \(E\) fixes an actual ambient coordinate
\(p\), then the original kernel is polynomial: its regularity
follows from the slice, and the established regular-kernel theorem
gives \(A=\mathbb C[p]^{[2]}\).[^2]

Write \(T_i=\partial_{x_i}\) and
\(\operatorname{ad}_E T=[E,T]\). The adjoint height of a partial
is its last nonzero iterated adjoint. Thus a good column here has
\(\operatorname{ad}_E^2T_i=0\), and a quadratic column has
\(\operatorname{ad}_E^3T_i=0\). The supplied-frame requirements
are conditions to prove, not properties automatic from (1).

| Supplied adjoint profile | Current conclusion with an original slice |
| --- | --- |
| All profiles covered by the earlier \(H\le9\) theorem | Polynomial kernel, by the earlier proof |
| \((1,1,1,3)\) | Complete recognition in the preceding one-cubic theorem |
| \((0,2,2,2)\) | Complete recognition in Section 2 below |
| \((1,1,2,2)\) | Partial reductions below; not completely recognized |
| Arbitrary supplied frame, or an unknown better frame | No universal reduction established |

Here \(H\) is the earlier shifted total height, the sum of the
four adjoint heights plus four. The all-profile threshold is still
\(H\le9\), not \(H\le10\). Recognizing another particular
height-ten profile does not change that distinction.

## 2. A three-variable quadratic-adjoint theorem without a slice

**Theorem.** Let \(R=\mathbb C[y_1,y_2,y_3]\), and let
\(D\in\operatorname{LND}(R)\). If
\[
\operatorname{ad}_D^3\partial_{y_i}=0\qquad(i=1,2,3),
\tag{2}
\]
then \(\ker D\) contains an actual coordinate of \(R\).

For \(D=0\) the conclusion is immediate. Otherwise set
\(v=Dy\), \(J=\operatorname{Jac}v\), and
\(U_i=\operatorname{ad}_D^2\partial_{y_i}\). The actual conjugate
of a partial is
\[
\exp(tD)\partial_{y_i}\exp(-tD)
=\partial_{y_i}+t[D,\partial_{y_i}]+\tfrac12t^2U_i.
\tag{3}
\]
Its highest coefficient is an LND: for each polynomial, an iterate
of the conjugate vanishes, and its top coefficient is the corresponding
iterate of \(U_i/2\). Each \(U_i\) also commutes with \(D\).
If one is fractionally independent of \(D\), the known commuting
derivations theorem already supplies a common invariant coordinate.[^3]

In the remaining case, write \(U_i=h_iD\) over
\(K=\operatorname{Frac}R\). Commutation gives \(Dh_i=0\).
For \(F_t=\exp(tD)y\), its inverse Jacobian is
\[
C(t)=(\operatorname{Jac}F_t)^{-1}
=I-tJ+\tfrac12t^2vh^{\mathsf t},\qquad \det C(t)=1.
\tag{4}
\]
The rank-one adjugate identity
\(\operatorname{adj}(A+qvh^{\mathsf t})v=\operatorname{adj}(A)v\)
then gives
\[
F'_t=\operatorname{adj}(I-tJ)v,\qquad D^4y=0.
\tag{5}
\]
The right side has degree at most two in \(t\). This degree
bound is used only in the dependent-top branch, not asserted as a
consequence of (2) alone.

Let \(m\) be the last nonzero coordinate iterate and put
\(H=D^my\). For \(m=1\), the three-variable nice-derivation
theorem gives an invariant linear form.[^4] For \(m=2,3\), compare
the coefficient of \(t^{2m}\) in
\(\operatorname{adj}(\operatorname{Jac}F_t)=C(t)\). It gives
\(\operatorname{adj}(\operatorname{Jac}H)=0\), hence
\(\operatorname{rank}\operatorname{Jac}H\le1\).

The top two coefficients of \(C(t)F'_t=v\) give
\[
h^{\mathsf t}H=0,\qquad
JH=\frac{m-1}{2}(h^{\mathsf t}D^{m-1}y)v.
\tag{6}
\]
For the polynomial field \(T_H=H\cdot\partial\), define
\(\kappa=-(m-1)h^{\mathsf t}D^{m-1}y/2\). Then
\([D,T_H]=\kappa D\) and \(D\kappa=0\). Commuting
\(D^m\) with \(T_H\) and evaluating on the coordinates yields
\[
(\operatorname{Jac}H)H=-m\kappa H.
\tag{7}
\]

If \(\kappa=0\), the nonzero polynomial field \(T_H\) is
nice and commutes with \(D\). An independent pair uses the
commuting theorem. A dependent pair has the same kernel, so the
nice-field invariant linear form is also invariant under \(D\).

If \(\kappa\ne0\), (7) puts \(H\) in the rank-one image
of its Jacobian. All columns of that Jacobian are proportional to
\(H\), so every partial kills every ratio \(H_i/H_j\).
Those ratios are complex constants. Consequently \(H=Fc\) for
a nonzero constant vector \(c\), and (6) implies
\(\operatorname{ad}_D^2T_c=0\). The previously proved
[single-partial lemma](research/height-seven-audit.md#2-a-single-partial-lemma-in-three-variables)
then supplies an invariant coordinate. Its dependent branch uses
primitive polynomial division and the genuine two-variable
triangularization theorem, without assuming a slice.[^1]

This proves the theorem. Its complete denominator and boundary details
are in the [standalone proof](research/three-variable-quadratic-frame-pass42.md).

## 3. Recognition of the commuting-column profile

Suppose the original sliced \(E\) is written in an actual frame
\(B=\mathbb C[t,y_1,y_2,y_3]\) with
\[
[E,\partial_t]=0,\qquad
\operatorname{ad}_E^3\partial_{y_i}=0.
\tag{8}
\]
Its coefficients are independent of \(t\), so
\(E=D+a(y)\partial_t\). Restriction to the actual three-ring
makes \(D\) an LND satisfying (2). If \(D=0\), the slice
forces \(a\) to be a nonzero constant, and the kernel is plainly
the three-ring. Otherwise Section 2 provides an invariant coordinate
of that three-ring, hence of the original four-ring. The regular-kernel
criterion applies and proves \(\ker E\simeq\mathbb C^{[3]}\).

No slice has been transferred from \(E\) to \(D\). For an
actual example showing why that matters, take
\[
N=\begin{pmatrix}-1&-3&-1\\1&1&1\\0&2&0\end{pmatrix},
\quad D(y)=Ny,\quad E=D+\partial_t.
\tag{9}
\]
Then \(N^3=0\), every column of \(N^2\) is nonzero, and
the exact profile is \((0,2,2,2)\). The base field vanishes
at the origin and has no slice. The original field has \(Et=1\),
with explicit inverse coordinates
\(k=(I-tN+t^2N^2/2)y\) and
\(y=(I+tN+t^2N^2/2)k\).

## 4. Dependent quadratic defects and the constant-recombination gate

Now assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0,
\quad V_i=\operatorname{ad}_E^2T_i\ (i=3,4).
\tag{10}
\]
If \(V_3,V_4\) have rank one, primitive polynomial division gives
\(V_3=aD_0,V_4=bD_0\), with \(D_0\) an LND commuting
with \(E\) and \(a,b\in\ker E\cap\ker D_0\).
The field \(bT_3-aT_4\) has second \(E\)-adjoint zero.
It need not itself be an LND, much less a coordinate partial.

A constant relation between the defects does give a third good partial
by a constant frame change, reducing to an already recognized mixed
case. A merely rational relation does not. This failure occurs on a
genuine polynomial cylinder, not just formal coefficient data.

Take \(f=u+v\), \(q=f^2+1\), and
\(E=f\partial_A+q\partial_C\). Its slice and invariant are
\(s=C-fA\), \(r=qA-fC\), with inverse
\(A=r+fs\), \(C=fr+qs\). In the actual frame
\((u+A^2/2,v+C^2/2,A,C)\), the two defects are
\(2f(\partial_A+2f\partial_C)\) and
\(2q(\partial_A+2f\partial_C)\). They are rationally dependent
but complex-linearly independent.

The natural syzygy \(Y=qT_3-fT_4\) even has unit coefficient
ideal, yet its divergence in this frame is
\[
\operatorname{div}Y=C-2fA\ne0.
\tag{11}
\]
A polynomial LND has zero divergence, by differentiating the unit
Jacobian of its polynomial flow. Thus this syzygy is not an LND.
The [full countercontrol](research/dependent-quadratic-defects-pass42.md)
excludes this uncorrected construction and constant recombination, not
nonlinear coordinate repair. The displayed inverse already repairs
the example nonlinearly.

## 5. Independent defects at flow degree two

Assume (10), \(\operatorname{rank}[V_3\mid V_4]=2\), and
\(E^3x=0\), \(h=E^2x\ne0\). The earlier full companion
calculation gives \(\operatorname{rank}\operatorname{Jac}h=2\).
Let \(L_0\) select the last two coordinates. The top inverse-flow
identity gives \(L_0h=0\), so
\(f=Ex_3\) and \(g=Ex_4\) are \(E\)-invariant.

Comparing the highest coefficients of the actual conjugated partials
acting on the actual flow gives
\[
\operatorname{span}_{\operatorname{Frac}B}
\{E,[E,T_1],[E,T_2],V_3,V_4\}
=\operatorname{span}\{V_3,V_4\}
=\ker\operatorname{Jac}h.
\tag{12}
\]
This plane has dimension two. Every displayed field kills \(f,g\)
and commutes with \(E\). The original slice gives \(B=A[s_*]\);
the kernel of restriction of this plane to \(A\) is exactly the
line spanned by \(E\). Hence the displayed nonzero leading
restrictions have rank exactly one on \(A\).

This is not a statement that all LNDs of \(A\) have rank-one
span or the same kernel. It supplies no intrinsic slice. In particular,
fixed-locus countercontrols from earlier passes still apply.

There is a useful additional closure. Put \(F=(f,g)^{\mathsf t}\)
and \(J=\operatorname{Jac}(Ex)\). The invariant-speed bracket
identity and (12) give
\[
L_0[V_3\mid V_4]=2(\operatorname{Jac}F)J_{\{3,4\}},
\qquad F\in\operatorname{im}\operatorname{Jac}F.
\tag{13}
\]
If \(\operatorname{rank}\operatorname{Jac}F\le1\), this image
condition forces \(F=0\) or a constant projective direction.
Thus one bad coordinate, or a constant linear combination of the two,
is an invariant ambient coordinate. With the original slice, the
regular-kernel theorem closes that branch.

A remaining degree-two instance must therefore have two algebraically
independent bad-coordinate speeds. The rank-two-defect premise is
essential: the rank-one example of Section 4 violates the image
condition in (13). The [complete proof](research/two-quadratic-degree-two-pass42.md)
keeps these hypotheses separate.

## 6. The full companion image at higher degree

Retain (10) and independent defects. Put \(h_j=E^jx\), let
\(m\) be the last nonzero index, and set \(h=h_m\),
\(\ell=L_0h_{m-1}\). The actual companion matrix is
\[
\mathcal M=\begin{pmatrix}J&-[V_3\mid V_4]/2\\L_0&0\end{pmatrix},
\qquad \mathcal M^6=0,\qquad
(\mathcal M^j)_{\rm UL}=\operatorname{Jac}h_j/j!.
\tag{14}
\]
If \(m\ge3\) and \(h\) is nonconstant, then \(3\le m\le5\),
and the nilpotence index of \(\mathcal M\) is \(m+1\).
There is one Jordan block of size \(m+1\); all others have total
size \(5-m<m\). Consequently
\[
\ker\mathcal M\cap\operatorname{im}\mathcal M^{m-1}
=\operatorname{im}\mathcal M^m
\quad\text{is a line}.
\tag{15}
\]

The crucial full-row identities are
\[
\mathcal M^{m-1}\binom{Ex}{0}
=\frac1{(m-1)!}\binom h{(m-1)\ell},
\qquad
(\mathcal M^m)_{\text{first four columns}}
=\frac1{m!}\binom{\operatorname{Jac}h}{m\operatorname{Jac}\ell}.
\tag{16}
\]
The first vector is nonzero and belongs to the line in (15).
Every differential column in the second expression is therefore
proportional to it. The upper components give \(h=cq\), with
\(c\) a nonzero constant vector satisfying \(c_3=c_4=0\),
and \(q\) a nonconstant invariant. The lower components give
\[
mq\,d\ell_i=(m-1)\ell_i\,dq.
\tag{17}
\]

If \(\ell=0\), the top identity gives \(Jc=0\), so the
constant good direction \(T_c\) commutes with \(E\). The
[one-good-partial recognition lemma](research/three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial)
applies with a constant nice field and the original slice, closing
this branch.

If \(\ell\ne0\), (17) makes \(\ell_i^m/q^{m-1}\) a
complex constant for each nonzero component. Unique factorization in
the original polynomial ring, and coprimality of \(m,m-1\), give
\[
h=cg^m,\qquad \ell=\lambda g^{m-1},\qquad
g\in\ker E\setminus\mathbb C,\quad
0\ne\lambda\in\mathbb C^2.
\tag{18}
\]
All prime multiplicities are retained. No curve-factorization theorem
or assertion that \(g\) is a coordinate is used. The proposed
rotating-direction correctors vanish under (16); they do not produce
a nonzero commuting field that would close this alternative.

## 7. Exact normalization ranks and the global boundary

On \(B_g\), the field \(\delta=E/g\) is an actual LND,
with \(\delta^mx=c\) and \(L_0\delta^{m-1}x=\lambda\).
Its adjoint bounds have the same orders, and its bad defect columns are
\[
\widetilde V_i=g^{-2}V_i+
2g^{-3}([E,T_i]g)E\qquad(i=3,4).
\tag{19}
\]
If \(E,V_3,V_4\) have rank three, the new pair remains independent.
Otherwise write \(E=\alpha V_3+\beta V_4\). The next-to-top
bad-column coefficient gives
\(\alpha[E,T_3]g+\beta[E,T_4]g=-g/2\). Thus the two-by-two
rank update is an idempotent of trace one. In both cases,
\[
\operatorname{rank}[\widetilde V_3\mid\widetilde V_4]
=\operatorname{rank}[E\mid V_3\mid V_4]-1\in\{1,2\}.
\tag{20}
\]
In the rank-drop case the surviving line is independent of \(E\).

This is an exact generic rank statement, not global recognition.
The coordinate partials need not be LNDs after localization at \(g\).
The normalized defects therefore cannot automatically be treated as
a new globally admissible polynomial LND frame. A polynomial replica,
its behavior along \(g=0\), and an actual coordinate construction
would each need proof.

A separate refinement holds when the original highest vector is
constant and \(m\ge4\). The unique longest companion block gives
an actual polynomial slice \(\sigma\) and constants \(c,d,\ell,\mu\)
such that
\[
h_{m-1}=c\sigma+d,\qquad
L_0h_{m-2}=\ell\sigma+\mu,\qquad E\sigma=1.
\tag{21}
\]
This does not assert that \(\sigma\) is a coordinate. The
constant-top degree-three boundary can have two longest Jordan blocks
and is not covered by this particular refinement. The full arguments
are in the [companion-image proof](research/two-quadratic-top-line-pass42.md).

## 8. A necessary condition for the normalized commuting corrector

The power law suggests an explicit candidate rather than an abstract
existence argument. Let \(T_\lambda\) be the constant bad-coordinate
direction with coefficients \(\lambda\), put \(k=T_cg\), and set
\[
Z=T_c+\frac{m-1}{2}[\delta,T_\lambda].
\tag{22}
\]
The original and normalized top identities give
\([\delta,Z]=0\), but also the more restrictive identities
\[
Zg=\frac{k}{2},\qquad
[E,Z]=-\frac{k}{2g}E,\qquad Ek=0.
\tag{23}
\]
Thus centralizing the normalized field does not automatically
centralize the original action.

For \(Z\) to be locally nilpotent on \(B_g\), it must kill
the unit \(g\), so \(k=0\). For a polynomial power-clearing
replica \(g^NZ\), \(N\ge1\), to be an LND on \(B\),
its value \(g^Nk/2\) on \(g\) is divisible by \(g\),
again forcing \(k=0\) by the LND divisibility criterion.
Even polynomiality of \(Z\) alone forces \(k=0\): applying
the commutator in (23) to the original slice makes \(k/g\)
polynomial, and a constant partial cannot take a polynomial to a
nonzero multiple of itself.

The clearing itself is explicit:
\[
g^2Z=g^2T_c+\frac{m-1}{2}
\bigl(g[E,T_\lambda]+(T_\lambda g)E\bigr).
\tag{24}
\]
It proves polynomiality, not local nilpotence. At \(k=0\),
local nilpotence or niceness of this commuting field remains unproved.
If \(k\) is a nonzero complex constant, a different argument
already closes the branch: in linear coordinates with
\(T_c=\partial_b\), the invariant \(g=kb+q\) is an actual
triangular coordinate. The original regular-kernel theorem applies.

The [denominator-gate proof](research/two-quadratic-localization-gate-pass42.md)
does not construct a high-degree residual with \(k\ne0\).
It gives a necessary condition for this proposed construction and
an elementary recognition branch, not a counterexample to cancellation.

## 9. An all-corrections obstruction in the degree-two branch

In the independent degree-two branch, write
\(H=(E^2x)\cdot\partial_x\). The top identity yields
\(L=[E,H]=-(fV_3+gV_4)/2\), with \([E,L]=0\).
For any polynomial \(E\)-slice \(\sigma\), the field
\[
Y_\sigma=H-\sigma L-(H\sigma-\sigma L\sigma)E
\tag{25}
\]
commutes with \(E\) and kills \(\sigma\). It genuinely
descends to a derivation of \(A\). Descent alone is therefore
not the missing condition for this candidate.

Consider the actual example
\(E=u\partial_a+(uv-1)\partial_c\), with physical frame
\((u+a^2/2,v+c^2/2,a,c)\). Its slice is \(s=va-c\),
its invariant is \(r=(uv-1)a-uc\), and the polynomial inverse
is \(a=us-r\), \(c=(uv-1)s-vr\). Both the defect pair and
the bad-speed pair have rank two. In these coordinates,
\(H=u^2\partial_u+(uv-1)^2\partial_v\).

Every displayed leading field
\(E,[E,T_1],[E,T_2],V_3,V_4\) kills \(u,v\). Therefore
for every polynomial-coefficient correction \(X\) of \(H\)
by their entire \(B\)-module,
\[
X(u)=u^2,\qquad X^n(u)=n!u^{n+1}\ne0.
\tag{26}
\]
No such \(X\) is locally nilpotent. This includes (25) for
every polynomial slice. If the correction preserves \(A\),
its restriction is not locally nilpotent either, since \(u\in A\).

These fields even have unit derivative ideal. Put \(g=uv-1\);
the identity
\(u^2(v^2-2v^2g)+g^2(3+2g)=1\) uses only their values on
\(u,v\). Removing a common factor cannot repair the failure,
and a nonzero polynomial multiple still fails the LND divisibility
criterion on \(u\).

The [complete obstruction proof](research/leading-plane-repair-obstruction-pass42.md)
does not obstruct arbitrary corrections, another frame, or cancellation.
The example already has a polynomial quotient. It proves that this
particular leading-field repair cannot supply the missing intrinsic
LND, even with unrestricted polynomial coefficients and slice choice.

## 10. The remaining mathematical obligations

The supplied \((1,1,2,2)\) profile is still unresolved in full.
Its dependent-defect branch needs a nonlinear coordinate argument
beyond constant recombination. The independent degree-two branch
retains algebraically independent speeds and only one leading intrinsic
direction. Higher-degree power-law branches need a global argument,
not just the normalized rank calculation.

Even a complete solution of that supplied profile would leave the
separate universal question: why should an arbitrary sliced action
admit a recognized frame, or a transformation reducing it to one?
No bound on the needed frame height has been proved for all candidates
in (1). Any successful completion must address this question or provide
a different unrestricted argument.

The proofs above are conditional mathematical deductions using stated
classical recognition theorems. Exact symbolic examples test formulas
and boundary cases; they do not prove those classical theorems or
unrestricted cancellation. Bibliographic novelty and human verification
remain separate unresolved obligations.

## Sources

[^1]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2), Theorem 2.5, PDF p. 5, and Theorem 2.7, PDF p. 6. These state the slice theorem and the established planar triangularization theorem. The retained version is the exact theorem source used here.

[^2]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and proof, PDF p. 11. The application requires a nonzero original LND, an actual invariant ambient coordinate and a regular original kernel.

[^3]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), author manuscript dated October 5, 2001, Proposition 3.5 and Theorem 3.6, PDF pp. 4-5. Two independent commuting LNDs of the actual complex polynomial three-ring have joint kernel generated by an actual coordinate.

[^4]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), Theorem 3.1(i), PDF p. 5, attributed to Z. Wang. A nonzero three-variable nice LND has an invariant nonzero linear form; this part needs neither a slice nor irreducibility. The earlier one-good-partial lemma also uses Hamann's relative cancellation theorem, stated as Theorem 2.6, PDF p. 4, only over its established base ring.
