# A parabolic coefficient form for the terminal moving quartic

The terminal quartic symmetry admits an actual coordinate shear
that preserves both original good partials. Its two rational
coefficients satisfy a parabolic relation over their common
invariant field. The original velocity identities show that
one power of the polynomial factor \(g\) clears the entire
symmetry to a global commuting nice locally nilpotent derivation.

This is a structural reduction, not recognition of the terminal
kernel. In particular the new bad-coordinate profile is not the
old two-quadratic profile, and the symmetry still has three
constant output directions.

## 1. Exact terminal input

Retain the original sliced polynomial action and terminal case of
[the quartic reduction](common-power-moving-quartic-reduction-pass70.md):
\[
B=k[x_1,x_2,X,Y],\quad k=\mathbb C,\quad
E\in\operatorname{LND}(B),\quad Es_*=1,\quad
g\in\ker E\setminus k,\quad \delta=E/g.
\]
The two original good partials have second adjoint zero; the
two original bad partials have third adjoint zero.
The highest layers have been normalized with \(c=e_1\) and
bad top direction \((1,0)\). All functions below initially
belong to \(B_g\), unless a stronger membership is stated.

The completed first and second images give
\[
\delta^3x=c\sigma+e,\qquad
\delta^2x=c\tau+e\sigma+v_0,\qquad
u_0=\tau-\frac{\sigma^2}{2},
\]
\[
\delta\sigma=1,\quad \delta\tau=\sigma,\quad
\delta u_0=0,\quad
e_B=(1,0),\quad (v_0)_B=\mu=(\mu_1,\mu_2),\quad
\mu_2\ne0.
\tag{1}
\]
The constant second residual is written
\(\nu=\nu_1e_B+\nu_2\mu\). Its full bad velocity is
\[
(\delta X,\delta Y)
=e_B\left(\frac{3\tau}{2}-\frac{\sigma^2}{4}\right)
   +\mu\sigma+\nu_1e_B+\nu_2\mu.
\tag{2}
\]
The vectors \(c,e,v_0\) and constants \(\mu_i,\nu_i\) are
complex constants. The derivation from the preceding note is
\[
S=T_{v_0}+\frac{\sigma-\nu_2}{2}T_e+
\left(\frac{\sigma^2}{6}-\frac{\nu_2\sigma}{6}
      +\frac{u_0}{2}-\frac{\nu_1}{3}\right)T_c.
\tag{3}
\]
Its fully proved identities are
\[
[\delta,S]=[E,S]=0,\quad Sg=0,\quad
S\sigma=0,\quad Su_0=\frac13,\quad
S^2x=\frac c6,\quad S^3x=0,\quad
S\in\operatorname{LND}(B_g).
\tag{4}
\]
The original slice was used to prove \(Sg=0\) before localized
local nilpotence was asserted. No global polynomiality of \(S\)
is assumed here.

## 2. Two genuine good partials survive the coordinate choices

Choose a second constant good direction \(c_2\) independent of
\(c\). Since \(e_B,\mu\) are independent, the ordered vectors
\((c,e,v_0,c_2)\) form a basis of \(k^4\).
Use the dual constant coordinates \((a_0,b,z,w)\).
The bad coordinates are explicitly
\[
z=\frac{Y}{\mu_2},\qquad b=X-\frac{\mu_1}{\mu_2}Y.
\tag{5}
\]
They kill both original good directions, while evaluating as
the duals of \(v_0\) and \(e\), respectively. Thus
\[
T_c=\partial_{a_0},\quad T_e=\partial_b,\quad
T_{v_0}=\partial_z,\quad T_{c_2}=\partial_w.
\]
This is an actual constant polynomial coordinate change.
In particular both \(\partial_{a_0}\) and \(\partial_w\)
retain the original second-adjoint bounds.

Equations (1)--(2) give
\[
\delta z=\sigma+\nu_2,\qquad
\delta b=\frac{\sigma^2}{2}+\frac{3u_0}{2}+\nu_1,\qquad
\delta^2a_0=\tau,\qquad \delta^2w=0.
\tag{6}
\]
Also \(Sz=1\), \(Sb=(\sigma-\nu_2)/2\), and \(Sw=0\).

Make the actual polynomial shear
\[
a=a_0-\frac{z^2}{12}+\frac{\nu_2}{3}b,
\tag{7}
\]
fixing \(b,z,w\). Its inverse changes the correction signs.
Since the corrections depend only on the two bad coordinates,
the actual partials \(\partial_a=T_c\) and
\(\partial_w=T_{c_2}\) are unchanged.

## 3. A common invariant gives the parabolic coefficient relation

