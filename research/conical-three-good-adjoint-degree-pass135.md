# Conical three-good speeds lower the selected adjoint degree

In a sliced polynomial fourfold, rank-two good speeds whose homogeneous
cone is not dense force the remaining coordinate partial to have adjoint
degree at most one. The conclusion includes its coefficient on the chosen
slice. No bound on the time degree of the remaining coordinate is needed.

This is a degree reduction inside a supplied actual coordinate frame,
not recognition of the entire conical class or a coordinate-entry theorem.

## 1. Actual hypotheses and conclusion

Assume
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2x_i=0,\qquad a_i=Ex_i,\qquad x_i=b_i+a_i u,\quad a_i,b_i\in A,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)=2,\\
P(a_1,a_2,a_3)=0
\quad\text{for some nonzero homogeneous }
P\in\mathbb C[T_1,T_2,T_3].
\end{gathered}
\tag{1}
\]
The four original generators are actual polynomial coordinates. The
global slice \(u\) is not assumed to be one of them or to be an ambient
coordinate. Set \(T=\partial_z\), holding the three goods fixed, and
use the convention \([E,T]=ET-TE\).

Then
\[
(\operatorname{ad}_E)^2T=0,\qquad
T(A)\subset A[u]_{\le1},\qquad T(u)\in A[u]_{\le1}.
\tag{2}
\]
More precisely the exact adjoint degree is \(d\in\{0,1\}\), and
\(T(A)\) has exact maximal \(u\)-degree \(d\), while
\(\deg_u T(u)\le d\). Thus when \(d=0\), even a linear term in
\(T(u)\) is excluded.

This complements the dense-cone conclusion of132, where the exact
degree is two.[^1] The proof reconstructs the cofactors and the
actual leading-LND step needed for the conical boundary.

## 2. The differential frame and invariant volume

Put \(F=\operatorname{Frac}A\). Choose two algebraically independent
speeds \(s,t\) and \(v\in A\) completing them to a transcendence basis
of \(F/\mathbb C\). Since \(A\simeq B/uB\) is finitely generated,
\(F/\mathbb C(s,t,v)\) is finite and separable. The three coordinate
partials extend uniquely through that extension. Every \(a_i\) is
algebraic over \(\mathbb C(s,t)\), so \((a_i)_v=0\).

The homogeneous relation in (1) makes the three functions
\(\eta a_i\), with \(\eta\) independent of \(F\), algebraically
dependent. In characteristic zero their differential wedge vanishes.
Writing \(a=(a_i)^T\), this gives
\[
d(\eta a_1)\wedge d(\eta a_2)\wedge d(\eta a_3)
=\eta^2\Delta\,ds\wedge dt\wedge d\eta=0,\qquad
\Delta=\det[a_s,a_t,a]=0.
\tag{3}
\]
Conversely, at rank two the same differential criterion makes (3)
equivalent to a nonzero homogeneous relation. No parametrization or
polynomial coordinates for the speed image are required.

Let \(\omega=dx_1\wedge dx_2\wedge dx_3\wedge dz\).
The differentials \(ds,dt,dv,du\) form a basis over \(F(u)\).
All original generators belong to \(A[u]\), so
\(\omega=J\,ds\wedge dt\wedge dv\wedge du\), with \(0\ne J\in F[u]\).
The actual flow \(\exp(\lambda E)\) is a polynomial automorphism
over \(\mathbb C[\lambda]\). Its original-coordinate Jacobian is
a unit of \(B[\lambda]\), hence a complex constant; evaluation at
\(\lambda=0\) makes it one. The flow fixes \(F\) and sends \(u\)
to \(u+\lambda\). Taking differentials over \(\mathbb C(\lambda)\)
therefore gives \(J(u+\lambda)=J(u)\). Consequently \(J=J_0\in F^*\).
It need not be a complex constant.

The first three rows of the full Jacobian, with columns ordered
\((s,t,v,u)\), are
\([b_s+u a_s,\ b_t+u a_t,\ b_v,\ a]\).
The equations \(Tx_i=0,Tz=1\) and the signed cofactors give
\[
\begin{aligned}
T(s)&=-\det[b_t+u a_t,b_v,a]/J_0,\\
T(t)&=\det[b_s+u a_s,b_v,a]/J_0,\\
T(v)&=-\det[b_s+u a_s,b_t+u a_t,a]/J_0,\\
T(u)&=\det[b_s+u a_s,b_t+u a_t,b_v]/J_0.
\end{aligned}
\tag{4}
\]
The only quadratic coefficient in \(T(v)\) is \(-\Delta/J_0\),
which is zero. Hence \(T(s),T(t),T(v)\) all have degree at most
one. For every \(f\in F\),
\(T(f)=f_sT(s)+f_tT(t)+f_vT(v)\): the difference of the two
derivations kills the separating base field, so separable algebraicity
kills it on \(F\). Thus \(T(F)\subset F[u]_{\le1}\).

