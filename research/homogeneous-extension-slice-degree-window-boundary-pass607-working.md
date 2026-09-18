# Slices and the degree window for homogeneous extensions

Date: 2026-09-17

Status: bounded working proof, pending independent saved-source review.
The positive-q implication stated as open below is not a theorem of this
note. No general cancellation, coordinate-entry, or novelty claim is made.

## 1. Results and the remaining question

Let R=C[x,y,z], let H be a nonzero ordinary-homogeneous LND of
derivation degree d>0, and let psi be ordinary homogeneous of degree ell.
On B=R[t] consider the triangular LND

\[
E=H+(1+\psi)\partial_t,\qquad q=\ell-d,\qquad
N=\max\{\deg_Hx,\deg_Hy,\deg_Hz\}.
\tag{1}
\]

The maximal LND degree N is positive. As usual, deg_H(0)=-infinity.
Irreducibility means that the coordinate coefficients of H have no
nonconstant common divisor. All explicit bases below have this property.

This note establishes the following bounded statements.

1. Sliceness does not force q>0. There is an explicit irreducible example
   with q=0, a completed polynomial slice, and no base shear that lowers
   the E-degree of the displayed coordinate t.
2. For H_j=x^j partial_y+y^j partial_z, j>=2, and every homogeneous
   psi of degree ell>=j, sliceness forces deg_H psi<=(ell-j+1)(j+1)-1.
   The proof uses the entire coefficient, not just a monomial ansatz.
3. For q>=1, every polynomial slice has a finite normalized weighted
   recurrence. An overcritical coefficient with deg_H psi=k>=qN would
   require normalized slice weight at least q+(k+1)ell.
4. A sliced example strictly below the critical equality still admits
   no lowering base shear. The particular unsliced coefficient psi=yz
   supplies a polynomial-endpoint control of the general formal proof.

The following possible positive-q implication remains UNPROVED here:

\[
\begin{gathered}
H\text{ irreducible},\quad d>0,\quad q=\ell-d\ge1,
\quad E\text{ sliced}
\\
\Longrightarrow\quad \deg_H\psi\le qN-1.
\end{gathered}
\tag{2}
\]

The q=0 example does not refute (2). The theorem for H_j proves (2)
only for that explicit class of bases, not for all irreducible homogeneous
H. The height bound gives a necessary condition on a hypothetical
overcritical slice, not an upper bound that rules it out in general.

For comparison, [605](irreducible-homogeneous-top-removal-via-plane-valuations-pass605-working.md)
removes the top term at the critical equality k=qN-1 for irreducible H.
The sliced examples in [598](homogeneous-sliced-first-shift-image-kernel-counterexample-pass598-working.md)
already occupy that equality after a gauge; the promotion in
[599](homogeneous-extension-gauge-first-shift-promotion-pass599-working.md)
assumes the inequality in (2). Neither supplies the missing implication.
No unfinished neighboring source is used.

## 2. A primitive sliced boundary at q=0

Take

\[
H=x^4\partial_y+y^4\partial_z,\qquad
\psi=x^2y,\qquad
E=H+(1+x^2y)\partial_t.
\tag{3}
\]

The derivation H is triangular and locally nilpotent. Its coefficients
x^4 and y^4 are relatively prime, so H is irreducible. It has ordinary
derivation degree d=3, while ell=3. Its whole y,z flow gives exact degrees

\[
\deg_H(x,y,z)=(0,1,5),\qquad N=5,\qquad q=0,
\qquad \deg_H\psi=1,\quad \deg_Et=2.
\tag{4}
\]

For example, y maps to y+x^4 w and z maps to
z+sum_{j=0}^4 binom(4,j)y^(4-j)x^(4j)w^(j+1)/(j+1),
whose final coefficient is nonzero. Also E^2t=x^6 and E^3t=0.

Put a=x^2, which is E-invariant, and define whole polynomials

\[
V=at-y^2/2,\qquad Q=aV-y,\qquad
U=t-yV+aV^2/2.
\tag{5}
\]

Direct differentiation and expansion give

\[
EV=a,\qquad EQ=0,\qquad aU=V+Q^2/2,
\qquad EU=1.
\tag{6}
\]

The last equality follows by applying E to the preceding identity and
cancelling the nonzero a in the domain. It is a polynomial identity;
the claimed slice is not being defined after inverting a.

In fact (x,Q,U) is an actual coordinate system on C[x,y,t]. Its whole
inverse is

