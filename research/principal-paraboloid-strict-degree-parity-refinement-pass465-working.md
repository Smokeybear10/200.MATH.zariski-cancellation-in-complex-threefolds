# Strict degree ratio: an even sigma degree and an exact half-degree remainder

Working necessary refinement: retain the complete actual264 chart in
the nonlinear first-slope sector k=s+f, f_s=0, n_ss nonzero and
f''' nonzero. In the strict alternative of460/461, suppose
a=deg(sigma)>1. Then a is even. More precisely, with the exact
centered generators and shear z=x-eta*q from461, there are coefficient
units lambda and kappa such that
\[
\begin{gathered}
z=\lambda P+S,\qquad P=\sigma,\qquad \deg S=a/2,\\
q=-P^2+R,\qquad \deg R=3a/2,\qquad
\lambda=\frac{t_3}{2\eta},\qquad t_3=f'''/6,\\
\deg_v\{\theta+\sigma^2+f'\sigma\}=3a/2.
\end{gathered}
\tag{1}
\]
The complete fourth potential also forces the coefficient identities
below, including f''''/f'''=8eta and t3/eta^4 in C*.

The remaining half-degree case is not excluded. This note does not
bound a, settle the balanced ratio, recover an original coordinate
or recognize the invariant ring.

## 1. Entire actual input and the exact strict equations

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md)
and the arbitrary-n formulas of
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md).
In particular
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE weighted initial kernel},\\
X=a_0u+x_0,\quad a_0\in L^*,\quad x_0\in A,\qquad
N=[u^4]\partial_Z|_A\ne0,\\
L=\operatorname{Frac}\ker_A N,\qquad [L:\mathbb C(t,s)]<\infty,
\qquad Nv=1,\\
O=L[A]=L[v]=L[y,\sigma,\theta],\qquad
\operatorname{Frac}A=L(v)=\mathbb C(y,z_{\rm int},w_{\rm int}),\\
\det\frac{\partial(Y,Z,W)}{\partial(t,s,v)}=-a_0^4\in L^*.
\end{gathered}
\tag{2}
\]
The notation z_int,w_int distinguishes the original intercepts from
the shear variable z below. All selected-partial, localization,
original-slice and return conditions remain retained. In particular
the original slice is not replaced by X/a0.

