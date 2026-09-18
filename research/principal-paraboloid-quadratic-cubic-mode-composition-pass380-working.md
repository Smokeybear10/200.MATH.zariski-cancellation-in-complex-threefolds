# Explicit coefficient families and a rank-one quadratic part

Working necessary reduction: combining the genuine lower-potential
gate377 with the literal scalar gate378 leaves explicit complex
rational formulas for H,g,f,G0. Except for the zero-slope overlap,
only the first lower-potential mode survives. In every case the binary
quadratic part of sigma in the coefficient-adjoined variables s,r has
rank one.

This is a composition of necessary conditions, not exclusion of all
remaining cases, sufficiency, or original-ring recognition. The exact
finite coefficient field F is not identified with C(t).

## 1. Retained actual entry and the two independently derived gates

Retain every actual hypothesis and exact-field identity of
[376](principal-paraboloid-quadratic-cubic-nonzero-leading-normal-form-pass376-working.md),
including its actual264/365/369/372 entry, original global slice,
full initial kernel, literal selected partial, both field returns,
and nonzero calibrated scalar. In particular
\[
\begin{gathered}
F=\ker_L\partial_s,\quad [F:\mathbb C(t)]<\infty,
\quad L=F(s),\quad K=F(s,r)=\mathbb C(y,z,w),\\
g=f''/2\in F^*,\quad E=g'/3+g/t\in F^*,\quad
H\in F^*,\quad E=d t^3H^4,\quad d\in\mathbb C^*,\\
\sigma=A r^2+(\beta s+\beta_0)r+e_2s^2+e_1s+e_0,
\quad A\ne0,\quad A,\beta,\beta_0,e_i\in F.
\end{gathered}
\tag{1}
\]
The exact t-derivative on F has constants C. Primes mean this
derivative. The coefficient E is not the original slice derivation.
None of t,s,r is being newly declared an original polynomial coordinate.

