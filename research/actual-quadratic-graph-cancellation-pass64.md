# Cancellation for the actual independent-defect quadratic graph

The full actual independent-defect quadratic graph of pass44 has
polynomial kernel. The proof does not require monomial speeds,
coprime speeds, a trivial polynomial Euler-invariant ring, or
regularity of the rational graph coefficients.

The moving-direction case contradicts actual coordinate-field
generation. The constant-direction case produces an actual
ambient coordinate fixed by the original derivation. An existing
Dedekind-base cancellation theorem then recognizes the kernel.

This is a conditional cancellation theorem for the specified
actual frame. It does not prove that an arbitrary sliced
derivation admits such a frame.

## 1. The actual hypotheses and the precise conclusion

Work over \(k=\mathbb C\). Assume the full hypotheses of
[the generic bad-pair theorem](generic-bad-pair-pass44.md).
In particular
\[
B=k[Q_1,Q_2,X,Y],\qquad E\in\operatorname{LND}_k(B),
\qquad E(s_*)=1,\qquad A=\ker E.
\tag{1}
\]
Here \(Q_1,Q_2,X,Y\) are genuine polynomial coordinates of
the original four-ring. The inherited invariant plane and its
fraction field satisfy
\[
C=k[a,b]\subseteq A,\qquad L=k(a,b),\qquad
B\cap L=C,\qquad B\otimes_C L=L[X,Y].
\tag{2}
\]
No assertion that \(a,b\) are ambient coordinates is made.
The actual bad speeds \(f=EX,\ g=EY\) belong to \(C\)
and are algebraically independent. On the generic ring,
\[
E=f\partial_X+g\partial_Y.
\tag{3}
\]

The true good-column equations give the exact graph
\[
Q_i=
\frac14(X,Y)\operatorname{Hess}_{f,g}(h_i)\binom XY
+(\nabla_{f,g}k_i)\binom XY+\ell_i,
\]
\[
h_i\in C,\quad k_i,\ell_i\in L,\qquad
\mathscr Hh_i=2h_i,\quad \mathscr Hk_i=k_i,\qquad
\mathscr H=f\partial_f+g\partial_g.
\tag{4}
\]
The field partials are the unique extensions to the finite
separable extension \(L/k(f,g)\). Two crucial actual consequences
are
\[
\det Q_{(f,g)}\in L^*,\qquad
k(Q_1,Q_2,X,Y)=L(X,Y).
\tag{5}
\]
The first follows from the true polynomial-in-\(X,Y\) Schur inverse.
The second follows from the original polynomial coordinates.
A guessed quadratic presentation would not supply them.

**Theorem.** Under the actual hypotheses (1)--(5),
\[
\boxed{A\simeq k^{[3]}.}
\tag{6}
\]
There is the following intermediate alternative:

- either \(B=C[X,Y]\), and the original action has an explicit
  affine slice over \(C\);
- or an element of \(C\) is an actual ambient coordinate of \(B\).

Both alternatives recognize the original kernel. The supplied
slice remains the original \(s_*\); it is not transferred to
a divided or unrelated derivation.

## 2. The rational Euler-invariant field is automatic

Put \(F=\ker_L\mathscr H\). Since \(\mathscr Hf=f\ne0\),
this is the kernel of a nonzero derivation. It contains the
nonconstant element \(g/f\).

It has transcendence degree exactly one over \(k\). If it
contained two algebraically independent elements \(u,v\),
then \(L/k(u,v)\) would be algebraic and separable.
A derivation which vanishes on \(k(u,v)\) must vanish on that
extension: differentiate a separable minimal polynomial.
This would contradict \(\mathscr Hf=f\ne0\).
The element \(g/f\) supplies the lower bound of one.

The generalized Lüroth theorem for transcendence-degree-one
subfields of \(k(a,b)\) therefore gives
\[
F=k(r)\quad\hbox{for some actual }r\in L.
\tag{7}
\]
We use its precise statement as recorded in de Bondt,
Theorem 1.1, credited there to Lüroth, Gordan, Steinitz and
Igusa.[^luroth] This is a standard external theorem input;
no proof of it is attributed to the new graph argument.

The generator \(r\) is in the unchanged actual field.
No roots are adjoined, and no formal or étale field is substituted
for \(L\).

The Euler commutators
\[
[\mathscr H,\partial_f]=-\partial_f,\qquad
[\mathscr H,\partial_g]=-\partial_g
\]
make all the Hessian and gradient coefficients in (4) weight
zero. Thus, without assuming that the \(k_i\) are regular,
\[
Q=\ell+S(r;X,Y),\qquad
S\in k(r)[X,Y]^2,\qquad S(r;0,0)=0.
\tag{8}
\]
Its degree is at most two, although the following argument
works for arbitrary finite degree.

## 3. The full determinant aligns the coefficient vectors

