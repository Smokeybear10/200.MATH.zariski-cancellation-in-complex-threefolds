# A weighted plane obstruction for nonlinear time coupling

Working result: in the supplied full actual chart264, assume
\(k=s+f(t)\), \(n_s=0\), \(f'''\ne0\), and \(\ell_s\ne0\).
Then necessarily \(\ell_{ss}=0\).

The proof eliminates the third formal variable using the third
potential, and uses the genuine fourth potential. If
\(\ell_{ss}\ne0\), its weighted leading form is a nonzero square of
the irreducible cusp polynomial \(U^2+(f'''/6)P^3\).
Every irreducible relation of the actual polynomial line would then
force one of the degree pairs \((3,2),(6,4)\), contrary to the
Abhyankar--Moh--Suzuki degree-divisibility theorem.

This is an exclusion of a coefficient subcase in an already supplied
actual chart. It is neither an ambient-coordinate construction nor
an arbitrary-entry or unrestricted cancellation theorem.

## 1. Retained actual hypotheses

Retain the complete actual entry of
[264](principal-one-affine-paraboloid-chart-pass264-working.md)
and the corrected fourth potential of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md).
The complete specialized primitive and graph are also recorded in
the fully read
[430](principal-paraboloid-arbitrary-longitudinal-plane-reduction-pass430-working.md);
they are displayed directly below so that the exclusion's inputs
are explicit.
In particular,
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad
E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\qquad a_0=EX\ne0,\\
I_{\mathrm{initial}}=(X^2Z-Y^2)
\quad\text{is the full weighted initial kernel}.
\end{gathered}
\tag{1}
\]
The literal \(Z\)-partial has exact intrinsic shift four, and its
selected nonzero locally nilpotent derivation \(N\) on \(A\) gives
\[
\begin{gathered}
L=\operatorname{Frac}\ker_A N,\qquad
[L:\mathbb C(t,s)]<\infty,\qquad
O=A\otimes_{\ker_A N}L=L[v],\qquad Nv=1,\\
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\qquad
L[y,z,w]=O .
\end{gathered}
\tag{2}
\]
Here \(t,s\) are algebraically independent. Their coefficient
partials extend uniquely to \(L\), commute, and fix the original
intrinsic variable \(v\). No identification \(L=\mathbb C(t,s)\)
is made.

The literal actual rows and their calibration are
\[
\begin{aligned}
Y&=y+\sigma X+tX^2,\\
Z&=z+(2t\sigma+k)X+t^2X^2,\\
W&=w+\theta X+sX^2,\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}
&=-a_0^4\in L^* .
\end{aligned}
\tag{3}
\]
Assume throughout this note that
\[
k=s+f,\qquad f_s=0,\qquad n_s=0,\qquad
f'''=\partial_t^3f\ne0,\qquad \varepsilon=\ell_s\ne0 .
\tag{4}
\]
Primes on \(f,n\) denote coefficient differentiation in \(t\).
They are elements of the exact field \(\ker_L\partial_s\), not
necessarily rational functions in \(t\). Since \(k_s=1\), this
is a nonzero-coupling subcase.

The first two potentials specialize to
\[
\begin{aligned}
z&=2ty+\sigma^2+f'\sigma+\theta+n,\\
w&=\ell-(2\sigma+f')y-\frac{f''}{2}\sigma^2-n'\sigma .
\end{aligned}
\tag{5}
\]
Consequently \(L[y,\sigma,\theta]=O\), with the whole polynomial
ring equality inherited from (2), not just equality of fraction
fields.

## 2. Elimination and the complete fourth potential

Use independent formal variables \(U,P,V\). The third potential is
\[
H=U^2+(f''P+n')U+\frac{f'''}6P^3+\frac{n''}2P^2
       -\ell_tP-\varepsilon V,\qquad
