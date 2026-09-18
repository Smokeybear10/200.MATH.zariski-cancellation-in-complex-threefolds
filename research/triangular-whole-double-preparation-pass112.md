# Arbitrary triangular perturbations still have a hidden quadratic parameter

No member of the triangular class below has a proper residual second-image
ideal at its whole double fiber. Finite polynomial division over a nilpotent
base supplies a global quadratic element, an exact monic conic presentation,
and every degree-module basis. The perturbation can have arbitrary odd or
high-degree terms; no even-polynomial or convergent-series hypothesis is used.

This is a theorem about a specified intrinsic triangular class. It does not
put an arbitrary actual frame into that class, recognize a general threefold,
or establish novelty. In particular it does not settle the remaining proper
whole-double alternative from111.

## 1. The exact family

Let e be any positive integer and Q any polynomial in C[x,y]. Put
\[
\begin{gathered}
P(x,y)=y^2+xQ(x,y),\qquad A=\mathbb C[x,y,z],\\
f=P(x,y)+x^ez,\qquad S=\mathbb C[x,f],\qquad
N=-x^e\partial_y+P_y\partial_z
 =\det\frac{\partial(x,f,\,\cdot\,)}{\partial(x,y,z)},\\
\mathfrak m=(x,f)S,\qquad
A/\mathfrak mA=\mathbb C[y,z]/(y^2).
\end{gathered}
\tag{1}
\]
The elements x,f are algebraically independent and A_x=S_x[y], by
solving for z. The derivation kills S. If d=deg_y P, then d is at
least two; assigning weights zero, one, d to x,y,z makes N lower
weight. Hence N is locally nilpotent. Since P_y modulo x equals 2y,
the coefficients x^e and P_y have gcd one. This is the actual primitive
polynomial base Jacobian on the displayed smooth polynomial threefold.

Flatness and the full kernel will be proved below; they are not assumed
from the shape of the generic fiber.

## 2. Constructive finite preparation

Use an independent base variable T, not the element f during construction.
Start with F_1=y squared-T and V_1=1. Inductively suppose
P-T-V_k F_k is divisible by x^k, F_k is monic quadratic in y, and
F_k modulo x is y squared-T, while V_k modulo x is one. Define
\[
\begin{gathered}
D_k(T,y)=\left.\frac{P-T-V_kF_k}{x^k}\right|_{x=0},\\
D_k=q_k(T,y)(y^2-T)+r_k(T,y),\qquad \deg_y r_k<2,\\
F_{k+1}=F_k+x^kr_k,\qquad V_{k+1}=V_k+x^kq_k.
\end{gathered}
\tag{2}
\]
The division is ordinary polynomial division by the monic polynomial
y squared-T in C[T][y]. It introduces no denominator in T. Modulo
x^(k+1), the change in the product V_k F_k is exactly
x^k(q_k(y squared-T)+r_k)=x^kD_k, because k is positive.
This proves the next divisibility and preserves both residue conditions.
The remainder degree keeps F_{k+1} monic quadratic.

After the e-1 steps k=1 through e-1, all resulting expressions are
finite polynomials. In particular
\[
\begin{gathered}
F_e=y^2+A_e(x,T)y+B_e(x,T),\quad
A_e(0,T)=0,\quad B_e(0,T)=-T,\\
P-T=V_eF_e+x^eR_e,
\qquad V_e\equiv1\pmod x,
\qquad A_e,B_e,R_e,V_e\text{ are polynomial}.
\end{gathered}
\tag{3}
\]
Here R_e=(P-T-V_eF_e)/x^e is a polynomial by construction.
For e=1 no induction is needed: F_1=y squared-T, V_1=1 and
R_1=Q. There is no infinite completion in this preparation.

## 3. The divided element is a global polynomial

Evaluate T at f in A, and denote evaluation by a hat. Equation (3)
becomes -x^e z=Vhat_e Fhat_e+x^e Rhat_e. In A/(x^e), the
element Vhat_e is a unit: if Vhat_e=1+xw, its inverse there is
the finite sum of (-xw)^j for j=0 through e-1. Therefore
Fhat_e vanishes in that quotient. Consequently
\[
\begin{gathered}
U=\frac{\widehat F_e}{x^e}\in A,\qquad
z=-\widehat V_eU-\widehat R_e,\qquad A=S[y,U],\\
NU=-(2y+A_e(x,f)),\qquad N^2U=2x^e\ne0,
\qquad N^3U=0.
\end{gathered}
\tag{4}
\]
Thus the denominator in U cancels in the original polynomial ring.
No global inverse of Vhat_e is asserted or needed. The formula for z
uses multiplication by Vhat_e, not division. Differentiating x^e U
and using invariance of the coefficients proves the derivative formulas.

## 4. Exact conic, faithful flatness and the full filtration

