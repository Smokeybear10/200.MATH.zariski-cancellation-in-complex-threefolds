# A finite root extension forces actual common powers

In the remaining dependent moving-top cases, a root of the highest
coefficient may first be adjoined in a finite algebraic field extension.
The full normalized companion then makes the preceding transverse layer
constant. Its nonzero bad component expresses that root as a rational
function in the original ring. Normality finally makes the root an
actual polynomial.

Thus the rotating alternatives of the preceding-curve reduction cannot
occur under the full supplied frame, for either moving order three or
four. This statement does not recognize the remaining common-power
quartic. Its cubic consequence uses the separate completed recognition
transfer.

## 1. Actual assumptions and the inherited weighted identities

Let
\[
B=k[x_1,x_2,x_3,x_4],\qquad k=\mathbb C,\qquad
K=\operatorname{Frac}B,\qquad E\in\operatorname{LND}(B),
\qquad E(s_*)=1.
\]
The displayed generators are actual polynomial coordinates, with
\(T_i=\partial_{x_i}\), and
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Write \(W_i=[E,T_i]\), \(V_i=[E,W_i]\) for bad \(i=3,4\).
Retain the dependent primitive decomposition
\[
V_3=aD,\qquad V_4=bD,\qquad
D\in\operatorname{LND}(B)\text{ primitive},\qquad
[E,D]=0,\qquad a,b\in\ker E\cap\ker D.
\tag{2}
\]
The cases with a nonzero complex constant relation between the
two defects are already recognized by the mixed slice theorem.
Assume no such relation; in particular \(a,b\ne0\).

The complete [dependent highest-vector reduction](dependent-defect-top-line-pass43.md)
gives the following exact data for a nonconstant highest vector
of order at least three:
\[
m\in\{3,4\},\qquad z=E^{m-1}x,\qquad
E^mx=cq,\qquad E^{m+1}x=0,
\]
\[
0\ne c\in k^4,\quad c_3=c_4=0,\qquad
q\in(\ker E\cap\ker D)\setminus k,\qquad Dz=c\theta.
\tag{3}
\]
Here \(\theta\in B\), with \(E\theta=0\); \(D\theta=0\)
is not assumed. Put \(\ell_0=(0,0,a,b)\). The full original
weighted row and primitive divisibility argument give
\[
\rho=\ell_0 z=qr,\qquad
r\in\ker E\cap\ker D,\qquad
[E,T_c]=-\frac{m-1}{2}rD.
\tag{4}
\]
The zero-\(r\) case is already recognized, so retain \(r\ne0\).
The original-slice argument in that same reduction proves that
\(E,D\) are independent over \(K\).

The original bad-column coefficient also gives, for
\(a_3=a,a_4=b\),
\[
V_i z=-\frac2m W_i(E^mx),\qquad
W_iq=-\frac m2a_i\theta.
\tag{5}
\]
The second equality uses the nonzero constant vector \(c\).
All identities above were proved with the variable weighted
auxiliary row retained. In particular the original lower row
\(\ell_0\operatorname{Jac}z\) was not replaced by
\(d(\ell_0z)\).

**Theorem.** There exists an actual polynomial
\(g\in(\ker E\cap\ker D)\setminus k\) such that
\[
q=g^m,\qquad z=c\tau+e\,g^{m-1},
\quad
\tau=z_j/c_j\in B,\quad E\tau=q,
\quad e\in k^4,\quad e_j=0,\quad (e_3,e_4)\ne(0,0),
\tag{6}
\]
where \(j\in\{1,2\}\) is any fixed index with \(c_j\ne0\).
In particular the preceding bad pair has actual common powers.

The proof does not assume this polynomial root exists at the start.

## 2. Work first in a genuine finite field extension

Choose one root \(g\) of \(T^m-q\) in an algebraic closure of \(K\),
and set
\[
L=K(g),\qquad R=B[g,g^{-1}]\subset L,\qquad g^m=q.
\tag{7}
\]
The extension \(L/K\) is finite and separable. Irreducibility of
\(T^m-q\) is not required; its chosen root has some finite
separable minimal polynomial. No equality \(R\simeq k^{[4]}\)
is asserted.

