# Higher image ideals with a nonreduced rank-three plinth

Fix an integer \(\nu\ge1\), and define
\[
\begin{aligned}
f&=xz-y^2,& r&=-x^3-yf^\nu,\\
h&=zf^{2\nu}+2x^2yf^\nu+x^5,& S&=x^2y+zf^\nu,\\
D_\nu&=\operatorname{Jac}(f,h,\cdot),& R&=\mathbb C[x,y,z].
\end{aligned}
\]
For this family, in every image degree \(j\ge0\),
\[
\boxed{\ker D_\nu=C=\mathbb C[f,h],\qquad
J_j=D_\nu^j(R)\cap C
=f^{\nu(j-\lfloor j/5\rfloor)}h^{\lceil j/2\rceil}C.}
\tag{1}
\]
In particular the nonreduced plinth is \(J_1=(f^\nu h)\).
This note proves (1) by exact presentations and global polynomial
witnesses, not by a finite grid. It does not assert novelty for
this computation or the family itself.

The family is the specialization \(E(2,\nu,t_1^2)\) in
[Dasgupta and Gaifullin, *On locally nilpotent derivations of polynomial
algebra in three variables*, Theorem 5.7](https://arxiv.org/html/2306.00510v2#S5),
whose hypotheses are \(m\ge2\), \(n\ge1\), and a polynomial
\(F(t_1,t_2)\) with nonconstant \(F(t_1,0)\). Their local-slice
symbol has the opposite sign to the present \(r\); their Jacobian
derivation is the same. That theorem establishes rank three for this
specialization. The source does not supply an all-image formula at
that location. For \(\nu=1\), the all-image calculation is already
in Freudenburg's Section 8.2.8, as recorded in the
[canonical reconstruction](rank-three-image-pass17.md).

## 1. Exact derivation and polynomial identities

The Jacobian formulas are
\[
\begin{aligned}
D_\nu f&=D_\nu h=0,& D_\nu r&=f^\nu h,\\
D_\nu x&=2f^\nu r,&D_\nu y&=-h-6x^2r,\\
D_\nu z&=2xf^{\nu+1}-10xyr.
\end{aligned}
\tag{2}
\]
They follow by direct differentiation, or by differentiating the
following relations after verifying the Jacobian value on \(x\):
\[
xh=r^2+f^{2\nu+1},\qquad f^\nu S=rx^2+h.
\tag{3}
\]
In particular \(f,h\) are algebraically independent: the nonzero
Jacobian \(D_\nu r=f^\nu h\) would vanish if their differentials
were dependent. Write \(C_0=\mathbb C[f,h]\) until its kernel
identification is proved below.

Introduce one more polynomial:
\[
q=\frac{r^5+h^3}{f^\nu}
=h^2S-2r^3f^{\nu+1}-rf^{3\nu+2}.
\tag{4}
\]
The second expression proves that the quotient is polynomial in the
original variables. It follows that
\[
f^\nu q=r^5+h^3,\qquad D_\nu q=5hr^4.
\tag{5}
\]

## 2. The two exact charts

After inverting \(f\), relations (3) give
\[
R_f=C_{0,f}[x,r]/(r^2-hx+f^{2\nu+1}),
\tag{6}
\]
with inverse formulas
\[
y=-\frac{r+x^3}{f^\nu},\qquad
z=\frac{h+2x^2r+x^5}{f^{2\nu}}.
\tag{7}
\]
After inverting \(h\), the other exact presentation is
\[
R_h=C_{0,h}[r,q]/(r^5-f^\nu q+h^3).
\tag{8}
\]
The needed inverse formulas are
\[
x=\frac{r^2+f^{2\nu+1}}h,
\qquad
y=-\frac{rq+3r^4f^{\nu+1}+3r^2f^{3\nu+2}+f^{5\nu+3}}{h^3},
\tag{9}
\]
and
\[
z=\frac{
q^2+f(5r^8+4h^3r^3)
+f^{2\nu+2}(10r^6+2h^3r)
+10r^4f^{4\nu+3}+5r^2f^{6\nu+4}+f^{8\nu+5}
}{h^5}.
\tag{10}
\]
To derive (10), substitute \(x=(r^2+f^{2\nu+1})/h\) into
the second formula of (7). The terms of lowest \(f\)-order in
its numerator combine into \((r^5+h^3)^2\), which becomes
\(f^{2\nu}q^2\). Every other term is divisible by at least
\(f^{2\nu+1}\), so division by \(f^{2\nu}\) leaves precisely
the nonnegative powers in (10). No inverse of \(f\) remains.

Each presentation is injective as well as surjective. The first
defining relation is primitive and linear in \(x\), and the second
is primitive and linear in \(q\); each is irreducible over the
appropriate fraction field, hence defines a domain. Their maps into
\(R_f\) and \(R_h\) are surjective maps of three-dimensional
domains with the displayed generically injective presentations, so
their kernels vanish. Equivalently both identify with their indicated
subrings of \(\operatorname{Frac}(C_0)[r]\).

On that generic polynomial line,
\[
D_\nu=f^\nu h\partial_r.
\tag{11}
\]
All original generators are polynomials in \(r\) over the invariant
fraction field, so this also proves local nilpotence without a
homogeneity hypothesis. The normal forms below show that the two
localized kernels are \(C_{0,f}\) and \(C_{0,h}\).
Since \(C_{0,f}\cap C_{0,h}=C_0\), one obtains
\(\ker D_\nu=C_0=C\).

## 3. Exact localized image ideals in every degree

The normal form in (6) is a free \(C_f\)-module on
\[
x^a r^\epsilon,\qquad a\ge0,\quad \epsilon\in\{0,1\}.
\]
These have distinct derivation degrees \(2a+\epsilon\), and
generic leading coefficients \(h^{-a}\). Thus
\[
J_j C_f=f^{\nu j}h^{\lceil j/2\rceil}C_f.
\tag{12}
\]
Likewise (8), viewed as monic of degree five in \(r\), has
normal-form basis over \(C_h\)
\[
r^i q^a,\qquad 0\le i<5,\quad a\ge0.
\]
The derivation degree is \(i+5a\), with generic leading
coefficient \(f^{-\nu a}\). Hence
\[
J_j C_h=f^{\nu(j-\lfloor j/5\rfloor)}h^jC_h.
\tag{13}
\]
Distinct normal-form monomials have distinct derivation degrees, so
leading terms cannot cancel across basis elements. This observation
proves the complete localized image statements, not only membership
of selected monomials. Equations (12) and (13) imply
\[
J_j\subseteq f^{\nu(j-\lfloor j/5\rfloor)}h^{\lceil j/2\rceil}C.
\tag{14}
\]

## 4. Global witnesses remove any intersection-supported defect

Use the ten original polynomials
\[
(b_0,\ldots,b_9)=(1,r,x,rx,x^2,S,y,ry,xy,rxy).
\]
Their derivation degrees are exactly their indices. The leading
coefficients of \(r,x,S,y,z\) in the coordinate \(r\) are
\[
1,\quad h^{-1},\quad f^{-\nu}h^{-2},
\quad -f^{-\nu}h^{-3},\quad f^{-2\nu}h^{-5},
\]
respectively. Write \(j=10k+i\), \(0\le i<10\), and let
\(\epsilon_i=1\) for \(i<6\), \(\epsilon_i=-1\) otherwise.
Then the actual polynomial
\[
H_j=\frac{\epsilon_i}{j!}b_i z^k
\]
satisfies
\[
D_\nu^jH_j
=f^{\nu(j-\lfloor j/5\rfloor)}h^{\lceil j/2\rceil}.
\tag{15}
\]
This proves the reverse inclusion in (14), and therefore (1).
In particular,
\[
J_{j+10}=f^{8\nu}h^5J_j,
\qquad
\ker D_\nu^{j+1}=\bigoplus_{i=0}^j C H_i,
\qquad R=\bigoplus_{i\ge0}C H_i.
\tag{16}
\]
The basis statement follows by subtracting the matching top image
and inducting on derivation degree, exactly as in the canonical
note. For every \(j\ge1\), the only associated primes of
\(C/J_j\) are \((f)\) and \((h)\); there is no embedded
prime at their intersection.

## 5. Invariant slice extensions and the genuine lifting distinction

For \(A,B\in C\), the pass16 whole-component exclusion and
higher-image reduction now apply without an unproved freeness premise:
\[
\boxed{
AD_\nu+B\partial_t\text{ has a slice}
\iff (Af^\nu h,B)C=C
\iff (A,B)C=C\ \text{and}\ B=c+fhQ,
\quad c\in\mathbb C^*,\ Q\in C.}
\tag{17}
\]
The last equivalence uses the fact that units are detected modulo
the nilradical. More explicitly, modulo \(f^\nu h\), the element
\(fhQ\) has nilpotence exponent at most \(\nu\). A unit
restricts to the same nonzero constant on both reduced axes, so
\(B-c\in(fh)\). Conversely this residue has a finite geometric
inverse modulo \(f^\nu h\).

There is an explicit affine certificate. Put \(p=f^\nu h\),
choose \(U,V\in C\) with \(AU+BV=1\), and set
\[
T=\frac1c\sum_{i=0}^{\nu-1}\left(-\frac{fhQ}{c}\right)^i,
\qquad K=(-1)^\nu\frac{h^{\nu-1}Q^\nu}{c^\nu}.
\]
Then \(BT+pK=1\), and
\[
s=UKr+(AUT+V)t
\quad\text{satisfies}\quad
(AD_\nu+B\partial_t)s=1.
\tag{18}
\]
For example, when \(\nu=2\), \(A=1\), and \(B=1+fh\),
the slice is \(hr+(1-fh)t\).

For \(\nu>1\), condition (17) does not force
\(B\equiv c\pmod{f^\nu h}\). The example \(B=1+fh\)
is the simplest countercontrol. Therefore the pass15 matrix lift
requiring scalar congruence modulo the actual local-slice value
cannot be invoked solely from (17). Formula (18) proves an affine
slice; it does not by itself prove a coordinate frame or polynomial
kernel. A separate lifting argument is needed for that conclusion.

## 6. Scope of the computation

An independent inline SymPy run under
`/opt/anaconda3/bin/python` passed 285 exact assertions in 1.984
seconds. It checked the physical Jacobian and polynomial-parameter
identities for \(\nu=1,2,3\); the two chart inverses, all witness
degrees from zero through 29, and the geometric inverse/affine-slice
identities for \(\nu=1,2,3,5\). No research module was imported.
These finite controls check formulas only; the arbitrary-parameter
and arbitrary-image-degree proof is in Sections 1-4.

The nonreduced parameter \(\nu\) multiplies the \(f\)-valuation
of every image ideal but does not change the residue-class witness
pattern. This is an exact result for the displayed rank-three family,
not for arbitrary members of the larger local-slice construction
family in Theorem 5.7. No ordinary-degree bound or ordinary
homogeneity assumption enters the proof.

The known \(\nu=1\) computation motivated this reconstruction.
Priority for the all-image formula when \(\nu>1\) has not been
established. No general Freeness Conjecture or cancellation claim is
made.