\[
\begin{aligned}
y={}&a^2U-aQ^2/2-Q,\\
t={}&U+\frac{a^3U^2}{2}-\frac{a^2UQ^2}{2}-aUQ
       +\frac{aQ^4}{8}+\frac{Q^3}{2},\qquad a=x^2.
\end{aligned}
\tag{7}
\]

Both substitution orders give the identity. To complete this to all
four coordinates, write B0=-aQ^2/2-Q and put

\[
P(x,Q,U)=\sum_{j=0}^4\binom4j
              a^{2j}B_0^{4-j}\frac{U^{j+1}}{j+1},
\qquad Z=z-P(x,Q,U).
\tag{8}
\]

Here partial_U P=(a^2U+B0)^4=y^4, so EZ=0. The inverse first uses
(7) and then z=Z+P. Thus
B=C[x,Q,Z,U], E=partial_U, and ker E=C[x,Q,Z]. This is a recognized
translation, not a cancellation counterexample.

Nevertheless, no polynomial P0 in the original base R can satisfy
deg_E(t-P0)<2. Such an inequality would imply

\[
H^2P_0=x^6.
\tag{9}
\]

Decompose P0 into its ordinary homogeneous components P0,j. Since H
has degree 3, H^2P0,j is either zero or homogeneous of degree j+6.
Only j=0 could contribute the degree-six right side, but H^2 annihilates
constants. Equation (9) is impossible. The same proof treats
lambda t+P0 with any lambda in C*: its required right side is a
nonzero complex multiple of x^6.

This is an obstruction for every fixed-base shear, not just a chosen
homogeneous shear. It does not obstruct the nonlinear completed slice
(5)--(8). The already actual all-positive frame
(x+z,y+z,z,t), of degrees (5,5,5,2), has the same fixed-base obstruction.
It is not a globally minimizing frame, as the displayed rectification
also supplies (x+U,Q+U,Z+U,U), with all four degrees equal to one.

## 3. The positive-q bound for the entire triangular class H_j

Fix an integer j>=2 and set

\[
H_j=x^j\partial_y+y^j\partial_z,\qquad
d=j-1,\quad N=j+1,\quad
\psi=\sum_{a+b+c=\ell}\gamma_{abc}x^ay^bz^c,\quad
\ell\ge j,\quad q=\ell-j+1.
\tag{10}
\]

The coefficients gamma_abc are arbitrary complex numbers, including
zero. The zero polynomial psi trivially satisfies the desired bound.
The base is an irreducible homogeneous LND with exact coordinate degrees
(0,1,N), as follows by integrating y along the whole H_j-flow and then
integrating y^j. We prove that a nonzero coefficient with actual
k=deg_H psi>=qN makes E=H_j+(1+psi)partial_t unsliced.

First separate raw monomial degrees from possible cancellation. A
monomial x^a y^b z^c has exact H_j-degree r=b+Nc. At a fixed ordinary
degree ell, the condition r>=qN is equivalent to

\[
Na+jb\le j^2-1.
\tag{11}
\]

In particular 0<=b<=j-1=N-2. At a fixed pair (ell,r), the residue
b=r modulo N now determines b uniquely in this interval. It then
determines c=(r-b)/N and a=ell-b-c. Thus every raw degree r>=qN
has at most one degree-ell monomial. Its nonzero top H_j-coefficient
cannot cancel against any other term of psi. If the actual degree is
k>=qN, then k is exactly the greatest raw monomial degree with nonzero
coefficient. No larger raw degree was silently discarded.

Choose a primitive N-th root omega. For b,c>=0 define

\[
C_{bc}=\frac{(-1)^c c!\bigl(\omega^{b+1}-1\bigr)}
                  {\prod_{i=0}^c(b+1+Ni)}.
\tag{12}
\]

This constant is the polynomial-antiderivative integral
N^(-c) integral_1^omega T^b(T^N-1)^c dT. Indeed expansion of the
c-th power makes the numerator omega^(b+1)-1 common to every term,
and the exact partial-fraction identity is

\[
\sum_{i=0}^c\frac{(-1)^{c-i}\binom ci}{B+Ni}
 =\frac{(-1)^cN^c c!}{\prod_{i=0}^c(B+Ni)}.
\tag{13}
\]

