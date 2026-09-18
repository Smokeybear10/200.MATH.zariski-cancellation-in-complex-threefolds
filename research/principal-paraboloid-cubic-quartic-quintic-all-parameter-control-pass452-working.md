# A degree-(3,4,5) control satisfying the entire all-parameter return

Working obstruction to one reduction strategy: the abstract quadric,
whole polynomial-line generation, the quadric gradient unit, and the
ENTIRE all-T return do not by themselves exclude the profile (3,4,5).
The explicit control below satisfies all four conditions, over every
extension of C and for every parameter T.

It is NOT an actual264 chart or a solution of the genuine fourth
potential. In fact the full resonant fourth support cannot vanish on
these polynomials: its first five coefficients force a subsequent
coefficient to be -80. Thus this control identifies a limitation of an
all-T-only argument, not a realization of the remaining actual profile.

## 1. Exact polynomial control and its whole-line inverse

In C[v], set
\[
\begin{aligned}
p&=2v^3-8v^2+4v+16,\\
x&=vp-5,\\
q&=-v^2p+10v,\qquad \zeta=q-p.
\end{aligned}
\tag{1}
\]
Then
\[
(\deg p,\deg x,\deg q)=(3,4,5),\qquad
x^2+pq=25,\qquad \deg\zeta=5,\quad \operatorname{lc}(\zeta)=-2.
\tag{2}
\]
The coefficient b of the abstract quadric is one, and zeta has the
resonant affine correction q-p. The evaluated quadric gradient is a
unit ideal:
\[
\frac{x}{50}(2x)+\frac{q}{25}p=1,\qquad
(2x,q,p)\,\mathbb C[v]=\mathbb C[v].
\tag{3}
\]
This is the single quadric-gradient unit, not the unit of minors with
a genuine fourth potential.

There is also an explicit polynomial inverse for the original triple.
Put w=x+5 and z=x-5, using these symbols only in this paragraph. Define
\[
A_0=\frac{8w^2-4wp-16p^2+p^3}{2000},\qquad
B_0=-\frac{z^2+30z+300}{1000}.
\tag{4}
\]
The identities
\[
vp=w,\qquad v(x-5)=-q,\qquad
2w^3-8w^2p+4wp^2+16p^3-p^4=0
\]
give
\[
\boxed{A_0p+B_0(x-5)=1,\qquad
v=A_0(x+5)-B_0q.}
\tag{5}
\]
For the unit identity, substitute w=z+10 in the cubic relation and
separate its constant 2000. Thus
\[
\mathbb C[p,x,q]=\mathbb C[v].
\tag{6}
\]
Every displayed identity remains valid after an arbitrary scalar
extension. No generic injectivity statement is substituted for(6).

## 2. The parameterized outputs and the exact pair factor

For T in any extension field of C, define
\[
A_T=x+Tp,\qquad B_T=\zeta,\qquad C_T=2px+Tp^2.
\tag{7}
\]
We prove
\[
\boxed{M[A_T,B_T,C_T]=M[v]
\quad\text{for every field extension }M/\mathbb C
\text{ and every }T\in M.}
\tag{8}
\]
The proof first treats an algebraically closed field Omega containing
M. It includes all distinct and repeated pairs, and will then descend
the polynomial-ring equality to M.

For independent u,v, write the polynomial divided difference
\[
p[u,v]=\frac{p(u)-p(v)}{u-v}
      =2(u^2+uv+v^2)-8(u+v)+4.
\tag{9}
\]
Define
\[
\mathcal F=x(u)+x(v),\qquad
\mathcal G=-\frac{\zeta(u)-\zeta(v)}{u-v}.
\]
The complete identity is
\[
\boxed{\mathcal G-\mathcal F=(uv+1)\,p[u,v].}
\tag{10}
\]
It follows directly from x(v)=vp(v)-5 and
-zeta(v)=(v^2+1)p(v)-10v. No denominator remains in(9),(10).
They therefore retain their derivative values on the diagonal.

With S=u+v and Pi=uv, the relevant exact symmetric formulas are
\[
\begin{aligned}
\mathcal F={}&2S^4-8S^3+4S^2+16S-10\\
             &-8\Pi S^2+24\Pi S-8\Pi+4\Pi^2,\\
\mathcal F\big|_{\Pi=-1}&=2(S-1)^4,\\
p[u,v]\big|_{\Pi=-1}&=2(S-1)(S-3).
\end{aligned}
\tag{11}
\]
In particular the candidate intersection on Pi=-1 is supported at
S=1, exactly where the p divided difference vanishes.

