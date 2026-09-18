# The nonzero cubic row is excluded by its actual initial relation

Working bounded exclusion, pending separate saved-source review:
retain the FULL actual degree-drop hypotheses of512, with noncomplex
coupling m, m_s=0 and affine intrinsic sigma=P. Then the quadratic
coefficient e of y and cubic coefficient g_3 of the original W row
cannot both be nonzero.

In particular, after the e=0 exclusion515, every remaining such
chart must have g_3=0. The result concerns the entire g_3-nonzero
branch, not only the two conditional ODE families in517.

The proof uses the actual polynomial three-ring over C(X), its
complete coefficient Jacobian, and growth of polynomial invariants.
It does NOT assume a global slice for the auxiliary derivation,
homogeneity of that derivation on a freely graded polynomial ring,
or rationality of the coefficient field. It does not invoke the
sliced four-ring theorem158 outside its stated hypotheses.

## 1. Full actual input and the precise contradiction hypothesis

Retain all hypotheses of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine levels and unit minors of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
universal494, and the directly proved
[degree-drop reduction512](principal-paraboloid-degree-drop-univariate-coupling-reduction-pass512-working.md).
In particular,

\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,
\quad X=a_0u+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad
I_{\mathrm{initial}}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE original initial kernel},\\
0\ne N=[u^4]\partial_Z|_A,\qquad
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad O=L[P],\quad NP=\rho\in L^*,\\
\operatorname{Frac}A=L(P),\quad
m=k_s\ne0,\quad m_s=0,\quad m\notin\mathbb C,\\
\theta=-P^2/m+bP+c,\qquad y=eP^2+lP+r,\qquad e_s=0.
\end{gathered}
\tag{1}
\]

Both actual returns, the original global slice and the literal
selected partial remain required. The coefficient partials on L
commute. Its s-constant field F_0 is finite over C(t); in particular
m,e,p=m_t belong to F_0, with p nonzero.

Suppose for contradiction that

\[
e\ne0,\qquad g_3:=\frac{p-2me}{m^2}\ne0.
\tag{2}
\]

At fixed actual X the entire polynomial rows remain

