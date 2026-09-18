# Polynomial-curve local slices and their invariant extensions

The finite-jet coordinate construction extends from the monomial curve
polynomial to an arbitrary monic polynomial. This note proves the base
derivation's kernel, primitivity and plinth, then constructs polynomial
coordinates for every invariant slice extension. The construction is a
restricted result, not a reduction of arbitrary threefold cancellation.
Its mathematical priority is not established.

## 1. Definition and polynomial presentation

Work over \(\mathbb C\). Let \(F(Y)\) be monic of degree
\(d\ge2\), let \(n\ge1\), and let \(P(X,f)\) satisfy
\(a:=\deg_XP(X,0)\ge1\). Put
\[
G(R,S)=S^dF(R/S),\qquad
f=xz-F(y),\qquad r=xP(x,f)+yf^n,
\]
\[
K(f,r)=G(r,f^n)+f^{nd+1},\qquad h=K(f,r)/x,
\qquad \delta=-\operatorname{Jac}(f,h,\cdot).
\tag{1}
\]
The homogenization \(G\) is a polynomial even at \(S=0\).
Taylor expansion gives the polynomial formula
\[
h=zf^{nd}+\sum_{k=1}^d
 \frac{F^{(k)}(y)}{k!}x^{k-1}P(x,f)^k f^{n(d-k)}.
\tag{2}
\]
In particular \(h\) is polynomial and
\[
h\equiv x^{d-1}P(x,0)^d\pmod f,
\qquad r\equiv xP(x,0)\pmod f.
\tag{3}
\]
The polynomial \(f\) is prime in \(R=\mathbb C[x,y,z]\):
it is primitive linear in \(z\), since \(x\) and \(F(y)\)
are coprime. Formula (3) implies that \(f,h\) are algebraically
independent. Indeed, in a polynomial relation remove the largest
common power of \(f\) from its coefficients, then reduce modulo
\(f\); a nonzero polynomial in the nonconstant expression
\(x^{d-1}P(x,0)^d\) cannot vanish.

There is an exact presentation
\[
R_f\cong
\frac{\mathbb C[f,f^{-1},h,x,r]}{(xh-K(f,r))}.
\tag{4}
\]
Recover \(y=(r-xP(x,f))/f^n\). The identity
\[
z=\frac h{f^{nd}}+
  \frac{F(y)-F(r/f^n)}x
\tag{5}
\]
is polynomial in the presented ring: the second numerator is divisible
by \(x\), because \(y-r/f^n=-xP(x,f)/f^n\). It gives the
inverse presentation and verifies \(f=xz-F(y)\). Alternatively,
injectivity follows by inverting \(x\), where \(f,x,r\) are
independent coordinates, and using the primitive linear relation in
\(h\) to exclude \(x\)-torsion.

