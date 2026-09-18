# A power-of-f local-slice multiplier and its two finite corrections

The nonunit multiplier \(a=f^e\), \(e\ge1\), does not destroy the
polynomial-kernel conclusion for the pass-18 bases. It does destroy the
uncorrected reverse formula. The repair first changes the new local-slice
polynomial \(Q\) through a finite jet, and then changes the old polynomial
\(P\) through the pass-19 curve reparametrization. These are distinct
corrections with distinct divisibility obligations.

The all-slice theorem first concerns powers of the already controlled
invariant \(f\). A coefficient-explicit extension then permits arbitrary
nonzero multipliers \(a(f)\), with all-slice coverage also proved for
\(a=f-1,Q=h\). It does not cover every slice extension for every
multiplier, all local-slice constructions, or cancellation. This is a
working algebraic proof; mathematical priority and external expert review
remain outstanding.
The [standalone six-method checker](nonunit_local_slice_checks_pass20.py)
passed in 0.559 seconds. Its independently re-evaluated inverse is a
bounded check of the two corrections, not a proof of the general theorem.

## 1. Setup, identities, and the exact reduction of common factors

Use the [pass-18 notation and hypotheses](polynomial-curve-lift-pass18.md):
\[
f=xz-F(y),\quad r=xP(x,f)+yf^n,\quad
G(T,S)=S^dF(T/S),\quad
K_n(f,T)=G(T,f^n)+f^{nd+1},\quad xh=K_n(f,r),
\tag{1}
\]
where \(F\in\mathbb C[Y]\) is monic of degree \(d\ge2\),
\(n\ge1\), and \(P_0=P(x,0)\) is nonconstant. Work in
\(R=\mathbb C[x,y,z]\). Given \(e\ge1\), put
\[
a=f^e,\quad N=n+e,\quad R_*=ar+hQ(f,h),\quad
k=\frac{K_N(f,R_*)}{h}
 =a^d x+Q\Delta_G(R_*,ar;af^n),
\tag{2}
\]
where \(\Delta_G\) is the polynomial divided difference. The equality
\(K_N(f,ar)=a^dK_n(f,r)\) proves that \(k\) is polynomial.
For
\[
D=\operatorname{Jac}(f,k,\cdot)
\]
the exact identities are
\[
DR_*=f^Nk,\quad Dh=f^NG_R(R_*,f^N),\quad
Dr=f^n\{k-(Q+hQ_h)G_R(R_*,f^N)\}.
\tag{3}
\]
They follow from the original Jacobian identity and \(hk=K_N(f,R_*)\).
After inverting \(f\), (2) has a polynomial inverse since \(a\) is
a unit. Hence
\[
R_f=\mathbb C[f^{\pm1},h,k,R_*]/(hk-K_N(f,R_*)),
\tag{4}
\]
and the usual degree-in-\(R_*\) argument proves local nilpotence.

