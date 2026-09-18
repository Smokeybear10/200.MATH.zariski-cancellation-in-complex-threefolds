# Quintic generation and whole-fiber nonvanishing

The actual quintic filtration can be constructed explicitly in the
reduced zero-first-jet sector of the degree-two coordinate-frame
problem. Its fifth image is principal and its entire module is free.
Nevertheless its generated algebra is not the actual intrinsic
algebra: every generating set in this sector requires an element
of intrinsic degree at least six.

The obstruction is scheme-theoretic. The induced derivation kills
the whole quintic algebra's image on the closed fiber, while a
primitive derivation on the actual smooth factorial threefold
cannot kill the whole fiber. Nilpotent directions are essential
to this comparison. Replacing a fiber by its reduction would
invalidate the argument.

The original working question remains
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The complex-threefold interpretation of the supplied conjecture
has not been confirmed by the professor. The results here do not
settle (1), construct an actual obstruction point, or establish
historical novelty. In particular the conditional degree-six
lower bound is not an example of a ring needing that degree.

## 1. Actual hypotheses and the established quartic layer

Let \(D\) be the nonzero primitive intrinsic locally nilpotent
derivation supplied by the actual independent degree-two frame.
Set
\[
C=\ker D\simeq\mathbb C^{[2]},\quad
R=C_{\mathfrak m},\quad\mathfrak n=(a,b),\quad
\mathcal A=A\otimes_C R,\quad L=\operatorname{Frac}R,
\]
\[
F_i=\ker D^{i+1},\qquad I_i=D^i(F_i)\subset R.
\tag{2}
\]
The actual \(A\) is smooth and factorial, and \(C\subset A\) is
faithfully flat. The closed fiber of \(\mathcal A\) is nonempty
and purely one-dimensional. These are inherited quotient
conclusions from the cylinder and actual leading frame, not
properties assigned to an approximate conic.[^1]

The local assumptions throughout the quintic construction are
\[
JR=\mathfrak n,\qquad B_1,B_2\in\mathfrak n^2.
\tag{3}
\]
Reducedness of \(J\) alone does not imply the second condition.
The sector includes actual second-image obstructions at ordinary
triples of the full plinth, but not arbitrary rank-one first jets.

Use invariant coefficients \(c,d,e,f,g,h,q_1,q_2,q_3\in R\) with
\[
B_1=a^2c+abd+b^2e,\quad
B_2=a^2f+abg+b^2h,\quad
Q=a^2q_1+abq_2+b^2q_3.
\]
The established actual elements satisfy
\[
r=az+bw,\quad Dr=p=aB_1+bB_2\ne0,\quad
Dz=\epsilon br+B_1,\quad Dw=-\epsilon ar+B_2,
\]
\[
\epsilon r^2-2B_2z+2B_1w-Q=0,\qquad\epsilon\in R^*.
\tag{4}
\]
The [quartic theorem](research/fourth-image-boundary-pass52.md)
gives the complete bases and coherent relations
\[
F_2=R\oplus Rz\oplus Rw,\quad F_3=F_2\oplus Rt,\quad
F_4=F_2\oplus RU\oplus RV,
\]
\[
aU=\epsilon w^2-2hz+2ew-q_3,\quad
bV=\epsilon z^2-2fz+2cw-q_1,\quad
t=-\frac{bU-aV}{2}-gz+dw-\frac{q_2}{2}.
\tag{5}
\]
Here \(D^3t=3\epsilon^2p^2\),
\(D^4U=6\epsilon^3ap^2\) and \(D^4V=6\epsilon^3bp^2\).
The divisions defining \(U,V,t\) were proved in the actual flat
algebra. Rational formulas alone do not establish their membership.

## 2. The actual fifth image and basis

