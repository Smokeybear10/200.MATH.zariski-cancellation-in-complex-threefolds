# An exact slice classification and limits of two general proof routes

September 13, 2026. Private research continuation.

## Result and scope

The explicit rank-three family now has a complete answer for every
coefficient of the form 1+qr: a slice exists exactly when q is divisible
by f, and every positive case has a polynomial kernel. The earlier
quadratic construction covered only part of this region. A finite
correction covers all of it, and an algebraic orbit argument excludes
every remaining coefficient, in every possible slice degree.

This is a complete working family proof, independently reconstructed
twice. It is not a proof of the unrestricted conjecture
\[
X\times_{\mathbb C}\mathbb A^1\simeq\mathbb A^4
\quad\Longrightarrow\quad X\simeq\mathbb A^3.
\tag{1}
\]
No human expert review, formal proof-assistant verification, or
statement-level novelty determination has occurred. Luo has not
confirmed the corrected dimensional interpretation of the original
email. None of the material has been submitted or sent externally.

The deep-research workflow required separate proof reconstructions,
primary-source checks for the curve argument, and an explicit boundary
between the universal conjecture and the family actually treated.
Failed generalization steps are retained as negative results.

## 1. Exact theorem and degree boundaries

In R=C[x,y,z], for every n>=1, set
\[
f=xz-y^2,\quad r=x^3+yf^n,\quad
h=zf^{2n}+2x^2yf^n+x^5,\quad
D=-\operatorname{Jac}(f,h,\cdot),\quad a=f^n.
\tag{2}
\]
The base is a published canonical local-slice construction. Its
primitive rank-three property, kernel C[f,h], and plinth ideal (ah)
are inherited inputs, not newly discovered here.[^1] Directly,
\[
Dr=ah,\quad Dx=2ar,\quad xh=r^2+f^{2n+1}.
\tag{3}
\]
For every q in C[f,h], let E=D+(1+qr)*partial_t on R[t].
Then
\[
E\text{ has a slice}\iff f\mid q.
\tag{4}
\]
Whenever a slice exists, the proof constructs polynomial coordinates
X,Y,Z,sigma with E=partial_sigma and ker E=C[X,Y,Z].
The sharp low-degree criteria are
\[
\begin{aligned}
\exists\text{ slice of }t\text{-degree}\le1&\iff f^n\mid q,\\
\exists\text{ slice of }t\text{-degree}\le2&\iff f^n\mid q^2.
\end{aligned}
\tag{5}
\]
No degree-zero slice exists. For nonzero q, put ell=v_f(q).

| Coefficient regime | Exact conclusion |
| --- | --- |
| ell=0 | No slice in any degree |
| ell>=n | Minimum t-degree one |
| 2ell>=n>ell | Minimum t-degree two |
| 3ell>=n>2ell | Minimum t-degree three |
| n>3ell>0 | Slice and polynomial kernel; exact minimum degree not determined here |

For q=0, t itself is a slice. The n=1 boundary is included.
The [complete proof](research/radical-noninvariant-pass22.md) supplies
every assumption, formula, inverse, and coefficient comparison.

## 2. Finite correction and global coordinates

On the abstract ring Lambda[x,r,t], with Lambda a Q-domain, a nonzero,
and a,q,h invariant coefficients, put
\[
L=qx/2-at,\quad \rho=r+hL,\quad X=x+L(r+\rho),\quad
\sigma_0=t+\frac{q(X-x)}{2a}.
\tag{6}
\]
The first two quantities are polynomial invariants, preserve
Xh-rho^2=xh-r^2, and together with sigma_0 give an automorphism after
inverting a.

Modulo a, their map is
\[
\phi_0(x)=x+qxr+q^2x^2h/4,\qquad
\phi_0(r)=r+qxh/2.
\tag{7}
\]
If q is nilpotent modulo a, this map has a finite polynomial inverse:
its additive difference from the identity raises powers of the
nilpotent ideal (q). A finite geometric sum is its inverse, including
when the coefficient quotient has zero divisors.

Let K=q^2xr/2+q^3x^2h/8 and lift H=phi_0^-1(K) from the quotient.
The correction
\[
\sigma=\sigma_0-H(X,\rho)/a
\tag{8}
\]
is polynomial, since its numerator is zero modulo a, and E(sigma)=1.
The full map is an automorphism modulo a and after inverting a.
A minimal-denominator argument then proves its inverse polynomial
globally. This is not a formal series asserted to algebraize.

For a=f^n, q is nilpotent modulo a exactly when f|q. To return to
the physical four-variable ring, use the finite curve correction
\[
U=(1+q(f,u^5)u^3/2)^2,\quad
W=u^2(1+q(f,u^5)u^3/2),\quad \psi(u)=uU,
\]
\[
\widetilde P=(W/U)\circ\psi^{-1}\pmod{f^n},\quad
Y=\frac{\rho-X\widetilde P}{f^n},\quad
Z=\frac{h-2\widetilde P Yf^n-X\widetilde P^2}{f^{2n}}.
\tag{9}
\]
Both curve directions are verified. Prime cancellation clears all
forward and inverse denominators in the physical polynomial rings.
The underlying full-ideal affine-modification framework is established
prior work; the required application conditions are checked explicitly.[^2]