Let \(A_0=\ell_{(f,g)}\) and
\(\lambda=(\partial_f r,\partial_g r)\).
The row \(\lambda\) is nonzero. Indeed the speed partials
span the \(L\)-space of \(k\)-derivations of \(L\); if both
killed \(r\), the ordinary \(a,b\) partials would also kill it,
making \(r\) constant.

Differentiating (8) gives
\[
Q_{(f,g)}=A_0+S_r\lambda.
\tag{9}
\]
Evaluation at \(X=Y=0\) in (5) makes \(A_0\) invertible.
The rank-one determinant identity gives
\[
\lambda A_0^{-1}S_r=0.
\]
Since \(\mathscr Hr=0\), the kernel of \(\lambda\) is
\(L(f,g)^{\mathsf t}\). Thus every coefficient vector of
\(S_r\) is collinear with
\[
\mathscr H\ell=A_0(f,g)^{\mathsf t}\ne0.
\tag{10}
\]

If \(S_r\ne0\), interchange the good rows if necessary
and choose a nonzero coefficient of \((S_1)_r\).
Then \(\mathscr H\ell_1\ne0\), and the ratio of the
corresponding second and first coefficient derivatives gives
\[
\rho\in k(r),\qquad
(S_2)_r=\rho(S_1)_r,\qquad
\mathscr H\ell_2=\rho\mathscr H\ell_1.
\tag{11}
\]
The actual rational kernel (7) gives
\[
I=\ell_2-\rho\ell_1\in k(r).
\]
With \(D=S_2-\rho S_1\), we have
\[
Q_2=\rho Q_1+D(r;X,Y)+I(r),\qquad
D_r=-\rho_r S_1.
\tag{12}
\]

No condition on \(C\cap F\) has been used. In particular a
nonconstant polynomial Euler invariant is still allowed.

## 4. A nonconstant direction is incompatible with generation

Extend \(\mathscr H\) by fixing \(X,Y\).
It kills \(k(r,X,Y)\), but
\(\mathscr HQ_1=\mathscr H\ell_1\ne0\).
The separable-minimal-polynomial argument shows that
\(Q_1\) is transcendental over \(k(r,X,Y)\).
Hence \(Q_1,r,X,Y\) are algebraically independent.

Set \(K=k(Q_1,X,Y)\). Formula (12) and actual generation give
\[
K(Q_2)\subseteq K(r)\subseteq L(X,Y)=K(Q_2).
\tag{13}
\]
Thus \(Q_2\), regarded as a rational function of \(r\) over
\(K\), has degree one.

Here are the exact pole and coefficient steps, so the conclusion
does not depend on importing an inapplicable hypothesis from
[the graph rigidity theorem](rational-euler-graph-rigidity-pass63.md).
Write
\[
D=\sum_{\nu\ne(0,0)}d_\nu(r)X^{\nu_1}Y^{\nu_2}.
\]
At every complex point of \(\mathbb P^1\), the pole order of
\[
\rho(r)Q_1+\sum_\nu d_\nu(r)X^{\nu_1}Y^{\nu_2}+I(r)
\tag{14}
\]
is the maximum of the pole orders of its coefficient functions.
At the most negative Laurent order, distinct monomials
\(Q_1,X^{\nu_1}Y^{\nu_2},1\) cannot cancel, by algebraic
independence. Their rational coefficient functions have no
other poles after extending the coefficient field to \(K\).
The ordinary rational-function degree equals the total pole
degree, as proved directly in pass63, equation (14).

If \(\rho\) were nonconstant, its pole divisor and that of
(14) would have to be the same single simple pole.
Every \(d_\nu\) would then have at most that pole, and hence
\[
d_\nu=A_\nu+B_\nu\rho,\qquad A_\nu,B_\nu\in k.
\]
This follows by moving the one pole to infinity, leaving
polynomials of degree at most one. Differentiating and using
(12) gives
\[
B_\nu\rho_r=-\rho_r s_{1\nu}.
\]
As \(\rho_r\ne0\), every coefficient \(s_{1\nu}\) of \(S_1\)
would be constant, contrary to the chosen nonzero derivative.

Therefore, whenever \(S_r\ne0\),
\[
\boxed{\rho\in k.}
\tag{15}
\]
This entire exclusion uses no premise that regular Euler
invariants are constant.

## 5. A constant direction supplies an actual invariant coordinate

If \(S_r\ne0\), equation (15) and (11) imply
\(D_r=0\), so \(D\in k[X,Y]\). Equation (12) now gives
\[
I=Q_2-\rho Q_1-D(X,Y)\in B\cap L=C.
\tag{16}
\]
In particular \(EI=0\).

The essential point is stronger than membership in the
invariant ring: \(I\) is an actual ambient coordinate.
The change
\[
(Q_1,Q_2,X,Y)\longmapsto(Q_1,I,X,Y)
\]
has the explicit polynomial inverse
\[
Q_2=I+\rho Q_1+D(X,Y).
\tag{17}
\]
Its coefficients are in \(k\), and the starting four elements
are the original actual coordinates, up to the permitted swap.
Consequently
\[
B=k[I][Q_1,X,Y].
\tag{18}
\]
There is no need to prove that \(I\) is a coordinate of \(C\),
or that the old adjoint bounds survive this final shear.