For example, (13) follows by matching the simple-pole residues on both
sides as rational functions of B; their difference is a polynomial
vanishing at infinity. This proves the identity for every c, including
c=0. All denominators in (12) are positive integers. For the unique
overcritical monomial one has b<=N-2, so omega^(b+1) is not one and
C_bc is nonzero.

Start a full E-orbit at (x,v,0,0), temporarily with x and v invertible.
The time tau=(omega-1)v/x^j carries y to omega v and z to zero. Along
the orbit, using eta for the varying y-coordinate, one has
z=(eta^N-v^N)/(N x^j) and d tau=d eta/x^j. Integrating the entire
1+psi, with every coefficient retained, gives

\[
\Delta t=\frac{v}{x^j}
 \left[\omega-1+x^\ell P(v/x)\right],\qquad
P(T)=\sum_{a+b+c=\ell}\gamma_{abc}C_{bc}T^{b+Nc}.
\tag{14}
\]

Terms with the same lower exponent may combine or vanish. At the
greatest overcritical degree k, uniqueness from (11) and nonvanishing
in (12) show that the leading coefficient A_k of P is nonzero.
Consequently P has degree exactly k. This is the step where both
raw-degree cancellation and return-polynomial cancellation are checked.

Also k>ell, since
qN-ell=j(ell-j)+1>=1. Introduce a formal parameter s and set

\[
x=s^k,\qquad v=s^{k-\ell}V(s),\qquad
P(T)=\sum_{r=0}^k A_rT^r.
\tag{15}
\]

To make the entire bracket in (14) zero, solve

\[
\omega-1+A_kV(s)^k+
 \sum_{r<k}A_rs^{\ell(k-r)}V(s)^r=0.
\tag{16}
\]

Choose a nonzero complex V0 with V0^k=-(omega-1)/A_k. The derivative
of the left side with respect to V at (s,V)=(0,V0) is the nonzero
constant k A_k V0^(k-1). Formal coefficient recursion therefore gives
a unique V(s) in C[[s]] with constant term V0 satisfying (16): at each
successive power of s the new coefficient has precisely that nonzero
linear coefficient and all remaining terms are already determined.
No convergence, rationality, or polynomiality of V(s) is asserted.

The two entire endpoint arcs are
(s^k,s^(k-ell)V(s),0,0) and
(s^k,omega s^(k-ell)V(s),0,0), both in C[[s]]^4. Their full E-flow
time is

\[
\tau=(\omega-1)s^{-(j-1)k-\ell}V(s),
\tag{17}
\]

which has a pole because V(s) is a unit. The finite polynomial E-flow
is defined over C((s)); (14)--(16) prove all four endpoint equalities,
not merely their leading terms. If Eu=1 for a polynomial u, evaluation
of its identity exp(tau E)u=u+tau would make the difference of two
elements of C[[s]] equal to (17), an impossibility. Thus E is unsliced.

This proves (2) for every homogeneous psi and each entire base H_j in
(10). It is only a necessary condition. It is not a theorem about sums
of arbitrary homogeneous LNDs, other homogeneous bases, or arbitrary
four-variable coordinate presentations.

## 4. Exact normalization of a slice when q>=1

Return to (1), now with q>=1 and ell=d+q. Give x,y,z weight one
and t weight q. These are auxiliary positive grading weights, not an
assertion that they equal the actual E-degrees of these coordinates.
Write

\[
L=\partial_t,\qquad F=H+\psi\partial_t,\qquad E=L+F.
\tag{18}
\]

Then L and F are commuting LNDs of respective weights -q and d.
Triangular local nilpotence follows because the H-derivative sequence
of psi is finite. No polynomial slice of F is assumed or needed.

Suppose Eu=1 for a whole polynomial u. Both summands of E change
weight by d modulo ell. Consequently projecting u to its components
of weight q modulo ell preserves Eu=1; all other residue classes have
zero E-image separately. Since 0<q<ell, the retained nonnegative
weights are exactly q+i ell for integers i>=0.

There is therefore a normalized slice

\[
u^*=\sum_{i=0}^M U_i,\qquad
\operatorname{wt}(U_i)=q+i\ell,\qquad U_M\ne0,
\tag{19}
\]

where zero intermediate components are permitted. Comparing its whole
E-image weight by weight gives precisely

\[
LU_0=1,\qquad
FU_i+LU_{i+1}=0\ (0\le i<M),\qquad FU_M=0.
\tag{20}
\]

There is no negative-weight term or omitted boundary equation. The
first equation has weight zero; the middle equations have weights
(i+1)ell, and the final one has weight (M+1)ell.

