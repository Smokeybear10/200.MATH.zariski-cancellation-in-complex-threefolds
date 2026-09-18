# Working recognition of the supplied absent-variable quartic configuration

Status: restricted working theorem with written proofs and finite algebra
controls. The general complex-threefold cancellation problem remains
unsolved. No historical novelty or human expert-review claim is made.

The remaining coefficient gates in both branches of
[synthesis189](weight-four-absent-variable-frontier-synthesis-pass189-working.md)
now have working proofs. Each surviving branch produces an invariant
coordinate in the original polynomial four-ring, with a polynomial
inverse. This advances the supplied configuration from a fraction-field
reduction to original-ring recognition.

## 1. Exact statement and retained hypotheses

Let
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E.
\tag{1}
\]
Assume the displayed variables are actual polynomial coordinates, the
global slice \(u\) is part of the given decomposition, and
\[
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf Y^4).
\tag{2}
\]
Here \(\deg_E f=\max\{j:E^jf\ne0\}\), and the weighted initial map
takes a formal coordinate of degree \(d\) to
\((E^df/d!)\tau^d\) in \(A[\tau]\).
Equation (2) specifies the entire kernel, not just a relation
satisfied by four leading coefficients.

**Working theorem.** Under (1)--(2), \(A\) is a polynomial
three-ring over \(\mathbb C\).

The proof uses the retained actual selected-derivation and chart
arguments184,187--189, not an assumption that a generic polynomial
parametrization has an original polynomial inverse. In particular the
[universal chart184](weight-four-universal-chart-potentials-pass184-working.md)
and the reductions summarized in189 supply
\[
\begin{gathered}
N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
a_E=EX\in L^*,\quad t=EY/a_E,\quad
\rho=(E^2W/2)/a_E^2,\quad (E^2Z/2)/a_E^2=t^4,\\
[L:\mathbb C(t,\rho)]<\infty,\quad
K=\ker_L\partial_\rho,\quad [K:\mathbb C(t)]<\infty,\quad
\ker_K\partial_t=\mathbb C,\\
Y=y+tX,\quad Z=z+(4t^3y+k)X+t^4X^2,\quad
W=w+\vartheta X+\rho X^2,\\
\mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(t,\rho,v)}=-a_E^3 .
\end{gathered}
\tag{3}
\]
The determinant is computed at fixed \(X\), and is independent
of \(X\). The coefficient partials are the exact ones on the finite
field \(L\). Neither \(K=\mathbb C(t)\) nor an original-ring unit
condition on \(a_E\) is assumed.

Put \(R=k_\rho\). These two alternatives are exhaustive.

## 2. Zero-R branch

The [zero-R reduction187](weight-four-absent-variable-zero-r-reduction-pass187-working.md)
excludes constant \(y\) and gives an affine line parameter with
\(Ny=\Gamma\in L^*\), a cubic \(\vartheta=P(y)\), and a nonzero
calibrated scalar identity.
The [cover-collapse189](weight-four-absent-zero-r-cover-collapse-pass189-working.md)
uses actual field return and curve degrees to prove
\(L=K(n)\), \(\rho=bn+c\), with \(b\in\mathbb C^*\) and \(c\in K\).

The new [field normal form190](weight-four-absent-zero-r-field-normal-form-pass190-working.md)
solves the remaining scalar coefficients. They initially yield
\(M_1=\alpha t+\beta\), \(W_0=Dn+g_0\), with
\(\alpha,\beta\in\mathbb C\), but only \(D,g_0\in K\).
An exact linear-pencil lemma and the coefficient identity
\(g_2'=-6t^2D'\) then force \(D\in\mathbb C\).
It would be incorrect to infer this from scalarity in \(y\) alone.

Those are precisely the hypotheses of the independent
[coordinate-return190](weight-four-absent-zero-r-coordinate-return-pass190-working.md).
They give
\[
\begin{gathered}
A_0(X,Y)=bX^2+\beta X+\alpha Y+D\in\mathbb C[X,Y],\\
I=W-A_0(X,Y)Z-Q_0(X,Y)=g_0,\qquad Q_0\in\mathbb C[X,Y],\\
W=I+A_0(X,Y)Z+Q_0(X,Y),\qquad B=\mathbb C[X,Y,Z,I],\qquad EI=0.
\end{gathered}
\tag{4}
\]
The correction \(Q_0\) has both an explicit coefficient formula and a
separate derivation by coefficient transport. In the latter proof,
subtracting \(A_0Z+g_0\) literally removes \(n\); the exact derivation
\(\partial_t-X\partial_y\), followed by \(y=Y-tX\), forces every
remaining coefficient to be complex. This is a polynomial shear
with its displayed inverse, not descent asserted from field rationality.

