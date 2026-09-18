# Quadratic slice selection and coordinate-frame constraints

Quadratic generation over an invariant base does not by itself
supply a low-degree slice, even when the ambient algebra is an
invariant localization of polynomial affine four-space. A smooth
faithfully flat example below has nonempty fibers, independent
translation speeds, and two nonzero quadratic accelerations, but
minimum slice-gauge degree exactly three. Its selected generators
fail the genuine coordinate hypothesis at an explicit point.

A separate positive result gives a finite free module and a
two-generated ideal that detect affine generic slices exactly.
A radial sufficient condition is stronger: it forces a retraction
to the invariant base, and consequently cannot hold across a
primitive plinth divisor. These results constrain a proposed
recognition argument. They do not prove complex-threefold
cancellation or show that an arbitrary sliced action admits the
coordinate frame studied here.

## 1. Problem and actual-frame hypotheses

The working cancellation question is
\[
A[s_*]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The intended correction and field specialization of the original
professor-supplied statement have not been confirmed. The original
conclusion \(\mathbb A^1\) has a dimension mismatch when \(r>1\).

The conditional branch considered here starts with an actual
polynomial coordinate system \(x_1,\ldots,x_4\) on
\(B=A[s_*]\), an LND \(E\) with \(Es_*=1\), and the previously
derived independent degree-two frame. In particular,
\[
E^3x_i=0,\qquad
\operatorname{ad}_E^2\partial_{x_i}=0\ (i=1,2),\qquad
\operatorname{ad}_E^3\partial_{x_i}=0\ (i=3,4).
\tag{2}
\]
The two highest bad fields are independent. Neither (2) nor its
existence for a general cancellation instance is inferred from
a generic parametrization.

The [actual generic-pair theorem](research/generic-bad-pair-pass44.md)
and the intrinsic quotient results give a primitive nonzero LND
\(D\) on \(A\), a polynomial invariant surface \(C=\ker D\),
and a faithfully flat inclusion \(C\subset A\). At a closed
base point put \(R=C_{\mathfrak m}\), \(L=\operatorname{Frac}R\),
\(\mathcal A=A_R\), and \(\mathcal B=B_R\). The exact graph is
\[
\mathcal B_L=L[x_3,x_4],\quad
\mathcal A_L=L[j],\quad j=gx_3-fx_4,\quad
E=f\partial_{x_3}+g\partial_{x_4},
\]
\[
x_i=\mathcal Q_i(x_3,x_4),\quad
\deg\mathcal Q_i\le2\ (i=1,2),\quad
\mathcal B\cap L=R.
\tag{3}
\]
The speeds \(f,g\in R\) are algebraically independent over
\(\mathbb C\), but need not be coprime. The two good
accelerations \(h_i=E^2x_i\) also lie in \(R\).

There are actual commuting invariant derivations
\[
K_3=-\Delta\partial_{x_4},\qquad
K_4=\Delta\partial_{x_3},\qquad 0\ne\Delta\in R.
\tag{4}
\]
Their generic expressions do not authorize division by \(\Delta\)
in the actual ring.

## 2. A finite module for affine generic slices

Define
\[
V=\mathcal B\cap L[x_3,x_4]_{\le1}.
\tag{5}
\]
Equivalently, \(V\) is the common kernel of
\(K_3^2,K_3K_4,K_4^2\) in \(\mathcal B\). Characteristic zero
and (4) identify these with the three second partial derivatives.

For \(F\in V\), let
\[
\alpha=K_4F,\quad \beta=-K_3F,\quad
\gamma=\Delta F-\alpha x_3-\beta x_4.
\]
Each expression is actual and generically constant, so all three
belong to \(R\). Hence the full coefficient lattice
\[
\Gamma=\{(\gamma,\alpha,\beta)\in R^3:
  \gamma+\alpha x_3+\beta x_4\in\Delta\mathcal B\}
\tag{6}
\]
is isomorphic to \(V\), by division of the displayed numerator
by \(\Delta\). It contains \(\Delta R^3\) and is a submodule
of the finite module \(R^3\). Thus \(V\) is finite torsion free
of rank three. All prime multiplicities of \(\Delta\) remain
in this condition.

Invariant localization commutes with the three kernel equations.
The actual embedded height-one intersection for \(\mathcal B\)
therefore implies
\[
V=\bigcap_{\operatorname{ht}\mathfrak p=1}V_{\mathfrak p}
\quad\text{inside }L+Lx_3+Lx_4.
\tag{7}
\]
The finite-module intersection criterion makes \(V\) reflexive;
over the regular local surface \(R\), it is free.[^1][^2]
Faithful flatness gives \(1\notin\mathfrak mV\). Extending this
unimodular element to a basis gives
\[
V=R\cdot1\oplus Ru\oplus Rv.
\tag{8}
\]
This is a module basis, not an ambient coordinate system.

Since \(E(V)\) consists of actual generic constants, it is an
ideal of \(R\). In terms of either description,
\[
\mathfrak s_{\mathrm{aff}}=E(V)=(Eu,Ev)R
 =\left\{\frac{f\alpha+g\beta}{\Delta}:
       (\gamma,\alpha,\beta)\in\Gamma\right\}.
\tag{9}
\]
Every quotient on the right is in \(R\) because it is the
actual derivative of the corresponding element of \(V\).
This is not a claim about arbitrary coefficient triples.

The exact criterion and kernel are
\[
\boxed{\text{an actual affine generic \(E\)-slice exists}
       \iff \mathfrak s_{\mathrm{aff}}=R,}
\]
\[
0\longrightarrow F_1(\mathcal A)\longrightarrow V
  \xrightarrow{E}\mathfrak s_{\mathrm{aff}}\longrightarrow0,
\qquad F_1(\mathcal A)=\ker D^2.
\tag{10}
\]
The inclusion \((f,g,h_1,h_2)R\subseteq\mathfrak s_{\mathrm{aff}}\)
follows from \(x_3,x_4,Ex_1,Ex_2\in V\). Neither a free middle
module nor an arbitrary supplied slice makes this ideal a unit.
The complete argument is in the
[affine-slice module note](research/affine-slice-module-pass57.md).

## 3. A smooth faithful example with minimum gauge three

Let
\[
R=\mathbb C[a,v]_{(a,v-1)},\qquad
\mathcal A=R[t,z]/(t^2-v-az),\qquad
\mathcal B=\mathcal A[s],\qquad E=\partial_s.
\tag{11}
\]
Here \(v\) is a unit and \(a\) is not. These are actual
invariant localizations of \(\mathbb C[a,t,z]\) and
\(\mathbb C[a,t,z,s]\), with \(v=t^2-az\).

The monic presentation gives
\[
\mathcal A=R[z]\oplus tR[z].
\tag{12}
\]
This proves faithful flatness over \(R\). The relative
Jacobian ideal \((2t,a)\) is the unit ideal because it contains
\(v=t^2-az\). Thus the relative algebra and its cylinder are
smooth. Their whole closed fibers are respectively
\(\mathbb C[z]\times\mathbb C[z]\) and
\(\mathbb C[z,s]\times\mathbb C[z,s]\), so neither is empty.

Put
\[
w=as+tz,\qquad q=ts+z^2.
\]
The exact identities
\[
aq=tw-vz,\qquad vs=tq-zw
\tag{13}
\]
give \(\mathcal B=R[t,w,z,q]\) and recover the actual slice
\(s=(tq-zw)/v\). Only the unit \(v\) is inverted in this
reconstruction.

The generic pair \((t,w)\) generates the whole polynomial
plane: \(z=(t^2-v)/a\) and
\(s=w/a-t(t^2-v)/a^2\) are polynomials over \(L\).
Choose the four actual \(R\)-generators
\[
X=w,\qquad Y=vw+t,\qquad
Q_1=z+w^2,\qquad Q_2=q+w^2.
\tag{14}
\]
With \(T=Y-vX\), their generic expressions are
\[
Q_1=\frac{T^2-v}{a}+X^2,\qquad
Q_2=\frac{TX}{a}-\frac{v(T^2-v)}{a^2}+X^2.
\tag{15}
\]
Both have total degree at most two in \(X,Y\). Their derivatives
satisfy
\[
EX=a,\quad EY=av,\quad EQ_1=2aX,\quad EQ_2=t+2aX,
\qquad E^2Q_1=E^2Q_2=2a^2.
\tag{16}
\]
The speeds \(a,av\) are algebraically independent over
\(\mathbb C\); their common factor \(a\) is retained.

Use the affine generic slice \(\sigma_0=w/a\). Because
\(\ker E=\mathcal A\), the gauges of all actual slices form
the complete coset
\[
-\frac{tz}{a}+\mathcal A
=-\frac{t(t^2-v)}{a^2}+\mathcal A
\quad\text{in }L[t].
\tag{17}
\]
Suppose it contained a polynomial of degree at most two.
The involution \(t\mapsto-t\), fixing \(z\), preserves
\(\mathcal A\). Taking odd parts would give
\[
t\left(-\frac za-\lambda\right)\in\mathcal A
\quad\text{for some }\lambda\in L.
\tag{18}
\]
By the monic basis (12), this requires
\(-z/a-\lambda\in R[z]\), impossible because its \(z\)
coefficient is \(-1/a\). The displayed supplied gauge has
degree three. Therefore
\[
\boxed{\min_{E\sigma=1}\deg_t(\sigma-\sigma_0)=3.}
\tag{19}
\]
This proof quantifies over every actual slice, not just a
family of chosen high-degree replicas.

The direct affine module is also exact. Substituting
\(w=as+tz\) in \(\lambda w+\mu t+c\) and comparing first
the \(s\) coefficients and then the monic basis gives
\[
V=R\cdot1\oplus Rt\oplus Rw,\qquad E(V)=aR.
\tag{20}
\]
Thus the whole ring has a slice while its affine-slice
ideal is proper.

The necessary boundary is equally explicit. At the surviving
point \((a,t,z,s)=(0,1,0,0)\), the Jacobian of
\((Q_1,Q_2,X,Y)\) in \((a,t,z,s)\) is
\[
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
0&0&1&0\\
0&1&1&0
\end{pmatrix},
\quad\text{of rank three.}
\tag{21}
\]
These four generators are not even local coordinates there.
Generation over an already available invariant base does not
imply the absolute coordinate property required in (2).

For the intrinsic action \(D=a\partial_t+2t\partial_z\),
the first filtration is \(R\oplus Rt\), and both the
plinth and second image are \(aR\). The second-image
correction ideal is a unit. This example is not a residual
second-image obstruction. It already has intrinsic algebra
generators \(t,z\) of degrees one and two.

For any gauge of degree \(n\ge3\), projection of \(Q_1\)
has degree exactly \(2n\), while the other selected
projections have degree at most \(2n\). The minimum maximum
degree of that projected list is six, not the minimum
generating degree of the algebra. See the
[full faithful-control proof](research/faithful-quadratic-slice-boundary-pass57.md).

The earlier [smooth flat control](research/quadratic-slice-selection-boundary-pass55.md)
also had minimum gauge three, but missed the closed fiber.
The example (11) removes that limitation. It does not establish
a bound of three in general or realize the genuine full frame.

## 4. Why radial regularity is too strong on the plinth locus

For a center \(\eta\), consider
\[
\Theta_\eta=(x_3-\eta_3)\partial_{x_3}
          +(x_4-\eta_4)\partial_{x_4}.
\tag{22}
\]
If it preserves \(\mathcal B\), then
\(\eta_i=x_i-\Theta_\eta x_i\in\mathcal B\cap L=R\).
Thus rational centers cannot silently bypass regularity.

For a chosen actual center, (4) makes regularity equivalent
to two full-divisibility tests:
\[
(x_3-\eta_3)K_4x_i-(x_4-\eta_4)K_3x_i
       \in\Delta\mathcal B,\qquad i=1,2.
\tag{23}
\]
The denominator is the entire \(\Delta\), including every
multiplicity. Generic regularity or radical divisibility
does not suffice.

If (23) holds, finite spectral projection extracts homogeneous
components of every actual polynomial. Its constant component is
\[
\prod_{k=1}^{d}\frac{k-\Theta_\eta}{k}F
     =F(\eta_3,\eta_4)\in R.
\tag{24}
\]
Although the operator depends on a degree bound \(d\), its
output is ordinary evaluation. Hence (24) defines one unital
\(R\)-algebra retraction \(\mathcal B\to R\).

Write the full primitive plinth as \(pC\). For every prime
\(\pi\in C\), the inherited whole-divisor argument gives
\[
A_{C_{(\pi)}}/\pi A_{C_{(\pi)}}=F_\pi[t],\quad
B_{C_{(\pi)}}/\pi B_{C_{(\pi)}}=F_\pi[t,s_*],
\]
\[
[F_\pi:\kappa]=1\iff\pi\nmid p,
\qquad \kappa=\operatorname{Frac}(C/\pi C).
\tag{25}
\]
Primitivity makes the residue derivation nonzero. Its
algebraic invariant ring is a finite field, and a local
slice gives the displayed polynomial line. If \(\pi\mid p\)
but this field were \(\kappa\), subtracting the residue value
of a minimal slice and dividing by \(\pi\) would contradict
minimality of the full plinth.

At \(\pi\mid p\), a residue retraction would restrict to a
unital \(\kappa\)-algebra embedding \(F_\pi\to\kappa\).
A proper finite extension admits no such map. Therefore
\[
\boxed{\pi\mid p\Longrightarrow
 \text{no regular radial center over }C_{(\pi)}.}
\tag{26}
\]
This needs only a proper extension, not its specialized
quadratic degree. A regular radial center over \(C_{\mathfrak m}\)
therefore forces \(p\notin\mathfrak m\). No converse is proved.

The [determinant argument](research/acceleration-divisor-extension-pass45.md)
gives \(p\mid\Delta\), not equality. Extra determinant factors
retain the unresolved full-power tests (23).

The positive [radial projection theorem](research/radial-slice-descent-pass55.md)
is still valid: when (23) holds, the degree-one spectral
projector sends any supplied \(E\)-slice to an actual affine
generic slice. It cannot be used where (26) forbids its premise.

An already polynomial cylinder illustrates nonnecessity. On
\(\mathbb C[a,y,z,s]\), take \(E=\partial_s\),
\(D=a\partial_y+2y\partial_z\), and \(v=y^2-az\).
The actual coordinates
\((a+s^2,z+s^2,s,y+s)\) have two quadratic accelerations.
Over the invariant DVR \((a)\), the residue constant field
is \(\mathbb C(v)(\sqrt v)\), so no radial center exists,
although \(s\) is an affine generic slice. Its adjoint
profile is not the unresolved independent profile. The
[divisor proof](research/radial-dvr-scope-pass56.md) gives
the complete computation.

## 5. Local centers and the exact patching obstruction

The two tests (23) form a linear equation in
\(\mathcal T=(\mathcal B/\Delta\mathcal B)^2\).
Put
\[
u=(K_4x_i)_i,\quad v=(-K_3x_i)_i,\quad
n=(x_3K_4x_i-x_4K_3x_i)_i\pmod{\Delta\mathcal B},
\]
\[
M=\ker(R^2\xrightarrow{(\eta_3,\eta_4)\mapsto
                         \eta_3u+\eta_4v}\mathcal T),
\qquad Q=(Rn+Ru+Rv)/(Ru+Rv).
\tag{27}
\]
The ambient target need not be finite, but \(Q\) is a
finite cyclic module. Existence of a center is exactly
\(Q=0\). Height-one solvability only makes \(Q\) finite
length at the closed point.

For parameters \(a,b\), local solutions on \(D(a)\) and
\(D(b)\) have a choice-independent difference class
\[
\omega\in M_{ab}/(M_a+M_b).
\tag{28}
\]
Its vanishing is equivalent to a global center in this
actual-ring setting. After gluing the coefficients in
\(R_a^2\cap R_b^2=R^2\), one must still use the embedded
height-one intersection to make both quotients in (23)
actual. The equivalence is false for unrestricted module
targets with classes supported only at the closed point.

Even a free \(M\) need not give vanishing: the formal
congruence \(b\eta_3=1\bmod aR\) has
\(M=aR\oplus R\), \(Q=R/(a,b)\), and no global solution.
This is a module countercontrol, not an actual frame.
Moreover, (26) already defeats local existence in the
plinth sector before patching becomes relevant. The
[patching proof](research/radial-center-patching-pass56.md)
retains these distinctions.

## 6. Leading-image constraints remain necessary, not sufficient

Let \(D=\mu\partial_j\) generically, define
\(F_n=\ker D^{n+1}\), \(I_n=D^nF_n\), and
\[
M_n=\frac{I_n}{n!\mu^n}\subset L.
\tag{29}
\]
This fractional ideal consists exactly of degree-\(n\)
leading coefficients of actual members of \(F_n\).

If an actual slice has minimum gauge degree \(n\ge2\)
with leading coefficient \(\lambda\), its two bad
projections have leading coefficients \(-f\lambda\)
and \(-g\lambda\). If \(\lambda\) itself lifted from
\(M_n\), subtraction of that actual invariant would
lower the gauge. Hence
\[
0\ne[\lambda]\in(M_n:(f,g))/M_n.
\tag{30}
\]
The class is necessary, not sufficient to construct a slice.

When \(M_n=cR\), unique factorization gives
\((M_n:(f,g))=(c/\gcd(f,g))R\). Thus a principal image
excludes minimum degree \(n\) only when the original
speeds are coprime. Normalizing \(j\) does not divide
the original action or remove a common speed factor.

Under the additional reduced zero-first-jet and
parameter-speed assumptions, the previously proved
identities are
\[
I_3=p^2R,\qquad I_4=p^2(a,b),\qquad I_5=p^3R,
\quad F_3=F_2\oplus Rt,\quad bU-aV=-2t+\eta,\ \eta\in F_2.
\tag{31}
\]
Principal images exclude minimum degrees three and five.
A hypothetical degree-four gauge has a unit leading
coefficient after division by \(p^2\). Its two bad
projections are the same unit multiple of \(U,V\)
modulo \(F_3\). Their determinant would have a unit
\(t\)-coefficient, contradicting its membership in
\(F_1\). Together with the established lower-degree
generation obstruction, this gives a conditional
minimum gauge at least six, not existence of such a
point or an upper bound. The
[leading-image proof](research/slice-leading-image-obstruction-pass55.md)
specifies the extra hypotheses and basis change.

## 7. Recognition theorems retain their actual hypotheses

Properness is already supplied by \(B=A[s_*]\), but an
arbitrary invariant is not an invariant ambient coordinate.
Kaliman's proper-action theorem supplies recognition only
after that coordinate premise is proved.[^3]

The current nice/quasi-nice image-ideal results concern
actual polynomial presentations over a fixed base. A
generic polynomial plane and two coordinates killed by
\(E^2\) do not establish that relative presentation.[^4]

Likewise an affine-plane fibration requires polynomial
fibers at every base prime, not merely a generic plane,
smoothness and faithful flatness. The proper finite
constant fields in (25) violate that premise.[^5]
A DVR hypersurface coordinate theorem that assumes its
quotient is \(R^{[2]}\) cannot supply that assumption from
the weaker data of the faithful example.[^6]

These are bounded applicability conclusions. They do not
establish that no relevant theorem exists or certify
historical novelty. Exact access and version boundaries
are retained in the separate source audits.

## 8. Evidence and unresolved obligations

The written results above integrate the independently audited
working55, working56 and working57 notes. The separate
[proof records](research/proof-audits-pass57-working.md)
distinguish complete algebraic reconstructions, primary
theorem applications and finite identity controls.

No new reusable test methods or suites arise from these
deductions. The accompanying full regression reruns the
same 995 methods in 123 suites as the preceding checkpoint.
Its captured output is in [verification-pass-57.json](verification-pass-57.json).
Those finite checks do not verify all-slice quantifiers,
every source theorem, or the general cancellation claim.

The remaining mathematical obligation is not to prove
a false quadratic-generator shortcut. A positive slice
selection argument must use additional genuine
coordinate-frame and adjoint equations, or another
recognition route must replace that step. Even complete
recognition of the supplied frame would leave the
unrestricted frame-reduction problem.

There is no unrestricted cancellation solution, human
expert review, proof-assistant verification, professor
confirmation, or historical novelty certification here.

## Sources

[^1]: The Stacks Project, [Tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB), finite torsion-free height-one intersection criterion for reflexivity, complete statement and proof.
[^2]: The Stacks Project, [Tag 0B3N](https://stacks.math.columbia.edu/tag/0B3N), reflexive modules on regular schemes of dimension at most two, complete statement and proof.
[^3]: Shulim Kaliman, [*Proper Ga-actions on C4 preserving a coordinate*](https://msp.org/ant/2018/12-2/ant-v12-n2-p01-s.pdf), Algebra & Number Theory 12 (2018), 227–258, Theorem 0.1 and Corollary 0.3.
[^4]: Nikhilesh Dasgupta and Animesh Lahiri, [*On image ideals of nice and quasi-nice derivations on R[X1,X2]*](https://arxiv.org/pdf/2302.13787v6), arXiv:2302.13787v6, 24 July 2026, Definitions 2.2–2.3 and the stated relative polynomial-plane hypotheses.
[^5]: Janaki Raman Babu and Prosenjit Das, [*Structure of A2-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/pdf/2001.07632v5), arXiv:2001.07632v5, definition of affine fibration, Lemma 4.2 and Theorem 4.4.
[^6]: Prosenjit Das and Amartya K. Dutta, [*Planes of the form b(X,Y)Z^n−a(X,Y) over a DVR*](https://arxiv.org/pdf/2002.02118v1), arXiv:2002.02118v1, Theorem 5.3 and its actual polynomial-quotient premise.
