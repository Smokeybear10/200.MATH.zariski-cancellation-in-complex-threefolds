# A moving-x residue and divergence-free Vénéreau controls

Date: 2026-09-17. Private bounded working proof; novelty UNKNOWN.
General complex-threefold cancellation remains UNSOLVED.

## 1. Statement and scope

Fix the actual polynomial ring and derivation
\[
 B=\mathbb C[x,y,z,u],\qquad A=\mathbb C[x,y,z],\qquad E=\partial_u,
\]
and the third Vénéreau coordinate
\[
 v=y+x^3\bigl(xz+y(yu+z^2)\bigr)
   =x^3y^2u+y+x^4z+x^3yz^2.                              \tag{1}
\]
Its whole coordinate status is recorded with an explicit completion
and inverse in
[615](venereau-coordinate-positive-shift-obstruction-pass615-working.md).
Use the exact polynomial-degree shift
\[
 \delta(D)=\max\{\deg_u Dx,\deg_u Dy,\deg_u Dz,\deg_u Du-1\},
 \qquad \deg_u0=-\infty.                                  \tag{2}
\]

For every locally nilpotent derivation \(D\) satisfying \(Dv=1\) and
\(\delta(D)=2\), its necessary normal form in Section 2 satisfies
\[
 a+p_{30}-\frac{p_{121}}2+\frac{p_{62}}3=\frac2{11},        \tag{3}
\]
where the labels mean precisely
\[
 \begin{aligned}
 a&=(A_0)_z(0,0,0),&p_{30}&=[x^3y^0z^0]P,\\
 p_{121}&=[x^2yz]P,&p_{62}&=[x^6y^0z^2]P.
 \end{aligned}                                                   \tag{4}
\]
All coefficients are ordinary polynomial coefficients, without
factorial normalization. The labels refer to the explicitly specified
monomials, not to a different indexing convention.

Relation (3) records how moving \(x\) changes the obstruction in
[619](venereau-x-fixed-shift-two-exclusion-pass619-working.md).
It is not a contradiction. Two complete polynomial controls below
satisfy it, \(Dv=1\), zero divergence, exact shift two, and a locally
nilpotent full \(u\)-initial derivation. One even has \(Dx\bmod x=z\).
Both whole derivations are nevertheless proved not locally nilpotent.

These are counterexamples to the sufficiency of the stated necessary
tests, not solutions of the shift-two completion problem. The existence
of an unrestricted shift-two LND or coordinate partial for this
specified \(v\) remains UNRESOLVED. No cancellation, termination,
arbitrary-entry, or novelty claim is made.

## 2. The exact unrestricted normal form

Suppose \(D\) is locally nilpotent, \(Dv=1\), and \(\delta(D)=2\).
The full filtration proof in
[618](venereau-shift-two-constraints-and-failed-lift-pass618-working.md)
gives
\[
 \overline D=\eta^2N\ \hbox{on }A[\eta],\qquad
 0\ne N\in\operatorname{LND}(A),\qquad N(x^3y^2)=0.         \tag{5}
\]
Indeed, every successive nonzero leading iterate lifts to an iterate
of \(D\), so the leading derivation is locally nilpotent. Homogeneity
makes \(\overline D\eta\) a multiple of \(\eta\). The locally nilpotent
semivariant lemma forces that image to vanish, so \(\deg_u Du\le2\).
Factorial closure gives \(Nx=Ny=0\). Localization to
\(\mathbb C(x,y)[z]\) then shows \(N=g(x,y)\partial_z\), since an LND
on a one-variable polynomial ring over a field has constant coefficient.

The exact whole components can be written
\[
 \begin{aligned}
 Dx&=A_0+xuP,&Dy&=B_0+x^2uQ,\\
 Dz&=C_0+uC_1+u^2yG,&Du&=d_0+ud_1+u^2d_2,
 \end{aligned}                                                   \tag{6}
\]
where all coefficients except \(G\) are arbitrary polynomials in \(A\),
and the whole coefficient equations of 618 give
\[
 G\in\mathbb C[x,y]\setminus\{0\},\quad
 g=yG\in(y^2,x^3y)\mathbb C[x,y],\quad B_0\equiv1\pmod{x^2A}.
                                                               \tag{7}
\]
In particular \(x\mid[u]Dx\) does not imply \(x\mid Dx\).
No assumption that \((x)\) is \(D\)-stable is made.

