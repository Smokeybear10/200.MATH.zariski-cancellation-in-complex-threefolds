# The omitted-pair boundary restricts the degenerate quartic unit exponents

**Status: bounded necessary restriction in the complete actual transverse
chart; no remaining branch is recognized.**

Under the full hypotheses of559 with its fourth pair-numerator coefficient
zero, a division-free identity relates the entire pair numerator to the
nonzero guard on the omitted pair-sum boundary. When delta is nonzero,
this removes the proposed numerator lambda times D squared. It also
excludes one exact delta value for the numerator lambda times u squared
times D. The other unit forms remain necessary possibilities, not actual
realizations.

## 1. Scope and the entire pair expression

Retain EVERY actual hypothesis of
[559](principal-paraboloid-cubic-transverse-quartic-pair-unit-restriction-pass559-working.md),
including its complete264/296/535 input, the noncomplex-T0 transverse
cubic family557, the original global slice, the selected leading LND,
finite intrinsic extension, all genuine potential equations, calibrated
scalar and both actual polynomial returns. None is replaced by the
formal coefficients below. In particular, over the same coefficient
field \(L'\),
\[
\begin{gathered}
\sigma=x^2+c,\qquad
\theta=ax^3+b_2x^2+dx+e,\\
y=rx^4+q_3x^3+y_2x^2+y_1x+y_0,\qquad a,m,r\ne0,\\
h=-4r/a^2,\quad p=m_t,\quad k_1=k_t,\quad k_2=k_{tt}.
\end{gathered}
\tag{1}
\]
The symbols \(\mathfrak n_t,\mathfrak n_s\) are genuine derivatives
of the retained potential, not independently prescribed actual data.
They can be treated as algebraic symbols only when verifying a necessary
polynomial identity that holds for every value of those derivatives.

Assume the quartic coefficient \(U_4\) of559 vanishes. Its whole
coefficient formula and the whole-W relation then give
\[
b_2=\frac{a^2m}{2}+\frac{a^2p}{4r},\qquad q_3=amr.
\tag{2}
\]
Both delta cases are still permitted at this stage. There is no assumption
that \(p,c,d,e\), a potential derivative, or a lower y coefficient is
nonzero. The exact conic restrictions563 and any subsequent coordinate
normalization are not needed for this result.

For independent ordered intrinsic variables set \(u=x_1+x_2\) and
\(z=x_1x_2\). Here \(u\) is the pair sum, not the global slice. Use the
entire expressions
\[
\begin{aligned}
S_\sigma&=u^2-2z+2c,\\
S_\theta&=a(u^3-3uz)+b_2(u^2-2z)+du+2e,\\
S_y&=r(u^4-4u^2z+2z^2)+q_3(u^3-3uz)
                         +y_2(u^2-2z)+y_1u+2y_0,\\
\mathcal E(u,z)&=S_y+k_2S_\sigma/2+pS_\theta/2+\mathfrak n_t\\
&\hspace{8mm}
-\frac{S_\sigma+k_1}{m}
       (pS_\sigma/2+hS_\theta/2+\mathfrak n_s).
\end{aligned}
\tag{3}
\]
Define
\[
\begin{gathered}
C=2c+k_1+mb_2,\qquad D(u)=2u+ma,\\
N(u)=u^3+ma u^2+Cu+md,\qquad u_*=-ma/2\ne0,\\
\delta=N(u_*)=m\left(d-\frac{aC}{2}+\frac{a^3m^2}{8}\right).
\end{gathered}
\tag{4}
\]
This C is merely an abbreviation, not a newly chosen constant.
Write \(\mathcal E=E_0+E_1z+E_2z^2\) and
\[
\mathcal U=E_0D^2+E_1DN+E_2N^2.
\tag{5}
\]
The full actual return in559, including diagonal pairs, licenses that
\(\mathcal E\) is a unit in
\(L'[u,u^{-1},z]/(N-Dz)\). The boundary omitted by inverting u supplies
the separate nonzero condition
\[
a y_1-dq_3\ne0,\qquad
\Lambda:=y_1-mrd\ne0.
\tag{6}
\]
The second version uses (2) and the proved nonzero a. Neither boundary
nor the delta-zero vertical component will be dropped.

## 2. A quadratic quotient and a division-free boundary identity

Substitution of (1),(2) in the complete expression (3) gives
\[
E_2=\frac{6r}{am}D,\qquad \deg_u\mathcal U\le3.
\tag{7}
\]
These are the full coefficient identities of559, not truncations.
In particular D divides the entire numerator. Put
\[
\mathcal V:=\frac{\mathcal U}{D}
     =E_0D+E_1N+\frac{6r}{am}N^2
     =v_2u^2+v_1u+v_0.
\tag{8}
\]
The symbol \(\mathcal V\) denotes this pair polynomial, not the actual
coordinate W or a conic-field element. It is a polynomial of degree at
most two, including when delta is zero.

Here are compact full-coefficient formulas useful for checking the
identity. Set
\[
\begin{aligned}
\eta&=\frac{\mathfrak n_s+pc+he}{m},\\
\mathcal A&=\frac{a^2m^2r}{2}+\frac{a^2mp}{4}
       -\frac{a^2p^2}{8r}+r(2c+k_1)-\frac{k_2}{2}+\eta.
\end{aligned}
\tag{9}
\]
Expansion of the whole (3),(8), retaining its lower terms, gives
\[
\begin{aligned}
E_1(u_*)&=2(\mathcal A-y_2)+\frac{2r\delta}{am},\\
v_2&=2\Lambda+am(\mathcal A-y_2)+4r\delta,\\
\mathcal V(u_*)&=\delta E_1(u_*)+\frac{6r\delta^2}{am}.
\end{aligned}
\tag{10}
\]
The last line follows directly from D(u*)=0 in (8). To verify the first
two without omitting any support, expand (3) as a quadratic in z, use
(2), and collect its linear z coefficient and the quadratic u coefficient
in (8). Equations (9),(10) print the resulting entire expressions.
The lower terms \(\mathfrak n_t,y_0\) cancel from these particular
coefficients; they remain in (3) and in \(v_1,v_0\).

Subtracting the first two lines of (10) gives the identity
\[
\boxed{2v_2-amE_1(u_*)-6r\delta=4\Lambda.}
\tag{11}
\]
Using the last line then gives
\[
\boxed{4\delta\Lambda
       =2\delta v_2-am\mathcal V(u_*).}
\tag{12}
\]
Both are division-free in delta. The only denominators in the input
and printed formulas involve the already nonzero a,m,r. In particular,
(12) is not obtained by silently deleting delta=0.

## 3. Nonzero delta: exact unit-exponent exclusions

Now suppose \(\delta\ne0\). The exact pair ring and unit law of559
give
\[
\mathcal U=\lambda u^iD^j,\qquad
\lambda\in(L')^*,\quad i\ge0,\quad j\ge1,\quad i+j\le3.
\tag{13}
\]
There are precisely six exponent pairs. Dividing (12) by the now
nonzero delta yields
\[
\Lambda=\frac{v_2}{2}-\frac{am}{4\delta}\mathcal V(u_*).
\tag{14}
\]
Substitute \(\mathcal V=\lambda u^iD^{j-1}\) and \(u_*=-am/2\).
The complete list is

| \((i,j)\) | Entire \(\mathcal U\) | \(\Lambda/\lambda\) | Boundary consequence |
| --- | --- | --- | --- |
| \((0,1)\) | \(\lambda D\) | \(-am/(4\delta)\) | Nonzero automatically |
| \((1,1)\) | \(\lambda uD\) | \(a^2m^2/(8\delta)\) | Nonzero automatically |
| \((2,1)\) | \(\lambda u^2D\) | \((8\delta-a^3m^3)/(16\delta)\) | Requires \(8\delta\ne a^3m^3\) |
| \((0,2)\) | \(\lambda D^2\) | \(0\) | Impossible |
| \((1,2)\) | \(\lambda uD^2\) | \(1\) | Nonzero automatically |
| \((0,3)\) | \(\lambda D^3\) | \(2\) | Nonzero automatically |

Thus the actual original boundary guard excludes
\[
\boxed{\mathcal U=\lambda D^2\quad(\lambda\ne0,\ \delta\ne0).}
\tag{15}
\]
For the \(\lambda u^2D\) possibility, the excluded value can also be
written, using (4),
\[
8\delta=a^3m^3\quad\Longleftrightarrow\quad d=aC/2.
\tag{16}
\]
No other unit shape is excluded by this boundary identity. In particular,
there is no license to remove the zero-degree or linear \(\mathcal V\)
possibilities merely because the generic degree bound is two.

## 4. Delta zero and the exact coefficient-map boundary

When delta is zero, the original vertical component still forces
\(E_1(u_*)=0\). Equation (11) then gives
\[
v_2=2\Lambda\ne0.
\tag{17}
\]
The complete559 graph-and-vertical unit argument gives exactly
\(\mathcal U=\Lambda uD^2\); (17) is consistent with that result,
since \(\mathcal V=\Lambda uD\) has quadratic coefficient
\(2\Lambda\). We do not apply the delta-nonzero table to this component.
The nonzero graph value at its intersection with the vertical line is
still required. No new exclusion of delta=0 is claimed.

There is a useful exact distinction between the two cases. Fix every
formal coefficient in (1)--(4) except \(y_2,y_1,y_0\). The affine-linear
map from those three coefficients to \((v_2,v_1,v_0)\) has matrix
\[
\frac{\partial(v_2,v_1,v_0)}{\partial(y_2,y_1,y_0)}
=\begin{pmatrix}
-am&2&0\\
-2C&am&4\\
-2md&0&2am
\end{pmatrix},\qquad
\det=-16\delta.
\tag{18}
\]
For a direct check, varying the three y coefficients changes
\(\mathcal V\) respectively by
\[
u^2D-2N=-am u^2-2Cu-2md,\qquad uD,\qquad 2D.
\tag{19}
\]
Their coefficients give (18), whose determinant is
\(-2a^3m^3+8amC-16md=-16\delta\).

Consequently, when delta is nonzero, every prescribed formal quadratic
\(\mathcal V\) fixes those three formal y coefficients uniquely.
This explains why merely solving the polynomial unit numerator for
them is not a contradiction: the remaining whole H equations, genuine
derivative compatibility, scalar and actual returns still matter.
It is not an assertion that arbitrary such formal data satisfy those
equations, are an actual chart, or realize one of the surviving shapes.
When delta is zero the same coefficient map is singular, consistently
with the extra graph/vertical compatibility that must be retained.

## 5. Verification and remaining scope

The complete held559 source was reread through EOF in dc4ba3+f0cc3f.
The target path was absent in f41456 before creation. The full current
writing guide was read in7a41ff. Fresh unsaved fd3367 reconstructed the
whole pair polynomial and its coefficient matrix; d2e370 checked every
unit-form boundary value; 69db31 rebuilt (3)--(12) with all lower
coefficients and verified the determinant and both compact coefficient
formulas, with every residual zero. The hand algebra needed to check
the identities is displayed above, not replaced by sampled values.

The result is a necessary exponent restriction inside FULL559 with
U4=0. It covers the nonzero-delta subcase without losing the zero-delta
boundary. It supplies no coordinate-entry result, no construction of
an actual example, no recognition of a remaining family and no
cancellation solution. No prior source or canonical record was changed.
No saved checker was executed, imported or compiled. Separate complete
saved-source review remains required after author hold. No historical
novelty, external expert review or formal proof certification is claimed.