The complete coefficient reduction is the key new construction.
Define
\[
\begin{aligned}
N_0={}&a(2cq_3-fq_2)+b(2dq_3-(e+g)q_2+2hq_1),\\
N_z={}&a(4ch-2fg)+b(4dh-2eg+4fh-2g^2+\epsilon q_3),\\
N_w={}&-a(4ce-2df+\epsilon q_1)-b(4ch+2de-2dg+\epsilon q_2),\\
N_U={}&2a^2c+2abd+abf+b^2(e+g),\\
N_V={}&a^2f+ab(e+g)+2b^2h.
\end{aligned}
\tag{6}
\]
Then
\[
\epsilon rt=N_0+N_zz+N_ww+N_UU+N_VV,
\qquad rt\in\mathfrak nF_4.
\tag{7}
\]
Every coefficient is in \(\mathfrak n\); the last two are in
\(\mathfrak n^2\). To verify the identity without assuming
generic coefficients descend, put
\(\mathcal F=\epsilon r^2-2B_2z+2B_1w-Q\). Before imposing
the conic, substitution of the fractions in (5) gives
\[
rt-\epsilon^{-1}(N_0+N_zz+N_ww+N_UU+N_VV)
=\mathcal F\,
\frac{a\epsilon z-2af-2be-b\epsilon w-2bg}{2ab\epsilon}.
\tag{8}
\]
Clear the denominator, evaluate in the actual domain, and cancel.
This is an exact all-coefficient identity, not a sampled equality.

An explicit split \(rt=aR_a+bR_b\) is
\[
\begin{aligned}
R_a=\epsilon^{-1}[&
2cq_3-fq_2+(4ch-2fg)z-(4ce-2df+\epsilon q_1)w\\
&+(2ac+2bd+bf)U+(af+b(e+g))V],\\
R_b=\epsilon^{-1}[&
2dq_3-(e+g)q_2+2hq_1
 +(4dh-2eg+4fh-2g^2+\epsilon q_3)z\\
&-(4ch+2de-2dg+\epsilon q_2)w+b(e+g)U+2bhV].
\end{aligned}
\tag{9}
\]
Both elements belong to \(F_4\). The resulting syzygy
\(a(zt-R_a)+b(wt-R_b)=0\), together with regularity of
\(a,b\) in \(\mathcal A\), supplies one actual \(Y\) with
\[
zt-R_a=bY,\qquad wt-R_b=-aY,\qquad
D^5Y=30\epsilon^3p^3,\quad D^6Y=0.
\tag{10}
\]
For instance, reduction modulo \(a\) first makes \(wt-R_b\)
divisible by \(a\); cancellation then supplies the other equation.
The derivative calculation uses the product rule and (5).

The full quadratic divisor charts give
\(I_5R_{(\pi)}=p^3R_{(\pi)}\) at every height-one base prime.
Their normalized monic basis is
\(1,\rho,\upsilon,\rho\upsilon,\upsilon^2,\rho\upsilon^2\),
where \(D\rho=p\), \(D\upsilon=2\rho\) and
\(p\upsilon=\rho^2-\eta\). The top fifth derivative is \(120p^3\).
UFD contraction gives \(I_5\subset p^3R\); (10) attains it.
Subtracting the matching multiple of \(Y\) proves
\[
\boxed{I_5=p^3R,\qquad F_5=F_4\oplus RY.}
\tag{11}
\]
The full [construction](research/quintic-correction-pass53.md)
also checks that changing the split changes \(Y\) only by \(F_4\).

The old quartic unit-coefficient obstruction does not propagate.
Its product with \(r\) lies in \(\mathfrak nF_4\), because
\(rt\in\mathfrak nF_4\) and \(rz,rw\in\mathfrak nF_3\).
Thus the principal fifth image is proved directly, not inferred
from an alternating pattern.

## 3. The whole quintic algebra has zero fiber velocity

The coherent cubic formula gives an exact coefficient-order bound.
Put \(c_0=ac+bd,\ d_0=be,\ e_0=af+bg,\ f_0=bh\). Then
\[
Dt=\epsilon Q+
 \epsilon[a(e_0+2d_0)+3bf_0]z
-\epsilon[3ac_0+b(d_0+2e_0)]w
+2(c_0f_0-d_0e_0).
\tag{12}
\]
Every coefficient is in \(\mathfrak n^2\).
Since \(Dz,Dw\in\mathfrak n^2F_2\), this proves
\(D(F_3)\subset\mathfrak n^2F_2\).

Differentiate the first quartic equation:
\[
aDU=-2\epsilon^2a(rw)+2\epsilon B_2w-2hDz+2eDw
\in\mathfrak n^2F_3.
\tag{13}
\]
The second equation gives the same bound for \(bDV\).
Because \(F_3\) is free and
\((\mathfrak n^2:a)=(\mathfrak n^2:b)=\mathfrak n\),
coefficientwise cancellation gives \(D(F_4)\subset\mathfrak nF_3\).