When f^n|q^3, H=q^2Xrho/2 already works and gives the displayed
cubic formula in the full note. Combined with (5), it proves the
exact cubic regime, not a minimum-degree formula in all higher regimes.

## 3. The all-degree obstruction

If q(0,H) is nonzero, choose a nontrivial fifth root epsilon and a
nonzero root x_0 of
\[
2+(1+\epsilon^3)x^3q(0,x^5)=0.
\tag{10}
\]
The polynomial is nonconstant with constant term 2. No simple-root
assumption is made.

In the smooth chart with f,x_1,x_2 and x_1x_2 inverted, impose
\[
h_1=h_2,\quad 2+q(f,h_1)(x_1^3+x_2^3)=0,\quad
h_i=x_i^5+f^{2n+1}/x_i.
\tag{11}
\]
The zero-f fiber near (0,x_0,epsilon*x_0) is zero-dimensional.
Dimension bounds give a curve component through this point not
contained in f=0. Normalize it and take its local DVR V.
The exact dimension, normalization, and DVR hypotheses are checked
against standard primary references.[^3]

The actual integral points P_i=(x_i,0,f/x_i,0) lie on the same
E-orbit over the fraction field, with parameter
\[
\tau=\frac{x_2^3-x_1^3}{f^n h_1}.
\tag{12}
\]
Its numerator and h_1 are units, while f has positive valuation:
tau does not belong to V. Equation (11) makes the t-displacement
zero, so both endpoints nevertheless belong to A^4(V).
Any polynomial slice would give S(P_2)-S(P_1)=tau, contradicting
integrality of the left side. This excludes every polynomial degree.

The [first audit](research/radical-noninvariant-audit-pass22.md)
and [second audit](research/all-q-bridge-audit-pass22.md) reconstruct
the finite inverse, physical lift, multiple-root-safe obstruction,
and exact degree boundaries. These are model audits, not expert review.

## 4. A stronger failed general proof step

The [full-center countercontrol](research/center-recognition-pass22.md)
uses the actual n=2 canonical base, p=f^2h, V=1+fh, and, for every
N>=5,
\[
S=\mathbb C[f,h,T],\quad I_N=p^NR\cap S,\quad
J_N=\theta(I_N)S,\quad \theta(T)=VT.
\tag{13}
\]
Both modifications are polynomial three-rings. Nevertheless no
automorphism of S carries I_N to J_N while preserving (fh), even
though no quotient jet or invariant plane is prescribed.

The actual reduced centers (f,T^5-h^3) and (h,T^2+f^5) force
any such map to weighted scalings and an fh-divisible translation.
The scalings lift to the original ring and can be removed.
The induced map on r would then have the form
r/(1+alpha*fh)+fh*B(f,h), alpha nonzero.
Divisibility of the image of f^2y=r-x^3 would require
\[
B(0,x^5)=\alpha x^3,
\tag{14}
\]
which is impossible by exponents modulo five.

Thus changing the prescribed jet or increasing N does not fix this
transport route. A general recognition proof needs more freedom,
such as changing denominator presentations or obtaining coordinates
without one descending ambient automorphism. This does not disprove
cancellation or all possible recognition algorithms.

## 5. The tangent projection also leaves a genuine gap

The [nonlinear-frame note](research/nonlinear-frame-pass22.md)
derives the canonical projected connection and two explicit controls.
For a sliced E on B=A[s]=C^[4], the tangent projection P=I-e*lambda
is idempotent, but the induced connection need not be flat.

The coordinate translation
\[
s=t-x^2,\quad E=y\partial_x+(1+2xy)\partial_t,\quad
a=x-ys,\ b=y,\ c=z
\tag{15}
\]
has an explicit polynomial inverse. Its projected connection has
nabla_(partial_a)(partial_a)=-2b*partial_a and nonzero curvature
R(partial_a,partial_b)(partial_a)=2*partial_a.
The projected coordinate partial (1+2ab)*partial_a is not locally
nilpotent either. These failures occur on a known polynomial kernel.

A second coordinate translation,
\[
s=t-x^2,\quad E_0=-\tfrac12\partial_x+(1-x)\partial_t,\quad
a=x+s/2,\ b=y,\ c=z,
\tag{16}
\]
has a flat torsion-free projected connection with
nabla_(partial_a)(partial_a)=partial_a. A horizontal field requires
F'+F=0 in its a-component, which has no nonzero polynomial solution.
Thus even this flat projected connection has no polynomial horizontal
frame.