A polynomial of weight q contains t only linearly, with a constant
coefficient. Hence

\[
U_0=t+P_q,\qquad P_q\in R_q,
\qquad \chi:=FU_0=\psi+H(P_q)\in R_\ell.
\tag{21}
\]

When M=0, the entire recurrence says exactly chi=0. Conversely,
chi=0 makes U0 itself a slice. Even if a particular normalized slice
contains higher components, chi=0 permits replacing it by U0 and
taking M=0. This handles the zero-chi case without defining its
nilpotency degree as a nonnegative integer.

For fixed M, (20) is an exact finite linear coefficient problem.
One equivalent way to parameterize it is to define the polynomial
antiderivative J_t by J_t(t^j A)=t^(j+1)A/(j+1) for A in R. Then

\[
U_{i+1}=Q_{i+1}-J_t(FU_i),\qquad
Q_{i+1}\in R_{q+(i+1)\ell},
\tag{22}
\]

with the final equation FU_M=0 still required. Formula (22) does not
assert that the terminal equation is solvable. A complete fixed-M
test expands the finite monomial bases at the weights in (19), applies
the entire E, and compares all resulting coefficients with 1.

The recurrence is equivalent to sliceness only after allowing some
finite M. No uniform upper bound on that M has been proved here.

## 5. A necessary height bound for an overcritical slice

Assume chi is nonzero, so M>=1. For every 1<=i<=M the recurrence gives

\[
\deg_t U_i\le i,\qquad
[t^i]U_i=\frac{(-1)^i}{i!}H^{i-1}\chi.
\tag{23}
\]

For i=1 this is U1=-t chi+Q1. Inductively, the coefficient of t^i
in FUi is H([t^i]Ui): the term psi partial_t lowers t-degree, and
deg_t Ui<=i. Integrating the recurrence proves the next coefficient
and the t-degree bound, including the case when that coefficient is
zero. The integration constant Q_i introduces no t-term.

The coefficient of t^M in the terminal equation FU_M=0 is therefore
(-1)^M H^M chi/M!. In particular

\[
H^M\chi=0,\qquad M\ge\deg_H\chi+1.
\tag{24}
\]

This conclusion does not require the top displayed t-coefficient of
U_M to be nonzero. It uses the entire terminal equation, not only an
ansatz for that coefficient.

Every polynomial in R_q has H-degree at most qN, by the product rule
for LND degree. Thus H(Pq), when nonzero, has H-degree at most qN-1.
If the actual coefficient is overcritical, meaning

\[
k:=\deg_H\psi\ge qN,
\tag{25}
\]

no possible Pq in (21) changes its top: deg_H chi=k. Every normalized
slice would consequently satisfy

\[
M\ge k+1,\qquad
\max\operatorname{wt}(u^*)=q+M\ell
                 \ge q+(k+1)\ell.
\tag{26}
\]

Irreducibility of H was not used in this recurrence or height bound.
In the setting of (2) it is an additional retained hypothesis, not a
missing step that turns the lower bound (26) into a contradiction.

## 6. Strict inequality does not guarantee fixed-base descent

For another entire coefficient over H_2 take

\[
H=x^2\partial_y+y^2\partial_z,\qquad
\psi=xy,\qquad E=H+(1+xy)\partial_t.
\tag{27}
\]

Here d=q=1, ell=2, N=3, and deg_H psi=1<qN-1=2. Equations
(5)--(7), now with a=x rather than x^2, give EQ=0 and EU=1 and the
same whole polynomial coordinate inverse on C[x,y,t]. To complete the
four-ring coordinates, use (8) with exponent four replaced throughout
by two, namely P=B0^2 U+a^2 B0 U^2+a^4 U^3/3. Its U-derivative is
then y^2, so Z=z-P is invariant and the whole E is again a translation
in (x,Q,Z,U).

But deg_E t=2, and any lowering base shear would require

\[
H^2P_0=H(xy)=x^3.
\tag{28}
\]

As H has ordinary degree one, only the degree-one part of P0 could
contribute to the right side. On R_1 one has
H^2x=H^2y=0 and H^2z=2x^2y. Its image cannot contain x^3. Thus no
polynomial base shear lowers this t-degree, despite the positive q,
strict inequality, and known whole rectification.

The theorem of Section 3 is therefore not a terminating fixed-base
reduction algorithm. The critical equality in605 can be removed;
strictly smaller coefficients can require a different coordinate move.

