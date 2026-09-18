# A scalar-slice replica obstruction for an actual weighted Euler frame

## 1. Exact statement and the coefficient boundary

Work in the known translation ring
\[
 B=\mathbf C[a,b,c,u],\qquad E=\partial_u,
 \qquad A=\ker_B E=\mathbf C[a,b,c].
\tag{1}
\]
There is an actual all-positive polynomial coordinate frame whose
degree sum and exact weighted Euler shift are
\[
 (\Sigma,\delta)=(25,10).
\tag{2}
\]
Its recovered leading derivation, extended to kill the given slice,
is \(\widetilde N=72a\partial_c\). No automorphism
\(\exp(f(u)\widetilde N)\), with \(f\in\mathbf C[u]\), lowers
the lexicographically ordered pair \((\Sigma,\delta)\). The same
obstruction holds if the recovered derivation is first primitively
normalized to \(\partial_c\), which itself has a slice.

More precisely, every such replica that does not increase the
coordinate degrees leaves all four degrees and the Euler shift
unchanged. Every other such replica increases the degree sum.
Here the weighted Euler field is recomputed from the actual
degrees of the transformed frame; it is not assigned the old
weights after a degree increase.

The restriction \(f\in\mathbf C[u]\) is essential. Allowing
coefficients from the invariant ring gives an explicit replica
that decreases the degree sum from 25 to 22. That entire actual
map and its inverse are printed below. Thus this is not an
obstruction to arbitrary replicas with multiplier in
\(\ker_B\widetilde N\), and it is not a globally minimizing-frame
example, a cancellation counterexample, or a descent theorem.
No novelty claim is made.

## 2. The complete frame, inverse, and recovered derivation

Take the actual frame from the no-slice control of source576:
\[
 \begin{split}
 X&=a+u^4,\qquad Y=b+u^5,\\
 Z&=c+a^2u^6+u^3,\\
 W&=u+Y^2-XZ.
 \end{split}
\tag{3}
\]
Define \(U=W-Y^2+XZ\). The entire inverse is
\[
 u=U,\qquad a=X-U^4,\qquad b=Y-U^5,
 \qquad c=Z-(X-U^4)^2U^6-U^3.
\tag{4}
\]
Substitution of (3) into (4) first gives \(U=u\), then recovers
\(a,b,c\). Conversely (4) gives back \(X,Y,Z\), followed by
\(U+Y^2-XZ=W\). Both orders are polynomial identities on the
whole fourfold, with no localization. The coordinate Jacobian
in the ordered variables \((a,b,c,u)\) is one.

The full fourth row expands to
\[
 W=(1-a^2)u^{10}-u^7-a^3u^6+2bu^5-cu^4-au^3+u+b^2-ac.
\tag{5}
\]
The exact degree tuple is \((4,5,6,10)\), with leaders
\((1,1,a^2,1-a^2)\). These are nonzero polynomials in \(A\);
no special fiber such as \(a=0\) is being substituted to
compute the global \(E\)-degrees.

Let \(D\) be the weighted Euler derivation of this actual frame:
\[
 D=4X\partial_X+5Y\partial_Y+6Z\partial_Z+10W\partial_W.
\tag{6}
\]
Its entire pullback to (1) is
\[
 \begin{split}
 D(u)&=10u,\\
 D(a)&=4a-36u^4,\qquad D(b)=5b-45u^5,\\
 D(c)&=6c-62a^2u^6+72au^{10}-24u^3.
 \end{split}
\tag{7}
\]
These formulas follow directly from the full inverse, or can be
verified by all four equations \(D(X_i)=d_iX_i\).

For any polynomial derivation written in the coordinates
\((a,b,c,u)\), its exact \(E\)-shift is the maximum of the
\(u\)-degrees of its three horizontal coefficients and the
\(u\)-degree of its last coefficient minus one. The product
rule proves the upper bound on every polynomial, and the
individual coordinates attain each nonzero candidate. Applying
this rule to (7) gives \(\delta=10\), attained on \(c\).
On the entire associated graded ring \(A[\eta]\),
\[
 \overline D=\eta^{10}(72a\partial_c),\qquad
 \overline D\eta=0.
\tag{8}
\]
Thus the derivation tested here really is the one recovered
from the actual Euler field, not a freely selected LND on \(A\).
It already kills \(u\), so its extension is \(\widetilde N\)
as stated. Removing its invariant common factor gives the
primitive derivation \(\partial_c\).

