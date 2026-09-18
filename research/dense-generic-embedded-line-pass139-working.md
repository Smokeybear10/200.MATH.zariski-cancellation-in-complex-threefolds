# Degree-controlled embedded lines in the dense three-good case

The dense-speed case admits a bounded-degree description after passing
to the intrinsic invariant field. The first two negative coefficients
of an exact Taylor expansion give a nonzero equation for the generic
line and a polynomial expression for its parameter. In particular,
the generic good-coordinate degrees are bounded by the last
coordinate's time degree plus one.

These are working generic-fiber results. They do not descend the
coefficient-field coordinates to complex polynomial coordinates or
solve cancellation for all supplied three-good frames.

## 1. Actual hypotheses and conclusions

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX,\quad t=EY,\quad b=EZ,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b)=2,\qquad
H(s,t,b)\ne0\ \text{for every nonzero homogeneous }
H\in\mathbb C[S,T,V].
\end{gathered}
\tag{1}
\]
All four displayed generators are actual polynomial coordinates.
Write \(m=\deg_E W\ge0\). No upper bound on \(m\) is assumed.
The given slice \(u\) is not assumed to be an ambient coordinate.

The selected actual partial \(T=\partial_W\) has exact degree two
in the \(u\)-filtration. Its leading coefficient is a nonzero
locally nilpotent derivation \(N\) of \(A\), fixing the speeds.[^1]
Put \(S_0=\ker_A N\), \(L=\operatorname{Frac}S_0\), and
\(A_L=(S_0\setminus\{0\})^{-1}A\). There are actual localized
Taylor coordinates \(y,z,w_0\), coefficient parameters
\(\tau=t/s,\rho=b/s\), and a generic line parameter \(v\), with
\[
\begin{gathered}
L/\mathbb C(\tau,\rho)\text{ finite separable},\qquad
A_L=L[v],\qquad N'=[X^2]T|_{A_L}=N/s^2=\partial_v,\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=\sum_{j=0}^{m}w_jX^j,\qquad
w_j\in L[y,z],\quad \deg_{y,z}w_j\le m-j .
\end{gathered}
\tag{2}
\]
The degree statement means that a polynomial representative in two
independent formal variables has the stated degree. Those
representatives need not be unique after evaluation at \(y,z\).
The actual-chart proof establishes (2) without using any classification
of the intrinsic quotient surface.[^2]

There are polynomials \(\Phi,\Psi,g\in L[U,V]\) such that
\[
\begin{gathered}
0\ne\Phi,\quad \deg\Phi\le m+1,\quad \Phi(y,z)=0,\\
\deg\Psi\le m+2,\quad \partial_v\Psi(y,z)=1,\quad
L[y,z]=L[\Psi(y,z)]=L[v],\\
\ker\bigl(L[U,V]\longrightarrow L[v],\ (U,V)\mapsto(y,z)\bigr)=(g),
\quad g\text{ irreducible},\quad 1\le\deg g\le m+1 .
\end{gathered}
\tag{3}
\]
The first two statements are consequences of the tail argument,
not a selection of a factor over a larger field.[^3]
Moreover
\[
\deg g=\max\{\deg_v y,\deg_v z\}\le m+1,\qquad
\deg_v w_j\le(m-j)(m+1)
\tag{4}
\]
for nonzero coefficients; constant generic coordinates have degree zero.
At least one of \(y,z\) is nonconstant because they generate \(L[v]\).

By the classical plane epimorphism theorem, \(g\) is a coordinate of
the polynomial ring \(L[U,V]\).[^4] This last assertion is only over
the coefficient field \(L\), not over \(\mathbb C\).

## 2. Why the negative tail cannot be omitted

The full actual chart first normalizes the Jacobian to one:
\[
\det
\begin{pmatrix}
y_\tau+X&y_\rho&y_v\\
z_\tau&z_\rho+X&z_v\\
W_\tau&W_\rho&W_v
\end{pmatrix}=1 .
\tag{5}
\]
The selected cofactor gives \([X^2]T(v)=1\).
Here \(\partial_\tau,\partial_\rho\) act on the finite separable
coefficient field and are extended to fix \(v\).
The partial \(T\) itself need not preserve \(L\).