## 3. No distinct pair collides, for any T

Fix T in Omega, and suppose that all three outputs in(7) take equal
values at distinct u,v in Omega.

If p(u)=p(v), equality of A_T gives x(u)=x(v). Equality of zeta,
with zeta=q-p, then gives q(u)=q(v). The polynomial inverse(5) forces
u=v, a contradiction. This disposes of the exceptional equal-p
boundary without dividing by p(u)-p(v).

Now suppose p(u) is different from p(v). Equality of A_T gives
\[
x(u)-x(v)+T\{p(u)-p(v)\}=0.
\]
The exact difference of the third output is
\[
\begin{aligned}
C_T(u)-C_T(v)
={}&\{p(u)-p(v)\}\{x(u)+x(v)\}\\
 &+\{p(u)+p(v)\}
       \{x(u)-x(v)+T(p(u)-p(v))\}.
\end{aligned}
\tag{12}
\]
Its vanishing therefore forces F=0. Equality of zeta gives G=0.
Since p[u,v] is nonzero in this branch, (10) forces uv=-1.
Equation(11) then gives S=1, followed by p[u,v]=0, a contradiction.

Thus the map defined by(7) separates every pair of distinct Omega
points for every T. This includes exceptional parameter values;
no generic-T open set has been substituted for the assertion.

## 4. No common critical point, including p'=0

Suppose all three output derivatives vanish at a point w in Omega.
The prime in this section is the derivative of the polynomial
intrinsic variable, not an exact coefficient-field derivative.

If p'(w)=0, then
\[
A_T'(w)=x'(w)=p(w)+wp'(w)=p(w).
\]
Hence p(w)=0 as well. But
\[
\zeta'=-p'(v^2+1)-2vp+10
\tag{13}
\]
would give zeta'(w)=10, a contradiction.

If p'(w) is nonzero, the first derivative equation is
x'(w)+Tp'(w)=0. The third derivative is
\[
C_T'(w)=2p'(w)x(w)+2p(w)\{x'(w)+Tp'(w)\}.
\tag{14}
\]
It forces x(w)=0. Also zeta'(w)=0. Apply(10) on the diagonal u=v=w:
F=2x(w)=0 and G=-zeta'(w)=0, so
(w^2+1)p'(w)=0. Consequently w^2=-1.

Now Pi=-1 and S=2w in(11). Its first equation gives S=1; the last
one gives p'(w)=0, contradicting the branch assumption. Thus at each
point at least one output derivative is nonzero, for every T.

## 5. Why finite, injective and immersed gives the WHOLE polynomial ring

For completeness, use the following elementary ring lemma. Let Omega
be algebraically closed and let
\[
R=\Omega[f_1,\ldots,f_m]\subseteq B=\Omega[v].
\]
Assume B is finite over R, the tuple f_i separates distinct Omega
points, and for every a in Omega some f_i'(a) is nonzero. Then R=B.
The proof makes no assumption that R is normal or already has the same
fraction field as B.

Fix a maximal ideal m of R. Since B is integral over R, it has a
maximal ideal above m. The tuple's injectivity gives exactly one
such ideal, (v-a), for some a in Omega. Indeed the residue field of
the finitely generated Omega-algebra R at m is Omega, and two
points above m would have the same tuple values.

Put A=R_m and B_m=(Omega[v])_m. This latter ring is local with its
unique maximal ideal induced by (v-a), and
\[
B_m=\Omega[v]_{(v-a)}.
\tag{15}
\]
For example, every polynomial not vanishing at a lies outside its
unique maximal ideal and is therefore already invertible in B_m.
This proves the equality of these localizations.

