# Product index and the first possible component parameter

In the actual proper-image whole-double alternative, an index-square
product module gives a new coefficient restriction: b squared belongs
to (h)+a(a,b). In particular h is nonzero and coprime to a. This is
not the mixed-fiber restriction involving coprimality with b.

The same all-divisor information also shows that the derivative of
every degree-at-most-three element lies in the maximal ideal times
the actual degree-two module. Every such element is constant on the
reduced component. The specified component parameter c therefore has
degree exactly four in this alternative.

Neither conclusion excludes the proper-image alternative. The proof
does not use an independent residue of G squared, an original normal
equation in the whole fiber ideal, or a simple companion.

## 1. Actual whole-double data

Use the all-speed-normal extension in
[all-normal111, Section 6](quadratic-all-normal-mixed-exclusion-pass111.md)
of the [whole-double dichotomy111](whole-double-second-degree-dichotomy-pass111.md).
Let (R,m) be the regular local invariant surface, K its fraction field,
and A the actual faithfully flat domain localized over R. Its full-kernel
LND N has generic polynomial line K[r]. In the proper alternative,
the precise data are
\[
\begin{gathered}
F_j=\ker(N^{j+1}|_A)\simeq R^{j+1},\qquad
F_1=R\{1,r\},\quad F_2=R\{1,G,H\},\\
r=aG+bH,\quad Nr=P\ne0,\quad J_2=(a,b)\subsetneq R,
\quad \gcd(a,b)=1,\quad \sqrt{J_2}=\mathfrak m,\\
NG=\varepsilon br+h,\qquad NH=-\varepsilon ar+B_2,
\qquad P=ah+bB_2,\qquad\varepsilon\in R^*,\\
Q=\varepsilon r^2-2B_2G+2hH\in R,
\qquad h\in\mathfrak m,\quad B_2,Q\in\mathfrak m^2,\\
A/\mathfrak mA=\mathbb C[G,c]/(G^2),\qquad
\bar N=\lambda G\partial_c,\quad\lambda\in\mathbb C^*,
\qquad H\in\mathfrak mA,\quad c\in F_4.
\end{gathered}
\tag{1}
\]
Both a and b are nonzero nonunits. Initially h is allowed to be zero.
The actual generating set also gives A=R[G,H,c], but the argument below
uses only the membership and nonconstant reduced residue of c.

At every height-one prime of R the exact degree-one slice or degree-two
conic models107 apply. In particular I3=N cubed F3 is contained in
P squared R: its valuation at every height-one prime is twice that of
P, and membership contracts in the UFD R. The generic coefficient
determinant of every actual basis of F4 has valuation minus four times
that of P at each height-one prime. These are full degree-module
statements, not a claim that the fourth derivative of c generates I4.
Their all-normal use is recorded in111, equation (1).

## 2. The coefficient extraction that survives in length two

The two residues 1,G are independent, so their R-span is pure in A
by [residue-basis purity107](residue-basis-purity-pass107.md). Both
G squared and H belong to mA. Expanding the invariant conic gives
\[
\begin{gathered}
Q+2B_2G=\varepsilon a^2G^2+2\varepsilon abGH
                   +\varepsilon b^2H^2+2hH,\\
\mathfrak K_0=\mathfrak m(h)+\mathfrak m(a^2)
                 +\mathfrak m(ab)+\mathfrak m^2(b^2),\\
\boxed{\qquad B_2,Q\in\mathfrak K_0.\qquad}
\end{gathered}
\tag{2}
\]
The four terms belong respectively to m(a squared)A, m(ab)A,
m squared(b squared)A and m(h)A. Contraction through the pure
basis 1,G extracts the two coefficients. This does not extract
a squared itself: its multiplying element G squared has zero
whole-fiber residue. That missing extraction is essential.

## 3. An actual product module of index b squared

All five elements 1,G,H,G squared,GH belong to F4. In K[r],
N=P partial_r, so integration of NG gives
G=g2 r squared+g1 r+g0 with
g2=epsilon b/(2P), g1=h/P, and g0 arbitrary. Let Delta denote
the coefficient determinant in 1,r,r squared,r cubed,r fourth.
Using H=(r-aG)/b and GH=(rG-aG squared)/b gives
\[
\begin{aligned}
\Delta(1,G,H,G^2,GH)
 &=b^{-2}\Delta(1,G,r,G^2,rG)\\
 &=b^{-2}\left(\frac{\varepsilon b}{2P}\right)^4
 =\frac{\varepsilon^4b^2}{16P^4}.
\end{aligned}
\tag{3}
\]
The permutation to 1,r,G,rG,G squared has even sign. In that order
the degrees are 0,1,2,3,4 and the leading coefficients are
1,1,g2,g2,g2 squared. The calculation does not require h nonzero.

Fix an actual R-basis E of F4. At a degree-one constant divisor,
P is a unit and r is a local polynomial coordinate, so Delta(E)
has valuation zero. At a degree-two divisor, a minimal first-degree
generator r0 and quadratic parameter t give the actual basis
1,r0,t,r0t,t squared with monic equation
p to the e times t=r0 squared+alpha r0+eta. Its determinant
valuation is minus four e. The global r differs from r0 by an
invariant unit-affine change, since both derivatives generate I1
there; thus e is the valuation of P and the same determinant
valuation holds in the powers of r.

