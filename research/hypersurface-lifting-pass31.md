# Polynomial derivation lifts and the all-thickening obstruction boundary

For the fixed conductor surface, a hypothetical hypersurface embedding
would admit an exactly equation-preserving polynomial derivation lift of
every one of its additive actions. Each such lift is locally nilpotent
on every finite thickening of the hypersurface. Neither assertion gives
a locally nilpotent derivation of the ambient polynomial ring.

This closes one proposed obstruction route: detecting failure to lift an
action to some finite equation-adic thickening cannot exclude this
surface's embedding. It does not construct the embedding or an ambient
additive action, and the minimum number of generators remains undecided.

## 1. The exact general first obstruction

Let \(W=\mathbb C[X,Y,Z]\), let \(0\ne F\in W\) be nonconstant,
and put \(R_F=W/(F)\). For now no special surface is assumed. Write
\[
J_F=(F_X,F_Y,F_Z)\subset W.
\tag{1}
\]
Every derivation \(D\) of \(R_F\) has a polynomial derivation lift
\(E\) on \(W\): choose arbitrary polynomial lifts of its values
on the three residue coordinates. Since \(D\) respects the relation,
\[
E(F)=Fg\qquad\text{for a unique }g\in W.
\tag{2}
\]
This is tangency to the hypersurface, not exact preservation of its
defining polynomial and not local nilpotence.

Two lifts differ by \(FV\), for some polynomial derivation \(V\).
Replacing \(E\) by \(E+FV\) changes \(g\) to \(g+V(F)\).
Thus the well-defined obstruction is
\[
\kappa_F(D)=[g]\in (J_F:F)/J_F
 =\operatorname{Ann}_{W/J_F}(F),
\tag{3}
\]
and
\[
\kappa_F(D)=0
\quad\Longleftrightarrow\quad
\exists E_0\in\operatorname{Der}_{\mathbb C}(W):
\quad E_0\bmod F=D,\quad E_0(F)=0.
\tag{4}
\]
The numerator condition in (3) follows from
\(Fg=E(F)\in J_F\). In the zero case, write
\(-g=\sum_i v_iF_i\) and take \(E_0=E+F\sum_i v_i\partial_i\).
This is a finite polynomial correction, not a formal series.

The map in (3) is \(R_F\)-linear and surjective. Indeed any
\(g\) with \(Fg\in J_F\) has an expression \(Fg=\sum_i a_iF_i\),
and \(E=\sum_i a_i\partial_i\) then induces a derivation of
\(R_F\) with the required obstruction. Consequently the cokernel
of restriction from exactly \(F\)-preserving polynomial derivations
to \(\operatorname{Der}(R_F)\) is precisely the module in (3).
The correction in (4) need not preserve a chosen slice, divergence,
other invariant polynomials, or local nilpotence.

## 2. Hypotheses for the fixed surface

Now assume, only for the following conditional argument, that
\[
R\cong W/(F)
\tag{5}
\]
is the unchanged fixed surface of
[pass 30](all-noninvariant-surface-pass30.md). Its normalization is
\[
B=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),\qquad
d=u^4-1,\quad e=du.
\tag{6}
\]
Its full conductor is \(I=dB=(d,e)R\). The reduced conductor curve
\(C=\operatorname{Spec}(R/I)\) is the disjoint union of three full
affine lines with their original scaled parameters \(t\). All of
its completed surface local rings are double crossings
\(\mathbb C[[\xi,\eta,t-t_0]]/(\xi\eta)\).

The corresponding normalized root pairs are
\[
(1,i),\qquad(1,-i),\qquad(-1,i),
\tag{7}
\]
with the branch labels retained exactly as in pass 30. Every
classified LND annihilates \(d,e\) and acts on each conductor
parameter as \(D(t)=c\), with one constant \(c\in\mathbb C\).

Choose polynomial lifts \(a,b\in W\) of \(d,e\), and denote the
ideal of the conductor curve in the hypothetical ambient space by
\[
K=(F,a,b)\subset W.
\tag{8}
\]
We will distinguish \(K\) from the ordinary Jacobian ideal \(J_F\)
until their required local equality has actually been proved.

