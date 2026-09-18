# Vénéreau shift-two constraints and a failed polynomial lift

Date: 2026-09-17. Private bounded working note; novelty UNKNOWN.
General complex-threefold cancellation remains UNSOLVED.

## 1. Result, setting, and limits

Work throughout in the actual polynomial ring
\[
 B=\mathbb C[x,y,z,u],\qquad A=\mathbb C[x,y,z],\qquad E=\partial_u,
\]
and fix the third Vénéreau coordinate
\[
 v=y+x^3\bigl(xz+y(yu+z^2)\bigr)=a u+b,
 \quad a=x^3y^2,\quad b=y+x^4z+x^3yz^2.                 \tag{1}
\]
Its whole polynomial coordinate status, with an explicit completion and
inverse, is supplied by
[615](venereau-coordinate-positive-shift-obstruction-pass615-working.md).
That source constructs a coordinate partial of shift 10; it does not
assert that this shift is minimal. The present note does not require
any new coordinate-status or literature-priority assertion.

For a nonzero polynomial derivation \(D\), use \(\deg_u0=-\infty\) and
define its exact shift by
\[
 \delta(D)=\max\{\deg_u Dx,\deg_u Dy,\deg_u Dz,\deg_u Du-1\}.
                                                               \tag{2}
\]
The Leibniz rule makes this the exact shift on all of \(A[u]\), not just
a bound on the four displayed generators.

This note establishes necessary equations for every locally nilpotent
derivation \(D\) with \(Dv=1\) and \(\delta(D)=2\). It also constructs a
whole polynomial derivation with \(Dv=1\), exact shift 2, and locally
nilpotent full initial derivation, but whose nonzero divergence proves
that the whole derivation is not locally nilpotent. No divergence-free
repair of shift at most 2 can retain its specified \(Dx,Dy\).
A separate elementary obstruction rules out retaining both \(x\) and
the auxiliary polynomial \(W\) from 615 as invariants of any derivation
sending \(v\) to 1.

These are bounded obstructions. The existence of a shift-two locally
nilpotent derivation, or an actual shift-two coordinate-partial
completion, remains unresolved in general. No equations below are
promoted to local nilpotence merely because they have polynomial
solutions. Nothing here establishes arbitrary four-variable entry,
termination of coordinate changes, or cancellation.

## 2. Necessary full initial action at shift two

Assume in this section that \(D\) is locally nilpotent, \(Dv=1\), and
\(\delta(D)=2\). Its nonzero homogeneous leading derivation on
\(\operatorname{gr}_uB=A[\eta]\) is locally nilpotent: successive nonzero
leading iterates lift to the corresponding iterates of \(D\), which
eventually vanish. Homogeneity gives
\(\overline D\eta=\beta\eta^3\). A locally nilpotent derivation on a
characteristic-zero domain cannot send an element to a nonzero multiple
of itself. Indeed, additivity of locally nilpotent degree would give
\(\deg_D h-1=\deg_D h+\deg_D q\) if \(Dh=hq\ne0\).
Consequently \(\overline D\eta=0\) and \(\deg_u Du\le2\).

It follows that
\[
 \overline D=\eta^2N,\qquad
 0\ne N\in\operatorname{LND}(A),\qquad N(a)=0.           \tag{3}
\]
The last equality is the coefficient of \(u^3\) in
\(D(au+b)=1\). Local nilpotence of \(N\) follows from
\(\overline D^{\,j}c=\eta^{2j}N^jc\) for \(c\in A\).
This is the shift-two specialization of
[614](nonunit-speed-coordinate-induced-action-pass614-working.md),
with its leading-filtration argument recalled here explicitly.

Factorial closure of \(\ker N\), applied to \(a=x^3y^2\), gives
\(Nx=Ny=0\). Thus
\[
             N=g(x,y)\partial_z,\qquad g\ne0.           \tag{4}
\]
To justify the lack of \(z\)-dependence, localize at the nonzero elements
of \(\mathbb C[x,y]\), which are killed by \(N\). A nonzero locally
nilpotent derivation of \(\mathbb C(x,y)[z]\) has constant coefficient
in front of \(\partial_z\); a coefficient of positive \(z\)-degree has
nonvanishing iterates on \(z\). Hence the original polynomial
coefficient lies in \(\mathbb C[x,y]\).

