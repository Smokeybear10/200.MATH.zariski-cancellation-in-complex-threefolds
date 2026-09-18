# Polynomial horizontal motion of a divisor-preserving plane

Allowing the old invariant plane to move with the homotopy parameter does
not remove its obstruction when the plinth divisor is not a fence.
Every polynomial additive horizontal motion preserving that divisor
actually fixes the plane pointwise. This conclusion uses a published
description of plane-curve stabilizers; it is not a new general
linearization theorem.

Applied to the local-slice homotopy, it gives an exact criterion for
horizontal LNDs preserving the old invariant subalgebra, without a bound
on their degrees or an assumption that its coordinates are individually
fixed. It does not exclude horizontal LNDs that change the embedded
invariant subalgebra itself.

## 1. The plane statement

Work over k=C. Put C=k[u,v], A=C[lambda], and take a nonconstant
nonzero p in C. A fence means an effective divisor equivalent under
a plane automorphism to F times A^1, with F a nonempty finite closed
subscheme of A^1. Equivalently its equation is a polynomial in one
plane coordinate, up to a nonzero scalar.[^stampfli]

**Proposition.** The following are equivalent:

1. The divisor Gamma=div(p) is not a fence.
2. Every delta in LND_k(A) with delta(lambda)=1 and delta(p)=0
   fixes C pointwise.

Thus, in the non-fence case, every such derivation is exactly
partial_lambda in the original plane coordinates.
The premise delta(p)=0 can equivalently be replaced by
delta(p) in pA: the usual LND-degree argument turns divisibility
by p into invariance.

The proposition concerns the full polynomial lambda-line. It does
not apply to a localized parameter curve or only to a formal neighborhood.

## 2. Published stabilizer input

Let G=Aut(A^2,Gamma), with its natural closed subgroup structure inside
the polynomial automorphism group. Stampfli's Proposition 3.0.3 states
that a non-fence has an algebraic stabilizer with no nonidentity
unipotent elements.[^stampfli] In characteristic zero, any nontrivial
connected unipotent subgroup contains a nontrivial additive subgroup.
Its elements would be unipotent plane automorphisms, which are excluded.

Consequently G^0 is a torus, possibly the trivial group. This is the
standard algebraic-group implication recorded, for example, in
Milne's Corollary 17.25 for connected group varieties over an
algebraically closed field.[^milne]

Every regular map A^1 -> G whose value at zero is the identity is
constant. Its image belongs to G^0. After identifying this torus
with (G_m)^r, each coordinate of the map is a unit in k[tau].
All such units are nonzero constants, and the value at zero fixes them.

This constancy is about arbitrary regular maps, not only group
homomorphisms. That distinction is essential for the next argument.

## 3. A genuine family of plane automorphisms

Assume Gamma is not a fence and delta satisfies item 2. Its polynomial
flow Phi_tau=exp(tau*delta) on A[tau] obeys

\[
\Phi_\tau(\lambda)=\lambda+\tau,\qquad
\Phi_\tau(p)=p,\qquad
\Phi_{-\tau}\Phi_\tau=\operatorname{id}.
\tag{1}
\]

Fix any scalar c. For a in C define

\[
\psi_{\tau,c}(a)
 =\left.\Phi_\tau(a)\right|_{\lambda=c}\in C[\tau].
\tag{2}
\]

For each tau this is a polynomial automorphism of the plane. Its
inverse is obtained from

\[
\left.\Phi_{-\tau}(a)\right|_{\lambda=c+\tau},
\tag{3}
\]

not from specialization at lambda=c. Indeed Phi_tau carries the
parameter from c to c+tau, so the reverse fiber map starts there.
The group identity in (1) verifies both inverse compositions.
The coefficients of (2) and (3) are polynomial in tau, and their
degrees in u,v are bounded uniformly, since the original flows are
finite polynomials.

Therefore tau -> psi_{tau,c} is a regular map from A^1 to the
plane automorphism group, with its image in G because p is fixed.
At tau=0 it is the identity. By Section 2 it is constant.
Differentiating at zero gives

\[
\left.\delta(u)\right|_{\lambda=c}
 =\left.\delta(v)\right|_{\lambda=c}=0.
\tag{4}
\]

This holds for every c in k. A polynomial in lambda over C vanishing
under all scalar specializations is zero. Hence delta(u)=delta(v)=0.
The value on lambda then identifies delta with partial_lambda.
This proves 1 implies 2.

Conversely, if Gamma is a fence, choose plane coordinates u_0,v_0
with p in k[u_0]. The derivation

\[
\delta=\partial_\lambda+\partial_{v_0}
\tag{5}
\]

