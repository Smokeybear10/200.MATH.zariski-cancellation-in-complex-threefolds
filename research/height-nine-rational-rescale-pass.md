# Rational rescaling closes the higher power-law branches

This note gives a closure argument for the power-law residual with
highest flow degree \(m=3\) or \(m=4\). The quadratic case has a direct
polynomial shear in [height-nine-power-law-pass.md](height-nine-power-law-pass.md).
The argument below supplies an ambient invariant coordinate, using the
three-variable single-partial lemma already proved in
[height-seven-audit.md](height-seven-audit.md). For a slice derivation,
regular-kernel recognition then gives a polynomial three-ring kernel.

The completed argument was independently reconstructed in
[the rational-rescale audit](height-nine-rational-rescale-independent-audit.md).
The [post-proof overlap check](mixed-commutator-postproof-literature.md)
identifies earlier literature for the rational Burgers formula, without
claiming novelty of the mixed-action recognition theorem.

The new issue is a rational Burgers equation. Its poles cannot simply be
discarded or assumed to divide a lower iterate with the desired order.
We classify the rational solution, rule out its positive-weight branch
using the slice, and clear the remaining plane denominators by an
invariant factor. The statement is a bounded mixed-commutator theorem,
not a reduction of every slice derivation to this frame.

## 1. Hypotheses and the invariant rescaling

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(E\) be an LND with a
polynomial slice \(s_*\), and set \(T_i=\partial_{x_i}\). Assume
\[
\operatorname{ad}_E^2T_i=0\quad(i\le3),\qquad
\operatorname{ad}_E^3T_4=0.
\tag{1}
\]
Suppose, for \(m\in\{3,4\}\), that
\[
E^m(x)=c g^m,\qquad E^{m-1}(x_4)=\lambda g^{m-1},\qquad E(g)=0,
\tag{2}
\]
where \(g\in B\setminus\{0\}\), \(c\in\mathbb C^4\setminus\{0\}\),
\(c_4=0\), and \(\lambda\in\mathbb C^*\). The nonconstant \(g\) case
is the residual of interest. Put
\[
W_i=[E,T_i],\qquad V=[E,[E,T_4]],\qquad A=c\cdot\partial_x.
\]
Coefficient extraction from the conjugated partials applied to the flow
gives \(W_i(E^m x)=0\) for \(i\le3\) and \(V(E^m x)=0\), as in
[the zero-top pass, Section 2](height-nine-zero-top-pass.md).
At least one component of \(c\) is nonzero, so (2) implies
\[
W_i(g)=0\quad(i\le3),\qquad V(g)=0.
\tag{3}
\]
In particular, \(E(T_i g)=0\) for \(i\le3\), and
\(E^2(T_4g)=0\).

Work temporarily in \(B_g\), and define
\[
\delta=g^{-1}E.
\]
This is an LND of \(B_g\), since
\(\delta^j f=g^{-j}E^j f\). It has
\[
\delta^m(x)=c,\qquad \delta^{m-1}(x_4)=\lambda.
\tag{4}
\]
The constant partials extend to derivations of \(B_g\), but need not
be LNDs there. No highest-coefficient LND assertion for those localized
partials will be used.

For any derivation \(T\) and any \(f\in\ker E\), direct expansion gives
\[
\operatorname{ad}_{fE}^2T
=f^2\operatorname{ad}_E^2T-2f[E,T](f)E.
\tag{5}
\]
Taking \(f=g^{-1}\) and using (3) proves
\[
\operatorname{ad}_{\delta}^2T_i=0\quad(i\le3),\qquad
\widetilde V:=\operatorname{ad}_{\delta}^2T_4
=g^{-2}V+2g^{-3}W_4(g)E.
\tag{6}
\]
Here \(E(W_4g)=Vg=0\). Together with \(Vg=0\) and \([E,V]=0\),
this shows \([\delta,\widetilde V]=0\). Thus the mixed bracket
identities survive rescaling, including the fourth triple bracket.

