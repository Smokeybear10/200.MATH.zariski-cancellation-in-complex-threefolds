# Integrability when the common-local-slice factor vanishes

## 1. Exact remaining-branch criterion

The branch \(p(0)=0\) in
[the degree-one integrability criterion](q1-integrability-pass36.md)
has a finite necessary-and-sufficient test. It is nonempty at every
positive vanishing order. Every primitive top in this branch is
nonsliced, so this classification does not provide a sliced-top
selection rule.

Use the same fixed model and conventions:
\[
R=\mathbb C[x,\lambda,b,c],\quad
h=x^2c-b^2,\quad F=p(x)b+Q(x,h),\quad
L=J_F=F_c\partial_b-F_b\partial_c,
\]
\[
g\in\mathbb C[x,T]\setminus\{0\},\quad
G(x,T)=\int_0^Tg(x,s)\,ds,\quad
K=h+\lambda G(x,F),\quad v=1+\lambda x,
\]
\[
\mathcal D=D_0+\lambda g(x,F)L=J_K,\qquad
D_0=x^2\partial_b+2b\partial_c.                                    \tag{1}
\]
Assume \(L\) is primitive and
\[
p=x^eu,\qquad e\ge1,\qquad u(0)\ne0.
\]
Here \(p\) is the factor in \(\mathcal DF=x^2p\). It is not
being identified with the full plinth generator of \(L\).

An actual canonical realization is a polynomial isomorphism fixing
\(x,\lambda\), normalized to \(w=b,z=c\) at \(\lambda=0\), carrying
\[
\Delta=x^2\partial_w+2(1+\lambda x)^2w\partial_z
\]
to \(\mathcal D\). A polynomial inverse is part of the requirement.

Write
\[
Q_0(T)=Q(0,T),\qquad
g(x,T)=g_0(T)+xg_1(T)+O(x^2).
\]
Let \(\operatorname{rad}(p)\) mean the product of distinct irreducible
factors, up to a nonzero scalar.

**Theorem.** Under the hypotheses above, an actual canonical
realization exists if and only if
\[
\boxed{
\begin{gathered}
\operatorname{rad}(p)\mid g(x,T)\quad\hbox{coefficientwise},\\
Q_0(T)=q_0+q_1T,\qquad q_1\ne0,\\
g_1(T)=\frac{2}{3q_1}.
\end{gathered}}                                                     \tag{2}
\]
There is no bound or further restriction on the higher \(x\)-jets
of \(Q,g\), other than the stated hypotheses and radical divisibility.

Every actual normalized realization in this branch satisfies
\[
W\equiv b-\frac23\lambda xb\pmod{x^2}.                              \tag{3}
\]
The construction below uses only finite nilpotent inversion modulo
\(x^{e+2}\) and \(u\), followed by the Chinese remainder theorem.

## 2. Exact criterion used and the zeroth-order obstruction

Theorem 1 of the previous note identifies actual realizability with
the existence of \(U\in\mathbb C[x,\lambda,T]\) such that
\[
N=F-Q(x,K)+\lambda U(x,\lambda,K)\in pR,\qquad W=N/p,
\]
\[
K+v^2W^2\in\mathbb C[x,\lambda]+x^2R.                              \tag{4}
\]
That theorem supplies an actual global polynomial inverse from
these congruences. It does not infer coordinates from a Jacobian
determinant alone.

Primitivity makes \(Q_0\) nonconstant. Otherwise \(F\bmod x\)
would be constant, so both coefficients of \(J_F\) would be
divisible by \(x\).

The coordinate boundary calculation in the previous note gives
\(\overline W=b+\alpha\lambda\), with \(\alpha\in\mathbb C\).
Reducing the second congruence in (4) modulo \(x\) gives
\[
\lambda G_0(Q_0(-b^2))+2\alpha\lambda b+\alpha^2\lambda^2
\in\mathbb C[\lambda].                                             \tag{5}
\]
Its odd part forces \(\alpha=0\). Since \(Q_0\) is nonconstant,
its even part forces \(G_0\) to be constant. The normalization
\(G_0(0)=0\) then gives
\[
g_0=0,\qquad G_0=0,\qquad \overline W=b.                            \tag{6}
\]
In particular \(x\mid g\). At each nonzero root of \(p\), the
uniform coefficient-ideal obstruction in Section 3 of the previous
note forces that root factor to divide \(g\). Together these give
the first condition of (2).

