# Algebraic dependence of the speeds of \(n-1\) good coordinates

## 1. Actual statement

Let \(n\ge2\). Suppose an actual polynomial \(n\)-ring has a locally
nilpotent derivation with an actual global slice, and that \(n-1\) members
of the supplied polynomial coordinate frame are affine along its orbits:
\[
 \begin{gathered}
 B=\mathbb C[x_1,\ldots,x_{n-1},z],\qquad
 E\in\operatorname{LND}_{\mathbb C}(B),\qquad E(u)=1,\\
 A=\ker E,\qquad B=A[u],\qquad E^2(x_i)=0\quad(1\le i<n).
 \end{gathered}
 \qquad
 \boxed{\operatorname{trdeg}_{\mathbb C}
             \mathbb C[E(x_1),\ldots,E(x_{n-1})]\le n-2.}
 \tag{1}
\]
The displayed polynomial extension is the actual slice presentation.
Neither \(u\) nor any invariant is assumed to be an ambient coordinate.
There is no hypothesis on the \(E\)-degree of \(z\).

In particular, the three speeds in a sliced three-good-coordinate frame
on \(\mathbb A^4_{\mathbb C}\) are algebraically dependent, even if the
remaining acceleration is nonconstant or its time degree exceeds two.
This is a structural restriction, not kernel recognition or unrestricted
cancellation. It does not prove that an arbitrary sliced action has
\(n-1\) good coordinates.

The constant-acceleration rank bound in
[pass 87](constant-acceleration-three-good-frame-pass87.md), Section 1,
had a narrower hypothesis. The decisive nilpotence mechanism below is
the retained [highest-vertical exclusion69](vertical-top-exclusion-pass69.md);
its actual-ring degeneration is reproduced rather than replaced by an
assumption about a localized or rational derivation.

## 2. Assume independent speeds and form the differential basis

Put \(m=n-1\), \(a_i=E(x_i)\), and \(b_i=x_i-a_i u\).
Then \(a_i,b_i\in A\), and
\[
 x_i=b_i+a_i u,\qquad
 a=(a_1,\ldots,a_m)^{\mathsf T},\qquad
 b=(b_1,\ldots,b_m)^{\mathsf T}.
 \tag{2}
\]
Assume for contradiction that the \(a_i\) are algebraically independent.

The algebra \(A\) is finitely generated: it is isomorphic to \(B/(u)\)
by evaluation at \(u=0\) in \(A[u]\). Thus \(F=\operatorname{Frac}A\)
is a finitely generated field of transcendence degree \(m\).
The extension
\(\mathbb C(a_1,\ldots,a_m)\subset F\) is finite algebraic and, in
characteristic zero, separable. In particular the coordinate derivatives
\(\partial_i=\partial/\partial a_i\) extend uniquely to \(F\), and
\(da_1,\ldots,da_m\) form a basis of \(\Omega_{F/\mathbb C}\).
Adjoining \(u\) gives the differential basis
\(da_1,\ldots,da_m,du\) of \(F(u)=\operatorname{Frac}B\).

These assertions concern a finite field extension. They do not assert
\(F=\mathbb C(a_1,\ldots,a_m)\), polynomiality of \(A\), or regularity
of these derivatives on \(A\).

## 3. Actual volume makes the rational determinant constant in \(u\)

The original coordinate volume is a nonzero rational multiple of this
differential basis. Since every original coordinate belongs to \(A[u]\),
the multiple is polynomial in \(u\) over \(F\):
\[
 dx_1\wedge\cdots\wedge dx_m\wedge dz
   =J(u)\,da_1\wedge\cdots\wedge da_m\wedge du,\qquad
 J(u)\in F[u]\setminus\{0\},\qquad J(u)=J_0\in F^*.
 \tag{3}
\]
Here is the justification for the final equality.

For an independent time parameter \(t\), the original polynomial flow
\(\exp(tE)\) is an automorphism of \(B[t]\), with polynomial inverse
\(\exp(-tE)\). Its Jacobian determinant in the original \(n\) coordinates
is a unit of \(B[t]\), hence a nonzero complex constant. Evaluation at
\(t=0\) makes that constant \(1\). Thus the original volume is invariant.
The flow fixes \(F\) and sends \(u\) to \(u+t\). In relative differentials
over \(\mathbb C(t)\), it fixes \(da_i\) and \(du\). Applying the flow
to the volume equality gives \(J(u+t)=J(u)\). Characteristic zero,
or differentiation in \(t\) at zero, implies \(J(u)\in F\).
It is nonzero because both displayed top-degree differential forms
are bases over \(F(u)\).

No assertion \(J_0\in\mathbb C^*\) is made. The flow Jacobian in the
original coordinates is constant, while this change-of-differential-basis
coefficient is only known to lie in \(F^*\).

## 4. The actual last-coordinate partial has an impossible top

Let \(D b=(\partial_j b_i)_{1\le i,j\le m}\) and \(M=uI_m+D b\).
The Jacobian matrix of the actual coordinates relative to
\((a_1,\ldots,a_m,u)\) has top block \((M\mid a)\).
Its bottom row consists of the corresponding derivatives of \(z\);
their precise degrees will not be needed.

Use the actual polynomial coordinate partial \(T=\partial_z\).
It is locally nilpotent on \(B\), kills each \(x_i\), and takes \(z\)
to \(1\). Solving these exact linear equations by cofactors gives
\[
 T(a)=-\frac{\operatorname{adj}(M)a}{J_0},\qquad
 T(u)=\frac{\det(M)}{J_0}.
 \tag{4}
\]
These formulas are identities in \(F(u)\). The adjugate formula does
not require inverting \(\det(M)\) or choosing a principal open set.
Its numerator has degree at most \(m-1\) in \(u\); the second numerator
is monic of degree \(m\).

