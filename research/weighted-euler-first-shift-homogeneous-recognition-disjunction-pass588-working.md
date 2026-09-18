# Both homogeneous recognition tests can fail at first Euler shift

## 1. Exact conclusion and scope

There is an actual polynomial coordinate frame of a sliced four-ring
whose positive E-degree tuple is (10,10,10,1) and whose exact weighted
Euler shift is one, but which has neither:

1. A slice for E homogeneous under that actual weighted Euler derivation.
2. An E-invariant ambient coordinate homogeneous under the same Euler
   derivation.

The example even has three commuting, locally nilpotent Euler spectral
components. Thus the proposed universal disjunction between the two
homogeneous tests is false, including in that commuting case. This
defeats the homogeneous invariant-coordinate fallback that remained
available in585, which treated a different pair of tests.

The invariant ring in this example is explicitly polynomial. Complete
polynomial maps and inverses are supplied below. The result does not
refute general recognition at shift one, recognition after changing the
frame, a nonhomogeneous invariant-coordinate test, or cancellation.
There is no globally minimizing-frame or novelty claim.

The starting three-variable Jacobian derivation is Freudenburg's known
example. It is reproduced with exactly the polynomials used below in
Section 5 of Dasgupta and Gaifullin, *On locally nilpotent derivations of
polynomial algebra in three variables* (2025); their reference19 credits
Freudenburg's 1998 paper *Actions of Ga on A3 defined by homogeneous
derivations*. [Primary provenance and reproduced example](https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=10094&wshow=paper)
We do not invoke the stronger published rank-three assertion. Local
nilpotence and the absence of linear invariants needed here are proved
directly.

The definitions of exact Euler shift and corrected recovery agree with
576--577. The homogeneous tests agree with582 and586, but their complete
finite-weight obstruction is repeated here. No arbitrary invariant ring
is assumed polynomial in a general theorem.

## 2. The entire three-variable derivation and its local slice

In the actual polynomial ring R=C[x,y,z], set

\[
 f=xz-y^2,\qquad r=x^3+yf,\qquad
 g=zf^2+2x^2yf+x^5=zf^2+2x^2r-x^5.
\tag{1}
\]

Take the Jacobian convention
\(H(P)=\det J(f,g,P)\). Differentiating these complete polynomials gives

\[
 \begin{aligned}
 H(x)&=-2fr,\\
 H(y)&=6x^2r-g,\\
 H(z)&=2x(f^2+5yr).
 \end{aligned}
\tag{2}
\]

All three coefficients are ordinary homogeneous of degree five. Thus
H has ordinary derivation degree four. The entire identities are

\[
 Hf=Hg=0,\qquad Hr=-fg=:h,\qquad Hh=0.
\tag{3}
\]

In particular r is a homogeneous local slice of ordinary degree three,
and h is a nonzero homogeneous invariant of ordinary degree seven. Its
sign in (3) is fixed by the stated Jacobian convention.

Here is a direct global local-nilpotence proof, including the exact
orders needed later. Since f is nonzero, calculations in the injective
localization R[f^{-1}] can use

\[
 y=\frac{r-x^3}{f},\qquad
 z=\frac{g-2x^2r+x^5}{f^2}.
\tag{4}
\]

This localization is only a way to verify polynomial identities. It is
not a change of the actual ring in the construction. Formula (3) gives
H-degree one for r, and (2) gives

\[
 H^2x=2f^2g,\qquad H^3x=0.
\tag{5}
\]

The derivation on R[f^{-1}] is locally nilpotent on the algebra generated
by f,f^{-1},g,r,x. That algebra contains y,z by (4). Equivalently,
repeated differentiation of (4) shows H^7y=0 and H^11z=0.
Injectivity of localization makes these identities hold in R itself.
Since x,y,z generate R, this proves that H is an LND of the whole R.

For an independent indeterminate s, write the finite polynomial flow
\(\Theta_s=\exp(sH)\). Its two simplest identities are