## 3. The global invariant normal frame is forced, not assumed

The immersion of the smooth curve \(C\) into smooth three-space
is regular of codimension two. Its conormal module \(K/K^2\) is
therefore locally free of rank two, and its associated graded algebra
is the symmetric algebra of that module.[^regular]

At each conductor point the defining equation lies in the square of
the ideal of the conductor: in completed ambient coordinates it is a
unit times \(\xi\eta\), with conductor ideal \((\xi,\eta)\).
This embedded description follows from the completed surface
isomorphism: lift the three residue parameters to the complete
three-variable power-series ring. Their independent linear parts
give a formal coordinate automorphism, and the two principal
kernels agree up to a unit. Faithful flatness of local completion
then gives the asserted local ideal membership.[^completion]

Thus \(F\in K^2\) globally. Membership can be checked at all
maximal ideals; outside \(C\) the localized ideal \(K\) is the
unit ideal. Equation (8) now shows that the classes of \(a,b\)
generate \(K/K^2\). A surjection from a free rank-two module to a
locally free rank-two module is an isomorphism. Hence
\[
K/K^2=(W/K)\bar a\oplus(W/K)\bar b.
\tag{9}
\]
This is a global conormal trivialization, but it is not a claim
that \(K=(a,b)\) globally in \(W\).

On a normalization branch at root \(r\), the first normal terms
of \(d,e\), using \(u-r\), have coefficients
\[
4r^3,\qquad 4r^4.
\tag{10}
\]
They therefore have slope \(\bar b=r\bar a\). On a paired pair
\((r_j,r_k)\), the determinant is
\(16r_j^3r_k^3(r_k-r_j)\ne0\). These statements hold along the
entire line, not just at one chosen point, since \(d,e\) depend
only on \(u\). They also verify (9) directly in the actual
normalization coordinates.

Let \(F_2\) be the degree-two normal symbol of \(F\). On the
\(j\)-th conductor line, the two reduced tangent branches and
(10) force
\[
F_2=c_j(t)(\bar b-r_j\bar a)(\bar b-r_k\bar a).
\tag{11}
\]
The coefficient belongs to \(\mathbb C[t]\): (9) expresses
\(F_2\) globally in the three quadratic monomials, and the
coefficient of \(\bar b^2\) is \(c_j(t)\). It is nonzero at
every point, because each completed singularity is an ordinary
double crossing. A nowhere-zero polynomial on the full complex
affine line is a nonzero constant. Thus
\[
c_j(t)\in\mathbb C^*.
\tag{12}
\]
This full-line step would be invalid on a punctured line with
nonconstant units. It is also invalid if a degeneration of the
normal quadratic is allowed somewhere on the conductor.

## 4. Vanishing of the exact first obstruction for all actions

Let \(D\) be any of the LNDs classified in pass 30 and \(E\)
any polynomial derivation lift as in (2). Since \(D(d)=D(e)=0\),
\[
E(a),E(b)\in(F)\subset K^2.
\tag{13}
\]
Also \(E(F)=Fg\), so \(E\) preserves \(K\) and its powers.
The induced derivation of the associated graded algebra kills
the two degree-one basis sections in (9). On its coefficient
ring \(W/K=\mathbb C[t]^3\), it acts by \(c\partial_t\).
Equations (11)-(12) therefore give
\[
E(F)_2=0.
\tag{14}
\]
On the other hand (2) gives \(E(F)_2=\bar g F_2\).
The element \(F_2\) is a nonzero divisor in the product of the
three polynomial algebras \(\mathbb C[t][\bar a,\bar b]\).
Consequently \(\bar g=0\), or
\[
g\in K.
\tag{15}
\]

