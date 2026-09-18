# A uniform shift-three lower bound when the derivation fixes x

Date: 2026-09-17. Private working proof; novelty UNKNOWN.
General complex-threefold cancellation remains UNSOLVED.

## 1. Statement and scope

Let B=C[x,y,z,u], and for an integer n>=1 set

\[
v_n=y+x^n\bigl(xz+y(yu+z^2)\bigr).
\]

If D is a locally nilpotent derivation of B with

\[
D(v_n)=1,\qquad Dx=0,
\tag{1}
\]

then its exact u-degree shift satisfies

\[
\delta(D)=\max\{\deg_u Dx,\deg_u Dy,\deg_u Dz,\deg_u Du-1\}\ge3.
\tag{2}
\]

The degree of zero is minus infinity. This is conditional on the
existence of D and makes no coordinate-status assertion for v_1.
The additional hypothesis Dx=0 is essential to the scope of this
proof: it is not inferred for an arbitrary slice derivation.

For n>=3 the classical polynomial completions used in
[615](venereau-coordinate-positive-shift-obstruction-pass615-working.md)
and [617](venereau-coordinate-shift-one-exclusion-pass617-working.md)
fix x, and their coordinate partials have exact shift 10. Consequently
the minimum over x-fixed coordinate partials in this range lies
between 3 and 10. The unrestricted lower bound remains 2, not 3.
Neither minimum is determined here. The original partial_u is already
a translation, so this is not a cancellation counterexample.

## 2. Reduction to whole degree-two equations

The fully written filtration argument in617 proves delta>=2 without
assuming Dx=0. Suppose, for a contradiction, that delta=2 in (1).
The same argument gives a full initial LND eta^2 N on C[x,y,z,eta],
where Nx=Ny=0 and deg_u Du<=2. In particular

\[
Dy=B_0+uB_1,\quad Dz=C_0+uC_1+u^2g,\quad
Du=d_0+ud_1+u^2d_2.
\tag{3}
\]

Here all coefficients except g are in C[x,y,z], while
g is in C[x,y]. Indeed N=g partial_z is locally nilpotent;
after localizing C[x,y] to its fraction field, an LND on the
one-variable polynomial ring has constant coefficient. This forces
g to be independent of z. These are entire component expressions,
not truncated approximations.

Write

\[
A=1+x^n z^2,\qquad a=x+2yz.
\]

The coefficient of u in D(v_n)=1 is

\[
A B_1+x^n(2yB_0+aC_1+y^2d_1)=0.
\]

Since A and x are coprime, B_1=x^n Q for a polynomial Q.
The coefficient of u^2, after dividing by x^n, is
2yB_1+ag+y^2d_2=0. Modulo y it forces y to divide g.
Write g=yG with G in C[x,y]. The exact equations become

\[
A B_0+x^n a C_0+x^n y^2d_0=1,
\tag{4}
\]
\[
A Q+2yB_0+y^2d_1+aC_1=0,
\tag{5}
\]
\[
2x^n Q+yd_2+aG=0.
\tag{6}
\]

Every polynomial LND on B has zero divergence. To see this directly,
exp(tD) is a polynomial automorphism over C[t], with inverse exp(-tD).
Its Jacobian determinant is a unit in C[t,x,y,z,u], hence a nonzero
constant, and evaluation at t=0 makes it 1. Its linear t coefficient
is div(D). Using Dx=0 and g_z=0, the coefficient of u in this
zero-divergence identity is

\[
x^n Q_y+(C_1)_z+2d_2=0.
\tag{7}
\]

In particular the term (C_1)_z must be retained.

## 3. The first two y-coefficients give a contradiction

Use ordinary polynomial coefficients, without factorial normalization:

\[
Q=q_0+yq_1+y^2q_2+\cdots,\qquad
G=e_0+ye_1+y^2e_2+\cdots,
\]
\[
C_1=c_0+yc_1+\cdots,\qquad
d_2=t_0+yt_1+\cdots.
\tag{8}
\]

