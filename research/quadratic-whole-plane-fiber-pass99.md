# The whole collapsed fiber has its original plane equation

When the speed normal is nonzero at a collapsed quadratic double
fiber, the original affine-plane description extends to the entire
nonreduced fiber. The remaining equation is exactly a square for
a whole double, or a square times a distinct linear factor for the
mixed (2,1) fiber. The original slice then identifies the actual
quotient fiber ring, including its nilpotents.

This is not an exclusion of either fiber or a global coordinate
recognition theorem. The nonzero-normal and collapsed hypotheses
are retained throughout.

## 1. Actual hypotheses and an original coordinate in the fiber ideal

Retain the supplied actual quadratic frame and the notation of
[volume-normal splitting99](quadratic-volume-normal-splitting-pass99.md).
The original polynomial ring is
\(B=\mathbb C[x_1,x_2,x_3,z]=A[u]\), with E the derivative in
u, canonical \(u=Ez/q\), \(q\in\mathbb C^*\), and three good
coordinates killed by \(E^2\). The actual invariant plane is
\(S=\mathbb C[s_1,s_2]\), its inclusion in A is faithfully flat,
and \(A=S[A_1,A_2,c]\).

Fix a closed base point \(\mathfrak m\) with
\(L_0=L(\mathfrak m)\ne0\). Treat either of these cases:

- the whole reduced fiber is a collapsed fixed component of
  multiplicity two;
- the fixed-containing fiber has profile (2,1). Both components
  are then collapsed by
  [companion-collapse98](quadratic-normal-companion-collapse-pass98.md).

There are actual constant affine good coordinates ell,Y,W, and
canonical centered invariants F,G, with
\[
\begin{gathered}
B=\mathbb C[\ell,Y,W,z],\qquad
\ell=L_0\cdot x_{\rm tr}-\kappa(\mathfrak m),\qquad
E\ell\in\mathfrak m^2,\quad EY\in\mathfrak m,\quad EW-1\in\mathfrak m,\\
F=\ell-uE\ell,\qquad G=Y-uEY,\qquad
\mathfrak q_2B=(\ell,Y),\quad \mathfrak q_2=(F,G),\\
\mathfrak q_1B=(\ell,Y-1),\quad\mathfrak q_1=(F,G-1)
\quad\text{in the mixed case only},\\
\boxed{\quad F\in\mathfrak mA,\qquad \ell\in\mathfrak mB.\quad}
\end{gathered}
\tag{1}
\]
In the whole-double case, complete the nonzero row L_0 by another
constant row in the annihilator of the nonzero speed
\(\mathbf b(\mathfrak m)\), and choose W to have E-speed one at
that point. The exact collapsed-plane proof92 gives the first
plane ideal in (1). The mixed construction and the normalization
of Y to values zero and one are exactly those of98.

The last line is the substantive volume input; it is stronger
than vanishing on the reduced components. Here is its exact
algebraic verification. Put
\(a=x_{\rm tr}-u\mathbf b\in A^3\). The original volume gives
\(L(s)\cdot a=\kappa(s)\). Hence
\(F=(L_0-L(s))\cdot a+\kappa(s)-\kappa(\mathfrak m)\)
belongs to \(\mathfrak mA\). Also
\(\ell=F+uE\ell\) belongs to \(\mathfrak mB\).
No division by Omega or fiber reduction occurs in this argument.

## 2. Cohen--Macaulayness removes embedded primary components

Set
\[
R=B/(\ell)=\mathbb C[Y,W,z],\qquad
J=\mathfrak mB/(\ell),\qquad R/J=B/\mathfrak mB.
\tag{2}
\]
The two polynomial parameters generating \(\mathfrak m\) form
a regular sequence after the flat inclusion \(S\to B\).
Its quotient is a nonzero complete intersection in the regular
ring B. Thus \(B/\mathfrak mB\) is Cohen--Macaulay of pure
dimension two and has no embedded associated primes. Its minimal
primes are exactly the listed component planes in (1).

Under the surjection \(B\to R\), associated primes of this same
quotient correspond. Therefore J has only height-one associated
primes: (Y) in the whole-double case, and (Y),(Y-1) in the
mixed case. This uses the whole quotient's Cohen--Macaulayness,
not an assumption that an arbitrary height-one ideal is principal.

Take a primary component Q of J with radical (p), where p is Y
or Y-1. Primaryness gives
\(Q=QR_{(p)}\cap R\): multiplication by an element outside (p)
cannot put an element into Q unless it was already in Q.
The local ring \(R_{(p)}\) is a DVR, so its nonzero proper ideal
is \((p^e)R_{(p)}\) for a positive integer e. In the polynomial
UFD R, contraction of this ideal is exactly \((p^e)R\).
For example, if a denominator not divisible by p times an
element is divisible by \(p^e\), that element has the same
divisibility. Consequently every primary component is the
indicated ordinary principal power, and
\[
J=(Y^{e_2})
\quad\text{or}\quad
J=(Y^{e_2})\cap((Y-1)^{e_1})
  =(Y^{e_2}(Y-1)^{e_1}).
\tag{3}
\]
The second intersection is a product because the two factors
are comaximal. No normalization or symbolic-power replacement
of the whole fiber has been made.

## 3. The exponents are the actual generic scheme lengths

