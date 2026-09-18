# The strict quadratic-sigma profile is excluded by parity

Working scoped exclusion: retain EVERY actual hypothesis of264 and
the nonlinear first-slope sector of458--461:
\[
k=s+f,\qquad f_s=0,\qquad n_{ss}\ne0,\qquad f'''\ne0.
\tag{1}
\]
Then the strict intrinsic degree profile
\[
\boxed{\deg\sigma=2,\qquad \deg y=\deg\theta=4}
\tag{2}
\]
cannot occur. The proof uses the entire reduced fourth relation and
its primitive tangent minor. It does not use465, impose rationality
on an exact coefficient field, or promote an intrinsic parameter to
an actual ambient coordinate.

## 1. Retained actual inputs and the complete strict relations

Retain the original globally sliced polynomial ring
\(B=\mathbb C[X,Y,Z,W]=A[u]\), \(E=\partial_u\), the exact E-degrees
\((1,2,2,2)\), and the ENTIRE weighted initial kernel
\(\mathsf X^2\mathsf Z-\mathsf Y^2\) from
[264](principal-one-affine-paraboloid-chart-pass264-working.md).
The literal selected nonzero N, its exact coefficient field L,
both original returns, coefficient localization, and full calibrated
scalar remain required. In particular the original slice is not
replaced by \(X/a_0\): one retains \(X=a_0u+x_0\), \(x_0\in A\).
The coefficient partials commute and have joint constants
\(\mathbb C\).

Use the exact intrinsic centering of
[458](principal-paraboloid-arbitrary-first-potential-birational-projection-pass458-working.md),
[460](principal-paraboloid-nonlinear-first-slope-tangent-degree-reduction-pass460-working.md)
and
[461](principal-paraboloid-strict-nonlinear-degree-ratio-pass461-working.md).
Write \(P=\sigma\), and let \(v_0\) be the polynomial-line parameter.
Under(2), their strict shear gives
\[
\begin{gathered}
O=L[v_0]=L[z,P,q],\qquad
\deg_{v_0}P=\deg_{v_0}z=2,\quad \deg_{v_0}q=4,\\
\mathcal H=z^2+2\eta zq+T(P)=0,\qquad
\eta\in L^*,\\
T\in L[P],\qquad \deg_PT=3,\qquad
t_3:=[P^3]T=f'''/6\ne0.
\end{gathered}
\tag{3}
\]
Here \(q=\theta+(n_{ts}P-\ell_s-(n_s)^2)/n_{ss}\),
\(z=x-\eta q\), and x is the centered first variable of460.
The equality \(\deg z=2\) follows from461(7),
\(\deg z+\deg q=3\deg P\), not from a guessed parametrization.
All moving-level terms remain in T.

The COMPLETE reduced fourth relation461(10) is
\[
\Psi=Cq^2+B(P)q+zT'(P)-\frac{D(P)}{2\eta}z^2+F(P)=0,
\tag{4}
\]
where
\[
C\in L,\quad \deg B\le2,\quad \deg F\le4,\qquad
D(P)=d_0+4\eta^2P,\quad d_0\in L.
\tag{5}
\]
The prime on T is the formal P-derivative. The symbol C denotes
one coefficient, not the field of complex numbers. These are the
exact coefficients of the genuine fourth potential after the
licensed shear and subtraction in461. They are not freely chosen
replacement equations.

