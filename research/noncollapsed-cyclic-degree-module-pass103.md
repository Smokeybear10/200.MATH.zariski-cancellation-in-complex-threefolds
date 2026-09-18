# A noncollapsed double component determines every local degree module

In the actual nonconical quadratic frame, a noncollapsed fixed component
forces an exact conic presentation over the local invariant base. This
holds with either first normal action and does not require a nonzero
speed normal at the base point. The two generators are an actual good
projection U and its actual derivative V=NU.

The proof uses a single generic double component to produce bases of
all degree modules. It consequently recovers the entire local fiber,
not just a completed neighborhood of that component. A higher-order
first plinth remains possible in the resulting intrinsic conic model;
no recognition of A or unrestricted frame reduction is asserted.

## 1. Actual inputs and the nonzero nilpotent derivative

Retain the actual nonconical quadratic setting and canonical field of
[Jacobian91](nonconical-global-jacobian-field-pass91.md). In particular
the following are actual rings, elements, and derivations:
\[
\begin{gathered}
B=A[u]=\mathbb C[x_1,x_2,x_3,z],\qquad
S=\ker(N|_A)=\mathbb C[s_1,s_2],\qquad K=\operatorname{Frac}S,\\
A\text{ is a smooth complex domain},\qquad
S\longrightarrow A\text{ is faithfully flat},
\qquad A_K=K[v],\qquad N|_{A_K}=\lambda\partial_v,
\quad\lambda\in K^*,\\
A=S[A_1,A_2,c],\qquad N^3A_i=0,\qquad N^5c=0,\\
\mathfrak m\subset S\text{ is closed},\qquad
\mathfrak q\in\operatorname{Min}(\mathfrak mA)
\text{ is a noncollapsed fixed component}.
\end{gathered}
\tag{1}
\]
Noncollapsed means that some constant complex linear combination U
of the two good relative generators has nonconstant residue on this
component. The generic component-degree and local Jacobian arguments
in [noncollapsed95](noncollapsed-quadratic-local-translation-model-pass95.md),
through its equation (4), give
\[
\begin{gathered}
O=A_{\mathfrak q},\quad \mathfrak n=\mathfrak qO,\quad
C=O/\mathfrak mO,\qquad
\operatorname{length}_O C=2,\qquad
\kappa(\mathfrak q)=\mathbb C(\bar U),\\
N^3U=0,\qquad p:=N^2U\in S\setminus\{0\},\qquad V:=NU,\\
V\equiv\delta x+\lambda_0 y\pmod{\mathfrak n^2},
\qquad \lambda_0\ne0,\qquad x\in\mathfrak mO,\\
\boxed{\quad
\bar V\ne0\text{ in }C,\qquad \bar V^2=0,\qquad
C/\sqrt{0}=\mathbb C(\bar U).
\quad}
\end{gathered}
\tag{2}
\]
Here x,y are the retained actual regular parameters, with an actual
coefficient field \(\mathbb C(U)\subset O\). The coefficient
\(\lambda_0=2\epsilon_0a_{02}\) is nonzero because the transverse
fiber has length two. That calculation precedes, and does not use,
the nonzero-first-normal-action hypothesis in95.

For clarity, the maximal ideal of a length-two local Artinian ring
is nonzero and has square zero. Thus \(\mathfrak n^2\subset\mathfrak mO\),
and the class of y is a nonzero generator of that maximal ideal.
The displayed congruence makes the class of V nonzero. Since the
component is fixed, V belongs to \(\mathfrak q\); its square is zero
in C. This verifies the required nilpotent class without asserting
that an arbitrary primitive field acts nontrivially on every chosen
thickening. No whole-fiber irreducibility or absence of punctures is
an input to (2).

## 2. The general image bound and its equality case

More generally, the argument below applies to any domain A with a
nonzero LND N, the flat full-kernel inclusion S and generic line in (1), a closed m,
and a multiplicity-two fixed component q, provided there is an
actual U in ker N cubed with nonconstant residue on q and with
NU nonzero in its generic Artinian fiber. U need not be an original
good combination. The residue-field equality in (2) is not needed
for this general implication: a nonconstant residue is already
transcendental over the complex numbers. The conclusions (4)--(5)
follow; smoothness additionally gives (6). Section 1 verifies all
these gates for the actual noncollapsed quadratic component.

In this general form N squared of U cannot be zero. Otherwise
V=NU would lie in S and have a scalar residue at m. Fixedness
puts V in q, so that scalar is zero, contradicting its specified
nonzero nilpotent class. Thus U has degree exactly two and V
degree exactly one, as used below.

