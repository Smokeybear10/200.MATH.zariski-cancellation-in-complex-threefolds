# Excluding the nonresonant quadratic profile by its genuine cubic cofactor

Working result: under the entire supplied actual264 chart and the moving
transverse-slope assumptions of438, the nonresonant normalized-quadric
profile (deg p,deg x,deg q)=(2,2,2) is impossible. The complete genuine
fourth equation has a forced cubic part. Its cofactor along the intrinsic
line has degree four, contrary to the evaluated gradient-minor unit ideal.

This is a bounded profile exclusion. All changes below are over the exact
coefficient field and are used only on the intrinsic polynomial line. No
coefficient-field coordinate is promoted to an original complex coordinate,
and no recognition claim for the remaining profiles is made.

## 1. Actual hypotheses and the complete fourth equation

Retain every hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
[438](principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md)
and
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md).
In particular, the actual polynomial four-ring is
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the full initial kernel},\\
N=[u^4]\partial_Z|_A\ne0,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
O=L[A]=L[v]=L[y,\sigma,\theta],\quad Nv=1,\quad
\operatorname{Frac}A=L(v)=\mathbb C(y,z,w).
\end{gathered}
\tag{1}
\]
The original nonzero calibrated scalar and all actual return statements
remain hypotheses. Put F=ker_L(partial_s), an exact finite extension of
C(t), not assumed rational. The coefficient partials commute and have
joint constants C. Assume
\[
k=s+f,\qquad n=\nu s+n_0,\qquad f,\nu,n_0\in F,\qquad
b=\nu'\ne0,\qquad \alpha=\frac{f'''}3-2b\ne0.
\tag{2}
\]
Thus this note is outside the resonance f'''=6b.

Use the entire third and fourth polynomials H,Q of438, with their actual
moving levels h,q0 in L. In particular neither h_t nor h_s is discarded.
For precision, the polynomial change of441 is defined by
\[
\begin{gathered}
a=f''-2\nu,\quad c=n_t-\nu f',\quad E_0=\ell_s+\nu^2,\\
R_3(P)=\frac{f'''}6P^3+
 \left(\frac{n_{tt}-\nu f''}{2}-\frac{a^2}{4}\right)P^2
 +\left(-\nu n_t-\ell_t-\frac{ac}{2}\right)P
 +\nu\ell-h-\frac{c^2}{4},\\
