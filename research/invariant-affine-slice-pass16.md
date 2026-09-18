# Higher-image torsion and the affine-slice question

The general polynomial-threefold affine-slice implication remains
unproved in this pass. There is an exact all-degree obstruction to a
nonlinear minimal slice: its leading coefficient must give nonzero
torsion in a higher image ideal. This yields a conditional reduction
theorem and identifies what a saturation argument would need to prove.
The normalized-curve geometric route is valid through its DVR step,
but its general local-plinth conclusion requires an additional theorem.

## 1. Setup and the exact target

Let \(R=\mathbb C^{[3]}\), \(0\ne D\in\operatorname{LND}(R)\),
\(C=\ker D\), and \(A,\beta\in C\). Put
\[
\delta=AD,\qquad E=\delta+\beta\partial_t.
\]
Assume that \(E\) has a slice. Constant or zero coefficient cases
are handled in
[the quotient-slice boundary note](quotient-slice-boundary-pass15.md).
Here take \(A\ne0\) and \(\beta\ne0\).

That note proves
\[
(A,\beta)C=C,
\]
and proves that an affine-in-\(t\) slice exists exactly when
\[
A P_D+\beta C=C,
\qquad P_D=D(R)\cap C.
\tag{1}
\]
Under the first displayed condition, this is equivalent to
\(P_D+\beta C=C\). The unresolved assertion is that an arbitrary
slice forces (1), not the construction of a slice once (1) is given.

## 2. Minimal nonlinear slices force higher-image torsion

For \(j\ge1\), define the \(C\)-ideal
\[
I_j=\delta^j(R)\cap C.
\]
Choose an \(E\)-slice of minimum degree in \(t\), and suppose
that degree is \(n\ge2\). Write
\[
s=r_0+r_1t+\cdots+r_nt^n,
\qquad c=r_n\ne0.
\]
Its coefficient equations are
\[
\delta r_0+\beta r_1=1,
\quad \delta r_j+(j+1)\beta r_{j+1}=0\ (1\le j<n),
\quad\delta r_n=0.
\tag{2}
\]
In particular \(c\in C\). Applying \(\delta\) repeatedly to
the constant equation gives, for \(n\ge2\),
\[
\delta^n r_0=(-1)^n n!\,\beta^n c.
\tag{3}
\]
The restriction \(n\ge2\) matters: for \(n=1\), the constant
term 1 has not yet been killed. Equation (3) proves
\(\beta^n c\in I_n\).

If \(c\in I_n\), choose \(h\in R\) with \(\delta^n h=c\).
Then \(\delta^{n+1}h=0\), and the following finite expression is
a polynomial in \(R[t]\):
\[
J_h=\sum_{j=0}^n
 \frac{(-1)^j}{j!}\,\beta^{n-j}t^j\delta^j h.
\tag{4}
\]
Consecutive terms cancel under \(E\), so \(E(J_h)=0\).
Its leading \(t\)-coefficient is \((-1)^n c/n!\). Consequently
\(s-(-1)^n n!J_h\) would be a slice of smaller \(t\)-degree,
contradicting minimality. We have proved
\[
\boxed{c\notin I_n,\qquad\beta^n c\in I_n.}
\tag{5}
\]
No variable-time exponential is assumed to be an automorphism.
Formula (4) is an explicit invariant polynomial; the notation
\(\beta^n\exp(-(t/\beta)\delta)(h)\) is only a shorthand for
its finite expansion.

Thus every minimal nonlinear slice produces a nonzero
\(\beta\)-power-torsion class in \(C/I_n\). In particular:

**Conditional affine-slice theorem.** If
\[
(I_j:\beta)=I_j\quad\text{for every }j\ge2,
\tag{6}
\]
then any \(E\)-slice can be reduced to an affine-in-\(t\) slice
by successive subtractions of polynomials of form (4).
For a given slice of degree \(N\), saturation only for
\(2\le j\le N\) suffices.

## 3. The obstruction can be written using the original derivation