We now prove \(g\in J_F\), keeping track of points outside the
hypersurface too. At a conductor point, formal ambient coordinates
give \(F=v\xi\eta\), where \(v\) is a unit. Its \(\xi\)-
and \(\eta\)-derivatives are respectively
\(\eta(v+\xi v_\xi)\) and \(\xi(v+\eta v_\eta)\).
Both parenthesized factors are units; the remaining derivative
is also in \((\xi,\eta)\). The Jacobian ideal is thus exactly
\((\xi,\eta)\). A formal coordinate change changes the gradient
by an invertible Jacobian matrix. By faithful flatness,
\[
(J_F)_{\mathfrak m}=K_{\mathfrak m}
\quad\text{at each conductor point.}
\tag{16}
\]
This computation does not assert that multiplying an arbitrary
singularity equation by a unit preserves its ordinary Jacobian
ideal. That statement is false in general.[^jacobian]

At a smooth point of \(F=0\), the Jacobian ideal is the unit
ideal. At a point with \(F\ne0\), the identity
\(Fg=\sum_i F_iE(X_i)\) and invertibility of \(F\) imply
\(g\in J_F\) locally. These cases and (15)-(16) cover all
maximal ideals of \(W\). Ideal membership is local, so
\[
g\in J_F\quad\text{globally},\qquad \kappa_F(D)=0.
\tag{17}
\]

**Conditional theorem.** For every hypothetical hypersurface
presentation (5), every LND of the fixed \(R\) has a polynomial
derivation lift \(E_0\) with \(E_0(F)=0\).

For this hypothetical presentation, the general obstruction module
in (3) is canonically isomorphic to \(W/K=\mathbb C[t]^3\) by
restriction. Locally on the conductor this follows from (16), where
\(F\in J_F\); off \(F=0\) the annihilator in (3) is zero;
and at smooth surface points both modules vanish. Thus (17) is
the vanishing of a real obstruction on these actions, not the
assertion that all derivations of an arbitrary hypersurface have
exactly equation-preserving lifts.

## 5. Every finite equation-adic thickening already has an action

Here is an elementary general lemma. Let \(E_0\) be a polynomial
derivation of \(W\) satisfying \(E_0(F)=0\), and suppose its
induced derivation on \(W/(F)\) is locally nilpotent. Then its
induced derivation on
\[
W/(F^N)
\tag{18}
\]
is locally nilpotent for every integer \(N\ge1\).

For any \(w\in W\), local nilpotence modulo \(F\) gives
\(E_0^{n_0}(w)=Fw_1\). Applying enough further iterates to
\(w_1\) makes its residue vanish, so, since \(E_0(F)=0\),
\(E_0^{n_0+n_1}(w)\in F^2W\). Repeat this process \(N\)
times. It proves nilpotence of each element of (18). Equivalently,
the finite filtration by powers of \(F\) has associated graded
pieces with the original LND, and induction lifts elementwise
nilpotence through the finite filtration.

Exponentiating the induced derivations gives compatible algebraic
additive actions on every thickening (18). The degree in the action
parameter need not be bounded as \(N\) grows. The inverse-limit
action therefore takes values in
\(\varprojlim_N\bigl((W/(F^N))[s]\bigr)\), not necessarily in polynomials
of bounded \(s\)-degree with coefficients in the completed ring.
An actual ambient LND would require a finite nilpotence exponent
for each ambient polynomial, independently of \(N\).

## 6. Exact controls for the missing uniform conclusion

The simple countercontrol suggested independently during this pass is
\[
W=\mathbb C[f,s,w],\qquad
E=\partial_s+fw\partial_w.
\tag{19}
\]
It satisfies \(E(f)=0\), \(E(s)=1\), and induces an LND on
every \(W/(f^N)\), but
\[
E^n(w)=f^n w\ne0\quad\text{for every }n.
\tag{20}
\]
Thus even a genuine polynomial slice together with all compatible
finite-thickening actions does not make the chosen ambient lift an LND.

