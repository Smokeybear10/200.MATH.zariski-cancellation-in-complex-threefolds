# Degree-five cubic-column reduction and the localized unit gate

The degree-five residual has a second explicit nice action after
localization at its invariant power-law factor. The original polynomial
slice is essential: it forces that rational nice field to fix the
inverted factor, so the field really is locally nilpotent on the
localized ring. Clearing its denominator then produces a polynomial
nice LND commuting with the original action.

When the power-law factor is a nonzero constant, this gives a complete
polynomial-kernel proof. For a nonconstant factor, the cleared action's
displayed local slice has a nonunit derivative. No global
coordinate-section or cancellation conclusion is drawn from that
localization. No novelty or expert-verification claim is made.

The subsequent [two-output closure](two-output-cubic-closure-pass40.md)
also handles nonconstant \(g\) when the constant vectors \(c,d\)
below are linearly dependent. Its additional denominator and
coordinate-descent argument is separate from the localization
proved here. The remaining degree-five case therefore has
nonconstant \(g\) and independent \(c,d\).

## 1. The actual residual and the rescaling calculation

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be an LND with
a polynomial slice \(s_*\), and let \(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2T_i=0\quad(i\le3),\qquad
\operatorname{ad}_E^4T_4=0,\qquad
V:=\operatorname{ad}_E^3T_4\ne0.
\tag{1}
\]
The residual from [pass 39](whole-frame-recognition-pass39.md) is
\[
E^5x=cg^5,\qquad E^3x_4=\lambda g^3,
\quad c\in\mathbb C^4\setminus\{0\},\quad c_4=0,
\quad \lambda\in\mathbb C^*,\quad
g\in\ker E\setminus\{0\}.
\tag{2}
\]
Here \(g\) may be constant. The known top identities give
\[
g^2\operatorname{Jac}(Ex)c=2\lambda V(x),\qquad
[E,T_i](g)=0\ (i\le3),\qquad V(g)=0.
\tag{3}
\]
The last two identities also follow from the highest coefficients
when the actual conjugated partials act on \(\exp(tE)x\).
Nothing asserts that \(g\) divides the coefficients of \(E\).

Put \(A=T_c=c\cdot\partial\). The fields \(E\) and \(V\) are
linearly independent over \(\operatorname{Frac}B\). Indeed, suppose
\(V=fE\). Evaluation on \(s_*\) makes \(f\) polynomial, and
\([E,V]=0\) gives \(E(f)=0\). Equation (3) then makes
\([E,A]=\kappa E\) for a rational \(\kappa\); evaluation on
\(s_*\) makes \(\kappa\) polynomial. The good-column bound for
\(A\) gives \(E\kappa=0\). Thus
\[
[E^5,A]=5\kappa E^5,
\qquad 0=A(cg^5)+5\kappa cg^5,
\qquad A(g)=-\kappa g.
\]
A constant partial is an LND on \(B\), so divisibility
\(g\mid A(g)\) forces \(A(g)=0\). Then \(\kappa=0\), and
(3) forces \(V=0\), a contradiction.

On \(B_g\), set \(\delta=E/g\). This is an LND of this
localized ring, with \(\delta^j x=g^{-j}E^j x\). If \(f\in\ker E\)
and \(T\) is any derivation, direct induction gives
\[
\operatorname{ad}_{fE}^kT
=f^k\operatorname{ad}_E^kT
-k f^{k-1}(\operatorname{ad}_E^{k-1}T)(f)E.
\tag{4}
\]
This is an identity of derivations, not a polynomiality assertion
about a rational multiple. Taking \(f=g^{-1}\) and using (3) gives
\[
\operatorname{ad}_\delta^2T_i=0\ (i\le3),\qquad
\operatorname{ad}_\delta^4T_4=0,
\quad
\widetilde V:=\operatorname{ad}_\delta^3T_4
=g^{-3}V+3g^{-3}E^2(T_4g)\delta\ne0.
\tag{5}
\]
Nonvanishing follows from the just-proved independence of \(E,V\).
The coordinate partials extend as derivations to \(B_g\); they are
not asserted to be LNDs there.

## 2. Full companion rows normalize the next coefficients

