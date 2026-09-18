# Fixed-good shears preserve the tails and determine minimal time degree

For an actual dense three-good chart, replacing the last coordinate
by itself plus a complex polynomial in the goods preserves both
negative-tail polynomials exactly. Their coefficient field and intrinsic
normalization can also be kept fixed.

The least last-coordinate time degree under these shears is one less
than the degree of the first tail. Consequently, primitivity of that
tail is equivalent to equality between this minimum plus one and the
degree of the exact generic embedded-line equation. This is a
fixed-good reduction criterion, not a proof that the first tail is
always primitive or a global recognition theorem.

## 1. Actual hypotheses and fixed normalization

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX,\quad t=EY,\quad b=EZ,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b)=2,\qquad
H(s,t,b)\ne0
\quad\text{for every nonzero homogeneous }H\in\mathbb C[S,T,B_0].
\end{gathered}
\tag{1}
\]
The four displayed generators of \(B\) are actual polynomial
coordinates. There is no upper bound on \(m=\deg_E W\ge0\).

Use the dense chart139 with one fixed choice of its normalized
intrinsic parameter.[^1] In particular,
\[
\begin{gathered}
T=\partial_W,\qquad N=[u^2]T|_A\ne0,\qquad
S_0=\ker_A N,\quad L=\operatorname{Frac}S_0,\\
\tau=t/s,\quad \rho=b/s,\qquad
L/\mathbb C(\tau,\rho)\text{ finite separable},\\
N'=N/s^2,\qquad A_L=L[v],\quad N'v=1,\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
y,z\in L[v],\quad L[y,z]=L[v].
\end{gathered}
\tag{2}
\]
Here \(A_L=(S_0\setminus\{0\})^{-1}A\), and \(v\) is fixed
throughout the argument. The coefficient partials
\(\partial_\tau,\partial_\rho\) extend uniquely from the rational
base to \(L\), commute, and are extended to \(L(v)\) by fixing \(v\).

For independent formal variables \(U,V\), write
\[
\begin{gathered}
H_d(f;U,V)=\sum_{a+b=d}
 \frac{\partial_\tau^a\partial_\rho^b f}{a!\,b!}U^aV^b,\qquad
\Theta(f)=\sum_{d\ge0}H_d(f;y,z)X^{-d},\\
\mathscr S=\sum_{j=0}^{m}X^j\Theta(f_j),\qquad
W=(\mathscr S)_{\ge0},\qquad
\mathscr R=W-\mathscr S,\quad T\mathscr R=1,\\
R_1=-\sum_{j=0}^{m}H_{j+1}(f_j;U,V),\qquad
f_{-1}=R_1(y,z)\in L,\\
\Phi=R_1-f_{-1}\ne0,\qquad
\Psi=-\sum_{j=0}^{m}H_{j+2}(f_j;U,V)-H_1(f_{-1};U,V).
\end{gathered}
\tag{3}
\]
The \(f_j\in L\) are the canonical downward peeling coefficients.
The Taylor map is an embedding into \(L(v)((X^{-1}))\);
it satisfies \(T\Theta(f)=0\). These formal and actual-ring
statements, including the nonzero first relation, are inherited
from the complete chart and tail proofs139.[^2]

The same tail proof gives \(\Phi(y,z)=0\),
\(\partial_v\Psi(y,z)=1\), and \(1\le\deg\Phi\le m+1\).
Degrees of polynomials in \(U,V\) below are ordinary total degrees
over \(L\). No independence of the evaluated pair \(y,z\) is assumed.

## 2. Exact invariance under every polynomial bad-slot shear

Let \(P\in\mathbb C[X,Y,Z]\) and put
\(\widetilde W=W+P\). This is an actual elementary coordinate
change with inverse \(W=\widetilde W-P\), fixing all three goods.

