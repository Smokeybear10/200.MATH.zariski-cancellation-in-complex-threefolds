# A common highest field and a four-entry normal identity

The highest second adjoints of an actual nice sliced action have one
common polynomial locally nilpotent direction. This conclusion does not
require a supplied constant good direction. Its intrinsic quotient is
the actual invariant plane furnished by the retained quotient theorem,
and all four original velocities belong to that plane.

The resulting normal row gives an exact polynomial syzygy. At a proper
zero of that row, its first nonzero homogeneous terms can span at most
two dimensions. This is a necessary local condition, not an exclusion
of every proper normal ideal or a recognition theorem. In particular,
the argument does not supply an apex or a constant good partial.

## 1. Actual hypotheses and the common line

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E=P\cdot\partial\in\operatorname{LND}(B),\qquad
E(s_*)=1,\qquad E(P)=0,\qquad A=\ker E.
\tag{1}
\]
Write \(J=\operatorname{Jac}_xP\), and assume \(J^2\ne0\).
The [sliced rank theorem74](nice-slice-adjoint-rank-pass74.md) and
[leading-boundary argument76](nice-leading-boundary-pass76.md) give,
over \(K=\operatorname{Frac}B\),
\[
J^3=0,\quad \operatorname{rank}J=2,\quad
\operatorname{rank}J^2=1,\quad
P\notin\operatorname{im}J,\quad E(J)=-J^2.
\tag{2}
\]
The nonmembership in (2) uses the original slice and the highest
vertical-adjoint exclusion, not only the nilpotent Jordan type.
No assumption about the constant kernel of \(J^2\) is made here.

Put \(C_i=(J^2e_i)\cdot\partial\), allowing zero fields.
Each nonzero \(C_i\) is an actual LND of B. Indeed the original
coordinate partial \(T_i\) has exact conjugate
\[
\exp(tE)T_i\exp(-tE)
=T_i-t(Je_i)\cdot\partial+t^2C_i.
\tag{3}
\]
On \(B[z,z^{-1}]\), conjugation with \(\exp(E/z)\), followed by
multiplication by the invariant unit \(z^2\), gives an LND that
preserves \(B[z]\). Its quotient at z=0 is precisely \(C_i\).
This proves local nilpotence by an actual restriction and quotient,
not by assuming arbitrary coefficient specializations preserve it.
Also \(E(J^2)=0\), and \(J(J^2e_i)=0\), so
\([E,C_i]=0\) and \(C_i(P)=0\).

Choose a nonzero column and divide the gcd of its four polynomial
coefficients in B. This gives a primitive polynomial field R.
Both that gcd and the coefficients of R belong to A: factorial
closure of \(\ker E\) applies to every nonzero column entry.
If the selected column is gR, then gR is an LND and
\((gR)(g)\in gB\). LND self-divisibility forces \(R(g)=0\).
Consequently \((gR)^n(b)=g^nR^n(b)\) for every b, proving that
R is an LND too.

Primitivity and unique factorization imply that every other column
has the form \(C_i=f_iR\) with \(f_i\in B\). To see the regularity,
write its rational multiplier as a reduced fraction. Its denominator
would divide every coefficient of R, and is therefore a unit.
We obtain
\[
C_i=f_iR,\qquad f_i\in B,\qquad
E(R(x_j))=0,\quad J R(x)=0,\quad
[E,R]=0,\quad R(P)=0.
\tag{4}
\]
Both the coefficient invariance and the equality \(JR(x)=0\)
are used in the commutator conclusion. Coefficient invariance alone
would not suffice.

For nonzero \(f_i\), the equality \([E,C_i]=0\) gives
\(E(f_i)=0\). Self-divisibility for the LND \(f_iR\), now applied
to \(f_i\), gives \(R(f_i)=0\). Zero multipliers satisfy both
identities as well. The construction is therefore an equality of
actual ambient directions, not only their classes modulo E.

## 2. The actual common quotient plane

R is not rationally parallel to E, by (2). Its restriction
\(r=R|_A\) is a nonzero LND. If it were zero, the original slice
presentation \(B=A[s_*]\) would give
\(R=R(s_*)E\), a contradiction. Define
\[
S=\ker r=A\cap\ker R.
\qquad
S\simeq\mathbb C[u,v],\quad
S\subset A\subset B\text{ faithfully flat},\quad
P_i,f_i\in S.
\tag{5}
\]
The last membership uses \(EP=RP=0\) and the preceding argument.
The plane and faithful-flatness conclusions are the exact
[intrinsic quotient theorem](intrinsic-quotient-surface-pass.md),
applied to the actual cylinder \(A[s_*]=B\) and the nonzero r.
The fibers of \(\operatorname{Spec}B\to\operatorname{Spec}S\)
are nonempty and purely two-dimensional: they are the intrinsic
curve fibers times the supplied slice line.

There is also an exact unit-row consequence in S. The original
slice equation gives \(\sum_i(\partial_{x_i}s_*)P_i=1\) in B.
Because every \(P_i\) belongs to S, faithful-flat contraction
gives \((P_1,P_2,P_3,P_4)S=S\). Choose \(\lambda_i\in S\)
with \(\sum_i\lambda_iP_i=1\). Then
\(\sigma_0=\sum_i\lambda_ix_i\) is an actual global E-slice,
expressed S-linearly in the original coordinates. This does not
make \(\sigma_0\) an ambient coordinate, prove
\(R(\sigma_0)=0\), or make the normal row below unimodular.