Put \(K=1+x^3z^2\) and \(\alpha=x+2yz\). The exact middle equation
from 618 is
\[
 KQ+3y^2A_0+
 x\bigl(2yB_0+y^2d_1+(4xz+3yz^2)P+\alpha C_1\bigr)=0.    \tag{8}
\]
Modulo \(x\), it licenses the polynomial substitutions
\[
 Q=-3y^2A_0+xR,\qquad
 B_1:=[u]Dy=-3x^2y^2A_0+x^3R,\qquad
 \tau=d_2+3P-6x^2yA_0.                                  \tag{9}
\]
Both \(R,\tau\) belong to \(A\); no localization is used.

## 3. Full transformed equations

The three coefficients of the entire equality \(Dv=1\) now become
\[
 T:=2x^3R+y\tau+\alpha G=0,                              \tag{10}
\]
\[
 M:=KR+2yB_0+y^2d_1+(4xz+3yz^2)P+\alpha C_1
                         -3x^2y^2z^2A_0=0,              \tag{11}
\]
\[
 KB_0+x^3\alpha C_0+x^3y^2d_0
                         +(4x^3z+3x^2yz^2)A_0=1.        \tag{12}
\]
Precisely, \([u^2]Dv=x^3yT\), \([u]Dv=x^3M\), and the left side of
(12) is \([1]Dv\). No other powers occur.

Every polynomial LND has zero divergence: its finite exponential is a
polynomial automorphism over \(\mathbb C[t]\), whose Jacobian is a unit
and equals 1 at \(t=0\). Differentiating at \(t=0\) proves the assertion.
The whole divergence of (6), after (9), is the constant term
\[
                     A_{0,x}+B_{0,y}+C_{0,z}+d_1          \tag{13}
\]
plus \(u\) times
\[
 V:=x^3R_y+C_{1,z}+2\tau+xP_x-5P
                         +6x^2yA_0-3x^2y^2A_{0,y}.      \tag{14}
\]
Both expressions vanish. The potential \(u^2\) coefficient is zero
because \(G_z=0\). All derivatives are genuine derivatives of the
displayed coefficient polynomials.

These are the additional moving-\(x\) terms that must be retained.
In particular neither they nor \(C_{1,z}\) may be dropped to restore
the \(x\)-fixed proof. The residue deduction below uses only
(10)--(12), (14), and \(G_z=0\).

## 4. Exact first two y-coefficient elimination

Introduce the ordinary coefficient notation
\[
 \begin{gathered}
 a_0=A_0(x,0,z),\quad p_0=P(x,0,z),\quad p_1=[y]P,\quad
 b=B_0(x,0,z),\\
 r_i=[y^i]R,\quad e_i=[y^i]G,\quad c_i=[y^i]C_1,\quad
 t_i=[y^i]\tau.
 \end{gathered}                                                   \tag{15}
\]
The \(e_i\) lie in \(\mathbb C[x]\); the others lie in
\(\mathbb C[x,z]\). No degree bounds are imposed on these polynomials.

Equation (12) at \(y=0\) is
\(Kb+x^4C_0(x,0,z)+4x^3za_0=1\). Inversion of \(K\) modulo \(x^4\)
therefore gives an actual polynomial \(F\in\mathbb C[x,z]\) with
\[
                     b=1-x^3z^2-4x^3za_0+x^4F.           \tag{16}
\]
This is an exact equality with polynomial remainder, not division by
\(K\) in the whole ring or an infinite expansion.

The constant \(y\)-coefficient of (10) gives \(e_0=-2x^2r_0\), so
\(r_0\) is independent of \(z\). The corresponding coefficient of
(11) is \(Kr_0+4xzp_0+xc_0=0\), which forces \(x\mid r_0\).
For some \(h\in\mathbb C[x]\), one obtains
\[
                 r_0=xh,\quad e_0=-2x^3h,\quad c_0=-Kh-4zp_0.
                                                               \tag{17}
\]
The coefficient of \(y\) in (10), and the constant coefficient in
(14), are
\[
 \begin{aligned}
 t_0&=-2x^3r_1-xe_1-2ze_0,\\
 0&=x^3r_1+(c_0)_z+2t_0+x(p_0)_x-5p_0.
 \end{aligned}                                                   \tag{18}
\]
Set \(S=r_1-2zh\) and \(J_0=x(p_0)_x-9p_0-4z(p_0)_z\).
Substitution into (18) yields
\[
                       E_1:=2xe_1+3x^3S-J_0=0.           \tag{19}
\]
Modulo \(x\), this is \(9p_0(0,z)+4z(p_0)_z(0,z)=0\).
Each coefficient of \(z^j\) is multiplied by \(9+4j\ne0\).
Therefore
\[
                                  p_0(0,z)=0.           \tag{20}
\]
The coefficient of \(y\) in (11) gives
\[
                    xc_1=-KS-2b-4xzp_1+5z^2p_0.         \tag{21}
\]
Using (16) and (20), its reduction modulo \(x\) says
\[
                                   S(0,z)=-2.           \tag{22}
\]
These reductions are reductions of polynomial identities. None assumes
that \(D\) descends modulo \((x)\).