\[
 \Theta_s(r)=r-fgs,\qquad
 \Theta_s(x)=x-2frs+f^2gs^2,
 \qquad \Theta_s(f)=f,\quad\Theta_s(g)=g.
\tag{6}
\]

Using (4) and these identities, the top s-coefficient in
\(\Theta_s(y)\) is \(-f^5g^3\) at degree six, and that in
\(\Theta_s(z)\) is \(f^8g^5\) at degree ten. Therefore

\[
 \begin{gathered}
 \deg_H(x,y,z)=(2,6,10),\\
 H^6y=-6!f^5g^3\ne0,\quad H^7y=0,\\
 H^{10}z=10!f^8g^5\ne0,\quad H^{11}z=0.
 \end{gathered}
\tag{7}
\]

No inverse power of f is required to define the actual flow:

\[
 \Theta_s(x)=\sum_{j=0}^{2}\frac{s^j}{j!}H^j x,\quad
 \Theta_s(y)=\sum_{j=0}^{6}\frac{s^j}{j!}H^j y,\quad
 \Theta_s(z)=\sum_{j=0}^{10}\frac{s^j}{j!}H^j z.
\tag{8}
\]

These are explicit finite polynomials from (2). They satisfy the whole
group identity \(\Theta_s\Theta_v=\Theta_{s+v}\), with inverse
\(\Theta_{-s}\), by the binomial identity for powers of H. This also
specifies the full maps below without omitting any lower coefficient.

The derivation kills no nonzero complex linear form in x,y,z. Indeed,
in the three complete coefficients (2), the monomials y^5, x^5, x^4y
respectively have coefficient vectors

\[
 (-2,0,0),\qquad (0,5,0),\qquad (0,0,10).
\tag{9}
\]

Thus H(alpha*x+beta*y+gamma*z)=0 implies alpha=beta=gamma=0.
For a nonzero linear form its image is homogeneous of degree five, so
it cannot be a nonzero complex constant either. This is all the
linear-invariant information used in the proof.

## 3. A whole sliced four-ring and both inverse maps

Extend R by an actual coordinate t, and define

\[
 B=R[t],\qquad E=H+(1+h)\partial_t,
 \qquad u=t-r.
\tag{10}
\]

Here H initially kills t. The two summands commute by Hh=0 and are
locally nilpotent, so E is locally nilpotent. Directly,

\[
 Eu=(1+h)-Hr=1.
\tag{11}
\]

In particular zeros of 1+h do not invalidate the construction. No
division by 1+h, h, f or g is used to obtain this slice.

The change from (x,y,z,t) to (x,y,z,u) is already a polynomial shear,
with t=u+r(x,y,z). In these latter actual coordinates E is
\(\widehat H+\partial_u\), where \(\widehat H\) acts by (2) on
x,y,z and kills u. This is the extension of H appropriate to R[u];
it must not be confused with the earlier extension that killed t.
Because \(\widehat H(u)=0\), the polynomial map
\(\exp(-u\widehat H)\) is an actual automorphism of R[u]. Put

\[
 (\xi_1,\xi_2,\xi_3)=\Theta_{-u}(x,y,z).
\tag{12}
\]

Formula (8) makes each right side an entire polynomial. Differentiating
it with E gives E(xi_i)=0, since differentiating the parameter -u
cancels H. Thus the forward map is

\[
 (x,y,z,t)\longmapsto
 \bigl(\Theta_{-(t-r(x,y,z))}(x,y,z),\ t-r(x,y,z)\bigr).
\tag{13}
\]

Its complete polynomial inverse is

\[
 \begin{aligned}
 (x,y,z)&=\Theta_u(\xi_1,\xi_2,\xi_3),\\
 t&=u+r\bigl(\Theta_u(\xi_1,\xi_2,\xi_3)\bigr)
    =r_\xi+(1+h_\xi)u.
 \end{aligned}
\tag{14}
\]