Set R=S_m, \(\mathfrak r=\mathfrak mR\), and \(A_R=A\otimes_S R\).
The finite locally free degree-module theorem in
[degree-module102](quadratic-degree-module-fiber-rigidity-pass102.md),
equation (2), applies independently of that note's later collapsed
fiber hypotheses. It gives, for every n at least zero,
\[
\begin{gathered}
F_n=\ker(N^{n+1}:A_R\longrightarrow A_R),\qquad
F_n\simeq R^{n+1},\\
\dim_{\mathbb C}\operatorname{im}
\bigl(F_n\longrightarrow A_R/\mathfrak rA_R\bigr)\le n+1.
\end{gathered}
\tag{3}
\]
The local freeness uses finiteness of successive derivative-image
ideals, invariant principal saturation, and faithful flatness over
the regular surface. It does not require those image ideals to be
locally free. The dimension bound follows by factoring the reduction
map through the module fiber. Without further information it is
only an upper bound, not an assertion that this map is injective.

In the present sector the bound is attained in every degree. Since
V has N-degree one and U has N-degree two, define
\[
\begin{aligned}
\mathcal B_{2k}
 &=\{1,U,\ldots,U^k\}\ \cup\ \{V,VU,\ldots,VU^{k-1}\},\\
\mathcal B_{2k+1}
 &=\{1,U,\ldots,U^k\}\ \cup\ \{V,VU,\ldots,VU^k\},\\
\boxed{\quad F_n=\bigoplus_{b\in\mathcal B_n}Rb,\qquad
F_n\cap\mathfrak rA_R=\mathfrak rF_n.\quad}
\end{aligned}
\tag{4}
\]
The second set is empty in the first line when k=0. Each set has
n+1 elements and is contained in F_n by the Leibniz rule.

To prove independence, map to the single Artinian ring C in (2).
A constant complex linear relation has the form
P(\(\bar U\))+\(\bar V\)Q(\(\bar U\))=0. Reducing to its residue
field first gives P=0, because \(\bar U\) is transcendental over
the complex numbers. A nonzero Q(\(\bar U\)) is a unit of C, so
it cannot annihilate the nonzero \(\bar V\). Hence Q=0 as well.
This only needs the residue and unit statements, even if the
component field was not initially known to equal \(\mathbb C(\bar U)\).

The classes of these n+1 elements are therefore independent in
F_n/\(\mathfrak rF_n\). By (3) they are a basis of that vector
space. Nakayama gives the R-basis in (4). Independence of its
residues in C also proves the displayed intersection statement.
This is a proved equality case, not a general base-change claim
about degree modules.

## 3. The entire local algebra is the actual cyclic conic

Local nilpotence makes the union of the F_n equal to A_R. Equation
(4) therefore gives A_R=R[U,V]. Put \(\eta=2pU-V^2\).
Since NU=V and NV=p, this element is invariant. Kernel localization
gives \(\eta\in R\); in fact U,V,p are global elements, so
\(\eta\in S\). Both p and eta vanish at m because they belong
to \(\mathfrak q\cap S\). We obtain
\[
\begin{gathered}
p=N^2U\ne0,\qquad \eta=2pU-V^2\in\mathfrak m,\\
\boxed{\quad
A_R\simeq R[\mathsf U,\mathsf V]/
(\mathsf V^2-2p\mathsf U+\eta),
\qquad \mathsf U\mapsto U,\quad\mathsf V\mapsto V.
\quad}\\
NU=V,\qquad NV=p,\qquad N|_R=0,\\
F_1=R\oplus RV,\qquad N(F_1)=pR,\\
A/\mathfrak mA\simeq\mathbb C[\bar U,\bar V]/(\bar V^2).
\end{gathered}
\tag{5}
\]
There is no hidden extra kernel in the presentation. The proposed
source is free over R[\(\mathsf U\)] with basis
1,\(\mathsf V\), because the equation is monic in \(\mathsf V\).
It is therefore R-torsion-free. After passing to K, p is a unit
and the equation solves for \(\mathsf U\), while V has generic
degree one and generates A_K. The surjective map is then an
isomorphism. Its original kernel is R-torsion and must be zero.

Reduction at m gives the last line of (5). Localizing S outside m
does not change this fiber. Thus a noncollapsed fixed component
is necessarily the whole reduced fiber and is the entire affine
line with coordinate \(\bar U\). These conclusions were known
from96 by other arguments. Here they follow directly from the
new module bases, without using those conclusions in the proof.

One can use just F_2 and F_4 for the actual finite generating set:
their bases are 1,V,U and 1,V,U,VU,U^2. The elements A1,A2 belong
to F_2 and the specified c belongs to F_4, so these two bases
already give the same algebra generation. The all-degree argument
also proves the exact filtration and does not need that additional
degree bound on c. Neither argument identifies U or V as original
ambient coordinates.

