# A smooth second generator is incompatible with singular distinguished a

In the actual proper whole-double alternative, the distinguished coefficient
a cannot belong to the square of the base maximal ideal while b is smooth.
This excludes every finite colength of (a,b) in that sector, not only
colength two. The proof keeps the different fiber roles of G and H intact.
An allowed shear and unit scaling lead to a weighted factorization of P
into two coprime nonunits, contradicting its single analytic prime support.

This is a bounded exclusion within the supplied actual quadratic frame.
It does not exclude the sector where both coefficients are singular or
recognize the threefold.

## 1. Actual hypotheses and the one-prime input

Retain [product-index112](whole-double-product-index-pass112.md). Over the
regular local invariant surface (R,m), the actual flat algebra A has
\[
\begin{gathered}
F_2=R\{1,G,H\},\qquad r=aG+bH,\qquad Nr=P\ne0,\\
NG=\varepsilon br+h,\qquad NH=-\varepsilon ar+B_2,\qquad
P=ah+bB_2,\qquad\varepsilon\in R^*,\\
Q=\varepsilon r^2-2B_2G+2hH\in R,\qquad
J=(a,b)\text{ is }\mathfrak m\text{-primary},\\
A/\mathfrak mA=\mathbb C[c,G]/(G^2),\qquad H\in\mathfrak mA,\\
b^2\in(h)+aJ,\qquad
B_2,Q\in\mathfrak m(h)+\mathfrak m(a^2)
                    +\mathfrak m(ab)+\mathfrak m^2(b^2).
\end{gathered}
\tag{1}
\]
The [smooth-coefficient exclusion113](whole-double-smooth-coefficient-exclusion-pass113.md)
gives h in m squared. The independent
[ramified-completion113, Sections 2--3](whole-double-ramified-completion-descent-pass113.md)
gives P=v p^e, with v a unit, e positive, and p remaining prime in Rhat.
Its proof uses the actual whole-fiber topology and divisor models.
Neither scalar completion contraction nor completed-kernel rigidity is
needed below.

Assume for contradiction that a belongs to m squared and b does not.
Put n=length_R(R/J). Since b is smooth and a belongs to m squared,
n is finite and at least two. Completion preserves this length.

## 2. A coefficient change preserving the two fiber roles

Choose formal base coordinates Rhat=C[[x,y]] with y=b. The image of a
modulo y has order n. Write
a=u x^n+y tau with u in C[[x]] a unit. Because a and u x^n belong to
m squared, tau belongs to mRhat. In A'=A tensor_R Rhat make the changes
\[
\begin{gathered}
G_1=uG,\qquad H_1=H+\tau G,\qquad
a_1=x^n,\quad b_1=y,\quad\varepsilon_1=u\varepsilon,\\
h_1=uh,\qquad B_{2,1}=B_2+\tau h,\qquad Q_1=uQ,\\
r=x^nG_1+yH_1,\qquad
NG_1=\varepsilon_1yr+h_1,\qquad
NH_1=-\varepsilon_1x^nr+B_{2,1},\\
P=x^nh_1+yB_{2,1},\qquad
Q_1=\varepsilon_1r^2-2B_{2,1}G_1+2h_1H_1.
\end{gathered}
\tag{2}
\]
These identities follow by expansion and N-invariance of all base
coefficients. The actual N and r, hence the scalar P, are unchanged.
The new G1 has a nonzero constant multiple of G as its nilradical residue.
The new H1 still has zero whole-fiber residue because tau is in m.
No interchange of G and H or arbitrary constant shear is used.

The ideal J Rhat is (x^n,y). The first coefficient restriction in (1)
also survives, but requires checking. Modulo (h1)+x^n(x^n,y), the old
a J is contained in tau(y squared). Thus y squared belongs to
(h1)+x^n(x^n,y)+m(y squared). Absorbing the last scalar coefficient
with a unit gives y squared in (h1)+x^n(x^n,y).

For the sharp B2,Q bound, reapply the exact conic in (2) rather than
assuming covariance of all coefficient ideals. The two residues 1,G1
remain independent in the flat Rhat-algebra A', so their span is pure
by [purity107](residue-basis-purity-pass107.md). The elements G1 squared
and H1 belong to mA'. Expanding the conic and contracting its two
coefficients gives precisely the last bound of (1) for the new
coefficients. Rename them a,b,G,H,epsilon,h,B2,Q from now on.

## 3. Normalized coefficient ideals

