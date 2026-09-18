# A polynomial cylinder velocity cannot support the exact cubic branch

In the actual nonconical constant-acceleration setting, the exact cubic
relative branch cannot have velocity column \(b=(s,t,f(s))^t\) with
\(f\in\mathbb C[s]\). The original potential and unit volume force
\(f(s)=a s^3+c s\), with \(a\ne0\). That coefficient family has a
common zero in its speed row, contradicting the actual unit-row theorem.

This is a restriction on a specified velocity form, not a reduction of
every cubic branch to that form. A principal-open example realizes the
forced cubic family and its unit volume. Thus neither rank-one cubic
tensor nor generic volume compatibility alone gives a contradiction.
No cancellation or historical-novelty claim is made.

## 1. Actual hypotheses and the cylinder connection

Retain the actual hypotheses of [invariant-plane88](constant-acceleration-invariant-plane-pass88.md),
[potential90](nonconical-quadratic-potential-pass90.md) and
[cubic-relation90](nonconical-cubic-relation-pass90.md). In particular,
all four original generators are polynomial coordinates, the action has
its polynomial slice, and the intrinsic invariant plane is the actual
embedded plane S. Add the displayed velocity assumption:

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\quad A=\ker E,\quad
Eu=1,\quad Ez=qu,\quad q\in\mathbb C^*,\\
S=\mathbb C[s,t],\qquad Ex_{\rm tr}=b=(s,t,f(s))^t,
\quad f\in\mathbb C[s],\quad (s,t,f(s))S=S,\\
\Omega=\det[b,b_s,b_t]=f-sf'\ne0,\qquad
g=\frac{f''}{\Omega},\quad
G_{11}=g,\quad C^1_{11}=-sg,\quad C^2_{11}=-tg,\\
G_{12}=G_{22}=0,\qquad C^j_{12}=C^j_{22}=0,\qquad
T_{111}=\tau:=-g'-2sg^2,
\quad T_{112}=T_{122}=T_{222}=0.
\end{gathered}
\tag{1}
\]

These connection coefficients follow directly by expanding
\(b_{ss}=(0,0,f'')^t\) in the three columns \(b,b_s,b_t\).
The other second derivatives vanish. Substitution in90's definition of
T gives its last line. Primes below mean the ordinary derivative in s.
The unit-row premise is the actual consequence88, not an additional
coefficient ansatz. In this form it is equivalent to \(f(0)\ne0\).

Let \(K=\mathbb C(s,t)\). The two actual relative generators satisfy
\(A_K=K[y_1,y_2]=K[v]\). Assume their irreducible plane relation has
exact total degree three. The nonzero potential relation90 is then a
nonzero scalar multiple of that irreducible cubic. In particular
\(\tau\ne0\), since its only possible cubic term is
\(q\tau Y_1^3/6\).

## 2. The original first relative variable is already linear

The elementary curve calculation90 shows that the maximum v-degree
of the two generators is three and that degrees (2,3) cannot generate
K[v]. The potential's unique cubic monomial also shows that y1 cannot
have v-degree three: its ninth-degree contribution could not cancel
against any quadratic or linear term. Thus y2 has degree three and
y1 has degree at most two. Degree two is the excluded (2,3) case;
degree zero cannot generate K[v] together with a degree-three element.
Consequently y1 has degree one.

Use the actual generic coordinate \(v=y_1\). Changing from the
intrinsic generic coordinate to this one scales the volume determinant
by an element of K*, and introduces no v-dependent denominator. Write
\(y_2=R(s,t,v)\), of degree three in v. In the potential relation,
the v-six coefficient first forces \(B_{22}=0\), and then the v-four
coefficient forces \(B_{12}=0\). Here B denotes the symmetric array90,
not the original polynomial ring. For (1), these entries are
\(-\rho_{tt}\) and \(-\rho_{st}\). Hence

