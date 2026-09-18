# Actual invariants give a denominator-free coefficient fiber

The actual coordinate inverse gives polynomial representatives for all
invariants in the projected source triple. Keeping the three unnormalized
good speeds and one primitive coefficient-field element therefore gives
four polynomial equations whose ideal is exactly the selected generic
curve ideal. No denominator saturation or first-tail equation is needed.

This removes denominator artifacts from the compatibility test. It does
not prove that the first tail forces the four equations, nor that the
first tail is always primitive.

## 1. Actual projection of polynomial invariants

Retain the actual dense three-good setup139 and the source data142:[^1]
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad
s=EX\ne0,\quad t=EY,\quad b=EZ,\\
N=[u^2]\partial_W|_A\ne0,\quad S=\ker_A N,\quad L=\operatorname{Frac}S,\\
\tau=t/s,\quad \rho=b/s,\quad K=\mathbb C(\tau,\rho),\quad [L:K]<\infty,\\
A_s=\mathbb C[y,z,w_0]_{s_0},\qquad
F=\operatorname{Frac}A=L(v),\qquad L[y,z]=L[v],\\
w_0=\Omega(y,z),\quad \Omega\in L[U,V],\qquad
\ker(L[U,V]\to L[v])=(g).
\end{gathered}
\tag{1}
\]
The speed rank is two and its homogeneous cone is dense. In particular
the speed ratios are independent, and the extension in (1) is separable.
The polynomial \(g\) is the irreducible equation for the specified
evaluation \((U,V)\mapsto(y,z)\). The source triple \(y,z,w_0\) is
algebraically independent over \(\mathbb C\).

On \(B_s\), put \(D=E/s\). Since \(Es=0\), this is an LND with
\(DX=1\). Its slice projection is the multiplicative Taylor evaluation
\[
\pi_X(f)=\sum_{j\ge0}\frac{(-X)^j}{j!}D^j(f),\qquad
\pi_X(X,Y,Z,W)=(0,y,z,w_0),\qquad
\pi_X(a)=a\quad(a\in A).
\tag{2}
\]
Each sum is finite. This is the flow evaluated at parameter \(-X\),
not the operator exponential of the variable-coefficient derivation
\(-XD\).

Write an actual invariant as \(a=P_a(X,Y,Z,W)\), with complex
polynomial \(P_a\). Multiplicativity in (2) gives
\[
a=P_a(0,y,z,w_0),\qquad
A\subset\mathbb C[y,z,w_0]\subset A_s.
\tag{3}
\]
Thus every invariant has a polynomial source representative. The reverse
inclusion \(\mathbb C[y,z,w_0]\subset A\) is not claimed: the projected
generators may themselves have invariant denominators in the original
ring. In particular (3) is not a global polynomial presentation of \(A\).

## 2. A primitive element can be chosen polynomially

The intrinsic construction gives \(N(s)=N(t)=N(b)=0\), so the three
speeds belong to \(S\), and \(s\in L^*\). Choose finitely many
\(z_1,\ldots,z_r\in S\) with \(L=K(z_1,\ldots,z_r)\).
Such a list exists: take finitely many field generators of the finite
extension and include their numerators and denominators from \(S\).

There are finitely many distinct \(K\)-embeddings of \(L\) into an
algebraic closure of \(K\). For any two distinct embeddings, at least
one \(z_i\) has different images. The complex coefficient vectors
\((\lambda_1,\ldots,\lambda_r)\) for which their images of
\(\sum_i\lambda_i z_i\) coincide form a proper complex linear
subspace. Finitely many such proper subspaces cannot cover
\(\mathbb C^r\). Consequently one may choose
\[
e=\sum_i\lambda_i z_i\in S,\quad \lambda_i\in\mathbb C,
\qquad L=K(e)=\mathbb C(s,t,b,e).
\tag{4}
\]
Indeed \(e\) has \([L:K]\) distinct conjugates, and hence generates
the separable extension. If \(L=K\), take \(e=0\).
The final field equality follows because the field on the right
contains \(t/s, b/s,e\), while all four generators already lie in \(L\).

By (3), select complex polynomials \(p_s,p_t,p_b,p_e\) in three
independent source variables \(\boldsymbol\xi\), representing
\(s,t,b,e\), respectively. Write
\(\widehat p_i=p_i(U,V,\Omega(U,V))\).

## 3. The four equations define the whole generic line

The exact statement is
\[
\boxed{\quad
(\widehat p_s-s,\widehat p_t-t,
 \widehat p_b-b,\widehat p_e-e)=(g)
 \quad\text{in }L[U,V].\quad}
\tag{5}
\]
Here is a direct graph proof, with no independence assumption on the
four coefficient generators. Put
\(R_0=\mathbb C[y,z,w_0]\) and
\(S_c=\mathbb C[s,t,b,e]\subset R_0\). Its fraction field is \(L\).
Then
\[
\begin{gathered}
S_c[\boldsymbol\xi]/(p_i(\boldsymbol\xi)-i:i=s,t,b,e)
 \simeq R_0,\\
L[\boldsymbol\xi]/(p_i(\boldsymbol\xi)-i:i=s,t,b,e)
 \simeq L[y,z,w_0]=L[v].
\end{gathered}
\tag{6}
\]
For the first line, the map from \(\mathbb C[\boldsymbol\xi]\)
to the displayed quotient is surjective: the equations express each
generator of \(S_c\) as a source polynomial. Composing with actual
evaluation gives the isomorphism
\(\mathbb C[\boldsymbol\xi]\to R_0\). The surjection is therefore
also injective. This accounts for all relations in \(S_c\).
Localizing at its nonzero elements proves the second line.