The slice gives a useful exact primitivity statement in every polynomial
coordinate system \(y\):
\[
1=E(s_*)=\sum_j\frac{\partial s_*}{\partial y_j}E(y_j).
\tag{7}
\]
Consequently, if a rational function \(q\) has \(qE(y_j)\in B\) for
all \(j\), then \(q\in B\). This uses the unit derivative ideal,
not the false assertion that multivariable gcd one implies a unit ideal.

## 2. Constant-top reduction over the localization

Write \(J_\delta=\operatorname{Jac}(\delta x)\) and
\(\widetilde v=\widetilde V(x)\). The conjugation identities give
\[
C_\delta(t)=I-tJ_\delta+\frac{t^2}{2}\widetilde v e_4^{\mathsf T}
=\operatorname{Jac}(\exp(t\delta)x)^{-1}.
\tag{8}
\]
Its determinant is one. One direct justification is
\(\operatorname{div}\delta=g^{-1}\operatorname{div}E-g^{-2}E(g)=0\):
an LND of the polynomial ring has zero divergence, and the usual flow
Jacobian differential equation remains valid on the localization.
Only derivation and Jacobian algebra is used here.

First consider \(\widetilde v=0\). The top coefficient in
\(C_\delta(t)(\delta x)(\exp(t\delta)x)=\delta x\), together with
(4), gives \(J_\delta c=0\). Hence \([A,\delta]=0\), and
\[
[A,E]=\frac{A(g)}gE.
\]
Both fields on the left are polynomial. Equation (7) makes \(A(g)/g\)
polynomial. Since \(A\) is a constant partial up to a linear coordinate
change, \(g\mid A(g)\) forces \(A(g)=0\). Thus \(A\) is a nonzero
constant translation commuting with \(E\). A good constant direction
independent of \(A\) descends to a coordinate partial on \(\ker A\cong
\mathbb C^{[3]}\), so the three-variable lemma closes this branch.

Now assume \(\widetilde v\ne0\). Form
\[
M=\begin{pmatrix}J_\delta&-\widetilde v/2\\e_4^{\mathsf T}&0\end{pmatrix}.
\]
Block elimination gives \(\det(I-tM)=\det C_\delta(t)=1\), hence
\(M^5=0\) over \(\operatorname{Frac}B\). Moreover,
\[
(M^j)_{\mathrm{upper\ left}}=\frac1{j!}\operatorname{Jac}(\delta^j x).
\tag{9}
\]
For clarity, the needed rank descent is purely matrix algebra. If
\(M^{j+1}=0\), \(\operatorname{rank}M^j\le1\), and its upper-left
four-by-four block vanishes, a nonzero factorization \(M^j=uv^{\mathsf T}\)
would force either \(u\) or \(v\) to be supported on its fifth entry.
The relations \(MM^j=M^jM=0\) would then contradict respectively
\(Me_5=(-\widetilde v/2,0)\ne0\) or
\(e_5^{\mathsf T}M=(e_4^{\mathsf T},0)\ne0\).
Thus \(M^j=0\).

In dimension five, \(M^5=0\) gives \(\operatorname{rank}M^4\le1\).
Since \(\delta^4x\) is constant for \(m=4\), and zero for \(m=3\),
the descent gives \(M^4=0\), then \(\operatorname{rank}M^3\le1\).
For \(m=3\), the constant \(\delta^3x\) gives \(M^3=0\) and
\(\operatorname{rank}M^2\le1\). In both cases,
\[
\operatorname{rank}\operatorname{Jac}(\delta^{m-1}x)\le1.
\tag{10}
\]

On the open variety \(\operatorname{Spec}B_g\), the map
\(H=\delta^{m-1}x\) satisfies \(\delta H=c\ne0\). Its image closure
is an irreducible curve by (10), and each flow orbit maps onto an entire
affine line parallel to \(c\). Therefore that closure is one affine
line. Taking a constant linear functional nonzero on \(c\) gives
\[
H=c\eta+d,\qquad \eta\in B_g,\quad\delta\eta=1,
\quad d\in\mathbb C^4.
\]
This does not assert that \(\eta\) is polynomial on all of affine four-space.