## 3. The overlapping-divisor correction and its first jet

Put \(n=e+2\) and work first modulo \(x^n\). The polynomial
\[
\phi(T)=T+\lambda G(x,Q(x,T))
\]
is the identity modulo the nilpotent ideal \((x)\), by (6).
It has a finite polynomial inverse \(\psi\) in
\[
(\mathbb C[x]/(x^n))[\lambda,T].
\]
Explicitly, writing \(E(T)=\phi(T)-T\), the iteration
\[
\psi_0=T,\qquad \psi_{j+1}=T-E(\psi_j)
\]
stabilizes modulo \(x^n\): successive differences acquire one
additional factor of \(x\). The same argument gives uniqueness
and both inverse compositions.

Choose any polynomial lift of \(\psi\), normalized to
\(\psi|_{\lambda=0}=T\), and set
\[
U_*=\frac{Q(x,T)-Q(x,\psi(T))}{\lambda}.                            \tag{7}
\]
The division is polynomial. Since \(F=Q(x,h)\bmod x^e\) and
\(K=\phi(h)\bmod x^e\), its associated numerator
\[
N_*=F-Q(x,\psi(K))
\]
is divisible by \(x^e\). This conclusion is independent of the
chosen lift. Temporarily let \(W_*=N_*/p\); it is regular at
\(x=0\), since \(u(0)\ne0\). Its possible denominators at roots
of \(u\) will be removed in Section 5.