The generation in (4) induces an exact presentation
\[
\begin{gathered}
A\simeq S[\mathsf Y,\mathsf U]/
\bigl(\mathsf Y^2+A_e(x,f)\mathsf Y+B_e(x,f)-x^e\mathsf U\bigr),\\
A=\bigoplus_{j\ge0}S U^j\ \oplus\ \bigoplus_{j\ge0}S yU^j.
\end{gathered}
\tag{5}
\]
To prove injection, the proposed source is free over S[Uscr] with
basis 1,Yscr, since the relation is monic in Yscr. It has no x-torsion.
After inverting x the presentation solves for Uscr and becomes
S_x[Yscr], mapping isomorphically to A_x=S_x[y]. Its original kernel
is x-torsion and hence zero. The displayed nonzero free S-module makes
S to A faithfully flat.

In the generic field K=Frac(S), U is quadratic in y with leading
coefficient x^(-e), while N=-x^e partial_y. The basis monomials U^j
and yU^j have respective, pairwise distinct y-degrees 2j and 2j+1.
In a finite S-linear expansion the highest nonzero coefficient therefore
cannot cancel. This proves the complete, all-polynomial filtration:
\[
\begin{gathered}
\ker(N^{n+1}|_A)
 =\bigoplus_{2j\le n}S U^j
  \ \oplus\!\bigoplus_{2j+1\le n}S yU^j,\\
\ker N=S,\qquad F_1=S\{1,y\},\qquad
F_2=S\{1,y,U\},\\
I_n=N^nF_n=x^{e\lceil n/2\rceil}S,
\qquad I_1=I_2=x^eS.
\end{gathered}
\tag{6}
\]
The formula includes n=0. For n=2j the top derivative of U^j is
(2j)! x^(ej). For n=2j+1 the top derivative of yU^j is
-(2j+1)! x^(e(j+1)). Lower-degree basis elements contribute zero.
Factorials are units over C, proving the image ideals. No bounded
coefficient search substitutes for this distinct-degree argument.

## 5. The whole residue and the exact limit of this result

Reducing the recovery formula for z first modulo x and then at the
whole fiber gives
\[
\begin{gathered}
U\bmod x=-z-R_e(0,y^2,y),\\
U\bmod\mathfrak mA=-z-r_0-r_1y
\quad\text{for some }r_0,r_1\in\mathbb C,\\
\overline{NU}=-2y\ne0,
\qquad \overline{N^2U}=0,\qquad
\boxed{\ I_2R=I_1R\text{ for }R=S_{\mathfrak m}.\ }
\end{gathered}
\tag{7}
\]
The residue of R_e(0,0,y) has only constant and linear terms modulo
y squared. Thus U has a nonconstant reduced residue, and its derivative
is a nonzero nilpotent on the entire double. It is a hidden quadratic
parameter in the precise sense of111, for every Q and every e.

This family even has degree-two elements surviving at every invariant
divisor, when that condition concerns the full degree module: (5) shows
that the entire algebra is generated by 1,y,U from F2. Every base fiber
of this monic conic has dimension one, so both y,U cannot have algebraic
residues on any generic divisor fiber. Such a fiber is a domain: the
full kernel is factorially closed in the polynomial UFD A, so an
irreducible invariant remains irreducible and prime in A. This does
not impose the same condition on a different, preselected good pair.

The coordinate z has N-degree exactly d=deg_y P, since for n at least
one its nth derivative is (-x^e)^(n-1) times the nth y-derivative of P.
In particular degree-four perturbations satisfy z in F4 with exact
degree four. The two elements y,U are in F2 and generate A over S,
so the two-F2-plus-one-F4 requirement is also available in that subclass.
It does not create a proper image ideal: (6) rules that out everywhere.

The underlying triangular class is genuinely narrower than an arbitrary
actual original frame. It fixes an ambient invariant coordinate x and
the specific polynomial form f=y squared+xQ+x^e z. No theorem here
puts the remaining actual proper whole-double sector into this form.

## Relation to the retained controls and verification

For Q=y^4, this includes the family of
[Catalan104](quadratic-catalan-hidden-parameter-pass104.md). That note
used an explicit even-power inverse; (2) replaces it by finite monic
division and handles arbitrary odd terms and arbitrary polynomial Q.
For Q divisible by x^(e-1), a direct polynomial z-shear already reduces
to the basic family101, but that special divisibility is not assumed.
The conic, flatness and exact image ideals are proved here, not inferred
from a completion or from the earlier finite Catalan tests.

The [standalone checker](triangular_whole_double_checks_pass112.py)
has one method. It performs the finite recursion for a perturbation
containing odd and quartic terms, checks exact polynomial U and recovery,
and verifies finite derivative and residue instances. It does not certify
the arbitrary-Q, all-e or all-degree proof. The nonflat fourth-image
control106 remains a different construction; it is not repaired by
the present argument. No file through111 is changed, and no new
primary-source theorem, original-frame realization or novelty claim
is introduced.

The first assertion-bearing author run passed its one method in 1.753
unittest seconds, exit zero (output `14256d`; tool wall time
2.010415875 seconds). This finite run is separate from the written
all-polynomial proof and from independent read-only proof/code reviews.