Therefore there are polynomials in \(A\) such that
\[
 \begin{aligned}
 Dx&=A_0+uA_1,& Dy&=B_0+uB_1,\\
 Dz&=C_0+uC_1+u^2g,& Du&=d_0+ud_1+u^2d_2.
 \end{aligned}                                                   \tag{5}
\]
Here and below \(g\) is restricted as in (4); every other coefficient
is allowed arbitrary dependence on \(x,y,z\) unless explicitly stated.
In particular, no independence of the genuine coefficient derivatives
is assumed.

## 3. Entire coefficient equations and divisibility consequences

Substitution of (5) into the whole equality \(Dv=1\) gives precisely
the following three coefficient equations:
\[
 \begin{aligned}
 0={}&3x^2y^2A_1+2x^3yB_1+x^3y^2d_2+x^3(x+2yz)g,       &&[u^2],\\
 0={}&3x^2y^2A_0+2x^3yB_0+x^3y^2d_1
 +(4x^3z+3x^2yz^2)A_1\\
 &+(1+x^3z^2)B_1+x^3(x+2yz)C_1,                         &&[u],\\
 1={}&(4x^3z+3x^2yz^2)A_0+(1+x^3z^2)B_0
 +x^3(x+2yz)C_0+x^3y^2d_0.                              &&[1]
 \end{aligned}                                                   \tag{6}
\]
There is no omitted higher power of \(u\).

Divide the first equation by \(x^2\) and reduce modulo \(x\).
It gives \(x\mid A_1\). After writing \(A_1=xP\), divide that same
equation by \(x^3\) and reduce modulo \(y\). This gives \(y\mid g\).
The second equation of (6) now gives \(x^2\mid B_1\).
Thus one may write
\[
 A_1=xP,\qquad B_1=x^2Q,\qquad g=yG,
 \quad P,Q\in A,\quad G\in\mathbb C[x,y],\quad G\ne0.     \tag{7}
\]
After domain cancellation, the top and middle equations become
\[
 T:=y(3P+d_2)+2x^2Q+(x+2yz)G=0,                         \tag{8}
\]
\[
 \begin{aligned}
 M:={}&(1+x^3z^2)Q+3y^2A_0\\
 &+x\bigl(2yB_0+y^2d_1+(4xz+3yz^2)P+(x+2yz)C_1\bigr)=0.
 \end{aligned}                                                   \tag{9}
\]
The unaltered constant equation in (6) implies
\[
                         B_0\equiv1\pmod{x^2A}.         \tag{10}
\]

There is an additional useful restriction on the full initial action.
At \(y=0\), equation (9) reads
\[
 (1+x^3z^2)Q(x,0,z)+x^2\bigl(4zP(x,0,z)+C_1(x,0,z)\bigr)=0.
                                                               \tag{11}
\]
Since \(x\) and \(1+x^3z^2\) are coprime, this implies
\(x^2\mid Q(x,0,z)\). Equation (8) at \(y=0\), after cancelling
\(x\), gives \(G(x,0)=-2xQ(x,0,z)\). Hence \(x^3\mid G(x,0)\), and
\[
             G\in(y,x^3)\mathbb C[x,y],\qquad
             0\ne g\in(y^2,x^3y)\mathbb C[x,y].          \tag{12}
\]
In particular the raw initial \(N=g\partial_z\) has no slice, since
its image lies in \(yA\). Its primitive normalization is nevertheless
\(\partial_z\), which does have a slice. This fixed-divisor observation
is not an obstruction to the existence of the whole \(D\).

The fact \(x\mid A_1\) gives only
\(Dx=A_0+xuP\). It does not give \(x\mid Dx\), and the locally
nilpotent semivariant argument cannot be applied to infer \(Dx=0\).
No such inference is used anywhere in this note.

## 4. The whole divergence equations

Every locally nilpotent derivation of a polynomial ring has zero
divergence in polynomial coordinates. To see this directly,
\(\exp(tD)\) is a polynomial automorphism over \(\mathbb C[t]\), with
inverse \(\exp(-tD)\). Its Jacobian is a unit of
\(\mathbb C[t,x,y,z,u]\), hence a nonzero complex constant. At \(t=0\)
it is 1. Differentiating at \(t=0\) gives \(\operatorname{div}D=0\).