\[
\begin{aligned}
Y&=y+PX+tX^2,\\
Z&=2ty+P^2+k_tP+m\theta+n+(2tP+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
mw&=\ell-(2P+k_t)y-F(P,\theta),\\
F(P,V)&=k_{tt}P^2/2+pPV+n_tP+n_sV.
\end{aligned}
\tag{3}
\]

Their exact P degrees and leading coefficients are therefore

\[
(d_Y,d_Z,d_W)=(2,2,3),\qquad
(Y_2,Z_2,W_3)=(e,2te,g_3).
\tag{4}
\]

For W_3, the contributions are −2e/m from (2P)y and p/m^2
from pP*theta; the remaining terms have degree at most two.
The quadratic theta contribution in Z cancels P^2 before its
leading coefficient 2te is read. These are exact degrees, not
upper bounds or a formal profile assigned to another ring.

Put K=\mathbb C(X) and

\[
R=K[Y,Z,W]=K^{[3]},\qquad F=L(X).
\tag{5}
\]

Because X is an actual coordinate, this is an actual polynomial
three-ring. We have an injection R into F[P] and
Frac(R)=F(P): indeed Frac(B)=L(P)(u)=L(P)(X), since
u=(X−x_0)/a_0. The variables X and P are transcendental in
the indicated extensions. Also F is finite separable over K(t,s).

The FULL original scalar at fixed X is

\[
J=\det\frac{\partial(Y,Z,W)}{\partial(t,s,P)}
  =-a_0^4/\rho\in L^*\subset F^*.
\tag{6}
\]

Thus it is nonzero and independent of P. No t or s derivative of
its value is assumed to vanish. The lower coefficients in (3) are
not set to zero; their exact degrees and (6) are sufficient below.

## 2. The actual auxiliary LND supplies two polynomial invariants

Extend N from A to B=A[u] by Nu=0 and define

\[
\Delta=a_0N-(NX)E.
\tag{7}
\]

This preserves the actual polynomial ring, fixes X and kills L.
On L[X,P] it is g_0*partial_P, where g_0=a_0*rho is a nonzero
coefficient-field element. Its restriction to R is a nonzero K-LND.
Local nilpotence follows from this polynomial overring, not from
an assertion that any difference of LNDs is locally nilpotent.
Its degree filtration on R equals P degree.

Let A_D=ker_R Delta. This kernel contains two algebraically
independent polynomial elements over K. To see the relevant
local-slice argument explicitly, let b=Delta^2Y=2g_0^2e.
Then b is a nonzero invariant in R, and v=Delta(Y)/b in R_b
has Delta(v)=1. The finite Taylor projection in v gives
R_b=(A_D)_b[v]. Taking fraction fields shows

\[
\operatorname{trdeg}_K A_D=2.
\tag{8}
\]

No finite generation of A_D or global slice for Delta is required.
The original global slice u belongs to E, not to Delta.

## 3. The full coordinate-initial kernel is a height-one prime

Use fresh source variables and an independent initial parameter eta.
Define the positive-weight map

\[
\begin{aligned}
\phi:K[\mathsf Y,\mathsf Z,\mathsf W]&\longrightarrow F[\eta],\\
(\mathsf Y,\mathsf Z,\mathsf W)&\longmapsto
(e\eta^2,2te\eta^2,g_3\eta^3),\\
\operatorname{wt}(\mathsf Y,\mathsf Z,\mathsf W)&=(2,2,3).
\end{aligned}
\tag{9}
\]

Using derivative-normalized Delta leaders would multiply these
three images by g_0^2,g_0^2,g_0^3. A rescaling of the independent
eta by g_0 gives the same kernel, so no speed has been normalized
away in passing to (9).

The first two images are algebraically independent over K. Their
fraction field contains their ratio 2t, transcendental over K,
and e*eta^2 is transcendental over F. On the other hand all three
images belong to F_0(X)[eta], which has transcendence degree two
over K. Thus im(phi) has exactly transcendence degree two.
Its full kernel is a height-one prime in a UFD, so

\[
\ker\phi=(H),\quad H\text{ irreducible and weighted homogeneous},
\qquad D=\operatorname{wt}H>0.
\tag{10}
\]

For completeness the kernel is graded. Every weighted component
of a generator belongs to the kernel; divisibility by that same
generator then forces it to have a single weight. Since the first
two images are independent, H must involve mathsf W. Characteristic
zero and irreducibility give

\[
H_{\mathsf W}\notin(H).
\tag{11}
\]

The source kernel (10) is not the original four-variable initial
kernel in (1), nor is im(phi) identified with the entire associated
graded algebra of R.

## 4. A cofactor bound for the actual partial W

Let T=partial_W on R, holding the actual Y,Z and the field K fixed.
It extends to Frac(R)=F(P). Invert the full matrix in (6).
The cofactor for T(t) uses the Y,Z rows and columns s,P; the
cofactor for T(s) uses their columns t,P. Each has P degree at
most 2+2−1=3. The cofactor for T(P) uses their two horizontal
columns, so it has degree at most 2+2=4. Division by J introduces
no P denominator. Therefore

\[
T(t),T(s)\in F[P]_{\le3},\qquad T(P)\in F[P]_{\le4}.
\tag{12}
\]

For every a in F, exact separability of F/K(t,s) gives
T(a)=a_t*T(t)+a_s*T(s). This is an equality of derivations into
F(P); it does not require that T preserve F. Thus T(a) has degree
at most three in P. Apply the product rule to any polynomial
f=sum a_j P^j in F[P]. The coefficient derivatives have degree
at most j+3, and the P derivative term has degree at most
(j−1)+4. Hence

\[
\deg_P T(f)\le\deg_P f+3\quad\text{whenever }T(f)\ne0.
\tag{13}
\]

In particular this holds for EVERY element of the actual R.
The actual partial T preserves R, so its repeated use gives

\[
\deg_P T^j(f)\le\deg_P f+3j\quad(T^j(f)\ne0).
\tag{14}
\]

This is the needed all-ring bound. It does not require P to be
an actual global slice or polynomial coordinate of R. It also
does not require the stronger and unproved bound deg_P T(P)<=3.

## 5. Exact derivative multiplicity bounds D by five

Take a nonconstant polynomial invariant f in A_D and let Q be its
unique polynomial expression in the source variables over K.
Let M>0 be its source weighted degree. Since f has P degree zero,
its weighted top Q_M belongs to ker(phi). Write its exact
multiplicity as

\[
Q_M=H^\ell G,\qquad \ell\ge1,\quad H\nmid G,
\qquad \ell D\le M.
\tag{15}
\]

Repeated source differentiation gives the complete residue

\[
\partial_{\mathsf W}^{\ell}(H^\ell G)
\equiv \ell!G(H_{\mathsf W})^\ell\pmod H,
\tag{16}
\]

which is nonzero by (11) in the domain modulo H. Its weight is
M−3ell. Every lower weighted component of Q, after the same
derivatives, has smaller weight or vanishes. By the FULL kernel
identity (10), evaluating the remaining top has nonzero leading
coefficient in P. Therefore the exact degree is

\[
\deg_P T^\ell f=M-3\ell.
\tag{17}
\]

But (14) and deg_P f=0 give M−3ell<=3ell. Together with (15),

\[
\ell D\le M\le6\ell.
\tag{18}
\]

Existence of a nonconstant invariant implies D<=6. If D=6, every
nonconstant invariant has M=6ell, so its G in (15) has weight zero
and belongs to K. Define A_N to be the K-vector space of invariants
whose original source weighted degree is at most N. The map taking
the weighted top identifies each graded quotient with a subspace
of the span of a single H^ell, and all other positive weights
have zero graded quotient. Consequently

\[
\dim_K A_N\le\lfloor N/6\rfloor+1.
\tag{19}
\]

Choose algebraically independent f_1,f_2 in A_D using (8), and let
C be the sum of their positive source weighted degrees. The
(n+1)^2 monomials f_1^i*f_2^j with 0<=i,j<=n belong to A_(Cn)
and are linearly independent over K. This contradicts (19) for
large n. Thus

\[
\boxed{D\le5.}
\tag{20}
\]

This dimension argument uses neither a finite generating set for
A_D nor a polynomial presentation of it. The source weights are
the positive degrees (4), not an assumed homogeneous grading for
the derivation Delta itself.

## 6. No relation of the required weight exists

There is no positive-weight-one polynomial for weights (2,2,3).
At weights two and four, every polynomial is a linear or quadratic
form in mathsf Y,mathsf Z, whose images are algebraically independent.
At weight three a polynomial is a scalar multiple of mathsf W;
at weight five it is mathsf W times a linear form in mathsf Y,mathsf Z.
Their nonzero images cannot multiply to zero in F[eta]. Thus there
is NO nonzero weighted homogeneous relation of any weight one
through five. This contradicts (10),(20).

The contradiction proves that (2) cannot occur in the full retained
actual chart. After515's separate exclusion of e=0, the only
remaining noncomplex-coupling degree-drop branch has g_3=0.
No conclusion about that remaining branch, other projected curves,
or arbitrary chart entry is obtained by this note alone.

## 7. Verification and exact scope

The current sources512,515 and the actual264 input have been read.
Source158 was read completely to distinguish its sliced four-ring
hypotheses from the direct three-ring cofactor proof above. Nothing
from its leading-LND construction or original global-slice premise
is applied to Delta. Every needed cofactor and multiplicity argument
is supplied here independently.

Fresh unsaved fbfe1e constructs the whole generic adjugate for
polynomial rows of degrees(2,2,3). Its t,s,P degree rows are
(4,4,3),(4,4,3),(5,5,4), confirming in particular the W-column
bounds(12). It also enumerates every monomial of weights one
through five used in Section6. These finite checks supplement,
not replace, the exact field, kernel and growth proofs.

Two separate AI reconstructions independently checked the all-ring
chain rule, the P-column degree-four boundary, every iteration's
actual-ring license, the FULL initial kernel, multiplicity residue,
quadratic invariant growth and all small weights. Both found the
outlined proof clean before authoring. A complete saved-source
review remains separate from those outline checks.

All original lower coefficients, both actual returns, the genuine
levels and calibrated nonzero scalar are retained. The proof needs
no new root, generic-coordinate promotion, converse or realization.
This is not an unrestricted cancellation result or a novelty claim.
No saved checker was executed, imported, compiled or rerun, and
no earlier source or canonical record was edited in authoring it.