For independent formal \(U,V\), define
\[
H_d(f;U,V)=\sum_{a+b=d}
\frac{\partial_\tau^a\partial_\rho^b f}{a!\,b!}U^aV^b,\qquad
\Theta(f)=\sum_{d\ge0}H_d(f;y,z)X^{-d}.
\tag{6}
\]
The coefficientwise Taylor map is multiplicative, and its nonzero
constant term makes it a field embedding into \(L(v)((X^{-1}))\).
It sends the separating base parameters to \(Y/X,Z/X\), which the
actual \(T\) kills. Separable algebraicity then proves
\(T\Theta(f)=0\) for every \(f\in L\).
The derivation extends continuously to this formal Laurent field
because its coefficient-degree shift is uniformly at most two.
There is no analytic convergence or global coordinate change here.

Successively subtracting the top terms \(X^j\Theta(f_j)\), for
\(j=m,\ldots,0\), yields \(f_j\in L\) and
\[
\mathscr S=\sum_{j=0}^mX^j\Theta(f_j),\qquad
W=(\mathscr S)_{\ge0},\qquad
\mathscr R=W-\mathscr S,\qquad T\mathscr R=1 .
\tag{7}
\]
This is the source of the representatives in (2). Discarding
\(\mathscr R\) would discard the equation \(T(W)=1\).

The coefficient of \(X\) in \(T\mathscr R\) says that
\[
\begin{gathered}
R_1(U,V)=-\sum_{j=0}^m H_{j+1}(f_j;U,V),\qquad
f_{-1}=R_1(y,z)\in L,\qquad \Phi=R_1-f_{-1},\\
\Psi(U,V)=-\sum_{j=0}^mH_{j+2}(f_j;U,V)
             -H_1(f_{-1};U,V).
\end{gathered}
\tag{8}
\]
If \(\Phi\) were the zero formal polynomial, its homogeneous parts
would make all order-\(j+1\) derivatives of each \(f_j\) zero.
All higher derivatives would then vanish, so every Taylor term would
truncate and \(W=\mathscr S\). That contradicts \(T(W)=1\).
Thus the relation in (3) is genuinely nonzero.

Subtracting \(X^{-1}\Theta(f_{-1})\) from \(\mathscr R\) leaves a
tail starting at \(X^{-2}\). Its first coefficient is
\(\Psi(y,z)\), so the constant term of its \(T\)-image gives
\(\partial_v\Psi(y,z)=1\).
Consequently \(\Psi(y,z)=v+c\), \(c\in L\), and (3) follows.
These arguments include \(m=0\).

## 3. The implicit and parametric degrees agree

Here is a direct proof of (4), using only the equality
\(L[y,z]=L[v]\). Let \(D=\deg g\), extend the coefficient field
by an independent indeterminate \(\lambda\), and write
\(K=L(\lambda)\), \(q=z+\lambda y\).
The leading coefficients cannot cancel identically in \(\lambda\), so
\(\deg_v q=\max(\deg_v y,\deg_v z)=d\).

The polynomial \(g(U,Q-\lambda U)\) is irreducible in \(K[U,Q]\).
Its coefficient of \(U^D\) is
\(g_D(1,-\lambda)\ne0\), where \(g_D\) is the highest homogeneous
part of \(g\). Thus its degree in \(U\) is exactly \(D\), and
Gauss's lemma makes it irreducible in \(K(Q)[U]\).
The evaluation field is
\(K(y,q)=K(y,z)=K(v)\). Therefore
\[
[K(v):K(q)]=D .
\quad\text{Also}\quad
[K(v):K(q)]=\deg_v q=d .
\tag{9}
\]
For the second equality, \(q(T)-Q\) is irreducible over \(K(Q)\):
it is primitive and linear in the independent \(Q\) over \(K[T]\),
then Gauss's lemma applies. Its \(T\)-degree is \(d\).
This proves \(D=d\le m+1\).

Substitution of \(y(v),z(v)\), each of degree at most \(m+1\),
into the representative for \(w_j\) of degree at most \(m-j\)
proves the second bound in (4).
No claim that either individual degree is one follows.

## 4. The exact generic coordinate conclusion and its limits

