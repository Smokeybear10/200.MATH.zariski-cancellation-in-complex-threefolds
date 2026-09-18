# All additive actions and automorphisms of the fixed conductor surface

The remaining three-generator embedding question is not decided here.
There is, however, an intrinsic classification: every nonzero locally
nilpotent derivation of the fixed surface has the same kernel, and every
automorphism is the exponential of one of these derivations. Thus changing
the action or applying an arbitrary surface automorphism cannot turn the
remaining all-noninvariant case into an invariant-containing case.

The classification also identifies a nontrivial line bundle of exact
order four spanned by all additive velocities. This is an actual module
of derivations on the fixed surface, not an abstract module model or a
replacement for the missing hypersurface embedding argument.

## 1. The unchanged surface

Retain the normalization, conductor, and scaled gluing of
[pass 23](nodal-elimination-pass23.md):

\[
B=\mathbb C[u,y,z]/(A(u)z-y(y-1)),\quad
A=(u-1)(u-i),\quad d=u^4-1,
\]
\[
R=B\times_{\mathbb C[t]^6}\mathbb C[t]^3,
\qquad I=dB=(d,du)R.
\tag{1}
\]

The pairs, in their fixed order, are
\[
((1,0),(i,0)),\qquad ((1,1),(-i,*)),\qquad
((-1,*),(i,1)).
\tag{2}
\]
Here the split line at \((r,\epsilon)\) has shared parameter
\(t=z/[r(2\epsilon-1)]\), while the ordinary line at \(r\) has
\(t=y/[rA(r)]\). No unscaled replacement of these parameters is used.

Put
\[
\delta_0(u)=0,\qquad \delta_0(y)=A(u),\qquad
\delta_0(z)=2y-1,
\qquad M=\mathbb C u+d\mathbb C[u].
\tag{3}
\]
The derivation \(\delta_0\) is an LND of \(B\); it need not itself
descend to \(R\). The predecessor's specified action is \(u\delta_0\).

## 2. Complete classification of the LNDs

**Theorem.** Including the zero derivation, one has
\[
\operatorname{LND}(R)=\{p(u)\delta_0|_R:p\in M\}.
\tag{4}
\]
Every nonzero member has kernel
\[
T=\mathbb C+d\mathbb C[u].
\tag{5}
\]

First any LND \(D\) of \(R\) lifts uniquely to an LND of \(B\).
For completeness this follows directly from the exponential action:
\(\exp(sD)\), fixing the indeterminate \(s\), is an automorphism
of \(R[s]\) and its fraction field. The integral closure of
\(R[s]\) in that field is \(B[s]\): this extension is integral,
has the same fraction field, and \(B[s]\) is normal since \(B\)
is smooth. Therefore the automorphism preserves \(B[s]\).
The group law inherited in the fraction field gives a polynomial
additive action on \(B\), hence the required LND. This also proves
uniqueness. It does not assume that arbitrary actions on the
normalization descend.

The lifted action preserves the conductor, which is intrinsic to
the inclusion \(R\subset B\). Thus \(D(d)\in dB\). The
principal-ideal property of LNDs gives \(D(d)=0\), hence
\(4u^3D(u)=0\) and \(D(u)=0\). One can prove the property by
the additive LND degree on products: if \(D(d)=dh\ne0\), then
\(\deg_D d-1=\deg_D d+\deg_D h\), an impossibility.[^1]