The \(y^2\) coefficient of (10) and the \(y\) coefficient of (14) are
\[
 \begin{aligned}
 t_1&=-2x^3r_2-xe_2-2ze_1,\\
 0&=2x^3r_2+(c_1)_z+2t_1+x(p_1)_x-5p_1+6x^2a_0.
 \end{aligned}                                                   \tag{23}
\]
Eliminating \(t_1,c_1,e_1\) with (19), (21), and (23) gives the
whole functional identity
\[
 \begin{aligned}
 2x^2e_2={}&-2x^4r_2-KS_z+4x^3zS-2b_z
              +28zp_0+13z^2(p_0)_z-2xz(p_0)_x\\
          &+x^2(p_1)_x-9xp_1-4xz(p_1)_z+6x^3a_0.
 \end{aligned}                                                   \tag{24}
\]
For an off-equation check, call the second line of (23) \(V_1\),
and call the right side of (24) \(R_*\). After the other displayed
substitutions, the exact identity is
\[
                         xV_1=R_*-2x^2e_2-2zE_1.        \tag{25}
\]
Thus no division by a coefficient value, or independence of genuine
coefficient derivatives, is being assumed.

## 5. Exact coefficient extraction

Differentiate (24) with respect to \(z\), and extract \([x^3z^0]\).
The left side vanishes because \(e_2\in\mathbb C[x]\).
The term involving \(r_2\) has a factor \(x^4\) and contributes zero.
For the term \(-KS_z\), differentiate (19) twice in \(z\):
\[
 3x^3S_{zz}=x(p_0)_{xzz}-17(p_0)_{zz}-4z(p_0)_{zzz}.     \tag{26}
\]
Here \((e_1)_z=0\) was used. At \(z=0\), (26) implies
\[
                    -[x^3z^0]S_{zz}=\frac{22}{3}p_{62}. \tag{27}
\]
Indeed, the coefficients of \(x^6z^0\) in \((p_0)_{zz}\) and
\(x(p_0)_{xzz}\) are respectively \(2p_{62}\) and \(12p_{62}\).
This is coefficient extraction from a polynomial identity, not
evaluation after division by \(x\).

Every contribution to \([x^3z^0]\partial_z(24)\) is recorded here:

| Term before the z derivative | Contribution |
|---|---:|
| \(-2x^4r_2\) | \(0\) |
| \(-KS_z\) | \(22p_{62}/3\) |
| \(4x^3zS\) | \(-8\), by (22) |
| \(-2b_z\) | \(4+16a\), by (16) |
| \(28zp_0+13z^2(p_0)_z-2xz(p_0)_x\) | \(22p_{30}\) |
| \(x^2(p_1)_x-9xp_1-4xz(p_1)_z\) | \(-11p_{121}\) |
| \(6x^3a_0\) | \(6a\) |

In the second row \(K(x,0)=1\) and \(K_z(x,0)=0\).
In the fourth row \(x^4F_{zz}\) contributes zero. Summation gives
\[
                   22a+22p_{30}-11p_{121}+\frac{22}{3}p_{62}-4=0,
                                                               \tag{28}
\]
which proves (3).

No degree bound was put on a coefficient polynomial. Higher
coefficients cannot contribute to the specified monomial under the
displayed differentiations and multiplications. This is not a
finite-degree candidate search. It forces the combination (3), not
\(a\ne0\) by itself.

## 6. An independent finite coefficient certificate