For every \(f\in F\), the differential-basis property gives
\(T(f)=\sum_i(\partial_i f)T(a_i)\). Thus its degree in \(u\) is at
most \(m-1\). In particular, for \(f\in A\), this expression also lies
in the actual ring \(B=A[u]\), because \(T\) is the original
polynomial partial. Uniqueness of coefficients in \(F[u]\) therefore
puts all of its coefficients in \(A\), with the same degree bound.
Likewise all coefficients of \(T(u)\) belong to \(A\). Consequently
\[
 \begin{gathered}
 T(f)=\sum_{j=0}^{m-1}f_j u^j\quad(f\in A,\ f_j\in A),\\
 T(u)=\sum_{j=0}^{m}h_j u^j,\qquad
 h_j\in A,\qquad h_m=J_0^{-1}\ne0,\\
 \operatorname{ad}_E^{m+1}T=0,\qquad
 \operatorname{ad}_E^m T=m!J_0^{-1}E\ne0 .
 \end{gathered}
 \tag{5}
\]
The commutator formulas follow by applying them to \(A\) and \(u\),
which generate \(B\). In particular \(J_0^{-1}\in A\) follows from
the actual coefficient of \(T(u)\); it was not obtained by declaring
an arbitrary rational denominator invertible on \(A\).

Equation (5) already contradicts the exact highest-vertical lemma69.
For completeness, the full degeneration needed in this instance
follows next.

## 5. The leading derivation is genuinely locally nilpotent

Adjoin an indeterminate \(\varepsilon\) killed by \(T\).
In \(B[\varepsilon,\varepsilon^{-1}]\), let \(\Phi\) fix \(A\) and
\(\varepsilon\), and send \(u\) to \(u/\varepsilon\).
The derivation
\[
 \begin{gathered}
 T_\varepsilon=\varepsilon^{m-1}\Phi T\Phi^{-1},\\
 T_\varepsilon(f)=
       \sum_{j=0}^{m-1}f_j u^j\varepsilon^{m-1-j}\quad(f\in A),\\
 T_\varepsilon(u)=
       \sum_{j=0}^{m}h_j u^j\varepsilon^{m-j},\qquad
 T_\varepsilon(\varepsilon)=0
 \end{gathered}
 \tag{6}
\]
is locally nilpotent on the Laurent ring. Indeed it is a conjugate
of the original LND multiplied by an invariant unit.

The displayed nonnegative exponents show that it preserves
\(B[\varepsilon]\). Its restriction is locally nilpotent: vanishing
of an iterate in the Laurent ring implies vanishing in this injected
subring. The ideal \((\varepsilon)\) is stable, so specialization gives
an LND \(T_0\) of the original domain \(B=A[u]\), with
\[
 T_0(u)=h_m u^m=J_0^{-1}u^m\ne0.
 \tag{7}
\]
This also covers \(m=1\); no positive-degree assumption on the scaling
factor is needed.

For an LND \(D\) on a characteristic-zero domain, its degree on
nonzero products is additive. If \(D(f)\ne0\), that derivative has
\(D\)-degree one less than \(f\). Hence \(f\mid D(f)\) forces
\(D(f)=0\): otherwise the product expression would have degree at
least that of \(f\). Apply this to \(D=T_0\) and \(f=u\).
Since \(m\ge1\), equation (7) is a nonzero multiple of \(u\), which
is impossible. This contradicts the assumed algebraic independence
and proves (1).

## 6. Scope for the four-dimensional investigation

For \(n=4\), any actual sliced frame with three good coordinates has
good-speed transcendence degree \(0\), \(1\), or \(2\). The bound is
independent of the time degree of the last coordinate, and in
particular applies to the nonconstant-acceleration first profile in
[the pass-124 frontier](unrestricted-entry-frontier-pass124.md).

The degree-zero speed-field case is recognized directly. Over
\(\mathbb C\) all the speeds are then constants. If one is nonzero,
the corresponding actual coordinate divided by its speed is an
ambient coordinate slice, so the kernel is a polynomial three-ring.
If all are zero, the slice equation reads
\(1=E(z)\partial_z u\), making \(E(z)\) a complex unit and again
giving \(\ker E=\mathbb C[x_1,x_2,x_3]\).
Thus a hypothetical nonpolynomial kernel in this supplied class
can have only speed-field transcendence degree one or two.

Neither remaining speed field is identified with a polynomial
subring or with an actual invariant coordinate system by this proof.
The original polynomial inverse and volume hypotheses cannot be
replaced by a rational formal matrix model. No conclusion that
nonconstant acceleration can be made constant, or that every
sliced derivation has such a frame, has been obtained.

The initial determinant calculation under independent speeds would
also give coefficient identities in the quadratic-time case. Their
antecedent has now been excluded, so they are not retained as a
surviving Euler-equation branch or used to assume a polynomial
formula for the acceleration.

## 7. Proof and verification boundaries

The cofactor calculation, finite-separable differential argument,
and actual-ring degree extraction were independently reconstructed.
The Laurent-parameter degeneration is the retained mechanism69,
reproduced above in full. The narrower actual constant-acceleration
comparison87 and that retained lemma were freshly read through EOF.
No new primary classification theorem, assumption that the slice is
a coordinate, or cancellation conclusion enters the proof.

This is a written AI research deduction, not human expert review,
formal proof verification, or a cleared historical novelty claim.
No numerical example can certify the arbitrary-ring quantifiers.
No file through pass124 or live index is changed by this note.