The exact coefficient partials commute and have joint constants C.
Let mathbb F=ker_L(partial_s), finite over C(t), and assume
\[
k=s+f,\quad f\in\mathbb F,\qquad e=n_{ss}\ne0,\qquad
f'''\ne0,\qquad a=\deg_vP>1,\quad P=\sigma.
\tag{3}
\]
No rationality of mathbb F or L is assumed. All intrinsic degrees
refer to v, with coefficients in L.

Use the exact affine centerings from
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md):
\[
x=y+\frac{(f''-2\nu)P+n_t-\nu f'}2,\qquad
q=\theta+\frac{bP-C_0}{e},\qquad
\nu=n_s,\quad b=n_{ts},\quad C_0=\ell_s+\nu^2.
\tag{4}
\]
In the STRICT alternative 2r>3a, the result of
[461](principal-paraboloid-strict-nonlinear-degree-ratio-pass461-working.md)
gives
\[
\begin{gathered}
\deg_vx=\deg_vq=\deg_vy=\deg_v\theta=r=2a,\qquad
\eta=\frac{\operatorname{lc}_v x}{\operatorname{lc}_v q}\in L^*,\\
e=-2\eta^2,\quad e_t=-8\eta^3,\quad e_s=0,\qquad
\eta_t=2\eta^2,\quad \eta_s=0,\\
z=x-\eta q,\qquad \deg_vz=a,\qquad
O=L[z,P,q].
\end{gathered}
\tag{5}
\]
The derivative identities for eta are the strict460 identities.
The degree of z follows from461's equality deg(z)+r=3a.
The shear is over L only, not an original complex coordinate change.

The entire third and fourth levels of461 are
\[
\mathcal H=z^2+2\eta zq+T(P)=0,\qquad
T(P)=t_3P^3+t_2P^2+t_1P+t_0,\qquad t_3=f'''/6\ne0,
\tag{6}
\]
\[
\boxed{\Psi=Cq^2+B(P)q+zT'(P)-\frac{D(P)}{2\eta}z^2
                              +\mathcal F(P)=0,}
\tag{7}
\]
where
\[
\begin{aligned}
B(P)&=B_2P^2+B_1P+B_0,\qquad D(P)=d_0+4\eta^2P,\\
\mathcal F(P)&=F_4P^4+F_3P^3+F_2P^2+F_1P+F_0,\qquad
F_4=f''''/24-2\eta t_3.
\end{aligned}
\tag{8}
\]
All letters C,Bj,d0,Fj,tj are the exact coefficient elements defined
by461(8)--(10), not free replacements for a genuine potential.
In particular C here is a scalar coefficient, not the complex field.
The prime on T in(7) denotes its FORMAL P-derivative. Coefficient
derivatives are always written with t or s subscripts.

The invertible shear and subtraction of D(P)*Hcal/(2eta) used in461
preserve the evaluated gradient-minor unit. Whole generation
O=L[z,P,q] makes the tangent (z',P',q') unimodular: differentiate a
polynomial expression for v in those three elements. The primitive
tangent argument therefore gives
\[
\begin{aligned}
W&:=(\mathcal H_z\Psi_q-\mathcal H_q\Psi_z)_{\rm ev}
    =-\psi P',\qquad \psi\in L^*,\\
\deg_vW&=a-1.
\end{aligned}
\tag{9}
\]
The primes in(9) are intrinsic derivatives fixing L. The complete
minor, with every term of(7) retained before differentiation, is
\[
\boxed{W=4Czq+4\eta Cq^2+2B(P)z+2\eta B(P)q
                     -2\eta zT'(P)+2D(P)z^2.}
\tag{10}
\]
The polynomial Fcal has no z or q derivative, but it remains present
in the fourth level(7).

## 2. A constant first remainder would contradict whole generation

Since deg(z)=deg(P)=a, define
\[
\lambda=\frac{\operatorname{lc}_v z}{\operatorname{lc}_v P}\in L^*,
\qquad z=\lambda P+S,\qquad \deg_vS<a.
\tag{11}
\]
Suppose first that S belongs to L, including S=0. The nonzero
polynomial z is then in L[P], and(6) gives
q=-(z^2+T(P))/(2eta*z) in L(P). Since q also belongs to L[v],
it belongs to L[P].

Here is the elementary intersection justification, so this step
does not assume a normal projected ring. For any nonconstant P(v),
\[
L(P)\cap L[v]=L[P].
\tag{12}
\]
Write an element of the intersection as A(P)/B(P) with A,B coprime
in the polynomial ring L[P]. The Euclidean algorithm supplies
I(P)A(P)+J(P)B(P)=1. Since B(P(v)) divides A(P(v)) in L[v],
it then divides 1. Hence B(P(v)) is a unit. As P is nonconstant,
this forces B constant, proving(12). Equivalently in the present
linear-denominator case, polynomial division by lambda*P+S leaves
a coefficient remainder, which must vanish for the quotient to
be polynomial in v.

Now z and q are both in L[P]. The WHOLE ring return O=L[z,P,q]
would give O=L[P]. A polynomial expression for v in P then has
degree 1=a*deg(expression), so a=1. This contradicts(3).
Consequently
\[
\boxed{c:=\deg_vS\text{ is an integer with }0<c<a.}
\tag{13}
\]
No division by an evaluated polynomial was promoted to a ring
identity without the intersection proof.

## 3. The second remainder has exact degree a+c

Define the coefficient unit kappa and the lower remainder R by
\[
\kappa=\frac{\operatorname{lc}_v q}{(\operatorname{lc}_vP)^2}\in L^*,
\qquad q=\kappa P^2+R,\qquad \deg_vR<2a.
\tag{14}
\]
The degree-3a part of(6) gives
\[
2\eta\lambda\kappa+t_3=0.
\tag{15}
\]
After that cancellation the ENTIRE relation is
\[
2\eta\lambda PR+2\eta\kappa P^2S+2\eta SR+
             (\lambda P+S)^2+t_2P^2+t_1P+t_0=0.
\tag{16}
\]
If deg(R)>a+c, the PR term is uniquely highest: a>c makes it
higher than SR, and the assumed inequality makes it higher than
P^2S and all terms of degree at most2a. If deg(R)<a+c, including
R=0, then P^2S is uniquely highest, because c>0.
Both are impossible. Thus
\[
\boxed{\deg_vR=a+c,\qquad
\deg_v\!\left(R+\frac{\kappa}{\lambda}PS\right)<a+c.}
\tag{17}
\]
The second statement is the leading-coefficient cancellation in(16).
In particular R is nonzero. Neither P nor S is assumed monic.

## 4. Top fourth and minor degrees eliminate three coefficients

The degree-4a terms of the full fourth level(7) are exactly
Cq^2, B2*P^2*q and F4*P^4. The degree-4a terms of W are exactly
4eta*Cq^2 and 2eta*B2*P^2*q. Their coefficients, after dividing
by the appropriate nonzero leading powers of P, give
\[
C\kappa^2+B_2\kappa+F_4=0,\qquad
4\eta C\kappa^2+2\eta B_2\kappa=0.
\tag{18}
\]
Every other term in either comparison has degree at most3a.
These equations allow C=0 and force, without dividing by C,
\[
B_2=-2C\kappa,\qquad F_4=C\kappa^2.
\tag{19}
\]

Substitute B2=-2C*kappa and q=kappa*P^2+R into(10).
The entire C-dependent part becomes
\[
4CR(z+\eta q)
=4\eta C\kappa P^2R+4CzR+4\eta CR^2.
\tag{20}
\]
If C were nonzero, its first term would have degree3a+c.
The other two degrees are2a+c and2a+2c, both smaller because
c<a. All terms independent of C have degree at most3a, also
smaller because c>0. Thus the displayed first term is uniquely
highest and has nonzero leading coefficient, contradicting(9).
It follows that
\[
\boxed{C=B_2=F_4=0.}
\tag{21}
\]

The coefficient identity for F4 in(8) now gives
\[
f''''/f'''=8\eta.
\tag{22}
\]
Indeed f''''=48eta*t3 and f'''=6t3. Therefore
(t3)_t=8eta*t3. Combined with eta_t=2eta^2 and the vanishing
s-derivatives in(5), both exact derivatives of t3/eta^4 vanish.
The joint constants of L are C, so
\[
\boxed{t_3/\eta^4\in\mathbb C^*.}
\tag{23}
\]
This uses exact joint constants, not rationality of mathbb F.