The General affine agent independently supplied a direct certificate
for the same residue. It is included as a second check, not an extra
assumption or a separate result. Write the raw whole components as
\[
 Dx=A_0+uA_1,\quad Dy=B_0+uB_1,\quad
 Dz=C_0+uC_1+u^2g,\quad Du=d_0+ud_1+u^2d_2,
\]
with \(g\in y\mathbb C[x,y]\). Define
\[
 \mathsf C=[u^0]Dv,\quad \mathsf M=[u]Dv,\quad
 \mathsf T=[u^2]Dv,\quad \mathsf J=[u]\operatorname{div}D,
\]
and
\[
 \mathcal L=[z]A_0+[x^4]A_1-\tfrac12[x^3yz]A_1
                              +\tfrac13[x^7z^2]A_1.     \tag{29}
\]
Here brackets extract precisely the displayed monomial in \(x,y,z\).
Direct expansion of coefficient operators gives
\[
 \begin{aligned}
 66\mathcal L={}&12[1]\mathsf C+12[x^3z^2]\mathsf C\\
 &+6[x^2y^2z]\mathsf M-12[x^3y]\mathsf M-6[x^6yz^2]\mathsf M\\
 &+18[x^7z]\mathsf M+6[x^{10}z^3]\mathsf M\\
 &-6[x^5y^3z]\mathsf T+12[x^6y^2]\mathsf T
                                  +4[x^9y^2z^2]\mathsf T\\
 &-12[x^{10}yz]\mathsf T-3[x^{13}yz^3]\mathsf T\\
 &+3[x^2yz]\mathsf J-6[x^3]\mathsf J-2[x^6z^2]\mathsf J.
 \end{aligned}                                                   \tag{30}
\]
For an explicit verification of its all-degree scope, allow arbitrary
polynomial \(g\) temporarily, retaining the raw component degree bounds.
The right side of (30) minus \(66\mathcal L\) expands to exactly
\[
 \begin{aligned}
 &-6[xy^3z]g+4[x^5y^2z^2]g-4[x^6yz]g\\
 &\hspace{8mm}-24[x^7]g-3[x^9yz^3]g-6[x^{10}z^2]g.
 \end{aligned}                                                   \tag{31}
\]
All six terms vanish when \(g\in y\mathbb C[x,y]\). These identities
follow by expanding the finite polynomials \(v_x,v_y,v_z,v_u\) in
\(Dv\) and applying the ordinary coefficient differentiation rule
\([x^iy^jz^k]\partial_x F=(i+1)[x^{i+1}y^jz^k]F\), and likewise for
the other variables. No support cutoff on the unknown coefficients
is involved.

For \(Dv=1\) and zero divergence, (30) gives
\(66\mathcal L=12\). Substituting \(A_1=xP\) makes
\(\mathcal L=a+p_{30}-p_{121}/2+p_{62}/3\), again giving (3).
The author freshly checked (30)--(31) by expanding every possible
contributing coefficient operator, independently of the functional
elimination in Sections 4--5.

## 7. A complete divergence-free control

The General affine agent constructed the following whole polynomial
derivation \(D_*\); the author and root independently checked it.
Every right side below is divided by 33:
\[
 \begin{aligned}
 33D_*x={}&-11ux^4-34ux^3yz-12x^3z^3-30x^2yz^4,\\
 33D_*y={}&33-66ux^3y-33x^3z^2,\\
 33D_*z={}&132u^2x^2y^2+44ux^3z+213ux^2yz^2
                                      +81x^2z^4-6xyz^5,\\
 33D_*u={}&33u^2x^3-162u^2x^2yz-288ux^2z^3
                                      +90uxyz^4+102xz^6.
 \end{aligned}                                                   \tag{32}
\]
Expanding these entire polynomials gives
\[
                       D_*v=1,\qquad\operatorname{div}D_*=0.
                                                               \tag{33}
\]
Equivalently, summing \((D_*\xi)v_\xi\) over the four original
variables gives 1, and summing \(\partial_\xi(D_*\xi)\) gives 0.
The exact component \(u\)-degrees are \((1,1,2,2)\), so
\[
 \delta(D_*)=2,\qquad
 \overline{D_*}=\eta^2(4x^2y^2\partial_z).                \tag{34}
\]
This full \(u\)-initial derivation is locally nilpotent and kills the
speed \(x^3y^2\).

Nevertheless \(D_*\) is not locally nilpotent: its whole \(D_*x\)
is nonzero and divisible by \(x^2\), hence by \(x\). For an LND on a
domain, \(Dx=xq\ne0\) would imply
\(\deg_Dx-1=\deg_Dx+\deg_Dq\), which is impossible.

The first component gives the whole coefficient polynomials
\[
 A_0=-\frac4{11}x^3z^3-\frac{10}{11}x^2yz^4,\qquad
 P=-\frac13x^3-\frac{34}{33}x^2yz.                       \tag{35}
\]
Thus its residue data are
\[
 (a,p_{30},p_{121},p_{62})=(0,-1/3,-34/33,0),
 \qquad -1/3+17/33=2/11.                                 \tag{36}
\]
The whole coefficient and divergence equations can therefore absorb
the residue while still failing local nilpotence.

## 8. A control whose full Dx is not divisible by x