Put \(q=\delta^{m-2}x_4\), and write \(r=m-1\). Further coefficients
in (8) and its inverse give
\[
J_\delta c=\frac{r\lambda}{2}\widetilde v,
\qquad J_\delta H=\frac cr+\frac{r-1}{2}q\widetilde v,
\qquad J_\delta\operatorname{Jac}H
=\frac r2\widetilde v\operatorname{Jac}q.
\tag{11}
\]
Substituting \(H=c\eta+d\) shows
\(\operatorname{Jac}(q-\lambda\eta)=0\); this rational function is
constant. After adjusting \(d\), set
\[
\sigma=\frac q\lambda
=\frac{E^{m-2}x_4}{\lambda g^{m-2}},\qquad
H=c\sigma+d,
\qquad d_4=\lambda,
\qquad J_\delta d=\frac cr-\frac{\lambda\sigma}{2}\widetilde v.
\tag{12}
\]
In particular \(\delta\sigma=1\) and \(E\sigma=g\in B\).

Let \(B_0=d\cdot\partial_x\). The rational vector field
\[
D_0=rB_0+\sigma A
\tag{13}
\]
commutes with \(\delta\), by (11)-(12). Also
\(D_0x_4=r\lambda\). Since \(m\ge3\), commutation and (12) give
\[
D_0\sigma=\lambda^{-1}\delta^{m-2}(D_0x_4)=0.
\tag{14}
\]
The constant fields \(A,B_0\) are independent because
\(c_4=0\) and \(d_4=\lambda\ne0\). Choose linear coordinates
\((a,b,z_1,z_2)\) with
\[
A=\partial_a,\qquad B_0=\partial_b,\qquad x_4=\lambda b.
\]
Then (14) is the rational Burgers equation
\[
r\sigma_b+\sigma\sigma_a=0.
\tag{15}
\]

## 3. Classification of the rational Burgers denominator

Let \(R=\mathbb C[z_1,z_2]\), so \(B=R[a,b]\). Write
\(\sigma=N/D\) in reduced form, with nonzero coprime polynomials
\(N,D\in R[a,b]\). Clearing \(D^3\) in (15) gives
\[
rD(N_bD-ND_b)+N(N_aD-ND_a)=0.
\tag{16}
\]
Reducing modulo \(D\) gives \(D\mid N^2D_a\). Coprimality, with
all irreducible multiplicities retained, implies \(D\mid D_a\).
Degree in \(a\) forces \(D_a=0\).
Divide (16) by \(D\) and reduce modulo \(N\). This gives
\(N\mid rD N_b\), hence \(N\mid N_b\) and \(N_b=0\).
The remaining equation is \(N_a=rD_b\). Its left side depends only
on \((a,z)\), and its right side only on \((b,z)\), so
\[
N=\alpha(z)a+\beta(z),\qquad
D=\frac{\alpha(z)}r b+\gamma(z),
\qquad \alpha,\beta,\gamma\in R.
\tag{17}
\]
No squarefreeness assumption was used.

Next \(E\sigma=g\) gives
\[
D E(N)-N E(D)=gD^2.
\]
Reduction modulo \(D\), again using the full gcd, yields \(D\mid E(D)\).
For an LND on a domain of characteristic zero, divisibility
\(f\mid E(f)\) implies \(E(f)=0\): otherwise the additive LND degree
on products conflicts with \(\deg_E E(f)=\deg_E f-1\).
Thus
\[
E(D)=0,\qquad E(N)=gD.
\tag{18}
\]
The displayed expression for \(\sigma\) in (12) also gives
\[
D\mid g^{m-2}\quad\text{in }B.
\tag{19}
\]
This is the only denominator divisibility inferred from the original
lower iterate. It does not assume that the quotient in (12) is polynomial.

## 4. The nonzero slope forces a fixed locus

