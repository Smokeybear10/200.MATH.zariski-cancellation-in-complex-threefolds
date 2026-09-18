# Audit of the rank-two quasi-translation closure

The proposed residual argument is valid. In four variables, the conditions
\[
J=\operatorname{Jac}(b),\qquad Jb=0,\qquad J^2=0,
\qquad \operatorname{rank}J=2
\tag{1}
\]
force a nonzero constant linear relation among the components of \(b\).
Here rank is over the rational function field. The Euler-cone argument
works, and a separate Jacobian calculation verifies the decisive
homogenization-rank step without using image geometry.

Consequently, if \(E=b\cdot\partial_x\) is the slice derivation under
consideration, it fixes an ambient linear coordinate. The regular-kernel
recognition theorem then identifies \(\ker E\) with \(\mathbb C^{[3]}\).
This audit establishes that residual branch. The reductions from the full
double-bracket system to this branch and the other branches are separate
proof obligations, not re-proved here.

## 1. The Euler-cone step

Let \(F=\mathbb C(x_1,x_2,x_3,x_4)\). Since \(J^2=0\), one has
\(\operatorname{im}_FJ\subseteq\ker_FJ\). Both spaces have dimension two,
so
\[
\operatorname{im}_FJ=\ker_FJ.
\]
The equation \(Jb=0\) therefore gives \(b=Jv\) for some \(v\in F^4\).
No polynomial solution \(v\), regularity at every point, or global
surjectivity of the coefficient map is needed.

Let \(S\) be the Zariski closure of the image of
\(b:\mathbb A^4\to\mathbb A^4\), with defining prime ideal
\[
I=\{P\in\mathbb C[y_1,y_2,y_3,y_4]:P(b)=0\}.
\]
For \(P\in I\), the chain rule gives
\[
(\nabla P)(b)J=0.
\]
Multiplication by the rational vector \(v\) gives
\[
(\nabla P)(b)b=0.
\]
This is a polynomial identity, even though the intermediate vector was
rational. With \(\mathcal E_y=\sum_i y_i\partial_{y_i}\), it says
\[
\mathcal E_y(I)\subseteq I.
\tag{2}
\]

For completeness, (2) really makes \(I\) homogeneous. If
\(P=\sum_{j\in M}P_j\in I\) is its decomposition into nonzero homogeneous
parts of distinct total degrees, the finite collection
\(P,\mathcal E_yP,\ldots,\mathcal E_y^{|M|-1}P\) lies in \(I\).
The coefficient matrix on the \(P_j\) is a Vandermonde matrix in those
distinct nonnegative integers and is invertible over \(\mathbb C\).
Hence every \(P_j\in I\). Thus \(S\) is a closed cone.

The rank assumption also gives \(\dim S=2\), by the characteristic-zero
Jacobian criterion for transcendence degree. In particular, the cone
conclusion concerns the closure of the image. It does not assert that
\(b\) attains the origin. Those are different statements.

## 2. Homogenization and its image

Put \(d=\max_i\deg b_i\), which is at least one, and introduce \(t\).
Define the five-component polynomial map
\[
\widetilde b(x,t)=\bigl(t^d b(x/t),0\bigr).
\tag{3}
\]
Every component is homogeneous of degree \(d\). On \(t\ne0\), its image
lies in \(S\times\{0\}\), because \(b(x/t)\in S\) and \(S\) is a cone.
Every polynomial equation of \(S\times\{0\}\) therefore vanishes on
\(\widetilde b\) on a dense open subset of the source, hence identically.
This also handles \(t=0\); no separate assertion about points at infinity
is required.

Conversely, specializing \(t=1\) recovers \((b(x),0)\), whose image is
dense in \(S\times\{0\}\). Hence
\[
\overline{\operatorname{im}\widetilde b}=S\times\{0\},
\qquad \operatorname{rank}\operatorname{Jac}(\widetilde b)=2.
\tag{4}
\]

The equation \(Jb=0\) makes \(x+b\) a quasi-translation.
[De Bondt, Proposition 1.3 and Proposition 5.1](https://arxiv.org/pdf/1501.05168)
provide the quasi-translation criterion and this homogenization
construction. The latter proposition alone allows rank to increase by
one. Equation (4), not that general bound, is what rules out rank three
in this application.

## 3. Independent direct check of the preserved rank

There is a shorter algebraic verification of (4). Work over
\(\mathbb C(x,t)\), put \(z=x/t\), and differentiate (3):
\[
\operatorname{Jac}_{x,t}(\widetilde b)
=t^{d-1}
\begin{pmatrix}
J(z)&d\,b(z)-J(z)z\\
0&0
\end{pmatrix}.
\tag{5}
\]
Since \(b(z)\in\operatorname{im}J(z)\), the last column in (5) lies in
the span of the first four. Those first four have rank two. Thus the
homogenized rank is exactly two, independently of the cone argument.
Also,
\[
\operatorname{Jac}(\widetilde b)\,\widetilde b
=\bigl(t^{2d-1}J(z)b(z),0\bigr)=0,
\]
which independently checks the quasi-translation condition.

The full-rank-half-dimensional hypothesis is substantive. For example,
\(b=(1,x_3,0,0)\) satisfies \(Jb=J^2=0\) but has Jacobian rank one.
Its image is not a cone, and its degree-one homogenization
\((t,x_3,0,0,0)\) has rank two. Thus one must not replace the argument
above with blanket rank preservation for arbitrary quasi-translations.

## 4. The exact homogeneous theorem and descent of its conclusion

[De Bondt, Theorem 5.3, attributed to Gordan and Noether](https://arxiv.org/pdf/1501.05168)
states that a homogeneous quasi-translation in dimension \(n\), whose
coefficient Jacobian has rank two, has coefficient-image linear span of
dimension at most \(n-2\). There is no additional irreducibility or
coefficient-gcd-one hypothesis in the theorem's statement; its proof
handles common factors.

Apply it to (3) in dimension five. Equations (3)--(5) verify every needed
hypothesis, so
\[
\dim_{\mathbb C}\operatorname{Span}
\bigl(\operatorname{im}\widetilde b\bigr)\le3.
\]
By specialization at \(t=1\), the span of the original image of \(b\)
inside \(\mathbb C^4\) also has dimension at most three. Hence there is
\(0\ne c\in\mathbb C^4\) with
\[
c_1b_1+\cdots+c_4b_4=0.
\tag{6}
\]
This is more than the automatic relation given by the fifth zero
component. Equivalently, the annihilator in five dimensions has dimension
at least two, while only one dimension is explained by that zero
component.

Now \(p=\sum_i c_ix_i\) is an ambient linear coordinate and
\(E(p)=0\). For the original slice setup, \(K=\ker E\) is regular because
\(K[s]\cong\mathbb C^{[4]}\). Thus
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
applies over \(\mathbb C[p]\), giving
\[
K=\mathbb C[p]^{[2]}\cong\mathbb C^{[3]}.
\]

## 5. Audit outcome and scope

No error was found in the Euler preservation, the cone conclusion, the
image-closure equality, the preserved rank, or extraction of a relation
among the original four coefficients. Formula (5) gives a separate check
of the most consequential intermediate step.

The proof uses neither an attained zero of \(b\), nor a finite coefficient
map, nor a global section of an intrinsic quotient. It proves the precise
residual branch (1). As an independent audit, it remains source-dependent
mathematics, not a novelty claim, formal verification, or a separate
audit of the other branches needed for full height-eight closure.