Put
\[
\beta=\frac{\sigma-\nu_2}{2},\qquad
\kappa=\frac{\sigma^2}{6}+\frac{u_0}{2}
       -\frac{\nu_1}{3}-\frac{z}{6}-\frac{\nu_2^2}{6}.
\]
Evaluating (3) on the coordinates after (7) gives
\[
S=\partial_z+\beta\partial_b+\kappa\partial_a,\qquad
S\beta=S\kappa=0,\qquad
\delta\beta=\frac12,\quad \delta\kappa=\frac{\beta}{3}.
\tag{8}
\]
For the last equality, use
\(\delta\kappa=\sigma/3-(\sigma+\nu_2)/6\).
Define
\[
h=3\kappa-\beta^2
=\frac{\sigma^2}{4}+\frac{\nu_2\sigma}{2}
 +\frac{3u_0}{2}-\nu_1-\frac z2-\frac{3\nu_2^2}{4}.
\]
Then
\[
\delta h=Sh=0,\qquad
\boxed{S=\partial_z+\beta\partial_b+
          \frac{\beta^2+h}{3}\partial_a.}
\tag{9}
\]
This is a rational nice field, since all three coefficients
are fixed by \(S\). It has three constant output directions.
Equation (9) is a relation over a common invariant field;
it is not a constant linear relation between the outputs.

## 4. Exact original velocities and further common invariants

Write \(c_0=2\nu_1+\nu_2^2/2\). Equation (6) becomes
\[
\delta z=2\beta+2\nu_2,\qquad
\delta b=\beta^2+h+\frac z2+c_0.
\tag{10}
\]
Let \(K=\delta w\). Since \(\delta^2w=0\), \(Sw=0\),
and \([\delta,S]=0\), one has
\(\delta K=SK=0\).
The polynomial \(p=Ew=gK\) therefore belongs to \(B\)
and is killed by both \(E,S\).

There is also an exact rational invariant
\[
i=\delta a-\frac b3-\frac{2\beta^3}{9}
                  -\frac{2h\beta}{3},\qquad
\delta i=Si=0.
\tag{11}
\]
To verify the first derivative, differentiate (7) twice and
use (6):
\[
\delta^2a-\frac{\delta b}{3}
=\frac{\sigma^2}{6}+\frac{u_0}{2}
 -\frac{\nu_1}{3}-\frac z6-\frac{\nu_2^2}{6}
=\kappa.
\]
The \(\delta\)-derivative of
\(2\beta^3/9+2h\beta/3\) is
\((\beta^2+h)/3=\kappa\).
For the second derivative,
\(S(\delta a)=\delta(Sa)=\delta\kappa=\beta/3\),
which cancels \(Sb/3\); all the remaining terms are \(S\)-invariant.
Thus the full normalized velocity has the form
\[
\delta(a,b,z,w)=
\left(\frac b3+\frac{2\beta^3}{9}+\frac{2h\beta}{3}+i,\,
      \beta^2+h+\frac z2+c_0,\,
      2\beta+2\nu_2,\,
      K\right).
\tag{12}
\]
The original polynomial velocity is \(g\) times this vector.
Polynomiality of that product is inherited from the actual
original action, not inferred from the rational display alone.

In fact the bad velocity gives an actual numerator
\[
N=g\beta=\frac{Ez-2\nu_2g}{2}\in B,\qquad
EN=\frac{g^2}{2},\qquad SN=0.
\tag{13}
\]
Two further cleared coefficients are actual polynomials:
\[
H=g^2h=g\,Eb-N^2-g^2\left(\frac z2+c_0\right)\in B,
\]
\[
I=g^3i=g^2Ea-\frac{g^3b}{3}
              -\frac{2N^3}{9}-\frac{2HN}{3}\in B.
\tag{14}
\]
Consequently \(g,H,I,p\) are all actual common invariants of
the original \(E\) and the localized \(S\).
The two fields are fraction-field independent: \(S\beta=0\)
but \(E\beta=g/2\ne0\), and \(Sz=1\).
Their annihilator in the four-dimensional differential space
has dimension two, so
\[
\operatorname{trdeg}_k k[g,H,I,p]\le2.
\tag{15}
\]
The same bound holds for \(k(g,h,i,K)\). This is not a proof
that \(h\in k(g)\), that the common invariant ring is a polynomial
plane, or that any of these invariants is an ambient coordinate.

## 5. One power gives a global commuting nice derivation

