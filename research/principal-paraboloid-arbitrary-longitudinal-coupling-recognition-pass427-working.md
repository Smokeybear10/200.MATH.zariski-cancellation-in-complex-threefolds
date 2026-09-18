# Recognition with arbitrary longitudinal coupling and two one-variable potentials

Working result, conditional on the retained actual chart264 and the
specified earlier recognition inputs: the original kernel is C^[3] if

    k_s is a nonzero complex constant,    n_s=ell_s=0.

There is NO condition on k_ttt. This removes that derivative restriction
from this two-one-variable-potential sector, not from all of422's scope.
It does not normalize arbitrary coupling or establish entry into the
principal chart from an arbitrary cancellation candidate.

The new k_ttt nonzero branch is proved directly below. Its key step is
an elementary root-multiplicity obstruction, followed by an actual
preserved polynomial three-ring. It does not require the lengthy
nonlinear-potential exclusions418--423. The k_ttt zero branch uses
348's actual normalization and337's retained recognition result.

## 1. Full actual entry and the limited normalization

Retain EVERY actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), including
the full weighted initial ideal and the literal selected derivation:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\quad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad a=EX\ne0,\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\quad
N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,
\quad Na=Nt=Ns=0,\quad Nv=1,\\
O=L[v]=L[y,z,w]=L[y,\sigma,\theta],\quad
K=\operatorname{Frac}A=\mathbb C(y,z,w)=L(v),\\
J(X)=\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a^4\in L^*.
\end{gathered}
\tag{1}
\]
Assume additionally k_s=m in C*, n_s=ell_s=0. The actual map
W_1=mW, with X,Y,Z unchanged, has polynomial inverse W=W_1/m.
It gives s_1=ms, theta_1=m theta, w_1=mw, k_{s_1}=1.
Both potentials n and ell are unchanged. The full initial ideal
is preserved, the literal Z-partial and N are unchanged, and both
actual returns survive. The row determinant and coefficient change
each multiply by m, so the calibrated J remains -a^4.

Rename the normalized variables. Thus throughout Sections2--5,
\[
k=s+f,\qquad f,n,\ell\in\mathbb F:=\ker_L\partial_s,
\qquad [\mathbb F:\mathbb C(t)]<\infty.
\tag{2}
\]
These are exact field elements, not presumed rational functions or
polynomials in t. Primes denote the extended t-derivative, whose
constant field is C. All coefficient partials fix v. The coefficients
of the actual fixed-X expansions belong to A_a, not necessarily A.

The first two complete potentials264 specialize to
\[
\begin{aligned}
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-n'\sigma,\\
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+s+f)X+t^2X^2,\\
W&=w+\theta X+sX^2.
\end{aligned}
\tag{3}
\]

## 2. A cubic relation and its evaluated gradient unit

In independent formal variables U,P,V, the complete third potential is
\[
H=U^2+(f''P+n')U+\frac{f'''}6P^3
                 +\frac{n''}2P^2-\ell'P,
\qquad H(y,\sigma,\theta)=h\in L.
\tag{4}
\]
It is independent of V because n_s=ell_s=0 and the normalized
coupling has k_s=1 and no mixed or second s-derivative.
The level h is not assumed s-constant.