The explicit high-gate coefficients include
\[
A=-\frac{4E}{g^2H},\qquad
\beta=-\frac{2tH'+4H}{t^2gH},\qquad
\beta_0=-\frac{2G_0'}{tgH}.
\tag{2}
\]
The independently scoped conclusions of
[377](principal-paraboloid-quadratic-cubic-lower-potential-two-mode-gate-pass377-working.md)
and
[378](principal-paraboloid-quadratic-cubic-sixth-scalar-gate-pass378-working.md)
are respectively
\[
8te_2=H\beta\quad\text{or}\quad16te_2=H\beta,
\tag{3}
\]
and
\[
\begin{gathered}
C_0=c_1+c_2t,\qquad c_1,c_2\in\mathbb C,
\qquad(c_1,c_2)\ne(0,0),\\
H=\frac1{tC_0},\qquad E=\frac{d}{tC_0^4},\qquad
G_0=\frac{u_1t+u_0}{C_0},\quad u_0,u_1\in\mathbb C.
\end{gathered}
\tag{4}
\]
Here C0 is not the coefficient C=ell_s+s^2/(4t^4) in the literal
third-potential parametrization. It is a nonzero element of F,
even if it vanishes at an individual curve point.

## 2. Comparing the dimensionless differential equations

Let D=t partial_t and use377's coefficient functions
\[
\zeta=t\frac{H'}H+2,\qquad \omega=\frac{tE}{g}\ne0.
\tag{5}
\]
That note derives, without dividing by zeta, the two necessary systems
\[
\begin{aligned}
D\zeta&=\zeta(2\omega-\zeta-1)
    &&\text{in the first mode of (3)},\\
D\zeta&=\zeta(3\omega-\zeta-1)
    &&\text{in the second mode of (3)},\\
D\omega&=\omega(4\zeta-1-3\omega)
    &&\text{in both modes}.
\end{aligned}
\tag{6}
\]
Meanwhile (4) gives directly
\[
\zeta=\frac{c_1}{C_0},\qquad
D\zeta=\zeta(\zeta-1).
\tag{7}
\]

First suppose c1 is nonzero. Then zeta is nonzero in F. Comparing
the first equation of (6) with (7) gives omega=zeta. Comparing the
second instead gives omega=2zeta/3. In the latter case the
derivative of this proposed identity would require
\[
\frac23\zeta(\zeta-1)
=\frac23\zeta(2\zeta-1),
\tag{8}
\]
using the third equation of (6). This forces zeta=0, a contradiction.
Thus in this case only the first mode survives, and
\[
\boxed{\omega=\zeta,\qquad 8te_2=H\beta
\qquad(c_1\ne0).}
\tag{9}
\]
No assumption c2 nonzero was made in this comparison.

If c1=0, then c2 is nonzero, zeta=0 and beta=0 by (2),(5).
Either mode of (3) forces e2=0. This is their retained overlap:
\[
\boxed{\beta=e_2=0\qquad(c_1=0).}
\tag{10}
\]
It has not been discarded by dividing by beta or zeta.

## 3. The three explicit coefficient families

For c1 nonzero, (4),(5),(9) give immediately
\[
g=\frac{tE}{\zeta}=\frac{d}{c_1 C_0^3}.
\tag{11}
\]
If c2 is also nonzero, integration of f''=2g in the exact field F
therefore gives
\[
\boxed{
H=\frac1{t(c_1+c_2t)},\quad
g=\frac{d}{c_1(c_1+c_2t)^3},\quad
f=\frac{d}{c_1c_2^2(c_1+c_2t)}+f_1t+f_0,
\quad f_1,f_0\in\mathbb C.
}
\tag{12}
\]
If c2=0, then c1 is nonzero and instead
\[
\boxed{
H=\frac1{c_1t},\quad g=\frac{d}{c_1^4},\quad
f=\frac{d}{c_1^4}t^2+f_1t+f_0,
\quad f_1,f_0\in\mathbb C.
}
\tag{13}
\]
Both displayed primitives have the required second derivative.
Subtracting them from f leaves an element with zero second derivative
in F, hence a complex affine function of t. This is exact integration,
not a rational-function ansatz.

Finally suppose c1=0 and c2 nonzero. Set Delta=d/c2^4 in C*.
Equation E=g'/3+g/t in (1),(4) becomes
(t^3 g)'=3Delta/t^2. Exact integration gives
\[
\boxed{
H=\frac1{c_2t^2},\quad E=\frac{\Delta}{t^5},\quad
g=\frac{v_0}{t^3}-\frac{3\Delta}{t^4},\quad
f=\frac{v_0}{t}-\frac{\Delta}{t^2}+f_1t+f_0,
\qquad v_0,f_1,f_0\in\mathbb C.
}
\tag{14}
\]
The value v0=0 is included. Since Delta is nonzero, the displayed g
is not identically zero for any value of v0. All three families retain
the uniform G0 formula in (4), including constant G0. Equivalently
\[
G_0'=\lambda t^2H^2,\qquad
\lambda=u_1c_1-u_0c_2\in\mathbb C.
\tag{15}
\]
No division by lambda has been made.

## 4. Rank one over the exact coefficient field

For c1 nonzero, (2),(5),(9) give
\[
A=-\frac{4\zeta}{tgH},\qquad
\beta=-\frac{2\zeta}{t^2g},\qquad
e_2=-\frac{H\zeta}{4t^3g}.
\tag{16}
\]
These directly imply beta^2=4A e2. If c1=0, the same equality
follows from beta=e2=0 in (10). Consequently in every case
\[
\boxed{\beta^2-4Ae_2=0.}
\tag{17}
\]
Because A is nonzero, the binary quadratic part of sigma is precisely
\[
A r^2+\beta rs+e_2s^2
=A\left(r+\frac{\beta}{2A}s\right)^2,
\tag{18}
\]
of rank one over F. This requires no square root of A, and its
linear change is only over the adjoined coefficient field.
It is not a rank claim about an original-coordinate quadratic form.

The complete square, useful for a later polynomial-return analysis,
is the identity
\[
\sigma=Aq^2+\left(e_1-\frac{\beta\beta_0}{2A}\right)s
                 +e_0-\frac{\beta_0^2}{4A},\qquad
q=r+\frac{\beta s+\beta_0}{2A}.
\tag{19}
\]
Here F[s,q]=F[s,r], but q is not asserted to lie in or generate
an original polynomial coordinate ring before adjoining F.

## 5. Scope and evidence

These explicit families and the rank-one identity are necessary
consequences of377 and378 under their shared complete actual376
entry. The one-variable function l and the remaining lower-potential
and scalar equations are not solved by this composition. In
particular f,H,G0 in C(t) does not force F=C(t). The finite field
extension and the original-coordinate conditions must still be kept.

The complete final377 and378 sources were read through EOF in213f28.
The complete379 polynomial-return proof was read in8a94fd but is
not needed for this composition. Fresh unsaved165dc9 independently
verified both dimensionless mode substitutions, the rank-one identity
in the nonzero-slope case, the reciprocal H differential equation,
and both nonconstant-family g and f primitives. The c2=0 primitive
in (13) is checked directly by two differentiations. The zero-slope,
constant-G0 and v0=0 boundaries are retained in the written argument.

No saved checker was executed, imported, compiled or rerun. No
earlier source or canonical index was edited. No realization,
original-ring recognition, unrestricted cancellation, novelty,
human-expert review or proof-assistant certification is claimed.