Clear the denominator of (13):
\[
Z=D D_0=N\partial_a+rD\partial_b.
\tag{20}
\]
This is polynomial. Equations (13) and (18) imply \([\delta,Z]=0\),
so
\[
[E,Z]=-\frac{Z(g)}gE,\qquad [Z,E]=\frac{Z(g)}gE.
\tag{21}
\]
Equation (7) shows that \(\rho=Z(g)/g\) belongs to \(B\).

Suppose \(\alpha\ne0\). In this case
\[
Z=(\alpha a+\beta)\partial_a+(\alpha b+r\gamma)\partial_b.
\]
Let \(n=\deg_{a,b}g\). Because \(D\) is genuinely linear in \(b\)
and divides \(g^{m-2}\), equation (19) forces \(n\ge1\).
The derivation \(Z\) does not increase total \((a,b)\)-degree, and its
action on the highest homogeneous part of \(g\) is multiplication by
\(n\alpha\). Comparing degrees and leading parts in \(Zg=\rho g\)
therefore gives
\[
\rho=n\alpha.
\tag{22}
\]
Applying (21) to \(g\), using \(Eg=0\), yields \(E\rho=0\), hence
\(E\alpha=0\).

Localize at \(\alpha\), and center the two coordinates:
\[
a'=a+\frac\beta\alpha,\qquad b'=b+\frac{r\gamma}\alpha.
\]
Then \(B_\alpha=R_\alpha[a',b']\) and
\(Z=\alpha\mathcal E\), where
\(\mathcal E=a'\partial_{a'}+b'\partial_{b'}\). Since \(E\alpha=0\),
(21)-(22) give
\[
[\mathcal E,E]=nE.
\tag{23}
\]
The shifts may have nonzero \(E\)-derivatives; equation (23) already
includes them and does not assume \(E\beta=E\gamma=0\).

In the \((a',b')\)-grading, (23) makes \(E(z_i)\) homogeneous of
degree \(n\), and \(E(a'),E(b')\) homogeneous of degree \(n+1\).
All these coefficients lie in the proper ideal \((a',b')\) of
\(R_\alpha[a',b']\), while \(E(\alpha^{-1})=0\). Thus
\[
E(B_\alpha)\subseteq(a',b').
\]
This contradicts \(E(s_*)=1\). The contradiction is scheme-theoretic
and does not require choosing a point or proving a coefficient map
surjective. Consequently
\[
\alpha=0,\qquad N,D\in R.
\tag{24}
\]

## 5. A constant denominator gives a polynomial commuting partial

If \(D\in\mathbb C^*\), then \(\sigma\in R\) and
\(D_0=r\partial_b+\sigma(z)\partial_a\) is a polynomial nice LND.
Since \([D_0,E]=(D_0g/g)E\), equation (7) makes \(D_0g/g\) polynomial.
LND divisibility now gives \(D_0g=0\), so \([D_0,E]=0\).

The actual polynomial change
\[
q_0=a-\frac b r\sigma(z),\qquad (b,z_1,z_2)\text{ unchanged}
\]
has polynomial inverse and gives
\(D_0=r\partial_b\), \(A=\partial_{q_0}\).
Hence \(E\) preserves the coordinate three-ring
\(\mathbb C[q_0,z_1,z_2]\), and its surviving constant partial
\(\partial_{q_0}\) still satisfies the good double bracket.
The three-variable lemma produces an ambient invariant coordinate.
If the restriction of \(E\) is zero, the whole coordinate three-ring
is invariant, which is an even simpler closing case.

## 6. A nonconstant plane denominator gives a plane LND

Suppose instead that \(D\in R\setminus\mathbb C\). Equations (18)
show that \(N,D\) are algebraically independent: if they were dependent,
\(N\) would be algebraic over \(\mathbb C(D)\), and a derivation
killing \(D\) would kill \(N\) in characteristic zero, contradicting
\(E(N)=gD\ne0\).