The q_i,c_i,t_i belong to C[x,z], and the e_i belong to C[x].
All coefficients used below are exact coefficients of the original
polynomials; no bound on their degrees in x or z is imposed.

First reduce (4) modulo y. With b=B_0(x,0,z), this gives

\[
(1+x^n z^2)b+x^{n+1}C_0(x,0,z)=1.
\]

Since 2n>=n+1, inversion modulo x^(n+1) yields a polynomial
F in C[x,z] such that

\[
b=1-x^n z^2+x^{n+1}F.
\tag{9}
\]

The constant y-coefficient of (6) gives
e_0=-2x^(n-1)q_0. Hence q_0 is independent of z.
The constant coefficient of (5), namely A q_0+x c_0=0,
then forces q_0=xh for h in C[x], and

\[
q_0=xh,\qquad e_0=-2x^n h,\qquad c_0=-Ah.
\tag{10}
\]

The coefficient of y in (6) and the constant coefficient in (7) are

\[
t_0=-2x^n q_1-xe_1-2ze_0,
\qquad x^n q_1+(c_0)_z+2t_0=0.
\tag{11}
\]

Substitute (10). The result is

\[
2xe_1=-3x^n(q_1-2zh).
\]

Because e_1 is independent of z, so is q_1-2zh. Thus for a
polynomial k in C[x],

\[
q_1=2zh+k,\qquad e_1=-\frac32 x^{n-1}k.
\tag{12}
\]

The coefficient of y in (5) reads
A q_1+2b+x c_1+2z c_0=0. Using (9), (10), and (12),

\[
x c_1=-Ak-2b
       =-k-2+x^n z^2(2-k)-2x^{n+1}F.
\]

Consequently k=-2+x ell for a polynomial ell in C[x], and

\[
c_1=-\mathrm{ell}+x^{n-1}z^2(4-x\mathrm{ell})-2x^nF.
\tag{13}
\]

Finally, the y^2 coefficient in (6) and the y coefficient in (7) give

\[
t_1=-2x^n q_2-xe_2-2ze_1,
\qquad 2x^n q_2+(c_1)_z+2t_1=0.
\tag{14}
\]

Eliminating t_1 and substituting (12)-(13) gives the undivided identity

\[
xe_2=-x^n q_2-2x^{n-1}z+2x^n\mathrm{ell}\,z-x^nF_z.
\tag{15}
\]

The left side has no z dependence. Differentiate (15) with respect
to z, cancel x^(n-1) in the polynomial domain, and obtain

\[
0=-x(q_2)_z-2+2x\mathrm{ell}-xF_{zz}.
\tag{16}
\]

Evaluation at x=0 says 0=-2, a contradiction. The undivided form
(15) handles n=1 without introducing any negative power of x.
This excludes shift two and proves (2) for all integers n>=1.

## 4. What the proof does and does not use

The contradiction actually applies to every divergence-free derivation
with Dx=0, D(v_n)=1, deg_u Dy<=1, deg_u Dz<=2, deg_u Du<=2,
and [u^2]Dz in C[x,y]. Local nilpotence was used to force these
degree and leading-coefficient conditions and zero divergence.

It does not exclude shift-two derivations whose full Dx is nonzero.
In that case the x-derivative contribution to D(v_n), as well as
the divergence term (Dx)_x, changes the displayed equations.
Divisibility of a leading coefficient of Dx is not divisibility of
the entire Dx and cannot be used to declare x invariant.

The argument was found while checking the failed shift-two lift
recorded in618. It supersedes that note's fixed-Dy obstruction within
the x-fixed branch, but does not replace its unrestricted necessary
conditions or settle the unrestricted shift-two question.

Root's fresh unsaved check71f054 reconstructs every displayed
y-coefficient relation and the final contradiction for n=1,...,9.
The symbolic exponent argument in Sections2-3, not those finite checks,
proves the uniform statement. No saved checker was executed, imported,
or compiled. Author EOF review and independent saved-source review are
separate gates. No human expert review, formal-assistant certification,
or public novelty claim has occurred.