In the specified \(R_a\), the coefficients of \(U,V\) belong
to \(\mathfrak n\), so \(DR_a\in\mathfrak n^2F_3\).
The product needing care is
\[
D(zt)=\epsilon b(rt)+B_1t+zDt\in\mathfrak n^2F_4.
\]
The first term uses the full reduction (7), and the last uses
\(F_2F_2\subset F_4\). Consequently
\(bDY=D(zt-R_a)\in\mathfrak n^2F_4\). Since \(DY\in F_4\)
and that module is free, the same coefficient rule gives
\[
\boxed{
D(F_3)\subset\mathfrak n^2F_2,\quad
D(F_4)\subset\mathfrak nF_3,\quad
D(F_5)\subset\mathfrak nF_4.}
\tag{14}
\]
This is the complete [velocity argument](research/quintic-fiber-velocity-pass53.md),
not an assertion that products of arbitrary filtration modules
have the smaller degree required.

Let \(\bar{\mathcal A}=\mathcal A/\mathfrak n\mathcal A\).
The induced derivation therefore satisfies
\[
\bar D\bigl(\operatorname{image}(R[F_5]\longrightarrow
\bar{\mathcal A})\bigr)=0.
\tag{15}
\]
The statement retains the entire fiber, including nilpotents.
Nonvanishing on the rest of the actual fiber needs a separate proof.

## 4. A primitive derivation is nonzero on every whole fiber

The following structural statement is more general than the
special frame: let \(A\) be a smooth factorial complex threefold,
\(D\ne0\) a primitive LND, \(C=\ker D=\mathbb C[u,v]\), and
assume \(C\subset A\) faithfully flat. Then
\[
\boxed{\bar D\ne0\text{ on every whole scheme fiber over }C.}
\tag{16}
\]

Choose finite algebra generators \(x_i\) of \(A\).
Their nonzero derivative values have gcd one. Indeed their gcd
\(\delta\) divides \(D\delta\); the LND degree rule forces
\(D\delta=0\), and otherwise \(D/\delta\) would be a proper
invariant-factor division of \(D\). Hence for any prime
\(\mathfrak q\),
\[
hD(A_{\mathfrak q})\subset A_{\mathfrak q},\
h\in\operatorname{Frac}A
\quad\Longrightarrow\quad h\in A_{\mathfrak q}.
\tag{17}
\]
An irreducible denominator would divide every generator value
in the localized UFD. This does not say their ideal is the unit ideal.

Fix a closed base point, now write its parameters as
\(a=u-\alpha,\ b=v-\beta\), and choose a prime \(\mathfrak q\)
minimal over \((a,b)A\). Flatness and the height theorem give
\(\operatorname{ht}\mathfrak q=2\). Thus \(S=A_{\mathfrak q}\)
is a regular local surface and \((a,b)S\) is parameter-primary.
The component field has transcendence degree one. Choose an
actual \(t_0\in A\) with transcendental residue. Then
\[
K=\mathbb C(t_0)\subset S,\qquad
[\kappa(\mathfrak q):K]<\infty,\qquad
T=S/(a,b)\text{ is a nonzero Artinian complete intersection}.
\tag{18}
\]
The finite extension is separable. Over the perfect field \(K\),
\(S\) is essentially smooth; its relative differential module
is free of rank two. Choose \(x,y\in S\) with \(dx,dy\) a basis.
Together with \(dt_0\) these give a basis over \(\mathbb C\).
This is a local differential choice, not a rational section or
a global coordinate assertion.[^4]

Write \(da=a_xdx+a_ydy,\ db=b_xdx+b_ydy\) in relative
differentials over \(K\), and set
\(\Delta=a_xb_y-a_yb_x\).
The conormal presentation makes the image of \(\Delta\) generate
\(\operatorname{Fitt}_0\Omega_{T/K}\). It is nonzero: after
scalar extension to an algebraic closure, any local factor has
a coefficient-compatible presentation as a two-variable
power-series ring modulo two parameters. Its Jacobian generates
a nonzero socle by the classical characteristic-zero socle theorem.[^2]
Fitting base change and localization carry a zero ideal to zero,
which would contradict that fact.[^3] Therefore
\(\Delta\notin(a,b)S\). This reasoning retains a possibly
nonrational original component field.