For \(f\in A\), its actual image also belongs to \(B=A[u]\).
Uniqueness of coefficients in \(F[u]\) returns the coefficient bound
to \(A[u]\). The last cofactor returns only the preliminary bound
\(T(u)\in A[u]_{\le2}\). Eliminating that possible quadratic term
requires the next step; it is not a consequence of \(\Delta=0\)
by inspection of its own determinant.

## 3. Local nilpotence controls the vertical coefficient

First \(T(A)\ne0\). Otherwise \(0=Tx_i=a_iT(u)\), and one
nonzero speed forces \(T(u)=0\). Since \(A,u\) generate \(B\),
this would make the actual nonzero partial \(T\) vanish.

Choose finite algebra generators of \(A\), and let \(k\) be the
largest \(u\)-degree of their images under \(T\). The derivation
rule gives the same bound on every element of \(A\), so
\(k\in\{0,1\}\) is the exact horizontal degree. Give the zero
polynomial degree \(-\infty\), and set
\[
\begin{gathered}
d=\max\{k,\deg_uT(u)-1\}\in\{0,1\},\\
T(f)=\sum_{j=0}^{d}D_j(f)u^j\quad(f\in A),\qquad
T(u)=\sum_{j=0}^{d+1}h_j u^j,\quad h_j\in A.
\end{gathered}
\tag{5}
\]
Each \(D_j\) is a derivation of \(A\). At least one of \(D_d\)
and \(h_{d+1}\) is nonzero by the definition of \(d\).

Here is the full actual-ring leading argument from125.[^2]
Adjoin \(\varepsilon\), extend \(T\) to kill it, and on
\(B[\varepsilon,\varepsilon^{-1}]\) let \(\Psi\) fix \(A,\varepsilon\)
and send \(u\) to \(u/\varepsilon\). Then
\(\varepsilon^d\Psi T\Psi^{-1}\) is an LND: it is an actual
conjugate of \(T\) multiplied by an invariant unit. Its values are
\[
\begin{aligned}
T_\varepsilon(f)&=\sum_{j=0}^{d}D_j(f)u^j\varepsilon^{d-j},\\
T_\varepsilon(u)&=\sum_{j=0}^{d+1}h_j u^j\varepsilon^{d+1-j}.
\end{aligned}
\tag{6}
\]
It preserves \(B[\varepsilon]\), and its restriction is locally
nilpotent by injection into the Laurent ring. Specializing
\(\varepsilon=0\) gives a nonzero LND \(H\) of \(B\) with
\(H(f)=u^dD_d(f)\) on \(A\) and \(H(u)=h_{d+1}u^{d+1}\).

For an LND on a characteristic-zero domain, \(f\mid H(f)\)
forces \(H(f)=0\). Indeed LND degree is additive on nonzero
products, whereas a nonzero derivative lowers that degree by one.
Since \(d\ge0\), this applies to \(u\), forcing \(h_{d+1}=0\).
Thus \(\deg_uT(u)\le d\) and \(D_d\ne0\). It follows that \(k=d\).
In particular \(k=0\) cannot coexist with a nonzero linear or
quadratic term in \(T(u)\).

Now \(H^j(f)=u^{dj}D_d^j(f)\), so \(N=D_d\) is a nonzero LND
of \(A\). None of this localizes \(T\) at a polynomial it may move.
The only localization of that LND used above is by the new invariant
indeterminate \(\varepsilon\).

## 4. The exact adjoint and the degree-zero case

Since \(E\) kills \(A\) and \(Eu=1\), iterated commutators with
\(E\), evaluated on \(A\) or on \(u\), differentiate the coefficients
of \(T\) in \(u\). Thus (5) and the improved vertical bound prove
(2) and the asserted exact degree \(d=k\).

