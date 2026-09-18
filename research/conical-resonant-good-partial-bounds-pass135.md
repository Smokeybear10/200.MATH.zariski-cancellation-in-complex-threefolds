# Resonant conical speeds bound every good partial by degree two

The radial identity \(Rq=2q\) cancels the only possible cubic horizontal
cofactor of a good-coordinate partial. Local nilpotence then also removes
the possible cubic coefficient on the slice. This gives a height bound
inside the supplied frame, not recognition of the conical class.

## 1. Actual rings and the radial condition

Assume
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2x_i=0,\quad a_i=Ex_i,\quad x_i=b_i+a_i u,\quad a_i,b_i\in A,\\
E^3z=0,\quad q=E^2z\in A,\quad
z=c_0+c_1u+\tfrac12qu^2,\quad c_0,c_1\in A,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)=2,
\quad H(a_1,a_2,a_3)=0
\text{ for a nonzero homogeneous }H.
\end{gathered}
\tag{1}
\]
The four displayed generators are actual polynomial coordinates. The
given slice is not assumed to be one of them. The acceleration may be
nonconstant; the argument also permits \(q=0\).

Let \(T_4=\partial_z\). The selected leading-LND construction gives a
nonzero \(N\in\operatorname{LND}(A)\) killing all \(a_i\) and \(q\).
The conical cofactor theorem gives the selected adjoint degree at most
one.[^1] Define
\[
S=\ker N\subset A,\qquad L=\operatorname{Frac}S,\qquad
K_a=\mathbb C(a_1,a_2,a_3)\subset L,\qquad
[L:K_a]<\infty .
\tag{2}
\]
The local-slice theorem gives \(\operatorname{trdeg}_{\mathbb C}L=2\)
and \(\operatorname{Frac}A=L(v)\) for a suitable local-slice numerator
\(v\in A\). These assertions require neither \(S\simeq\mathbb C^{[2]}\)
nor a global slice for \(N\). Finiteness in (2) follows because \(L\)
is a finitely generated field algebraic over \(K_a\): it is the
constant field in the finite extension of a rational separating field.
Equivalently, adjoining the transcendental \(v\) preserves linear
independence and bounds its degree by the finite degree of
\(\operatorname{Frac}A/\mathbb C(s,t,v)\), for the \(s,t\) below.

The kernel of \(\mathbb C[T_1,T_2,T_3]\to\mathbb C[a_1,a_2,a_3]\)
is a homogeneous prime of height one. Thus the Euler derivation
descends to \(K_a\), where it sends every \(a_i\) to \(a_i\).
It extends uniquely through the finite separable extension to a
derivation \(R\) of \(L\). Choose two algebraically independent
speeds \(s,t\). The corresponding partial derivatives extend uniquely
to \(L\), and
\[
R=s\partial_s+t\partial_t,\qquad
a=s a_s+t a_t,\qquad
Rq=sq_s+tq_t.
\quad\text{Assume }Rq=2q.
\tag{3}
\]
Here \(a=(a_1,a_2,a_3)^T\). The identity for \(R\) follows from
uniqueness of the extension from \(\mathbb C(s,t)\); it does not
choose polynomial coordinates on \(S\).

## 2. The unique cubic horizontal cofactor

Put \(F=\operatorname{Frac}A=L(v)\). Extend the partial derivatives
in \(s,t\) to kill \(v\), and let \(\partial_v\) kill \(L\). The
actual volume form is
\[
dx_1\wedge dx_2\wedge dx_3\wedge dz
=J_0\,ds\wedge dt\wedge dv\wedge du,\qquad J_0\in F^*.
\tag{4}
\]
Indeed its coefficient initially belongs to \(F[u]\). The polynomial
flow of the actual LND has Jacobian one and fixes \(F\), so translation
of \(u\) fixes that coefficient. It is therefore independent of \(u\).
It need not be a complex constant.[^1]

Order the full Jacobian columns as \(s,t,v,u\). Its first three rows
are the rows of
\([b_s+u a_s,\ b_t+u a_t,\ b_v,\ a]\).
The last row is
\[
\bigl(c_{0,s}+c_{1,s}u+\tfrac12q_su^2,
      c_{0,t}+c_{1,t}u+\tfrac12q_tu^2,
      c_{0,v}+c_{1,v}u,
      c_1+qu\bigr).
\tag{5}
\]
The missing \(u^2\) term in the third entry uses \(q\in L\).

Fix a good partial \(T_j=\partial_{x_j}\), \(1\le j\le3\), and let
\(i<k\) be the other two good indices. Cramer's rule immediately gives
\(\deg_uT_j(s),\deg_uT_j(t)\le2\) and
\(\deg_uT_j(u)\le3\). Only \(T_j(v)\) can have a cubic horizontal
term. With the displayed row and column orders, its coefficient is
\[
\begin{aligned}
[u^3]T_j(v)
&=\frac{(-1)^{j+3}}{J_0}
\det\begin{pmatrix}
a_{i,s}&a_{i,t}&a_i\\
a_{k,s}&a_{k,t}&a_k\\
q_s/2&q_t/2&q
\end{pmatrix}\\
&=\frac{(-1)^{j+3}}{2J_0}
\det\begin{pmatrix}a_{i,s}&a_{i,t}\\a_{k,s}&a_{k,t}\end{pmatrix}
(2q-Rq)=0.
\end{aligned}
\tag{6}
\]
For the second equality, subtract \(s\) times the first column and
\(t\) times the second from the third. The first two resulting entries
are zero by (3), and the last is \(q-Rq/2\). This also fixes the sign.

