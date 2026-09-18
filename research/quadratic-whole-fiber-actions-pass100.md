# The actual derivations on the whole collapsed quadratic fiber

In the nonzero-normal collapsed cases, the canonical N kills the
whole transverse fiber coordinate G and translates c by a polynomial
in G alone. The original bad partial also preserves the whole
fiber, but need not preserve its intrinsic invariant subring.
Its exact failure to commute with E is determined by the nilpotent
part of the slice difference h.

The actual cubic identity makes that nilpotent coefficient constant
when the first normal action is nonzero, so E and the original
partial commute on the entire fiber in that case. With zero first
normal action, only a degree-two bound follows here. All identities
in this note are explicitly restricted to the whole fiber unless
stated otherwise; they are not lifts to the original rings.

## 1. The exact fiber rings and the nilpotent slice correction

Retain the hypotheses of
[whole-plane-fiber99](quadratic-whole-plane-fiber-pass99.md): a whole
collapsed fixed double or a mixed (2,1) fiber, with
\(L(\mathfrak m)\ne0\). Its actual ideals and presentations are
\[
\begin{gathered}
I=\mathfrak mB=(\ell,H(Y)),\qquad
\mathfrak mA=(F,H(G)),\\
H(t)=t^2\quad\text{or}\quad H(t)=t^2(t-1),\qquad
D_0=\mathbb C[G]/(H(G)),\\
\mathcal A=A/\mathfrak mA=D_0[c],\qquad
\mathcal B=B/I=D_0[c,u]=D_0[\sigma,z],\\
E=\partial_u,\qquad \sigma=u-h,\qquad
z=c+q\sigma h+\frac q2\sigma^2,
\qquad h\in\mathcal A,\quad q\in\mathbb C^*.
\end{gathered}
\tag{1}
\]
The same actual Y and G have equal residues. The symbol c is
the original invariant generator from the completed S-matrix,
not a newly chosen parameter. Also
\(\sigma=W+\alpha Y+\beta_0\) in \(\mathcal B\), for complex
constants \(\alpha,\beta_0\). The original partial
\(T=\partial_z\) preserves I and kills Y,W and sigma in this
quotient. The original N preserves I, kills u, and commutes with E.

For a whole double put \(\epsilon=G\), \(e_2=1\), and \(e_1=0\).
For the mixed case put
\(e_1=G^2\), \(e_2=1-G^2\), and
\(\epsilon=G-G^2\). These are the simple and double idempotents
and the double nilpotent coordinate: \(\epsilon^2=0\) and
\(e_1\epsilon=0\). The collapsed-plane argument makes h constant
on each reduced component. Therefore its exact whole-fiber form is
\[
\begin{gathered}
h=\eta+\epsilon\beta(c),\qquad \beta\in\mathbb C[c],\\
\eta=\eta_2\quad\text{or}\quad
\eta=\eta_2e_2+\eta_1e_1,\qquad \eta_i\in\mathbb C,\\
h_c=\epsilon\beta'(c),\qquad h_c^2=0.
\end{gathered}
\tag{2}
\]
The nilpotent term has not been discarded. The polynomial beta
is uniquely determined with this chosen constant part eta.

## 2. The whole canonical Jacobian coefficient is constant on each factor

Let \(t_j=s_j-s_j(\mathfrak m)\) be the polynomial parameters
generating the closed base ideal \(\mathfrak m\). Express them
in B using the exact
ideal in (1):
\((t_1,t_2)^t=M(\ell,H(Y))^t\).
Both pairs are regular sequences generating I. Thus their
classes are two bases of the free rank-two \(\mathcal B\)-module
\(I/I^2\), and \(\det M\) is a unit modulo I.

Differentiate the displayed expression and reduce modulo I.
Terms involving derivatives of M are multiplied by ell or H
and vanish. The defining original Jacobian of N then gives
\[
\begin{gathered}
Nf=V H'(Y)\bigl(u_W f_z-u_z f_W\bigr)
\quad\text{in }\mathcal B,\qquad V\in\mathcal B^*,\\
NG=0,\qquad
Nc=U H'(G),\qquad U\in\mathcal B^*.
\end{gathered}
\tag{3}
\]
The unit V includes the nonzero constant determinant of the
actual affine change of original good coordinates. No
redefinition of the canonical field or division by a vanishing
fiber parameter is being made.