We have a=x^n, b=y and h in m squared. Write the normalized first
restriction as y squared=s h+x^(2n)t+x^n y w. The last two terms have
ordinary orders at least four and three. Comparing the nonzero quadratic
term y squared forces s to be a unit and h to have ordinary order two.
It follows that
\[
\begin{gathered}
J=(x^n,y),\qquad
h=s^{-1}\bigl(y^2-x^{2n}t-x^nyw\bigr)\in J^2,
\quad s\in\widehat R^*,\\
\boxed{\quad B_2,Q\in\mathfrak mJ^2.\quad}
\end{gathered}
\tag{3}
\]
Indeed every summand in the transformed sharp ideal is contained in
mJ squared once h belongs to J squared. Its terms m(a squared) and
m(ab), together with m(h), supply the required bound; no extraction
of a squared through a nonzero residue of G squared is made.

The coefficient of y squared in the weighted leading form of h below
is the nonzero residue of s inverse. In particular that leading form
is not divisible by x.

## 4. The weighted initial factors are coprime

Give x weight one and y weight n. This positive filtration is equivalent
to the ordinary maximal-ideal filtration. Each generator of J squared
has weight 2n, while every element of m has weight at least one. Hence
\[
\begin{gathered}
h=h_{2n}+O_{\rm wt}(2n+1),\qquad
h_{2n}=\alpha y^2+\beta x^ny+\delta x^{2n},\quad\alpha\ne0,\\
B_2=O_{\rm wt}(2n+1),\qquad
P=x^nh_{2n}+O_{\rm wt}(3n+1),\\
\gcd(x^n,h_{2n})=1,\qquad
(x^n,h_{2n})=(x^n,y^2)\subset\mathbb C[x,y].
\end{gathered}
\tag{4}
\]
The symbols alpha,beta,delta in (4) are complex constants. The quotient
by the last ideal has monomial basis x^i y^j for i<n and j<2. Its
highest possible weight is 2n minus one. Thus every weighted homogeneous
polynomial of weight at least 2n belongs to that ideal.

## 5. Complete lifting of the two factors

Start with L=x^n and H0=h2n. Suppose their product agrees with P below
weight d, for d at least 3n+1, and let E_d be the weighted degree-d
part of P minus the current product. By (4), choose weighted homogeneous
polynomials U_(d-2n), V_(d-n) satisfying
\[
E_d=h_{2n}U_{d-2n}+x^nV_{d-n},\qquad
L\longleftarrow L+U_{d-2n},\qquad
H_0\longleftarrow H_0+V_{d-n}.
\tag{5}
\]
The first new correction has weight at least n+1, and the second at
least 2n+1. Existing higher terms of either factor contribute only
above weight d. The product of the corrections has weight 2d-3n,
which is at least d+1. Thus the new product agrees through weight d.
Continuing, with zero corrections when the error vanishes, gives
convergent factors in Rhat satisfying
\[
\begin{gathered}
P=L H_0,\qquad
L=x^n+O_{\rm wt}(n+1),\qquad
H_0=h_{2n}+O_{\rm wt}(2n+1),\qquad
\gcd(L,H_0)=1,\\
\boxed{\quad
\text{actual proper whole-double branch and }a\in\mathfrak m^2
\quad\Longrightarrow\quad b\in\mathfrak m^2.
\quad}
\end{gathered}
\tag{6}
\]
For coprimality, a common nonunit formal divisor would have a positive
weighted initial form dividing both x^n and h2n, contrary to (4).
Both L and H0 are nonunits. In the regular local UFD Rhat their product
therefore has at least two distinct prime divisors, contradicting the
single analytic prime support of P. This proves the boxed conclusion.
Neither factor is claimed smooth or irreducible by itself.

## Scope and verification

The original colength-two question is the case n=2. The same complete
argument treats every n at least two because all coefficient changes
preserve the distinguished fiber roles and all weighted errors can be
lifted. It uses actual flat purity for the normalized sharp bound, but
the factorization from (3) onward is a coefficient-ring argument. No
weak formal model is presented as an actual frame.

The separate case where a itself is smooth is not proved here. Nor
does this proof apply when both a and b lie in m squared. In particular
it does not finish the proper whole-double problem or the arbitrary-frame
entry problem. Completed finite-degree descent113 is not used.

The complete product-index112 proof and purity107 proof were reread;
the exact single-prime and coefficient-exclusion sections113 were
checked in the current frozen versions. The weighted factor lifting
is proved directly, not inferred from a finite truncation test. Root
independently reconstructed the all-n extension from the colength-two
outline. No numerical method or fresh external source theorem is added,
and no file through113 is changed.