For this section write
\[
h_j=\delta^j x,\quad P=\delta x,\quad J=\operatorname{Jac}P,
\quad U=\operatorname{ad}_\delta^2T_4,\quad u=U(x),
\quad v=\widetilde V(x).
\]
Thus \(h_5=c\), \((h_3)_4=\lambda\), and \((h_4)_4=0\).
The last identity follows from applying \(\delta\) to the preceding
constant. The actual polynomial-in-time flow on \(B_g\) has inverse
Jacobian
\[
\mathcal C(t)=I-tJ+t^2u e_4^{\mathsf t}/2+t^3v e_4^{\mathsf t}/6.
\]
Its determinant is one: it is a unit of \(B_g[t]\), and its
specialization at zero is one. As in pass 39, the companion is
\[
M=\begin{pmatrix}J&-u/2&-v/6\\ e_4^{\mathsf t}&0&0\\0&1&0\end{pmatrix},
\qquad M^6=0,\qquad (M^j)_{1:4,1:4}=\frac{\operatorname{Jac}h_j}{j!}.
\tag{6}
\]
Both left and right kernels avoid the auxiliary plane because
\(v\ne0\). The upper-left block of \(M^5\) is zero, and its
rank is at most one. The kernel-support argument in pass 39 gives
\(M^5=0\).

Define the specific rational polynomial-in-the-localization slice
\[
\sigma=\frac{(h_2)_4}{\lambda}
=\frac{E^2x_4}{\lambda g^2},\qquad \delta\sigma=1.
\tag{7}
\]
The first four entries of the last row of \(M^4\) are
\(d(h_2)_4/2=\lambda\,d\sigma/2\). They are nonzero. Since
\(M^4\) has rank at most one, every row of
\(\operatorname{Jac}h_4/24\) is proportional to \(d\sigma\).
Evaluation on \(\delta\), using \(\delta h_4=c\), gives
\[
h_4=c\sigma+d,\qquad d\in\mathbb C^4,\quad d_4=0.
\tag{8}
\]
The assertion about constants uses the common kernel of the four
ordinary partials on \(\mathbb C(x_1,x_2,x_3,x_4)\), not a
polynomial curve-factorization theorem on an open set.

Now \(M^4\ne0\) and \(M^5=0\), so the nilpotent Jordan type
is \((5,1)\) and \(\operatorname{rank}M^3=2\). Its first four
columns contain the rows of
\(\operatorname{Jac}h_3/6\), \(\lambda\,d\sigma/2\), and
\(dP_4\). Consequently
\[
\tau=P_4-\lambda\sigma^2/2,\qquad
k=h_3-c\sigma^2/2-d\sigma
\quad\Longrightarrow\quad
\delta\tau=\delta k=0,
\quad\operatorname{rank}\operatorname{Jac}(k,\tau)\le1.
\tag{9}
\]
Indeed the full joint rank with \(\sigma\) is at most two, and
\(d\sigma(\delta)=1\) separates its row from the invariant rows.
Also \(k_4=\lambda\).

## 3. Actual good columns force an affine relation

Let \(W_i=[\delta,T_i]\), \(i\le3\). Comparing coefficients
in \((T_i+tW_i)(\exp(t\delta)x)=e_i\) gives
\[
W_i\sigma=0,\qquad
W_i\tau=-\frac\lambda2T_i\sigma,
\qquad W_i k=-\frac c4T_i\sigma.
\tag{10}
\]
For the last identity the coefficient of time degree four is
\(T_ih_4/24+W_ih_3/6=0\). For the middle identity the
fourth coordinate has degree three and the coefficient of time
degree two is \(T_i(h_2)_4/2+W_iP_4=0\). These factorials
are different from the degree-six branch.

At least one \(T_i\sigma\) is nonzero. Otherwise
\(\sigma\in\mathbb C(x_4)\). The equation \(\delta\sigma=1\)
then makes \(\delta\) a nonzero derivation preserving that
rational function field, whose constants are exactly \(\mathbb C\).
Successive integration of \(\delta^3x_4=\lambda\) gives
\[
x_4=\lambda\sigma^3/6+A\sigma^2+B\sigma+C,
\qquad A,B,C\in\mathbb C.
\]
Together with \(\sigma\in\mathbb C(x_4)\), this would imply
\(\mathbb C(x_4)=\mathbb C(\sigma)\), contradicting the degree
three of the displayed polynomial map. This argument is valid
rationally; it does not misidentify \(\sigma\) with a polynomial
in \(x_4\).

