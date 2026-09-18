# Recognition from distinct kernels in a commuting component quotient

## 1. Precise recognition branch

Work over \(\mathbb C\). Let
\[
 B=\mathbb C[X_1,X_2,X_3,X_4],\qquad
 E\in\operatorname{LND}_{\mathbb C}(B),\qquad
 Eu=1,\qquad A=\ker E.
\tag{1}
\]
The slice theorem gives \(B=A[u]\), but neither a polynomial
presentation of \(A\) nor ambient coordinateness of \(u\) is assumed.
Suppose the actual positive weighted Euler derivation
\[
 D=\sum_{i=1}^4 w_iX_i\partial_{X_i},\qquad w_i\in\mathbb Z_{>0},
 \qquad E=\sum_{\lambda\in\mathcal S}E_\lambda,
 \qquad [D,E_\lambda]=\lambda E_\lambda
\tag{2}
\]
has nonzero, pairwise commuting, locally nilpotent components
\(E_\lambda\). The finite set \(\mathcal S\) consists of distinct
integer weights. The important special case is \(w_i=\deg_E X_i>0\),
but the argument allows any actual positive weighting.

There is a negative component \(L\) with an actual homogeneous
coordinate slice \(t\). Its actual quotient is
\(R=\ker L\cong\mathbb C^{[3]}\), and all other components restrict
to commuting LNDs \(\delta_\lambda\) of \(R\).

**Conditional recognition theorem.** If two nonzero restricted
derivations \(\delta_\lambda,\delta_\mu\) have distinct kernels,
then \(A\cong\mathbb C^{[3]}\). The same conclusion holds if all
restrictions vanish, or if their common kernel contains an actual
coordinate of \(R\).

The two distinct kernels are a hypothesis about the restrictions,
not about the number of ambient components. This source does not
prove that the hypothesis always holds. In particular it does not
recognize every action of a torus-normalized commutative unipotent
group. The nonzero restrictions may all have the same kernel, with
no actual coordinate in that kernel supplied by this argument.

The proof uses two exact primary theorems, stated below. It does not
use a general linearization, simultaneous triangularization, orbit
separation, or cancellation theorem. No novelty is claimed.

## 2. Exact primary inputs and their hypotheses