The ring \(k[I]\) is a polynomial one-ring, hence a Dedekind
domain containing the rationals. The original \(E\) is a
locally nilpotent \(k[I]\)-derivation of its polynomial
three-ring (18), and it still has the actual slice \(s_*\).
Derksen, van den Essen and van Rossum's Theorem 4.4 therefore
gives
\[
A=\ker E\simeq k[I]^{[2]}\simeq k^{[3]}.
\tag{19}
\]
Equivalently, their Corollary 4.5 applies with the invariant
ambient coordinate as its last variable.[^dedekind]

This is exactly where an established cancellation theorem
is used. Its base is the one-dimensional ring \(k[I]\),
not the two-dimensional common invariant plane \(C\).

## 6. Constant graph coefficients give the explicit other branch

It remains that \(S_r=0\). Every coefficient of \(S\) is
then constant. The actual differences \(Q_i-S_i\) belong
to \(B\cap L=C\), so \(\ell_i\in C\) and
\[
B=C[X,Y].
\tag{20}
\]
The original slice gives \(1\in(f,g)C\), because
\(E(B)\subseteq(f,g)C[X,Y]\) and one may evaluate at \(X=Y=0\).

Choose \(u_0,v_0\in C\) with \(u_0f+v_0g=1\), and set
\[
\sigma=u_0X+v_0Y,\qquad j=gX-fY.
\]
Then
\[
X=f\sigma+v_0j,\qquad Y=g\sigma-u_0j,\qquad
E\sigma=1,\qquad Ej=0.
\tag{21}
\]
Thus
\[
B=C[\sigma,j],\qquad A=C[j]\simeq k^{[3]}.
\tag{22}
\]
This proves the theorem in the remaining case.

## 7. Exact scope and what has changed

The full actual graph of pass44 is now recognized, including
ramified common speed zeros and common speed divisors.
Those possibilities need not be eliminated individually:
the proof either removes the graph dependence on the rational
Euler parameter or obtains an invariant ambient coordinate.

The earlier monomial exclusions and divisor conditions remain
valid. They are no longer required to resolve this particular
graph recognition problem. No theorem about arbitrary
ramified germs is inferred from formal monomialization.

The proof does not establish the existence of the pass44 frame
for a general sliced derivation of the four-variable polynomial
ring. It also does not, by itself, certify every earlier branch
of a larger frame classification. The full supplied-profile
and universal-frame dependency audit remains separate.
Accordingly the original complex-threefold cancellation
conjecture is not marked solved.

The professor's intended field and dimension also remain
unconfirmed. No expert review, formal proof-assistant check,
historical novelty certification, or publication is claimed.

## Sources and verification boundary

The input graph and actual determinant identities are proved in
[pass44](generic-bad-pair-pass44.md). The pole-divisor argument
was written and independently AI-audited in
[pass63](rational-euler-graph-rigidity-pass63.md).
The argument here does not invoke the latter theorem with its
trivial-invariant-intersection hypothesis deleted: Sections 3--4
reproduce precisely the part of its proof that never used it.

The main agent directly read de Bondt's Theorem 1.1 and
attribution paragraph in the retained v4 primary text.
That paper states the generalized Lüroth theorem and points
to earlier proofs; it does not provide a new proof there.
The main agent also directly read the author-uploaded
Dedekind theorem, its complete proof, and Corollary 4.5 with
proof. These are explicit established inputs, not new results.

The affine and jet agents each independently read the complete
saved proof through EOF and reconstructed all 22 equations,
both source applications, and every actual-coordinate gate
without finding a gap. The geometry agent separately reconstructed
the coordinate extraction, both alternatives, and the complete
inherited pass44 inputs. These are AI audits, not expert review.
No numerical suite could establish the generalized Lüroth or
Dedekind cancellation inputs; none is claimed here.

[^luroth]: Michiel de Bondt, *Rational maps H for which K(tH)
has transcendence degree 2 over K*,
[arXiv:1501.06046v4](https://arxiv.org/pdf/1501.06046v4),
Theorem 1.1 and its following attribution paragraph, PDF p. 4.
Retained exact inputs: [PDF](../tmp/pdfs/bondt-1501.06046v4.pdf)
and [layout text](../tmp/pdfs/bondt-1501.06046v4.txt).
The PDF's version banner says 2 November 2017; the retained
document title page separately prints 2 July 2021.

[^dedekind]: Harm Derksen, Arno van den Essen and Peter van Rossum,
*The Cancellation Problem in Dimension Four*,
[author-uploaded primary manuscript](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four),
Nijmegen Report 0022, October 2000, Theorem 4.4 and
Corollary 4.5, printed pp. 8--9. The selected complete
statements and proofs were read directly; no claim of a new
full-paper or publication-history audit is made.