The evaluated gradient minors of \(\mathcal H,\Psi\) generate O.
Whole generation makes \((z_{v_0},P_{v_0},q_{v_0})\) a primitive
polynomial tangent vector. The primitive tangent argument of461
therefore supplies \(\psi\in L^*\) with
\[
\begin{aligned}
W&:=\mathcal H_z\Psi_q-\mathcal H_q\Psi_z\\
 &=(2z+2\eta q)(2Cq+B)
       -2\eta z\{T'-Dz/\eta\}\\
 &=4Czq+4\eta Cq^2+2Bz+2\eta Bq
       -2\eta zT'+2Dz^2
 =-\psi P_{v_0}.
\end{aligned}
\tag{6}
\]
All expressions in(6) are evaluated on the polynomial line.
The derivative is the ordinary intrinsic derivative fixing L,
not the assertion \(Nv_0=1\). No term of F contributes to these
two formal partials, but F remains in the full relation(4).

## 2. Scalar extension and the even residual boundary

Extend L to an algebraic closure M. The whole-ring identity,
the equations, and the unit gradient-minor ideal extend to
\(M[v_0]\). It is enough to derive a contradiction there.
This is only a scalar extension of the intrinsic calculation.
No coefficient-field derivation or original ambient coordinate
is normalized by this step.

An affine change \(v=\alpha_0v_0+\beta_0\), \(\alpha_0\in M^*\),
centers and makes the quadratic P monic. Since z also has exact
degree two, write
\[
P=v^2+p_0,\qquad
z=\lambda P+kv+h,\qquad
\lambda\in M^*,\quad p_0,k,h\in M.
\tag{7}
\]
The chain rule in(6) gives
\[
W=-\widetilde\psi P_v=-2\widetilde\psi v,
\qquad \widetilde\psi=\alpha_0\psi\in M^*.
\tag{8}
\]
Thus the even part of W is zero. No statement about the speed
of the original N on v is made.

First suppose \(k=0\). Then \(z\in M[P]\setminus\{0\}\).
Equation(3) gives
\[
q=-\frac{z^2+T(P)}{2\eta z}
\tag{9}
\]
in the rational function field \(M(v)\). The right side is fixed
by \(v\mapsto-v\). Since q is already polynomial, it is even
and belongs to \(M[P]\). This field calculation does not declare
z to be a unit of the polynomial ring.
Whole generation would now give
\(M[v]=M[z,P,q]=M[P]\), impossible for \(\deg_vP=2\).
Consequently
\[
k\ne0.
\tag{10}
\]

## 3. An exact divisibility argument, including repeated roots

Put
\[
Z_0(P)=\lambda P+h,\quad
\overline z=Z_0(P)-kv,\quad
\mathcal N(P)=Z_0(P)^2-k^2(P-p_0).
\tag{11}
\]
Then \(z\overline z=\mathcal N(P(v))\), and
\(\deg_P\mathcal N=2\) with leading coefficient \(\lambda^2\).
Equation(3) says that z divides \(T(P(v))\) in \(M[v]\).
We claim this is exactly the condition
\(\mathcal N(P)\mid T(P)\) in \(M[P]\).

Indeed, in \(M[v]/(z)\), the identity
\[
v=-\frac{\lambda P+h}{k},\qquad P=v^2+p_0
\tag{12}
\]
shows that the quotient is generated by P and that
\(\mathcal N(P)=0\). Hence there is a surjection
\[
M[P]/(\mathcal N)\longrightarrow M[v]/(z).
\tag{13}
\]
Both sides have dimension two over M, so this is an isomorphism.
Its kernel description proves the claim. This argument uses
neither distinct roots nor a reduced quotient; a repeated root
of z or of \(\mathcal N\) is included.

It follows that
\[
T(P)=\mathcal N(P)L_1(P),\qquad
L_1(P)=\alpha P+\beta,\qquad
\alpha=t_3/\lambda^2\ne0.
\tag{14}
\]
Substitute(14) into(3). In the polynomial domain \(M[v]\),
\[
z\{z+2\eta q+\overline zL_1(P)\}=0.
\]
Cancel the nonzero polynomial z, without declaring it a unit.
This gives the complete expression
\[
q=-\frac{z+L_1\overline z}{2\eta}
  =-\frac{(L_1+1)Z_0}{2\eta}
       +v\,\frac{k(L_1-1)}{2\eta}.
\tag{15}
\]
No lower coefficient in(7) or(14) has been dropped.

## 4. The odd fourth relation and the even primitive minor

The decomposition
\[
M[v]=M[P]\oplus vM[P],\qquad v^2=P-p_0
\tag{16}
\]
defines the even and odd parts. Let
\[
\mathcal E(P)=
(L_1-1)\left\{B-\frac{C}{\eta}(L_1+1)Z_0\right\}
       +2\eta T'-2DZ_0.
\tag{17}
\]
Substitution of(7),(15) into the ENTIRE relation(4) gives
\[
\Psi_{\rm odd}=\frac{k}{2\eta}v\,\mathcal E(P).
\tag{18}
\]
For example the odd contributions before taking out this factor
are \(2C Q_0Q_1v+BQ_1v+kT'v-DZ_0kv/\eta\), where
\(Q_0=-(L_1+1)Z_0/(2\eta)\) and
\(Q_1=k(L_1-1)/(2\eta)\). The full F is even.
Since \(\Psi=0\), \(k\ne0\), and the ring is a domain,
\[
\mathcal E(P)=0.
\tag{19}
\]
The embedding \(M[P]\hookrightarrow M[v]\) justifies treating
this as a polynomial identity in P.

Independently, substitute the same expressions into the complete
original minor(6). Its even part is
\[
\begin{aligned}
W_{\rm even}={}&
\frac{C}{\eta}(L_1^2-1)
       \{Z_0^2+k^2(P-p_0)\}\\
 &+(1-L_1)BZ_0-2\eta Z_0T'
       +2D\{Z_0^2+k^2(P-p_0)\}.
\end{aligned}
\tag{20}
\]
Adding \(Z_0\mathcal E\) cancels every displayed \(Z_0\)-term:
\[
\boxed{
W_{\rm even}+Z_0\mathcal E
=k^2(P-p_0)
       \left\{\frac{C}{\eta}(L_1^2-1)+2D\right\}.}
\tag{21}
\]
These are exact identities, not just leading-coefficient equalities.

By(8),(19), the left side of(21) is zero. The polynomial
\(P-p_0\) is nonzero, including when \(p_0=0\), and \(k\ne0\).
Thus polynomial cancellation gives
\[
\frac{C}{\eta}\{(\alpha P+\beta)^2-1\}
       +2d_0+8\eta^2P=0.
\tag{22}
\]
Its \(P^2\)-coefficient is \(C\alpha^2/\eta\). Since
\(\alpha,\eta\ne0\), this forces \(C=0\).
The P-coefficient of(22) is then \(8\eta^2\ne0\), a contradiction.
This proves the exclusion(2).

## 5. Boundaries, evidence, and retained scope

The proof includes \(C=0\), every zero lower coefficient, a repeated
root of either quadratic in Section3, and \(p_0=0\).
It never divides by \(L_1-1\), \(L_1+1\), or v.
The rational-field division in(9) is used only to infer parity;
no evaluated nonconstant polynomial is declared invertible in the
polynomial ring. Divisibility and domain cancellation are
distinguished from polynomial invertibility throughout.

The complete held461 was freshly read through EOF in c94384 before
authoring. Its exact full relations and unit-minor input are used;
465 and the proposed general even-degree refinement are not inputs.
The earlier full-source audits of458,460,461 remain bounded audits,
not recursive certification of every historical dependency.

Fresh unsaved inline calculations1c638f and2bdab5 reconstructed
the whole third relation, the entire odd part(18), the entire
even-part identity(21), the quotient relation(12), and both final
coefficients in(22). Fresh8a6586 checked the norm identity both
modulo \(v^2-P+p_0\) and after direct substitution \(P=v^2+p_0\).
Root's separate fresh d15503 reconstruction checked the full H,
the odd fourth relation, and the original even minor identity with
arbitrary lower coefficients, as well as both final coefficients.
All asserted residuals were zero. The written two-dimensional
quotient argument supplies the repeated-root divisibility step;
the identities alone are not offered as that proof.

This note excludes only the strict intrinsic profile(2) under the
retained actual chart hypotheses. It gives no new coordinate return,
realization, or conclusion about other strict or balanced profiles.
No all-parameter collision assertion is needed here.
No saved checker was executed, imported, compiled, or rerun.
No earlier source or canonical file was edited. No historical novelty,
external expert review, or formal certification is claimed.
