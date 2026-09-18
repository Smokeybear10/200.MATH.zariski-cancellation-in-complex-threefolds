# A unit joint-curve row gives an actual affine-modification presentation

## 1. Exact supplied-frame hypotheses

Suppose that the actual polynomial four-ring has a sliced derivation and
a joint polynomial curve parameter as follows:
\[
 \begin{gathered}
 B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad A=\ker E,\qquad Eu=1,\\
 Ex_i=f_i(p),\qquad Ez=c,\qquad E c=q=g(p),\qquad Ep=0,\\
 p\in B\setminus\mathbb C,\quad f_i,g\in\mathbb C[t],\quad
 \gcd(f_1,f_2,f_3)=1,\quad
 \operatorname{trdeg}_{\mathbb C}\mathbb C[f_1(p),f_2(p),f_3(p)]=1,\\
 \alpha=p_z\ne0.
 \end{gathered}
 \tag{1}
\]
Here and below univariate functions and their derivatives are evaluated
at \(p\) when used as elements of \(B\). The parameter is polynomial,
not assumed to be a coordinate. The unit row is a genuine univariate
Bézout condition, not merely a gcd condition in a polynomial plane.

The [joint-curve proof126](three-good-joint-curve-bound-pass126.md)
provides this setup for the remaining unit-speed, joint-rank-one case.
It separately recognizes a nonunit speed row, or \(p_z=0\).
This note assumes the specific dependence \(q=g(p)\); it does not
replace that condition by arbitrary \(q\) in an invariant plane.

## 2. The commutator and a univariate split basis

