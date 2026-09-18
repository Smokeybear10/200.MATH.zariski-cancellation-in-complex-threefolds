# A generic invariant coordinate and the remaining zero-speed fibers

Working result: after the actual descent319, the common invariant
\(\alpha\in A\) is a coordinate of
\(\mathbb C(X)[Y,Z,W]\). Moreover every fiber
\(A/(\alpha-\lambda)\) for which \(a(\lambda)\ne0\) is an actual
complex polynomial two-ring.

The proof constructs two commuting derivations on the original
four-ring that fix X, and only then invokes the three-variable
commuting-derivations theorem over \(\mathbb C(X)\). It does not
apply that theorem to three derivations on a four-variable ring.
Nor does it descend the generic coordinate to a coordinate of the
original \(\mathbb C[X]\)-algebra.

## 1. Exact retained hypotheses and scope

Retain the complete actual conic inputs and conclusions of the fully
read [318](principal-paraboloid-conic-original-slice-speed-pass318-working.md)
and [319](principal-paraboloid-conic-curve-intersection-rank-two-descent-pass319-working.md).
The constant-speed case is already recognized by319, so assume the
original speed a is nonconstant. The specific consequences used here
are
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
K=\operatorname{Frac}A,\qquad EX=a\ne0,\quad Ea=0,\\
T=A\cap\mathcal F=\mathbb C[\alpha],\qquad
\mathcal F=\mathbb C(\alpha),\qquad
a=a_0(\alpha)\in T\setminus\mathbb C,\\
K=\mathcal F(s,\sigma),\qquad
N=\rho\,\partial_\sigma,\qquad D_2=b\,\partial_s
            \quad\hbox{on }\mathcal F[s,\sigma],\\
0\ne N,D_2\in\operatorname{LND}_{\mathbb C}(A),\qquad
[N,D_2]=0,\qquad
\rho\in\mathcal F^*,\quad b\in T\setminus\{0\}.
\end{gathered}
\tag{1}
\]
Here N and \(D_2\) are actual derivations on A, not merely the
displayed generic vector fields. Both kill T and a. The pair is
independent over K, its common invariant field is \(\mathcal F\),
and \(\alpha-\lambda\) is prime in A for every
\(\lambda\in\mathbb C\). All these are the proved319 inputs.

The original conic hypotheses, initial kernel, and profile1222 are
retained through those inputs. The argument below does not use a
new theorem about the auxiliary time profile \((2,2,3)\).
The finite-field and invariant-denominator descent preceding (1)
has not been replaced by a generic-coordinate assumption.

## 2. Two original commuting LNDs fixing the actual coordinate X

Write \(D_1=N\). Extend \(D_1,D_2\) from A to the original
\(\mathcal B=A[u]\) by \(D_i u=0\). These extensions remain
commuting LNDs and commute with E. Define the actual polynomial
derivations
\[
\mathscr P_i=aD_i-(D_iX)E,\qquad i=1,2 .
\tag{2}
\]
Their coefficients belong to \(\mathcal B\).
Since \(D_i a=0\),
\[
E(D_iX)=D_i(EX)=0,\qquad
\mathscr P_iX=0,\qquad [E,\mathscr P_i]=0 .
\tag{3}
\]

The following localization proves local nilpotence and mutual
commutation without any division in the original ring.
Put \(c_X=X-au\in A\). Since a is a nonzero common invariant,
\[
\mathcal B_a=A_a[X].
\tag{4}
\]
Indeed \(u=(X-c_X)/a\), and X is transcendental over K.
On (4), \(\mathscr P_i\) fixes X and restricts to \(aD_i\) on
\(A_a\). This restriction is locally nilpotent because
\((aD_i)^j=a^jD_i^j\). Thus \(\mathscr P_i\) is locally nilpotent
on (4), and hence on its preserved original subring \(\mathcal B\).
The restrictions \(aD_1,aD_2\) commute because \(D_1,D_2\) commute
and both kill a. Since both fields also kill X, this proves
\[
[\mathscr P_1,\mathscr P_2]=0
\quad\hbox{on }\mathcal B.
\tag{5}
\]