Localize at \(\mathbb C[u]\setminus\{0\}\). On the generic
fiber \(B_{\mathbb C(u)}=\mathbb C(u)[y]\), an LND annihilating
\(\mathbb C(u)\) has the form \(q(u)\partial_y\). Indeed a
coefficient of positive \(y\)-degree gives nonzero iterates of
\(y\) by leading degrees. Since \(D(y)\in B\cap\mathbb C(u)
=\mathbb C[u]\), initially \(q\in\mathbb C[u]\). For the displayed
intersection, every fiber of \(u\) is nonempty and reduced; a rational
function of \(u\) with a pole at \(u=r\) has negative order along
each component of that fiber and cannot be regular on \(B\).
Differentiating the defining relation gives
\[
A D(z)=(2y-1)q(u).
\tag{6}
\]
At both \(r=1,i\), reduction modulo \(u-r\) gives
\(B/(u-r)=\mathbb C[z]\times\mathbb C[z]\), and \(2y-1\)
is a unit there, with values \(-1,1\). Thus \(q(r)=0\).
Consequently \(q=Ap\) with \(p\in\mathbb C[u]\), and
\(D=p\delta_0\).

On each of the six lines the derivation of the shared parameter is
\[
D(t)=p(r)/r.
\tag{7}
\]
The diagonal subring defining the pinch is preserved precisely when
these two constants agree in every pair. The graph on the four roots
with the three edges (2) is connected. Thus (7) must have one common
value \(c\), or equivalently
\[
p(r)=cr\quad(r=1,i,-1,-i)
\quad\Longleftrightarrow\quad p=cu+dq_1(u).
\tag{8}
\]
This proves necessity and sufficiency for descent. Sufficiency for
local nilpotence follows by restricting the LND \(p\delta_0\) of
\(B\). For nonzero \(p\), its normalization kernel is
\(\mathbb C[u]\); intersecting with \(R\) gives (5), by the same
connected gluing graph. This proves (4).

In particular all LNDs commute, their sum is again an LND, and the
Makar-Limanov invariant is exactly \(\operatorname{ML}(R)=T\).
This assertion is about this nonnormal surface, not about arbitrary
LNDs on hypersurfaces.

## 3. Every automorphism is an exponential

**Theorem.** The additive group of the complex vector space \(M\)
is the full automorphism group:
\[
\operatorname{Aut}_{\mathbb C}(R)
=\{\exp(p(u)\delta_0)|_R:p\in M\}\cong(M,+).
\tag{9}
\]
In particular every automorphism fixes \(T\) pointwise.

Let \(\varphi\) be an automorphism. Since \(T=\operatorname{ML}(R)\)
is characteristic, \(\varphi\) acts on its normalization
\(\mathbb C[u]\). Hence \(u\mapsto\alpha u+\beta\).
The unique nonnormal point of \(T\) has precisely the four roots
of \(d\) as its normalization preimages. Their sum is zero, so
preserving that set forces \(\beta=0\), and then \(\alpha^4=1\).
The lifted automorphism of \(B\) must preserve the set of parameter
values with reducible fiber. That set is exactly \(\{1,i\}\).
Among the four rotations, only \(\alpha=1\) preserves this set.
Therefore \(\varphi(u)=u\).

The generic polynomial line now gives
\[
\varphi(y)=a(u)y+b(u),\qquad a,b\in\mathbb C(u),\quad a\ne0.
\tag{10}
\]
Both coefficients are polynomials. At an ordinary fiber a pole in
(10) cannot cancel identically in its free coordinate \(y\).
At a split fiber, take the maximal pole order of \(a,b\): its
leading numerator has the form \(a_0 y+b_0\), and regularity at
both components requires simultaneously \(b_0=0\) and
\(a_0+b_0=0\). This contradicts a genuine leading pole. Iterating
removes every possible pole. Applying the same argument to the
inverse gives \(a^{-1}\in\mathbb C[u]\), so \(a\in\mathbb C^*\).

The two split fibers require \(a\{0,1\}+b(r)=\{0,1\}\).
Thus either \(a=1\) and \(b(1)=b(i)=0\), or \(a=-1\) and
\(b(1)=b(i)=1\). In the minus case the pair
\((L_{10},L_{30})\) maps to \((L_{11},L_{31})\), which is not
a pair of the fixed conductor equivalence relation. No shift of the
line parameters can repair that mismatch. The minus case is excluded.

