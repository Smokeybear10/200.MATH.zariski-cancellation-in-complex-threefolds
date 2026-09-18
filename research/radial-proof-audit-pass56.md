# Independent audit of the radial obstruction and patching proofs

The current complete versions of
[the radial DVR scope note](radial-dvr-scope-pass56.md) and
[the radial-center patching note](radial-center-patching-pass56.md)
have been independently read through their ends and reconstructed.
No mathematical correction remains requested. In particular, the
patching proof now includes the actual intersection argument needed
after gluing a center on the punctured local base.

## 1. The local obstruction uses the entire residue ring

For an actual intermediate algebra
\(R[X,Y]\subseteq\mathcal B\subseteq L[X,Y]\), with
\(\mathcal B\cap L=R\), regularity of the centered radial operator
first puts both center coordinates in \(R\). Its finite degree-zero
spectral projector gives literal evaluation at this center. Thus the
projectors, although chosen separately for each degree bound, define
one multiplicative unital retraction \(\mathcal B\to R\).
There is no inference that the radial operator is locally nilpotent.

I separately reread Section 2 of
[the inherited residue-degree proof](quadratic-residue-degree-pass46.md).
At a primitive plinth prime, its full residue statement is
\[
\mathcal B_{(\pi)}/\pi\mathcal B_{(\pi)}
=F_\pi[t,s_*],\qquad [F_\pi:\kappa]>1.
\]
The nonzero reduced derivation, finite constant field, and equivalence
between nontrivial constant extension and plinth support all follow
with their stated primitivity, factoriality, and faithful-flatness
inputs. Restricting a supposed residue retraction to the field
\(F_\pi\) is therefore impossible. This is a full-ring obstruction,
not an assertion about the invariant ring of an arbitrary reduction
or about a selected coordinate-image subring.

The obstruction works for every positive plinth multiplicity and
needs only \([F_\pi:\kappa]>1\), not the separate quadratic-cover
classification. A regular center on a closed-base localization would
localize to every divisor through that point. Hence its existence
forces the primitive plinth to be a unit there. The converse is not
proved or used.

## 2. Determinant multiplicities and the actual control

I reread Section 4, equations (13)--(14), of
[the acceleration-divisor extension](acceleration-divisor-extension-pass45.md).
The actual normalized invariant
\(j_0=g_0x_3-f_0x_4\) satisfies
\[
K_3j_0=f_0\Delta,\qquad K_4j_0=g_0\Delta.
\]
Primitive coefficient saturation makes the restrictions of the
determinant fields invariant polynomial multiples of \(D\). The two
displayed values consequently belong to the full plinth. Unique
factorization and \(\gcd(f_0,g_0)=1\) imply \(p\mid\Delta\).
This uses no Bezout unit ideal and proves no equality \(p=\Delta\).
At an extra factor of \(\Delta\) not dividing \(p\), the field
obstruction is absent, but the original numerator conditions still
retain the complete valuation of \(\Delta\). Solvability there is
not established by either audited note.

The polynomial control in Section 3 of the DVR note also checks.
Both displayed coordinate inverse compositions are exact. Its
derivation has coordinate values \((2x_3,2x_3,1,1)\), both good
accelerations equal to \(2\), and exact adjoint heights
\((0,0,1,0)\). The separately chosen commuting fields
\(-D_0\) and \(aE_0-D_0\) have the claimed generic outputs, but
are not being identified with missing independent top-frame fields.

The monic presentation gives faithful flatness over the invariant
plane. At the invariant DVR \((a)\), the residue field extension is
\(\mathbb C(v)[y]/(y^2-v)\), of degree two, and the quotient is
smooth because \((a,2y)\) is the unit ideal when \(v\) is a unit.
The current wording correctly confines this smoothness assertion to
the invariant DVR quotient. The global invariant-plane quotient is
not asserted to be smooth everywhere.

The numerator in the radial formula reduces to
\(v-\bar\eta_u y\). The independent residue basis \(1,y\)
excludes its vanishing. Yet the displayed bad coordinate \(s\) is
already an actual affine generic slice. Thus the control excludes
necessity of the radial test under the weaker stated hypotheses;
it does not realize the remaining independent-defect frame.

## 3. The repaired global patching argument

The finite modules \(P=Rn+Ru+Rv\), \(Q=P/(Ru+Rv)\), and
\(M=\ker(R^2\to\mathcal T)\) are correctly defined even though
\(\mathcal T\) need not be finite. The exact equation for a center
is \(\phi(\eta)=n\), so \(Q=0\) is equivalent to existence.
Height-one solvability makes \(Q\) finite length, not necessarily
zero. The two principal-open solutions exist by exact localization,
and their difference defines the stated choice-independent overlap
class in \(M_{ab}/(M_a+M_b)\).

Vanishing of that class first produces a common pair in
\(R_a^2\cap R_b^2=R^2\). It does not alone show that the target
equation holds globally for an unrestricted target module. The
current proof supplies the missing step explicitly: every height-one
prime lies in \(D(a)\cup D(b)\), so each of the two actual
numerators divided by \(\Delta\) lies in every height-one
localization of \(\mathcal B\). The inherited embedded intersection
then puts both in \(\mathcal B\). This proves the global equation
and the asserted equivalence in precisely the actual-ring setting.

The formal congruence example has exactly
\(M=aR\oplus R\), \(Q=R/(a,b)\), and nonzero overlap coefficient
\(-1/(ab)\) in the indicated basis. It shows that freeness does not
force overlap-class vanishing. It is explicitly not presented as an
actual quadratic graph or an actual frame.

## 4. Verification and source scope

This audit is a complete independent reconstruction of both current
written proofs, including their final wording corrections and the
specified inherited residue and determinant-divisibility arguments.
No new standalone checker, test method, or regression is added.

The primary applicability statements in Section 4 of the DVR note
were checked for consistency with the hypotheses and proof uses
actually written there. I did not independently reread the complete
new Babu--Das and Das--Dutta primary proofs in this audit. Their
reported direct reads are the geometry author's primary-source
verification record. The root reviewer fully read the note and
reconstructed its algebra, but did not freshly read those complete
primary proofs in this turn. This audit claims no additional primary
read, and no original Sathaye proof read is claimed.

The resulting research boundary is exact: the radial sufficient
criterion cannot cross an actual primitive plinth divisor. Neither
note supplies an unrestricted frame, a different low-degree slice
selection theorem, or a cancellation conclusion.
