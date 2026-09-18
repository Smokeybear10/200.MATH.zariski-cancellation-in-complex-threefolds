# The genuine quadratic frame has no simple common speed zero

Under the full independent-defect quadratic-frame hypotheses, the
two bad-coordinate speeds cannot have a common zero at which their
Jacobian on the invariant plane is invertible. This excludes the
entire local sector in which those speeds generate the maximal
ideal, without any assumption on the intrinsic second-image ideal.

The argument uses the actual good-column graph equations. It does
not apply to arbitrary quadratic generators over an invariant base.
It leaves ramified isolated zeros, common divisor components, and
the unrestricted frame-selection problem open.

## 1. Hypotheses and statement

Retain the full actual setup of
[the generic bad-pair theorem](generic-bad-pair-pass44.md):
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad Es_*=1,
\]
\[
C=\mathbb C[a,b]\subseteq A,\quad L=\operatorname{Frac}C,
\quad B_L=L[X,Y],\quad X=x_3,\quad Y=x_4,
\]
\[
E=f\partial_X+g\partial_Y,\qquad
f,g\in C,\qquad \operatorname{trdeg}_{\mathbb C}\mathbb C(f,g)=2.
\tag{1}
\]
The original polynomial coordinates satisfy the supplied adjoint
bounds of that theorem. The invariant plane and the equality
\(B\cap L=C\) are inherited actual conclusions, not assumptions
about four arbitrary generators.

The two uniquely extended field partials \(\partial_f,\partial_g\)
commute on the finite separable extension \(L/\mathbb C(f,g)\).
Put \(\mathscr H=f\partial_f+g\partial_g\). The actual graph has
\[
h_i=E^2x_i\in C,\quad k_i,\ell_i\in L,\qquad
\mathscr Hh_i=2h_i,\quad \mathscr Hk_i=k_i,
\]
\[
x_i=\frac14(X,Y)\operatorname{Hess}_{f,g}(h_i)
                  \binom X Y
       +(\nabla_{f,g}k_i)\binom X Y+\ell_i,\qquad i=1,2.
\tag{2}
\]
These precise Hessian, gradient, and weight equations are the
relevant consequences of the true ambient good partials.

For a closed point \(P\) of \(\operatorname{Spec}C\), write
\(R=C_{\mathfrak m_P}\), \(\mathfrak m=\mathfrak m_PR\), and
\(\mathcal B=B_R\).

**Theorem.** If \(f(P)=g(P)=0\), then
\[
\boxed{\det\frac{\partial(f,g)}{\partial(a,b)}(P)=0.}
\tag{3}
\]
Equivalently, \((f,g)R=\mathfrak m\) is impossible at a
common zero in the actual setup (1)--(2).

No hypothesis about the intrinsic image ideal \(J\), first
correction jets, or the multiplicity of the primitive plinth
is added.

## 2. Regular Euler eigenfunctions at a simple zero

Suppose temporarily that
\[
f,g\in\mathfrak m,\qquad (f,g)R=\mathfrak m.
\tag{4}
\]
Their initial linear forms are a basis of
\(\mathfrak m/\mathfrak m^2\). Thus the ordinary two-by-two
Jacobian in the actual invariant coordinates \(a,b\) has
unit determinant in \(R\). Inverting that matrix expresses
\(\partial_f,\partial_g\) as \(R\)-linear combinations of
\(\partial_a,\partial_b\). These derivations preserve \(R\)
and have the prescribed values on \(f,g\), so they agree
with the unique field extensions used in (2).

In particular, \(\mathscr H\) preserves \(R\) and every
\(\mathfrak m^n\). On
\[
\operatorname{gr}_{\mathfrak m}R
  =\mathbb C[\operatorname{in}(f),\operatorname{in}(g)],
\qquad
\operatorname{gr}_{\mathfrak m}^n(\mathscr H)=n\operatorname{Id}.
\tag{5}
\]
The induced derivation multiplies every homogeneous
degree-\(n\) element by \(n\), because
\(\mathscr Hf=f\) and \(\mathscr Hg=g\).

Here the graded-ring description can be checked directly:
the initial linear terms of \(f,g\) are an invertible
linear change from \(a-a(P),b-b(P)\), and hence their
degree-\(n\) monomials are a basis of the degree-\(n\)
initial forms. There is no assumption that \(f,g\)
generate \(C\) globally.

**Eigenfunction lemma.** If \(r\in R\) and
\(\mathscr Hr=d r\), for an integer \(d\ge0\), then
\[
r=\sum_{i+j=d}c_{ij}f^ig^j,\qquad c_{ij}\in\mathbb C.
\tag{6}
\]
The zero element is included.

For a nonzero \(r\), its order \(n\) at \(P\) is finite:
write it as a polynomial numerator divided by a
denominator not vanishing at \(P\). Comparing the initial
form in its eigenvalue equation and using (5) gives
\((n-d)\operatorname{in}(r)=0\), so \(n=d\).
Choose the homogeneous polynomial \(q(f,g)\) of degree
\(d\) having that initial form. Then
\[
\mathscr H(r-q)=d(r-q),\qquad r-q\in\mathfrak m^{d+1}.
\]
If this difference were nonzero, the same finite-order
argument would give it order exactly \(d\), a contradiction.
Thus \(r=q\), proving (6).

This is an exact local-germ argument, not a finite jet
approximation. One can equivalently work in
\(\widehat R=\mathbb C[[f,g]]\), where Euler's equation
kills all coefficients outside degree \(d\), but completion
or a convergence assertion is not required.

