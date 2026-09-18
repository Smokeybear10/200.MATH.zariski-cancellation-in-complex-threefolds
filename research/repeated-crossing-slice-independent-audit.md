# Independent audit of the repeated-crossing slice shortcut

The proposed shortcut is valid for a slice of a locally nilpotent
derivation on the original four-variable polynomial ring. In fact, every
fiber of either constant-axis normal form is an affine three-space,
without assuming stability. The slice hypothesis then identifies that
fiber ring with the kernel and proves that the slice is a coordinate.
The corresponding conclusion for a merely stable coordinate does not
follow from this argument.

## 1. The fiber is an affine-plane fibration over a line

Consider orientation A:

\[
 F=x^r y^s u+ay+cx^kz+B(x)+xyR(x,y,z),
 \qquad a,c\in\mathbb C^*,\quad r,s,k\ge1.
\]

For any \(\lambda\in\mathbb C\), set

\[
 A_\lambda=\mathbb C[x,y,z,u]/(F-\lambda).
\]

The equation is primitive and linear in \(u\). Its coefficient is
\(x^ry^s\), while its remainder reduces to
\(ay+B(0)-\lambda\) modulo \(x\), and to
\(cx^kz+B(x)-\lambda\) modulo \(y\). Neither is zero, so the
coefficient and remainder have gcd one. Gauss's lemma makes
\(F-\lambda\) irreducible, hence prime in the polynomial UFD.
Thus \(A_\lambda\) is a domain.

The map \(\mathbb C[x]\to A_\lambda\) is injective. For example,
localizing also at \(y\) identifies the quotient with
\(\mathbb C[x,x^{-1},y,y^{-1},z]\), in which \(x\) is
transcendental. Therefore \(A_\lambda\) is torsion-free over the
PID \(\mathbb C[x]\), hence flat. It is finitely presented over
that ring.

The fiber at \(x=0\) is

\[
 A_\lambda/xA_\lambda
 =\mathbb C[y,z,u]/(ay+B(0)-\lambda)
 \simeq\mathbb C[z,u].
 \tag{1}
\]

There is also a uniform trivialization after inverting \(x\). Over
\(L=\mathbb C[x,x^{-1}]\), regard \(F-\lambda\) as

\[
 p u+q(z),\qquad p=x^ry^s,\qquad
 q(z)=cx^kz+B(x)-\lambda+y\bigl(a+xR(x,y,z)\bigr).
\]

The leading linear coefficient \(cx^k\) is a unit of \(L\).
Modulo \(p\), the element \(y\) is nilpotent, since \(x\) is a
unit. Consequently the finite inverse construction in
[repeated-crossing-pass.md](repeated-crossing-pass.md), Section 1,
applies over \(L[y]\), with nilpotent perturbation parameter \(y\).
It gives a polynomial companion to \(F-\lambda\), and hence

\[
 A_\lambda[1/x]\simeq L^{[2]}.
 \tag{2}
\]

This proves both the generic-fiber assertion over \(\mathbb C(x)\)
and the affine-plane assertion at every \(x=\alpha\ne0\).
Together with (1), it checks the residue-field fiber at every prime
of \(\mathbb C[x]\). Thus \(A_\lambda\) is an
\(\mathbb A^2\)-fibration over \(\mathbb C[x]\) in the standard
finite-type, flat, polynomial-fiber sense.

No restriction on the degree of \(R\) was used. The local calculation
does not need a specialization of Maubach's theorem; the explicit
finite inverse already supplies it.

## 2. The classical fibration theorem applies

An \(\mathbb A^2\)-fibration over a DVR containing \(\mathbb Q\)
is a polynomial algebra by Sathaye's theorem. Apply this to every
localization \(\mathbb C[x]_{(x-\alpha)}\). The generic localization
is polynomial by (2). Bass–Connell–Wright then globalizes the locally
polynomial algebra to a symmetric algebra; the relevant projective
module over the PID \(\mathbb C[x]\) is free. Consequently

\[
 A_\lambda\simeq\mathbb C[x]^{[2]}\simeq\mathbb C^{[3]}.
 \tag{3}
\]