## 3. Nonzero-R branch

The [constant-projection exclusion188](weight-four-absent-variable-constant-projection-exclusion-pass188-working.md)
excludes constant \(y\).
The [rigidity188](weight-four-absent-variable-nonzero-r-rigidity-pass188-working.md)
and [quartic-graph reduction189](weight-four-absent-nonzero-r-quartic-graph-reduction-pass189-working.md)
then give affine \(y\), a pure quartic graph, and
\(R=1/(\alpha t+\beta)\), \(n=cR^2\rho+n_0\), with
\(\alpha,\beta,c\in\mathbb C\) and \(n_0\in K\).
The proof excludes the other graph possibilities over the exact
algebraic field, including the nonrational local-series alternatives.

The new [nonzero-R recognition190](weight-four-absent-nonzero-r-coordinate-recognition-pass190-working.md)
introduces a coefficient-field element \(h\) with \(h_\rho\ne0\).
The scalar determinant makes \(\rho\) affine in \(h\).
Its positive coefficients then give \(T''=0\) and
\((5\alpha t+\beta)T'+\alpha T=0\), forcing \(\alpha=0\).
Thus \(r=R\) and \(T=r\rho_h\) are nonzero complex constants.
Actual field return first removes a possible residual field
extension and then, using a polynomial-pencil pole argument, forces
the last slope \(b=z_{0,h}\) to be complex.

The actual \(h\)-coefficients now allow two polynomial substitutions:
\[
\begin{aligned}
B_0(X)&=b+TX,& \lambda_0(X)&=X/r-c,\\
J&=W-\lambda_0(X)Z,&
I&=Z-B_0(X)J-Q_0(X,Y)=g_0,\\
Z&=I+Q_0(X,Y)+B_0(X)J,&
W&=J+\lambda_0(X)Z .
\end{aligned}
\tag{5}
\]
Here \(B_0,\lambda_0\in\mathbb C[X]\) and
\(Q_0\in\mathbb C[X,Y]\).
The correction is justified by the full \(X\)-independent determinant,
retaining the factors \(\rho_h=T/r\) and \(\Gamma=Ny\).
It is not deduced just from the determinant at \(X=0\).
Coefficient transport again forces complex coefficients, and the
two displayed inverse orders prove \(B=\mathbb C[X,Y,I,J]\).
The equality \(I=g_0\in K\) proves \(EI=0\).

## 4. Recognition endpoint and verification scope

Both branches supply an actual invariant ambient coordinate \(I\).
The original nonzero derivation \(E\) is therefore
\(\mathbb C[I]\)-linear on a polynomial three-ring over
\(\mathbb C[I]\).
Its kernel \(A\) is regular: \(A\simeq B/(u)\), and \(Eu=1\)
expresses one as a polynomial combination of the original partial
derivatives of \(u\), so the hypersurface \(u=0\) is smooth.
The exact hypotheses of
[Bhatwadekar--Gupta--Lokhande Theorem 3.5](https://arxiv.org/html/1501.01438v1)
are now supplied, and it gives
\[
A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]}.
\tag{6}
\]

The proof has separate saved-source AI reconstructions. The finite
symbolic controls check the residual identities, the derivative
coefficients used in the field arguments, and polynomial inverse
orders. They do not prove exact field return, the pencil lemmas,
the retained184--189 inputs, or the published recognition theorem
in a proof assistant. Execution evidence belongs in the separate
verification record, not in the statement of the theorem.

## 5. Remaining obligations toward the full goal

This result is restricted to the supplied actual frame (1)--(2).
It does not establish that every globally sliced derivation enters
this frame, even after a polynomial change of variables.
The one-dimensional split bad-coefficient form
\(XYZ+X^4+Y^4\), positive quadratic bad-variable rank, height-two
initial kernels, higher possible minimum time profiles, and the
arbitrary-entry problem remain separate obligations.

An actual example of this absent-variable configuration would test
nonvacuity, but is not assumed in this proof. The older actual
example187 belongs to the different common-factor relation.
No minimality assertion about time profiles is made here.

The professor has not confirmed the interpretation of the original
email as complex-threefold cancellation. The full goal remains
active and unsolved. No external contact, submission, public
posting, new automation, historical novelty clearance, human
expert review, or formal certification is asserted.