We have \(a=1\), \(b=Ap\), and the defining equation forces
\[
\varphi(y)=y+Ap,
\qquad
\varphi(z)=z+(2y-1)p+Ap^2.
\tag{11}
\]
This is exactly \(\exp(p\delta_0)\). Its shifts on the six shared
parameters are \(t\mapsto t+p(r)/r\). The same condition (8)
is necessary and sufficient for descent, proving (9).

This is stronger than ruling out one proposed torus action. It
classifies the full automorphism group, including its potential
discrete elements. It does not assert that automorphisms extend to
any chosen ambient affine space.

## 4. The actual additive-velocity line bundle has order four

For integers \(k\ge0\), put
\[
M_k=\mathbb C u^k+d\mathbb C[u]\subset\mathbb C(u).
\tag{12}
\]
These are finite fractional \(T\)-modules. Since \(u\) and \(d\)
are coprime, direct multiplication gives
\[
M_iM_j=M_{i+j},\qquad M_{k+4}=M_k,
\qquad M_0=T.
\tag{13}
\]
For example an explicit identity witnessing \(M_1M_3=T\) is
\[
u\bigl((1-d)u^3\bigr)+d^2=1.
\tag{14}
\]
An invertible fractional ideal is an invertible module, so (13)
places \(M=M_1\) in \(\operatorname{Pic}(T)\). Its order is
exactly four. If \(M_k=aT\), extension to \(\mathbb C[u]\)
gives \(a\mathbb C[u]=\mathbb C[u]\), so \(a\in\mathbb C^*\)
and \(M_k=T\). The residue vector of \(u^k\) at the four roots
is constant exactly when \(4\mid k\).

The same construction on the actual surface gives
\[
N_k=M_kR=u^kR+dR\subset B,
\qquad N_iN_j=N_{i+j},\quad N_4=R.
\tag{15}
\]
Here \(M_k=Tu^k+Td\): coprimality of \(u^k,d\) shows that
\(d u^k\mathbb C[u]+d^2\mathbb C[u]=d\mathbb C[u]\).
Thus (15) is the pullback invertible module, with its actual image
in the common fraction field. At conductor pairs its elements have
residues proportional to \((r_j^k,r_k^k)\).

Again its order is exactly four. If \(N_k=aR\), extending to the
normalization gives \(aB=B\), because \((u^k,d)B=B\). The
already proved equality \(B^*=\mathbb C^*\) forces \(a\) constant.
Then \(u^k\in R\), which by the connected graph (2) requires
\(4\mid k\). This also shows directly why a nontrivial gluing
class does not disappear upon pullback from \(T\) to \(R\).

The \(R\)-span of all LNDs in \(\operatorname{Der}_{\mathbb C}(R)\)
is exactly
\[
\mathcal V=N_1\delta_0=(uR+dR)\delta_0.
\tag{16}
\]
Multiplication by the nonzero rational derivation \(\delta_0\)
identifies this module with \(N_1\). Its two displayed generators
are actual descended LNDs. At an ordinary point at least one is
nonzero, since \((u,d)=1\) and \(\delta_0\) has no zero on
the smooth normalization. At a conductor point \(u\delta_0(t)=1\).
Thus their velocities span a line at every closed point, although
the resulting invertible module is not globally free.

Every individual nonzero LND has a fixed point. If \(p=cu+dq\)
has \(c=0\), it vanishes on the conductor. If \(c\ne0\), it
is a nonconstant polynomial, is nonzero at the four conductor roots,
and has a zero somewhere else. Its entire ordinary fiber there is
fixed. There is nevertheless no point fixed by all LNDs, by the
preceding two-generator calculation. These statements concern
actual actions and actual fixed loci, not just module ranks.

## 5. Consequences and the exact failed embedding inference