Every \(f\in F\) satisfies
\(T_j(f)=f_sT_j(s)+f_tT_j(t)+f_vT_j(v)\).
The difference kills a separating transcendence basis, hence kills
the whole finite separable extension. Equation (6) therefore gives
\(T_j(F)\subset F[u]_{\le2}\).
For \(f\in A\), the image is also an actual element of \(A[u]\), so
uniqueness of polynomial coefficients returns the bound to \(A[u]\).

## 3. The slice coefficient and exact adjoint bound

The horizontal action \(T_j(A)\) is nonzero. Otherwise \(T_j\),
localized at the nonzero elements of \(A\), would be an LND of
\(F[u]\) killing \(F\), hence \(T_j=fE\) with \(f\in F\).
Its value on \(u\) is an actual polynomial, so \(f\in A\).
The identity \(T_j(x_j)=fa_j=1\) forces \(f,a_j\in\mathbb C^*\),
and \(T_j(x_i)=fa_i=0\) for \(i\ne j\) forces both other speeds
to vanish. This contradicts rank two.

Let \(k_j\in\{0,1,2\}\) be the maximal \(u\)-degree of the images
of finite algebra generators of \(A\). The derivation rule bounds
all of \(T_j(A)\) by the same number. Set
\(d_j=\max\{k_j,\deg_uT_j(u)-1\}\le2\).
Write its leading horizontal coefficient as \(D_{d_j}\) and its
possible coefficient of \(u^{d_j+1}\) on \(u\) as \(h_{d_j+1}\).

The actual Laurent degeneration from125 gives a nonzero LND
\(\mathcal H\) on the original \(B=A[u]\), with
\(\mathcal H(f)=u^{d_j}D_{d_j}(f)\) for \(f\in A\) and
\(\mathcal H(u)=h_{d_j+1}u^{d_j+1}\).[^2]
For clarity, this is obtained by adjoining an invariant parameter
\(\varepsilon\), conjugating \(T_j\) by \(u\mapsto u/\varepsilon\),
multiplying by \(\varepsilon^{d_j}\), and specializing at zero.
The degree bounds make all coefficients polynomial in \(\varepsilon\),
so local nilpotence descends from the actual Laurent conjugate.

Since \(d_j\ge0\), the polynomial \(u\) divides \(\mathcal H(u)\).
Self-divisibility for an LND on a characteristic-zero domain forces
\(\mathcal H(u)=0\). Thus \(h_{d_j+1}=0\), while nonzero leading
degree forces \(D_{d_j}\ne0\). Consequently \(d_j=k_j\) and
\(\deg_uT_j(u)\le d_j\). Iterated commutation with \(E=\partial_u\)
differentiates these coefficients. We have proved
\[
\begin{gathered}
T_j(A)\subset A[u]_{\le2},\qquad T_j(u)\in A[u]_{\le2},
\qquad (\operatorname{ad}_E)^3T_j=0\quad(1\le j\le3),\\
d_4\le1,\qquad (d_1,d_2,d_3,d_4)\le(2,2,2,1),\qquad
\mathcal{H}_{\rm partial}:=\sum_{j=1}^4(d_j+1)\le11.
\end{gathered}
\tag{7}
\]
The selected bound \(d_4\le1\) is the conical theorem135, not a new
conclusion of the good cofactors.

## 4. Conditional height consequence and limits

If one invokes the retained working height-ten recognition theorem,
any unrecognized instance satisfying (1) and (3) must have the exact
ordered degrees \((2,2,2,1)\), or sorted profile \((1,2,2,2)\).[^3]
This is only the arithmetic consequence of (7) and that additional
recognition input. The cofactor proof does not recognize height eleven,
construct a frame attaining it, or prove that a frame of smaller height
can be reached.

The radial condition is an identity in the actual finite field \(L\),
not an assertion that \(q\) is constant or lies in the constant
quadratic speed span. No invariance of \(S\) under the original partials,
freeness of \(N\), polynomial presentation of \(A\) over \(S\), or
coordinate-entry statement is used or concluded.

## Sources

1. [Conical three-good speeds lower the selected adjoint degree](conical-three-good-adjoint-degree-pass135.md),
   Sections 2--4. Actual invariant volume, finite-separable coefficient
   return, selected leading LND and its degree bound.
2. [An intrinsic additive action fixing every good-coordinate speed](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2--5. The actual Laurent degeneration, local slice and
   annihilation of the leading acceleration coefficient.
3. [Recognition of the supplied two-quadratic frame and height ten](height-ten-closure-pass73.md).
   Additional retained working recognition input for the conditional
   profile statement only, not a new result of this note.

[^1]: [Conical cofactor135](conical-three-good-adjoint-degree-pass135.md), Sections 2--4; [intrinsic leading125](three-good-intrinsic-speed-quotient-pass125.md), Sections 2--5.
[^2]: [Intrinsic leading125](three-good-intrinsic-speed-quotient-pass125.md), Sections 2--3.
[^3]: [Retained height-ten recognition73](height-ten-closure-pass73.md).
