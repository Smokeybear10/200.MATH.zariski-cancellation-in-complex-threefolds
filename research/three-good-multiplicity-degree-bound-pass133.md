# A multiplicity-sensitive degree bound for coordinate-initial relations

The actual selected bad partial bounds how much an original weighted
expression can drop in the slice filtration. A first relation drops by
at most four; a top expression containing that relation with multiplicity
\(k\) drops by at most \(4k\). The inverse-verified cubic frame realizes
equality for every \(k\).

This is a necessary degree estimate. Combined with invariant growth,
it yields the separate quadratic-or-primitive-cubic dichotomy below.
It does not prove termination of an enlarged-generator subduction
procedure or passage of the later correction conditions.

## 1. Actual filtration and the first relation

Assume the actual sliced dense quadratic three-good setup
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad E=\partial_u,\\
x_i=b_i+a_i u,\qquad z=c_0+c_1u+c_2u^2,\qquad c_2=q/2\ne0,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)=2,
\qquad a_1\tau,a_2\tau,a_3\tau
\text{ algebraically independent over }\mathbb C.
\end{gathered}
\tag{1}
\]
Here \(\tau\) is an indeterminate, and all coefficients of the
displayed slice expansions belong to \(A\).
The retained actual intrinsic construction gives
\(N\ne0\) locally nilpotent on \(A\), with
\(a_i,c_2\in S=\ker N\) and
\(\operatorname{trdeg}_{\mathbb C}S=2\) by the elementary local-slice
argument.[^1] No affine-plane presentation of \(S\) is used.
The exact dense cofactor theorem gives, for \(T=\partial_z\),
\(T(A)\subset A[u]_{\le2}\), \(T(u)\in A[u]_{\le2}\),
and \([u^2]T|_A=N\).[^2]

Use capital letters for independent source variables and assign weights
\((1,1,1,2)\) to \((X_1,X_2,X_3,Z)\). The coordinate-initial map is
\[
\begin{gathered}
\theta:\mathbb C[X_1,X_2,X_3,Z]\longrightarrow A[\tau],\qquad
X_i\longmapsto a_i\tau,\quad Z\longmapsto c_2\tau^2,\\
\ker\theta=(\Phi),\qquad
\Phi\text{ irreducible and weighted homogeneous},\qquad
\Phi_Z\notin(\Phi).
\end{gathered}
\tag{2}
\]
Indeed the image lies in \(S[\tau]\), of transcendence degree three,
and its three good generators are algebraically independent. Its kernel
is therefore a height-one prime in a polynomial UFD. It is a graded
ideal, so its generator can be chosen weighted homogeneous.
No nonzero polynomial in the three \(X_i\) alone belongs to the kernel.
Thus \(\Phi\) involves \(Z\); in characteristic zero its nonzero
\(Z\)-derivative has smaller \(Z\)-degree and cannot be divisible by
\(\Phi\).

This identifies the algebra of coordinate initials, not the full
associated graded ring \(\operatorname{gr}_E B=A[\tau]\). The distinction
already occurs in the actual cubic example below.[^3]

## 2. The multiplicity bound

Let \(P\ne0\) be an original-coordinate polynomial, with weighted degree
\(m\), top weighted part \(P_m\), and
\(n=\deg_E P(x_1,x_2,x_3,z)\). Suppose
\[
P_m=\Phi^k\Psi,\qquad k\ge1,\qquad \Phi\nmid\Psi.
\quad\text{Then}\quad
m-4k\le n\le m-1.
\tag{3}
\]
The substitution is an isomorphism of polynomial rings because the four
original generators are actual coordinates, so its value is nonzero.
The upper bound follows from \(\theta(P_m)=0\).