The [pass-29 theorem](global-invariant-embedding-pass29.md) excluded
every generating triple containing an element of \(T\). Equations
(4) and (9) now make this intrinsic: neither changing to another
nonzero additive action nor applying any automorphism of the surface
changes \(T\), even pointwise in the automorphism case. Thus any
three-generator presentation would have three noninvariant generators
for every nonzero additive action on this surface.

If any nonzero action extends to an ambient LND on \(\mathbb C^{[3]}\)
under a hypothetical hypersurface embedding, that ambient LND must
have rank three. An invariant ambient coordinate would restrict to
a forbidden invariant-containing triple; if its restriction were
constant, the hypersurface would itself be a coordinate plane,
contradicting its conductor singularities. Together with the
[finite-Lie recognition theorem](levi-bridge-pass29.md), this also
forces infinite-dimensional closure with the translations of every
ambient polynomial frame. A triangular three-variable LND has an
invariant coordinate: if its first coefficient is a nonzero constant,
successive polynomial integrations straighten it to a coordinate
partial; otherwise its first coordinate is already invariant.
These are conditional restrictions on an
ambient extension, not an assertion that such an extension exists.

The following tempting implication has **not** been established:
\[
\text{a hypersurface presentation of }R
\quad\Longrightarrow\quad
\text{some ambient coordinate restricts to }T.
\tag{17}
\]
Normalization functoriality lifts an action from \(R\) to \(B\),
not to an unrelated polynomial presentation \(\mathbb C[X,Y,Z]\).
Neither the abelian automorphism group nor the nontrivial line bundle
(16) supplies that missing lift or an ambient coordinate. In particular,
one cannot apply the two-variable relative kernel theorem without
first having an invariant ambient coordinate. Doing so would assume
exactly the conclusion needed to close the all-noninvariant gap.

The order-four class is not by itself a hypersurface obstruction:
the earlier computation of \(\operatorname{Pic}(R)\) already allows
torsion, and no theorem excluding this particular velocity module
for hypersurfaces was obtained. No repetition of the previously
vanishing stable-cotangent test is being claimed as new evidence.

This bounded pass therefore stops at the exact all-action and
all-automorphism classification and its nontrivial module. It does
not prove \(\mu(R)=4\), produce a generating triple, or decide
the stronger ambient quotient realization. No novelty, human review,
formal verification, or unrestricted cancellation claim is made.

## Finite verification boundary

The independent standalone file
[all_noninvariant_surface_checks_pass30.py](all_noninvariant_surface_checks_pass30.py)
imports only unittest and SymPy. It checks the actual normalization
derivation, all six scaled line speeds, the degree-three remainder
classifier and negative examples, both polynomial flow inverses and
composition, all affine permutations of the four roots, the excluded
branch swap, the explicit fractional-ideal inverse and residue orders,
and the absence of a common zero of the two displayed velocities.

Command:
```
/opt/anaconda3/bin/python research/all_noninvariant_surface_checks_pass30.py
```
The initial completed run passed all six methods in 0.289 seconds.
These finite identities support but do not replace the written
all-degree classifications, normalization argument, Picard proofs,
or the source-dependent pass-29 embedding obstruction.

## Source boundary

[^1]: H. Flenner and M. Zaidenberg, [*Locally nilpotent derivations on affine surfaces with a C-star action*](https://arxiv.org/pdf/math/0403215), Proposition 1.1 and Corollary 1.2(b), including the proof, printed pp. 3-4, directly read in this pass. The same primary source's Lemma 1.8 proof records normalization lifting in its cyclic-extension setting. The normalization argument needed here is reconstructed directly above, not inferred from that lemma's extra hypotheses. The source's classification results assume normality and are not applied to this nonnormal surface. The conductor, units of the normalization, and gluing-module facts used here are the fully proved fixed constructions in [pass 20](nodal-conductor-pass20.md), [pass 21](nodal-embedding-pass21.md), and [pass 23](nodal-elimination-pass23.md).