The monomial specialization \(F(Y)=Y^d\) is the displayed
Dasgupta--Gaifullin Theorem 5.7 family. The arbitrary monic case
already fits Freudenburg's general local-slice construction, recalled
as their Theorem 2.17.[^1] In fact, start with
\(D_0=x\partial_y+F'(y)\partial_z\), whose kernel is
\(\mathbb C[x,f]\) and which sends \(r\) to \(xf^n\).
Modulo \(x\), the minimal irreducible relation of \(f,r\)
is \(K(f,r)=0\): after inverting \(f\), it becomes
\(F(r/f^n)+f=0\), of degree \(d\) over \(\mathbb C(f)\).
The existing theorem therefore supplies the LND construction.
The direct proofs below also compute its exact plinth. The
[statement-level audit](polynomial-curve-literature-pass18.md)
records the substitutions, original source, and distinction between
this established machinery and the four-variable coordinate claim.

## 2. Local nilpotence and exact invariant ring

A direct Jacobian calculation gives
\(\operatorname{Jac}(f,x,r)=xf^n\). Applying it to \(xh=K\)
therefore gives
\[
\delta f=\delta h=0,\qquad
\delta r=f^nh,\qquad \delta x=f^nG_R(r,f^n).
\tag{6}
\]
After inverting \(fh\), (4) becomes
\(R_{fh}=\mathbb C[f^{\pm1},h^{\pm1}][r]\).
On this ring \(\delta=f^nh\partial_r\), so every element
of \(R\) has a finite nilpotent derivative sequence. This proves
that the polynomial Jacobian derivation is locally nilpotent.

Since \(G\) is monic in \(r\), (4) has the free module basis
\[
x^b r^i,\qquad b\ge0,\quad 0\le i<d,
\quad\text{over }\mathbb C[f^{\pm1},h].
\tag{7}
\]
Its elements have distinct \(\delta\)-degrees \(db+i\): in
the further localization at \(h\), \(x=K/h\) has degree
\(d\) in \(r\), with nonzero leading coefficient \(1/h\).
Thus a nonconstant basis term cannot cancel the highest degree of
another. Invariants of \(R_f\) are precisely
\(\mathbb C[f^{\pm1},h]\), and its elements of degree at most
one are precisely \(b(f,h)+c(f,h)r\) over that ring.

If an invariant of \(R\) had a pole in \(f\), clearing its
highest pole and reducing modulo \(f\) would give a nonzero
polynomial in \(x^{d-1}P(x,0)^d\) equal to zero. Hence
\[
\ker\delta=C:=\mathbb C[f,h].
\tag{8}
\]
This proof does not assume that invariants commute with an arbitrary
specialization.

## 3. Primitivity, the plinth and rank

Because kernels of LNDs are factorially closed, \(f,h\), which
are prime in (8), are prime in \(R\). Any common irreducible
factor of the coefficients of \(\delta\) divides
\(\delta r=f^nh\), and so must be \(f\) or \(h\).
Modulo \(h\) in (4), \(G_R\) has degree \(d-1\) in
\(r\), whereas the monic relation \(K\) has degree \(d\).
It is nonzero there, so \(h\nmid\delta x\).

Writing \(P_0(x)=P(x,0)\), differentiation of \(r\) gives
\[
\delta y=h-G_R(r,f^n)(P+xP_x).
\]
Its residue modulo \(f\) is
\[
x^{d-1}P_0^{d-1}\bigl((1-d)P_0-dxP_0'\bigr),
\tag{9}
\]
which is nonzero: its leading coefficient has factor
\(1-d-da\ne0\). Thus \(f\nmid\delta y\), proving
primitivity.

Set \(H_0=x^{d-1}P_0^d\), \(R_0=xP_0\).
The element \(R_0\) is not in \(\mathbb C(H_0)\).
Indeed \(\deg H_0=d(a+1)-1>a+1=\deg R_0\), whereas
\(R_0\in\mathbb C(H_0)\) would make
\([\mathbb C(x):\mathbb C(H_0)]\) divide
\([\mathbb C(x):\mathbb C(R_0)]\).

Suppose \(u\in R\) and \(\delta^2u=0\). By (7),
\(u=b(f,h)+c(f,h)r\) with \(b,c\in C_f\). If either
coefficient has a pole in \(f\), multiply by the largest required
power and reduce modulo \(f\). The resulting nontrivial identity
\(b_0(H_0)+c_0(H_0)R_0=0\) contradicts either the preceding
field-degree fact or nonconstancy of \(H_0\). Consequently
\[
\ker\delta^2=C\oplus Cr,\qquad
\delta(R)\cap C=f^nhC.
\tag{10}
\]
In particular \(r\) is a minimal local slice, with the full
nonreduced plinth multiplicity \(n\), not just its radical.

For rank, use the published fact that a primitive rank-at-most-two
LND on three-space has a nonzero local-slice derivative in
\(\mathbb C[u]\) for an invariant ambient coordinate \(u\).
This is Lemma 4.3 of Dasgupta--Gaifullin, whose proof localizes at
\(\mathbb C(u)\).[^1] By (10), both \(f\) and \(h\)
would divide a nonzero polynomial in \(u\). Factorial closure of
\(\mathbb C[u]\) would put both in that one-variable ring,
contradicting (8). Thus \(\delta\) has rank three.

## 4. Invariant slice extensions

Let \(A,B\in C\) and \(E=A\delta+B\partial_t\) on
\(R[t]\). The general affine-replacement proof, with its stated
geometric dependencies, gives the equivalence
\[
E\text{ has a slice}
\quad\Longleftrightarrow\quad
(A,B)C=C\ \text{ and }\ B=c+fhQ,
\quad c\in\mathbb C^*,\ Q\in C.
\tag{11}
\]
Indeed its criterion is \((Af^nh,B)=1\). A unit on each of
the two coordinate axes \(f=0\) and \(h=0\) is constant,
and the constants agree at their intersection. This gives the stated
form of \(B\). Conversely that form makes \((f^nh,B)=1\),
and adjoining \((A,B)=1\) gives the criterion.
The necessary geometric implication is in the
[all-rank affine-replacement note](general-invariant-affine-pass17.md),
with its [second audit](pointwise-plinth-second-audit-pass17.md).

The remaining sections construct polynomial coordinates in every
positive case. For sufficiency they need only the hypotheses on the
right of (11), not the geometric implication. Divide \(E\) by
\(c\), so henceforth \(c=1\), and choose \(U,V\in C\)
with \(Af^nhU+BV=1\). Set \(g=f^nh\) and
\[
\rho=Br-Agt,\qquad s=Ur+Vt,
\qquad r=V\rho+Ags,\quad t=-U\rho+Bs.
\tag{12}
\]
Then \(E\rho=0\), \(Es=1\), and the two matrices are
inverse. Both \(B\) and \(V\) are 1 modulo \(h\), and
\(B\) is 1 modulo \(f\).

## 5. Finite correction and forward coordinates

Define
\[
X=\frac{G(\rho,f^n)+f^{nd+1}}h.
\tag{13}
\]
It is polynomial because \(\rho-r\) is divisible by \(h\)
and \(xh=G(r,f^n)+f^{nd+1}\). More precisely,
\[
X\equiv B^d x\pmod{f^n},\qquad X\equiv x\pmod f.
\tag{14}
\]
For the first congruence expand the numerator difference from
\(B^d xh\). Terms involving \(t\) contain \(f^nh\);
each lower homogeneous term has a factor \(f^n\), and
\(B^j-B^d\) is divisible by \(h\). The constant correction
\((1-B^d)f^{nd+1}\) also has both factors. This proves
divisibility before reduction, without canceling \(h\) modulo
\(f^n\).

In \(\mathbb C[X,f]/(f^n)\), define the unique finite jet
\[
H=b_H^{1-d}P(b_H^{-d}X,f),\qquad
b_H=B\bigl(f,X^{d-1}H^d\bigr).
\tag{15}
\]
Start with \(P(X,f)\), truncate modulo \(f^n\), and apply
the displayed update \(n-1\) times. Since \(B=1+fhQ\),
every unit power has a finite binomial expansion, and changing \(H\)
by a multiple of \(f^j\) changes the update by a multiple of
\(f^{j+1}\). This proves existence and uniqueness in any
specialized algebra with \(f^n=0\).

In the original ring modulo \(f^n\), one has
\(r=xP\), \(h=x^{d-1}P^d\), \(\rho=B xP\), and
\(X=B^d x\). Hence
\(B^{1-d}P(B^{-d}X,f)\) solves (15) there, so uniqueness gives
that value for \(H\). Therefore
\[
Y=\frac{\rho-XH}{f^n}
\tag{16}
\]
is polynomial. Use the representative of \(H\) of degree less
than \(n\) in \(f\), and put
\[
S_F(X,H,Y,f)=\sum_{k=1}^d
\frac{F^{(k)}(Y)}{k!}X^{k-1}H^k f^{n(d-k)}.
\]
Taylor's formula yields
\[
X(h-S_F)=f^{nd}(F(Y)+f).
\tag{17}
\]
Since \(f\) is prime and \(X\equiv x\pmod f\),
\(f\nmid X\). Thus \(f^{nd}\mid h-S_F\), proving
polynomiality of
\[
Z=\frac{h-S_F} {f^{nd}},\qquad f=XZ-F(Y).
\tag{18}
\]
Each of \(X,Y,Z\) is annihilated by \(E\).

## 6. Explicit polynomial inverse

Now work in the independent polynomial ring
\(T=\mathbb C[X,Y,Z,s]\). Define
\[
f=XZ-F(Y),\quad \rho=XH+Yf^n,\quad h=S_F+Zf^{nd}.
\tag{19}
\]
These satisfy \(Xh=G(\rho,f^n)+f^{nd+1}\).
The reconstructed \(h\) is nonzero: specialize \(Y\) to
any complex root of \(F\) and \(Z=0\). Then \(f=0\)
and \(h=X^{d-1}P(X,0)^d\ne0\). This argument does not
assume that \(F(0)=0\).

Evaluate \(A,B,U,V\) at these \(f,h\), recover \(r,t\)
from (12), and define
\[
W=\frac{V-1}h\rho+Af^ns,
\qquad
x=X+W\frac{G(r,f^n)-G(\rho,f^n)}{r-\rho}.
\tag{20}
\]
The divided difference denotes its polynomial expression, including
when the two arguments coincide. Also \((V-1)/h\) is polynomial
in \(C\). As \(r-\rho=hW\), (20) gives
\(xh=G(r,f^n)+f^{nd+1}\).

Modulo \(f^n\), the same expansion as in (14) gives
\[
x\equiv V^dX,\quad r\equiv V\rho=VXH,\quad
H\equiv V^{d-1}P(V^dX,f).
\tag{21}
\]
For clarity, the first equality follows from
\(x\equiv X+((V^d-1)/h)\rho^d\): replace
\(\rho^d\) by \(hX\) modulo \(f^n\), multiplying by
the already polynomial coefficient \((V^d-1)/h\). There is
no division by \(h\) in a nonreduced quotient. The last equality
uses (15), the fact that \(h\equiv X^{d-1}H^d\pmod{f^n}\),
and \(BV\equiv1\pmod{f^n}\).

Thus \(y=(r-xP(x,f))/f^n\) is polynomial. Since
\(x\equiv X\pmod f\), the prime \(f=XZ-F(Y)\) does
not divide \(x\). Equation (2) in the reconstructed variables
gives
\[
x\bigl(h-S_F(x,P(x,f),y,f)\bigr)
   =f^{nd}(f+F(y)).
\]
Consequently
\[
z=\frac{h-S_F(x,P(x,f),y,f)}{f^{nd}}
\tag{22}
\]
is polynomial and \(xz=f+F(y)\). Equations (12), (20)-(22)
are the requested inverse formulas.

Substituting the forward coordinates recovers the original \(r,t\)
by (12), then \(x\) from \(xh=K\) with \(h\ne0\),
then \(y,z\). Thus \(X,Y,Z,s\) generate \(R[t]\).
The surjection from a polynomial four-ring has prime kernel of height
zero and is injective. Therefore
\[
R[t]=\mathbb C[X,Y,Z,s],\qquad
E=\partial_s,\qquad \ker E=\mathbb C[X,Y,Z]
\tag{23}
\]
in the normalized case. Undoing the nonzero scalar normalization does
not change the invariant ring or coordinate conclusion.

## 7. Scope and next obstruction

The extension includes polynomials with nonzero constant terms,
distinct roots, repeated roots, and multiple critical values. It uses
the specific two-chart relation (4); no classification of all rank-three
LNDs by that relation has been proved. The direct sufficiency proof
is algebraic. Necessity in (11) additionally depends on the source-based
pointwise theorem recorded in pass 17.

The finite correction changes the presentation of the common invariant
ring. It does not purport to extend the canonical scaling of a local
slice while fixing the original invariant plane. The
[radical-modification investigation](radical-modification-attack-pass18.md)
tests precisely that distinction. Formal agreement along the plinth
does not by itself give polynomial global coordinates.

Finite Taylor and Hermite corrections have explicit predecessors in
Danielewski cylinder isomorphisms.[^2] The present polynomial-kernel
conclusion is not attributed to that theorem. No claim of priority
follows from the bounded source comparison.

## 8. Proof checks and reproducibility

The [separate algebraic exploration](polynomial-fiber-findings-pass18.md)
reconstructs the localized presentation and kernel. Its finite examples
do not replace the all-parameter primitivity and plinth proofs in
Section 3. A second independent reconstruction also found no gap in
Sections 1-3. The [coordinate audit](polynomial-curve-lift-audit-pass18.md)
checks Sections 4-6, including every lower coefficient of \(F\),
both directions of divisibility, and the global composition.

The standalone [eight-method checker](polynomial_fiber_checks_pass18.py)
tests exact physical Jacobians and actual forward and inverse jet
expressions. These are finite regression controls, not formal verification
of the arbitrary-parameter proof. The current full execution record is
[verification-pass-18.json](../verification-pass-18.json). No human
expert review or proof-assistant certification has occurred.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [On locally nilpotent derivations of polynomial algebra in three variables](https://www.mathnet.ru/eng/sm10094), *Sbornik: Mathematics* 216(4) (2025), 456-484. Theorem 2.17, Lemma 4.3, Corollary 5.6, and Theorem 5.7. Published full HTML consulted. The general local-slice construction is credited there to Freudenburg's 1997 paper; the explicit arbitrary-monic application above is not the displayed Theorem 5.7 family.
[^2]: L. Moser-Jauslin and P.-M. Poloni, [Isomorphisms between cylinders over Danielewski surfaces](https://arxiv.org/html/2002.12202), arXiv:2002.12202v1 (2020), Section 4 and Theorem 4.0.1. Methodological predecessor, not a general polynomial-kernel theorem.