Using (5) and (7), the complete divergence is
\[
 \begin{aligned}
 \operatorname{div}D={}&A_{0,x}+B_{0,y}+C_{0,z}+d_1\\
 &+u\bigl(P+xP_x+x^2Q_y+C_{1,z}+2d_2\bigr).
 \end{aligned}                                                   \tag{13}
\]
The potential \(u^2\) coefficient is \(g_z=0\), already justified
in (4). Thus both displayed coefficients in (13) must vanish.
Combining its \(u\) coefficient with (8), without dividing by \(y\),
gives the further necessary identity
\[
 y\bigl(xP_x-5P+x^2Q_y+C_{1,z}\bigr)
       -4x^2Q-2(x+2yz)G=0.                               \tag{14}
\]
More precisely the left side is identically
\(y[u]\operatorname{div}D-2T\), even before either equation is imposed.

The term \(C_{1,z}\) is indispensable. In particular, even after an
additional assumption \(Dx=0\), it cannot be deleted from the
divergence equation without a separate proof. These equations are
necessary conditions, not a sufficiency criterion for local nilpotence.

## 5. A whole polynomial lift with the right initial action

The following construction was supplied by the root agent and checked
independently by the author of this note. Define
\[
 \alpha=x+2yz,\qquad h=z^2+2yu,\qquad
 L=x^2-2xyz+4y^2z^2,\qquad J=8xyz-16y^2z^2.              \tag{15}
\]
Define a whole polynomial derivation \(D_*\) by
\[
 \begin{aligned}
 D_*x&=0,& D_*y&=1-x^3h,\\
 D_*z&=Lh^2+y^2u^2J,&
 D_*u&=-8yz^3h^2-\alpha u^2J.
 \end{aligned}                                                   \tag{16}
\]
The exact identity
\(\alpha L-8y^3z^3=x^3\) implies
\[
 \alpha D_*z+y^2D_*u=x^3h^2,
 \qquad
 D_*v=(1+x^3h)(1-x^3h)+x^6h^2=1.                       \tag{17}
\]
Thus this is a whole polynomial lift, not an assigned leading vector.

For explicit degree and derivative verification, its full last two
components are
\[
 \begin{aligned}
 D_*z={}&4x^2y^2u^2
 +(4x^2yz^2-8xy^2z^3+16y^3z^4)u\\
 &+x^2z^4-2xyz^5+4y^2z^6,\\
 D_*u={}&-8x^2yzu^2-32y^2z^5u-8yz^7.
 \end{aligned}                                                   \tag{18}
\]
It has exact shift 2 and full initial derivation
\[
            \overline{D_*}=\eta^2(4x^2y^2\partial_z),    \tag{19}
\]
which is nonzero and locally nilpotent. In particular it passes the
initial-action test and the pure \(Dv=1\) coefficient equations.
But the full divergence is
\[
 \operatorname{div}D_*
 =-2u(x^3+4x^2yz+12xy^2z^2-32y^3z^3)
   +2z^3(2x^2-5xyz-4y^2z^2).                            \tag{20}
\]
This polynomial is nonzero; at \((x,y,z,u)=(1,0,0,1)\) it is \(-2\).
Consequently \(D_*\) is not locally nilpotent. A locally nilpotent
initial derivation is not a sufficient substitute for this whole-ring
requirement.

## 6. No divergence-free repair with the first two components fixed

Consider any polynomial derivation \(\widetilde D\) satisfying
\[
 \widetilde Dv=1,\qquad \delta(\widetilde D)\le2,
 \qquad \widetilde Dx=0,\qquad
 \widetilde Dy=1-x^3(z^2+2yu).                            \tag{21}
\]
Local nilpotence is not assumed. Subtracting (17) from
\(\widetilde Dv=1\) and cancelling \(x^3\) gives
\[
 \alpha(\widetilde Dz-D_*z)+y^2(\widetilde Du-D_*u)=0.
\]
The polynomials \(\alpha=x+2yz\) and \(y^2\) are coprime in the
whole UFD \(B\). Hence every solution has exactly the form
\[
 \widetilde Dz=D_*z+y^2f,\qquad
 \widetilde Du=D_*u-\alpha f,
 \qquad f\in B.                                         \tag{22}
\]
This covers all corrections with the two specified components fixed,
not just a selected class of coefficients. Since
\(\deg_u\widetilde Dz\le2\), (18) and (22) force
\[
                f=f_0+uf_1+u^2f_2,\qquad f_i\in A.      \tag{23}
\]
Although a general derivation of shift at most 2 could initially have
\(\deg_u\widetilde Du\le3\), equation (22) itself now gives the
stronger bound \(\deg_u\widetilde Du\le2\). No local-nilpotence
assumption was used to make this reduction.