Put \(T=\partial_z\), \(Q=[E,T]\), and \(\delta=c_z\).
The exact determinant and content argument in Sections 6--7 of the
joint-curve proof gives
\[
 \begin{gathered}
 Q=-\alpha f'(p)\cdot\partial_{\rm good}-\delta\partial_z,
 \qquad Q\in\operatorname{LND}(B),\qquad [E,Q]=0,\\
 Ep=Qp=E\alpha=Q\alpha=0,\qquad
 Qc=-\frac{g'(p)}2\alpha,\qquad Q^2x_i=0.
 \end{gathered}
 \tag{2}
\]
In particular \(N=Q|_A\) is defined. Its nonvanishing will follow
from an explicit element of \(A\), rather than from nonvanishing of
\(Q\) on \(B\) alone.

The rows \(f,f'\) are independent over \(\mathbb C(t)\).
Otherwise their nonzero component ratios have zero derivative and
are complex constants. The unit gcd of the components of \(f\)
would then force every component to be constant, contradicting (1).
Divide \(f\times f'\) by the gcd of its entries to obtain a
unimodular row \(n\in\mathbb C[t]^3\). Thus \(nf=nf'=0\).

All the following module choices are made over the PID \(\mathbb C[t]\).
The kernel of the unit row \(n\) is free of rank two. A row with
value one on the unimodular column \(f\) splits off its span inside
this kernel, so choose a second basis column \(V\). Choose \(U_0\)
with \(nU_0=1\). Then \(M=[f,V,U_0]\) is an invertible matrix over
\(\mathbb C[t]\). Write its inverse rows as \(\lambda,\mu,n\), and
define actual elements by substitution:
\[
 \begin{gathered}
 \begin{pmatrix}\sigma\\Y\\h\end{pmatrix}
       =M(p)^{-1}x_{\rm good},\qquad
 x_{\rm good}=f(p)\sigma+V(p)Y+U_0(p)h,\\
 E\sigma=1,\quad EY=Eh=0,\qquad
 f'=\ell f+\beta V,\quad
 \ell=\lambda f',\quad\beta=\mu f'\in\mathbb C[t]\setminus\{0\},\\
 Q\sigma=-\alpha\ell(p),\qquad NY=QY=-\alpha\beta(p)\ne0,
 \qquad Qh=0.
 \end{gathered}
 \tag{3}
\]
The decomposition of \(f'\) has no \(U_0\) term because \(nf'=0\).
The coefficient \(\beta\) is nonzero by the independence of
\(f,f'\). This proves that \(N\) is a nonzero intrinsic LND.
No ambient automorphism induced by \(M(p)\) is asserted.

## 3. The actual plane and the two-generator kernel

Apply the retained
[intrinsic quotient-surface theorem](intrinsic-quotient-surface-pass.md)
to this particular nonzero \(N\) on \(A\). Its hypotheses are supplied
by \(A[u]\simeq\mathbb C^{[4]}\): the smooth contractible threefold
\(\operatorname{Spec}A\) is dominated by an affine three-plane, as
proved in the retained theorem. It follows that
\[
 \begin{gathered}
 S=\ker N\simeq\mathbb C^{[2]},\qquad S\longrightarrow A
       \text{ is faithfully flat},\qquad p,\alpha,h\in S,\\
 B=S[\sigma,Y,z],\qquad
 A=S[Y,d_0],\qquad d_0=z-\sigma c+\frac q2\sigma^2.
 \end{gathered}
 \tag{4}
\]
For the equality for \(B\), its displayed generators belong to \(B\),
whereas (3) expresses all four original coordinates in their algebra:
the coefficients are in \(\mathbb C[p]\subset S\), and \(h\in S\).

For the equality for \(A\), the actual slice theorem gives
\(B=A[\sigma]\). Its evaluation at \(\sigma=0\) is the finite
Taylor homomorphism
\(\pi_\sigma(b)=\sum_{j\ge0}(-\sigma)^jE^j(b)/j!\).
It fixes \(S,Y\), kills \(\sigma\), and maps \(z\) to \(d_0\).
Applying it to the actual algebra equality for \(B\) proves (4).
These are equalities of subalgebras, not free polynomial presentations.

The source-dependent plane and flatness theorem is used exactly as
in [the intrinsic-speed proof125, Section 6](three-good-intrinsic-speed-quotient-pass125.md).
The construction otherwise extends the split-module argument of
[the constant-acceleration curve note89](constant-acceleration-curve-speed-pass89.md)
to the joint dependence \(q=g(p)\).

## 4. Generic polynomiality and the residual first derivative

Let \(K=\operatorname{Frac}S\). By (3), \(b=NY=-\alpha\beta(p)\)
is a nonzero element of \(S\), and \(N^2Y=0\). After inverting
\(S\setminus\{0\}\), the element \(Y/b\) is a slice for \(N\).
The local slice theorem and exact invariant localization give
\(A_K=K[Y]\). In particular \(Y\) is transcendental over \(K\).

One also has a useful, but only generic, slope identity. Define
\(k=c-q\sigma\in A\). From (2)--(3),
\[
 \begin{gathered}
 Nk=\alpha(q\ell-g'/2),\qquad
 k=\frac{g'/2-q\ell}{\beta}\,Y+\nu,\qquad \nu\in K,\\
 A_K=K[Y],\qquad
 d_0\in K[Y].
 \end{gathered}
 \tag{5}
\]
Indeed the difference in the middle expression is killed by \(N\)
and lies in \(A_K\), whose invariant ring is \(K\).
The slope belongs to \(\mathbb C(p)\), but no assertion that it
or \(\nu\) lies in \(S\) is needed or proved.

## 5. A primitive relation and its exact saturation

Write \(d_0=F(Y)/a\), where \(0\ne a\in S\) and \(F\in S[Y]\),
clearing the finitely many coefficients in (5). Cancel their common
content so that the gcd of \(a\) and all coefficients of \(F\) is one.
With independent variables \(y,t\), the resulting actual presentation is
\[
 \begin{gathered}
 A\simeq S[y,t]/\bigl(a t-F(y)\bigr)
       =S[Y,F(Y)/a]\subset S[Y]_a,\\
 y\longmapsto Y,\qquad t\longmapsto d_0,\qquad
 a\,N(d_0)=b\,F'(Y),\quad b=-\alpha\beta(p),\\
 a\in S^*\quad\Longrightarrow\quad
 A=S[Y]\simeq\mathbb C^{[3]}.
 \end{gathered}
 \tag{6}
\]
Here is the saturation argument. The ring \(S[y]\) is a UFD.
The polynomial \(L=a t-F(y)\) is primitive over it: every prime
dividing the coefficient \(a\) in \(S[y]\) comes from
\(S\), and none divides all coefficients of \(F\). It is linear
and irreducible over \(\operatorname{Frac}(S[y])\), so Gauss's lemma
makes it irreducible and prime in \(S[y,t]\).

The surjection \(S[y,t]\to A\) follows from (4). After localizing
at the nonzero elements of \(S\), its kernel is precisely \((L)\),
because \(A_K=K[Y]\). If \(H\) belongs to the unlocalized kernel,
clear the finitely many \(S\)-denominators in the generic divisibility
to obtain \(sH=LR\) with \(0\ne s\in S\) and \(R\in S[y,t]\).
The prime \(L\) does not divide \(s\), since its degree in \(t\)
is one. Therefore \(L\mid H\) already in \(S[y,t]\).
This proves the asserted kernel without assuming the desired
presentation is torsion-free or a polynomial ring.

For a nonunit \(a\), (6) is the affine modification of the actual
three-ring \(S[Y]\) obtained by adjoining \(F(Y)/a\), with center
ideal \((a,F(Y))\). This description does not assert freeness of
the intrinsic action, a slice for it, or triviality of every fiber.
It does not show that the denominator can be made a unit.

## 6. A precise base-field boundary

The nonzero original derivative \(p_z\) implies that \(p\) has positive
degree in the original \(z\). Thus it is transcendental over
\(\mathbb C(x_1,x_2,x_3)\), and \(p,x_1,x_2,x_3\) are algebraically
independent. Over \(\mathbb C(p)\), the nonzero linear form
\(h=n(p)\cdot x_{\rm good}\) is consequently transcendental. Hence
\[
 \operatorname{trdeg}_{\mathbb C}\mathbb C[p,h]=2,
 \qquad \mathbb C(p,h)\subset K
       \text{ is a finite algebraic field extension}.
 \tag{7}
\]
The finiteness uses that \(K\) is a finitely generated field and
the two fields have the same transcendence degree. Neither
\(S=\mathbb C[p,h]\) nor equality of their fraction fields follows.
Likewise the variable-coefficient split basis (3) does not give an
ambient coordinate system in the original four-ring.

This identifies an actual affine-modification frontier in the supplied
unit joint-curve branch. It is not recognition of that whole branch,
nor an arbitrary-frame entry theorem. The constant-acceleration
specialization retains its separate recognition results, but they
are not transferred to variable \(g(p)\) by the presentation alone.

The complete joint-curve126, curve89, and intrinsic quotient-surface
proofs were read for this argument. The plane/flatness result retains
its stated Kaliman--Saveliev and miracle-flatness dependencies; no
fresh primary-source proof audit, numerical execution, or change to
an earlier file accompanies this note.