If \(d=1\), write \(Q=[E,T]\). Then
\[
\begin{gathered}
0\ne Q,\qquad [E,Q]=0,\qquad Q|_A=N\in\operatorname{LND}(A),
\qquad Q(u)=h_1\in A,\qquad N(a_i)=0,\\
\exp(\lambda E)T\exp(-\lambda E)=T+\lambda Q.
\end{gathered}
\tag{7}
\]
The equality \(N(a_i)=0\) follows from the coefficient of \(u^2\)
in \(T(b_i+a_i u)=0\). Also \(Q\) itself is locally nilpotent:
\(\varepsilon\exp(\varepsilon^{-1}E)T\exp(-\varepsilon^{-1}E)
=\varepsilon T+Q\) is an LND on the Laurent extension, preserves
\(B[\varepsilon]\), and specializes to \(Q\).
The coefficient \(h_1\) is not asserted to vanish. Hence \(Q\)
must not be identified with the extension of \(N\) killing \(u\).

If \(E^3z=0\), then \(N(q)=Q(q)=0\) for \(q=E^2z\). For
\(q\ne0\), this is the top coefficient of \(Tz=1\), using
\(\deg_uT(u)\le1\); for \(q=0\) it is immediate. This does not
make \(q\) a complex constant.

If \(d=0\), then \([E,T]=0\). In particular \(T(a_i)=0\), so
\(E\) restricts to a nonzero nice LND of the actual polynomial
ring \(\mathbb C[x_1,x_2,x_3]\). The retained three-variable
linear-invariant theorem gives a constant nonzero linear good
coordinate fixed by \(E\); the regular-kernel recognition theorem
then gives \(A\simeq\mathbb C^{[3]}\), with the original slice
supplying regularity.[^3] This is the previously established
degree-zero recognition gate, not a new recognition argument.

If the rank-two speed image has no homogeneous linear relation,
this degree-zero alternative is impossible. Consequently the
nonlinear conical case has exact selected adjoint degree one.
It still requires further recognition work.

## 5. Sharpness and scope

The upper bound one is attained in the actual conical frame
\[
\begin{gathered}
(x_1,x_2,x_3,z)=(a,\ b+a^2u,\ v+bu,\ u),\qquad E=\partial_u,\\
a=x_1,\quad u=z,\quad b=x_2-x_1^2z,\quad v=x_3-bz,\\
T=\partial_u-a^2\partial_b+(a^2u-b)\partial_v,\qquad
[E,T]=a^2\partial_v\ne0 .
\end{gathered}
\tag{8}
\]
The successive displayed inverse verifies both polynomial inverse
orders. Its speeds \((0,a^2,b)\) have rank two and a linear homogeneous
relation. This is the retained132 control, not a new example or
evidence of existence in the nonlinear conical branch.

The conclusion sharpens the rank-only bound126 without assuming
constant acceleration. The older conical88 proof used
\(E^2z\in\mathbb C^*\); that assumption is absent here.[^4]
No unit good-speed ideal, intrinsic quotient-plane presentation,
free intrinsic action, or ambient coordinate status for the given
slice was used to prove (2). The argument does not recognize every
supplied three-good quadratic frame or solve arbitrary frame entry.

## Sources

1. [Dense three-good speeds force exact bad-partial adjoint degree two](dense-three-good-adjoint-degree-pass132.md),
   Sections 2--4 and 6. Separating field, actual invariant volume,
   cofactor signs, and the existing conical control.
2. [An intrinsic additive action fixing every good-coordinate speed](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2--4. The actual Laurent leading-LND argument.
3. [Rank-sensitive adjoint bounds from an actual three-good frame](three-good-flow-cofactor-bounds-pass126.md),
   Section 4. The retained degree-zero recognition proof, using the
   three-variable linear-invariant theorem and the regular-kernel theorem.
4. [The conical speed branch supplies the original good last partial](constant-acceleration-conical-good-direction-pass88.md),
   Sections 1--2. Earlier constant-acceleration comparison.

[^1]: [Dense cofactor132](dense-three-good-adjoint-degree-pass132.md), Sections 2--4.
[^2]: [Intrinsic leading125](three-good-intrinsic-speed-quotient-pass125.md), Sections 2--4.
[^3]: [Cofactor126](three-good-flow-cofactor-bounds-pass126.md), Section 4, with its explicitly inherited recognition inputs.
[^4]: [Constant-acceleration conical88](constant-acceleration-conical-good-direction-pass88.md), Sections 1--2.

