# The full companion image forces a single power-law top

For an actual two-quadratic frame with independent defect columns, a
nonconstant highest flow vector cannot rotate in its two-dimensional
output plane. The full six-dimensional companion matrix forces that
vector and the preceding pair of bad-coordinate coefficients into one
image line. Unique factorization in the original polynomial ring then
gives an exact common power law.

This is a reduction of the supplied-frame problem, not a solution of
the remaining two-quadratic sector. In particular, dividing the action
by the new invariant factor preserves the adjoint bounds but can lower
the defect rank from two to one. The exact criterion is the generic
rank of the original action together with those two columns.

## 1. Actual hypotheses and conclusions

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
0\ne E\in\operatorname{LND}(B),\qquad T_i=\partial_{x_i},
\]
and assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Put
\[
P=E(x),\quad J=\operatorname{Jac}P,\quad h_j=E^j(x),
\quad V_i=\operatorname{ad}_E^2T_i\quad(i=3,4),
\]
\[
\mathcal V=[V_3(x)\mid V_4(x)],\qquad
L_0=\begin{pmatrix}0&0&1&0\\0&0&0&1\end{pmatrix},
\qquad \operatorname{rank}\mathcal V=2.
\tag{2}
\]
Ranks are over \(K=\operatorname{Frac}B\). Let \(m\) be the
highest index with \(h_m\ne0\), and set
\(h=h_m\), \(\ell=L_0h_{m-1}\).

**Nonconstant-top reduction.** If \(m\ge3\) and \(h\) is
nonconstant, then \(3\le m\le5\), and
\[
h=cq,\qquad
0\ne c\in\mathbb C^4,\quad c_3=c_4=0,\quad
q\in\ker E\setminus\mathbb C.
\tag{3}
\]
There are precisely the following alternatives.

1. If \(\ell=0\), the genuine constant coordinate direction
   \(T_c=\sum c_iT_i\) commutes with \(E\). If \(E\) has a
   polynomial slice, the one-good-output-partial recognition lemma
   proves that \(E\) fixes an actual ambient coordinate and
   \(\ker E\simeq\mathbb C^{[3]}\).
2. If \(\ell\ne0\), after changing the constant normalization of
   \(c\), there are
   \[
   g\in\ker E\setminus\mathbb C,\qquad
   0\ne\lambda\in\mathbb C^2,
   \qquad h=cg^m,\quad\ell=\lambda g^{m-1}.
   \tag{4}
   \]
   No recognition conclusion is asserted for this alternative.

The first conclusion is stronger than merely putting \(h\) and
\(\ell\) on a common polynomial curve. Its proof uses no polynomial
curve factorization theorem and does not make that parameter a
coordinate.

## 2. The full image line, including both auxiliary coordinates

The [actual-flow companion calculation](two-quadratic-defects-pass39.md)
gives
\[
\mathcal M=
\begin{pmatrix}J&-\mathcal V/2\\L_0&0\end{pmatrix},
\qquad\mathcal M^6=0,
\qquad
(\mathcal M^j)_{\mathrm{UL}}=
\frac{\operatorname{Jac}h_j}{j!}.
\tag{5}
\]
Its block lemma applies because \(\mathcal V\) is injective and
\(L_0\) is surjective: if \(\mathcal M N=N\mathcal M=0\),
then \(N\) and its upper-left block have the same rank.
Indeed neither the right nor the left kernel of \(\mathcal M\)
has a nonzero vector supported only on the auxiliary plane. Deleting
the auxiliary columns and then rows therefore preserves rank.

For a nonconstant highest \(h=h_m\), descending from
\(\mathcal M^6=0\) using the vanishing later Jacobian blocks gives
\[
\mathcal M^{m+1}=0,\qquad\mathcal M^m\ne0.
\tag{6}
\]
Thus its Jordan form has a block of size \(m+1\). Since
\(m\ge3\), that block is unique and all remaining blocks have
total size \(5-m\le2\), strictly smaller than \(m\).
It follows that
\[
\ker\mathcal M\cap\operatorname{im}\mathcal M^{m-1}
=\operatorname{im}\mathcal M^m,
\qquad
\dim_K\operatorname{im}\mathcal M^m=1.
\tag{7}
\]
For \(m=3\), the possible additional block has size at most two.
The type \((3,3)\) is not an exception: it has
\(\mathcal M^3=0\), contrary to (6).

The indispensable extra vector is obtained by applying the full
companion power to the actual velocity, not by discarding the lower
rows:
\[
\mathcal M^{m-1}\binom{P}{0}
=\frac1{(m-1)!}\binom{h}{(m-1)\ell}.
\tag{8}
\]
For the upper block, use
\((\operatorname{Jac}h_{m-1})P=h_m\). For the lower block,
\((\mathcal M^{m-1})_{\mathrm{LL}}
=L_0\operatorname{Jac}h_{m-2}/(m-2)!\), giving (8).