## 7. A polynomial-endpoint control of the overcritical obstruction

Consider the separate entire derivation

\[
H=x^2\partial_y+y^2\partial_z,\qquad
\psi=yz,\qquad E=H+(1+yz)\partial_t.
\tag{29}
\]

Here H is irreducible, d=1, ell=2, q=1, and the base degrees are
(0,1,3), so N=3. Direct differentiation gives
H^4(yz)=8x^6 and H^5(yz)=0. Thus k=4, deg_Et=5, and the coefficient
is overcritical. Formula (26) requires M>=5 and normalized slice
weight at least 11, but does not itself exclude such a slice.

There is instead an exact polynomial-flow obstruction. For an
independent parameter tau the finite E-flow is

\[
\begin{aligned}
x_\tau={}&x,\\
y_\tau={}&y+x^2\tau,\\
z_\tau={}&z+y^2\tau+x^2y\tau^2+x^4\tau^3/3,\\
t_\tau={}&t+\tau(1+yz)
 +\frac{\tau^2}{2}(x^2z+y^3)
 +\frac23\tau^3x^2y^2
 +\frac13\tau^4x^4y+\frac1{15}\tau^5x^6.
\end{aligned}
\tag{30}
\]

Choose a primitive cube root zeta and a nonzero complex constant
kappa with kappa^2=(zeta+1)/10. These choices are possible because
zeta+1 is nonzero. For an independent variable epsilon put

\[
\begin{gathered}
p(\epsilon)=(\kappa\epsilon^2,\epsilon,0,0),\qquad
p'(\epsilon)=(\kappa\epsilon^2,\zeta\epsilon,0,0),\\
\tau(\epsilon)=\frac{10(\zeta-1)}{\zeta+1}\epsilon^{-3}.
\end{gathered}
\tag{31}
\]

Substitution in the entire formulas (30), using
zeta^2+zeta+1=0, gives

\[
\exp(\tau(\epsilon)E)\,p(\epsilon)=p'(\epsilon).
\tag{32}
\]

This notation denotes the point flow associated to (30); it is an
identity over C[epsilon,epsilon^(-1)]. Both endpoints themselves are
polynomial at epsilon=0, while the nonzero time has a pole there.

If a polynomial u satisfied Eu=1, its finite flow identity would be
u(p')-u(p)=tau. After (31), the left side belongs to C[epsilon], and
the right side is a nonzero constant times epsilon^(-3). This is
impossible. Hence (29) has no polynomial slice.

In fact the coordinate coefficients of E have no common zero: their
vanishing would give x=y=0 and then 1+yz=1. This observation does
not substitute for the flow proof and is not being promoted to a
slice criterion. No general properness or action-classification
theorem is used.

## 8. Scope and verification

Fresh unsaved exact algebra checked both substitution orders in (7),
all slice identities, the recurrence boundaries M=0,1,2, and the
entire flow (30) with all endpoint identities in (32). The endpoint
calculation reduced exact rational expressions modulo
zeta^2+zeta+1; it was not a numerical choice of a root. The general
recurrence and height bound are proved in Sections 4--5, not inferred
from those controls.

Separate exact checks reconstructed the partial-fraction constants,
the overcritical raw-degree uniqueness, and the entire return polynomial
with unrestricted homogeneous coefficient symbols in small triangular
cases. The all-j and all-ell argument is Section 3: its uniqueness
inequality, rational identity, and formal coefficient recursion handle
all lower terms without appealing to a finite grid.

An earlier finite coefficient search for (29) tested normalized
weights only through 15 and found no slice there. That bounded
failure was not a no-slice proof; (30)--(32) supply the independent
all-degree obstruction. No unbounded conclusion is based on the
finite search.

The q=0 and strictly subcritical xy examples are recognized polynomial;
the overcritical yz example is unsliced. Section 3 proves (2) for the
specific triangular bases H_j, while the version for arbitrary
irreducible ordinary-homogeneous H remains unproved. Even a proof of
that general implication would not put an arbitrary sliced derivation
on C^[4] into the homogeneous extension form (1), or justify an
iteration after a degree-lowering shear changes the relevant hypotheses.
Those entry and termination issues remain. No result here refutes or
proves general cancellation.

No saved checker was executed, imported, or compiled. No canonical
file, expert review, proof-assistant certificate, or external contact
is implied by this working note.