Put \(C_z=z/2+c_0\) and define the actual polynomials
\[
U=Eb-gC_z,\qquad V=Ea-\frac{gb}{3}.
\]
Equations (10)--(14) give
\[
U=g(\beta^2+h),\qquad
\kappa=\frac{U}{3g},\qquad
T:=gS=g\partial_z+N\partial_b+\frac U3\partial_a
\in\operatorname{Der}_k(B).
\tag{16}
\]
In particular one power of \(g\), not an unspecified larger
power, clears every coefficient.

The original velocity identities imply
\[
Eg=0,\qquad EN=\frac{g^2}{2},\qquad
EU=gN,\qquad EV=\frac{gU}{3}.
\tag{17}
\]
Indeed \(E^2b=2gN+\nu_2g^2\), while
\(E C_z=N+\nu_2g\), proving the \(U\)-identity.
For \(V\), multiply
\(\delta^2a-\delta b/3=\kappa\) by \(g^2\).
Also
\(SU=E(Sb)-gS C_z=E\beta-g/2=0\), and
\(SV=E(Sa)-gSb/3=E\kappa-g\beta/3=0\).
Consequently
\[
Tg=TN=TU=TV=0,\qquad Tw=0,\qquad
[E,T]=0,\qquad T^2(a,b,z,w)=0.
\tag{18}
\]
The polynomial derivation \(T\) is therefore a global nice
LND: its polynomial coefficients are fixed by \(T\), so its
flow on the actual coordinates is the translation by those
coefficients. It is nonzero because \(Tz=g\ne0\).
The distinction from a global slice remains essential:
\(Tz=g\), not \(1\). Inverting \(g\) recovers the previously
known coordinate slice for \(S\), but no inversion has been
removed from that slice assertion.

The cleared invariants now have the sharper expressions
\[
H=-N^2+gU,\qquad
I=\frac{4N^3}{9}-\frac{2gUN}{3}+g^2V.
\tag{19}
\]
Thus \(H\equiv-N^2\) and \(I\equiv4N^3/9\) modulo \(gB\).
The resulting cusp congruence in fact lifts to
\[
\begin{aligned}
81I^2+16H^3
={}&g^2\bigl[-12U^2N^2+72VN^3\\
 &\qquad+g(16U^3-108UNV)+81g^2V^2\bigr].
\end{aligned}
\tag{20}
\]
Hence \(J=(81I^2+16H^3)/g^2\) is an actual polynomial
common invariant of \(E,T\), and of \(S\) on \(B_g\).
This follows either from the displayed expansion and
(17)--(18), or by differentiating the quotient in the
fraction field, since \(g,H,I\) are common invariants.
The congruences do not imply \(g\mid N\). They do not
produce a polynomial coefficient \(\beta=N/g\) or a
global slice for \(T\).

## 6. The new profile and the recognition boundary

The two good partials remain actual original-good ones.
The other two partials after (7) are
\[
T_b'=T_e-\frac{\nu_2}{3}T_c,\qquad
T_z'=T_{v_0}+\frac z6T_c.
\]
The full original top identity is
\(g[E,T_c]=-3V_X/2\), and \(E^2z=g^2\).
The commutator product rule therefore gives
\[
\operatorname{ad}_E^2T_b'=V_X\ne0,\qquad
\operatorname{ad}_E^3T_z'
=\frac{g^2}{2}[E,T_c]
=-\frac34gV_X\ne0,\qquad
\operatorname{ad}_E^4T_z'=0.
\tag{21}
\]
Thus this particular parabolic coordinate presentation is bounded
by \((1,1,2,3)\), not by the old \((1,1,2,2)\).
It cannot be sent back to the cubic or mixed theorem merely
because the symmetry became nice.

The already known original-coordinate endpoints still apply if
\(p\) is constant: if \(p=0\), \(w\) is an invariant ambient
coordinate; if \(p\ne0\), \(w/p\) is an actual coordinate slice.
No such constancy follows from (15). This note does not use
omission of \(g\) by a good direction as a stand-alone
recognition criterion; any such application would have to
verify the additional hypotheses of the specific inherited
recognition theorem.

The two-direction rational theorem cannot be applied merely
to (9), because it has two varying output coefficients rather
than one. The known localized coordinate-section identity
also remains only a localization of a polynomial three-ring.
The parabolic relation, explicit global nice replica, and
cleared invariant identities are exact additional constraints
for a further proof; they do not complete its global descent.

## Verification scope

The calculations above use the fully proved terminal quartic
identities and actual polynomial coordinate changes. A separate
exact symbolic expansion checked (20); it was not a new test
suite or regression. These calculations add
no polynomial-root assumption, classification search, numerical
suite, regression total, metadata change, historical-novelty
claim, human review, or formal verification.
The pass70 packet and earlier files are unchanged.