Here is a direct verification of the needed gradient-unit property,
without invoking the fourth-potential argument296. Let d hold X
fixed, and let A_X=dY, B_X=dZ-2t dY, C_X=dW. Put
\[
\gamma=2\sigma+f',\qquad
\beta=2y+f''\sigma+n'=H_U^{\rm ev},\qquad
\rho=f''y+\frac{f'''}2\sigma^2+n''\sigma-\ell'=H_P^{\rm ev}.
\tag{5}
\]
The full rows(3), differentiated before any substitution of X, give
\[
\boxed{C_X+\gamma A_X-XB_X
       =-\beta(d\sigma+Xdt)-\rho\,dt.}
\tag{6}
\]
For example dw=-gamma dy-beta d sigma-rho dt, while
B_X=gamma d sigma+d theta+beta dt+X(gamma dt+ds).
These identities keep all coefficient derivatives of f,n,ell.

At X=0, taking the determinant of(6) with the first two rows
expresses the unit J(0)=-a^4 as an O-linear combination of beta
and rho. Consequently
\[
(\beta,\rho)O=O.
\tag{7}
\]
This uses the original calibrated scalar, not merely the formal
existence of a cubic relation.

Complete the square over L, not in the ambient polynomial ring:
\[
x=y+\frac{f''\sigma+n'}2,\qquad
R(P)=\frac{(f''P+n')^2}{4}-\frac{f'''}6P^3
       -\frac{n''}2P^2+\ell'P+h.
\tag{8}
\]
Then the exact identities are
\[
x^2=R(\sigma),\qquad
\beta=2x,\qquad \rho-f''\beta/2=-R'(\sigma).
\tag{9}
\]
Here R' in(9) means the FORMAL P-derivative, not the t-derivative.
Thus(7) is equivalent to
\[
(2x,R'(\sigma))O=O.
\tag{10}
\]

## 3. Elementary polynomial obstruction

**Lemma.** Let F be a characteristic-zero field, R in F[P] a
polynomial of degree at least three, and x,p in F[v]. If
x^2=R(p) and (2x,R'(p))F[v]=F[v], then p and x are constant.

**Proof.** Extend scalars to an algebraic closure of F; a Bezout
identity for the unit ideal survives. Suppose d=deg p is positive.
Every scalar r has a preimage under the nonconstant polynomial p.
If R had a repeated root r, choose v_0 with p(v_0)=r. The equation
gives x(v_0)=0 and R'(p(v_0))=0, contradicting the unit ideal.
Thus R is squarefree.

Choose three distinct roots r_1,r_2,r_3 of R. At a root v_0 of
p-r_i, all other factors of R(p) are nonzero, so its multiplicity
equals that of p-r_i. Since R(p)=x^2, this multiplicity is even.
For each i there are at most d/2 distinct roots of p-r_i. The
polynomial p' therefore has at least d-d/2=d/2 zeros counted with
multiplicity on that fiber. The three fibers are disjoint. In
characteristic zero p' is nonzero of degree d-1, but this gives

    d-1 >= 3d/2,

which is impossible. Hence p is constant. The square of x is
then constant, so x is constant as well. This proves the lemma.

The lemma includes repeated-root cubics by the first part of its
proof. No smoothness, genus formula, whole plane-ring return, or
parametrization of a singular cubic has been assumed.

If f''' is nonzero, R in(8) has exact degree three, with cubic
coefficient -f'''/6. Equations(9)--(10) and the lemma therefore imply
\[
\boxed{f'''\ne0\quad\Longrightarrow\quad y,\sigma\in L.}
\tag{11}
\]
The conclusion concerns the actual generic-line functions. It does
not make either of them an ambient coordinate.

## 4. The constant projection gives an actual preserved three-ring

From(3),(11), w belongs to L and z=theta+z_c with z_c in L.
The whole return O=L[y,z,w] consequently gives
\[
L[\theta]=L[v],\qquad N\theta\in L^*.
\tag{12}
\]
This uses equality of polynomial rings, not only of fraction fields.

Extend N from A to B=A[u] by Nu=0 and write X=au+x_0 with
x_0 in A. Define the ORIGINAL-ring derivation
\[
\mathcal P=aN-(NX)E.
\tag{13}
\]
Since Na=0 and E commutes with the extended N, this commutes
with E, fixes X, and restricts to aN on A. In particular it is
locally nilpotent on A and
\[
\mathcal P^j(u)=-a^{j-1}N^j(x_0)\quad(j\ge1).
\tag{14}
\]
Thus it is locally nilpotent on B=A[u]. This argument neither
assumes a is a unit of A nor assumes N has a global slice.

On A_a[X], P acts as aN on coefficient functions and fixes X.
The literal rows(3),(11)--(12) therefore give, as equalities in B,
\[
\mathcal PX=\mathcal PY=0,\quad
\mathcal PZ=\tau,\quad \mathcal PW=X\tau,
\qquad \tau=aN\theta\ne0.
\tag{15}
\]
The actual shear S=W-XZ has polynomial inverse W=S+XZ. Hence
\[
B=\mathbb C[X,Y,S][Z],\quad
\mathcal P=\tau\partial_Z,\quad
\ker_B\mathcal P=R_0:=\mathbb C[X,Y,S].
\tag{16}
\]
The last equality follows from the domain property and characteristic
zero even if tau is a nonunit. Commutation makes R_0 E-stable.

The restriction delta=E|R_0 is nonzero, with delta X=a and
delta^2 X=0. Let c be the gcd of its three coordinate coefficients.
Since c divides the invariant a, additivity of locally nilpotent
degree gives delta c=0. Thus D=delta/c is an irreducible locally
nilpotent derivation of this ACTUAL polynomial three-ring, with
DX nonzero and D^2X=0.

[Daigle's theorem as stated in Dasgupta--Gupta, Theorem4.8](https://arxiv.org/html/1701.03635v1)
then supplies an invariant coordinate of R_0, hence of B=R_0[Z].
The original global slice makes A regular: A=B/(u), and
E(u)=1 expresses 1 in the ideal of the original coordinate
partials of u, so that hypersurface is smooth.
[Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
applies to the original nonzero E fixing that ambient coordinate
and gives A isomorphic to C^[3]. This proves recognition for the
new f''' nonzero branch.

## 5. The f''' zero branch and the precise assembled statement

If f'''=0, exact constants give
f=gamma t^2/2+b t+d with gamma,b,d in C. Working in the ORIGINAL
pre-normalized chart with k_s=m, the actual map supplied by348 is
\[
X_*=X-\gamma/2,\quad Y_*=Y,\quad Z_*=Z,\quad
W_*=mW-\gamma Z/2+bY+dX^2.
\tag{17}
\]
It has a polynomial inverse, using only division by m. The full
actual-chart transport was proved in
[348](principal-paraboloid-constant-coupling-general-first-normalization-pass348-working.md),
with its B=-gamma/2 and first-potential f there equal to n here.
Its complete transported potentials give
\[
\begin{aligned}
k_*&=s_*,\qquad n_*=n-\gamma^2t^2/4,\\
\ell_*&=\ell-\gamma n/2+\gamma t n'-\gamma^3t^2/4,
\qquad \partial_{s,*}=m^{-1}\partial_s.
\end{aligned}
\tag{18}
\]
Both starred potentials have zero s*-derivative. Thus the retained
working recognition theorem
[337](principal-paraboloid-two-one-variable-potentials-recognition-pass337-working.md)
applies. This branch uses337's stated dependencies; it is not a
new recursive certification of them.

Combining the two branches gives the working implication
\[
\boxed{\text{Under EVERY actual hypothesis of264,}\quad
k_s\in\mathbb C^*,\quad n_s=\ell_s=0
\quad\Longrightarrow\quad A\cong\mathbb C^{[3]}.}
\tag{19}
\]
There is no derivative bound on the longitudinal coefficient
k-ms, and no rationality or polynomiality assumption on n or ell.
For k_ttt nonzero, the stronger necessary conclusion Ny=N sigma=0
also holds in the normalized chart.

## 6. Evidence and boundaries

Root read264 and425 completely in d97aa1,348 and424 in3c1893,
296 and422 inbb9a32, and337 in75d5bb. The writing guide was read
through EOF8756ee. Fresh unsaved d93d9f checked the centered cubic,
gradient transport and complete actual m-scaling. Fresh93adad
reconstructed every component of the all-X covector identity(6)
with arbitrary coefficient functions, and the transported potentials
in(18). All residuals were zero. These finite identities do not
replace the root-counting or original-ring arguments above.

The exact primary endpoint statements were freshly inspected in
turn4635view0--1. Independent full-source review and the final hash
are recorded separately after that review, not presumed here.

This is a restricted-chart working result. It has no expert review,
formal proof-assistant verification or novelty clearance. No actual
example with these added hypotheses and k_ttt nonzero is supplied:
the necessary-case argument does not assert nonvacuity. The result
neither forces n_s=ell_s=0 in a general candidate nor makes k_s
constant, and does not solve arbitrary-frame entry or cancellation.
No saved checker was executed, imported, compiled or rerun. No
older proof was edited, and no external contact or submission occurred.