Put \(J_j=D^j(R)\cap C\). Since \(A\) is invariant and nonzero,
\[
I_j=A^jJ_j.
\tag{7}
\]
The identity \((A,\beta)C=C\) and (3) imply \(A^n\mid c\)
in \(C\). Write \(c=A^n c_0\). Equation (5) becomes
\[
\boxed{c_0\notin J_n,\qquad\beta^n c_0\in J_n.}
\tag{8}
\]
Thus saturation of the higher image ideals of \(D\), rather than
of its replica \(AD\), is enough. No saturation property for
arbitrary three-variable LNDs is established here.

These ideals have the same reduced support as the ordinary plinth
ideal. Indeed \(J_j\subseteq P_D\), while for every
\(p=Dr\in P_D\),
\[
D^j(r^j)=j!p^j.
\]
Hence \(\sqrt{J_j}=\sqrt{P_D}\). This does not exclude embedded
associated primes or assert that all \(J_j\) are principal.
In particular, the principality theorem for \(P_D=J_1\) must not
be silently applied to every higher image ideal.

## 4. Audit of the normalized-curve DVR route

Suppose an irreducible component \(\Gamma\) of \(V(\beta)\)
is not contained in the plinth support. Normalize \(\Gamma\),
and let \(V\) be the DVR at a point above
\(p\in\Gamma\cap V(P_D)\). Base change gives \(T=R\otimes_CV\).

The known faithful flatness of \(R\) over \(C\) makes \(T\)
faithfully flat over \(V\). Its generic fiber is
\(\operatorname{Frac}(V)[\rho]\), because \(\Gamma\) is not
contained in the plinth support. Flatness embeds \(T\) into that
generic fiber, so \(T\) is a domain. An invariant lies in
\(\operatorname{Frac}(V)\). A negative valuation would make a
uniformizer invertible in \(T\), contradicting its nonempty
special fiber. Therefore \(\ker D_V=V\).

The original slice, reduced to \(T[t]\), gives a \(D_V\)-slice:
evaluate its constant \(t\)-coefficient and multiply by the
invariant coefficient \(A\), as in (3) of the preceding pass.
It follows that \(T=V[\rho]\). Thus the original fiber at \(p\)
is a reduced affine line, and \(D\) acts there by a nonzero
translation.

This much is verified. The next proposed implication is

> A reduced affine-line quotient fiber with nonzero translation
> action forces the base point outside the plinth support.