For the last unit assertion, the additional factor is
\(u_Wc_z-u_zc_W\). Since sigma differs from W by an affine
function of Y, this is the relative Jacobian of (u,c) in
(sigma,z). These are two actual polynomial presentations over
the same ring D_0 in (1), with polynomial inverse transition
maps. The chain rule makes their relative Jacobian a unit,
even though D_0 is nonreduced. The derivatives in W,z are
legitimate quotient derivations since I is independent of
both variables.

The units of \(\mathcal B\) reduce to nonzero complex constants
on each reduced affine-plane factor. Any difference from those
constant components is in \(\epsilon\mathcal B\). But
\(H'(G)\epsilon=0\). Consequently all nilpotent, possibly
c-dependent or u-dependent, parts of U disappear from (3).
There are constants \(\lambda\in\mathbb C^*\) and, in the
mixed case, \(\rho\in\mathbb C^*\), such that
\[
\begin{gathered}
N=n(G)\partial_c\text{ on }\mathcal B=D_0[c,u],\qquad
n(G)=\lambda G\quad\text{or}\quad
n(G)=\lambda(G-G^2)+\rho G^2,\\
\boxed{\quad NG=0,\qquad N^2c=0,\qquad Nh=0
\quad\text{on the whole fiber}.\quad}\\
NG\in\mathfrak mA,\qquad N^2c\in\mathfrak mA,\qquad
Nh\in\mathfrak mA\quad\text{in the original }A.
\end{gathered}
\tag{4}
\]
In the last line the symbols denote the original invariant
elements before quotienting. The zero of Nh in the second line
uses \(n(G)h_c=0\), not constancy of beta. This argument is
stronger than merely writing Nc as a unit times H' and allowing
that unit arbitrary c-dependence.

## 3. The original bad partial on the whole fiber

Work in the presentation \(D_0[c,u]\), where E is the derivative
in u. Since T kills G and sigma, differentiation of (1) gives
\(Tu=h_cTc\), followed by
\(1=Tz=(1+q\sigma h_c)Tc\). The second factor is a unit by (2).
Its exact inverse is \(1-q\sigma h_c\), so
\[
\boxed{\quad
TG=0,\qquad Tc=1-q\sigma h_c,\qquad Tu=h_c,\qquad
T=h_c\partial_u+(1-q\sigma h_c)\partial_c
\quad\text{on }\mathcal B.
\quad}
\tag{5}
\]
In obtaining Tu, the term \(q\sigma h_c^2\) is zero. Starting
with Tu equal to h_c without this step would overlook the
dependence of c on the original z-direction.

Using (2), (4), and \(\sigma=u-h\), direct commutators give
\[
\begin{gathered}
\boxed{\quad [E,T]=-q h_c\partial_c,\qquad [N,T]=0
\quad\text{on }\mathcal B.\quad}\\
[E,T]=0\ \Longleftrightarrow\ h_c=0
\ \Longleftrightarrow\ T(\mathcal A)\subset\mathcal A,\\
h_c=0\quad\Longrightarrow\quad Tu=0,\quad Tc=1.
\end{gathered}
\tag{6}
\]
For \([N,T]\), note that \(Nh_c=n(G)h_{cc}=0\), \(N\sigma=0\),
and \(Tn(G)=0\). For the subring equivalence, the coefficient of
u in \(Tc=1-q(u-h)h_c\) is \(-qh_c\). In the actual polynomial
extension \(\mathcal A[u]\), it vanishes exactly when h_c does.
This coefficient test is valid with nilpotents. Also the square
of the induced commutator in (6) is zero, because both h_c and
h_cc belong to the same square-zero ideal.

None of (4)--(6) asserts that T preserves A or commutes with E
or N in B itself. In particular a quotient commutator can
vanish while the original commutator is nonzero.

## 4. The actual cubic identity bounds the nilpotent coefficient

There is a global identity \(N^3h=0\) before taking the fiber.
Indeed the original volume equation expresses Omega times h
as an S-linear combination of A_1,A_2 and an element of S.
N kills S and \(N^3A_i=0\). The nonzero Omega cancels in the
domain A, proving the identity.

Use the constant-left-inverse coordinates of
[volume-normal splitting99](quadratic-volume-normal-splitting-pass99.md)
at the double component. Its quotient column is
\((1,a_0+a_1c)^t\), and its transverse quadratic coefficient
is \(b\in\mathbb C^*\). With normal parameters x,y=G of
weights two,one, the actual leading derivation is
\(D_* =\gamma x\partial_y+\lambda y\partial_c\), where
\(\gamma=-\nu a_1\), \(\lambda=2\nu b\), and
\(\nu\in\mathbb C^*\). This also identifies the double
constant lambda in (4) with that retained normalization.

The free conormal basis gives
\(h-\eta_2\equiv\alpha(c)F+\beta(c)G\pmod{\mathfrak q_2^2}\).
It is the same beta as (2), since F and G squared vanish on the
whole double factor. Also \(F\equiv x\pmod{\mathfrak q_2^2}\)
has weight at least two. Thus the weight-one part of h minus
its constant residue is exactly \(\beta(c)y\). Terms in x or
in the square of the normal ideal have weight at least two.
The weight-four part of the
actual identity \(N^3h=0\) is
\[
\begin{gathered}
D_*^3(\beta(c)y)=
3\gamma^2\lambda\beta'(c)x^2
+6\gamma\lambda^2\beta''(c)xy^2
+\lambda^3\beta'''(c)y^4=0,\\
\boxed{\quad
a_1\ne0\ \Longrightarrow\ \beta\in\mathbb C,
\qquad
a_1=0\ \Longrightarrow\ \deg\beta\le2.
\quad}
\end{gathered}
\tag{7}
\]
The displayed coefficients follow by three ordinary applications
of D_*. Its coefficients are constant except for beta and its
derivatives. The strict weighted filtration means higher terms
in the original derivation or h cannot cancel these coefficients.

The retained conormal formula identifies \(a_1\ne0\) with
nonzero first normal action. In that case beta is constant,
so h belongs to D_0, including on the mixed simple factor.
Equation (6) proves commutation of E and T on the entire
nonreduced fiber and preservation of its intrinsic subring.
When the first normal action is zero, (7) does not force that
commutation: a linear or quadratic nilpotent coefficient remains
allowed by this calculation.

## 5. An exact fiber-algebra boundary to a global lift

Over the explicitly nonreduced ring
\(D=\mathbb C[\epsilon]/(\epsilon^2)\), choose
\(q,\lambda\in\mathbb C^*\) and set
\[
\begin{gathered}
E=\partial_u,\qquad N=\lambda\epsilon\partial_c,
\qquad h=\epsilon c^2,\qquad
\sigma=u-\epsilon c^2,\qquad z=c+\frac q2u^2,\\
z_0=z-\frac q2\sigma^2,\qquad
c=z_0-q\sigma\epsilon z_0^2,\qquad
u=\sigma+\epsilon z_0^2,\\
T=\partial_z\text{ in }D[\sigma,z],\qquad
Tu=2\epsilon c,\quad Tc=1-2q\sigma\epsilon c,\\
[E,T]=-2q\epsilon c\partial_c\ne0,\qquad
[N,T]=0,\qquad N^2c=Nh=0.
\end{gathered}
\tag{8}
\]
The middle line is an actual polynomial inverse over D. To
check it, the forward equations give
\(z_0=c+q\sigma\epsilon c^2\), hence
\(\epsilon z_0^2=\epsilon c^2\); substitution proves both
orders. All derivative identities are then direct. In
particular beta has the allowed degree two, yet the induced
commutator is nonzero.

This is only a polynomial fiber-algebra control. It does not
construct a smooth threefold, a base quotient with the required
canonical Jacobian, an original four-coordinate inverse frame,
or a first-normal-zero lift. Its purpose is precise: polynomial
invertibility over the whole fiber and the displayed induced
identities do not themselves eliminate the remaining nilpotent
coefficient. Higher normal orders or a global constraint would
be required for that further step.

## Scope and provenance

Root proposed the induced-N and commutator question. Geometry
proved the exact whole-fiber coefficient using the conormal
transition determinant and its units, and derived the original
T formulas and the polynomial fiber control. Jet independently
derived the weighted beta coefficient and its sharp remaining
degree bound; Geometry reconstructed the same cubic calculation.
The proof uses the retained whole-fiber and normalized-volume
statements99, not a new primary-source theorem.

The formulas concern actual induced actions in the stated
fiber, while (8) is separately labeled algebra-only. Neither
kind of calculation proves global commutation, freeness,
recognition of A, or unrestricted cancellation. All files
through99 are unchanged.