For a good index with \(T_i\sigma\ne0\), (10) gives
\(W_i\tau\ne0\). Equation (9) makes each \(dk_j\) a rational
multiple of \(d\tau\). Evaluation on this \(W_i\) identifies
that multiple as \(c_j/(2\lambda)\). Thus
\[
k=\frac{c}{2\lambda}\tau+e,
\qquad e\in\mathbb C^4,
\quad e_4=\lambda.
\tag{11}
\]
In particular \(\tau\) is nonconstant. No polynomial or rational
curve parameter has been assumed to be a coordinate.

## 4. The nice rational field and the original-slice unit lemma

The coefficients of time degrees five, four, and three in
\(\mathcal C(t)P(\exp(t\delta)x)=P\), using (8)--(11), give
\[
Jc=2\lambda v,\qquad
Jd=c/4+3\lambda u/2-\lambda\sigma v,
\]
\[
Je=c\sigma/12+d/3-\lambda\sigma u/2
       +(\lambda\sigma^2/6-2\tau/3)v.
\tag{12}
\]
Define the rational coefficient vector and derivation
\[
z=e+\frac\sigma3d+
       \left(\frac{\sigma^2}{12}+\frac{\tau}{3\lambda}\right)c,
\qquad Z=z\cdot\partial.
\tag{13}
\]
It is defined on the fraction field and preserves \(B_g\) as a
derivation. Equations (12) give
\(Jz=d/3+\sigma c/6=\delta z\), so
\[
[\delta,Z]=0,\qquad Zx_4=\lambda.
\]
Apply commutation to (7) and (9):
\[
Z\sigma=\delta^2(Zx_4)/\lambda=0,
\qquad Z\tau=\delta(Zx_4)-\lambda\sigma Z\sigma=0.
\tag{14}
\]
Hence \(Z(z)=0\), so \(Z^2x_i=0\) for the four generators.
This alone is not a proof of local nilpotence on \(B_g\): the
inverted element must be checked.

**Original-slice unit lemma.** Let \(E\) be an LND on a polynomial
ring with a polynomial slice \(s_*\), let \(0\ne g\in\ker E\),
and put \(\delta=E/g\). Suppose a derivation \(Z\) of the
fraction field has coefficients in \(B_g\), satisfies
\(Z^2x_i=0\), and commutes with \(\delta\). Then
\[
Z(g)=0,
\quad Z\in\operatorname{LND}(B_g),
\quad [E,Z]=0.
\tag{15}
\]

To prove this, the product rule first shows that every polynomial
of \(B\) has a finite \(Z\)-iterate, regardless of whether its
intermediate images lie in \(B\). In particular some iterate
kills \(g\), and some iterate kills \(s_*\). Since
\(\delta s_*=g^{-1}\), commutation makes some iterate kill
\(g^{-1}\) as well. Their formal exponential series are therefore
polynomials in time, and their product is one. Units of
\(\operatorname{Frac}(B)[t]\) are time-constant, so both
exponentials are constant and \(Zg=0\). Now every element
\(f/g^r\) has eventually zero iterates, proving actual local
nilpotence on \(B_g\). The last conclusion follows from
\(E=g\delta\).

Without the slice-commutation hypothesis, generator niceness
does not check units. For example on \(\mathbb C[a,d]_d\),
\(Z=\partial_d+(a/d)\partial_a\) has \(Z^2a=Z^2d=0\), but
\(Z^n(d^{-1})=(-1)^nn!d^{-n-1}\ne0\). This is a control
against the omitted unit check, not a residual-case example.

Applied to (13), the lemma allows a completely polynomial
commuting field. If \(q=E^2x_4\) and \(p=Ex_4\), set
\[
\mathcal W=g^4Z
=g^4T_e+\frac{g^2q}{3\lambda}T_d
 +\left(\frac{g^3p}{3\lambda}
               -\frac{q^2}{12\lambda^2}\right)T_c.
\tag{16}
\]
It is a nonzero polynomial nice LND, \([E,\mathcal W]=0\), and
\(\mathcal W(x_4)=\lambda g^4\). It is independent of \(E\)
over the fraction field, since \(\mathcal W\sigma=0\), whereas
\(E\sigma=g\ne0\). Its restriction to \(\ker E\) is a
nonzero intrinsic LND: otherwise it would be a multiple of
\(E\) on \((\ker E)[s_*]\).

## 5. Constant-factor recognition and the remaining global gate