## 5. The next two minor degrees fix lambda, kappa and B1

After(21), the degree-3a terms of(10) give
\[
B_1\kappa=3t_3\lambda-4\eta\lambda^2.
\tag{24}
\]
To inspect the next degree without losing a possible tie, substitute
z=lambda*P+S and q=kappa*P^2+R. The only terms of degree2a+c
after the preceding cancellation are
2eta*B1*PR, -6eta*t3*P^2*S and16eta^2*lambda*P^2*S.
For example P*S^2 has degree a+2c<2a+c. All remaining terms
have degree at most max(2a,a+2c)<2a+c. By(17) the coefficient relative to
the leading term of P^2*S is
\[
-\frac{2\eta B_1\kappa}{\lambda}-6\eta t_3+16\eta^2\lambda
=12\eta(2\eta\lambda-t_3),
\tag{25}
\]
where(24) was used in the equality. Degree2a+c is greater than
a-1, so this coefficient must vanish. All its divided coefficients
are nonzero by(5),(11),(15). Therefore
\[
\boxed{\lambda=\frac{t_3}{2\eta},\qquad
\kappa=-1,\qquad B_1=-2\eta\lambda^2.}
\tag{26}
\]
In particular lambda also belongs to mathbb F*. This argument
does not assume that the lower remainder R equals its leading
approximation in(17); only that exact leading cancellation is used.

## 6. The complete zW expansion and the half-degree tie

