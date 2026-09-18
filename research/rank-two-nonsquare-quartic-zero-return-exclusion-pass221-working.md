# Zero return forces a binary-quadratic square

Status: working necessary-condition theorem for the supplied rank-two
quartic frame. The zero-return branch is impossible unless the binary
quartic is a square. Consequently the squarefree projected-line
conclusion in220 no longer needs a separate nonzero-return assumption.
This does not make a projected line an original polynomial coordinate.

## 1. Exact supplied hypotheses

Keep the actual hypotheses of
[general quartic220](rank-two-binary-quartic-leading-sextic-pass220-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(a\tau,b\tau,e_0\tau^2,h_0\tau^2)\bigr)
 =(\mathsf Z\mathsf W-F_4(\mathsf X,\mathsf Y)).
\end{gathered}
\tag{1}
\]
Here the four capital letters are original polynomial coordinates,
tau is independent, F4 is a nonzero complex homogeneous binary quartic,
and the equality specifies the entire initial kernel.

The actual chart of
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
supplies an exact coefficient field L, a selected parameter v, and
\[
\begin{gathered}
t=b/a,\quad \rho=h_0/a^2,\quad f(t)=F_4(1,t),\quad
q=e_0/a^2=f(t)/\rho,\\
[L:\mathbb C(t,\rho)]<\infty,\qquad
y,z,w,\vartheta\in L[v],\qquad L[y,z,w]=L[v].
\end{gathered}
\tag{2}
\]
The ratios t,rho are algebraically independent; f(t) and rho are
therefore nonzero elements of L. The two coefficient derivatives
extend to L and fix v. No rationality of L is assumed.

For formal variables U,V define
\[
H_j(c;U,V)=\sum_{i=0}^j
\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{3}
\]
There are exact coefficients k,n,ell,m in L for which, putting
\[
\begin{gathered}
\mathfrak f=H_2(q)+H_1(k)+n,\qquad
\mathcal R=\mathfrak f_V,\qquad R=\mathcal R(y,\vartheta),\\
S=H_3(q)+H_2(k)+H_1(n),\\
Q=H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,
\end{gathered}
\tag{4}
\]
the actual potentials give
\[
\begin{gathered}
z=q_\rho w+\mathfrak f(y,\vartheta),\qquad
Rw+S(y,\vartheta)=\ell,\\
\frac{f(t)}{\rho^3}w^2+
\mathfrak f_\rho(y,\vartheta)w+Q(y,\vartheta)=0.
\end{gathered}
\tag{5}
\]
The coefficient derivative in the last line is taken before
evaluation. Its leading coefficient in w is a nonzero element of L.
These identities and the whole-line return, rather than a formal
parametrization alone, are the inputs below.

## 2. The exact obstruction in the zero-return branch