The polynomial \(\xi_3-\Omega(\xi_1,\xi_2)\) belongs to the exact
kernel in the second line of (6). Adding it changes no ideal. Eliminate
\(\xi_3\); the resulting quotient is the specified evaluation
\(L[U,V]\to L[v]\). Its kernel is \((g)\), proving (5).
This is a full ideal equality, not only a statement about factors or
radicals. Unlike a general rational-source presentation142, its generic
fiber needs no punctures or saturation.[^2]

Since the actual first tail \(\Phi\ne0\) belongs to \((g)\), (5)
also gives the exact criterion
\[
\Phi\in L^*g
\quad\Longleftrightarrow\quad
\Phi\mid\widehat p_s-s,\ \widehat p_t-t,
                  \widehat p_b-b,\ \widehat p_e-e.
\tag{7}
\]
For the converse, these divisibilities put \((g)\subset(\Phi)\).
Together with \(\Phi\in(g)\), this forces association. No implication
from \(\Phi=0\) to the four identities has been added.

## 4. Comparison with the normalized rational source equations

The normalized coefficients can use the particular common denominator
\(q=p_s\), not an arbitrary complex source denominator:
\[
\begin{gathered}
\tau=\frac{p_t(y,z,w_0)}{p_s(y,z,w_0)},\qquad
\rho=\frac{p_b(y,z,w_0)}{p_s(y,z,w_0)},\qquad
e=\frac{p_e(y,z,w_0)p_s(y,z,w_0)}{p_s(y,z,w_0)},\\
\Delta=\widehat p_s,\qquad
A_\tau=\widehat p_t-\tau\widehat p_s,\quad
A_\rho=\widehat p_b-\rho\widehat p_s,\quad
A_e=\widehat p_s(\widehat p_e-e),\\
(A_\tau,A_\rho,A_e,\widehat p_s-s)=(g),
\qquad q(y,z,w_0)=s\in L^*.
\end{gathered}
\tag{8}
\]
Modulo \(\widehat p_s-s\), the denominator is the nonzero
coefficient-field scalar \(s\). Thus (8) and (5) generate the same
ideal. In the rational formulation, this particular denominator has
no zeros on the actual generic line.

One may instead multiply all normalized numerators and their
denominator by \(p_s^{M-1}\), for \(M\ge1\). Adding
\(\widehat p_s-s\) still makes the denominator \(\widehat p_s^M\)
a unit, so the same four-equation ideal results. The boundary choice
\(M=0\) means an independently polynomial normalized presentation,
not a formula with a negative exponent. In particular, when
\(s\in\mathbb C^*\), the functions \(\tau,\rho,e\) have polynomial
source representatives, and their three equations alone define \((g)\)
by the graph argument. No speed-return equation is then needed.

## 5. Remaining obstruction and scope

An extra irreducible first-tail factor cannot satisfy all four
polynomial source-return identities in (5). This has no denominator
exception, whether that factor is active or inactive. It identifies
the precise remaining compatibility obstruction, not its impossibility.

The formal inverse-branch family141 does not supply that implication.
For example its source ratio \(\rho=w_0/F'(z)\) is not a polynomial
of \(y,z,w_0\) when \(\deg F>1\), so it cannot be a constant-first-speed
actual source model.[^3] This is an explicit boundary of the polynomial
projection argument, not an actual extra-factor counterexample.

No claim is made that the chosen four source polynomials have uniformly
bounded degree, that their divisibility by \(\Phi\) is automatic, or
that this gives a global coordinate of \(A\). Arbitrary coordinate
entry and cancellation remain outside the result.

## Sources

1. [A dense all-degree chart and its formal Taylor peeling139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--3 and 6. Actual slice projection, projected polynomial
   localization, coefficient field and whole generic line.
2. [The actual generic fiber gives the full compatibility saturation142](source-generic-fiber-saturation-pass142-working.md),
   Sections 2--4. The graph argument with rational source expressions;
   here actual polynomial invariant representatives remove that denominator.
3. [Formal tail factors and inverse branches in every degree141](formal-tail-inverse-branch-family-pass141-working.md),
   Sections 2 and 5. Its rational projected source ratio and nonunit
   original Jacobian are incompatible with the stronger actual interpretation.

The arguments above use the exact actual chart inputs and elementary
field and ring deductions. No new classification theorem or historical
novelty assertion is made.

[^1]: Source 1. The actual coordinate frame is essential for (2)--(3).
[^2]: Source 2. The present source ring is unlocalized and contains all
    four polynomial coefficient generators.
[^3]: Source 3. No actual extra first-tail factor is supplied by that family.
