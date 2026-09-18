# The actual coordinate forces a smooth critical-value function

The normalized quadratic expression for the original coordinate z
imposes differential conditions beyond coprimality of its invariant
coefficients. On the full open set where the reduced return denominator
h is invertible, its critical-value function has no critical points.
Inverting the additional common factor g is unnecessary. The retained
two-speed action also shows that this smooth function need not be a
slice for any locally nilpotent derivation on that open base.

## 1. Keep the original coordinate differential

Use the actual sliced setting and normalization of the
[centered-return proof](rank-one-centered-return-quotient-pass85.md):
\[
B=A[s]=\mathbb C^{[4]},\qquad A=\ker E,\qquad
F=z=w+gvs+\frac{gh}{2}s^2,
\qquad g,h,v,w\in A,\quad gh\ne0.
\tag{1}
\]
The differential argument has a broader scope than that predecessor's
speed-frame conclusions. It requires only a sliced actual E and one
original coordinate z of E-degree two: E cubed z=0 and E squared z
nonzero. There is no bound on the E-degrees of the other three original
coordinates. Indeed q=E squared z is invariant, so its factors g and
h are invariant by E-degree additivity; the same definitions of v
and w then give (1). No good-speed-zero or speed-ideal conclusion is
transferred to this broader class. Root identified this scope
strengthening after the initial differential reconstruction.

Here z is an original polynomial coordinate, not merely a polynomial
with the indicated degree in s. The actual base Spec A is smooth.
For example, A=B/(s), and E(s)=1 makes the hypersurface differential
ds unimodular in the smooth polynomial four-ring. The original
coordinate partial T_z satisfies T_z(F)=1.

Restrict T_z to A and expand its values as polynomials in s. This
gives finitely many complex derivations D_j of A, with
D_s=sum s^j D_j. Finiteness follows by choosing finite algebra
generators of A; extracting coefficients of the Leibniz identity
shows that every D_j is a derivation. Write lambda(s)=T_z(s).
The identity T_z(F)=1 becomes
\[
1=\bigl(dw+s\,d(gv)+\tfrac12s^2d(gh)\bigr)(D_s)
  +g(v+hs)\lambda(s).
\tag{2}
\]
Equivalently, dF is unimodular in the decomposition
Omega_B=Omega_A[s] direct sum B ds. No assertion that any D_j is
locally nilpotent is needed or follows from this coefficient expansion.

For a one-form eta on A, let j(eta) denote the ideal of its values
on all complex derivations of A. Evaluating (2) at s=0 proves the
global ideal identity
\[
j(dw)+(gv)=A.
\tag{3}
\]
Thus w has no critical point at a base point where gv vanishes.
This does not say that w is globally a coordinate or that j(dw)=A.

## 2. Eliminate the critical parameter on D(h)

In A_h evaluate s at -v/h and put
\[
r=w-\frac{gv^2}{2h},\qquad
D_* =\sum_j(-v/h)^jD_j,
\qquad D_*(r)=1,\qquad j(dr)=A_h.
\tag{4}
\]
Every D_j extends uniquely to A_h by the quotient rule, so D_* is
an actual derivation of this localized ring. To verify (4), the
coefficient g(v+hs) in (2) is zero on this section. The pullback of
the first one-form in (2) is exactly dr: the extra derivative of
the section is multiplied by that same zero coefficient. This also
follows by directly differentiating w-gv squared/(2h).

There is no division by g in this argument. In particular, (4)
holds at points where g=0 and h is nonzero. For any complex value t,
define the discriminant polynomial
\[
\Delta_t=2h(w-t)-gv^2=2h(r-t).
\qquad
d\Delta_t\equiv2h\,dr\pmod{\Delta_t}
\quad\text{in }\Omega_{A_h}\otimes A_h/(\Delta_t).
\tag{5}
\]
The latter differential is unimodular on that quotient, by (4).
Consequently each hypersurface Delta_t=0 inside the smooth base
D(h) is smooth, or empty. This is the hypersurface differential
criterion, not a statement that a quadratic cover is finite globally.
The name discriminant comes from the discriminant -g Delta_t of
F-t as a quadratic polynomial in s; no inversion of g is used in (5).

## 3. A pointwise constraint on the common-factor divisor

At a closed base point with g=0, let bars denote the scalar values
and covectors in its cotangent space. Equation (2), at every complex
value of s, forces
\[
\begin{array}{ll}
(\bar h,\bar v)\ne(0,0):&
  dw\notin\mathbb C\,dg,\\
\bar h=\bar v=0:&dw\ne0.
\end{array}
\tag{6}
\]
Indeed the vertical derivative of F is zero there, while its
horizontal differential is dw+(s bar(v)+s squared bar(h)/2)dg.
In the first case the scalar polynomial in s is nonconstant and
attains every complex value. If dg is nonzero and dw is a multiple
of it, some value of s makes the entire differential zero. If dg=0,
the excluded multiple is dw=0 and the contradiction already holds
at s=0. In the second case the horizontal differential is dw for
every s. This is a pointwise covector statement; it does not assert
smoothness of the divisor g=0 when g has repeated factors.