Subscripts xi mean evaluation at the displayed three independent
polynomial coordinates, not an extension of their field. For the first
inverse order, recover u=t-r, apply Theta_u to Theta_-u, and then
recover t=u+r. For the other order, (14) first gives t-r(x,y,z)=u;
applying Theta_-u to Theta_u recovers every xi_i. These are whole
polynomial identities, including the parameter substitutions.
They prove

\[
 B=\mathbb C[\xi_1,\xi_2,\xi_3,u],\qquad
 E=\partial_u,\qquad
 A=\ker E=\mathbb C[\xi_1,\xi_2,\xi_3].
\tag{15}
\]

In particular u and all xi_i are actual ambient coordinates. Their
failure to be homogeneous for the later Euler grading does not change
that fact. The polynomial invariant ring is proved for this control,
not inferred for an arbitrary sliced four-ring.

## 4. The actual positive frame and exact Euler shift

Use the following linear frame of the original actual ring R[t]:

\[
 Y_1=x+z,\qquad Y_2=y+z,\qquad Y_3=z,\qquad T=t.
\tag{16}
\]

Its full inverse is x=Y1-Y3, y=Y2-Y3, z=Y3, t=T; its Jacobian is one.
Since E restricts to H on R, (7) gives degree ten for each of the first
three rows. Also Et=1+h is nonzero and E^2t=0. Thus the exact tuple and
the entire actual Euler derivation are

\[
 (d_1,d_2,d_3,d_4)=(10,10,10,1),\qquad
 D=10\sum_{i=1}^3Y_i\partial_{Y_i}+T\partial_T
   =10(x\partial_x+y\partial_y+z\partial_z)+t\partial_t.
\tag{17}
\]

The equality on the right uses only the displayed invertible linear
change. These weights are the exact E-degrees, not freely assigned
ordinary weights.

For a direct all-ring shift calculation, write H_xi for the copy of H
in the coordinates xi and L_xi for their ordinary Euler derivation.
Transporting the complete field (17) through (13)--(14) gives

\[
 \begin{aligned}
 D(u)&=(1-29h_\xi)u-29r_\xi,\\
 D|_A&=M+uN,\\
 M&=10L_\xi+29r_\xi H_\xi,\qquad
 N=(29h_\xi-41)H_\xi.
 \end{aligned}
\tag{18}
\]

Here is a derivation of every term. Since r has ordinary degree three,
D(u)=t-30r(x)=u-29r(x). Formula (6) replaces r(x) by r_xi+u*h_xi,
giving the first row. For the other rows use
\([10L,H]=40H\) in the finite flow (8). Acting by 10L on
Theta_-u(x_i), with u held fixed for this part, gives
10xi_i-40u*H_xi(xi_i). The derivative of the parameter contributes
-D(u)*H_xi(xi_i). Substituting the first row yields precisely M+uN.
This computation can alternatively be checked against all four
complete eigen-equations from (14),(17).

Since h is nonconstant, N is nonzero. It is an LND on A: it is the
replica of H_xi by its invariant 29h_xi-41. Formula (18) bounds the
E-degree of D(P) by deg_E(P)+1 for every polynomial in A[u]. Equality
is attained on xi_1 because N(xi_1) is nonzero. Therefore the exact
whole-ring shift is

\[
 \delta=1,\qquad
 [E,D]=N+(1-29h_\xi)E,\qquad [E,[E,D]]=0.
\tag{19}
\]

This proves exact shift directly. Niceness of some rows or an assigned
leading profile is not used in place of the all-ring calculation.

## 5. Both homogeneous tests fail

First note the common finite-weight restriction. If a nonconstant
D-homogeneous polynomial P is an actual ambient coordinate, its
differential cannot vanish at the Euler origin: completing P to a
polynomial coordinate system gives a Jacobian determinant which is a
nonzero constant. Hence P has a nonzero linear term. If instead EP=1,
evaluation at that origin also forces a nonzero linear term, because
E is a polynomial vector field. In either situation, positivity of the
weights in (17) shows that the eigenweight of P belongs to {1,10}.