At the component prime \(\mathfrak q_i\subset A\), write
\(\mu_i=\operatorname{length}_{A_{\mathfrak q_i}}
A_{\mathfrak q_i}/\mathfrak mA_{\mathfrak q_i}\).
The map \(A_{\mathfrak q_i}\to B_{\mathfrak q_iB}\) is a flat
local polynomial extension followed by localization. Its residue
ring is the field extension \(\kappa(\mathfrak q_i)(u)\).
Extending a composition series of the Artinian quotient is exact,
and each residue-field factor remains a simple module over the
target local ring. Therefore its length remains \(\mu_i\).

Quotienting this target by ell gives exactly the DVR quotient
in (3), and does not change the length of a module annihilated
by ell. Put \(p_2=Y\), and \(p_1=Y-1\) in the mixed case.
It follows that
\[
e_i=\operatorname{length}_{R_{(p_i)}}(R/J)_{(p_i)}
   =\mu_i,\qquad
\mu_2=2,\quad \mu_1=1,
\tag{4}
\]
The simple component is absent in the whole-double case.
The lengths are those of the quotient fiber, not of the fixed
scheme of N.

Define H(T) to be \(T^2\) in the whole-double case and
\(T^2(T-1)\) in the mixed case. Equations (2)--(4), and then
canonical E-slice evaluation, prove
\[
\boxed{\quad
\mathfrak mB=(\ell,H(Y)),\qquad
\mathfrak mA=(F,H(G)).
\quad}
\tag{5}
\]
For the second equality, evaluation at u=0 in B=A[u] fixes
\(\mathfrak mA\), maps ell to F and Y to G, and is a ring
homomorphism. Applying it to the exact first ideal equality
gives both inclusions. Thus H is the whole equation, not just
its squarefree reduction.

## 4. The actual original invariant c gives the fiber-ring isomorphism

Let sigma be the original alternative slice used in the
S-matrix completion88. The specified invariant generator is
\(c=z-qu\sigma+q\sigma^2/2\), not an arbitrarily chosen
polynomial parameter. Modulo \(\mathfrak mB\), the S-coefficients
of sigma specialize to constants. Thus sigma is an affine
linear combination of ell,Y,W. Since E-sigma equals one,
E-Y equals zero and E-W equals one in that quotient, its
W-coefficient is one. With ell zero, it has the form
\(\sigma=W+\alpha Y+\beta\), for constants \(\alpha,\beta\).
Hence, putting \(D_0=\mathbb C[Y]/(H(Y))\),
\[
B/\mathfrak mB=D_0[\sigma,z],\qquad
E\sigma=1,\quad EY=0,\quad E^3z=0,\qquad
\pi_\sigma(z)=z-qu\sigma+\frac q2\sigma^2=c.
\tag{6}
\]
Here \(\pi_\sigma\) is the finite E-slice evaluation
\(\sum_j(-\sigma)^j E^j/j!\). It is a ring homomorphism and
fixes the kernel. The canonical presentation also gives
\(B/\mathfrak mB=(A/\mathfrak mA)[u]\), with E the derivative
in u. This has kernel exactly \(A/\mathfrak mA\), even though
that ring may have nilpotents: in characteristic zero, the
derivative of a polynomial in u is zero only when its positive
coefficients vanish.

Applying \(\pi_\sigma\) to the algebra generators Y,sigma,z in
(6) proves surjectivity from \(D_0[c]\) onto that kernel.
Injectivity is equally explicit. In the actual polynomial ring
\(D_0[\sigma,z]\), take ordinary evaluation at sigma=0. The
displayed polynomial c then maps to z. Therefore the proposed
map \(D_0[T]\to D_0[\sigma,z]\), \(T\mapsto c\), followed by
this evaluation is the isomorphism \(D_0[T]\to D_0[z]\).
The original map is injective. This argument does not cancel
a nilpotent element or infer injectivity from dimension alone.

Finally Y and the actual G have the same residue, because
\(Y-G=uEY\in\mathfrak mB\). We have proved the precise
presentation with the actual invariant generators:
\[
\boxed{\quad
\mathbb C[T,Z]/(H(T))\ \xrightarrow{\ \sim\ }\ A/\mathfrak mA,
\qquad T\longmapsto\bar G,\quad Z\longmapsto\bar c.
\quad}
\tag{7}
\]
In particular the whole double is an actual constant square-zero
thickening over its component parameter, and the mixed fiber is
the product of that thickening with the actual simple affine line.
This is a fiber-ring isomorphism, not a polynomial presentation
of A itself.

There is also an immediate original-coordinate consequence:
\(\partial_z\) preserves the whole ideal \(\mathfrak mB\), since
both generators in (5) are independent of z. This is stronger
than preservation of its radical. It does not assert that
\(\partial_z\) preserves A, commutes with E on the whole
nonreduced quotient, or supplies a global invariant coordinate.

## Scope and provenance

Root's exact volume-normal splitting supplies the original
coordinate ell inside the whole fiber ideal. Geometry derived
the Cohen--Macaulay/primary/DVR reconstruction and the actual
slice-retraction fiber presentation. General and Jet independently
checked the primary-contraction and multiplicity outline before
this file was written. No new primary-source theorem, numerical
method, normalization hypothesis, or actual exceptional example
is supplied by this argument.

Both alternatives retain L(m) nonzero and a collapsed fixed
double component; the mixed alternative uses the companion
collapse theorem98. The result does not cover L(m)=0, prove
freeness or recognize A. All files through98 are unchanged.