H(y,\sigma,\theta)=h,\quad h\in L .
\tag{6}
\]
Put
\[
S(U,P)=U^2+(f''P+n')U+\frac{f'''}6P^3+
       \frac{n''}2P^2-\ell_tP-h .
\]
Since \(\varepsilon\in L^*\), (6) gives the polynomial elimination
and exact plane return
\[
\theta=\frac{S(y,\sigma)}{\varepsilon},\qquad
L[y,\sigma]=L[y,\sigma,\theta]=L[v].
\tag{7}
\]
This division is only in the coefficient field. It is not an
assertion that \(\varepsilon^{-1}\) is in the original ambient ring.

For clarity, the genuine fourth potential used below can be written
in full:
\[
\begin{aligned}
Q={}&\frac{f''}{2}U^2+
 \left\{\frac{f'''}2P^2+(n''+2\varepsilon)P+
                   f'\varepsilon-\ell_t\right\}U\\
&+\frac{f''''}{24}P^4+\frac{n'''}6P^3
 +\frac{f''\varepsilon-\ell_{tt}}2P^2
 +(n'\varepsilon-h_t)P\\
&-\ell_{ts}PV-\frac{\ell_{ss}}2V^2-h_sV .
\end{aligned}
\tag{8}
\]
An additive element of \(L\) is immaterial. In this specialization
the formal \(\lambda=F_V/k_s\) of296 is zero, while
\(D=2P+f'\) and \(\beta=2U+f''P+n'\). Direct differentiation gives
precisely296's corrected components
\[
Q_U=H_P-(2P+f')H_V,\qquad
Q_P=H_t-h_t-(2U+f''P+n')H_V,\qquad
Q_V=H_s-h_s .
\tag{9}
\]
The coefficient derivatives in (9) hold \(U,P,V\) fixed. In
particular, the two derivatives of the actual level \(h\) in
(8),(9) have not been discarded.

The retained linear coefficient of the full scalar (3), as proved
in296, therefore gives
\[
Q(y,\sigma,\theta)=q,\qquad q\in L .
\]
Define
\[
\Phi(U,P)=Q\!\left(U,P,\frac{S(U,P)}{\varepsilon}\right).
\quad\text{Then}\quad
\Phi(y,\sigma)=q .
\tag{10}
\]
The stronger minor-unit and plane-cofactor conclusions available
from296 are not needed in this proof. Divisibility by the whole
plane equation will suffice.

## 3. The exact weighted leading form

Suppose for contradiction that \(\ell_{ss}\ne0\). Assign positive
weights
\[
\operatorname{wt}(U)=3,\qquad \operatorname{wt}(P)=2,
\qquad C(U,P)=U^2+\frac{f'''}6P^3 .
\tag{11}
\]
Coefficients in \(L\) have weight zero. The two displayed monomials
of \(C\) both have weight six. Every other term of \(S\) has weight
at most five, so \(\operatorname{in}_{\mathrm{wt}}S=C\).

In (8), all terms not involving \(V\) have weight at most eight.
The term \(PV\), after substitution, has weight at most eight,
and the term \(V\) has weight at most six. Thus the only source of
weight twelve is the substituted \(V^2\) term. It follows that
\[
\operatorname{wtdeg}(\Phi-q)=12,\qquad
\operatorname{in}_{\mathrm{wt}}(\Phi-q)
 =-\frac{\ell_{ss}}{2\varepsilon^2}
       \left(U^2+\frac{f'''}6P^3\right)^2 .
\tag{12}
\]
In particular \(\Phi-q\) is a nonzero polynomial.
The lower terms of the square in (12) can have weights up to
eleven, but cannot alter its weight-twelve form.

The polynomial \(C\) is irreducible in \(L[U,P]\). Indeed, as a
monic quadratic in \(U\), a factorization over \(L(P)\) would make
\(-f'''P^3/6\) a square in \(L(P)\). Its valuation at \(P=0\)
is three, which is odd. Gauss's lemma then proves the stated
irreducibility over \(L[P]\). No extraction of a root from \(L\)
or assumption that \(L\) is algebraically closed is involved.

## 4. The whole plane equation and its two separate degrees

By (7), evaluation defines a surjective map
\[
L[U,P]\longrightarrow L[v],\qquad (U,P)\longmapsto(y,\sigma).
\]
Its kernel is a height-one prime in the two-variable polynomial
UFD, so it is generated by an irreducible nonconstant polynomial
\(G(U,P)\). Equation (10) gives \(G\mid(\Phi-q)\).
Weighted initial forms multiply, and \(L[U,P]\) is a UFD.
Therefore (12) and the irreducibility of \(C\) imply
\[
\operatorname{in}_{\mathrm{wt}}G=c_G C^j,\qquad
c_G\in L^*,\qquad j\in\{1,2\}.
\tag{13}
\]
The exponent is not zero: positive weights make the initial form
of a nonconstant polynomial have positive weight.

Equation (13) includes nonzero terms \(U^{2j}\) and \(P^{3j}\).
Every term of \(G\) has weight at most \(6j\), which at the same
time bounds its \(U\)-degree by \(2j\) and its \(P\)-degree by
\(3j\). Thus both separate degrees are exact:
\[
\deg_U G=2j,\qquad \deg_P G=3j .
\tag{14}
\]
In particular \(y\) and \(\sigma\) are both nonconstant. If one
were constant, the entire kernel would instead be generated by
a linear polynomial in that variable, contrary to (14).

The whole return (7) gives \(L(y,\sigma)=L(v)\).
Irreducibility and Gauss's lemma identify \(G\), up to a nonzero
element of the relevant rational function field, with the minimal
polynomial of \(y\) over \(L(\sigma)\), and of \(\sigma\) over
\(L(y)\). Hence
\[
\begin{aligned}
\deg_v\sigma
 &=[L(v):L(\sigma)]=\deg_U G=2j,\\
\deg_v y
 &=[L(v):L(y)]=\deg_P G=3j .
\end{aligned}
\tag{15}
\]
The first equalities use the ordinary degree formula for a
nonconstant polynomial in one variable. They do not assert that
either \(y\) or \(\sigma\) alone generates \(L[v]\).

## 5. Degree divisibility and the precise conclusion

The characteristic-zero Abhyankar--Moh--Suzuki degree theorem says
that if \(F[p(v),q(v)]=F[v]\), one of the two positive polynomial
degrees divides the other. The primary proof by
[Makar-Limanov, *A new proof of the Abhyankar--Moh--Suzuki
Theorem*](https://arxiv.org/pdf/1212.0163v1)
states this over a field \(F\) in its opening theorem.
Its Lemma1 also supplies the function-field degree formula used
in (15). We apply the theorem with the exact characteristic-zero
field \(F=L\); no specialization or coefficient-field rationality
is required.

For \(j=1\) or \(2\), neither \(2j\) divides \(3j\) nor \(3j\)
divides \(2j\). Equations (7),(15) contradict the theorem.
The supposition \(\ell_{ss}\ne0\) was therefore impossible:
\[
\boxed{
\text{Under the full actual264 hypotheses, }\quad
k=s+f,\quad f_s=n_s=0,\quad f'''\ell_s\ne0
\quad\Longrightarrow\quad \ell_{ss}=0 .}
\tag{16}
\]

This does not prove that the remaining affine-in-\(s\) second
potential is realizable or recognized. It does not address the
\(\ell_s=0\) boundary, assert a normalization of arbitrary \(k,n\),
or replace the actual whole-line return by a rational return.
The known degree-two-projection recognition in307 is not counted
as additional coverage here.

The proof uses the complete264 and296 inputs, the matching fully
read430 reduction, and the primary degree theorem. The earlier333
and340 plane arguments were read
for comparison, but their specialized coefficient exclusions are
not transferred into this calculation. Fresh unsaved exact
calculation \(d7e43c\) rebuilt the general296 Taylor expression and
all three gradients (9), and returned zero residuals for (8),(12);
it also verified that the terms outside the substituted \(V^2\)
term have weight at most eight. The primary theorem and Lemma1
were freshly inspected in \(turn4642view0\).
The algebraic proof above, not numerical sampling, supplies the
weighted-factor and whole-ring deductions.

No saved checker was executed, imported, compiled or rerun.
No earlier source or canonical index was edited. This working
note makes no novelty or formal-certification claim.