The plane Jacobian of \((N,D)\) is therefore nonzero. Solving the
two equations
\[
\delta N=D,\qquad \delta D=0
\]
for \(\delta z_1,\delta z_2\) gives
\[
\delta z_i\in\operatorname{Frac}R.
\tag{25}
\]
Choose a common reduced denominator \(h\in R\setminus\{0\}\) and
write
\[
\delta z_i=p_i/h,\qquad p_i\in R,\qquad\gcd(h,p_1,p_2)=1.
\]
The gcd condition means that for every irreducible factor \(\pi\)
of \(h\), at least one numerator is not divisible by \(\pi\).
Irreducibles of the UFD \(R\) remain prime in \(R[a,b]\).
Since \(E(z_i)=g p_i/h\in B\), valuation at each such \(\pi\),
including its multiplicity in \(h\), implies
\[
h\mid g\quad\text{in }B.
\tag{26}
\]
As \(g\in\ker E\), factorial closure of an LND kernel gives
\(E(h)=0\). Equivalently \(\delta h=0\).

Define on the polynomial plane
\[
\Delta=h\delta|_R.
\]
Its coefficients \(p_1,p_2\) are polynomial. It is nonzero because
\(\Delta N=hD\ne0\). For every \(f\in R\), the commuting invariant
factors give
\[
\Delta^j f=h^j\delta^j f=h^j g^{-j}E^j f.
\tag{27}
\]
The last expression vanishes for all sufficiently large \(j\), since
\(E\) is an LND. Thus \(\Delta\) is an actual polynomial LND of
\(R=\mathbb C[z_1,z_2]\), not merely a rational vector field.

Rentschler's plane theorem, in the exact form recalled by
[Dasgupta and Gaifullin, Theorem 2.7](https://arxiv.org/pdf/2306.00510),
gives a coordinate \(p\) of \(R\) with \(\Delta p=0\). Equation (27)
for \(j=1\) then gives \(Ep=0\). Since \(p\) is a plane coordinate,
it is also an ambient coordinate of \(B\).

## 7. Kernel recognition and a primitive cubic control

Both branches of (24), and the earlier \(\widetilde v=0\) branch,
produce an ambient coordinate \(p\in\ker E\). The slice theorem gives
\(B=(\ker E)[s_*]\), so \(\ker E\) is Noetherian and regular.
Apply [Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
to the \(\mathbb C[p]\)-LND on \(B=\mathbb C[p]^{[3]}\). It follows
that
\[
\ker E=\mathbb C[p]^{[2]}\cong\mathbb C^{[3]}.
\]
This final step is an application of an existing regular-kernel theorem.

There is a nonempty primitive cubic control. In physical coordinates
\((a,b,c,w)\), set
\[
D_*=\partial_a+a\partial_b+(b+a^2/2)\partial_c,
\qquad f=c-ab+a^3/6,
\qquad E=fD_*+\partial_w.
\]
One has \(D_*f=0\), \(Ew=1\), and
\[
E^3x=2f^3e_c,\qquad E^2b=f^2.
\]
The partials in \(a,c,w\) are good, while
\(\operatorname{ad}_E^2\partial_b=2fD_*\ne0\) and the next bracket
vanishes. After rescaling,
\[
\delta=D_*+f^{-1}\partial_w,\qquad
\operatorname{ad}_{\delta}^2\partial_b=-2f^{-2}\partial_w\ne0,
\qquad \delta^2x=(0,1,2a,0).
\]
Here \(\sigma=a\) and \(D_0=2(\partial_b+a\partial_c)\) commutes
with both \(\delta\) and \(E\). Sixteen inline exact symbolic checks
verified these identities in 0.163 seconds. They check this control,
not the all-parameter denominator or invariant-coordinate arguments.

The combined quadratic shear and rational-rescale proofs close the
power-law residual in flow degrees two, three, and four, subject to the
stated mixed-commutator hypotheses and the previously proved
three-variable single-partial lemma. They do not supply a general
reduction of arbitrary slice derivations to height at most nine, and
they make no novelty or peer-review claim.