Choose i with f_i'(a) nonzero and set r=f_i-f_i(a) in mA. In B_m,
r is (v-a) times a unit, so B_m/rB_m=Omega. Constants in A surject
onto this quotient. Therefore
\[
B_m=A+rB_m.
\tag{16}
\]
The A-module B_m/A is finite, and(16) says it equals r times itself.
Since r lies in the maximal ideal of the local ring A, Nakayama's
lemma makes this quotient zero. This is exactly the finite-module
form of
[Stacks, Lemma10.20.1(2)](https://stacks.math.columbia.edu/tag/00DV);
no normalization theorem is invoked. Hence B_m=A for every m.
The finite R-module B/R is zero after localization at every maximal
ideal and is therefore zero. This proves the lemma.

Apply it to
\[
R_T=\Omega[A_T,\zeta,C_T].
\]
The polynomial zeta has degree five and leading coefficient -2.
Its monic equation for v, with zeta as a coefficient in R_T,
shows that Omega[v] is a finite R_T-module. Sections3--4 supply
the lemma's point and derivative hypotheses. Thus
\[
\Omega[A_T,\zeta,C_T]=\Omega[v]
\quad\text{for every }T\in\Omega.
\tag{17}
\]

Finally start with any M/C and any T in M, and take an algebraic
closure Omega of M. Scalar extension of the subring
M[A_T,zeta,C_T] gives exactly the ring on the left of(17).
The quotient of M[v] by this subring, considered as an M-vector
space, becomes zero after tensoring with Omega. A field extension
is faithfully flat, so the quotient was already zero. This proves
the full all-extension, all-parameter assertion(8).

## 6. Explicit failure of the genuine resonant fourth potential

The abstract data above do NOT satisfy the full actual chart.
Here is an algebraic failure before any attempt at original-coordinate
construction or calibrated coefficient differentiation.

In the actual resonant (3,4,5) branch, the exact support of441 and
the coefficient comparison in442, Section5, force
delta=epsilon=F2=0. With b=1 the FULL fourth level would have to be
\[
\Phi=xq+u_1px+\kappa p^3+c_{20}p^2+c_{11}pq
          +c_{10}p+c_{01}q+c_{00},
\tag{18}
\]
vanishing on the polynomial line. The displayed coefficients may be
arbitrary elements of any extension field of C for this test. No
numerical or rational ansatz for the actual coefficient field is used.

Substitution of(1) gives the following six exact coefficients:
\[
\begin{array}{c|l}
v^9&4(2\kappa-1)\\
v^8&-4(c_{11}+24\kappa-8)\\
v^7&4(8c_{11}+108\kappa+u_1-20)\\
v^6&-4(20c_{11}-c_{20}+176\kappa+8u_1)\\
v^5&2(-c_{01}-16c_{20}-336\kappa+40u_1+135)\\
v^4&4(2c_{01}+65c_{11}+20c_{20}+864\kappa-62).
\end{array}
\tag{19}
\]
The first five zero equations uniquely force
\[
\kappa=\tfrac12,\qquad c_{11}=-4,\qquad
u_1=-2,\qquad c_{20}=-8,\qquad c_{01}=15.
\tag{20}
\]
The v^4 coefficient then equals -80, not zero. The remaining
coefficients c10,c00 have lower intrinsic degree and cannot alter it.
Thus no polynomial of the genuine required support(18) vanishes.
In particular no choice of a moving third level or fourth scalar
level repairs this failed control.

## 7. Scope and evidence

This is a formal polynomial-line control satisfying the quadric,
whole generation, its single gradient unit, and every all-T ring
equality. It is not a four-variable globally sliced example,
does not supply the exact coefficient-field derivative constraints
or the calibrated original scalar, and fails the genuine resonant
fourth potential explicitly by(19),(20). It therefore cannot be used
as evidence that an actual (3,4,5) chart exists.

Conversely, an argument using only the four verified abstract
properties cannot exclude that profile. Further work must use
additional actual structure, such as the full genuine potential
or the original calibrated scalar. No tentative normal-form
classification of arbitrary degree-(3,4,5) curves is asserted here.

Fresh unsaved99f029 checked the quadric, both identities(5),
the full factor(10), the complete symmetric formulas(11), and
the derivative identities(13),(14), with zero residuals.
Fresh59c5a3 independently reconstructed all coefficients of(18),
including the six written in(19). The generation lemma is the
local finite-module argument above, not a symbolic-rank or
finite-sampling claim. Stacks00DV was read directly for the exact
Nakayama input. The writing guide was read before authoring.

No saved checker was executed, imported, compiled or rerun.
No earlier proof source or canonical ledger was edited. No
actual realization, remaining-profile recognition, unrestricted
cancellation, historical novelty, expert review or formal
certification is claimed.