First remove a possible common power of \(f\). If \(Q\ne0\), let
\(v=\operatorname{ord}_f Q\) and \(s=\min(e,v)\); for \(Q=0\),
take \(s=e\). Then
\[
R_*=f^sR',\quad k=f^{ds}k',\quad
D=f^{ds}D',\qquad D'=\operatorname{Jac}(f,k',\cdot),
\tag{5}
\]
where the reduced construction has multiplier \(f^{e-s}\) and
polynomial \(Q/f^s\). If \(s=e\), this is exactly the additive
construction of [pass 19](iterated-local-slice-bridge-pass19.md).
If \(s<e\), the new \(Q\) has \(Q(0,h)\ne0\).
Thus the only new primitive case is \(e\ge1\) and
\(q(h):=Q(0,h)\ne0\). The rest of Sections 2 through 6 concerns that
case. Invariant replicas in (5) are restored at the end.

## 2. Exact kernel, primitivity, plinth, and the quadratic exception

Write
\[
H_0=x^{d-1}P_0^d,\quad r_0=xP_0,\quad
\kappa(H)=H^{d-1}q(H)^d,\quad \tau(H)=Hq(H).
\]
Then
\[
k\equiv\kappa(H_0),\qquad R_*\equiv\tau(H_0)\pmod f.
\tag{6}
\]
The first expression is nonconstant. The monic chart (4) has invariant
ring \(\mathbb C[f^{\pm1},k]\), and contraction through \(f=0\)
therefore gives the exact kernel
\[
C=\ker D=\mathbb C[f,k].
\tag{7}
\]
Here contraction is the elementary pole test: a coefficient pole in
\(f\), after clearing its highest power, would give a nonzero polynomial
in \(\kappa(H_0)\) equal to zero.

Factorial closure makes \(f,k\) prime in \(R\). A common factor of
the coefficients of \(D\) must divide \(DR_*=f^Nk\), so it can only
be \(f\) or \(k\). The degree-\(d-1\) polynomial \(G_R\) does
not vanish modulo the monic degree-\(d\) relation in (4), excluding
\(k\). Also
\[
Dy\equiv x\,\frac{d}{dx}\kappa(H_0(x))\not\equiv0\pmod f,
\tag{8}
\]
which excludes \(f\). Thus \(D\) is primitive.

Let \(b=\deg q\). Except when \(d=2,b=0\),
\[
\deg\kappa=db+d-1>b+1=\deg\tau.
\]
Consequently \(\tau(H)\notin\mathbb C(\kappa(H))\). A polynomial
in \(H\) rational in \(\kappa(H)\) would be polynomial in it,
since coprime numerator and denominator stay coprime after substitution.
The chart (4) gives degree-at-most-one elements
\(b(f,k)+c(f,k)R_*\). A negative \(f\)-pole would reduce to a
nontrivial relation between \(1\) and \(\tau(H_0)\) over
\(\mathbb C(\kappa(H_0))\), which has just been excluded. Therefore
\[
\ker D^2=C\oplus CR_*,\qquad P_D=f^NkC
\quad\text{if }(d,b)\ne(2,0).
\tag{9}
\]

The exception is real. Suppose \(d=2\), \(q=c\ne0\), and write
\(F(Y)=Y^2+\ell Y+c_0\). Then
\[
k=a^2x+2arQ+hQ^2+\ell af^nQ.
\tag{10}
\]
Over \(\mathbb C[f]/(f^e)\), the map
\(h\mapsto hQ(f,h)^2\) has a finite polynomial inverse: its
reduction is \(c^2h\). Choose a polynomial \(\psi(f,k)\) such
that \(\psi(f,hQ^2)=hQ\pmod{f^e}\). Then
\[
u=(R_*-\psi(f,k))/a\in R,\qquad Du=f^nk.
\tag{11}
\]
Expanding (10) one further order in \(f\), and using
\(\psi_k(0,c^2H)=1/c\), gives
\[
u\equiv-r_0+w(H_0)\pmod f
\]
for a polynomial \(w\) depending on the chosen representative.
Since \(r_0\notin\mathbb C(H_0)\), the same pole argument, now
with basis \(1,u\), proves
\[
\ker D^2=C\oplus Cu,\qquad P_D=f^nkC
\quad\text{if }d=2,\ q\in\mathbb C^*.
\tag{12}
\]
For example, if \(Q=c\) is actually constant, then
\(k/c^2\) is precisely the pass-18 polynomial \(h\) with
\(P\) replaced by \(P+a/c\). Thus its plinth cannot have the
extra exponent \(e\). No multiplicity is inferred from the displayed
nonminimal local slice alone.

In both branches the reduced plinth support is \(V(fk)\). The
primitive rank-at-most-two criterion used in pass 18 excludes rank at
most two, since both algebraically independent primes \(f,k\) divide
every local-slice derivative. Thus the primitive new case has rank three.

## 3. Slice coefficients and the first, Q-curve, correction

Consider \(E=AD+B\partial_t\), \(A,B\in C\), and assume it has
a slice. The [pass-17 affine-replacement theorem](general-invariant-affine-pass17.md),
with its stated geometric dependencies, and (9) or (12) give
\[
(A,B)=1,\qquad B=c+fkJ(f,k),\quad c\ne0.
\tag{13}
\]
Conversely these conditions suffice. Normalize \(c=1\). Even in
the exceptional case (12), they imply
\((Af^Nk,B)=1\), so the nonminimal slice \(R_*\) can still be
used. Choose \(U,V\in C\) with \(Af^NkU+BV=1\), and put
\[
\rho=BR_*-Af^Nkt,\qquad \sigma=UR_*+Vt.
\tag{14}
\]
Then \(E\rho=0\), \(E\sigma=1\), and the inverse is
\(R_*=V\rho+Af^Nk\sigma\), \(t=-U\rho+B\sigma\).

Define the invariant polynomial
\[
\widehat h=K_N(f,\rho)/k
 =h+\frac{\rho-R_*}{k}\Delta_G(\rho,R_*;f^N).
\tag{15}
\]
Both this expression and the following sharper congruence hold already
on the abstract surface
\(S=\mathbb C[f,x,h,r]/(xh-K_n(f,r))\), with an adjoined \(t\):
\[
\widehat h\equiv B^dh\pmod{f^N}.
\tag{16}
\]
Indeed the \(t\)-terms have a factor \(f^N\). In each lower
homogeneous term of \(G\), the difference from the degree-\(d\)
scaling contains \(f^N\), and its remaining \(B^j-B^d\) is
divisible by \(k\). The constant correction has the same property.
This verifies (16) before any cancellation in a nilpotent quotient.

Construct \(\widetilde Q\) over \(S_{e+1}=\mathbb C[f]/(f^{e+1})\).
Use the cone curve with parameter \(H\):
\[
(h,k,R_*)=(H,H^{d-1}Q(f,H)^d,HQ(f,H)).
\]
Let
\[
b(f,H)=B(f,H^{d-1}Q(f,H)^d),\qquad \beta(H)=Hb(f,H)^d.
\]
Since \(b\equiv1\pmod f\), \(\beta\) has a finite polynomial
inverse \(j_Q\). Define
\[
\widetilde Q(f,Z)=
 \bigl(b^{1-d}Q\bigr)(f,j_Q(Z))\pmod{f^{e+1}},
\tag{17}
\]
and choose its representative of degree at most \(e\) in \(f\).
This is exactly the [pass-19 curve lemma](iterated-local-slice-bridge-pass19.md),
applied to the first curve rather than the old \(P\)-curve.
In particular it includes the inverse curve identity.

The actual surface is not this curve modulo \(f^{e+1}\): it has
the normal displacement \(ar\). The following calculation retains it.
In the polynomial formula (2),
\[
k-H^{d-1}Q(f,H)^d\in aS\quad(H=h).
\]
Since \(B-1\) has a factor \(f\), it follows that
\(B(f,k)-b(f,h)\in faS\). Combining this with (16) and
\(N\ge e+1\) gives
\[
\widehat h\equiv hb(f,h)^d,\qquad
\rho\equiv hb(f,h)Q(f,h)+ar\pmod{f^{e+1}}.
\]
Consequently
\[
\rho-\widehat h\widetilde Q(f,\widehat h)
 \equiv ar\pmod{f^{e+1}}.
\tag{18}
\]
The extra order in (17) is what preserves the first normal displacement.

## 4. A polynomial surface-cylinder isomorphism, not a rational inverse

Set
\[
\widehat r=\frac{\rho-\widehat h\widetilde Q(f,\widehat h)}a,
\quad
\widehat x=
 \frac{k-\widetilde Q(f,\widehat h)
       \Delta_G(\rho,a\widehat r;af^n)}{a^d}.
\tag{19}
\]
The first quotient is polynomial by (18), and
\(\widehat r\equiv r\pmod f\). If \(N_x\) is the numerator
of the second quotient, the homogeneous identity gives
\[
\widehat hN_x=a^dK_n(f,\widehat r).
\]
Here \(f\) is prime in \(S[t]\), because its quotient is the
integral cone \(xh=r^d\), and
\(\widehat h\equiv h\not\equiv0\pmod f\).
Repeated prime-factor cancellation therefore gives
\(a^d\mid N_x\). No UFD assertion about \(S\) is needed.
Thus \(\widehat x\) is polynomial,
\[
\widehat x\widehat h=K_n(f,\widehat r),\qquad
(\widehat x,\widehat h,\widehat r)\equiv(x,h,r)\pmod f.
\tag{20}
\]
The congruence for \(\widehat x\) uses only that \(h\) is a
nonzerodivisor in the integral cone.

There is a polynomial inverse on an independent copy
\(\mathbb C[f,X,H,T,\sigma]/(XH-K_n(f,T))\). Set
\[
\rho=aT+H\widetilde Q(f,H),\quad
k=a^dX+\widetilde Q(f,H)\Delta_G(\rho,aT;af^n).
\]
Evaluate \(A,B,U,V\) at this \((f,k)\), recover \(R_*,t\)
by (14), and put
\[
h=H+\left(\frac{V-1}{k}\rho+Af^N\sigma\right)
            \Delta_G(R_*,\rho;f^N).
\tag{21}
\]
This is polynomial, since \(V\equiv1\pmod k\).
Modulo \(a\), this is the inverse scaling on the
\(\widetilde Q\)-curve: \(V=B^{-1}\),
\(h=V^dH\), and \(R_*=V\rho\). The inverse statement
in (17), specialized to this nilpotent algebra, gives
\(R_*-hQ(f,h)\in aS[\sigma]\). Hence
\[
r=(R_*-hQ(f,h))/a,\qquad
x=(k-Q(f,h)\Delta_G(R_*,ar;af^n))/a^d
\tag{22}
\]
are polynomial, the second by the same prime-factor argument.
After inverting \(f\), these maps are the ordinary inverse mutations
and inverse matrix. Both surface rings are domains, so identities after
that localization are identities globally. Equations (14)-(22) therefore
give an actual polynomial isomorphism between the two surface cylinders.

## 5. The induced cone automorphism and the second, P-curve, correction

The surface-cylinder isomorphism just proved must still be shown to
respect the original overring's denominator ideals. Its first three
coordinates, modulo \(f^n\), are independent of \(t\).
For \(\widehat h\), the difference from its value at \(t=0\)
is divisible by \(f^N\). The corresponding difference for
\(\widehat r\) is divisible by \(f^{N-e}=f^n\).
Comparing the two identities
\(\widehat x\widehat h=K_n(f,\widehat r)\), and cancelling
powers of the prime \(f\), gives the same conclusion for
\(\widehat x\). The inverse formulas have exactly the same properties
with \(\sigma\) in place of \(t\). Thus their reductions give
mutually inverse automorphisms \(\alpha,\alpha^{-1}\) of
\[
\mathbb C[f]/(f^n)[x,h,r]/(xh-r^d).
\]
By (20), \(\alpha\equiv\mathrm{id}\pmod f\).

These automorphisms also preserve the vertex ideal \(I=(x,h,r)\).
By (16), \(\widehat h=B^dh\pmod{f^n}\); the reduction of
\(k\) is in \(I\), so its degree-one part is exactly \(h\).
For \(\widehat r\), use before dividing by \(a\) the explicit
polynomial expression
\[
B ar+B hQ-B^dh\widetilde Q(f,B^dh)+f^N L.
\tag{23}
\]
The middle difference is divisible by \(a\) in the free polynomial
ring in \(f,x,h,r\), by the calculation leading to (18), and it has
an explicit factor \(h\). Its quotient still vanishes at
\(x=h=r=0\); the remaining error after division is a multiple of
\(f^n\). Thus \(\widehat r\in I\) in the cone quotient.
Finally the degree-one part of
\(\widehat x\widehat h=\widehat r^d\) is the constant term of
\(\widehat x\) times \(h\). Since \(d\ge2\), it must vanish,
so \(\widehat x\in I\). This argument does not cancel a nilpotent
parameter after specialization. The inverse satisfies the same statements.

Apply the pass-19 finite curve lemma to \(\alpha\) on the old curve
\[
(x,h,r)=(u,u^{d-1}P(u,f)^d,uP(u,f))
\quad\text{over }\mathbb C[f]/(f^n).
\]
It produces a polynomial jet \(\widetilde P(X,f)\), of degree less
than \(n\) in \(f\), with \(\widetilde P(X,0)=P_0(X)\),
and inverse curve identities. Therefore
\[
Y=\frac{\widehat r-\widehat x\widetilde P(\widehat x,f)}{f^n},
\qquad
Z=\frac{\widehat h-
 T_F(\widehat x,Y,\widetilde P(\widehat x,f),f)}{f^{nd}}
\tag{24}
\]
are polynomial and satisfy \(f=\widehat xZ-F(Y)\).
The first assertion is the curve identity. The second follows by the
Taylor identity and \(\gcd(f,\widehat x)=1\) in the physical
polynomial ring, exactly as in pass 19.

For the inverse, begin with independent \((X,Y,Z,\sigma)\), put
\(f=XZ-F(Y)\), \(T=X\widetilde P+Yf^n\), and
\(H=T_F(X,Y,\widetilde P,f)+Zf^{nd}\). Apply the polynomial
inverse (21)-(22). The inverse \(P\)-curve identity gives
\(r-xP\in f^n\), and the Taylor identity recovers polynomial
\(y,z\). The maps are inverse after localization and hence globally.
It follows that
\[
R[t]=\mathbb C[\widehat x,Y,Z,\sigma],\qquad
E=\partial_\sigma,\qquad
\ker E=\mathbb C[\widehat x,Y,Z]\cong\mathbb C^{[3]}.
\tag{25}
\]

## 6. Full scope for powers of f, and the distinct-divisor boundary

For every base (1), every \(e\ge1\), and every polynomial \(Q\),
every invariant slice extension of the derivation in (2)-(3) has
polynomial kernel. For \(Q(0,h)\ne0\), Sections 2 through 5 prove
this constructively, with the exact exceptional plinth (12). In the
general case use (5): if the reduced multiplier remains nonunit, the
same proof applies; if it is a unit, apply pass 19. Replacing \(A\)
by \(Af^{ds}\) absorbs the invariant replica. In particular no
assertion that the original unnormalized Jacobian is always primitive
is made.

For a multiplier vanishing away from \(f=0\), the finite jets are
different. The explicit coefficient version of the Chinese-remainder
construction is given in Section 8; Section 9 verifies that its premise
covers every slice extension for the requested contrast \(a=f-1,Q=h\).
The [uncorrected inverse obstruction](nonunit-inverse-obstruction-pass20.md)
is a separate calculation. Failure of that formula is not identified
with a nonpolynomial kernel.

## 7. A bounded two-correction control with an actual initial pole

Take \(d=2\), \(F=Y^2\), \(P=x^2\), \(n=e=2\),
\(Q=h\), and \(B=1+fk\). The uncorrected numerator obeys
\[
\rho-\widehat h^2=-3fh^5\pmod{f^2},
\]
so dividing it by \(a=f^2\) has a genuine simple pole.
The first correction is
\[
\widetilde Q(h,f)=h-3fh^4+24f^2h^7\pmod{f^3}.
\]
With this degree-two representative, the corrected old-curve map is
\[
\widehat x=x-f(12x^{16}+506x^{53})\pmod{f^2},
\]
and the second correction is
\[
\widetilde P(X,f)=X^2+f(31X^{17}+1265X^{54})\pmod{f^2}.
\]
The checker verifies these independently derived coefficients, both
directions of the first normal-displacement congruence for five
\((d,e,Q)\) choices, the final inverse \(P\)-curve, lower-coefficient
homogeneous identities, and the genuine quadratic constant-\(Q\)
plinth exception. The sixth method performs coefficientwise CRT for
\(a=f^2(f-1)^2\), then independently verifies both directions at
both distinct divisor neighborhoods. The command is

```sh
/opt/anaconda3/bin/python research/nonunit_local_slice_checks_pass20.py
```

## 8. Arbitrary multiplier: a coefficient-explicit CRT extension

There is a useful extension without assuming that a particular displayed
local slice is minimal. Let \(0\ne a(f)\in\mathbb C[f]\), let
\(Q\in\mathbb C[f,h]\), and put
\[
\Phi(f,T)=G(T,af^n)+a^df^{nd+1},\quad
R_*=ar+hQ,\quad k=\Phi(f,R_*)/h,
\quad D=\operatorname{Jac}(f,k,\cdot).
\tag{26}
\]
Then \(DR_*=af^nk\). Let \(q_a(f)\) be the monic squarefree
product of the distinct factors of \(af\). The following is a
sufficient coefficient condition, not a claimed necessary one:
\[
(A,B)\mathbb C[f,k]=\mathbb C[f,k],\qquad
B=1+q_a(f)kJ(f,k).
\tag{27}
\]
Under (27), \(AD+B\partial_t\) has a slice and the polynomial
kernel conclusion (25), even if \(D\) is not primitive or
\(\mathbb C[f,k]\) has not been identified with its entire kernel.

Here is the complete modification of the proof. Factor
\(a=c\prod_g g^{v_g}\) into \(g=f-\lambda\), and write
\(e=\operatorname{ord}_f a\). For each \(g\mid a\), perform
the \(Q\)-curve construction (17) over
\(\mathbb C[f]/(g^{v_g})\). Its scaling factor satisfies
\(b\equiv1\pmod g\), so its parameter inverse is a finite
polynomial: iterate in the nilpotent ideal \((g)\).
At \(g=f\), impose the construction one order deeper, modulo
\(f^{e+1}\); if \(e=0\), impose simply
\(\widetilde Q\equiv Q\pmod f\). These conditions have
pairwise coprime coefficient ideals, so coefficientwise polynomial CRT
gives a single \(\widetilde Q\in\mathbb C[f,h]\).

Replace \(f^N\) everywhere by \(af^n\), and replace \(K_N\)
by \(\Phi\), in (14)-(22). The matrix exists because (27)
implies \((Aaf^nk,B)=1\). The forward first numerator vanishes
modulo each \(g^{v_g}\), by its \(Q\)-curve identity, hence is
divisible by \(a\). The inverse numerator has the same property,
using the inverse curve identity at each factor. Every \(g=f-\lambda\)
is prime in the original abstract surface: its quotient is
\(\mathbb C[x,h,r]/(xh-K_n(\lambda,r))\), an integral domain,
since \(K_n(\lambda,r)\) is a nonzero monic polynomial in \(r\).
Moreover \(\widehat h\equiv h\not\equiv0\pmod g\), since
\(B\equiv1\pmod g\). Repeated prime-factor cancellation makes
both second quotients, with denominator \(a^d\), polynomial.
After inverting \(af\), the maps are the ordinary inverse mutations
and inverse matrix. Both surface rings are domains, so the composition
identities hold globally. Thus the two surface-cylinder maps are
mutually inverse polynomial maps.

It remains to justify the old \(f\)-adic overring, rather than just
the new divisors. At \(f=0\), write \(a=f^e u(f)\) with
\(u(0)\ne0\). If \(e>0\), the extra \(f^{e+1}\) jet
retains the normal displacement \(ar\) exactly as in (18).
If \(e=0\), division by \(a\) is already invertible in the
\(f\)-adic quotient, and \(\widetilde Q\equiv Q\pmod f\)
gives the same identity reduction. The \(t\)-difference in
\(\widehat h\) has a factor \(af^n\), and that in
\(\widehat r\) has a factor \(f^n\). The inverse has the
same property. The arguments of Section 5, with the unit \(u\)
inverted in the finite \(f\)-adic ring, give a vertex-preserving,
\(t\)-independent cone automorphism congruent to the identity.
The second \(P\)-curve correction and the global inverse follow
unchanged. This proves the coefficient-explicit assertion.

Condition (27) must not be promoted to necessity without a plinth
calculation. In particular, for \(d=2\), \(Q=c\in\mathbb C^*\),
and arbitrary \(a\), (10) identifies \(k/c^2\) with the old
base after \(P\mapsto P+a/c\). Its plinth is \(f^nk\),
so a factor of \(a\) away from \(f=0\) need not constrain \(B\)
at all. This is an exact counterexample to that stronger necessity claim.

## 9. The contrasting divisor a=f-1 with Q=h

For \(a=f-1\), \(Q=h\), the coefficient premise (27) does cover
every invariant slice extension. The chart after inverting \(fa\)
is
\[
R_{fa}=\mathbb C[f,(fa)^{-1},h,k,R_*]/(hk-\Phi(f,R_*)).
\]
At \(f=1\), the residues are
\(k=h^{2d-1}\), \(R_*=h^2\); their degrees in the transcendental
parameter \(h\) are \(2d-1>2\). At \(f=0\), put
\(L=-1+x^{d-2}P_0^{d-1}H_0\). Then
\[
k=xL^d,\qquad R_*=xP_0L\pmod f.
\]
Writing \(D_0=\deg H_0=d(\deg P_0+1)-1\), their degrees in
\(x\) are \((2d-1)D_0>2D_0\). Thus the invariant pole test
contracts to \(\mathbb C[f,k]\) at both divisors, and the
degree-at-most-one pole test excludes cancellation at both. Consequently
\[
\ker D=\mathbb C[f,k],\qquad
\ker D^2=\mathbb C[f,k]\oplus\mathbb C[f,k]R_*,\qquad
P_D=(f-1)f^nk\mathbb C[f,k].
\tag{28}
\]

Primitivity is equally exact. Every irreducible coefficient factor is
one of \(f-1,f,k\).
The monic chart excludes \(k\), and the derivative in (8), with
the present nonconstant residue \(xL^d\), excludes \(f\).
Modulo \(f-1\), the new Jacobian is
\(-(2d-1)h^{2d-2}D_1\), which is nonzero because the old
\(D_1\) is primitive and the fiber ring is a domain.
Thus \(D\) is primitive and rank three.

The three plinth lines \(f=0\), \(f=1\), and \(k=0\) have
connected union. A polynomial unit on each line is a nonzero constant,
and the two intersection points identify the three constants. The
affine-replacement criterion therefore gives exactly
\((A,B)=1\), \(B=c+f(f-1)kJ\), with \(c\ne0\).
After normalizing \(c=1\), Section 8 applies. Here \(a\) is
squarefree, so the first CRT correction can simply be
\(\widetilde Q=Q\): \(B=1\pmod a\) already supplies the
required first inverse divisibility, and \(a\) is a unit at
\(f=0\). Only the second \(P\)-curve correction is needed.
This proves polynomial kernels for every invariant slice extension of
this contrasting nonunit family as well.

## Verification boundary

The proof uses the already recorded pass-18 kernel and local-slice facts,
the pass-19 finite curve lemma, and, only for necessity of the coefficient
condition, the pass-17 source-dependent affine-replacement theorem.
The coordinate sufficiency proof needs only (13) for powers of \(f\),
or the explicitly stronger condition (27) for the arbitrary-multiplier
CRT construction.
The companion exact checker is a bounded control of the formulas, not
an independent formal verification of this all-parameter theorem.