Here is the normal-displacement calculation with the full error
order. Since \(G\) and all its \(T\)-derivatives are divisible by
\(x\),
\[
K=\phi(h)+\lambda p b\,g(x,Q(x,h))
                 \pmod{x^{e+2}}.                                 \tag{8}
\]
Indeed the next Taylor term has order at least \(2e+1\), which
is at least \(e+2\), including equality when \(e=1\).
Also \(\psi'(T)\equiv1\bmod x\). Applying \(\psi\) to (8) gives
\[
\psi(K)\equiv h+\lambda p b\,g(x,Q(x,h))
                 \pmod{x^{e+2}}.
\]
The correction has order at least \(e+1\), so its square has
order at least \(2e+2\). A further Taylor expansion of \(Q\),
followed by division by \(p=x^eu\), yields
\[
W_*\equiv b-x\lambda b\,Q_0'(-b^2)g_1(Q_0(-b^2))
                 \pmod{x^2}.                                     \tag{9}
\]
No normal term of order one was discarded at \(e=1\).

To compare this with an arbitrary \(U\) satisfying (4), note that
\(\lambda(U-U_*)(K)\) is divisible by \(x^e\). Substitution
\(T\mapsto K\bmod x=-b^2\) is injective on
\(\mathbb C[\lambda,T]\). Extracting a lowest nonzero \(x\)-term
therefore proves \(U-U_*=x^eV\) with polynomial \(V\).
Both \(W\) and \(W_*\) reduce to \(b\), so the same injection
forces \(x\mid V\). Consequently
\[
W\equiv W_*+x\lambda J(\lambda,-b^2)\pmod{x^2}                       \tag{10}
\]
for a polynomial \(J\). The scalar \(u(0)^{-1}\) is absorbed
in \(J\). This accounts for every correction at this order.

## 4. An all-degree parity equation

Let
\[
H(T)=G_1(Q_0(T)),\qquad G_1'=g_1,\quad G_1(0)=0.
\]
The order-\(x\) coefficient of \(K\) is
\(\lambda H(-b^2)\). Combining (9)--(10) with \(v^2\) gives
\[
K+v^2W^2\equiv
x\lambda\left(
 H(T)+2T H'(T)-2T+2bJ(\lambda,-b^2)
\right)\pmod{x^2},\qquad T=-b^2.                                  \tag{11}
\]
The polynomial \(x^2c\) has disappeared only because this is
a congruence modulo \(x^2\).

The last term is odd in \(b\); all preceding terms are even.
The second congruence in (4) therefore implies
\[
H(T)+2T H'(T)-2T\in\mathbb C.                                      \tag{12}
\]
For \(H=\sum_jh_jT^j\), the coefficient multiplier is \(2j+1\).
Characteristic zero gives the exact solution
\[
H(T)=h_0+\frac23T.                                                 \tag{13}
\]
In particular \(H\) is nonconstant. Composition degrees in
\(H=G_1\circ Q_0\) force both \(G_1,Q_0\) to be linear.
Thus \(Q_0=q_0+q_1T\), \(q_1\ne0\), and
\(g_1=2/(3q_1)\), proving necessity of all of (2).

The odd part of (11) also forces \(J=0\). Since
\(Q_0'g_1(Q_0)=2/3\), equation (9) becomes (3).
Thus the first-jet statement holds for every realization, not
only for the construction in Section 5.

## 5. Finite global construction

Assume (2). At the marked divisor use the class \(U_*\) of
(7) modulo \(x^{e+2}\). The computations above give
\[
N_*\in(x^e),\qquad
W_*\equiv b-\frac23\lambda xb\pmod{x^2},
\]
\[
K+v^2W_*^2\equiv
\frac{2q_0}{3q_1}\lambda x\pmod{x^2}.                              \tag{14}
\]
The last residue is independent of \(b,c\), as required.

If \(u\) is nonconstant, work separately in
\[
A=\mathbb C[x]/(u).
\]
The radical-divisibility condition makes \(G\) coefficientwise
nilpotent in \(A\). The same finite inverse construction gives
\(\psi_u\) for \(T\mapsto T+\lambda G(x,Q(x,T))\), and
\[
U_u=\frac{Q(x,T)-Q(x,\psi_u(T))}{\lambda}
\quad\hbox{in }A[\lambda,T].                                      \tag{15}
\]
It makes the numerator in (4) zero modulo \(u\). Repeated
roots are retained in the quotient \(A\); they are not
replaced by reduced-point conditions.

Because \((x^{e+2})\) and \((u)\) are comaximal, combine
(7) and (15) by the Chinese remainder theorem. If \(u\)
is constant, use (7) alone. The resulting polynomial
\(U\) has \(N\) divisible by both \(x^e\) and \(u\), hence
by \(p\). Its quotient \(W=N/p\) is polynomial everywhere
and retains the residue in (14). Thus (4) holds.

Taking, for example, the representative constant correction
\[
C=-\frac{2q_0}{3q_1}\lambda x
\]
makes
\[
Z=(K+C+v^2W^2)/x^2
\]
polynomial and normalized at \(\lambda=0\). The global inverse
argument of Theorem 1 in the previous note applies. This
finishes sufficiency without an infinite formal series or
a Jacobian-one sufficiency assumption.

## 6. Explicit nonemptiness at every vanishing order

For every integer \(e\ge1\), take
\[
p=x^e,\qquad Q=T,\qquad g=\frac23x.
\]
Then \(L=x^2\partial_b+(2b-x^e)\partial_c\) is primitive,
and (2) holds. There is a short closed-form actual inverse.

Put
\[
t=\frac23\lambda x,\quad n=e+2,\quad
A_n=\sum_{j=0}^{n-1}(-t)^j,\quad
B_n=1-tA_n,\quad C_n=\frac{(-t)^n}{x^e}.
\]
The last expression is polynomial and divisible by \(x^2\).
Define
\[
W=B_nb+C_nh,\qquad
K=tx^eb+(1+t)h,\qquad
Z=(K+v^2W^2)/x^2.                                                 \tag{16}
\]
The numerator of \(Z\) is divisible by \(x^2\) by (14)
with \(q_0=0\). In independent coordinates \(b,h\), the matrix
\[
\begin{pmatrix}B_n&C_n\\tx^e&1+t\end{pmatrix}
\]
has determinant one, since
\((1+t)A_n=1-(-t)^n\). This is an actual linear-coordinate
identity over \(\mathbb C[x,\lambda]\).

For target coordinates \(w,z\), put
\(I=x^2z-v^2w^2\). The inverse is
\[
b=(1+t)w-C_nI,\qquad
h=-tx^ew+B_nI,\qquad
c=(h+b^2)/x^2.                                                    \tag{17}
\]
Modulo \(x^2\), the first expression is \((1+t)w\), while
the second is \(-(1-t)v^2w^2\). Their combination in (17)
is divisible by \(x^2\), since \(3t=2\lambda x\).
Thus (17) is polynomial. The determinant identity recovers
\(b,h\) in both directions, and \(x^2c=h+b^2\) recovers
\(c\), with cancellation valid in the polynomial domain.
Equations (16)--(17) are complete global inverses.

More generally every prescribed \(p=x^eu\), \(u(0)\ne0\),
occurs for some data satisfying (2): take \(Q=T\) and
\[
g=\frac23x\,\frac{\operatorname{rad}(u)(x)}
                       {\operatorname{rad}(u)(0)},
\]
with \(\operatorname{rad}(u)=1\) for constant \(u\).
The primitive derivation has coefficients \(x^2\) and
\(2b-p(x)\), whose gcd is one. Section 5 gives the actual
inverse in this arbitrary-\(u\) case.

## 7. Primitive-top and transfer boundaries

In every case of (2),
\[
L\bmod x=2q_1b\,\partial_c.
\]
Therefore \(L\) vanishes on the line \(x=b=0\). Evaluation
at any point of that line annihilates every \(L(f)\), so
\(L\) cannot have a polynomial slice. Also \(g\) has exact
\(x\)-order one, because \(g_1\ne0\). In the prescribed
coordinates,
\[
D_1=g(x,F)L\equiv\frac43xb\,\partial_c\pmod{x^2}.
\]
Its nonzero value as a derivation ensures that the resulting
canonical realization has relative degree exactly one.

Together with the \(p(0)\ne0\) constructive criterion in
pass 36, this decides realizability for all primitive
polynomial normal-form data of pass 35. It does not show
that every realization admits a degree-one repair path
to a sliced top.

The actual coordinates \(x,\lambda,b,c\) and the known
relative polynomial plane are indispensable hypotheses.
They do not follow from an unspecified
\(A[s]\simeq\mathbb C^{[4]}\) with polynomiality of \(A\)
unknown. Nothing here proves general threefold cancellation,
classifies arbitrary sliced actions, or transfers the finite
construction to a nonpolynomial unknown quotient.

## Dependencies and verification boundary

The only recognition input beyond the explicit congruence
algebra is Theorem 1 and the off-boundary coefficient-ideal
argument of
[q1-integrability-pass36.md](q1-integrability-pass36.md).
The polynomial normal-form scope and its primary planar
references are recorded in
[general-q1-repair-pass35.md](general-q1-repair-pass35.md).

The separate
[bounded exact checker](vanishing_plinth_integrability_checks_pass38.py)
has eight methods and imports only unittest and SymPy.
It controls the normal-displacement calculation at \(e=1,2\),
the repeated-root CRT correction for \(p=x^2(x-1)^2\),
both physical inverse divisibilities for \(1\le e\le5\),
actual action identities, parity obstructions, and primitive-top
fixed points. The first run passed all eight methods in
3.605 seconds, with no mathematical or assertion corrections.

An independent full-proof reconstruction found no correction,
including the \(e=1\) remainder, comparison with every \(U\),
and the predecessor theorem's global inverse. Finite computations
do not replace the all-degree and all-multiplicity arguments above.
No novelty, expert-review, or Lean-verification claim is made.