The change of divergence is precisely
\[
 \operatorname{div}\widetilde D-\operatorname{div}D_*
                  =y^2 f_z-\alpha f_u.                  \tag{24}
\]
If \(\operatorname{div}\widetilde D=0\), comparison of \(u^2\)
in (20), (23), and (24) first gives \(f_{2,z}=0\).
The coefficient of \(u\) then gives
\[
 y^2f_{1,z}-2(x+2yz)f_2
       =2x^3+8x^2yz+24xy^2z^2-64y^3z^3.                 \tag{25}
\]
Write \(f_2=c_0(x)+yc_1(x)\pmod{y^2}\), licensed by
\(f_{2,z}=0\). The constant coefficient modulo \(y\) in (25) is
\(-2xc_0=2x^3\), so \(c_0=-x^2\). The coefficient of \(y\) is then
\[
                 -2xc_1+4x^2z=8x^2z,
 \qquad
                 c_1=-2xz,                              \tag{26}
\]
which is impossible because \(c_1\in\mathbb C[x]\).
Thus there is no divergence-free derivation satisfying (21), and in
particular no locally nilpotent derivation satisfying (21).

The proof places no degree bound on the \(x,y,z\)-coefficients in
(23). Its only degree restriction is the exact shift restriction
already imposed in (21). It does not exclude changing \(Dx\) or \(Dy\),
and does not exclude higher-shift repairs.

## 7. A separate obstruction to keeping both \(x\) and \(W\)

Use the original auxiliary polynomial from 615:
\[
             p=yu+z^2,\qquad W=x^2u-2xzp-yp^2.           \tag{27}
\]
There is no polynomial derivation \(D\), of any shift and without
assuming local nilpotence, such that
\[
                         Dx=DW=0,\qquad Dv=1.            \tag{28}
\]
Indeed, \(Dx=0\) makes \((x)\) stable. Pass to
\(B/(x)=\mathbb C[y,z,u]\), and write \(\overline D\) for the induced
derivation. Since \(v\equiv y\pmod x\), one has \(\overline Dy=1\).
Also \(W\equiv-yp^2\pmod x\), where the displayed \(p=yu+z^2\)
is unchanged. Consequently
\[
 0=\overline D(-yp^2)=-p\bigl(p+2y\overline Dp\bigr).    \tag{29}
\]
This quotient is a domain and \(p\ne0\), so the bracket vanishes.
Reducing it modulo \(y\) would give \(z^2=0\) in \(\mathbb C[z,u]\),
a contradiction. This argument concerns the specified original \(W\),
not every possible invariant of a completion.

The General affine agent supplied an independent derivation of this
short obstruction. The author separately checked the whole reduction
in (29). It is distinct from the fixed-\(Dx,Dy\) obstruction in Section 6.

## 8. Evidence and status

The root agent supplied the polynomial construction (15)--(16).
The author independently reconstructed its whole components, \(D_*v=1\),
exact shift, full initial action, nonzero divergence, and all-polynomial
syzygy obstruction. Fresh unsaved symbolic computations also checked
the entire generic coefficient ledger (6), its exact reductions
(8)--(9), the whole divergence and division-free identity (14), and
the reduction used in (29). The divisibility and impossibility proofs
are given above; they are not conclusions drawn from a finite grid.

No saved checker was executed, imported, or compiled. No canonical
file or prior source was edited. No human expert review, formal proof
assistant certification, or priority determination is claimed.
Author review and a future independent saved-source review remain
distinct gates.

The unrestricted shift-two completion problem for this specified \(v\)
remains UNRESOLVED. A separate stronger follow-up,
[619](venereau-x-fixed-shift-two-exclusion-pass619-working.md), addresses
all locally nilpotent lifts with \(Dx=0\), rather than fixing \(Dy\) as
in Section 6. At this note's author hold, 619 is a root-authored HELD
source pending independent saved-source review; it is not a dependency
of any proof here. The unrestricted case permits \(Dx\ne0\).

In particular, failure of the explicit lift and of
all repairs fixing its two chosen components is not failure of every
possible locally nilpotent lift. The original \(E=\partial_u\) already
has a known polynomial kernel; this example is a calibration of a
proposed reduction step, not a cancellation counterexample.