With \(\omega=dt_0\wedge dx\wedge dy\), define a regular local
Jacobian derivation \(J_{\rm Jac}\) by
\[
\iota_{J_{\rm Jac}}\omega=da\wedge db,\qquad
J_{\rm Jac}(t_0)=\Delta.
\tag{19}
\]
It kills \(a,b\). Over the function field that vertical
derivation space is one-dimensional, so
\(J_{\rm Jac}=hD\). Equation (17) proves \(h\in S\) before
quotienting. Hence
\[
J_{\rm Jac}(t_0)\notin(a,b)S
\quad\Longrightarrow\quad D(t_0)\notin(a,b)S.
\tag{20}
\]
This proves nonvanishing on the local scheme at the generic point
of each closed-fiber component. At a height-one base fiber,
vanishing would make its prime divide every derivative value,
contradicting primitivity; faithful flatness keeps the fiber
nonempty. Generic-fiber nonvanishing is immediate.
These cases establish (16).

The [full proof](research/primitive-fiber-nonvanishing-pass54.md)
does not require a global canonical trivialization.
The familiar polynomial action
\(D_0=x\partial_y+2y\partial_z\), with \(h=xz-y^2\),
shows the precise boundary: on the fiber \(x=h=0\),
\(\bar D_0(z)=2y\ne0\) in \(\mathbb C[y,z]/(y^2)\),
while the derivation on its reduced line is zero.
The replica \(xD_0\) vanishes on the whole fiber and is not primitive.

## 5. Full quintic non-generation and the algebraic equality test

The actual cylinder setup satisfies all hypotheses of (16).
Combining (15) with nonvanishing on the same whole fiber gives
\[
\boxed{R[F_5]\ne\mathcal A.}
\tag{21}
\]
Every generating set therefore contains an element of intrinsic
degree at least six. Neither a presentation for \(R[F_5]\) nor
a reduced-line fiber theorem is needed. The result says nothing
about existence of an actual point satisfying (3), or sufficiency
of degree six.

For completeness, the exact full-algebra equality test is
\[
K=\mathcal A
\quad\Longleftrightarrow\quad K\text{ is }R\text{-flat}
\quad\Longleftrightarrow\quad(a,b)\text{ is }K\text{-regular},
\tag{22}
\]
for any intermediate algebra \(R\subset K\subset\mathcal A\)
agreeing with \(\mathcal A\) at all height-one base primes.
The quartic divisor theorem ensures this premise for \(K=R[F_5]\).

The nontrivial implication needs no finite-generation assumption
on \(\mathcal A/K\). For \(x\in\mathcal A\), the annihilator
of its cyclic class is either the unit ideal or
\(\mathfrak n\)-primary. In the latter case
\(a^Nx,b^Nx\in K\). Regularity makes \(b^N\) a nonzerodivisor
modulo \(a^NK\), so \(a^Nx\in a^NK\), and cancellation gives
\(x\in K\). Regularity of these powers follows by induction
from regularity of \(a,b\). Conversely, a nonzero socle class
of a finite cyclic quotient gives \(x\notin K\) with \(ax,bx\in K\),
and the class of \(ax\) exhibits the failure of regularity.

Thus (21) also proves failure of this parameter regularity on
the whole quintic algebra. Freeness of the finite module \(F_5\)
does not supply regularity of its generated algebra.
The [saturation note](research/quintic-saturation-gate-pass53.md)
deduplicates this argument against the earlier intersection results.

## 6. Where the actual fiber can meet the quartic model