A valid conditional lemma remains: on a smooth affine complex
threefold with H^1_dR=0, a commuting derivation basis has an exact
dual coframe. Every locally nilpotent member then has an intrinsic
slice. The missing step is existence of the required commuting frame
containing such a member. Tangent-module freeness is not that step.

## 6. Five actual generators of the auxiliary conductor surface

The [surface-generation proof](research/nodal-generators-pass22.md)
constructs a closed embedding of the fixed pinched surface into A^5.
This is a statement about its actual global coordinate ring, not only
its normalization, local rings, or stable invariants.

After one uniform rescaling preserving the original gluing, its
normalization and conductor are
\[
B=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),\quad d=u^4-1.
\tag{17}
\]
The proof gives explicit polynomial trace and common-parameter lifts
c,tau, and a polynomial beta in two variables. Its five generators are
\[
R=\mathbb C[c,\tau,\zeta,\kappa,d],\qquad
\zeta=z-\beta(c,\tau)u,\quad \kappa=u^2-cu.
\tag{18}
\]
Although u belongs only to the normalization, all five displayed
functions have equal restrictions on each prescribed pair of lines,
so they belong to R. The full coefficient formulas are in the note.
They are algebra generators, not five independent coordinates.

A polynomial Bezout identity recovers y from the generators and u;
z is recovered directly. Hence B=S[u] for the proposed subring S,
and u satisfies its displayed monic quadratic. R is therefore finite
over S. Three exact univariate polynomial gcd certificates exclude
all additional off-conductor point identifications. The exceptional
denominator cases and every conductor pair are treated separately.
Explicit derivatives span each smooth cotangent space and all three
directions of every nodal cotangent space.

Two local Nakayama arguments now give R=S. This step uses finiteness,
unique closed points with equal residue fields, and cotangent
surjectivity on the pinched ring itself. A pointwise bijection or
an immersion of its normalization alone would not suffice.

The proof also excludes two particular three-generator attempts:
no triple retaining both d and du works, because its conductor
quotient would have to generate C[t]^3 with one element; and
{c,tau,zeta} identifies two explicit distinct off-conductor points.
The established minimum-generator bounds are three through five.
No exclusion of every triple or quadruple, no A^3 embedding, and
no required ambient quotient or LND are supplied.

The [independent audit](research/nodal-generators-audit-pass22.md)
reconstructs the point separation and cotangent certificates.
The [seven-method checker](research/nodal_generators_checks_pass22.py)
verifies their exact polynomial identities. These certificates are
finite algebraic parts of the written proof, not numerical sampling.

## 7. Verification and remaining scope

The [new standalone checker](research/radical_nonlinear_checks_pass22.py)
imports only unittest and SymPy. It checks generic and cubic slice
identities, finite quotient inverses, corrected numerators, both full
inverse compositions for an exact example, both physical curve
directions, coefficient equations, orbit endpoints, a deliberately
multiple-root control, and center/connection identities.

The initial targeted execution was interrupted during needless
expansion of terms vanishing in the finite quotient. Composition was
changed to truncate at each multiplication, with the same cases and
assertions retained. All 15 methods then passed in 3.006 seconds.
This was a performance correction, not a failed mathematical identity.
The first full regression completed at 05:45:42 UTC with 466 methods
across 35 suites passing. A final expanded packet run, including the
surface-generation controls, ran from 05:57:14 through 05:58:30 UTC:
all 473 methods across 36 suites passed. The exact execution is in
[verification-pass-22.json](verification-pass-22.json).

The [regression runner](research/run_regression_pass22.py) and the
project README give reproducible commands. Finite examples supplement
the written universal arguments; independent inline checks and repeated
runs do not inflate the number of distinct test methods.

The [targeted priority comparison](research/priority-comparison-pass22.md)
confirms inherited base and degree-module results and identifies an
unresolved full-text comparison with Freudenburg's 2009 family.
It does not establish novelty or exhaustive literature coverage.

The universal gap remains: no reduction puts every slice derivation
on C^[4] into this coefficient family, and no polynomial-recognition
theorem covers every required full-center modification. The negative
controls rule out particular proofs, not the desired conclusion.
General cancellation remains unsolved.

## Sources

[^1]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), Theorem 5.7; G. Freudenburg, [*Canonical factorization of the quotient morphism for a Ga-action on an affine variety*](https://arxiv.org/pdf/1602.08786), Section 8.2. The n=1 degree modules and canonical local-slice machinery are prior work.

[^2]: S. Kaliman and M. Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), Proposition 2.1 and Corollary 2.2. These are full-ideal sufficient lifting statements, not assertions that all isomorphisms descend.

[^3]: The Stacks Project, [dimension and principal ideal bounds](https://stacks.math.columbia.edu/tag/00KD), [finite normalization of varieties](https://stacks.math.columbia.edu/tag/0BXR), and [normal curve local rings](https://stacks.math.columbia.edu/tag/0B8Y).