## 3. The actual velocities make the linear terms regular

Apply (6) with \(d=2\) to the actual \(h_i\in R\).
Each \(h_i\) is a homogeneous quadratic polynomial in
\(f,g\) with complex coefficients. Therefore
\[
\nabla_{f,g}h_i\in R^2,\qquad
\operatorname{Hess}_{f,g}(h_i)\in\operatorname{Mat}_2(\mathbb C).
\tag{7}
\]
The \(k_i\) were only known to be rational, so applying
the lemma to them at this point would be unjustified.

Instead differentiate the actual graph (2) by \(E\).
This action kills its base-field coefficients. Euler's
identities give
\(\operatorname{Hess}(h_i)(f,g)^{\mathsf t}=\nabla h_i\)
and \((\nabla k_i)(f,g)^{\mathsf t}=k_i\), hence
\[
Ex_i=\frac12(\nabla_{f,g}h_i)\binom X Y+k_i.
\tag{8}
\]
Both \(Ex_i\) and the displayed linear term belong to
\(\mathcal B\). Thus \(k_i\in\mathcal B\cap L=R\).
The intersection follows from \(B\cap L=C\) by clearing
the inverted invariant denominators.

Now apply (6) with \(d=1\). Each \(k_i\) is a complex
linear combination of \(f,g\), so \(\nabla k_i\) has
constant complex entries. Subtracting the quadratic
and linear terms in (2) from the actual \(x_i\) gives
\(\ell_i\in\mathcal B\cap L=R\). Consequently
\[
x_1,x_2\in R[X,Y],\qquad
\boxed{\mathcal B=R[X,Y].}
\tag{9}
\]
The second conclusion uses that the original four
coordinates generate \(\mathcal B\) over \(R\).
Algebraic independence of \(X,Y\) is inherited from
the actual generic ring, so this is a polynomial
extension, not a quotient presentation.

## 4. The supplied slice gives the contradiction

On the whole ring in (9),
\[
E(\mathcal B)\subseteq(f,g)R[X,Y].
\]
The actual supplied slice \(s_*\) remains in \(\mathcal B\),
and \(Es_*=1\). Evaluating the resulting polynomial
ideal identity at \(X=Y=0\) yields
\[
1\in(f,g)R=\mathfrak m,
\tag{10}
\]
which is impossible. This proves (3).

The last step does not construct a new slice or assume
that the original slice was affine in the generic pair.
The original arbitrary slice is used only after full
local polynomial equality (9) has been proved.

## 5. Exact consequences and the remaining zero schemes

The theorem says that every common speed zero is a
critical point of the speed map on the actual invariant
plane. Equivalently, by the complex Nullstellensatz,
\[
\det\frac{\partial(f,g)}{\partial(a,b)}
\in\sqrt{(f,g)C}.
\tag{11}
\]
This is a necessary ideal constraint, not a converse
realization of a frame.

If a common zero is isolated, its local zero scheme
cannot be reduced. Indeed, a reduced zero-dimensional
local quotient of \(R\) is its residue field
\(\mathbb C\), which would imply \((f,g)R=\mathfrak m\),
already excluded. The theorem does not say that
positive-dimensional common-zero components are
nonreduced, nor does it eliminate nonreduced isolated
zeros.

The parameter-speed sector of
[the conditional leading-image bound](slice-leading-image-obstruction-pass55.md)
assumed \((f,g)R=\mathfrak m\) in addition to conditions
on \(J\) and the first jets. Under the full inherited
graph assumptions, that entire sector is now excluded.
Its earlier lower-bound implication remains logically
valid but no longer describes a possible surviving
full-frame point. The distinct reduced condition
\(JR=\mathfrak m\) does not imply the speed-ideal
condition and is not excluded by this theorem.

## 6. Why ramified speed coordinates are different

Correct Euler weights and independent polynomial
accelerations alone do not allow (6) to be used at a
ramified zero. A base-only control is
\[
f=a^2,\quad g=b^2,\qquad
\mathscr H=\tfrac12(a\partial_a+b\partial_b),\qquad
h_1=a^4,\quad h_2=a^3b,\quad k=ab.
\tag{12}
\]
Then \(\mathscr Hf=f,\mathscr Hg=g\),
\(\mathscr Hh_i=2h_i\), \(\mathscr Hk=k\), and
\(\det\operatorname{Jac}_{a,b}(h_1,h_2)=4a^6\ne0\).
The isolated speed zero at the origin is nonreduced.
The actual field derivatives are
\(\partial_f=(2a)^{-1}\partial_a\) and
\(\partial_g=(2b)^{-1}\partial_b\), so
\[
\partial_f^2h_2=\frac{3b}{4a},\qquad
\partial_g^2h_2=-\frac{a^3}{4b^3},\qquad
\nabla_{f,g}k=\left(\frac b{2a},\frac a{2b}\right).
\tag{13}
\]
These have genuine poles. This is a control of the
Euler and rank assumptions, not an example satisfying
the full actual graph, Schur complement, and slice
hypotheses.

Conversely, a nontrivial algebraic speed-field
extension is not automatically an obstruction to the
proof: \(f=a+a^2,g=b\) still has a simple zero at the
origin and a unit local speed Jacobian. Only the local
unramifiedness used in (4) is required, not global
polynomial coordinates or equality \(L=\mathbb C(f,g)\).

The theorem excludes a subcase of an already supplied
frame. It proves neither recognition of every remaining
supplied frame nor a universal way to choose such a
frame for an arbitrary cancellation problem.
