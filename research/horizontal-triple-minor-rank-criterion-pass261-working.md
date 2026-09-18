# Exact horizontal triple minors in an arbitrary positive-time frame

For an actual globally sliced polynomial four-ring with positive coordinate
time degrees, the sum of three selected partial shifts is at least one less
than the omitted coordinate's time degree. Equality holds exactly when the
three intrinsic leading actions are generically independent. In that event
their commuting additive actions recognize the kernel as affine three-space.

This is a necessary-condition and recognition criterion at arbitrary time
degrees. It does not show that equality occurs in some coordinate frame.
Strict inequality can hold for all four triples even when the kernel is
already polynomial. No arbitrary-entry or cancellation solution is claimed.

## 1. Actual hypotheses and the retained leading construction

Let
\[
B=\mathbb C[X_1,X_2,X_3,X_4]=A[u],\quad E=\partial_u,\quad
K=\operatorname{Frac}A,\quad d_i=\deg_E X_i>0.
\tag{1}
\]
For each literal coordinate partial \(T_i=\partial_{X_i}\), use the exact
horizontal shift \(k_i\) from the fully read
[arbitrary-positive-weight theorem158](arbitrary-positive-weight-initial-bound-pass158-working.md):
\[
\begin{gathered}
T_i|_A=\sum_{r=0}^{k_i}u^rD_{ir},\qquad
0\ne N_i:=D_{i,k_i}\in\operatorname{LND}_{\mathbb C}(A),\\
k_i\ge0,\qquad T_i(u)\in A[u]_{\le k_i}.
\end{gathered}
\tag{2}
\]
The shifts are horizontal degrees, not merely upper cofactor estimates.
That theorem proves (2) on the actual ring by degeneration of the coordinate
LNDs, and proves that the leading actions kill all four leading coefficients.
The latter annihilation is not needed for the minor identity below.

Choose a separating transcendence basis \(\xi_1,\xi_2,\xi_3\) for
\(K/\mathbb C\), and put
\[
M=\frac{\partial(X_1,X_2,X_3,X_4)}
        {\partial(\xi_1,\xi_2,\xi_3,u)},\qquad \det M=J_0\in K^*.
\tag{3}
\]
The determinant is independent of \(u\): the actual polynomial flow
\(\exp(sE)\) has Jacobian one, fixes \(K\), and translates \(u\).
The separating partials extend uniquely to the finite separable field
extension; they are not asserted to preserve \(A\).

Let \(H\) be the first three rows of \(M^{-1}\).
Its \(i\)-th column is
\((T_i\xi_1,T_i\xi_2,T_i\xi_3)^\mathsf{t}\).
These entries are in \(K[u]\) and have maximum degree exactly \(k_i\).
Indeed the chain rule transfers the bound from \(A\) to \(K\), and a
derivation of the separable field extension that kills every \(\xi_j\)
is zero. Thus the column of \(N_i\) in this basis is nonzero.

## 2. The complementary-minor identity is exact

For an index \(\ell\), delete column \(\ell\) from \(H\), retaining the
other columns in their original order. The complementary-minor identity
for an inverse matrix gives
\[
\boxed{\det H_{\widehat\ell}
 =(-1)^{4+\ell}\frac{M_{\ell4}}{\det M}
 =(-1)^{4+\ell}\frac{E(X_\ell)}{J_0}.}
\tag{4}
\]
One can obtain the sign directly by expanding the wedge of the three
horizontal dual rows and then adjoining \(du\); it is also the
cofactor sign with omitted row four and column \(\ell\).
No leading-term approximation is used in (4).

In characteristic zero the right side has exact \(u\)-degree
\(d_\ell-1\), since \(d_\ell>0\). The degree of the determinant on the
left is at most the sum of its three column degrees. Moreover its
coefficient at that sum is the determinant of the three leading columns.
Consequently
\[
\boxed{
\sum_{i\ne\ell} k_i\ge d_\ell-1,\qquad
\bigwedge_{i\ne\ell}N_i\ne0
\ \Longleftrightarrow\ 
\sum_{i\ne\ell}k_i=d_\ell-1.}
\tag{5}
\]
Here the wedge is over \(K\), in increasing index order.
If the sum is strictly larger, the top determinant vanishes.
If it equals \(d_\ell-1\), (4) makes that coefficient nonzero.
These are both directions of the equivalence, not just a sufficient bound.

## 3. Equality supplies a global recognition endpoint

The leading actions commute. For \(f\in A\), the coefficient of
\(u^{k_i+k_j}\) in \([T_i,T_j]f=0\) is
\([N_i,N_j]f\). Terms differentiating the explicit powers of \(u\)
have degree at most \(k_i+k_j-1\), by the vertical bound in (2).
When both shifts are zero these derivative terms vanish.
Thus
\[
[N_i,N_j]=0\quad\text{for every }i,j.
\tag{6}
\]