Suppose \(g\in\mathbb C^*\). Then \(\sigma,\tau,z\) are
polynomial on \(B\), and \(Z\) is an actual polynomial LND with
the ambient-coordinate slice \(t_0=x_4/\lambda\). Its kernel
\(R\) is a genuine polynomial three-ring:
\[
B=R[t_0],\qquad
R\simeq B/(x_4)\simeq\mathbb C^{[3]}.
\]
Explicitly \(y_i=x_i-t_0z_i\), \(i\le3\), generate \(R\).
Their inverse is
\(x_i=y_i+t_0z_i(y_1,y_2,y_3,0)\),
\(x_4=\lambda t_0\), because (14) makes every coefficient
invariant under the section projection.

The restricted derivation \(\delta|_R\) is an LND with slice
\(\sigma\). Miyanishi's three-variable kernel theorem and the
slice theorem give \(K=\ker(\delta|_R)\simeq\mathbb C^{[2]}\)
and \(R=K[\sigma]\). These are precisely the established
Theorems 2.8 and 2.5 in the primary source below.[^kernel]
Also \(\delta t_0\in R\). Integrating its polynomial expansion
in \(\sigma\) gives \(H\in R\) with \(\delta H=\delta t_0\).
Then \(\xi=t_0-H\) is invariant, and
\[
B=K[\sigma,\xi],\qquad
\ker E=\ker\delta=K[\xi]\simeq\mathbb C^{[3]}.
\tag{17}
\]
This proves the complete constant-factor degree-five branch. The
final splitting is also reconstructed in the companion
[degree-six proof](cubic-degree-six-pass40.md).

For nonconstant \(g\), (13)--(16) remain valid, but (16) gives
only the nonunit derivative \(\lambda g^4\) on the displayed
coordinate. Removing a coefficient gcd does not automatically
make that derivative a unit. Nor does a slice on the localized
three-ring justify applying a global three-variable theorem to
that localized ring. These are separate missing hypotheses.

An actual four-variable control isolates the first failed inference.
On \(\mathbb C[a,b,c,d]\), take
\[
E=\partial_b,\quad g=a,\quad \delta=a^{-1}\partial_b,
\quad Z=\partial_d+(c/a)\partial_b,
\quad \sigma=ab-cd.
\]
Then \(E(b)=1\), \([\delta,Z]=0\), \(Z^2x_i=0\),
\(Zg=0\), \(Zd=1\), \(\delta\sigma=1\), and
\(Z\sigma=0\). Yet the primitive cleared field
\(aZ=a\partial_d+c\partial_b\) vanishes on the plane
\(a=c=0\), so it has no polynomial slice. Its localized
section coordinates have the genuine inverse
\(b=(\sigma+cd)/a\), with a denominator that cannot simply
be discarded. This example does not satisfy the degree-five
highest-iterate hypotheses. It refutes only the proposed inference
from the proved localized two-action and unit facts to a global
slice for the cleared field.

The remaining obligation is therefore global recognition across
\(V(g)\) using the full actual-frame data, or a different valid
coordinate repair. The later two-output proof supplies that
additional argument when \(d\in\mathbb Cc\); the independent
\(c,d\) case is still open. This note does not assert that the rational
coefficients in (13) extend to \(B\), that \(g\) is an ambient
coordinate, or that the cleared field has a polynomial slice.
No degree-five nonpolynomial example is constructed.

## Verification and source scope

The rescaling identity, original-slice unit lemma, good-column
affine relation and coefficient construction were independently
reconstructed by the main agent and the other active algebra
auditor during this pass. These are AI proof audits, not expert
review. The [standalone checker](cubic_degree_five_checks_pass40.py)
imports only `unittest` and `sympy`. Its first run passed all five
methods in 0.461 seconds. It checks nonzero higher rescaling
corrections, the missing-unit negative control, the actual
four-variable localized section and its inverse, and the exact
denominator-clearing coefficients. It neither constructs a full
degree-five residual example nor proves the universal matrix-rank
or localization quantifiers.

[^kernel]: Nikhilesh Dasgupta and Sergey Gaifullin,
[*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510),
Theorem 2.5 on PDF p. 5 and Theorem 2.8 on PDF p. 6, both
complete statements directly read in this pass. The three-variable
kernel result is explicitly attributed there to Miyanishi. Here it
is used only for the actual global ring \(R\simeq\mathbb C^{[3]}\)
in the constant-factor case.