The exact combined statement for a PID is explicitly recorded by
Janaki Raman Babu and Prosenjit Das in
[*Structure of A2-fibrations having fixed point free locally nilpotent derivations*](https://arxiv.org/pdf/2001.07632v5),
the discussion between Problem 4.6 and Theorem 4.7, printed p. 9.
Their Section 1 gives the definition of an affine fibration, and
Theorem 2.2 records the Bass–Connell–Wright globalization theorem.
The characteristic-zero and finite-presentation hypotheses are met
here. This use does not require a locally nilpotent derivation on
\(A_\lambda\) over \(\mathbb C[x]\).

The original references identified there are Avinash Sathaye,
*Polynomial ring in two variables over a DVR: a criterion*,
*Inventiones Mathematicae* **74** (1983), 159–168; and Hyman Bass,
Edwin H. Connell, and David L. Wright, *Locally polynomial algebras
are symmetric algebras*, *Inventiones Mathematicae* **38** (1976/77),
279–299, Theorem 4.4. The precise theorem scope here was checked in
the accessible Babu–Das text; the original papers were not reread
in full during this audit.

For orientation B, exchange \(x\) and \(y\) throughout the argument,
including the coefficient exponents. The same result holds over
\(\mathbb C[y]\). Unequal multiplicities cause no obstruction.

## 3. Why an original slice closes the argument

Now assume \(D\) is a locally nilpotent derivation on
\(S=\mathbb C[x,y,z,u]\) with \(D(F)=1\), and put \(K=\ker D\).
The slice theorem gives

\[
 S=K[F],\qquad K\simeq S/(F)\simeq A_0.
\]

Equation (3) makes \(K\simeq\mathbb C^{[3]}\). Choose generators
\(k_1,k_2,k_3\) realizing this polynomial presentation inside \(K\).
Then

\[
 S=\mathbb C[k_1,k_2,k_3,F],
\]

so \(F\) is a coordinate. There is no requirement that \(D(x)=0\):
the fibration argument was carried out on the quotient, and the slice
theorem transports its abstract polynomial presentation to \(K\).

For an original slice with arbitrary repeated-crossing coefficient,
the earlier integral residue argument supplies orientation A or B when
the axis restriction is constant. The nonconstant-axis branch was
already handled by an explicit inverse. Thus these steps together
settle original LND slices in the full two-factor monomial-coefficient
family, without a degree bound on the remainder.

A merely stable coordinate supplies a suitable slice derivation after
adjoining variables. It does not, by itself, supply one on \(S\).
Knowing \(S/(F-\lambda)\simeq\mathbb C^{[3]}\) for every
\(\lambda\) does not furnish the decomposition \(S=K[F]\) used
above. Therefore this shortcut does not prove coordinate descent for
the entire stable-coordinate family, and it does not decide the
Vénéreau candidate's coordinate status without the original-slice
hypothesis.

## 4. A concrete nonmonomial cubic coefficient to eliminate next

One useful extension of the coefficient analysis is

\[
 P=z(xy-1),\qquad F=Pu+H(x,y,z).
\]

In fact its reduced boundary already excludes stability for every
\(H\). Here is the short obstruction, included to make the proposed
next step concrete.

Let \(D=V(P)\subset\mathbb A^3\). It is the union of

\[
 D_1=\{xy=1\}\simeq\mathbb C^*\times\mathbb A^1,
 \qquad D_2=\{z=0\}\simeq\mathbb A^2,
\]

with intersection \(L\simeq\mathbb C^*\). Compact-support
Mayer–Vietoris gives

\[
 H_c^2(D;\mathbb Z)\simeq H_c^1(L;\mathbb Z)\simeq\mathbb Z,
\]

because the degree-one and degree-two compact-support groups of both
\(D_1\) and \(D_2\) vanish. The closed-open sequence in
\(\mathbb A^3\) then gives

\[
 H_c^3(\mathbb A^3\setminus D;\mathbb Z)\simeq\mathbb Z.
\]

Choose \(\lambda\) away from any constant values of \(H\) on the
two components and among the generic regular values of the nonconstant
restrictions. Then the reduced set
\(C=V(P,H-\lambda)\) is a union of noncompact affine curves, or
is empty. It has \(H_c^0(C)=0\). The closed complement in
\(X_\lambda=V(Pu+H-\lambda)\) is \(E=C\times\mathbb A^1\),
so \(H_c^2(E)=0\). Its open complement is
\(\mathbb A^3\setminus D\). Consequently the fiber's closed-open
sequence injects

\[
 \mathbb Z\simeq H_c^3(\mathbb A^3\setminus D)
 \lhook\joinrel\longrightarrow H_c^3(X_\lambda).
\]

This contradicts stable-coordinate fiber cohomology. The obstruction
does not depend on \(\deg H\), so it applies in particular to the
quartic linear-variable family with this cubic coefficient.

After such boundary-support exclusions, a distinct remaining target is
the nonconstant quadratic coefficient in
\(F=A(v)u^2+B(v)u+C(v)\), starting with \(A(v)=x\).
The quotient-fibration proof above relies on a unit linear coefficient
after localizing a base variable; a quadratic expression in \(u\)
does not automatically provide that structure.

## 5. The general support obstruction and the three-plane coefficient

**Support obstruction lemma.** Let \(P\ne0\) be a polynomial in
three complex variables and \(D=V(P)_{\mathrm{red}}\). If

\[
 H_c^2(D;\mathbb Z)\ne0,
\]

then \(Pu+H\) is not a stable coordinate for any polynomial \(H\).
In particular, it cannot be an original LND slice. Only the reduced
support of \(P\) matters, so the statement permits repeated factors.

To prove it, choose \(\lambda\) outside the finite set of values of
\(H\) on those irreducible components of \(D\) where it is constant.
Let \(p_{\mathrm{red}}\) be a square-free defining polynomial for
\(D\). Then \(p_{\mathrm{red}}\) and \(H-\lambda\) share no
irreducible factor. If their common zero set \(C\) is nonempty, they
form a regular sequence in the three-variable polynomial ring, so
\(C\) is of pure dimension one. Passing to its reduced support does
not change this conclusion. In particular, it has no isolated point
component. Every connected component of a complex affine curve is
noncompact, so \(H_c^0(C;\mathbb Z)=0\); the same holds if it is
empty.

For \(X_\lambda=V(Pu+H-\lambda)\), put
\(U=X_\lambda\cap\{P\ne0\}\) and
\(E=X_\lambda\setminus U\), with reduced topology. Then

\[
 U\simeq\mathbb A^3\setminus D,\qquad
 E\simeq C\times\mathbb A^1,\qquad
 H_c^2(E;\mathbb Z)=H_c^0(C;\mathbb Z)=0.
\]

The closed-open sequences for \(D\subset\mathbb A^3\) and for
\(E\subset X_\lambda\) give respectively

\[
 H_c^2(D;\mathbb Z)\simeq H_c^3(U;\mathbb Z),
 \qquad
 H_c^3(U;\mathbb Z)\lhook\joinrel\longrightarrow
 H_c^3(X_\lambda;\mathbb Z).
\]

The latter group would vanish for a stable-coordinate fiber. This is
the required contradiction. No smoothness of \(C\) and no Euler-only
argument is needed; the absence of compact connected components is
the exact input.

For the genuine cubic coefficient \(P=xyz\),

\[
 \mathbb A^3\setminus D=(\mathbb C^*)^3,
 \qquad H_c^3((\mathbb C^*)^3;\mathbb Z)=\mathbb Z.
\]

The last identity follows directly from compact-support Künneth:
each factor has \(H_c^1=\mathbb Z\), \(H_c^2=\mathbb Z\),
and only the degree pattern \((1,1,1)\) contributes to degree three.
Thus \(H_c^2(D)=\mathbb Z\), and \(xyzu+H(x,y,z)\) is excluded
for every \(H\). The same holds for
\(x^ry^sz^t u+H\) whenever \(r,s,t\ge1\).

For \(P=z(xy-1)\), the complement calculation independently confirms
Section 4. Put \(V=\mathbb A^2\setminus\{xy=1\}\). The
closed-open sequence with the hyperbola \(\mathbb C^*\) gives
\(H_c^1(V)=0\) and \(H_c^2(V)=\mathbb Z\). Hence

\[
 H_c^3(\mathbb C^*\times V;\mathbb Z)
 =H_c^1(\mathbb C^*;\mathbb Z)\otimes H_c^2(V;\mathbb Z)
 =\mathbb Z.
\]

Both coefficient supports are therefore excluded by the same general
lemma, and both are genuine cubic coefficient cases outside the
two-factor repeated-crossing family.