The full two source-weight spaces are

\[
 B_1=\mathbb C t,\qquad
 B_{10}=\operatorname{span}_{\mathbb C}\{x,y,z,t^{10}\}.
\tag{20}
\]

At weight one a nonzero P=alpha*t satisfies
EP=alpha*(1+h), which is neither zero nor one. At weight ten write

\[
 P=\alpha x+\beta y+\gamma z+\epsilon t^{10}.
 \quad
 EP=H(\alpha x+\beta y+\gamma z)
           +10\epsilon(1+h)t^9.
\tag{21}
\]

If EP is zero or one, its t^9 coefficient forces epsilon=0 in the
polynomial domain R[t]. Formula (9) then rules out EP=0 for a nonzero
linear form. Ordinary homogeneity of its H-image rules out EP=1.
The zero linear form does not supply a coordinate or a slice.

Thus there is neither a D-homogeneous E-slice nor a D-homogeneous
E-invariant ambient coordinate. No assumption is made that every
invariant is homogeneous, or that every homogeneous invariant has a
nonzero linear term. For example f and g are nonconstant homogeneous
E-invariants; their differentials vanish at the origin, so they are
not ambient coordinates there. The proof excludes the precise
coordinate and slice tests, not the existence of homogeneous
invariants altogether.

## 6. The failure persists in a commuting finite spectral action

In the original actual coordinates of (17), the three nonzero spectral
components of E are

\[
 E_{40}=H,\qquad E_{-1}=\partial_t,\qquad
 E_{69}=h\partial_t.
\tag{22}
\]

They have the indicated weights because H has ordinary degree four
as a derivation and h has ordinary degree seven. They are pairwise
commuting LNDs, using Hh=0. Their entire identities include

\[
 [D,E_{40}]=40E_{40},\quad
 [D,E_{-1}]=-E_{-1},\quad [D,E_{69}]=69E_{69},
 \qquad [E_\lambda,E_\mu]=0.
\tag{23}
\]

The three components are complex-linearly independent, and their
finite spectral projections belong to Lie_C(D,E). Their commuting
span consists of LNDs, whereas D is not an LND. Hence

\[
 \operatorname{Lie}_{\mathbb C}(D,E)
   =\mathbb C D\ltimes
     \bigl(\mathbb C H+\mathbb C\partial_t
                         +\mathbb C h\partial_t\bigr),
 \qquad \dim=4.
\tag{24}
\]

The corresponding additive flows are polynomial and normalized by the
actual Euler torus. The homogeneous coordinate t is a slice for the
component partial_t, but Et=1+h, not one. Thus neither commuting
spectral decomposition nor this finite-dimensional closure repairs the
two homogeneous tests for their sliced sum E.

The invariant coordinates in (15) and the slice u still recognize this
particular ring explicitly. The counterexample does not establish the
absence of nonhomogeneous invariant coordinates; it proves the opposite
for this known polynomial control. It does not rule out a general
shift-one recognition theorem by other means, or a reduction which
changes the frame before applying a homogeneous test.

## 7. Verification boundary

Fresh unsaved algebra reconstructs the entire Jacobian row (2), the
invariant and local-slice identities, the exact terminating iterates
and their nonzero top coefficients, and the finite-flow group identity
on all three generators. It also verifies all complete transported
Euler eigen-equations in (18), both commutators, the full three spectral
fields, their brackets, and the coefficient obstruction (9),(21).
The two polynomial inverse proofs use the complete finite flow (8),
not sampled points or a formal leading truncation.

No saved checker was executed, imported or compiled. No canonical or
prior source was edited. The known Freudenburg derivation is credited
above; the stronger rank-three theorem is unnecessary to the proof.
This source refutes only the stated homogeneous recognition
disjunction at exact first Euler shift and makes no general
cancellation, global-minimality, human-review or novelty claim.