The root agent supplied the Hamiltonian addition
\[
 \mathcal H=z(v_y\partial_x-v_x\partial_y),\qquad
 D^\sharp=D_*+\mathcal H.                                \tag{37}
\]
The complete derivatives are
\[
 v_y=1+x^3z^2+2x^3yu,\qquad
 v_x=4x^3z+3x^2yz^2+3x^2y^2u.                           \tag{38}
\]
Thus (32), together with the exact additions
\[
 \begin{aligned}
 D^\sharp x-D_*x&=z+x^3z^3+2x^3yzu,\\
 D^\sharp y-D_*y&=-4x^3z^2-3x^2yz^3-3x^2y^2zu,\\
 D^\sharp z-D_*z&=0,\qquad D^\sharp u-D_*u=0,
 \end{aligned}                                                   \tag{39}
\]
specifies every whole polynomial component.
Cancellation gives \(\mathcal H v=0\), and equality of mixed partials
gives \(\operatorname{div}\mathcal H=z(v_{yx}-v_{xy})=0\).
Consequently
\[
 \begin{gathered}
 D^\sharp v=1,\quad\operatorname{div}D^\sharp=0,\quad
 \delta(D^\sharp)=2,\quad
 \overline{D^\sharp}=\eta^2(4x^2y^2\partial_z),\\
                         D^\sharp x\bmod x=z.
 \end{gathered}                                                   \tag{40}
\]
The exact component \(u\)-degrees are again \((1,1,2,2)\).
The simple whole-\(x\) semivariant rejection of \(D_*\) is unavailable.

Its \(A_0\) gains \(z+x^3z^3\), and its \(P\) gains \(2x^2yz\).
Accordingly
\[
 (a,p_{30},p_{121},p_{62})=(1,-1/3,32/33,0),
 \qquad 1-1/3-16/33=2/11.                                \tag{41}
\]
This is a complete control with genuine motion through \(x=0\), not
a formal selection of leading vectors.

## 9. A second filtration proves the moving-x control is not LND

Use ordinary total degree, with all four original variables of degree
one. The maximum component degree of \(D^\sharp\) is 7, so its exact
shift for this filtration is 6. Every component of \(\mathcal H\) has
degree at most 6 and cannot alter the ordinary full initial derivation.
Extracting every degree-seven component of (32) gives
\[
 \begin{aligned}
 D_{\rm top}x&=-\frac{10}{11}x^2yz^4,&D_{\rm top}y&=0,\\
 D_{\rm top}z&=-\frac2{11}xyz^5,&
 D_{\rm top}u&=\frac{30uxyz^4+34xz^6}{11}.
 \end{aligned}                                                   \tag{42}
\]
This is the entire ordinary initial derivation. Its nonzero image of
\(x\) is a multiple of \(x\), so the semivariant lemma proves that
\(D_{\rm top}\) is not locally nilpotent.

If \(D^\sharp\) were locally nilpotent, its full leading derivation
for this ordinary-degree filtration would also be locally nilpotent.
Every successive nonzero leading iterate is the initial form of the
corresponding whole iterate, with degree increased by 6 at each step.
Eventual vanishing of whole iterates forces eventual vanishing of the
leading iterates. This contradicts (42), proving that \(D^\sharp\)
is not locally nilpotent.

This argument is not a finite-iterate test. It uses the complete
leading derivation in a second filtration, despite local nilpotence
of the \(u\)-initial derivation in (40).

## 10. Evidence and conclusion

The author derived the functional elimination and coefficient
extraction from the full 618 equations. The General affine agent
independently supplied the coefficient certificate (30) and constructed
(32). The root agent constructed (37). Fresh independent unsaved
algebra verified the whole transformed equations, all functional
eliminations, every coefficient-operator term of (30)--(31), the
complete four-component controls, both divergence identities, the
residue evaluations, and every component of (42).

No saved checker was executed, imported, or compiled. No canonical
file or prior source was edited. No human expert review, formal proof
assistant certification, or priority determination is claimed.
Author EOF review and independent saved-source review are distinct gates.

The exact conclusion is that the nonzero residue (3) must be
accounted for, but polynomial coefficient consistency, whole zero
divergence, a locally nilpotent \(u\)-initial action, and nonzero
motion of \(x\) modulo \(x\) still do not suffice to produce an LND.
The unrestricted shift-two problem remains UNRESOLVED. Neither control
is an actual coordinate partial or generates an algebraic additive-group
action. The starting \(E=\partial_u\) already has polynomial kernel;
this is a boundary for a proposed reduction method, not a cancellation
counterexample.