No proof of that local implication in this generality is supplied
here. It should not be inferred just from generic-fiber statements.
For comparison,
[Masuda, Theorem 3.9](https://arxiv.org/html/2312.05455v1)
assumes an irreducible LND on a factorial affine variety with affine
invariant ring and principal plinth ideal. It describes the general
closed fiber over each plinth component as more than one disjoint
affine line. Its stated conclusion concerns general closed fibers,
not every special point on the component.

For the concrete triangular family
\(D=x^m\partial_y+P(x,y)\partial_z\), the separate branch audit
can compute the special fiber explicitly and contradict it directly
when \(\deg_yP(0,y)\ge1\). That successful special-case calculation
does not establish the general local implication above. Components of
\(V(\beta)\) contained in plinth support also require a separate
argument.

### 4.1. Finite factorization does not by itself prevent escaping components

The abstract properties of a finite factorization are insufficient for
the proposed local conclusion. Consider
\[
Y=\operatorname{Spec}\mathbb C[t,(t+1)^{-1},y],
\qquad \pi:Y\longrightarrow\mathbb A^1_u,\quad u=t^2,
\qquad D=\partial_y.
\]
A general fiber of \(\pi\) consists of two affine lines. The fiber
at \(u=1\), however, is the single reduced affine line \(t=1\):
the line \(t=-1\) has been removed. Moreover, \(\pi\) is smooth
along the retained fiber, since \(d(t^2)/dt=2\) there.

There is nevertheless a factorization through the nodal curve
\[
Z=\operatorname{Spec}
 \mathbb C[u,w]/\bigl(w^2-u(u-1)^2\bigr),
\qquad
\kappa(t,y)=\bigl(t^2,t(t^2-1)\bigr),
\qquad \theta(u,w)=u.
\]
The map \(\theta\) is finite of degree two. The map \(\kappa\)
is surjective and every fiber is a reduced affine line. Indeed, away
from the node it is the normalization parameter followed by the
affine-line projection. At the node \((1,0)\), its two normalization
points are \(t=1,-1\), and the first remains after the second is
deleted. Thus even finite \(\theta\), surjective \(\kappa\)
with connected fibers, and smoothness along the retained fiber do not
exclude generic components disappearing. No ramification along that
retained component is required.

This is a countercontrol for the proposed inference, not a
three-dimensional polynomial quotient counterexample. It is also not
asserted to be the particular Stein factor produced by
[Kaliman, Lemma 2.2 and Proposition 3.2(i)](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf).
Lemma 2.2 constructs a proper compactification factorization and then
restricts it; connectedness is stated for the proper factor's fibers,
whereas the lemma's displayed conclusion for the restricted map is a
general affine-line product. Proposition 3.2(i) supplies finiteness
under its ambient homological and smoothness hypotheses. Further
control of this specific factorization, or a local triviality theorem,
is needed before using it to establish the local-plinth assertion.

## 5. A localized sharpness control, not a polynomial-base counterexample

The saturation premise cannot be discarded for arbitrary smooth
affine bases. Let
\[
R'=\mathbb C[x,y,z,v^{-1}],\qquad v=x^2z-y^2,
\qquad D=x^2\partial_y+2y\partial_z,
\]
and set \(E=D+x\partial_t\). Define
\[
\rho=y-xt,
\qquad Z=z-t^2,
\qquad w=xZ-2\rho t.
\]
Then \(E\rho=Ew=0\), \(E(Z)=2\rho\), and
\(v=xw-\rho^2\). Therefore
\[
s=\frac{wt-\rho Z/2}{v}
=\frac{-yz+3xzt-3yt^2+xt^3}{2v}
\quad\text{satisfies}\quad E(s)=1.
\tag{9}
\]
There is no affine-in-\(t\) slice. On the original polynomial
ring, the plinth ideal of this \(D\) is \((x^2)\): it is
principal, contains \(x^2=Dy\), cannot be the unit ideal because
of fixed points, and cannot contain \(x\), since evaluation of
\(Dr=x\) at \(y=0\) would make \(x^2r_y(x,0,z)=x\).
The principality input is the exact three-variable theorem recalled
in
[Dasgupta and Gaifullin, Theorem 2.10(ii)](https://arxiv.org/pdf/2306.00510).
Invariant localization preserves the plinth ideal, so on \(R'\)
it is still \((x^2)\). Its sum with \((x)\) is proper, and
criterion (1) excludes affine slices.

The coefficient \(v^{-1}\) in (9) is essential to the scope:
\(R'\) is an open subset of affine three-space, not
\(\mathbb C^{[3]}\). This example does not answer the original
question negatively. It demonstrates that a global polynomial-base
property must do real work in any unconditional saturation or
affine-slice theorem.

## 6. Endpoint

An independent inline SymPy run under
`/opt/anaconda3/bin/python` passed 21 exact assertions in 0.085 seconds.
These checked the seven displayed invariant and slice identities of
Section 5, the cancellation and leading coefficient of (4) for each
degree from two through six using \(h=y^n\), and four identities
for the nodal normalization and retained fiber. The calculations are
checks of these formulas, not computational proofs of the all-degree
or geometric assertions.

The pass supplies the all-degree torsion obstruction (5), its
original-derivation form (8), and the conditional reduction theorem
(6). It validates the DVR argument up to its precise remaining local
step and gives a scoped countercontrol to a proposed shortcut through
finite factorization. It does not prove that every invariant-coefficient slice on
\(\mathbb C^{[3]}[t]\) is affine in the added variable, and it
does not produce a polynomial-base counterexample.