The exact quartic algebra \(K_4\) has vertical fiber
\(S_0[U,V]\), where \(S_0\) is a nonzero finite algebra of
complex dimension at most three. Each reduced vertical component
has height one. If a component were locally principal at an actual
image point, its nonunit local equation would divide both \(a,b\)
in the actual local domain. This contradicts regularity: writing
\(a=\tau a',b=\tau b'\) gives \(ba'=b'a\) but \(a'\notin(a)\).
Consequently
\[
\operatorname{image}\operatorname{Spec}\bar{\mathcal A}
\subset\operatorname{Sing}(K_4)\cap V(\mathfrak nK_4).
\tag{23}
\]
Regular local rings are factorial, so each height-one component
would be principal at a regular point.[^5]
This is a support statement, not vanishing of a Jacobian ideal
in a possibly nonreduced actual fiber.

At a residue point \((z_0,w_0)\), let \(G\) be the three-by-two
\(Z,W\) differential matrix of the three quartic relations.
Their remaining first-order columns are
\(d_a=\gamma_a+(0,V,U)^{\mathsf t}\) and
\(d_b=\gamma_b+(V,U,0)^{\mathsf t}\).
The cotangent matrix is \([d_a\mid d_b\mid G\mid0\mid0]\).[^6]
If \(G\) has rank two and left null vector
\(\ell=(\ell_1,\ell_2,\ell_3)\), the singular subset is
\[
\ell_3U+\ell_2V+\ell\gamma_a=0,\qquad
\ell_2U+\ell_1V+\ell\gamma_b=0.
\tag{24}
\]
It is a point when \(\ell_1\ell_3-\ell_2^2\ne0\), otherwise
a line or empty. Rank one gives the proper conic
\(\det[v,d_a,d_b]=0\) for a nonzero column-image vector \(v\);
rank zero leaves the entire plane singular.

If \(S_0=\mathbb C\), then \(z-z_0,w-w_0\in\mathfrak n\mathcal A\).
Expanding in \(a,b\), the flat conormal module
\(\mathfrak n\mathcal A/\mathfrak n^2\mathcal A
\simeq\bar{\mathcal A}^{\,2}\) makes (24) hold in the whole
actual fiber. Thus
\[
S_0=\mathbb C,\quad\ell_1\ell_3-\ell_2^2\ne0
\quad\Longrightarrow\quad
\operatorname{image}(K_4\to\bar{\mathcal A})=\mathbb C.
\tag{25}
\]
This does not make the actual fiber zero-dimensional.

The [support note](research/quartic-fiber-image-support-pass53.md)
gives an exact weaker polynomial control:
with \(p=a^3+b^3\) and actual polynomial overring \(R[t_0]\),
take \(z=a^2t_0+bp\,t_0^2/2\) and
\(w=b^2t_0-ap\,t_0^2/2\).
The quartics \(U=(w^2-2z)/a\), \(V=(z^2+2w)/b\) are polynomial.
The quartic model has only the singular point \(U=V=0\)
on its plane fiber, and the entire line fiber of the overring
contracts to that point. Its true primitive plinth is a unit;
these are not its full \(F_4\) generators. It does not realize
the unresolved frame, but it rules out point contraction alone
as a contradiction.

## 7. The missing low-degree selection theorem

The actual generic graph supplies
\(B_L=L[x_3,x_4]\), \(A_L=L[j]\), and an affine generic
\(E\)-slice \(\sigma_0\). Here \(E\) is the original sliced
action and \(j\) an affine transverse coordinate.
Choose one actual slice \(s_*=\sigma_0+H_*(j)\). All actual
slice gauges form exactly
\[
H_*+\mathcal A\subset L[j].
\tag{26}
\]
Thus existence of a slice with transverse degree at most \(N\)
is the additive membership condition
\(H_*\in\mathcal A+L[j]_{\le N}\). For \(N\ge1\), its class
is independent of either slice choice and affine transverse
coordinate changes.

The good coordinates of the quadratic graph have the form
\(x_i=h_i\sigma_0^2/2+A_i(j)\sigma_0+B_i(j)\), with
\(\deg A_i\le1,\deg B_i\le2\), and some \(h_i\ne0\).
For an actual slice \(s=\sigma_0+H\), projection gives
\[
\rho_s(x_i)=h_iH^2/2-A_iH+B_i,\qquad
\max_i\deg_D\rho_s(x_i)=2\deg H\quad(\deg H\ge2).
\tag{27}
\]
The leading square cannot cancel. Gauges of degree at most one
give all projected degrees at most two. Consequently
\[
\exists\text{ projected }F_5\text{ list}
\quad\Longleftrightarrow\quad
H_*\in\mathcal A+L[j]_{\le2}
\quad\Longleftrightarrow\quad
\exists\text{ projected }F_4\text{ list}.
\tag{28}
\]
Each projected list generates \(\mathcal A\), so the quartic
theorem already excludes (28) at an actual point satisfying (3).
The quintic result (21) is stronger because it excludes unrelated
generating sets as well.

Large arbitrary gauges do not refute a possible minimum bound.
For an actual intrinsic local slice \(r\in A\) with \(Dr\ne0\),
\[
\Phi_N=\exp(r^N E),\qquad
\Phi_N^{-1}=\exp(-r^N E),\qquad
\Phi_N(s_*)=s_*+r^N.
\tag{29}
\]
These are actual polynomial automorphisms, without a presumed
polynomial coordinate system for \(A\). They make projected
degrees arbitrarily high while leaving (26) unchanged.
The [bridge note](research/profile-generation-gap-pass54.md)
also records why the inherited original flow-time bound of six
does not bound this transverse minimum.

A theorem forcing a degree-five generating set from the entire
actual profile would now exclude the sector. It remains unproved.
A theorem forcing a degree-two gauge would also suffice, but is
a different existential assertion. Full supplied-profile
recognition and universal reduction to that profile remain
additional obligations even if this local sector is excluded.

## Verification and sources

The captured expanded regression ran from
2026-09-13 21:16:35 UTC to 2026-09-13 21:18:11 UTC.
All 995 methods in 123 suites passed. The only added suite is
the two-method quintic checker, whose observed unittest time was
1.066 seconds. Repeated runs and inline diagnostics do not
increase these counts. The regression checks finite exact
identities, not the quantified socle, flatness, divisor or
classification theorems.

This checkpoint consolidates the separately frozen working53
and working54 packets. Their historical standalone-only flags
remain unchanged. The
[construction audit](research/proof-audits-pass53-working.md) and
[geometric audit](research/proof-audits-pass54-working.md)
record independent AI reconstructions and source boundaries.
There is no human expert review, Lean proof, historical novelty
certification or general cancellation solution.

Reproduce the finite checks with:

~~~sh
/opt/anaconda3/bin/python research/run_regression_pass54.py
/opt/anaconda3/bin/python research/quintic_correction_checks_pass53.py
/opt/anaconda3/bin/python research/consistency_checks_pass54.py
~~~

[^1]: [Foundational quotient audit](research/intrinsic-quotient-foundation-audit-pass51.md), including the actual primitive normalization and the application of Kaliman--Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), Theorem 2.7 and Corollary 2.8(2). Faithful flatness uses the explicitly checked dimension equality and [Stacks 00R4](https://stacks.math.columbia.edu/tag/00R4). No invariant ambient coordinate is inferred.

[^2]: David Eisenbud and Bernd Ulrich, [*Duality and socle generators for residual intersections*](https://arxiv.org/pdf/1309.2050v4), arXiv:1309.2050v4, 10 July 2016, Appendix Section 8 and Theorem 8.1, printed pp. 40--41. The used input is the classical characteristic-zero, zero-dimensional complete-intersection socle theorem, not a statement about arbitrary residual intersections.

[^3]: The Stacks Project, [0C0S(2)](https://stacks.math.columbia.edu/tag/0C0S) for coefficient-compatible completion after algebraic closure, and [07ZA(3)](https://stacks.math.columbia.edu/tag/07ZA) for Fitting base change.

[^4]: The Stacks Project, [Smooth morphisms, 01V4](https://stacks.math.columbia.edu/tag/01V4), Lemma 29.35.14 and the nearby differential exact sequence. Relative differential coordinates are chosen only locally after the transverse field has been specified.

[^5]: The Stacks Project, [00LM](https://stacks.math.columbia.edu/tag/00LM), flat preservation of regular sequences; [0AG0](https://stacks.math.columbia.edu/tag/0AG0), regular local UFDs; [01WS](https://stacks.math.columbia.edu/tag/01WS), effective Cartier local equations.

[^6]: The Stacks Project, [00TS](https://stacks.math.columbia.edu/tag/00TS), the closed-point regularity and cotangent-dimension criterion. The application is to an affine neighborhood of the exact quartic complete intersection, with its local dimension established beforehand.
