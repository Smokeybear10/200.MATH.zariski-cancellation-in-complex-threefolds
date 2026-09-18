# Bounded audit of the original-ring recognition dependencies

This audit found no new gap in the selected recognition bridges
used downstream by422. It also produced an actual countercontrol
to several invalid localization shortcuts. It does not recursively
certify422's entire proof chain or add a new class of cancellation
candidates to its scope.

The important distinction is between a proved polynomial change
in the original four-ring and a change over a localized coefficient
field. Only the former can supply the ambient-coordinate hypotheses
of the published recognition endpoint.

## 1. The published invariant-coordinate endpoint

The primary statement of Bhatwadekar--Gupta--Lokhande,
[Theorem3.5](https://arxiv.org/html/1501.01438v1#S3.Thm3),
applies to a nonzero locally nilpotent derivation D of
k[T,X,Y,Z], in characteristic zero, with D(T)=0 and regular
kernel. It concludes that the kernel is a polynomial two-ring
over k[T]. The variable T must be an ACTUAL polynomial coordinate.

For the present globally sliced four-ring B=A[u], regularity
does not require cancellation. The slice identifies A with B/(u).
Writing E in the original polynomial coordinates gives

    1=E(u)=sum_i E(x_i)*partial_i(u).

Thus the hypersurface u=0 has no singular points over C.
It follows that A is smooth, hence regular. Once an invariant
ambient coordinate has separately been constructed, the primary
theorem legitimately recognizes A.

This reasoning does not show that every regular kernel contains
an ambient coordinate. Using the theorem before constructing one
would assume a principal part of the problem.

## 2. The actual stable-three-ring route

Daigle's theorem, as stated in Dasgupta--Gupta,
[Theorem4.8](https://arxiv.org/html/1701.03635v1), applies to an
irreducible LND D on a polynomial three-ring over a
characteristic-zero field when an actual variable X satisfies
DX nonzero and D^2X=0. It supplies a polynomial coordinate frame
containing an invariant coordinate. It does not require a slice
for that restricted D.

In the constant-projection branch of337 and298, the original
slice presentation supplies the global auxiliary derivation

    P=a0*N-(N X)*E,     X=a0*u+x0,     N(u)=0,     N(a0)=0.

On A it is a0*N, while P(u)=-N(x0). This proves local nilpotence
on the ORIGINAL A[u]: each element of A is killed by an iterate,
and P^r(u)=-a0^(r-1)*N^r(x0) for r>=1. Both coefficient
derivations preserve A. No generic-field extension is needed.

The literal rows in that branch give

    P(X)=P(Y)=0,   P(Z)=tau,   P(W)=X*tau,   tau != 0.

The actual shear S=W-XZ has inverse W=S+XZ. Therefore
P=tau*partial_Z on B=C[X,Y,S][Z], and its entire kernel is
R=C[X,Y,S], even when tau is not a unit. Since P commutes
with E, this actual polynomial three-ring is E-stable.

The restriction delta=E|R is nonzero and satisfies
delta(X)=a0, delta^2(X)=0. Its coefficient gcd c divides the
invariant a0, so factorial closure makes c invariant. Primitive
division D=delta/c is an irreducible LND on R, still with
DX nonzero and D^2X=0. The preceding primary theorem supplies
an invariant coordinate of R, hence of B=R[Z]. Section1 then
applies to the original E.

This verifies the original-ring bridge in that branch. It does
not independently re-prove every earlier scalar argument that
reduces to the branch.

## 3. Corrected301 produces an actual lower-degree frame

The original301 Section3 incorrectly claimed its auxiliary
derivation fixed Y. Its mandatory
[correction](principal-paraboloid-affine-second-potential-pass301-correction-working.md)
explicitly withdraws that argument and replaces it by a full
scalar contradiction. The audited downstream notes use this
correction, not the withdrawn fixed-ring assertion.

In the corrected ell_s nonzero, ell_ss=0 case, the coefficient
argument gives complex constants c,f0,f1,f2 and the identity

    Rcal=Y^2+XW-X^2Z=y^2+rX,    s-c*r=f2*t^2+f1*t+f0.

The first actual map is

    Z1=Z-c*Rcal,    W1=W-c*X*Rcal,

with X,Y fixed. It preserves Rcal, so its polynomial inverse
adds the same displayed terms, expressed in the new coordinates.
The second map is the actual triangular shear

    W2=W1-f2*Z1-f1*Y-f0*X^2.

Its inverse is polynomial because every fi is complex. The
resulting actual frame (X,W2,Y,Z1) has degrees(1,<=1,2,2).
If W2 has degree zero, Section1 applies; otherwise the exact1122
working theorem257 applies with its retained dependencies.

There is no requirement that the old initial ideal or selected
intrinsic partial survive these maps.257 accepts an actual
exact1122 frame without that old principal-kernel condition.
A coefficient-field map with a similar degree pattern would
not justify this use.

## 4. The intrinsic quotient input in the nice-action route

The retained quotient note applies Kaliman--Saveliev to
X=Spec A with X times A1 isomorphic to A4. The cylinder makes
X smooth and contractible. Restricting the smooth projection
A4 to an affine three-plane transverse to one fiber gives a
dominant map A3 to X, so the required domination hypothesis
is verified without assuming X is A3.

The primary [Lemma2.1 and Corollary2.8](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf)
then give an affine-plane quotient for any nonzero intrinsic
additive action, with nonempty curve fibers. Together with
regularity, the equidimensional fibers justify miracle flatness.
The paper's product recognition additionally requires a FREE
intrinsic action. Existence of an intrinsic LND alone does not
supply freeness.

This supports the specified common-plane/fiber input used by
the conditional quadric proof80. It is not a shortcut to
cancellation for all sliced four-rings.

## 5. The targeted geometric transfer in the nice branch

Geometry independently challenged the no-apex80 bridge rather
than treating repeated citations as verification. The published
[de Bondt Theorem3.8(i)](https://arxiv.org/html/1501.04845v3)
applies to the indicated homogeneous quasi-translation in
dimension five, with Jacobian rank three. It supplies intersecting
GN-planes through pairs of image points.

The saved proof removes the image component's intersections
with other zero-set components before putting the GN-planes
inside that component. After projectivizing, its complete
incidence argument derives a smooth quadric surface from two
covering line families. It does not assume smoothness, apply
a Hessian theorem to a nongradient map, or use the unavailable
no-linear-invariant hypothesis in dimension five.

The audited proof still retains its earlier rank and apex
identities. The conclusion of this audit is that the published
geometric transfer and the incidence argument introduce no
new gap, not that all earlier nice-action inputs are certified.

The current [Cid preprint, Theorem5.4](https://arxiv.org/html/2604.03471v1)
is consistent with this boundary: it gives a conjugacy and
linearization criterion, not a general polynomial-kernel theorem
in dimension four. This targeted comparison is not a novelty
audit or evidence of the priority of any local working theorem.

## 6. An actual negative control for invalid upgrades

The separately reviewed
[control424](principal-paraboloid-nonunit-speed-actual-control-pass424-working.md)
is a genuine polynomial automorphism of a translation action.
It satisfies the principal1222 full initial kernel and both
actual returns, with complete scalar J=-a0^4, but

    a0=EX=T is nonunit,
    N=-T^3*partial_V has no global slice on A=C[T,V,H],
    v=-V/T^3 and w=-V/T-T^2 are not in A.

Its initial kernel, exact selected partial, inverse maps and
full scalar are verified explicitly, not only on a rational
ansatz. It rules out inferring polynomial entry of the generic
parameter from any of those chart gates alone.

The control has k_s=0. It does not realize422's nonzero-coupling
family or contradict that theorem. No improper EX-unit assumption
was found in the freshly inspected264 and259.

## 7. Precise coverage of this audit

| Proof bridge | Outcome of this pass | Boundary still retained |
| --- | --- | --- |
| Published invariant-coordinate recognition | Hypotheses match after an actual coordinate is constructed. | Does not construct that coordinate. |
| 249 and256 endpoints of257 | Actual stable three-ring or explicit invariant coordinate and polynomial inverse checked. | Not a recursive proof of157,248,250,252--255 or156. |
| 337/298 constant-projection endpoint | Global auxiliary LND, actual kernel three-ring and primitive restriction checked. | Earlier coefficient reductions are separate inputs. |
| Corrected301 degree lowering | Full scalar correction and both actual inverse maps checked. | Subsequent257 retains its stated dependencies. |
| 330,344,346 composition | Uses the named endpoints with their stated restrictions. | 297,334,339--342,345 were not re-certified by Jet's bounded audit. |
| Three-good156 case split and selected dense bridges | No circular cancellation step found in the reviewed sources. | Whole historical rank, signed-tail and normalization chains remain retained. |
| No-apex80 geometric transfer | Exact published hypothesis and full incidence argument checked. | Earlier74/76, good-direction77--79 and all-double-adjoint inputs are not recursively certified. |
| Underlying actual chart264 | Localization and scalar survive the nonunit-speed control424. | No entry theorem for arbitrary candidates, nor nonzero-coupling realization. |

In particular, this pass does not upgrade422 from a conditional
working theorem to an independently established, publication-ready
result. No new field, dimension, time-degree profile or coupling
range has been recognized by the audit.

## 8. Evidence and next proof obligation

Root revalidated the current README and ledger in450c66/5054fa,
with matching held hashes6a5a77, and read the writing guide in5a8ed3.
Primary BGL and DG statements areturn4623view0--1. The exact
Kaliman--Saveliev statements areturn4627view0; the current Cid
comparison isturn4628view0--1. Root read264 in8be2d5, the
intrinsic quotient note inf17150, quadric80 in671205, no-apex80
in8ff1a2, and the301 correction in3dacbb.337's full argument
and the actual301 maps were read in051839 and41825f.

General read257,249,256 completely in efff15,3d0a99,2bf396
and rehashed f2bd7e. It independently checked both primary
recognition hypotheses and reconstructed256's scalar, invariant
and inverse identities. Jet's full330/337/344/346/298/301 and
correction reads, final rehash93b3ac, and fresh0412c7/46bcfe
check the actual degree-lowering and corrected-scalar bridges.
Geometry's full156 read is0a57cd+3d795a; its final no-apex80
and apex76 reads arebc37b1/e34a63, with rehashadf88b and primary
de Bondt readsturn4630view0/turn4631view0. Their bounded reports
explicitly preserve the unreviewed dependency lists above.

Root control e7e422 and General independent e9bc7f verify424's
full identities. General's complete held424 review is9087ab
at SHA ccfeb259bab5593e7498644ea8289a262aee53fa77b047cac6858ed718a04e8d.
Finite algebra checks do not certify the field, geometric or
universal recognition arguments.

The next task remains a mathematically substantive gap, not an
automatic extension from reviewed special cases: either reduce
general coupling in the actual principal chart by a legitimate
ambient map, or prove a recognition argument that handles it.
Any attempted shortcut must survive424 and the older actual
countercontrols. The global arbitrary-frame entry problem
remains separate and unresolved.

No saved checker was executed, imported, compiled or rerun.
No earlier proof was silently repaired or broadened, and no
external contact, submission, formal certification or historical
novelty claim occurred.