Each \(k\)-derivation \(U\) of \(K\) extends uniquely to \(L\).
Indeed, if \(p(T)\in K[T]\) is the minimal polynomial of \(g\),
its value must be \(U(g)=-U(p)(g)/p'(g)\), where \(U(p)\)
means coefficientwise differentiation. Separability makes the
denominator nonzero. This formula defines a derivation on
\(K[T]/(p)\), since it kills the defining relation, and hence
on its fraction field. For the coordinate partials, differentiating
\(g^m=q\) then gives the explicit formula
\[
T_i g=\frac{T_i q}{m g^{m-1}}.
\tag{8}
\]
It shows that each extended \(T_i\) preserves \(R\), including
its generator \(g^{-1}\). The extensions commute, because their
commutators restrict to zero on \(K\), and a derivation of a
separable algebraic extension vanishing on the base field is zero.
No extended \(T_i\) is asserted to be locally nilpotent on \(R\).

Since \(Eq=Dq=0\), the extended fields satisfy \(Eg=Dg=0\).
Consequently \(E,D\) remain LNDs on \(R\), and
\[
\delta=E/g\in\operatorname{LND}(R),\qquad
[\delta,D]=0,\qquad
\delta^mx=c,\qquad
y:=\delta^{m-1}x=z/g^{m-1},\qquad \delta y=c.
\tag{9}
\]
Local nilpotence here follows from the original polynomial action
and the fixed adjoined generators, not from a coordinate presentation
of \(R\).

The extended partials form an \(L\)-basis of
\(\operatorname{Der}_k(L)\). Indeed, for any such derivation \(U\),
the difference
\(U-\sum_i U(x_i)T_i\) vanishes on \(K\), and hence on \(L\).
Their independence follows by evaluation on the four \(x_i\).
Thus the ordinary coordinate chain rule remains valid on \(L\).

## 3. The normalized defects have rank one

The highest original good-column identity gives \(W_iq=0\)
for \(i=1,2\), hence \(W_i g=0\) there. The bad defects kill
\(g\), because \(Dg=0\).
For bad \(i\), equations (5),(8) give
\[
W_i g=-\frac{a_i\theta}{2g^{m-1}}.
\]
The direct rescaling formulas on \(L\) are
\[
\operatorname{ad}_\delta^2T_i
=g^{-2}\operatorname{ad}_E^2T_i
 +2g^{-3}(W_i g)E,
\]
\[
\operatorname{ad}_\delta^3T_i
=g^{-3}\operatorname{ad}_E^3T_i
 +3g^{-4}(V_i g)E
\quad\text{for bad }i.
\tag{10}
\]
These are identities of extended derivations, not a
local-nilpotence assertion about the partials.

It follows that all normalized adjoint bounds in (1) persist.
Moreover, writing \(a_3=a,a_4=b\),
\[
\widetilde V_i:=\operatorname{ad}_\delta^2T_i
=\frac{a_i}{g^2}\,\mathcal D,\qquad
\mathcal D=D-\frac{\theta}{q}E.
\tag{11}
\]
Independence of \(E,D\) remains true after field extension.
Therefore \(\mathcal D\ne0\), and its line is independent
of \(\delta\). The normalized defect pair has rank exactly one
over \(L\), with either nonzero multiplier sufficient for that
rank conclusion. Its coefficients preserve \(R\), since
\(\theta/q=\theta/g^m\in R\).

Nothing in this calculation puts \(a,b\) into a univariate
parameter ring or makes the variable auxiliary row constant.

## 4. The extended chain rule gives the full polynomial inverse

Let \(P=\delta x\), \(J=(T_iP_j)_{j,i}\), let
\(d=\mathcal D(x)\), and set
\[
\ell=(0,0,a/g^2,b/g^2),\qquad
M=\begin{pmatrix}J&-d/2\\ \ell&0\end{pmatrix}
\in\operatorname{Mat}_5(R).
\tag{12}
\]
The extended partials form the chain-rule basis proved above.
The conjugated fields
\(\exp(t\delta)T_i\exp(-t\delta)\) preserve \(R[t]\)
and have the finite coefficient matrix
\[
C(t)=I-tJ+\frac{t^2}{2}d\ell.
\tag{13}
\]
Only the normalized adjoint bounds are used to truncate this
matrix. The original extended partials need not be LNDs.

Put \(F_t=\exp(t\delta)x\in R[t]^4\), and define
\(\operatorname{Jac}F_t=(T_i(F_t)_j)_{j,i}\).
Conjugation gives
\[
\bigl(\exp(t\delta)T_i\exp(-t\delta)\bigr)((F_t)_j)
=\delta_{ij}.
\]
The chain rule on \(L\) therefore gives
\[
(\operatorname{Jac}F_t)C(t)=I.
\tag{14}
\]
These are square matrices over the commutative domain \(R[t]\).
Their determinants multiply to one, and evaluation at \(t=0\)
gives one for each. Units of the polynomial ring over a domain
are constant in \(t\), so both determinants equal one.
Both matrix multiplication orders in (14) are consequently valid.

This is an actual inverse matrix identity derived from the
automorphism \(\exp(t\delta)\) of \(R[t]\). It is not an
assumption that the \(F_t\) define polynomial coordinate changes
of the original \(B\), nor that the automorphism fixes \(K\).
No claim is made that exponentials of arbitrary elements of
the full field \(L\) are polynomial in \(t\).

Schur elimination of the last coordinate gives
\(\det(I-tM)=\det C(t)=1\). Cayley--Hamilton and the upper block
of the formal resolvent then yield
\[
M^5=0,\qquad
(M^j)_{\mathrm{UL}}
=\frac{\operatorname{Jac}(\delta^jx)}{j!}
\quad(j\ge0).
\tag{15}
\]
This retains the complete variable row \(\ell\).
No derivative of that row is inserted into a matrix product.

## 5. Two-sided descent and the rank-one preceding image

For clarity, the needed block lemma is valid over any field.
If a matrix \(N\) satisfies \(MN=NM=0\), then
\[
\operatorname{rank}N=\operatorname{rank}N_{\mathrm{UL}}.
\tag{16}
\]
Indeed \(\ker M\) has no nonzero vector supported solely on
the fifth coordinate, because \(d\ne0\). Projection of
\(\operatorname{im}N\subset\ker M\) to the first four
coordinates is therefore injective and preserves rank.
The rows of this projected matrix lie in the left kernel of
\(M\). That left kernel has no nonzero row supported solely
on the fifth coordinate, because \(\ell\ne0\).
Projection of those rows to the first four coordinates again
preserves rank, proving (16).

By (9), every \(\operatorname{Jac}(\delta^jx)\) with \(j\ge m\)
vanishes. Start with \(M^5=0\) and descend:
if \(M^{s+1}=0\) and \(s\ge m\), apply (16) to \(N=M^s\).
Its upper block vanishes by (15), so \(M^s=0\).
Thus \(M^m=0\).

On the other hand,
\[
\operatorname{Jac}(y)P=\delta y=c\ne0.
\]
Hence \(M^{m-1}\ne0\). In dimension five, for \(m=3\) or \(4\),
a nilpotent matrix with nilpotence index \(m\) has exactly one
Jordan block of size \(m\); two such blocks would require
dimension at least six. Therefore
\[
\operatorname{rank}M^{m-1}
=\operatorname{rank}\operatorname{Jac}(y)=1.
\tag{17}
\]
For the second equality apply (16) to \(M^{m-1}\).
Its upper block differs from \(\operatorname{Jac}(y)\) only
by the nonzero constant \((m-1)!\).

The image of \(\operatorname{Jac}(y)\) is exactly \(Lc\),
since it contains the nonzero vector \(c\).
Fix \(j\) with \(c_j\ne0\), and put
\(\sigma=y_j/c_j\in R\). It follows that
\[
T_i(y-c\sigma)=0\quad\text{for every }i=1,2,3,4.
\tag{18}
\]

## 6. Common extended-partial constants are still complex

Here is the field-constant argument, without a rationality
assumption on \(L\). Suppose \(\alpha\in L\) is killed by all
extended \(T_i\). Let
\[
p(T)=T^d+\sum_{\nu=0}^{d-1}p_\nu T^\nu\in K[T]
\]
be its monic minimal polynomial. Differentiating \(p(\alpha)=0\)
by \(T_i\) gives
\(\sum_{\nu<d}(T_i p_\nu)\alpha^\nu=0\).
Minimality implies \(T_i p_\nu=0\) for every \(\nu,i\).
The common constants of the four ordinary partials on
\(K=k(x_1,x_2,x_3,x_4)\) are exactly \(k\), so every
\(p_\nu\in k\). Thus \(\alpha\) is algebraic over \(k\);
algebraic closedness of \(k=\mathbb C\) makes \(\alpha\in k\).

Apply this to (18). There is an actual constant vector
\(e\in k^4\), with \(e_j=0\), such that
\[
y=c\sigma+e,\qquad
z=c\tau+e g^{m-1},\qquad
\tau=z_j/c_j,\qquad \sigma=\tau/g^{m-1}.
\tag{19}
\]
Since the two bad components of \(c\) vanish,
\(z_i=e_i g^{m-1}\) for \(i=3,4\).

## 7. A nonzero bad component descends the root

If \(e_3=e_4=0\), then \(z_3=z_4=0\) and
\(\rho=a z_3+b z_4=0\), contradicting \(\rho=qr\ne0\).
Choose a bad index \(i\) with \(e_i\ne0\).
Equation (19) now gives
\[
g=\frac{e_iq}{z_i}\in K.
\tag{20}
\]
Here \(z_i=e_i g^{m-1}\ne0\), so the displayed division is
legitimate. This proves membership in the original fraction
field before any normality argument.

The element \(g\in K\) satisfies the monic equation
\(g^m-q=0\) over \(B\). The original polynomial ring \(B\)
is normal, so \(g\in B\). Its already established derivatives
\(Eg=Dg=0\) remain zero on the original ring. Since \(q\)
is nonconstant, \(g\) is nonconstant. Equations (19)--(20)
prove every assertion in (6).

In particular a polynomial root is a conclusion of the full
frame, not a normalization made before the proof. The adjoined
ring \(R\) may then be identified with \(B_g\), but that
identification was not available when the rank argument began.

## 8. Consequences and exact remaining scope

The actual invariant transverse layer \(k_0=z-c\tau\) satisfies
\(k_0=e g^{m-1}\). Since some bad component of \(e\) is nonzero,
\[
\operatorname{Frac}k[q,(k_0)_1,\ldots,(k_0)_4]=k(g).
\]
This follows directly from (20) and the common powers, without
a new polynomial curve-factorization theorem.

The earlier [preceding-curve theorem](dependent-preceding-curve-pass44.md)
already put \(q=Q(u)\) and \(k_0=K(u)\) into an actual polynomial
parameter algebra. In that notation the weighted expressions
\(mQK_i'-(m-1)Q'K_i\) for bad \(i\) must now vanish.
For example, (20) gives \(g\in k(u)\); the retained polynomial
intersection \(B\cap k(u)=k[u]\) gives \(g=G(u)\), after which
\(Q=G^m\) and \(K_i=e_iG^{m-1}\) give the vanishing directly.

Thus its rotating alternative is excluded for actual remaining
dependent moving orders three and four. The formal rotating data
used in older checkers were explicitly not asserted to realize
the full original frame; their existence does not contradict this
additional consequence of all the extended Jacobian identities.

For \(m=3\), the separately proved
[common-power cubic transfer](dependent-common-power-cubic-pass70.md)
recognizes the original kernel. Together with the already recognized
constant-relation and zero-\(r\) cases, this recognizes the dependent
moving cubic sector covered by the high-top reduction.

For \(m=4\), this proof supplies an actual common-power normalization
and the full transverse layer (19), but does not recognize its
kernel. In particular no polynomial-ring recognition theorem is
applied to \(R\), and no actual coordinate is inferred merely
from the localized slice \(\sigma\).
The higher independent moving sectors and the existence of a
universal suitable frame are also outside this theorem.

## Proof and verification provenance

The original complete weighted reduction and preceding-curve note
were reread before this argument. The needed field extension,
chain-rule basis, polynomial matrix inverse, two-sided block descent,
common-constant and original-normality arguments are supplied above.
The curve theorem is only used to compare the final conclusion with
the older parameter notation, not to manufacture the adjoined root.

The cubic recognition corollary retains the original-slice,
one-good-output, plane and invariant-coordinate source gates of its
separate proof. This note makes no fresh full-primary-paper audit
claim for those inherited recognition theorems.

The proof is a bounded algebraic deduction under the actual supplied
frame. It adds no numerical method or regression claim by itself,
no shared metadata change, human expert-review claim,
proof-assistant verification or historical novelty verdict.
The pass69 packet and earlier frozen files are unchanged.