With(21),(26), write
\[
B(P)=-2\eta\lambda^2P+B_0,\qquad
T(P)=2\eta\lambda P^3+t_2P^2+t_1P+t_0,\qquad
D(P)=d_0+4\eta^2P.
\tag{27}
\]
Multiply the exact W in(10) by z and use only the third relation
2eta*z*q=-z^2-T(P). This gives the entire identity
\[
\boxed{zW=B(P)z^2-B(P)T(P)-2\eta z^2T'(P)+2D(P)z^3.}
\tag{28}
\]
Before imposing the third level, the difference between its two
sides is exactly B(P)*Hcal. In particular no lower coefficient
was discarded in this elimination.

Substitute z=lambda*P+S. The FULL expansion is
\[
zW=K_3P^3+K_2(S)P^2+K_1(S)P+K_0(S),
\tag{29}
\]
where
\[
\begin{aligned}
K_3={}&-2\lambda\{\eta B_0-d_0\lambda^2
                           +\eta\lambda^3+\eta\lambda t_2\},\\
K_2(S)={}&12\eta^2\lambda S^2
 +(6d_0\lambda^2-4\eta\lambda^3-8\eta\lambda t_2)S
 +B_0\lambda^2-B_0t_2,\\
K_1(S)={}&8\eta^2S^3
 +(6d_0\lambda-2\eta\lambda^2-4\eta t_2)S^2
 +(2B_0\lambda-4\eta\lambda t_1)S
 +2\eta\lambda^2t_0-B_0t_1,\\
K_0(S)={}&2d_0S^3+(B_0-2\eta t_1)S^2-B_0t_0.
\end{aligned}
\tag{30}
\]
The symbol K3 in this expansion is new notation for the displayed
coefficient, not the earlier lower fourth polynomial in461.
The coefficients of P^2*S^2 and P*S^3 are exactly
12eta^2*lambda and8eta^2, both nonzero.

Equations(29),(30) are polynomial identities evaluated in O.
We do NOT assume P and S algebraically independent. The following
argument compares intrinsic degrees of their evaluated terms.
Since deg(z)=a and deg(W)=a-1,
\[
\deg_v(zW)=2a-1.
\tag{31}
\]

Suppose c>a/2. The term12eta^2*lambda*P^2*S^2 has degree2a+2c.
It exceeds3a, the degree of a nonzero K3*P^3. It also exceeds
a+3c because c<a, and exceeds every other term in(30).
Its leading coefficient cannot vanish. It is therefore uniquely
highest, contradicting(31).

Suppose instead c<a/2. The only possible degree-3a term in(29)
is K3*P^3: all terms in K2(S)*P^2 have degree at most2a+2c<3a,
and those in K1(S)*P have degree at most a+3c<3a. Since
3a>2a-1, it follows that K3=0. After this forced vanishing,
12eta^2*lambda*P^2*S^2 is uniquely highest. Its degree2a+2c
exceeds a+3c because c<a, and exceeds the degrees of all its
remaining competitors. Again it exceeds2a-1 and has nonzero
coefficient, contradicting(31).

These two cases exhaust every possibility except
\[
\boxed{c=a/2,\qquad a\text{ is even}.}
\tag{32}
\]
The equality case is deliberately retained: K3*P^3 and the displayed
P^2*S^2 term then have the SAME degree3a and may cancel. The proof
does not discard that tie or assert that the lower comparisons close it.

## 7. Exact surviving degrees and scope

Combining(17),(26),(32),
\[
\deg_vS=a/2,\qquad q=-P^2+R,\qquad
\deg_vR=3a/2,\qquad
\deg_v(R-\lambda^{-1}PS)<3a/2.
\tag{33}
\]
By(4), the original combination zeta=theta+P^2+f'P differs from
R=q+P^2 by an affine polynomial in P. Since3a/2>a, this correction
cannot change its degree. Thus the last assertion in(1) is exact.
No field-valued coefficient was used as an original complex coordinate.

The complete current460 and461 inputs were read before using their
strict equations. Fresh unsaved28b0d8 independently reconstructed
the entire C-dependent remainder(20), the coefficient reduction(25),
the exact off-level difference B(P)*Hcal in(28), and EVERY term
of the expansion(29),(30). All residuals were zero.
The polynomial intersection, degree alternatives and unique-leading
arguments are the written proofs above, not conclusions of finite
numerical enumeration.

All actual264/296/458/460/461 pedigree remains retained. No recursive
certification of every earlier recognition note is claimed.
This result only refines the strict r=2a branch with a>1.
It proves neither a finite upper bound nor exclusion of the surviving
even degrees, and does not settle the balanced r=3a/2 branch.

No saved checker was executed, imported, compiled or rerun.
Only this newly assigned note was created; no earlier source or
canonical file was changed. No unrestricted cancellation, original
chart-entry, realization, historical novelty or formal-certification
claim is made.