is locally nilpotent, sends lambda to one, and fixes p, but does
not fix C. This proves the converse and the precise fence boundary.
The existence in (5) is only on the invariant plane cylinder;
it need not lift to a chosen ambient modification.

## 4. Consequence for the full local-slice homotopy

Let R=k^[3], let D be a nonzero primitive LND with C=ker D=k^[2],
and let its full plinth be pC with p nonzero nonunit. Choose a minimal
local slice Dr=p. For d in sqrt(pC) put

\[
\mathcal B=R[\lambda,w]/((1+\lambda d)w-r),
\qquad \mathcal A=C[\lambda].
\tag{6}
\]

The established two-chart construction gives a primitive vertical
LND Delta with ker Delta=mathcal A and full plinth p*mathcal A.
The [full normalizer proof](coupled-homotopy-pass25.md), Sections 1-2,
shows that any horizontal LND delta of mathcal B satisfying
delta(mathcal A) contained in mathcal A must commute with Delta
and satisfy delta(p)=0. That proof uses the UFD property and
constant units obtained from the actual stable cylinder, not
an assumption that mathcal B is already polynomial.

If div(p) is not a fence, restrict delta to mathcal A and apply
Sections 1-3. It must fix C. The previously proved full-plinth
relative criterion then gives

\[
\boxed{
\begin{gathered}
\exists\,\delta\in\operatorname{LND}_k(\mathcal B),\
\delta(\lambda)=1,\
\delta(\mathcal A)\subseteq\mathcal A\\
\Longleftrightarrow\quad d\in pC ,
\qquad\text{provided }\operatorname{div}(p)\text{ is not a fence}.
\end{gathered}}
\tag{7}
\]

The relative input is the
[common-residue theorem](relative-modification-classification-pass19.md),
Section 5. The slice of delta would identify the lambda=0 and
lambda=1 fibers over C, namely R and R[r/(1+d)], forcing p|d.
Its common residue is one on every plinth component, so connectedness
of the support is not required.

For d=pH the converse is explicit:
delta(lambda)=1, delta(w)=0, and delta|R=HwD. Its coefficient Hw
is invariant under delta, so local nilpotence follows directly.
It fixes C and works whether or not the divisor is a fence.

The non-fence conclusion includes the factor-field argument in the
companion note: if the distinct factors of p generate a field of
transcendence degree two, they cannot all be polynomials in one
plane coordinate. It also covers irreducible non-fence curves,
where that elementary factor argument alone has no force.

## 5. Exact scope and the parameter boundary

The conclusion does not say that a non-fence has no symmetry.
For example, div(uv) has the torus symmetry
(u,v) -> (a*u,a^(-1)*v). What it has no room for is nonconstant
polynomial motion along the entire affine lambda-line starting
at the identity.

On a punctured parameter line, this restriction disappears:

\[
(u,v,\lambda)\longmapsto
(\lambda u,\lambda^{-1}v,\lambda)
\tag{8}
\]

is a regular plane-automorphism family for lambda in G_m and
preserves uv. It is not a polynomial family over A^1.
Likewise the formal family (exp(lambda)u,exp(-lambda)v)
preserves uv but is not polynomial. Neither example contradicts
the proposition.

The [explicit fence control](coupled-homotopy-pass25.md), Sections 5-6,
is complementary: its plinth x^2 is a fence, but no plane-normalizing
horizontal LND lifts to the actual polynomial ambient family.
An unrestricted horizontal coordinate partial exists and sends the
old invariant h outside the old subalgebra. Therefore the fence
boundary on the plane is not a sufficient ambient lifting criterion.

No arbitrary-X recognition theorem follows from (7). The surviving
construction must permit the embedded quotient subalgebra itself
to change, or use a different intrinsic route. The stabilizer and
torus inputs are published results; priority for this application
has not been audited comprehensively.

## Sources

[^stampfli]: I. Stampfli, [*Automorphisms of C^3 Commuting with a C+-Action*](https://arxiv.org/pdf/1406.6246), arXiv:1406.6246v2, Proposition 3.0.3 and Proposition 3.0.5, printed pp. 5-6. Published in *International Mathematics Research Notices* 2015(19), 9832-9856, [DOI 10.1093/imrn/rnu232](https://doi.org/10.1093/imrn/rnu232). The plane-divisor argument uses Blanc and Stampfli's earlier classification, credited in that proof.

[^milne]: J. S. Milne, [*Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*](https://www.jmilne.org/math/Books/iAG2022.pdf), corrected CUP 2022 text, Corollary 17.25, printed p. 360; the connected-group and algebraically closed-field convention is in Section 17(b), printed p. 354.