\[
\begin{gathered}
\rho=A(s)+c t,\quad A\in\mathbb C(s),\ c\in\mathbb C,\qquad
B_{11}=g(A-sA')-A'',\\
L_i=\chi_i+q\rho\rho_i,\qquad L_2\ne0,\\
R=a_0+a_1v+a_2v^2+a_3v^3
=\frac{\zeta-L_1v-(q/2)B_{11}v^2-(q/6)\tau v^3}{L_2},
\qquad a_3=-\frac{q\tau}{6L_2}\ne0.
\end{gathered}
\tag{2}
\]

The vanishing second derivatives of the rational function rho justify
its displayed form in characteristic zero. If L2 were zero, the
remaining polynomial relation would be a nonzero polynomial in the
transcendental element v, which is impossible. No affine transformation
of the base derivative fields is made here.

## 3. The unit determinant gives a scalar compatibility equation

In these unchanged base coordinates, the matrix entries90 are
\(K_{11}=\rho-sgv\), \(K_{12}=0\),
\(K_{21}=R_s-tgv\), \(K_{22}=\rho+R_t\).
The evaluated gradient is \((-L_2R_v,L_2)\). Expanding the actual
three-by-three volume determinant therefore gives

\[
\frac{\mathcal J}{\Omega L_2}
=R_s+R_vR_t+sgvR_v-tgv\in K^*.
\tag{3}
\]

The actual original-coordinate volume supplies the unit. All entries
are polynomials in v and u over K, because only base elements were
inverted in90. A merely nonzero rational Jacobian would not suffice.

Compare positive powers of v in (3). The v-five coefficient is
\(3a_3(a_3)_t\), so \((a_3)_t=0\). The v-four coefficient then
gives \((a_2)_t=0\). The v-three coefficient says
\((a_1)_t=-sg-a_3'/(3a_3)\), a function only of s. Put
\(a_1=h(s)t+j(s)\). The v-two coefficient now makes
\((a_0)_t\) a function only of s, so \(a_0=k(s)t+l(s)\).
The t-coefficient of the v-one term is consequently

\[
h'+h^2+sg h-g=0,\qquad h=-sg-\frac{a_3'}{3a_3}.
\tag{4}
\]

There is a second, independent expression for h from the potential.
Since \(a_3=-q\tau/(6L_2)\) and \((a_3)_t=0\), one has
\((L_2)_t=0\). Integrating
\(\chi_t=L_2-qcA-qc^2t\) gives
\(\chi=(L_2-qcA)t-qc^2t^2/2+\chi_0(s)\).
Thus \(L_1=L_2't+\chi_0'+qAA'\). Comparing the t-coefficient
of \(a_1=-L_1/L_2\) yields

\[
h=-\frac{L_2'}{L_2},\qquad
\frac{a_3'}{a_3}=\frac{\tau'}{\tau}+h,\qquad
\boxed{\quad h=-\frac14\left(3sg+\frac{\tau'}{\tau}\right),
\qquad h'+h^2+sg h-g=0.\quad}
\tag{5}
\]

These necessary identities combine actual potential and actual volume.
They do not follow from the rank-one tensor in (1) alone.

## 4. Polynomial asymptotics force the forbidden cubic speed

If f has degree at most one, then g and tau vanish, already contradicting
the exact cubic branch. Let \(n=\deg f\ge2\). Laurent expansion at
infinity, using \(\Omega\sim(1-n)f\), gives

\[
\begin{gathered}
g=-\frac n{s^2}+O(s^{-3}),\qquad
\tau=-\frac{2n(n+1)}{s^3}+O(s^{-4}),\qquad
h=\frac{3(n+1)}{4s}+O(s^{-2}),\\
h'+h^2+sg h-g
=-\frac{(3n-1)(n-3)}{16s^2}+O(s^{-3}).
\end{gathered}
\tag{6}
\]

The rational identity (5) forces its Laurent coefficients to vanish.
For the integer n at least two, (6) gives n=3.
Write \(f=a s^3+b s^2+c s+d\), with \(a\ne0\), and set
\(\beta=b/a\), \(\delta=d/a\). The linear term c drops from
both f'' and Omega. Direct expansion of the definitions gives

\[
\begin{gathered}
g=-3s^{-2}+\tfrac12\beta s^{-3}+O(s^{-4}),\quad
\tau=-24s^{-3}+\tfrac{15}2\beta s^{-4}+O(s^{-5}),\quad
h=3s^{-1}-\tfrac{29}{64}\beta s^{-2}+O(s^{-3}),\\
h'+h^2+sg h-g=\tfrac{35}{64}\beta s^{-3}+O(s^{-4}),\\[2pt]
\text{if }\beta=0:\quad
g=-3s^{-2}-\tfrac32\delta s^{-5}+O(s^{-8}),\quad
\tau=-24s^{-3}-\tfrac{51}2\delta s^{-6}+O(s^{-9}),\\
h=3s^{-1}+\tfrac{123}{64}\delta s^{-4}+O(s^{-7}),\quad
h'+h^2+sg h-g=-\tfrac{315}{64}\delta s^{-5}+O(s^{-8}).
\end{gathered}
\tag{7}
\]

For example, substituting the first g and tau expansions into (5)
gives the displayed coefficient -29/64 of h. In the second case,
the residual coefficient is \(-123\delta/64-3\delta\).
Thus these coefficients can be checked directly without expanding
a large rational numerator. Identity (5) first forces b=0 and then
d=0. Hence f has the asserted form \(a s^3+c s\).
But at \((s,t)=(0,0)\) all three entries of b vanish, contradicting
the actual unit row in (1). This excludes the exact cubic relative
branch under the specified polynomial cylinder-velocity assumption.

## 5. Scope and the compatible principal-open boundary

The [principal-open control118](cubic-principal-open-frame-control-pass118.md)
constructs the speed \((s,t,s^3)\) with the complete potential and
nonzero constant original-coordinate Jacobian on s nonzero. Its
coordinate inverse is valid on that principal open set, but its
canonical slice has a genuine pole on the omitted divisor.
This matches the forced family above and shows why the final global
unit-row gate cannot be dropped. It is not an actual global polynomial
four-space frame or a counterexample to this theorem.

The argument does not prove that an arbitrary rank-one cubic tensor can
be put into the cylinder-velocity form by allowed changes. In general,
a base-dependent affine change of the two relative variables also
changes the tangent frame; its resulting base fields need not commute.
The unchanged coordinates s,t used above avoid that additional issue.
The exact cubic branch outside this velocity family remains untreated
here, as does entry of an arbitrary sliced derivation into the supplied
constant-acceleration framework.

There is also a useful limit on changing the base of this theorem.
Pull back the principal-open control by the polynomial substitution
\(t_{\rm old}=st-1\). Its new speed column is
\((s,st-1,s^3)\), which is globally a unit row, since
\(1=ts-(st-1)\). Its determinant is \(-2s^4\), and the
pulled-back original-coordinate Jacobian is \(-2s\), a unit on
the same s-open set. The canonical slice still has the original
pole. This is not a counterexample to the theorem: the substitution
is not an automorphism of the whole polynomial base plane, since
its inverse requires division by s. It prevents extending the
cylinder exclusion merely by a birational base normalization.

The [quadratic reduction117](quadratic-velocity-shear-pass117.md)
has a different premise, namely relative degree two. This proof uses
the actual volume/potential framework90 and unit row88 directly,
without its recognition endpoint or the later conic/fiber chain.
The complete retained statements just used were read through EOF.
The Laurent calculation was also checked in an inline symbolic
calculation, which is finite evidence distinct from the written
all-degree argument. No new primary theorem or original-paper proof
was imported, and no numerical calculation certifies an actual frame.

The later [polynomial-pullback proof118](cubic-polynomial-pullback-exclusion-pass118.md)
retains this scalar argument and proves a stronger exclusion for
\(b=(s,p(s,t),f(s))\), with \(p_t\ne0\). Its new endpoint is
irreducibility of an original affine-linear coordinate. It therefore
excludes the unimodular pullback above without treating that polynomial
base substitution as a global automorphism. This note remains the
scalar-calculation prerequisite, not an additional independent branch.

The third method of the shared [checker118](cubic_moving_frame_checks_pass118.py)
checks the exact residual for degrees two, three and four and the two
generic cubic Laurent coefficients. These finite tests do not establish
the all-degree argument in (6), the actual volume hypothesis, or the
polynomial-pullback transfer. The final three-method code was reviewed
through EOF here without a further execution; its author run and the
root's canonical capture are separate evidence.