If equality holds for one index in (5), three of these commuting LNDs
give a \(\mathbb G_a^3\)-action on \(\operatorname{Spec}A\) with a
three-dimensional orbit. The orbit is open. Orbits of a unipotent
algebraic group on an affine variety are closed, by the
Kostant--Rosenlicht theorem, recalled explicitly in
[Arzhantsev's introduction](https://arxiv.org/html/2102.11330v1).
Since \(\operatorname{Spec}A\) is irreducible, that orbit is the whole
variety. Its stabilizer is zero-dimensional, hence trivial in a vector
group in characteristic zero. The orbit is therefore \(\mathbb A^3\):
\[
\boxed{\text{Equality in any one of (5) implies }A\simeq\mathbb C^{[3]}.}
\tag{7}
\]
This is the retained rank-three endpoint from
[intrinsic-actions-pass, Section 5](intrinsic-actions-pass.md),
now detected by an exact numerical condition.

For a hypothetical nonpolynomial kernel all four inequalities must
therefore be strict. Integrality yields
\[
\sum_{i\ne\ell}k_i\ge d_\ell\quad(1\le\ell\le4),\qquad
\sum_{\ell=1}^4 d_\ell\le3\sum_{i=1}^4k_i.
\tag{8}
\]
Neither (8) nor the upper shift bounds of158 give an upper bound on the
minimum coordinate time-degree sum.

## 4. The minors are unimodular, but a basis change need not be coordinates

The slice chain rule gives the actual identity
\[
1=Eu=\sum_{\ell=1}^4 E(X_\ell)T_\ell(u).
\tag{9}
\]
Equations (4) and (9) show that the four maximal minors of \(H\)
generate the unit ideal in \(K[u]\). Thus \(H\) is a split surjection
\(K[u]^4\longrightarrow K[u]^3\), and polynomial module operations
over this field polynomial ring can put it in a full-rank normal form.

Such module operations are not automatically actual coordinate changes.
They can introduce rational functions of invariants, and even a
polynomial invertible change of a derivation basis need not preserve
commutativity or local nilpotence. The elementary basis
\[
\partial_a,\quad a\partial_a+\partial_b,\quad\partial_c,\quad\partial_u
\tag{10}
\]
of derivations of \(\mathbb C[a,b,c,u]\) has determinant one relative to
the coordinate basis. Its second member is not locally nilpotent,
since every positive iterate on \(a\) is \(a\). Its bracket with the
first member is \(\partial_a\ne0\).
Consequently row reduction of the polynomial matrix cannot be promoted
to a degree-lowering polynomial automorphism without a separate
integrability and ring-return argument.

## 5. Equality and strict-inequality actual controls

For the translation \(E=\partial_u\) on \(\mathbb C[a,b,c,u]\), take
\[
(X_1,X_2,X_3,X_4)=(a+u,b+u,c+u,u).
\tag{11}
\]
Every \(d_i=1\); all \(k_i=0\). The leading restrictions are
\(\partial_a,\partial_b,\partial_c,-\partial_a-\partial_b-\partial_c\).
Every triple is independent and every equality in (5) holds.

In contrast, use the actual triangular frame
\[
x_1=a,\quad x_2=b+a^2u,\quad x_3=c+bu,\quad x_4=u,
\]
then the invertible linear change
\[
X_1=x_1-x_2-x_3-x_4,\quad X_2=x_2,\quad X_3=x_3,\quad X_4=x_4.
\tag{12}
\]
Its polynomial inverse is obtained from
\[
a=x_1,\quad u=x_4,\quad b=x_2-x_1^2x_4,\quad
c=x_3-x_2x_4+x_1^2x_4^2,\quad
x_1=X_1+X_2+X_3+X_4.
\]
Every \(d_i=1\), but every \(k_i=2\) and every
\(N_i=2a\partial_c\), as follows by differentiating the inverse.
Thus every left sum in (5) is six, while \(d_\ell-1=0\).
The minors still have exact degree zero through cancellations.
This is the explicit rank-collapse control from the fully inspected
Section 6 of intrinsic-actions-pass, not a new counterexample.
Its kernel is the ordinary polynomial three-ring.

## 6. Scope

The new content is the exact complementary-minor criterion (5) and its
connection to the global rank-three endpoint, including the split-module
boundary. The old leading-LND construction and unipotent orbit theorem
are identified inputs. The countercontrols show why this is not an
arbitrary-coordinate reduction algorithm.

No classification of the remaining rank-one and rank-two cases follows.
No historical novelty, independent human review, proof-assistant
certification or unrestricted cancellation theorem is claimed.