The new selected partial equals the old one: \(T\) kills the goods
and has \(T(\widetilde W)=1\), which determines the coordinate
partial uniquely. Therefore \(T,N,S_0,L,N'\) in (2) are unchanged.
The speeds, their ratios, and \(y=Y-\tau X,\ z=Z-\rho X\) are
unchanged too. Keeping the same \(v\) keeps the coefficient
partials and \(\Theta\) literally unchanged. The Taylor projection
of the last coordinate can change, but it does not change any
of this fixed data.

Decompose \(P=\sum_{j=0}^{d}P_j\) into its homogeneous pieces,
allowing \(P=0\). Set \(p_j=P_j(1,\tau,\rho)\), so that
\(p_j\in\mathbb C[\tau,\rho]\) has degree at most \(j\).
Multiplicativity of \(\Theta\) and its values
\(\Theta(\tau)=Y/X,\ \Theta(\rho)=Z/X\) give
\[
P_j(X,Y,Z)=X^j\Theta(p_j),\qquad
H_k(p_j;U,V)=0\quad(k>j).
\tag{4}
\]
Although the first identity is conveniently written in the Laurent
field, both sides are the same polynomial: the Taylor series on
the right truncates at order \(j\). In particular no localization
at the geometric divisor \(X=0\) is required for the shear or its
inverse.

Pad \(f_j\) and \(p_j\) by zero to a common finite upper index.
Then the canonical peeling coefficients for \(\widetilde W\) are
\(\widetilde f_j=f_j+p_j\). To see uniqueness, a finite sum
\(\sum_jX^j\Theta(c_j)\) with a nonzero largest \(c_j\) has
coefficient \(c_j\) at its highest power \(X^j\); its nonnegative
part cannot vanish. Thus the polynomial-part expansion determines
all the nonnegative peeling coefficients. This also handles
cancellation of the previous highest coefficient.

It follows that
\[
\begin{gathered}
\widetilde{\mathscr S}=\mathscr S+P,\qquad
\widetilde{\mathscr R}=\mathscr R,\qquad
\widetilde f_{-1}=f_{-1},\\
\widetilde R_1=R_1,\qquad
\widetilde\Phi=\Phi,\qquad
\widetilde\Psi=\Psi .
\end{gathered}
\tag{5}
\]
The last line is an identity in the formal ring \(L[U,V]\), not
merely after evaluation: every added
\(H_{j+1}(p_j)\) and \(H_{j+2}(p_j)\) is zero by (4).
The adjusted tail
\(\mathscr R-X^{-1}\Theta(f_{-1})\) is also unchanged.

There is no upper-degree restriction on \(P\). In particular,
a shear of degree larger than \(m\) obeys (4)--(5).
Such a nonzero shear cannot lower the last degree: if
\(d=\deg P>m\), its \(X^d\) coefficient is the nonzero
\(P_d(1,\tau,\rho)\), since \(\tau,\rho\) are independent.
Hence \(\deg_E(W+P)=d\). More generally the same argument proves
\(\deg_E P=\deg P\) for every nonzero polynomial in the goods,
using \(E=s\partial_X\) in the actual localized chart.

## 3. Finite algebraic extensions do not create extra polynomial jets

The exact joint constant field of \(L\) is
\[
\ker(\partial_\tau|_L)\cap\ker(\partial_\rho|_L)=\mathbb C .
\tag{6}
\]
Here is a proof which does not replace \(L\) by its rational base.
For a joint constant \(c\in L\), let
\(M(T_0)=T_0^e+\sum_{i<e}a_iT_0^i\) be its monic minimal
polynomial over \(\mathbb C(\tau,\rho)\).
Differentiating \(M(c)=0\) with either coefficient partial gives
a polynomial of degree less than \(e\), vanishing at \(c\).
Minimality implies that every corresponding derivative of \(a_i\)
vanishes.

The joint constants in \(\mathbb C(\tau,\rho)\) are \(\mathbb C\).
Indeed, for a rational function in one variable over a
characteristic-zero coefficient field, a zero derivative makes it
constant: writing it as a coprime quotient, its denominator would
otherwise divide its own lower-degree derivative; then the
numerator derivative also vanishes. Apply this first in \(\tau\)
over \(\mathbb C(\rho)\), then in \(\rho\).
Thus \(a_i\in\mathbb C\), so \(c\) is algebraic over
the algebraically closed field \(\mathbb C\), and \(c\in\mathbb C\).
This proves (6).

For every integer \(h\ge0\) and \(f\in L\), one consequently has
\[
H_{h+1}(f;U,V)=0
\quad\Longleftrightarrow\quad
\partial_\tau^a\partial_\rho^b f=0\quad(a+b=h+1)
\quad\Longleftrightarrow\quad
f\in\mathbb C[\tau,\rho]_{\le h}.
\tag{7}
\]
The first equivalence uses independent formal monomials and
characteristic zero. For the second, argue by induction on \(h\).
When \(h=0\), it is (6).
For \(h>0\), every order-\(h\) mixed derivative of \(f\)
is a joint constant \(c_{ab}\in\mathbb C\).
Subtract the homogeneous polynomial
\(\sum_{a+b=h}c_{ab}\tau^a\rho^b/(a!\,b!)\).
All its order-\(h\) derivatives match those of \(f\), so the
difference has all such derivatives zero. The induction
hypothesis places that difference in
\(\mathbb C[\tau,\rho]_{\le h-1}\).
The converse follows by differentiating a polynomial.

In particular, the disappearance of the top formal homogeneous
part of \(\Phi\) is a condition over \(\mathbb C\), even when the
coefficient field is a proper finite extension. It is not enough
to assume that evaluated Taylor terms vanish on the generic line;
(7) concerns their vanishing in \(L[U,V]\).

## 4. Exact minimal degree and an explicit minimizing shear

Define
\[
\mu=\min_{P\in\mathbb C[X,Y,Z]}\deg_E(W+P),\qquad
D=\deg\Phi\ge1 .
\tag{8}
\]
Every \(W+P\) is an actual last coordinate and has \(T(W+P)=1\),
so it is nonzero and its time degree is a nonnegative integer.
The set in (8) is nonempty. By (5) and the tail bound139 applied
to every sheared frame, \(D\le\deg_E(W+P)+1\). Thus
\(\mu\ge D-1\).

The homogeneous part of degree \(j+1\) in \(\Phi\) is exactly
\(-H_{j+1}(f_j;U,V)\). Different indices cannot cancel it.
Therefore every \(j\ge D\) satisfies the vanishing condition (7),
and \(f_j\in\mathbb C[\tau,\rho]_{\le j}\).
Define
\[
\begin{gathered}
P_*=-\sum_{j=D}^{m}X^j f_j(Y/X,Z/X)\in\mathbb C[X,Y,Z],\\
\deg_E(W+P_*)=D-1,\qquad
\boxed{\ \mu=\deg\Phi-1\ } .
\end{gathered}
\tag{9}
\]
Each summand is the homogeneous polynomial obtained from \(f_j\)
by degree-\(j\) homogenization. The displayed ratios create no
denominators in \(P_*\).
The sum is empty if \(D=m+1\).

By (4), this shear sets precisely the peeling coefficients
\(f_j\), \(j\ge D\), to zero. The coefficient at \(X^{D-1}\)
of the remaining polynomial is \(f_{D-1}\), which is nonzero:
the degree-\(D\) homogeneous part
\(-H_D(f_{D-1};U,V)\) of \(\Phi\) is nonzero.
This proves the exact degree in (9), not just an upper bound.

For \(m\ge1\), an immediate equivalent top-degree test is
\[
\begin{gathered}
\text{some fixed-good shear lowers the degree }m\\
\Longleftrightarrow\quad \deg\Phi<m+1
\quad\Longleftrightarrow\quad
f_m\in\mathbb C[\tau,\rho]_{\le m}.
\end{gathered}
\tag{10}
\]
The last condition supplies a homogeneous degree-\(m\) lowering
shear directly. Conversely, a shear of degree greater than \(m\)
cannot lower it, and comparison of the \(X^m\) coefficient in any
lowering shear gives the same polynomial condition.

If \(m=0\), the inherited nonzero relation has degree exactly one.
Thus \(D=1\), the sum in (9) is empty, and \(\mu=0\).
In this case \(f_0\notin\mathbb C\), since otherwise
\(\Phi=0\) in (3). There is no claim of a reduction to a negative
time degree, or of discarding a constant-degree coordinate.

## 5. Primitivity is precisely a remaining degree equality

Let \(g\in L[U,V]\) generate the exact evaluation kernel
\[
\ker\bigl(L[U,V]\longrightarrow L[v],\ (U,V)\longmapsto(y,z)\bigr)
=(g),\qquad g\text{ irreducible}.
\]
The map and its kernel are unchanged under the shears above.
Write \(\Phi=gH\). The tail identities imply
\(H(y,z)\in L^*\), hence \(g\) has multiplicity one in \(\Phi\);
they do not imply \(H\in L^*\).[^3]

Here “primitive first tail” means associated to this exact
irreducible equation, not coefficient-content primitivity.
Additivity of total degree for nonzero polynomial products over
\(L\), together with (9), gives
\[
\begin{gathered}
\deg g\le\mu+1,\qquad
\Phi\in L^*g
\quad\Longleftrightarrow\quad H\in L^*
\quad\Longleftrightarrow\quad
\deg g=\mu+1 .
\end{gathered}
\tag{11}
\]
Equivalently, \(\Phi\) is irreducible if and only if this degree
equality holds. No factor is selected after extending \(L\):
the kernel and all degrees in (11) use the same exact field.

Thus minimizing the last time degree does not by itself establish
primitivity. It places the first tail at its sharp formal degree
\(\mu+1\), while the possible strict inequality
\(\deg g<\mu+1\) is a separate problem. The result concerns all
polynomial shears in one fixed set of three goods, not arbitrary
changes of the good-coordinate ring, a global invariant coordinate,
or cancellation.

## Sources

1. [A dense all-degree chart and its formal Taylor peeling139](dense-all-degree-taylor-chart-pass139-working.md),
   Sections 1--6. Actual hypotheses, normalized intrinsic derivation,
   finite coefficient field, Taylor embedding and canonical peeling.
2. [The first two negative Taylor coefficients in a dense chart139](dense-negative-tail-relations-pass139-working.md),
   Sections 2--4. Nonzero first relation, both signed tail formulas,
   degree bounds and the exact generic-line kernel.
3. [Degree-controlled embedded lines in the dense three-good case139](dense-generic-embedded-line-pass139-working.md),
   Sections 1--4. The distinction between an exact primitive equation
   and the first tail's possible residual factor.

The shear identities, coefficient-field derivative lemma and
minimization argument are proved directly here. No additional
classification theorem or historical novelty claim is used.

[^1]: Source 1. Its leading-derivation inputs are the retained
    intrinsic construction125, Sections 2--5, and dense cofactor132.
[^2]: Sources 1--2. These are exact formal series in the actual
    localized chart, not realization assertions about arbitrary jets.
[^3]: Source 2, its evaluated gradient-unit identity and factor consequence.

