# A nonlinear shear parameter excludes a nonplanar nilpotent image

The aligned-parameter obstruction extends to a class of genuinely
nonlinear projective parameters. Let r=y-F(x), where F is a rational
function of x with nonconstant derivative. A polynomial three-variable
map whose projective ratios are rational functions of r cannot have
a nonplanar image and a nilpotent Jacobian. No polynomial inverse or
homogeneity assumption is needed for this exclusion.

This is a restriction on a specified projective parameter. It does
not make a general parameter into one of this form, and it does not
settle the unrestricted conical-image line-family construction.

## 1. Statement and the actual change used in the calculation

Let x,y,z be independent complex variables. Fix F in C(x) such
that F' is not a complex constant, and put r=y-F(x). Suppose

\[
H=A(x,y,z)(1,f(r),g(r))^t\in\mathbb C[x,y,z]^3,
\qquad 0\ne A\in\mathbb C[x,y,z],\quad f,g\in\mathbb C(r).
\tag{1}
\]

If the original Jacobian K=Jac_(x,y,z)H is nilpotent, then f is
constant. Consequently the image of H is contained in the linear
plane H2=f H1.

Equivalently, if a polynomial map with nilpotent Jacobian has all
projective ratios in C(y-F(x)), its image is planar. If H1=0 this
is immediate; otherwise take A=H1 in (1). The conclusion applies
in particular to every polynomial F of degree at least two.

Set k=C(x). The substitution y=r+F(x) gives the exact field and
polynomial-ring identifications

\[
\mathbb C(x,y,z)=k(r,z),\qquad
k[y,z]=k[r,z],\qquad A\in k[r,z].
\tag{2}
\]

When F is a polynomial, (x,y,z) and (x,r,z) are even two-sided
global polynomial coordinate systems. When F is merely rational,
only (2) is used. In neither case do we claim that replacing H by
its expression in the new variables preserves its Jacobian's
nilpotence. All matrix identities below begin with the original
Jacobian in (1).

## 2. Nilpotence gives an exact scalar differential identity

Write h=(1,f(r),g(r))^t and let a prime on h,f,g mean ordinary
differentiation with respect to r. The product rule, in the
original coordinates, gives

\[
K=[h\mid A h']\binom{dA}{dr}.
\tag{3}
\]

Here dA and dr are the original three-entry gradient rows.
Define the rational derivations D0=h dot partial and
D1=h' dot partial. Expressing these two derivations in the
actual field identification (2), rather than forming a new
Jacobian, gives

\[
\begin{aligned}
c&=f(r)-F'(x),\\
D_0&=\partial_x+c\partial_r+g(r)\partial_z,\\
D_1&=f'(r)\partial_r+g'(r)\partial_z,\\
\binom{dA}{dr}[h\mid A h']
&=\begin{pmatrix}D_0A&A D_1A\\c&A f'\end{pmatrix}.
\end{aligned}
\tag{4}
\]

The derivative partial_x in the expression for D0 holds r,z
fixed. In particular D1 fixes k=C(x).

If UV is nilpotent, then VU is nilpotent because
(VU)^(n+1)=V(UV)^nU. Apply this to (3). Trace and determinant
of the two-by-two matrix (4) vanish, so

\[
D_0A=-A f',\qquad cD_1A=-A(f')^2,
\qquad D_1(Ac)=0.
\tag{5}
\]

The last equality uses D1c=(f')^2, since D1 fixes x.
These identities preserve all coefficients of the original
Jacobian. No constant-rank matrix alone is substituted for its
integrability conditions.

## 3. The highest z coefficient rules out nonconstant f

Suppose f is nonconstant. Then f' is nonzero in characteristic
zero. Expand the actual polynomial A of (2) as

\[
A=\sum_{j=0}^{n}a_j(x,r)z^j,
\qquad a_n\in k[r]\setminus\{0\}.
\tag{6}
\]

In D1(Ac)=0, the term g' partial_z lowers z-degree, while
c and f' are independent of z. Its coefficient at z^n is
therefore f' partial_r(a_n c)=0. The constants of partial_r
on k(r) are k, by differentiation of a reduced rational fraction.
Thus

\[
a_n c=\gamma\in k^*.
\tag{7}
\]

The constant is nonzero: a_n is nonzero and c cannot vanish
identically, because f is a nonconstant function of r while
F'(x) belongs to k.

Write f=M/N in lowest terms, where M,N are coprime in C[r]
and N is nonzero. Equation (7) becomes

\[
a_n\bigl(M-F'(x)N\bigr)=\gamma N
\quad\text{in }k[r].
\tag{8}
\]

The polynomial M-F'N is coprime to N, because M and N remain
coprime after extending the coefficient field to k. Its r-degree
is max(deg M,deg N), which is positive. Indeed, if the two
degrees are equal, cancellation of their leading terms would
force F'(x) to be the complex ratio of those leading coefficients,
contrary to the hypothesis; if the degrees differ, there is no
leading cancellation. The excluded zero-degree case would make
f constant.

But (8), with gamma a unit in k, would make the positive-degree
polynomial M-F'N divide N. This contradicts coprimality. Hence
f must be constant, proving the theorem.

## 4. Consequence and exact remaining construction question

The [pass77 aligned theorem](aligned-projective-line-family-obstruction-pass77.md)
treated a projective direction depending on an original linear
coordinate. The present theorem adds nonlinear polynomial shear
coordinates y-F(x), as well as the indicated rational versions.
For example F=x^2 is covered with no degree bound on A,f,g.
The proof does not infer nilpotence from a coordinate change;
the change is used only to compare scalar coefficients after
the full original factorization (3).

For the actual line-family map (s,y) to (s,y+sH(y)), a polynomial
inverse would force Jac H to be nilpotent, as proved in
[pass75, Section1](nice-good-direction-construction-boundary-pass75.md).
Thus this enlarged projective-parameter class cannot produce
the desired nonlinear conical rank-two image, regardless of
whether its line-family inverse exists. This is an exclusion
before the inverse gate, not an inference that nilpotence
constructs that inverse.

The general rational projective parameter need not be a linear
coordinate or a shear of the form treated here. In particular,
the binary parametrization does not supply the hypothesis (1).
No actual nonlinear conical-image example outside these classes,
or an exclusion of all such maps, is proved here.

The argument is elementary and source-free beyond the precisely
linked inherited line-family formula. The author read the saved
proof through EOF. No standalone checker, numerical method,
historical novelty or general cancellation claim is made.
All files through pass77 and shared metadata are unchanged.