Their fraction-field actions make the independence explicit:
\[
\begin{array}{c|ccc}
 &X&s&\sigma\\ \hline
\mathscr P_1&0&0&a\rho\\
\mathscr P_2&0&ab&0 .
\end{array}
\tag{6}
\]
The three displayed nonzero factors \(a,\rho,b\) belong to
\(\mathcal F^*\). Consequently the pair is independent over
\(\operatorname{Frac}\mathcal B\), and its common invariant field is
\[
\bigl(\operatorname{Frac}\mathcal B\bigr)^{\mathscr P_1,\mathscr P_2}
       =\mathcal F(X).
\tag{7}
\]
This also shows that the two kernels remain distinct under the
localization in the next section.

## 3. The precise arbitrary-field three-variable theorem

Set
\[
k=\mathbb C(X),\qquad R=k[Y,Z,W].
\tag{8}
\]
Because the actual \(\mathscr P_i\) kill X, they extend as
commuting nonzero k-LNDs to R. Their kernels are distinct by (6).
No algebraic closedness of k is asserted.

Proposition2.14 in Dasgupta and Gaifullin,
[*On locally nilpotent derivations of polynomial algebra in three
variables*](https://arxiv.org/pdf/2306.00510v2), states the needed
result for a field k of characteristic zero: two nonzero commuting
LNDs of \(k^{[3]}\) with distinct kernels have common kernel
\(k[f]\), where f is a variable of \(k^{[3]}\). The paper explicitly
distinguishes this arbitrary-field statement from Maubach's earlier
\(k=\mathbb C\) case and attributes the extension to Daigle and
Kaliman. Its field convention and exact proposition were freshly read.
Applying that precise statement gives
\[
R^{\mathscr P_1,\mathscr P_2}=k[f],
\qquad f\text{ is a coordinate of }R .
\tag{9}
\]
Neither irreducibility of the two LNDs nor a degree bound is required
by this proposition.

For clarity, the fraction field of (9) is the common invariant
fraction field in (7). This equality can be checked directly in the
UFD R. If a reduced fraction \(p/q\in\operatorname{Frac}R\) is
killed by either LND, then
\(qD(p)=pD(q)\). Coprimality makes \(p\mid D(p)\) and
\(q\mid D(q)\). The LND degree rule implies \(D(p)=D(q)=0\):
a nonzero derivative has smaller D-degree, whereas a nonzero
multiple cannot. Apply this to both derivations. Thus
\[
k(f)=\mathcal F(X)=k(\alpha).
\tag{10}
\]

The original element \(\alpha\in A\subset R\) is killed by both
\(\mathscr P_i\), so \(\alpha=G(f)\) for some nonconstant
\(G\in k[T]\). For a transcendental f,
\[
[k(f):k(G(f))]=\deg G .
\]
Equation (10) makes this degree one. Therefore
\[
\alpha=\lambda_1(X)f+\lambda_0(X),\qquad
\lambda_1(X)\in k^*,\ \lambda_0(X)\in k,
\quad\text{and}\quad
R=k[\alpha]^{[2]} .
\tag{11}
\]
In particular \(\alpha\), not just an unspecified rational
generator of its field, is a coordinate over k.
The primitive form of \(\mathscr P_1|_R\) has the same kernel,
so it has rank at most two over k. This is a generic-field rank
statement, not a relative \(\mathbb C[X]\)-coordinate conclusion.

## 4. Descent of a polynomial ring from a pure transcendental extension

We record the elementary specialization fact needed for the fibers.
Let C be a finitely generated complex algebra and let T be an
independent variable. If
\[
C\otimes_{\mathbb C}\mathbb C(T)
       \simeq_{\mathbb C(T)}\mathbb C(T)^{[n]},
\tag{12}
\]
then \(C\simeq_{\mathbb C}\mathbb C^{[n]}\).

Indeed choose finite generators and a finite presentation of C.
The isomorphism and its inverse use finitely many rational functions
of T as coefficients. Their defining relations and the two inverse
identities therefore hold after inverting one nonzero polynomial
\(q(T)\in\mathbb C[T]\). This gives an isomorphism over
\(\mathbb C[T,q(T)^{-1}]\). Choose a complex value \(T_0\) with
\(q(T_0)\ne0\), and tensor this isomorphism by \(T\mapsto T_0\).
Its two inverse maps specialize simultaneously and give the stated
complex polynomial-ring isomorphism.

This argument specializes a separately independent scalar variable.
It does not evaluate a possibly singular original coordinate fiber,
and it does not assert that arbitrary algebraic field forms are
trivial.

## 5. The original slice locates every genuinely bad fiber

Fix \(\lambda\in\mathbb C\) and put
\[
A_\lambda=A/(\alpha-\lambda),\qquad
\mathcal B_\lambda=\mathcal B/(\alpha-\lambda)
                   =A_\lambda[u].
\tag{13}
\]
These are domains because the fiber element is prime in A.
The original derivation descends as \(\partial_u\), and
the original speed specializes to the complex constant
\(a_0(\lambda)\).

Assume \(a_0(\lambda)\ne0\). Reducing
\(X=au+c_X\) modulo the fiber gives
\[
X=a_0(\lambda)u+\overline c_X,\qquad
\mathcal B_\lambda=A_\lambda[X].
\tag{14}
\]
Thus X really is an independent variable over \(A_\lambda\).
This is where nonzero original speed is essential.

On the other hand, localization at the nonzero polynomials in X
commutes with the quotient by \(\alpha-\lambda\), and (11) gives
\[
\mathbb C(X)\otimes_{\mathbb C[X]}\mathcal B_\lambda
       \simeq\mathbb C(X)^{[2]} .
\tag{15}
\]
Combining (14),(15), with the indicated independent X, yields
\[
A_\lambda\otimes_{\mathbb C}\mathbb C(X)
       \simeq\mathbb C(X)^{[2]} .
\tag{16}
\]
The finite-generation hypothesis in Section4 holds because
\(A_\lambda\) is a quotient of the finitely generated ring A.
Specialization of the finite isomorphism coefficients therefore proves
\[
\boxed{a_0(\lambda)\ne0\quad\Longrightarrow\quad
             A/(\alpha-\lambda)\simeq\mathbb C^{[2]}.}
\tag{17}
\]
Consequently the genuinely non-polynomial fibers, if any, are
contained in the finite set of zeros of \(a_0\).

## 6. Exact remaining boundary

At a zero of \(a_0\), equation (14) no longer follows: the original
X can lie in \(A_\lambda\), rather than supply its polynomial
slice variable. Thus (15) does not give (16) at those values.
They have not been removed.

Also, dependent fibers of a chosen commuting pair need not coincide
with non-polynomial fibers. In particular the denominator used to
construct \(D_2\) can produce additional dependent fibers even when
the quotient is a polynomial ring. Equation (17) concerns actual
fiber rings, not the independence of that chosen pair on every
fiber.

The coordinate in (11) is over \(\mathbb C(X)\). Its companion
coordinates can have denominators in X. No claim that they extend
to \(\mathbb C[X]\), or that \(\alpha\) is an original coordinate,
has been made. The zero-speed fibers remain an original-ring
obligation, so the note does not recognize the whole conic sector.

The complete318 and319 sources were independently read, and their
actual derivations and intersection hypotheses were reconstructed,
before this argument. The exact arbitrary-field Proposition2.14
was checked in its primary research source. No saved checker was
executed, imported, compiled or rerun, and no older proof, checker,
index or packet was edited. There is no claim of unrestricted
cancellation, novelty or formal verification.