## 4. Smoothness permits exactly two first-order base configurations

At a closed point of the fiber write U=t0 and V=0. In the ambient
regular local ring R[\(\mathsf U,\mathsf V\)] the linear term
of its defining equation is \(d\eta-2t_0\,dp\). The quotient
is regular because A is smooth. A hypersurface in a regular local
ring is regular precisely when its equation is not in the square
of the maximal ideal. Thus this vector cannot vanish for any
complex t0. Since \(\mathfrak r/\mathfrak r^2\) has dimension two,
\[
\boxed{\quad
\begin{cases}
dp=0,\quad d\eta\ne0,\quad\text{or}\\
dp,d\eta\text{ are linearly independent}
\end{cases}
\qquad\text{in }\mathfrak r/\mathfrak r^2.\quad}
\tag{6}
\]
Indeed if dp is nonzero and d eta is its scalar multiple, that
multiple is 2t0 for a complex t0, giving a singular point. If dp
is zero, the condition is exactly that d eta is nonzero.

In the independent case p,eta form base parameters. In the first
case eta is a parameter and p belongs to the base square. The
corresponding normal action is transparent from (5): at the generic
fiber point one may eliminate eta to use any independent base
parameter x together with V as normal parameters. Then Nx=0 and
NV=p. In the independent case p has nonzero normal linear part;
in the first case p has no normal linear part. This recovers both
first-normal branches without assuming either one in (2)--(5).

## 5. Higher first-plinth order is an actual intrinsic boundary

The first alternative in (6) is not empty as an intrinsic polynomial
algebra with a flat kernel plane. For every integer e at least one,
take
\[
\begin{gathered}
A_0=\mathbb C[x,V,U],\qquad
f=V^2-2x^eU,\qquad S_0=\mathbb C[x,f],\\
N_e=x^e\partial_V+V\partial_U,
\qquad \ker N_e=S_0,\qquad N_eU=V,\qquad N_e^2U=x^e,\\
A_0\simeq S_0[\mathsf U,\mathsf V]/
(\mathsf V^2-2x^e\mathsf U-f),\qquad
\mathfrak m_0=(x,f),\\
A_0/\mathfrak m_0A_0=\mathbb C[U,V]/(V^2),
\qquad p=x^e,\qquad\eta=-f.
\end{gathered}
\tag{7}
\]
The displayed presentation is free of rank two over S0[U],
so S0 into A0 is faithfully flat. The derivation is triangular
and locally nilpotent, and its coefficient gcd is one. With
the order x,V,U, twice this field is the Jacobian derivation
Jac(x,f,-), so the volume normalization differs only by a
nonzero constant.

For the exact kernel, invert x. The resulting algebra is
\((S_0)_x[V]\), and the invariant ring is \((S_0)_x\).
If a minimal expression x^{-k}P(x,f) is polynomial in A0 with
k positive, reduction of x^k times that equality modulo x
gives P(0,V^2)=0. The substitution from \(\mathbb C[f]\)
to \(\mathbb C[V]\) is injective, so x divides P in S0,
contradicting minimality. This proves the claimed whole kernel.

For e=1 the two differentials in (6) are independent. For every
e at least two, dp=0 and d eta is nonzero; the first normal action
is zero and the first plinth has arbitrarily high order e.
All the module and conic conclusions above hold. The rings A0
are themselves polynomial threefolds, so this is not a failure
of recognition. Nor is the indicated N asserted to be the
highest canonical field of an actual supplied nonconical E-frame.
It shows exactly why the cyclic conic and smoothness alone do
not make p a base coordinate or exclude the zero-normal branch.

## Scope and dependencies

The new result is the actual local presentation and full module
basis at every noncollapsed fixed double component, including
L(m)=0 and either first normal action. It uses the elementary
finite locally free theorem102 and the component-degree and
actual local Jacobian calculations95 before their extra normal
action hypothesis. It does not invoke the older47--54 unit
second-image or quartic-generation conditions, and it does not
infer freeness of arbitrary successive image ideals from the
freeness of the modules.

The more general form in Section 2 could also apply to a collapsed
component if an actual hidden degree-two U with the stated residues
were found. No existence theorem supplies such a U here. In
particular the specified degree-four generator c need not itself
belong to F_2, and generic dimension or module freeness alone does
not provide the needed injective residue classes.

The proof retains the specified U and NU. It is an algebraic
statement over S_m, not only a completed differential model.
No new primary-source theorem was read for this deduction, no
numerical method certifies it, and no original inverse-frame
realization is claimed for the intrinsic control. All files
through102 are unchanged.