Assume R=0 as an identity in L[v]. Direct differentiation gives
\[
0=-\frac{f'}{\rho^2}y+\frac{2f}{\rho^3}\vartheta+k_\rho,
\qquad
\vartheta=\frac{\rho f'}{2f}y-\frac{\rho^3k_\rho}{2f}.
\tag{6}
\]
No division by a projected polynomial has occurred; the denominators
are nonzero scalars in L. Substitute (6) into the middle equation
of (5). It becomes a polynomial equation in y over L of degree at
most three. The terms H2(k) and H1(n) have degrees at most two and
one after this affine substitution.

Thus the coefficient of y cubed comes only from H3(q). It is
\[
\begin{aligned}
H_3\left(q;1,\frac{\rho f'}{2f}\right)
&=\frac{f'''}{6\rho}
 -\frac{f'f''}{4\rho f}
 +\frac{(f')^3}{8\rho f^2}\\
&=\frac{\mathcal J(f)}{24\rho f^2},\\
\mathcal J(f)&=4f^2f'''-6ff'f''+3(f')^3.
\end{aligned}
\tag{7}
\]

If J(f) is nonzero, the equation is a nonzero cubic over L.
A nonconstant polynomial y(v) cannot satisfy such an equation:
the highest power of y has strictly larger v-degree than every
lower power. Hence y belongs to L, and (6) gives theta in L.
The last equation in (5), with its nonzero quadratic coefficient,
then forces w in L by the same degree argument. The first equation
forces z in L. This contradicts L[y,z,w]=L[v].

We have proved the necessary condition
\[
\boxed{R=0\quad\Longrightarrow\quad\mathcal J(f)=0.}
\tag{8}
\]
This step does not require birationality or normality of the
projected plane curve, and does not presume that its ring is L[v].

## 3. Classifying the vanishing obstruction, including infinity

For every nonzero complex polynomial f of degree at most four,
\[
\boxed{\mathcal J(f)=0
\quad\Longleftrightarrow\quad f=g^2
\text{ for some }g\in\mathbb C[t],\ \deg g\le2.}
\tag{9}
\]
The nonzero scalar square root is included in g.

To prove the forward direction, let r be any finite root of f
with multiplicity m, and write f=c(t-r)^m plus higher terms,
where c is nonzero. In J(f) the coefficient at order 3m-3 is
\[
c^3\{4m(m-1)(m-2)-6m^2(m-1)+3m^3\}
=c^3m(m-2)(m-4).
\tag{10}
\]
For the odd multiplicities possible here, m=1 or m=3, it is nonzero.
Consequently every finite root has even multiplicity if J(f)=0.
Factorization over C makes f a square of degree at most four.
The same conclusion holds when f is a nonzero constant.

Conversely, a direct differential identity gives
\[
\mathcal J(g^2)=8g^5g'''.
\tag{11}
\]
For degree g at most two, this vanishes. The identity proves
sufficiency without imposing restrictions on repeated roots.

Since F4 is homogeneous of degree four, the square equivalence
also holds projectively:
\[
f(t)=g(t)^2
\quad\Longleftrightarrow\quad
F_4(X,Y)=G_2(X,Y)^2,\qquad G_2=X^2g(Y/X).
\tag{12}
\]
The last expression is a polynomial homogeneous of degree two.
In particular a root at infinity has multiplicity 4-deg(f), which
is even in the square case. No projective root was omitted.

Combining (8)--(12) proves the working theorem
\[
\boxed{F_4\text{ is not a binary-quadratic square}
\quad\Longrightarrow\quad R\ne0.}
\tag{13}
\]
This is a necessary-condition result. It does not assert that an
actual zero-return frame exists for either of the square types.

## 4. Consequences for the general quartic reduction

The nonzero-return degree theorem in
[general quartic220](rank-two-binary-quartic-leading-sextic-pass220-working.md)
can now be applied without an additional R assumption to all three
nonsquare root partitions. Its exact conclusions are:

| Projective root multiplicities of F4 | Projected degree bound |
| --- | --- |
| 1+1+1+1 | g=1 and L[y,theta]=L[v] |
| 2+1+1 | g at most2 |
| 3+1 | g at most3 |

Here g is the degree of the irreducible relation of the projected
pair, equivalently max(deg_v y,deg_v theta) under the proved
birational return. It is not an ambient coordinate degree.
In particular,
\[
\boxed{F_4\text{ squarefree}\quad\Longrightarrow\quad
R\ne0,\quad L[y,\vartheta]=L[v],\quad
\max(\deg_vy,\deg_v\vartheta)=1.}
\tag{14}
\]
This remains a supplied-frame chart reduction. A scalar in L
cannot be used as a complex polynomial coordinate change without
a separate original-ring argument.

For orientation only, the two square root partitions are 2+2
and4. Actual constant invertible linear changes of X,Y, together
with a nonzero constant rescaling of a bad coordinate, normalize
them respectively to ZW-X squared Y squared and ZW-X to the fourth.
Exact degree one for the changed good coordinates is preserved
because t=b/a is transcendental. The full ideal transforms by the
same polynomial automorphism. This normalization alone asserts
neither existence nor an unrestricted cancellation theorem.

## 5. Verification and scope

The source derivation above was independently reconstructed before
saving. New unsaved inline algebra checked the complete cubic
substitution, differential square identity and local multiplicity
coefficient; these checks do not replace the whole-return or
coefficient-field arguments.

There is no new conclusion about arbitrary frame entry, higher
initial kernels, or unrestricted complex-threefold cancellation.
There is no human expert review, formal proof-assistant verification,
historical novelty clearance, submission, public posting or external
contact. Earlier frozen220 and219 sources are unchanged.