The first input is Maubach's three-variable commuting-derivations
theorem. In the author's manuscript, *The Commuting Derivations
Conjecture*, Theorem 3.6 says that two commuting LNDs of
\(\mathbb C[x,y,z]\), linearly independent over that polynomial
ring, have common kernel \(\mathbb C[f]\), where \(f\) is a
coordinate of the whole three-variable polynomial ring.
The theorem's full short proof and its Proposition 3.5 and
Theorem 2.4 route were read in the
[author's primary text](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf).
Its antecedent coordinate theorem is retained as an external theorem,
not recertified from a new proof here.

The equivalent formulation needed here appears in
[Dasgupta--Gaifullin, Proposition 2.14, version 2](https://arxiv.org/html/2306.00510v2):
nonzero commuting LNDs of \(k^{[3]}\) with distinct kernels have
joint kernel \(k[f]\) for a variable \(f\), in characteristic zero.
Here we use only \(k=\mathbb C\), so the original theorem suffices.
Indeed, a nontrivial polynomial linear relation between two nonzero
derivations makes them nonzero rational multiples in
\(\operatorname{Der}_{\mathbb C}(\operatorname{Frac}R)\); such
multiples have the same kernel on \(R\). Distinct kernels therefore
imply the required polynomial-ring linear independence. Neither
pointwise independence on every fiber nor a slice for either
restricted derivation is required.

The second input is
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1#S3).
For a characteristic-zero field \(k\), a nonzero
\(k[T]\)-linear LND of \(k[T,X,Y,Z]\) whose kernel is regular
has kernel \(k[T]^{[2]}\). The exact theorem and its full short
proof were read, together with the relevant Section 3 context.
There is no triangularity or homogeneity assumption in this theorem.
An actual invariant coordinate will supply its \(T\); regularity
will follow from the given slice, not be an additional assumption.

## 3. Extracting an actual coordinate slice for a component

Let \(o\) be the origin of the actual coordinate frame in (1).
Evaluating \(Eu=1\) there gives
\[
 1=\sum_i E(X_i)(o)\,\partial_{X_i}u(o).
\tag{3}
\]
Consequently \(E(X_j)(o)\ne0\) for some \(j\). The polynomial
\(E_\lambda(X_j)\) is homogeneous of weight \(w_j+\lambda\).
Positive weights imply that only \(\lambda=-w_j\) can contribute
a nonzero value at the origin, and a weight-zero polynomial is a
complex constant. Thus, for a nonzero scalar \(c\),
\[
 L=E_{-w_j},\qquad L(X_j)=c,\qquad t=X_j/c,
 \qquad L(t)=1,\qquad D(t)=w_jt.
\tag{4}
\]
This is an actual coordinate slice, since it is a scalar multiple of
one of the supplied polynomial coordinates. It is not asserted to
be an \(E\)-slice.

For completeness, the finite polynomial Taylor map is
\[
 \pi_L(g)=\sum_{r\ge0}\frac{(-t)^r}{r!}L^r(g).
\tag{5}
\]
Local nilpotence makes each sum finite. The product rule shows that
\(\pi_L\) is a ring homomorphism. Differentiating the sum telescopes,
so its image lies in \(R=\ker L\); it is the identity on \(R\)
and sends \(t\) to zero. Taylor inversion gives
\[
 g=\sum_{r\ge0}\frac{t^r}{r!}\pi_L(L^r g),
 \qquad B=R[t],\qquad \ker\pi_L=(t).
\tag{6}
\]
For the identity, expand the right side and group \(L^k g\): its
coefficient is \(t^k\sum_{r=0}^k(-1)^{k-r}/(r!(k-r)!)\),
which is zero except at \(k=0\). Algebraic independence of \(t\)
over \(R\) follows by applying the highest power of \(L\) to a
putative polynomial relation.

Because \(t\) is an actual coordinate, \(B/(t)\) is a polynomial
ring in the other three original coordinates. The quotient isomorphism
induced by (5) therefore proves
\[
 R=\mathbb C[z_i:i\ne j],\qquad z_i=\pi_L(X_i),
 \qquad B=\mathbb C[t,z_i:i\ne j].
\tag{7}
\]
These are whole polynomial-ring statements. No localization or
inference from an abstract stable-polynomial presentation is involved.
Each term of \(\pi_L(X_i)\) has weight \(w_i\), so the \(z_i\)
are homogeneous positive-weight coordinates of \(R\). Equivalently,
\([D,L]=-w_jL\) makes \(R\) stable under \(D\).

## 4. Restrictions and the distinct-kernel recognition proof

Commutation with \(L\) gives, for every other component,
\[
 \delta_\lambda=E_\lambda|_R\in\operatorname{LND}_{\mathbb C}(R),
 \qquad b_\lambda=E_\lambda(t)\in R,\qquad
 E_\lambda=\delta_\lambda+b_\lambda\partial_t
 \quad\text{on }R[t].
\tag{8}
\]
Restrictions are allowed to be zero. They commute with one another,
since the ambient derivations commute. Their local nilpotence follows
by restricting the iterates on the stable subring \(R\). Thus
\[
 E=\sum_{\lambda\ne-w_j}\delta_\lambda+
       \left(1+\sum_{\lambda\ne-w_j}b_\lambda\right)\partial_t.
\tag{9}
\]
In particular there is no reason for \(E(t)\) to equal one.

Suppose two nonzero restrictions have distinct kernels. Applying
the exact three-variable theorem to the actual ring (7) gives
\[
 \ker\delta_\lambda\cap\ker\delta_\mu=\mathbb C[f],
 \qquad R=\mathbb C[f,g,h]
\tag{10}
\]
for actual polynomial coordinates \(f,g,h\) of \(R\).
Every other \(\delta_\nu\) preserves this intersection. For instance,
\(\delta_\lambda(\delta_\nu v)=
\delta_\nu(\delta_\lambda v)=0\) whenever
\(v\in\ker\delta_\lambda\); the same argument applies to
\(\delta_\mu\).

An LND of \(\mathbb C[f]\) sends \(f\) to a scalar. To see this
without a hidden degree or zero case, write it as \(q(f)\partial_f\).
If \(q=0\) or is constant the assertion holds. If \(\deg q=e\ge1\),
its repeated action on \(f\) never vanishes: for \(e=1\) the leading
linear coefficient is repeatedly multiplied by a nonzero scalar;
for \(e>1\), the degrees of successive iterates are
\(1+r(e-1)\), with nonzero leading coefficients in characteristic
zero. This contradicts local nilpotence. Applying this to every
restriction gives
\[
 \delta_\nu(f)\in\mathbb C,\qquad L(f)=0,
 \qquad E(f)=\gamma\in\mathbb C.
\tag{11}
\]
No homogeneity of \(f\) or noncollision of its weights is needed.

If \(\gamma\ne0\), \(f/\gamma\) is an actual coordinate slice
for \(E\). In \(B=A[u]\), the difference \(f/\gamma-u\) lies
in \(A\). Evaluating this affine polynomial in \(u\) gives
\[
 A\cong B/(f)\cong\mathbb C^{[3]}.
\tag{12}
\]
The last isomorphism uses the actual coordinates \((f,g,h,t)\),
not an unproved coordinate-completion assertion.

If \(\gamma=0\), \(f\) is instead an actual invariant coordinate
of \(B=\mathbb C[f,g,h,t]\). Here \(A\) is regular: the slice
identifies it with \(B/(u)\), and
\(1=Eu=\sum_iE(X_i)\partial_{X_i}u\) makes the gradient ideal
of \(u\) the unit ideal. Thus this affine hypersurface is smooth
over \(\mathbb C\), hence regular. The nonzero derivation \(E\)
is \(\mathbb C[f]\)-linear, so Bhatwadekar--Gupta--Lokhande gives
\[
 A=\mathbb C[f]^{[2]}\cong\mathbb C^{[3]}.
\tag{13}
\]
This proves the conditional theorem, including both possible scalar
values in (11). The existence of the other two invariant generators
in (13) is a theorem endpoint; this proof does not compute them.

The argument of this section also applies without a grading whenever
one is independently given a commuting family of LNDs whose sum is
the sliced \(E\), one member has an actual coordinate slice, and
two restrictions on its polynomial threefold quotient have distinct
kernels. The grading was used to produce that member and quotient.

## 5. Zero restrictions and the precise remaining case

If every restriction is zero, (9) is \(E=b\partial_t\) with
\(b\in R\). The slice equation is
\(b\,\partial_tu=1\) in \(R[t]\). Hence \(b\) is a unit,
so \(b\in\mathbb C^*\); the coordinate \(t/b\) is an
\(E\)-slice and (12) applies.

More generally, if all restrictions kill an actual coordinate
\(f\) of \(R\), then \(E(f)=0\) and (13) applies directly.
This includes the case of just one nonzero restriction whose kernel
is already known to contain such a coordinate.

What is not settled by these arguments is the following alternative:
there are nonzero restrictions, they all have the same kernel, and
no coordinate of \(R\) in that common kernel has been established.
Having a polynomial two-variable kernel as an abstract ring would
not by itself place one of its generators in an actual coordinate
system of \(R\). Nor does positivity of the quotient grading alone
make an arbitrary homogeneous three-variable LND triangular.

The retained notes `commuting-coordinate-partial-pass.md` and
`commuting-quotient-pass15.md` already isolate related recognition
issues for an actual extension \(V+b\partial_t\). The earlier
`commuting-coordinate-descent-pass43.md` uses a different additional
actual-coordinate omission hypothesis. They were read to avoid
presenting the unrestricted extension problem as solved here.
No assertion about a counterexample to recognition is made in the
remaining case. It is a boundary of this sufficient criterion.

## 6. Exact controls for applicability and its limits

Here is a direct positive example with the Euler weights equal to
the actual \(E\)-degrees. In \(\mathbb C[t,x,y,z]\), put
\[
 a=x-t^2/2,\quad b=y-t^3/3,\quad c=z-t^4/4,
 \qquad
 L=\partial_t+t\partial_x+t^2\partial_y+t^3\partial_z,
 \quad M=a\partial_z,\quad N=a^2\partial_y.
\tag{14}
\]
These LNDs commute. For the Euler field of weights \((1,2,3,4)\),
their weights are respectively \(-1,-2,1\). The coordinate \(t\)
is an \(L\)-slice and \(R=\mathbb C[a,b,c]\), with inverse
\(x=a+t^2/2,y=b+t^3/3,z=c+t^4/4\). The restricted fields are
\(a\partial_c\) and \(a^2\partial_b\). Their respective kernels
are \(\mathbb C[a,b]\) and \(\mathbb C[a,c]\), with common
coordinate \(a\).

The sum \(E=L+M+N\) has \(E\)-degrees \((1,2,3,4)\) on the
displayed original coordinates and slice \(t\). Its complete
invariant-coordinate presentation and polynomial inverse are
\[
 \begin{gathered}
 A_1=a,\quad A_2=b-ta^2,\quad A_3=c-ta,\\
 x=A_1+t^2/2,\qquad
 y=A_2+tA_1^2+t^3/3,\qquad
 z=A_3+tA_1+t^4/4.
 \end{gathered}
\tag{15}
\]
Thus all ambient maps, restrictions and generation claims in this
control are actual polynomial identities. It illustrates the
criterion, not an unrecognized kernel or a claim of necessity.

For the failure of a tempting shortcut, the full retained582/587
control in \(\mathbb C[a,x,z,c]\) has
\[
 E=(1+a^2)\partial_x+a\partial_z,
 \quad u=x-az,\quad b=ax-(1+a^2)z,
 \quad x=(1+a^2)u-ab,\quad z=au-b.
\tag{16}
\]
Its actual positive-degree frame \((x,a+x,z,c+x)\) has degrees
\((1,1,1,1)\). The Euler field is the standard Euler derivation,
and the commuting spectral components are
\(\partial_x,a\partial_z,a^2\partial_x\), with weights
\(-1,0,1\). Choosing \(L=\partial_x\) gives the coordinate
slice \(x\) and \(R=\mathbb C[a,z,c]\). Nevertheless
\(E(x)=1+a^2\), and the other restrictions are
\(a\partial_z\) and zero. Three nonzero ambient components have
not supplied two distinct restricted kernels. This particular
example is recognized separately because \(a\) is an actual
invariant coordinate; it is not a counterexample to the conclusion
of cancellation or to recognition of this finite action.

## 7. Relation to the finite-action test and review status

The full source587 was read through EOF. Its first-shift and
pair-sum-noncollision test is one sufficient way to obtain the
commuting homogeneous LND hypothesis in (2). Its proof of finite
torus-normalized additive action does not include the distinct-kernel
condition of this source. Conversely, the recognition proof here
does not use shift one after the commuting family has been supplied.

The exact literature bridge is the three-variable common-coordinate
theorem, followed by the regular-kernel theorem in the zero-scalar
case. This is a conditional application of those primary results,
not a classification of arbitrary unipotent actions. It makes no
claim that every sliced derivation has a commuting spectral
decomposition, that every component quotient meets the criterion,
or that an arbitrary first-shift action is recognized.

Fresh unsaved algebra checks all brackets and homogeneous weights
in (14), the complete Taylor coordinates, the exact four
\(E\)-degrees, both inverse orders in (15), and all slice and
invariant identities. It also reconstructs both inverse orders and
the slice identities in (16). These controls do not replace the
general proofs or the explicitly retained external theorems.

No saved checker was executed, imported or compiled. No canonical
file was edited, and no unfinished source was read. Final hold
requires a complete author EOF reread and an exact hash, separately
reported for independent review.