## 3. All scalar-slice replicas and their whole inverse

It suffices to treat simultaneously
\[
 \Phi_{s,f}=\exp\bigl(s f(u)\partial_c\bigr),
 \qquad s=a\ \hbox{or}\ s=1,
 \qquad f\in\mathbf C[u].
\tag{9}
\]
Absorbing the nonzero constant 72 into \(f\) gives exactly
all replicas of the recovered derivation when \(s=a\).
The case \(s=1\) gives the primitive variant. These
automorphisms fix \(a,b,u\) and send \(c\) to \(c+s f(u)\);
their inverses change the sign of \(f\).

The transformed actual frame is
\[
 X_f=X,\quad Y_f=Y,\quad
 Z_f=Z+s f(u),\quad W_f=W-Xs f(u)
                         =u+Y_f^2-X_fZ_f.
\tag{10}
\]
For an explicit inverse set
\[
 U=W_f-Y_f^2+X_fZ_f,\quad
 a_f=X_f-U^4,\quad b_f=Y_f-U^5.
\tag{11}
\]
Then
\[
 u=U,\quad a=a_f,\quad b=b_f,\quad
 c=Z_f-a_f^2U^6-U^3-s(a_f)f(U),
\tag{12}
\]
where \(s(a_f)=a_f\) or one. Both inverse orders follow by
first recovering \(U\), then \(a,b\), then \(c\), and finally
the fourth row in (10). These formulas are valid for every
polynomial \(f\), not only for finitely many tested degrees.

Suppose first that \(f\ne0\), with degree \(k\) and leader
\(\lambda\in\mathbf C^*\). For \(k>6\), the exact degrees
are
\[
 (4,5,k,k+4),\qquad \Sigma_f=13+2k>25.
\tag{13}
\]
Indeed the new leaders of \(Z_f,W_f\) are respectively
\(s\lambda,-s\lambda\), and these are nonzero in \(A\).
The original degrees six and ten are strictly lower.

For \(k\le6\), including \(f=0\) separately, put
\(\lambda_6=[u^6]f\in\mathbf C\). The coefficients at the
old leading degrees of \(Z_f,W_f\) are
\[
 \begin{array}{c|cc}
 & [u^6]Z_f &[u^{10}]W_f\\ \hline
 s=a&a^2+a\lambda_6&1-a^2-a\lambda_6\\
 s=1&a^2+\lambda_6&1-a^2-\lambda_6.
 \end{array}
\tag{14}
\]
Every entry is nonzero as a polynomial in the independent
variable \(a\), for every constant \(\lambda_6\), including
zero. Consequently the exact degree tuple remains
\((4,5,6,10)\) and the degree sum remains 25. This proves
that (13) and this unchanged tuple exhaust all scalar-slice
replicas. In particular coordinatewise nonincrease is exactly
the range \(\deg f\le6\), with zero included.

## 4. The exact Euler shift cannot decrease in the remaining range

Now restrict to \(\deg f\le6\) or \(f=0\). The actual
degrees have not changed, so the weighted Euler derivation of
the transformed frame is exactly
\[
 D_f=\Phi_{s,f}D\Phi_{s,f}^{-1}.
\tag{15}
\]
In fact its eigen-equations follow by applying \(\Phi_{s,f}\)
to those for the whole original frame. We only use (15) as
the recomputed Euler field in this degree-preserving range.
For \(\deg f>6\), the actual weights change, and the degree
sum argument (13) is already decisive without using (15).