Ambient primitivity of R must be distinguished from primitivity of
r on A. The latter can have nonconstant content: one may write
\(r=hD\) with D primitive on the UFD A and \(h\in\ker D=S\).
No assertion that h is a unit, or that either intrinsic action is
free, follows from (4). This is the same saturation distinction
retained in [commuting-leading25, Section 4](commuting-leading-pass25.md)
and [primitive-fiber54](primitive-fiber-nonvanishing-pass54.md).

## 3. A normal row without a binary parametrization

Choose polynomial generators u,v of the actual S in (5). View
P as a polynomial vector in u,v, and set
\[
U=[P_u,P_v],\qquad L=\operatorname{Jac}_x(u,v),\qquad
J=UL,\qquad
N\cdot q=\det[P,P_u,P_v,q]\quad(q\in S^4).
\tag{6}
\]
Thus N is the signed four-entry cofactor row of the first three
columns. The matrix L has rank two in characteristic zero, so
\(\operatorname{im}_KJ=\operatorname{im}_KU\). Equations (2)
imply that \([P,P_u,P_v]\) has rank three. Hence \(N\ne0\).
The row annihilates P, both derivative columns, and R(x), since
\(R(x)\in\operatorname{im}J^2\subseteq\operatorname{im}J\).
There is no division by a parameter Jacobian or by the content of N.

All entries of N lie in S. Therefore
\(c=N\cdot x\) is killed by E and R, and belongs to S. It also
belongs to the extension of the ideal generated by N. Faithful
flatness in (5) contracts that ideal exactly. There are actual
\(a_1,\ldots,a_4\in S\) such that
\[
c\in(N_1,N_2,N_3,N_4)S,\qquad
c=\sum_iN_i a_i,\qquad
\boxed{\sum_iN_i(x_i-a_i)=0\text{ in }B.}
\tag{7}
\]
This is the four-entry counterpart of the invariant-normal identity
in [normal-syzygy78](binary-normal-syzygy-exclusion-pass78.md).
The latter's three independent homogeneous binary normal entries
are not available here. No binary representation or good partial
has been smuggled into (6)--(7).

## 4. A precise first-order-of-vanishing restriction

Let \(\mathfrak m=(u-u_0,v-v_0)\) be a maximal ideal of S
containing every \(N_i\), and let d be the smallest
\(\mathfrak m\)-adic order of a nonzero entry. Let
\(N_i^{[d]}(\xi,\eta)\) be its degree-d homogeneous term,
using zero when its order is larger. Then
\[
\boxed{
\dim_{\mathbb C}\operatorname{span}
\{N_1^{[d]},N_2^{[d]},N_3^{[d]},N_4^{[d]}\}\le2.
}
\tag{8}
\]
Here the terms are formed in the actual polynomial plane S, not
in a presumed coefficient field inside an ambient local ring.

For the proof choose a minimal prime \(\mathfrak n\) of
\(\mathfrak mB\). Its height is two by (5), and its contraction
to S is \(\mathfrak m\). The regular local ring
\(B_{\mathfrak n}\) has dimension two. The images of
\(u-u_0,v-v_0\) are a system of parameters and a regular sequence.
Consequently, writing \(I=\mathfrak mB_{\mathfrak n}\),
\[
\operatorname{gr}_I B_{\mathfrak n}
=(B_{\mathfrak n}/I)[\xi,\eta],\qquad
\sum_iN_i^{[d]}(\xi,\eta)\,
\overline{x_i-a_i}=0.
\tag{9}
\]
This is the complete-intersection associated-graded identity used
in normal-syzygy78, including a possibly nonreduced coefficient
ring. The displayed relation is the degree-d part of (7).

If the dimension on the left of (8) were at least three, its
coefficient matrix would have three independent complex rows.
Taking the corresponding coefficients in (9) would put three
independent constant linear combinations of \(x_i-a_i\) in I.
Contracting from \(B_{\mathfrak n}\) to B and replacing each
\(a_i\) by its complex value at \(\mathfrak m\) puts three
independent affine linear equations in \(\mathfrak n\).
Their ideal has height three in the actual four-coordinate
polynomial ring, contradicting \(\operatorname{ht}\mathfrak n=2\).
This proves (8).

The statement permits rank one or two at a proper zero. It does
not imply that the normal ideal is the unit ideal, and no
arbitrary coefficient row realizing those ranks is being promoted
to an actual nice sliced action.

## 5. Deduplication and the remaining gate

Highest-field degeneration and primitive UFD division are retained
mechanisms, not new source theorems. The additional conclusion here
is their simultaneous application to the whole actual Jacobian
square without a good partial, followed by the actual quotient-plane
normal identity and the explicit local restriction (8).

By [good-direction recognition79](nice-good-direction-recognition-pass79.md),
a hypothetical nonpolynomial kernel within a supplied nice frame
must have no nonzero constant good direction. All four original
partials then have nonzero second adjoints and zero third adjoints.
This does not raise the all-frame recognition threshold or establish
the existence of a nice frame for an arbitrary sliced action.

No freeness, ambient coordinate, global adapted slice, apex existence,
or general cancellation theorem follows from this note. No new
numerical suite, full regression, primary-source reread, historical
novelty, human expert review or formal proof verification is claimed.
All files through pass78 and shared metadata remain unchanged.
