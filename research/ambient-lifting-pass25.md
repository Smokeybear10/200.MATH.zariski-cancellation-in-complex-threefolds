# Ambient lifting at the nodal divisor: a multiplication gate and its boundary

The fixed action cannot come from a single relative Danielewski
modification at the node. Its restricted invariant algebra needs two
new algebra generators over the nodal base, while every such one-step
model supplies only one.

A different potential obstruction fails: the actual pinched surface
is faithfully flat over the prescribed nodal base. The nonflatness
over its larger invariant ring from pass 24 is therefore not an
ambient-flatness contradiction.

These statements do not decide whether an arbitrary primitive LND
on \(\mathbb C^{[3]}\) can have the prescribed nodal plinth component.
No such LND, hypersurface embedding of the fixed surface, or
nonfree normalization-module defect in \(\mathbb C^{[3]}\) is
constructed here.

## 1. Fixed rings and the problem being tested

Use the same gluing, action, and normalized coordinates as in
[pass 24](nodal-hypersurface-pass24.md):
\[
B=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),\qquad d=u^4-1,
\]
\[
R=B\times_{\mathbb C[t]^6}\mathbb C[t]^3,\qquad
\partial=u\big((u-1)(u-i)\partial_y+(2y-1)\partial_z\big).
\]
The conductor pairs, in the original order, have root pairs
\((1,i),(1,-i),(-1,i)\). The split or ordinary line labels and
the shared \(t\) are unchanged.

Set
\[
e=du,\quad v=du^2,\quad w=du^3,\qquad
T=\ker(\partial|_R)=\mathbb C+d\mathbb C[u],
\]
\[
A_0=\mathbb C[d,v]
  =\mathbb C[d,v]/(v^2-d^2(d+1))\subset T,\qquad
\mathfrak n=(d,v)\subset A_0.
\tag{1}
\]
The presentation of \(A_0\) uses independent symbols before the
displayed identification with its subring in \(R\).

The proved pass-24 data used below are
\[
T=A_0\oplus du\,\mathbb C[u^2],\qquad
T/\mathfrak nT=\mathbb C[e,w]/(e,w)^2,
\tag{2}
\]
\[
I=dB=(d,v)R,\qquad R/I=\mathbb C[t]^3.
\tag{3}
\]
For any hypothetical ambient extension \(D\) on \(W=\mathbb C^{[3]}\)
with \(C=\ker D\), an irreducible invariant \(P\), and the prescribed
identification \(C/(P)=A_0\), the restriction sequence is
\[
0\longrightarrow A_0\longrightarrow T
\longrightarrow (W/DW)[P]\longrightarrow0.
\tag{4}
\]
Thus the required defect is the rank-one, nonfree normalization
module \(\mathbb C[s]\), \(s=u^2\), not an arbitrary torsion module.
Here \(W/DW\) is a \(C\)-module, not a quotient algebra.

## 2. The nodal divisor must actually divide the plinth

Let \(D\ne0\) be an LND on \(W=\mathbb C^{[3]}\), let \(p\)
generate its plinth ideal in \(C=\ker D\), and let \(P\in C\)
be irreducible. If \(P\nmid p\), then
\[
\big((W/DW)[P]\big)\otimes_{C/(P)}
                   \operatorname{Frac}(C/(P))=0.
\tag{5}
\]

Indeed localize \(C\) at its prime \((P)\). The element \(p\) is
then a unit. A minimal local slice gives
\(W\otimes_C C_{(P)}=C_{(P)}[r]\) and \(D=p\partial_r\).
Integration in characteristic zero makes this derivation surjective.
Localization is exact, so the localized cokernel and its
\(P\)-torsion vanish. This is exactly (5).

Consequently the rank-one defect (4) forces \(P\mid p\).
Choosing a nodal invariant unrelated to the actual plinth of an
existing family cannot realize this gate. The argument does not
assert the absence of torsion supported only at special closed
points when \(P\nmid p\), and it does not say that arbitrary
plinth factors must be coordinates.

## 3. The actual map to the nodal base is faithfully flat

**Proposition.** The inclusion \(A_0\hookrightarrow R\) is faithfully
flat. At each closed point of the three conductor lines, the completed
local map is a formal power-series extension of the completed
nodal local ring.