The images of \(a,b,u\) under (15) are unchanged from (7).
Its full remaining coefficient is
\[
 D_f(c)=D(c)+6s f-D(s)f-10u s f'.
\tag{16}
\]
This follows by applying the inverse translation to \(c\),
differentiating \(c-sf\), then translating back. The
translation of the \(6c\) term is retained. In particular
\[
 \begin{array}{c|l}
 s=a&D_f(c)=D(c)+2af+36u^4f-10au f',\\
 s=1&D_f(c)=D(c)+6f-10u f'.
 \end{array}
\tag{17}
\]
These are entire identities with all lower coefficients of
\(f\) present. They do not assume that \(f\) is a monomial.

For \(\deg f\le6\), the exact coefficient of \(u^{10}\)
in (17) is
\[
 [u^{10}]D_f(c)=
 \begin{cases}
 72a+36\lambda_6,&s=a,\\
 72a,&s=1.
 \end{cases}
\tag{18}
\]
Neither polynomial can vanish identically for a constant
\(\lambda_6\). Every other term in (17) has degree at most
ten; the other horizontal coefficients in (7) have degrees
four and five, and \(D_f(u)=10u\). The all-ring shift rule
therefore proves
\[
 \delta_f=10\qquad(\deg f\le6\text{ or }f=0).
\tag{19}
\]
Combining (13),(14),(19), all degree-preserving replicas leave
\((\Sigma_f,\delta_f)=(25,10)\), whereas every other one has
\(\Sigma_f>25\). No value of the recomputed Euler shift in
that latter range can make the lexicographic pair smaller.
This proves the stated obstruction for both recovered and
primitive scalar-slice replicas.

## 5. An invariant-coefficient replica immediately escapes

The coefficient restriction must not be suppressed. In
\(\ker_B\widetilde N=\mathbf C[a,b,u]\), take the multiplier
\(-a u^6/72\). The resulting actual replica is
\[
 \Psi=\exp\left(-\frac{a u^6}{72}\widetilde N\right)
      =\exp(-a^2u^6\partial_c).
\tag{20}
\]
It fixes \(a,b,u\) and sends \(c\) to \(c-a^2u^6\). The
same map is an invariant-coefficient replica of the primitive
derivation \(\partial_c\). Its transformed rows are
\[
 X_*=a+u^4,\quad Y_*=b+u^5,\quad Z_*=c+u^3,
 \quad W_*=u+Y_*^2-X_*Z_*.
\tag{21}
\]
Their exact degrees are \((4,5,3,10)\), so the degree sum
decreases from 25 to 22. The leading coefficient of \(W_*\)
is one, and those of the other three rows are also one.
An entire inverse is
\[
 U=W_*-Y_*^2+X_*Z_*,\quad
 u=U,\quad a=X_*-U^4,\quad b=Y_*-U^5,
 \quad c=Z_*-U^3.
\tag{22}
\]
Both compositions recover the rows successively exactly as
before. Thus this escape is an actual polynomial coordinate
change, not an intrinsic-field substitution or a formal
leading-term cancellation.

The multiplier in (20) is not in \(\mathbf C[u]\). This is
precisely why it is compatible with the theorem. The example
refutes automatic descent using only the recovered derivation
with scalar-polynomial dependence on the given slice, even
after primitive normalization. It does not obstruct using
invariant coefficients, other recovered derivations, mixed
coordinate changes, or a separately justified minimizing-frame
argument. The invariant ring in (1) remains explicitly polynomial.

## 6. Verification and status

The relevant sources576--578 were read completely before this
note. The control (3) and its full Euler field are checked
directly here. Fresh unsaved algebra checks the whole
functional identities (16),(17) with an arbitrary function of
\(u\), the actual inverse formulas, degree boundary cases,
and the entire escape (21). The universal degree argument
uses the coefficient identities (14),(18), not a grid of
sample polynomial choices.

No saved checker was executed, imported or compiled, and no
canonical record was edited. Author self-review is not an
independent saved-source audit. The conclusion is restricted
to the two explicitly stated scalar-slice replica families;
there is no novelty, unrestricted-replica obstruction,
globally minimizing-frame claim, or general cancellation
conclusion.