There is also an irreducible nodal, divergence-free version. In
\(W=\mathbb C[X,Y,Z]\), put
\[
F=Y^2-X^2(X+1),\qquad
H=2Y\partial_X+(3X^2+2X)\partial_Y,
\qquad E=\partial_Z+FH.
\tag{21}
\]
The polynomial \(F\) is irreducible because \(X+1\) is not a
square in \(\mathbb C(X)\). Here \(H(F)=0\),
\(\operatorname{div}H=0\), so \(E(F)=0\) and
\(\operatorname{div}E=0\). Modulo \(F\) the induced action is
the coordinate translation \(\partial_Z\), and all thickenings
again have LNDs. Nevertheless
\[
E^n(X)=F^nH^n(X)\ne0.
\tag{22}
\]
To see the nonvanishing without a finite-pattern inference, \(H\)
maps any nonzero polynomial in \(\mathbb C[X,Y]\) with nonnegative real coefficients and
at least one positive-degree monomial to another such polynomial.
No nonconstant monomial is killed and no cancellation is possible.
Induction beginning with \(X\) proves \(H^n(X)\ne0\) for all
\(n\). This gives a domain control with a double-crossing singular
line and zero ambient divergence, not just a reducible nodal toy.

Both controls also have the different ambient lift \(\partial_s\)
or \(\partial_Z\), which is locally nilpotent. They refute an
implication about a chosen lift; they do not prove that no good
ambient lift exists for the fixed conductor surface.

## 7. The exact remaining gate

For the fixed \(R\), there is no obstruction of the form
"some action cannot be lifted to an equation-preserving polynomial
derivation" or "some finite equation-adic thickening has no additive
action extending it," conditional on a hypersurface presentation.
The normal-frame and full-line arguments prove these statements
for any such presentation, not only for a selected unknown equation.

What is still missing is a polynomial lift with uniform local
nilpotence on \(W\), or an independent obstruction to the existence
of (5). A non-LND lift does not rule out a different LND lift, and
the absence of an ambient LND lift would not by itself rule out the
hypersurface embedding. No assertion here changes those quantifiers.

This pass neither proves \(\mu(R)=4\) nor gives three generators.
It isolates and closes an entire infinitesimal obstruction route,
without repeating Picard, canonical-module, or stable-cotangent tests.
No novelty, human expert review, proof-assistant verification, or
unrestricted cancellation claim is made.

## 8. The separate zero-divergence obstruction is an F-torsion class

An ambient LND has zero divergence, because its polynomial
automorphisms have constant Jacobian determinant one. This is a
necessary condition that all-thickening nilpotence does not impose.
For a hypothetical equation \(F\), define
\[
\mathcal A_F=\{V\in\operatorname{Der}_{\mathbb C}(W):V(F)=0\},
\qquad
\mathcal C_F=W/\operatorname{div}(\mathcal A_F).
\tag{23}
\]
The denominator is a complex vector subspace, not generally an
ideal of \(W\). The quotient is nevertheless a
\(\mathbb C[F]\)-module: for \(V\in\mathcal A_F\),
\(\operatorname{div}(q(F)V)=q(F)\operatorname{div}V\).

Let \(E_0\) be the exactly \(F\)-preserving lift obtained in
Section 4. Its divergence is divisible by \(F\):
\[
\operatorname{div}E_0=Fh.
\tag{24}
\]
Here is the necessary justification. The adjunction generator of
the hypersurface dualizing module is the residue of
\(dX\wedge dY\wedge dZ/F\). Under a tangent lift with
\(E(F)=Fg\), its Lie derivative is multiplication by
\(\overline{\operatorname{div}E-g}\). This follows by
differentiating the ambient meromorphic form and taking residue
on the smooth locus; the identity of the two regular dualizing
sections then holds on the domain \(R\).

The actual additive action of \(D\) fixes a generator of the
trivial dualizing module: its multiplier is a unit in \(R[s]\),
which must belong to \(\mathbb C^*\), since
\(R^*\subset B^*=\mathbb C^*\). Evaluation at the identity
makes that multiplier one. Thus the Lie derivative of the
generator vanishes. With \(g=0\), this proves (24).