For the lower bound, apply the actual partial \(T^k\). Differentiation
in \(Z\) decreases weighted degree by two at each step. Modulo
\((\Phi)\), the Leibniz formula gives
\[
\begin{gathered}
\partial_Z^k(\Phi^k\Psi)
\equiv k!\,\Psi\Phi_Z^k\pmod{\Phi},\\
\deg_E\bigl(T^kP(x,z)\bigr)=m-2k,\\
[u^{m-2k}]\,T^kP(x,z)
=k!\,\Psi(a,c_2)\Phi_Z(a,c_2)^k\ne0.
\end{gathered}
\tag{4}
\]
In the congruence, a derivative term survives only if every one of the
\(k\) factors \(\Phi\) is differentiated at least once. The image of
the surviving product is nonzero by (2), primeness, and characteristic
zero. Lower weighted pieces of \(P\) cannot contribute at weight
\(m-2k\). This proves the exact degree assertion in (4).

On the other hand \(T\) raises \(E\)-degree by at most two on every
element of \(A[u]\). For a term \(f u^j\), its coefficient derivative
has degree at most \(j+2\), and its derivative through \(u\) has degree
at most \(j+1\). Iteration gives \(m-2k\le n+2k\), proving (3).

Write \(h_n=[u^n]P(x,z)\in A\). The degree-two leading coefficient
of \(T\) on \(A[u]\) is \(u^2N\), with \(N(u)=0\). Consequently
\[
N^k(h_n)=
\begin{cases}
k!\,\Psi(a,c_2)\Phi_Z(a,c_2)^k,&n=m-4k,\\
0,&n>m-4k.
\end{cases}
\tag{5}
\]
This coefficient formula follows by iterating the top coefficient rule;
it does not require any localization. The nonzero value in the first
case belongs to \(S\), so then \(N^{k+1}(h_n)=0\).

For the first relation itself, take \(P=\Phi\) and \(k=1\).
Its degree drop is at most four. A drop of less than four leaves its
leading coefficient in \(S\); a drop of four produces an actual local
slice for \(N\), with image \(\Phi_Z(a,c_2)\).

## 3. Sharpness and the limit of an iterative interpretation

The retained cubic frame is an actual translation example.[^3]
In independent coordinates \((a,b,v,u)\), put
\[
\begin{gathered}
X=u,\qquad Y=v+au,\qquad Z=a-v^3/2+bu,\\
W=b+3av^2/2+3a^2vu/2+a^3u^2/2,\\
\Phi=2XW-Y^3,\qquad
\Phi(x)=2Z-2a,\\
v=Y-XZ+X^2W-XY^3/2,
\qquad \operatorname{in}_{\mathrm{wt}}v=(X/2)\Phi.
\end{gathered}
\tag{6}
\]
The inverse recovers successively
\(u=X\), \(a=Z-XW+Y^3/2\), \(v=Y-aX\), and
\(b=W-3av^2/2-3a^2vX/2-a^3X^2/2\).
Substitution in either order verifies the polynomial inverse, without
inverting any variable.
The speeds are \((1,a,b)\), \(c_2=a^3/2\), and direct differentiation
of this inverse gives
\[
\begin{gathered}
Ta=-u,\qquad Tv=u^2,\qquad Tb=1+3v^2u/2,\qquad Tu=0,
\qquad N=\partial_v,\\
\operatorname{wt}(v^k)=4k,\qquad \deg_E(v^k)=0,
\qquad \operatorname{in}_{\mathrm{wt}}(v^k)=(X/2)^k\Phi^k,
\qquad N^k(v^k)=k!.
\end{gathered}
\tag{7}
\]
Thus equality in (3)--(5) occurs for every positive integer \(k\), in
one actual inverse-verified frame.

The same example prevents a stronger assertion about weights assigned
after adjoining new generators. First \(\Phi(x)=2Z-2a\) drops from
original weight three to \(E\)-degree one. Subtracting \(2Z\) recovers
\(-2a\), by a drop from current degree one to zero. After adjoining
\(a\) with degree zero, \(Y-aX=v\) drops from current degree one to
zero and has \(N(v)=1\). Thus the first coefficient moved by \(N\)
in an enlarged-generator procedure need not arise by a four-degree
drop in those enlarged weights. Its expression in the original
coordinate weights still has the four-degree drop in (6).

## 4. Relation degree, subsequent growth, and scope