R_3(P)=(bP-E_0)T_2(P)+\rho,\qquad d=-\rho,\\
p=P-E_0/b,\qquad x=U+(aP+c)/2,\qquad q=V+T_2(P).
\end{gathered}
\tag{3}
\]
Here division defines T2 and rho in L[P] before evaluation; it does not
invert b*sigma-E0 on the line. The inverse is
P=p+E0/b, U=x-(aP+c)/2, V=q-T2(P), and its polynomial Jacobian is
invertible. Reuse x,p,q for their evaluated elements of O. Then
\[
\mathcal H=x^2+bpq-d=0,\qquad O=L[x,p,q].
\tag{4}
\]
Let tau be substitution by that inverse. The fourth polynomial used here
is exactly
\[
\Phi=\tau\bigl(Q-q_0-f''(H-h)/2\bigr),
\tag{5}
\]
not a freely chosen equation of the line. Its complete support is
\[
\begin{aligned}
\Phi={}&\delta p^4+\alpha p^2x+\kappa p^3+\epsilon p^2q
       +bxq+u_1px-\frac{\ell_{ss}}2q^2\\
&+c_{20}p^2+c_{11}pq+c_{10}p+c_{01}q+c_{00},\\
\delta&=\frac{3b^2f''''-6bb'f'''-\ell_{ss}(f''')^2}{72b^2},
\qquad \epsilon=\frac{b'}2+\frac{\ell_{ss}f'''}{6b}.
\end{aligned}
\tag{6}
\]
Every coefficient not expanded in(6) is the exact coefficient defined
by(3),(5), with the full Q of438. In particular there is no omitted
lower polynomial or replacement of Phi by an auxiliary cubic.

The evaluated two-by-two gradient minors of mathcal H and Phi generate O.
Indeed subtracting f''(H-h)/2 from Q-q0 preserves the gradient wedge
over L. The polynomial change(3) acts on it by the second exterior power
of an invertible polynomial Jacobian, preserving its component ideal.
This is the actual scalar consequence supplied by438 and441.

Suppose for contradiction that
\[
\deg_vp=\deg_vx=\deg_vq=2.
\tag{7}
\]

## 2. The exact affine plane and its polynomial line

Define the nonzero leading ratio and the linear quadric shear
\[
\lambda=\frac{[v^2]x}{[v^2]p}\in L^*,\qquad
r=x-\lambda p,\qquad
q_1=q+\frac{2\lambda}{b}x-\frac{\lambda^2}{b}p.
\tag{8}
\]
The degree-four coefficient of(4) gives
[v^2]q=-lambda^2[v^2]p/b. Thus both r and q1 have intrinsic degree at
most one, with zero allowed. The shear is invertible over L, and
\[
r^2+bpq_1=d,\qquad O=L[r,p,q_1].
\tag{9}
\]
If q1 were nonconstant, its degree would be one and bpq1 would have
degree three, whereas r^2 has degree at most two. Hence q1 is constant.
If q1=0, then r^2=d forces r in L. The whole return in(9) would give
O=L[p], impossible for a polynomial p of degree two in v. Therefore
\[
q_1=q_c\in L^*,\qquad \deg_vr=1,\qquad
p=\frac{d-r^2}{bq_c},\qquad O=L[r].
\tag{10}
\]
The degree assertion for r follows directly from(9) with q_c nonzero.
No nonzero assumption on d has been made.

Set the formal affine linear polynomial
\[
G=q+\frac{2\lambda}{b}x-\frac{\lambda^2}{b}p-q_c.
\tag{11}
\]
The ordered coordinates (r,p,G) form an affine L-coordinate system on
L[x,p,q]. Their inverse is
\[
x=r+\lambda p,\qquad
q=G+q_c-\frac{2\lambda}{b}r-\frac{\lambda^2}{b}p,
\qquad \mathcal H=r^2+bp(G+q_c)-d.
\tag{12}
\]
Modulo G, the remaining equation is
H0=r^2+bq_c*p-d. Since bq_c is a nonzero field element, its quotient is
exactly L[r], with p=(d-r^2)/(bq_c). Together with(10), this proves the
complete evaluation kernel
\[
\ker\bigl(L[x,p,q]\longrightarrow O\bigr)=(\mathcal H,G).
\tag{13}
\]
There is no localization or saturation in(13). It holds also at d=0.

## 3. The forced cubic part of the genuine fourth polynomial

The p^4 term of(6) has intrinsic degree eight and all other terms have
degree at most six. Consequently delta=0. Write(6) in the coordinates
(r,p,G), then restrict to G=0. Its degree-three part before evaluation
is
\[
\left(\kappa+\alpha\lambda-\frac{\epsilon\lambda^2}{b}\right)p^3
 +\left(\alpha-\frac{2\epsilon\lambda}{b}\right)p^2r.
\tag{14}
\]
All remaining terms have total degree at most two in r,p: the constant
q_c contributes epsilon*q_c*p^2 and the lower terms in(6) remain
quadratic. Since p in(10) is an even quadratic in r, the first displayed
term has degree six, the second degree five, and all remaining terms
degree at most four. The two coefficients must therefore vanish:
\[
\alpha=\frac{2\epsilon\lambda}{b},\qquad
\kappa=-\frac{\epsilon\lambda^2}{b},\qquad \epsilon\ne0.
\tag{15}
\]
The last gate follows from alpha nonzero, b nonzero and lambda nonzero.

For explicit coefficient verification, direct substitution of(10),(12)
in the original polynomial(6) gives
\[
\begin{aligned}
[r^8]\Phi_{\rm ev}&=\frac{\delta}{b^4q_c^4},\\
[r^6]\Phi_{\rm ev}\big|_{\delta=0}
 &=-\frac{\alpha b\lambda+b\kappa-\epsilon\lambda^2}{b^4q_c^3},\\
[r^5]\Phi_{\rm ev}\big|_{\delta=0}
 &=\frac{\alpha b-2\epsilon\lambda}{b^3q_c^2}.
\end{aligned}
\tag{16}
\]
These are coefficients of the complete genuine polynomial, not just
its highest homogeneous form.

Using(15), the exact cubic part combines as
epsilon*p^2*(q+2lambda*x/b-lambda^2*p/b). Thus the entire Phi has the
identity
\[
\begin{aligned}
\Phi&=\epsilon p^2G+Q_2,\\
Q_2&=bxq+u_1px-\frac{\ell_{ss}}2q^2
 +(c_{20}+\epsilon q_c)p^2+c_{11}pq+c_{10}p+c_{01}q+c_{00}.
\end{aligned}
\tag{17}
\]
In particular Q2 has total degree at most two and vanishes on the line.

## 4. The complete quadratic relation space

Reduce Q2 modulo the affine linear polynomial G, using(12). Its
remainder is a polynomial of degree at most two in r,p, vanishing on
H0=r^2+bq_c*p-d. The evaluation kernel in L[r,p] is precisely (H0),
because H0 solves for p over L. Hence that remainder is a multiple of
H0. Total degrees in the polynomial domain add under multiplication,
so a polynomial of degree at most two can only be a constant multiple
of the nonzero degree-two polynomial H0. Therefore
\[
Q_2=A_0\mathcal H+G L_1,
\qquad A_0\in L,\qquad \deg L_1\le1.
\tag{18}
\]
To see the last degree bound directly, Q2-A0*mathcal H has degree at
most two and is divisible by the degree-one polynomial G; its quotient
has degree at most one. This also covers a zero remainder or quotient.

Combining(17),(18) gives a full polynomial identity, including every
lower coefficient:
\[
\boxed{\Phi=A_0\mathcal H+G\bigl(\epsilon p^2+L_1\bigr).}
\tag{19}
\]
Neither a complete-intersection normality assumption nor a field-only
kernel argument is used. The exact polynomial quotient in(13) supplied
the relation space.

## 5. The cofactor cannot be a unit

Take formal gradients of(19) over L and evaluate in O. Both G and
mathcal H vanish, so
\[
(\nabla\mathcal H\wedge\nabla\Phi)_{\rm ev}
 =\bigl(\epsilon p^2+(L_1)_{\rm ev}\bigr)
    (\nabla\mathcal H\wedge\nabla G)_{\rm ev}.
\tag{20}
\]
The left-hand components generate O by the full actual minor condition.
They all lie in the principal ideal of the displayed cofactor. That
cofactor must consequently be a unit of O=L[r], hence an element of L*.

But each of p,x,q has degree two in r, and L1 is affine linear in these
formal variables. Therefore deg_r(L1)_ev<=2. By(10),(15),
\[
\deg_r\bigl(\epsilon p^2+(L_1)_{\rm ev}\bigr)=4,
\qquad
[r^4]\bigl(\epsilon p^2+(L_1)_{\rm ev}\bigr)
   =\frac{\epsilon}{b^2q_c^2}\ne0.
\tag{21}
\]
This contradicts its being a unit. The nonresonant (2,2,2) profile is
excluded.

## 6. Verification and exact scope

The complete current438 and441 sources were read through EOF before
this note, as was the writing guide. Fresh unsaved calculation5c3e0a
reconstructed the affine shear and full quadric, all three coefficients
in(16), the complete quadratic remainder(17), every evaluated gradient
minor in(20), and the nonzero leading cofactor in(21). The identity
residuals were zero. The complete ideal and quadratic relation-space
arguments are proved in writing above; they are not inferred from
symbolic sampling.

The zero centered level d=0 is retained. The excluded q1=0 alternative
was treated before dividing by q_c. The proof only divides by b, lambda
and q_c after their nonvanishing is established. It does not assume
resonance, use the resonant scalar or constants of448, assume F=C(t),
or identify a coefficient-field map with an original coordinate change.

The conclusion concerns only this supplied actual chart and this
nonresonant quadratic profile. It does not exclude the nonresonant
affine profile or any unequal-degree profile. The actual hypotheses
and genuine gradient-minor input of438/441 remain inherited; this is
not a recursive certification of their entire dependency history.

No saved checker was executed, imported, compiled or rerun. No earlier
source or canonical index was edited. No unrestricted cancellation,
arbitrary-entry, realization, novelty or formal-certification claim
is made.