All other exactly \(F\)-preserving lifts of the same \(D\)
are \(E_0+FV\) with \(V\in\mathcal A_F\). Their new
coefficient in (24) is \(h+\operatorname{div}V\). Therefore
\[
\theta_F(D)=[h]\in\mathcal C_F
\tag{25}
\]
is independent of the choice of exact lift, and
\[
\theta_F(D)=0
\quad\Longleftrightarrow\quad
\text{there is a polynomial lift preserving F with divergence zero.}
\tag{26}
\]
In fact its target is smaller than the whole quotient:
\[
\theta_F(D)\in\mathcal C_F[F]
:=\{v\in\mathcal C_F:Fv=0\},
\tag{27}
\]
because \(Fh=\operatorname{div}E_0\) and
\(E_0\in\mathcal A_F\). These statements are complex-linear
obstruction statements, not an assertion of \(W\)-linearity.

There is an exact differential-form description. Contraction
with the ambient volume identifies vector fields with polynomial
two-forms. Under that identification,
\[
\mathcal C_F\cong
\Omega_W^3\Big/d\{\alpha\in\Omega_W^2:dF\wedge\alpha=0\}.
\tag{28}
\]
Indeed \(dF\wedge\iota_V\mathrm{vol}=V(F)\mathrm{vol}\)
and \(d\iota_V\mathrm{vol}=\operatorname{div}(V)\mathrm{vol}\).
The larger, usual Brieskorn-style quotient
\(\Omega_W^3/(dF\wedge d\Omega_W^1)\) surjects onto (28),
since \(dF\wedge\beta\) lies in the displayed kernel.
Exactness at the relevant Koszul spot would imply equality,
but cannot be assumed for a gradient with the nonisolated
critical curves present here. It is not asserted to be necessary:
extra Koszul classes may have zero differential or contribute
nothing new after applying the exterior derivative.

Neither the module \(\mathcal C_F[F]\) nor the class (25)
has been computed for an unspecified hypersurface presentation
of the fixed surface. Thus (23)-(28) identify a precise next
test, not a new nonzero obstruction. If the class vanishes,
local nilpotence is still not implied: the irreducible nodal
control (21) is already divergence-free. If the class is
nonzero for a particular action and embedding, that excludes
its ambient LND lift, not the hypersurface embedding itself.

## Finite exact verification

The independent standalone
[hypersurface_lifting_checks_pass31.py](hypersurface_lifting_checks_pass31.py)
imports only unittest and SymPy. Its five methods cover the three
actual normal slopes, a nonzero Jacobian-annihilator obstruction,
the possible critical point outside the zero hypersurface, an exact
polynomial lift and divergence corrections, and both
all-thickening/non-LND controls. The final targeted run passed
five methods in 0.198 seconds:
```
/opt/anaconda3/bin/python research/hypersurface_lifting_checks_pass31.py
```
The unknown hypersurface equation is neither instantiated nor
discovered by these tests. The global conormal and ideal-membership
arguments are written proofs, and the all-order conclusions require
their displayed inductive arguments. The companion
[finite-thickening note](finite-thickening-algebraization-pass31.md)
gives a stronger general criterion and quantitative algebraization
test; it is not needed for the conditional theorem proved here.

## Sources actually read

[^regular]: The Stacks Project, [Section 31.22, Lemmas 31.22.5 and 31.22.12](https://stacks.math.columbia.edu/tag/0638), including their proofs, and [Lemma 10.69.2](https://stacks.math.columbia.edu/tag/061M), including the full regular-sequence-to-associated-graded proof. These supply the regular immersion and symmetric normal-algebra facts. The actual global two-section frame is proved in (8)-(10), not supplied by a general freeness assumption.
[^completion]: The Stacks Project, [Lemma 10.97.3, Tag 00MC](https://stacks.math.columbia.edu/tag/00MC), statement and proof directly read: the completion of a Noetherian local ring is faithfully flat. The formal lifting of a minimal hypersurface presentation is reconstructed in Section 3. No analytic approximation or global coordinate theorem is used.
[^jacobian]: R. Epure and M. Schulze, [*Hypersurface singularities with monomial Jacobian ideal*](https://arxiv.org/pdf/2101.04069), version 3, Remarks 1.1 and 1.2 and Definition 1.3, printed pp. 1-2, directly read. These distinguish ordinary and extended Jacobian ideals and contact from right equivalence. The precise formal double-crossing Jacobian equality needed here is independently proved in (16); none of that paper's classification conclusions is needed.