The two-variable polynomial ring \(L[U,V]\) maps onto \(L[v]\)
with kernel \((g)\). The plane epimorphism theorem in characteristic
zero gives \(L[U,V]=L[g,h]\) for some \(h\).
Russell and Sathaye state this precise field-level theorem as
Section 1.1, citing Abhyankar and Moh.[^4]
Its hypotheses concern a polynomial ring over a field; they hold
over \(L\) even when \(L/\mathbb C(\tau,\rho)\) is nontrivial.

There is a useful distinction between \(g\) and the tail polynomial
\(\Phi\). The tail identities give
\((\Psi_U,\Psi_V)=(\Phi_\tau,\Phi_\rho)\) and imply that
\((\Phi_U(y,z),\Phi_V(y,z))L[v]=L[v]\).
If \(\Phi=gH\), it follows that \(H(y,z)\in L^*\), so \(g\)
occurs with multiplicity one. It does not follow that \(H\) is
constant in the two-variable polynomial ring. The complete chain-rule
proof is in the tail note.[^3]

Nor must the particular pair \((g,\Psi)\) be a plane automorphism.
For example \(g=V\) and \(\Psi=U+VU^2\) generate the right quotient
parameter modulo \(g\), but their Jacobian is
\(-(1+2UV)\), not a unit.
The existence of some complement \(h\) does not identify \(\Psi\)
as that complement.

Likewise \(y=v^2,z=v+v^4\) generate \(L[v]\), since \(z-y^2=v\),
while neither is linear in \(v\). Their primitive relation
\((V-U^2)^2-U\) has degree four, agreeing with (4)'s general
degree equality. These are elementary plane controls, not assertions
of actual sliced fourfold realization.[^5]

The actual coefficient-field localization satisfies
\[
(S_0\setminus\{0\})^{-1}B=L[v,X]=L[X,Y,Z],
\tag{10}
\]
and \(W\) can be eliminated there. None of (2)--(10) removes
the invariant denominators or the algebraic coefficient extension.
There is no inferred invariant ambient coordinate over \(\mathbb C\),
no recognition of every dense higher-degree frame, and no construction
of three good coordinates for an arbitrary cylinder.

## Sources

1. [Intrinsic leading derivation125](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2--5, and [dense selected degree132](dense-three-good-adjoint-degree-pass132.md),
   Sections 2--5. No use of125's source-dependent quotient-surface
   classification in Section 6 is required here.
2. [Actual dense all-degree Taylor chart139](dense-all-degree-taylor-chart-pass139-working.md).
   Actual localization, exact-field Taylor annihilation and peeling.
3. [First two negative Taylor coefficients139](dense-negative-tail-relations-pass139-working.md).
   Nonzero relation, polynomial slice, gradient ideal and multiplicity.
4. Peter Russell and Avinash Sathaye,
   [*On Finding and Cancelling Variables in k[X,Y,Z]*](https://www.ms.uky.edu/~sohum/ma561/affgeom/vars_in_k3.pdf),
   Journal of Algebra 57 (1979), 151--166, Section 1.1, printed p. 153.
   The stated epimorphism theorem is attributed to Shreeram S. Abhyankar
   and Tzuong-tsieng Moh,
   [*Embeddings of the line in the plane*](https://doi.org/10.1515/crll.1975.276.148),
   Journal für die reine und angewandte Mathematik 276 (1975), 148--166.
5. [Dense sliced examples and plane controls139](dense-sliced-controls-pass139.md),
   with the [finite exact checker139](dense_taylor_tail_controls_pass139.py).
   These verify specific identities, not the universal theorem.

The algebraic derivations above and in Sources 2--3 are working proofs.
The classical epimorphism theorem is an explicit external input,
not a new proof reconstructed here. Human expert review,
proof-assistant verification and historical novelty determination
remain outstanding.

[^1]: Source 1, the actual leading-LND construction and selected degree.
[^2]: Source 2, the complete localized chart and peeling argument.
[^3]: Source 3, especially Sections 2--4.
[^4]: Source 4, Section 1.1. The original1975 proof is not claimed newly audited.
[^5]: Source 5, the explicit distinction between actual frames and plane controls.