The actual top coefficient identities are
\[
L_0h=0,\qquad E\ell=0,\qquad
Jh=\frac{m-1}{2}\mathcal V\ell.
\tag{9}
\]
They show that the nonzero vector on the right of (8) is also
killed by \(\mathcal M\). Hence it spans the line in (7).
On the other hand, the four base columns of \(\mathcal M^m\)
are
\[
\frac1{m!}
\binom{\operatorname{Jac}h}{m\operatorname{Jac}\ell}.
\tag{10}
\]
Consequently every column in (10) is proportional to
\((h,(m-1)\ell)\). This is the full-row information that was
missing from a rank bound on \(\operatorname{Jac}h\) alone.

## 3. Original-ring factorization, with no coordinate assumption

Choose a nonzero component \(h_j\). The upper components of (10)
give, for every ambient partial \(T_k\),
\[
h_jT_kh_i-h_iT_kh_j=0.
\tag{11}
\]
Thus every rational ratio \(h_i/h_j\) is killed by all four
ambient partials and belongs to \(\mathbb C\). Taking
\(q=h_j\) proves (3), with the appropriate constant vector
\(c\). Since \(h\) is nonconstant, so is \(q\), and
\(Eh=0\) gives \(Eq=0\).

Comparing an auxiliary component in the same column yields
\[
m q\,T_k\ell_i=(m-1)\ell_i\,T_kq
\quad(i=1,2;\ k=1,2,3,4).
\tag{12}
\]
If \(\ell_i\ne0\), all partials kill
\(\ell_i^m/q^{m-1}\), so
\[
\ell_i^m=C_iq^{m-1},\qquad C_i\in\mathbb C^*.
\tag{13}
\]
For every irreducible polynomial \(\pi\) of the original UFD
\(B\), taking its valuation gives
\[
m\,v_\pi(\ell_i)=(m-1)v_\pi(q).
\tag{14}
\]
Since \(m\) and \(m-1\) are coprime, every multiplicity in
\(q\) is divisible by \(m\). Absorb its nonzero complex unit
into an \(m\)-th root to write \(q=g^m\) in \(B\).
Equation (13) then gives \(\ell_i=\lambda_i g^{m-1}\),
including zero components by setting \(\lambda_i=0\).
Finally \(E(g^m)=0\) implies \(Eg=0\). This proves (4),
including all repeated-factor cases.