## 4. Actual controls, including a failure of LND-slice promotion

First use the [actual cancellation frame](return-denominator-cancellation-control-pass85.md)
with original coordinates (a,x,c,z), E=a squared partial_x+
(a-1)(1+ax)partial_z, and invariant coordinate u. Put
H=-u-au-au squared/2. Its polynomial inverse is x=H+a squared s,
and z=((a-1)(x+ax squared/2)-u)/a squared. Thus
\[
\begin{gathered}
A=\mathbb C[a,u,c],\quad g=a-1,\quad h=a^3,
\quad v=1+aH,\quad
w=\frac{(a-1)(H+aH^2/2)-u}{a^2},\\
r=-\frac{u}{a^2}-\frac{a-1}{2a^3},\qquad
(-a^2\partial_u)(r)=1.
\end{gathered}
\tag{7}
\]
The expression for w is polynomial by the same truncated-inverse
congruence as in that frame. Formula (7) includes the divisor a=1,
which lies in D(h) but outside D(q). On this divisor w=-u and
dg=da; the du coefficient of dw is -1, verifying (6) there.

One additional subcase has g=(a-1) squared and
H=u+a(2u-u squared/2). Use the same formulas for the polynomial
inverse, v, w and h=a cubed with these replacements. The two
congruences modulo a squared again verify both inverse orders:
the map x to g(x+ax squared/2) is inverted modulo a squared by H.
It therefore remains an actual globally sliced action with proper
good-speed ideal (a squared). Its critical value is
r=-u/a squared-g/(2a cubed). At a=1, Delta_t=-2(u+t), whereas
the raw discriminant -g Delta_t has the repeated factor (a-1) squared.
Thus (5) cannot be upgraded to squarefreeness of the raw discriminant,
even on D(h). Here dg=0 at a=1, while the du coefficient of dw is -1, also
exercising the zero-dg case in (6). This is the additional actual
variant proposed by Geometry and approved by Root, not a new method.

For the retained two-speed frame with invariant base C[a,b,c], the
normalized expressions and an explicit splitting derivation are
\[
\begin{gathered}
g=1,\quad h=2ab,\quad v=1+ac+b^2,\quad w=bc,\quad
r=bc-\frac{(1+ac+b^2)^2}{4ab},\\
D_*=-a\partial_b-\left(b+\frac{v}{2b}\right)\partial_c,
\qquad D_*(r)=1,
\qquad [c^2]r=-\frac{a}{4b}.
\end{gathered}
\tag{8}
\]
The two-speed frame and both polynomial inverse orders are explicit
in the same control note. In this example A_h=C[a,a inverse,b,b inverse,c].
Although D_* splits dr, it is not locally nilpotent: it moves the
unit b, with D_*(b)=-a nonzero. An LND on a characteristic-zero
domain kills every unit, by additivity of LND-degree applied to a
unit and its inverse.

More strongly, no LND on this A_h can send r to 1. Any such LND
would kill a and b, and would extend to a locally nilpotent
K-derivation of K[c], where K=C(a,b). A derivation f(c)partial_c
of a one-variable polynomial ring is locally nilpotent only if
f is constant in c: otherwise its repeated action on c has nonzero
leading coefficients, including the linear case. Thus its value on
the genuinely quadratic r in (8) cannot be 1. In particular r is
not a polynomial coordinate over C[a,a inverse,b,b inverse].
This is a failure of an LND-slice or coordinate inference for the
localized critical-value function, not a failure of the original
global slice or of recognition for the retained action.

The [two-method checker](coordinate_critical_value_checks_pass86.py)
checks these actual coordinate inverses and finite differential
identities independently of earlier checker code. It does not prove
the general differential descent, all-fiber smoothness, or the
classification of one-variable LNDs by enumerating examples.

The initial two-method author run passed in 0.235 seconds, chunk
83bb1f. During the complete author reread, an unnumbered scalar
factor in the discriminant explanation was corrected from -2g to
-g; formulas (1)--(8) were unchanged. An explicit discriminant
calculation was then added within the first existing method. The
two-method run after this correction passed in 0.251 seconds, chunk
e44009, without any failed assertion. That version's checker SHA-256 was
89341fd4d7b43251240f4e00256400ddb317842a53746a396c2fd13f6a87e84c.
After the repeated-g control was added as a subtest of the first
existing method, the final two-method run passed in 0.565 seconds,
chunk 5e2ea8, with no failed assertion. The current checker SHA-256 is
6bbc22f085e971adfd626c7597d283b30c90a705c6f63f0c203322504c003fdc.
The two common-factor subtests still count as one unittest method;
the total remains two methods, now covering three actual actions.
The final proof and checker received a complete author EOF reread.

Root proposed the actual-coordinate differential investigation. Jet
derived the D(h) section argument and these controls; Geometry had
independently obtained the D(q) version before coordination. No new
primary-paper read or arbitrary-action computational certificate is
claimed. Canonical run capture and integration are separate Root work.
No files through pass85 are edited. The unrestricted recognition and
membership questions are unchanged; no novelty claim is made.