Here is the complete local calculation. Let a closed point \(q\) lie on a
conductor pair with normalized roots \(r_j,r_k\). In all three
pairs,
\[
r_j^2=1,\qquad r_k^2=-1.
\tag{6}
\]
At either normalization preimage of \(q\), \(d\) is a local
transverse parameter, since \(d'(r)=4r^3\ne0\). The shared conductor
parameter \(t\), centered at \(q\), lifts to a second formal
parameter. The normalization's two completed local rings are
therefore \(\mathbb C[[d,t]]\).

On the branch at a root \(r\), the exact formal expressions are
\[
u=r(1+d)^{1/4},\qquad
v=r^2d(1+d)^{1/2}.
\tag{7}
\]
Fractional powers mean the unique formal binomial series with
constant term one. They are not algebraic inverses asserted to
lie globally in \(R\).

The nodal base completion itself is
\[
\widehat{(A_0)_{\mathfrak n}}
 \cong \mathbb C[[d]]\times_{\mathbb C}\mathbb C[[d]],
\quad
v\longmapsto\big(d\sqrt{1+d},-d\sqrt{1+d}\big).
\tag{8}
\]
For example this follows by factoring
\(v^2-d^2(d+1)\) into its two distinct formal branches;
their intersection ideal gives their common residue field.
The surface pinch at \(q\) has exactly the same two base branches,
now with the common \(t\):
\[
\widehat R_q
 \cong \mathbb C[[d,t]]
             \times_{\mathbb C[[t]]}\mathbb C[[d,t]]
 \cong \widehat{(A_0)_{\mathfrak n}}[[t]].
\tag{9}
\]
The last isomorphism can also be checked coefficient by coefficient
in \(t\). Formula (7), including its opposite signs, proves
compatibility with the actual map from \(A_0\), rather than just
an abstract isomorphism of nodal local rings.

A power-series extension of a Noetherian ring is flat: view it as
the completion of its polynomial extension. Noetherian local
completion is faithfully flat. Thus (9) implies that \(R_q\)
is flat over \((A_0)_{\mathfrak n}\), by faithfully flat descent
through \(R_q\to\widehat R_q\). These completion facts, with proofs,
are [Stacks 00MB](https://stacks.math.columbia.edu/tag/00MB) and
[00MC](https://stacks.math.columbia.edu/tag/00MC).

Every point of \(R\) over \(\mathfrak n\) is a conductor point by
(3). Away from that fiber the base is smooth. Its non-generic
local rings are discrete valuation rings, and \(R_q\) is
torsion-free over them because \(A_0\hookrightarrow R\) is an
inclusion of domains. It is therefore flat there as well.
At the generic point the base is a field. This proves flatness
everywhere, including the nonclosed points by localization.

The map on spectra is surjective. Indeed the normalization
\(\operatorname{Spec}B\to\operatorname{Spec}R\) is finite and
surjective; every \(u\)-fiber of \(B\) is nonempty; and the
composite normalized base map is \(u\mapsto s=u^2\), followed
by the finite normalization of \(A_0\). It covers every closed
point, and the generic point is covered by dominance. Flatness
and surjectivity prove faithful flatness.

This passes a genuine necessary condition for an ambient
affine-three-space quotient. It does not contradict the proved
nonflatness of \(R\) over \(T\): these are different base rings.

## 4. A sharp relative algebra-generator obstruction

**Lemma.** \(T\) is not monogenic as an \(A_0\)-algebra, even
after localization at \(\mathfrak n\). It is generated by exactly
two new algebra generators over \(A_0\).

If it were generated by a single element, its fiber (2) would
be a monogenic \(\mathbb C\)-algebra. But every element of this
fiber is \(a+be+cw\), and
\[
(be+cw)^2=0.
\]
Its generated algebra has vector-space dimension at most two,
whereas the whole fiber has basis \(1,e,w\) and dimension three.
This is a contradiction. Conversely \(T=A_0[e,w]\), by the
four-generator presentation of \(T\) in pass 24.

The obstruction includes every change of a proposed generator by
an \(A_0\)-dependent shift or unit multiplier. It concerns the
entire fiber algebra, not only its reduced point or its generic
quadratic field extension.

**One-step exclusion.** Let \(C_*=\mathbb C[D_0,V_0]\), let
\[
P=V_0^2-D_0^2(D_0+1),\qquad k\ge1,
\]
and consider a relative one-step algebra and derivation
\[
W_F=C_*[\rho,Z]/(P^kZ-F(D_0,V_0,\rho)),
\]
\[
D_F(C_*)=0,\qquad D_F\rho=P^k,\qquad D_FZ=F_\rho.
\tag{10}
\]
Suppose its restriction \(W_F/(P)\) is an integral surface,
\(C_* /(P)\hookrightarrow W_F/(P)\), and its induced derivation
is nonzero. Then this restricted action is not the fixed action
on \(R\), under an isomorphism that identifies the base image
with \(A_0\).

For the proof, put
\[
K=A_0[\rho]/(\overline F).
\]
The stated assumptions make \(K\) a domain, and
\[
W_F/(P)=K[Z],\qquad
\overline{D_F}=\overline{F_\rho}\,\partial_Z.
\tag{11}
\]
The coefficient is nonzero. In characteristic zero, comparison
of polynomial coefficients in \(Z\) gives
\[
\ker\overline{D_F}=K.
\tag{12}
\]
This is monogenic over \(A_0\), contrary to the lemma.

No monicity assumption on \(F\) is needed for this exclusion.
Nor is \(W_F\) assumed to be a polynomial ring, smooth, or
factorial. In particular it excludes any member of (10) that
happened to be an affine-three-space algebra with the required
relative action. The same argument works after localizing the
base at any element nonvanishing at the node.

This is not an obstruction to an arbitrary \(\mathbb A^3\)
embedding of \(R\), or to arbitrary multi-stage affine
modifications. It does not claim a lower bound on an unspecified
canonical factorization's length unless that factorization is
known to have exactly the one-step form (10) at the node.

## 5. An actual algebraic first attempt, and its exact failure

The most direct quadratic center produces
\[
W_k=\mathbb C[D_0,V_0,\rho,Z]/
 \big(P^kZ-\rho^2+D_0V_0\big),\qquad k\ge1,
\]
\[
D_k\rho=P^k,\qquad D_kZ=2\rho,\qquad
D_kD_0=D_kV_0=0.
\tag{13}
\]
This is a genuine algebra with a genuine LND, not the
module-only operator from pass 24.

The defining polynomial is primitive and linear in \(Z\):
\(P\) and \(\rho^2-D_0V_0\) are coprime in
\(\mathbb C[D_0,V_0,\rho]\). Hence \(W_k\) is a domain.
Alternatively its monic relation in \(\rho\) gives a free
\(C_*[Z]\)-module with basis \(1,\rho\).

Localizing at \(P\) gives \((C_*)_P[\rho]\), so the kernel
is contained in \((C_*)_P\). The displayed free decomposition,
compared in the fraction field over \(C_*\), shows
\(W_k\cap\operatorname{Frac}C_*=C_*\). Thus
\[
\ker D_k=C_*.
\]
The ring \(W_k/(P)\) is a domain: in the normalization of \(A_0\),
\(D_0=s^2-1,V_0=s(s^2-1)\), and
\(D_0V_0=(s^2-1)^2s\) is not a square in \(\mathbb C(s)\).
The monic quadratic in \(\rho\) is therefore irreducible and
its quotient over \(A_0\) injects into its fraction-field quotient.

It follows that \(P\) is prime in \(W_k\). Also \(\rho\notin PW_k\).
A common element divisor of \(P^k\) and \(2\rho\) would have
to be a unit: primality of \(P\), applied repeatedly to a
factorization of \(P^k\), makes every divisor a unit times a
power of \(P\). Therefore \(D_k\) is primitive in the
element-divisor sense.

Its restricted invariant ring is nevertheless only
\[
K=A_0[\rho]/(\rho^2-dv)=A_0\oplus A_0\rho.
\tag{14}
\]
Under \(\rho\mapsto e\), this is the proper subring
\(A_0[e]\subset T\). The omitted invariant is \(w=du^3\).
The cokernel of invariant restriction is the free rank-one
module \(A_0\rho\), rather than the required nonfree
normalization module. At the node its finite invariant fiber
has length two, rather than three.

There is also a decisive ambient failure: the entire line
\(D_0=V_0=\rho=0\) is singular in \(W_k\). Every first partial
derivative of its defining equation vanishes there, for every
\(k\ge1\). Thus \(W_k\not\cong\mathbb A^3\).
The actual fiber over the node is
\(\mathbb C[\rho,Z]/(\rho^2)\), a doubled line, not the three
reduced lines of the fixed surface.

These failures do not show that no further modification can
repair this center. Such a repair would have to change the
special invariant algebra and the actual node fiber, not just
rename variables in (13).

## 6. Primary-source scope and the remaining question

Kaliman's final author version,
[*Free C+-actions on C3 are translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
Proposition 3.2 and Theorem 5.2(i), was reread. Its retained
component conclusion concerns normalization by \(\mathbb A^1\);
the proof also controls the intermediate fiber over a
self-intersection. It does not state that every retained
component is smooth or unibranch. We cannot replace the
prescribed nodal component by a coordinate line using that
result.

Masuda's primary paper,
[*Factorial affine \(G_a\)-varieties with principal plinth ideals*](https://arxiv.org/html/2312.05455),
Section 3, Theorems 3.8–3.9 and the passage before Corollary 3.10,
was read. The normal-form conclusions may localize at an
invariant outside the generic prime of the plinth component.
That element can vanish at its node. The displayed global
one-step specialization there also assumes factoriality of
the divisor's base ring. The present nodal \(A_0\) is not
factorial. Neither passage supplies (10) at this node for an
arbitrary LND on \(\mathbb C^{[3]}\).

The remaining genuine issue is therefore precise: can a
primitive LND on \(\mathbb C^{[3]}\), with this nodal invariant
divisor in its actual plinth, produce the two-generator
restricted invariant algebra and the nonfree defect (4)
through a construction not subject to the one-step exclusion?
This pass gives no construction or impossibility theorem for
that question. It does not promote the earlier module-only
countercontrol to an algebraic example.

## Verification

The standalone
[exact controls](ambient_lifting_checks_pass25.py) import only
unittest and SymPy. They check the four normalized formal
branches and paired signs, the full node-fiber algebra and
failure of monogenicity, the one-step derivation identities,
the singular line and doubled node fiber of (13), and the
proper quadratic-center subring.

The formal local ring argument, flatness descent, kernel
calculation, and all-parameter exclusion are written proofs,
not consequences of a sampled symbolic test.

The targeted run passed all five methods in 1.121 seconds.

~~~sh
/opt/anaconda3/bin/python research/ambient_lifting_checks_pass25.py
~~~