The matrix of the five actual elements in (3) relative to E has
entries in R. Its determinant has the valuations of b squared at
every height-one prime, hence equals a unit times b squared in
the UFD R. The adjugate identity proves
\[
M_b=R\{1,G,H,G^2,GH\}\subseteq F_4,
\qquad \boxed{\quad b^2F_4\subseteq M_b.\quad}
\tag{4}
\]
Only this annihilation statement is used. Neither M_b=F4 nor a
cyclic description of F4/M_b is asserted.

## 4. Derivative contraction and its asymmetric consequence

Set L0=(h)+aJ2+m(b squared). The derivatives of the product basis are
\[
\begin{gathered}
NG=h+\varepsilon abG+\varepsilon b^2H,\qquad
NH=B_2-\varepsilon a^2G-\varepsilon abH,\\
N(G^2)=2hG+2\varepsilon abG^2+2\varepsilon b^2GH,\\
N(GH)=-\varepsilon a^2G^2+\varepsilon b^2H^2+hH+B_2G,\\
\boxed{\qquad N(M_b)\subseteq L_0A,
\qquad b^2Nc\in L_0A.\qquad}
\end{gathered}
\tag{5}
\]
Here a squared and ab belong to aJ2, while b squared H belongs
to m(b squared)A. Equation (2) puts B2 in L0. These observations
check each term in (5); N kills the base coefficients. The last
membership uses b squared c in M_b from (4).

The whole residue of Nc is the nonzero nilpotent lambda G.
The one-element purity statement therefore applies to R Nc inside
the flat module A. Contracting the last membership in (5), and
cancelling the nonzero Nc in the domain, gives b squared in L0.
Absorb the term m(b squared) using a unit of the local ring. Thus
\[
\boxed{\begin{gathered}
b^2\in(h)+aJ_2,\qquad h\ne0,\qquad \gcd(h,a)=1,\\
h\notin\mathfrak mJ_2^2.
\end{gathered}}
\tag{6}
\]
If h were zero, the first membership would make a divide b squared,
contrary to coprimality and a being a nonunit. Any prime dividing both
h and a would similarly divide b, proving the gcd statement.
If h belonged to mJ2 squared, the same membership would imply
b squared belongs to aJ2+mJ2 squared. Writing the resulting coefficient
of b squared on the right as an element of m and absorbing it would
again make a divide b squared. This proves the last assertion.

No unit of Nc at a reduced point was used; there is no such point
on this whole-double fiber. The gcd in (6) is with a, not with b.
In particular it does not justify the mixed divided quartic110.

## 5. A direct cubic-module consequence of the divisor valuations

Let V be any element of F3. Write NV=A0+A1G+A2H in the actual
basis of F2. The whole derivative of any element is nilpotent in
the fiber (1). Since G is nilpotent and H has zero residue, this
forces A0 in m.

On the other hand N cubed V=epsilon P(bA1-aA2) belongs to
P squared R by Section 1. Since epsilon is a unit, there is l in R
such that bA1-aA2=P l. Substitute P=ah+bB2 and use coprimality:
\[
\begin{gathered}
b(A_1-B_2l)=a(A_2+hl),\\
A_1=B_2l+at,\qquad A_2=-hl+bt\qquad\text{for some }t\in R,\\
NV=A_0+t r+l(B_2G-hH)
   =A_0+t r+\tfrac l2(\varepsilon r^2-Q),\\
\boxed{\qquad N(F_3)\subseteq\mathfrak mF_2.\qquad}
\end{gathered}
\tag{7}
\]
Indeed a,b,h,B2 belong to m, so both A1 and A2 belong to m as
well. The factorization of a syzygy in a,b takes place in R;
no division by P in A or a completion is made.

If the whole residue of V is f(c)+G g(c), (7) implies
lambda G f prime(c)=0 in C[c,G]/G squared. Therefore f is
constant. Since N(F4) is contained in F3, we obtain
\[
\boxed{\begin{gathered}
W_3\subseteq\mathbb C+G\mathbb C[c],\qquad
N^2(F_4)\subseteq\mathfrak mF_2,\\
c\notin F_3,\qquad N^4c\ne0.
\end{gathered}}
\tag{8}
\]
Thus no cubic or lower-degree element is a reduced component parameter
in this proper branch. This statement does not bound the polynomial
g(c), identify W3 exactly, or claim purity of F2 or F3.

## 6. What remains open

The new contraction is not an exclusion. For example the coefficient
data R=C[x,y] localized at (x,y), a=x, b=y, h=y squared,
B2=Q=0 and epsilon=1 have P=xy squared nonzero and satisfy
(2) and all the ideal restrictions (6). In particular h can share
the entire divisor b despite being coprime to a. This is only a
coefficient check: no flat algebra A, actual degree lattices, canonical
whole fiber or original E-frame is constructed from this tuple.

The failed transfer from the mixed proof is exact. With only 1,G
available for coefficient extraction, (2) retains the term m(a squared)
and gives no membership for a squared itself. Equation (6) therefore
does not force h to divide a squared or produce the mixed contradiction.
The cubic-module consequence (7) rules out one route to a hidden
parameter but leaves the actual quartic c and its nilpotent derivatives.

The finite-free theorem102, all-normal dichotomy111, purity107 and
actual all-divisor classifications91/107 are the retained dependencies.
The product determinant and contraction above concern actual elements
of A, not coefficient-only examples. Root independently reconstructed
the cubic syzygy before saving. No numerical method or fresh primary
source theorem is used here. Files through111 are unchanged, and the
general cancellation and original-frame recognition goals remain open.