A weighted relation of degree two is exactly
\(Z-J_2(X)\) up to scalar, and is equivalent to \(q\) lying in
the constant quadratic speed span. A degree-three irreducible relation
must be \(L(X)Z-F_3(X)\), with \(L\ne0\) linear and
\(\gcd(L,F_3)=1\). Thus the primitive mixed relation sought in the
correction criterion is exactly the case \(\operatorname{wt}\Phi=3\).[^4]
The separate leading-dichotomy proof applies (3) to every nonconstant
invariant, then compares the positive original-weight filtration with
the growth of three algebraically independent invariants. It proves
\(\operatorname{wt}\Phi\le3\), and hence that exactly one of these
two forms occurs.[^5] In particular, weighted degree four is excluded
in the actual setup (1). The multiplicity calculation is the input to
that growth argument, not a reason to leave leading-relation existence
open. Neither argument proves passage of the two subsequent correction
tests.

No generation of the full associated graded ring by the four initials,
finite subduction algorithm, or invariant of a prescribed original
weight is asserted. The estimate uses the actual partial and its
proved degree bound; it is not a realization claim for arbitrary
weighted hypersurfaces or arbitrary speed tuples.

## 5. Comparison with the classical derivative method

The repeated-derivative and multiplicity mechanism is classical.
Vénéreau's paper works with ordinary total degree, algebraically
independent polynomials over a characteristic-zero field, and a
Jacobian-defined parachute. Its Property (2), followed by the main
theorem and its proof, differentiates up to the exact multiplicity
of a relation among leading forms.[^6]

Equations (3)--(5) specialize that method to the actual slice filtration:
the proved degree-two shift of \(\partial_z\) supplies the derivative
bound, and its intrinsic coefficient \(N\) records equality. The
ordinary-degree theorem is not invoked as a black box for the
\(E\)-filtration, whose degree-zero ring is \(A\). The proof above
establishes the needed specialization directly. No historical novelty
claim is made for the derivative method.

## Sources and comparisons

1. [An intrinsic additive action fixing every good-coordinate speed](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2--5. The actual leading LND, its common kernel, and the
   invariant-local-slice polynomial presentation.
2. [Dense three-good speeds force exact bad-partial adjoint degree two](dense-three-good-adjoint-degree-pass132.md),
   Sections 2--5. The actual cofactor bounds used in (3)--(5).
3. [Cubic acceleration outside the fixed-good quadratic span](three-good-cubic-acceleration-span-obstruction-pass129.md),
   Sections 1--5. The polynomial inverse, selected partial and
   coordinate-initial algebra underlying the exact control (6)--(7).
4. [Correcting a mixed cubic relation to an invariant coordinate](three-good-mixed-cubic-correction-criterion-pass130.md),
   Sections 1--3. The specified primitive cubic relation and its two
   correction conditions.
5. [A quadratic-or-primitive-cubic dichotomy for actual coordinate initials](three-good-quadratic-cubic-leading-dichotomy-pass133.md),
   Sections 2--4. The separate invariant-growth argument using (3).
6. Stéphane Vénéreau, [A parachute for the degree of a polynomial in algebraically independent ones](https://arxiv.org/pdf/0704.1561),
   arXiv:0704.1561v2 (2007), pp. 1--3, Property (2), main theorem,
   and the multiplicity lemma and their proofs. This is a method
   comparison, not a direct application of its ordinary-degree theorem.

[^1]: [Intrinsic-speed quotient125](three-good-intrinsic-speed-quotient-pass125.md), Sections 2--5.
[^2]: [Dense cofactor degree132](dense-three-good-adjoint-degree-pass132.md), Sections 2--5.
[^3]: [Actual cubic frame129](three-good-cubic-acceleration-span-obstruction-pass129.md), Sections 1--5.
[^4]: [Mixed-cubic correction130](three-good-mixed-cubic-correction-criterion-pass130.md), Sections 1--3.
[^5]: [Leading dichotomy133](three-good-quadratic-cubic-leading-dichotomy-pass133.md), Sections 2--4.
[^6]: [Vénéreau, arXiv:0704.1561v2](https://arxiv.org/pdf/0704.1561), pp. 1--3.