If instead \(\ell=0\), (9) and \(h=cq\) give \(Jc=0\).
Therefore \([E,T_c]=0\). Choose a constant linear change of the
two good coordinates so that \(T_c=\partial_b\) and the other
good direction is \(\partial_a\). The two complementary
coordinates are denoted \(u,v\). Now use
\(Z=\partial_b\), \(F=0\), \(g=1\) in the
[one-good-output-partial recognition lemma](three-output-cubic-closure-pass41.md#1-a-recognition-lemma-requiring-only-one-good-partial).
Its actual coordinate and slice hypotheses are satisfied. The lemma's
commuting-plane, relative cancellation and regular-kernel source gates
remain necessary; they are not replaced by this matrix argument.

## 4. What happens to the old vector correctors

For comparison, suppose any common polynomial parameterization has
been supplied, \(h=H(a)\), \(\ell=L(a)\). Cancelling its
nonzero differential in the earlier top identities gives
\[
JH=\frac{m-1}{2}\mathcal V L,
\qquad JH'=\frac m2\mathcal V L'.
\tag{15}
\]
The proposed good-plane correctors would be
\[
K_i=(m-1)L_iH'-mL_i'H.
\tag{16}
\]
Without the full image line, their brackets are
\[
[E,K_1]=-\frac{m(m-1)}2\det(L,L')V_4,
\qquad
[E,K_2]=\frac{m(m-1)}2\det(L,L')V_3.
\tag{17}
\]
Equations (7)--(10) now give the stronger conclusion
\(K_1=K_2=0\), and therefore \(\det(L,L')=0\).
The rotating-direction branch is not an actual residual here.
Nor does this route supply a nonzero corrected nice field: the
candidate correctors vanish identically. The power-law alternative
(4) must be investigated separately.

## 5. Exact rescaling boundary

In the nonzero-\(\ell\) alternative, \(\delta=E/g\) is an
actual LND on \(B_g\), with
\[
\delta^m x=c,\qquad L_0\delta^{m-1}x=\lambda.
\tag{18}
\]
The highest actual conjugated partials kill \(h\). Equivalently,
compare the top powers in
\(\operatorname{Jac}(\exp(tE)x)C(t)=I\). Thus
\([E,T_i]g=0\) for good \(i\), and \(V_i g=0\) for bad
\(i\). The rescaled adjoint bounds remain
\[
\operatorname{ad}_\delta^2T_1=
\operatorname{ad}_\delta^2T_2=0,
\qquad
\operatorname{ad}_\delta^3T_3=
\operatorname{ad}_\delta^3T_4=0.
\tag{19}
\]
Its exact bad defect columns are
\[
\widetilde V_i
=g^{-2}V_i+2g^{-3}\bigl([E,T_i]g\bigr)E,
\qquad i=3,4.
\tag{20}
\]
The added terms are in the direction of \(E\); they are not a
common scalar multiplication of the old columns. In fact their rank
is determined exactly.

If \(E,V_3,V_4\) have rank three, independence in (20) is
immediate. Otherwise write \(E=\alpha V_3+\beta V_4\) over
\(K\). The coefficients are \(E\)-invariant because the three
fields commute and \(V_3,V_4\) are independent. Write
\(W_i=[E,T_i]\) and \(\omega=(W_3g,W_4g)\). The next-to-top
coefficient of the actual bad column gives
\[
V_i h_{m-1}=-\frac2m W_i h
            =-2c g^{m-1}W_i g.
\]
Apply \(E=\alpha V_3+\beta V_4\) to \(h_{m-1}\), whose
\(E\)-derivative is \(cg^m\). Cancelling its nonzero constant
component and the nonzero power of \(g\) gives
\(\alpha W_3g+\beta W_4g=-g/2\). Thus, with
\(u=(\alpha,\beta)^{\mathsf t}\),
\[
[\widetilde V_3\mid\widetilde V_4]
 =g^{-2}\mathcal V N,
\qquad N=I_2+\frac2g u\omega,
\qquad N^2=N,\quad\operatorname{tr}N=1.
\tag{21}
\]
The idempotent \(N\) has rank exactly one. Consequently
\[
\operatorname{rank}[\widetilde V_3\mid\widetilde V_4]
=\operatorname{rank}[E\mid V_3\mid V_4]-1
\in\{1,2\}.
\tag{22}
\]
Moreover adjoining \(E\) to either defect pair gives the same
field span by (20). In the rank-drop case the surviving defect line
is therefore independent of the \(E\)-line. This is a generic
field statement, not a new global coordinate construction.

A constant change of the two bad coordinates can normalize the
nonzero vector \(\lambda\) to \((\lambda_0,0)\). It does not
by itself lower an adjoint height.

Even where rank two persists, (18)--(20) are statements on \(B_g\).
Coordinate partials need not remain locally nilpotent after this
localization. No polynomial quotient, global extension of a rational
symmetry, or reduction to a global lower-height coordinate frame is
inferred from them.

## 6. A separate constant-top full-row refinement

Suppose the original highest \(h_m=c\ne0\) is constant and
\(m\ge4\), still under (1)--(2). The top differential identity
and injectivity of \(\mathcal V\) make \(\ell\) constant.
The block lemma gives \(\mathcal M^m=0\), while (8) gives
\(\mathcal M^{m-1}\ne0\). There is a unique Jordan block of
size \(m\), and all others have size at most \(6-m<m-1\).
Hence \(\mathcal M^{m-1}\) has rank one, with constant image
direction \((c,(m-1)\ell)\).

Choose \(j\) with \(c_j\ne0\) and put
\(\sigma=(h_{m-1})_j/c_j\). Its full base columns give
\[
E\sigma=1,\qquad
h_{m-1}=c\sigma+d,\qquad
L_0h_{m-2}=\ell\sigma+\mu,
\tag{23}
\]
where \(d\in\mathbb C^4\), \(\mu\in\mathbb C^2\), and
\(L_0d=\ell\). Both equalities follow by integrating identities
of all four ambient partials, so their constants really are complex
constants, not arbitrary invariants. This produces an actual polynomial
slice \(\sigma\), but no coordinate assertion about it. The
remaining lower coefficients still require analysis.

## Verification boundary

The Jordan/image argument and UFD factorization above are all-degree
proofs under the actual supplied-frame hypotheses. The independent
[five-method exact checker](two_quadratic_top_line_checks_pass42.py)
passed its first run in 0.134 seconds. It checks all relevant partitions
of six, full companion rows on a genuine sliced degree-two boundary
example, formal rotating data that fail the companion determinant,
repeated-factor differential identities, and actual rescaling formulas.
The final rescaling method also checks the formal rank-update identity
in both coefficient charts and the independent three-field case;
these are linear-algebra controls, not new realizations of an action.
The completed five-method suite, including this refinement, passed in
0.226 seconds.
Only the degree-two example is asserted to realize the full
two-quadratic rank-two frame. These bounded controls do not create a
degree-three-to-six example or certify general cancellation. The
earlier height-ten problem remains open in the nonzero-\(\ell\)
residual and in the other unclosed profiles.
