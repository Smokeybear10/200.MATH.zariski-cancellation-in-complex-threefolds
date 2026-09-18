# The four-branch quotient and the ambient invariant-lifting obstruction

The descended derivation on the fixed pinched surface has a quotient
curve with **one four-branch point**, not three nodes. That curve is
not a plane curve. Consequently, any extension of this derivation
to a locally nilpotent derivation on \(\mathbb C^{[3]}\) must fail
surjectivity of invariant restriction to the surface.

For the prescribed degree-two map to the nodal cubic, the failure is
determined exactly: its obstruction module must be the normalization
module of that cubic. It has rank one and needs two generators at the
node. The intermediate quotient is also nonflat at every conductor
point, although that is not the flatness statement required of an
ambient affine-three-space quotient.

These are concrete necessary conditions and excluded inference rules.
They neither construct nor rule out an \(\mathbb A^3\) hypersurface
embedding of the fixed surface.

## 1. Fixed surface, action, and notation

Keep the same uniformly normalized surface as in
[the four-generator proof](nodal-elimination-pass23.md):
\[
B=\mathbb C[u,y,z]/(A(u)z-y(y-1)),\qquad
A(u)=(u-1)(u-i),\qquad d=u^4-1.
\tag{1}
\]
Its pinched subring \(R\subset B\) identifies the six conductor
lines in the same three pairs
\[
((1,0),(i,0)),\quad ((1,1),(-i,*)),\quad
((-1,*),(i,1)).
\tag{2}
\]
The shared parameters are still
\(t=z/[u_j(2\epsilon-1)]\) on split lines and
\(t=y/[u_jA(u_j)]\) on ordinary lines. No pair has been changed.

The exact conductor and quotient are
\[
I=dB=(d,du)R,\qquad R/I=\mathbb C[t]^3.
\tag{3}
\]
On the normalization, use
\[
\delta u=0,\qquad\delta y=A(u),\qquad\delta z=2y-1,
\qquad \partial=u\delta.
\tag{4}
\]
This is the predecessor's descended action, up to the harmless
nonzero constant associated with the uniform normalization.
It sends the shared \(t\) to one on each of the six lines.

The kernel in \(B\) is \(\mathbb C[u]\). The graph with vertices
\(1,-1,i,-i\) and edges given by (2) is connected. Hence the exact
restricted kernel is
\[
T=\ker(\partial|_R)
 =\{p(u):p(1)=p(-1)=p(i)=p(-i)\}
 =\mathbb C+d\mathbb C[u].
\tag{5}
\]
This equality is already proved in the
[original conductor construction](nodal-conductor-pass20.md),
Section 4. What follows computes its local algebra and the
consequences for an ambient extension.

## 2. One four-branch point, with an explicit presentation

Set
\[
e=du,\qquad v=du^2,\qquad w=du^3.
\]
Then \(T\) is free over \(\mathbb C[d]\), with basis
\(1,e,v,w\). Indeed reduce powers of \(u\) using \(u^4=d+1\).
Independence follows from independence of the four residue classes
of powers of \(u\) over \(\mathbb C[u^4]\).

The full algebra presentation is
\[
\begin{split}
T=\mathbb C[d,e,v,w]/(&e^2-dv,\ ev-dw,\ ew-d^2(d+1),\\
                    &v^2-d^2(d+1),\ vw-d(d+1)e,\
                      w^2-d(d+1)v).
\end{split}
\tag{6}
\]
For exactness, these relations reduce every product of \(e,v,w\)
to a \(\mathbb C[d]\)-linear combination of \(1,e,v,w\), whose
images are independent. Thus (6) has no hidden extra relations.

The single point over the four roots has maximal ideal
\[
\mathfrak m=d\mathbb C[u]=(d,e,v,w)T.
\tag{7}
\]
Since \(\mathfrak m^2=d^2\mathbb C[u]\),
\[
\dim_{\mathbb C}\mathfrak m/\mathfrak m^2=4.
\tag{8}
\]
Its normalization has four preimages. More explicitly,
\[
\widehat T_{\mathfrak m}\cong
\{(f_1,\ldots,f_4)\in\textstyle\prod_j\mathbb C[[q_j]]:
                    f_1(0)=\cdots=f_4(0)\}
\]
\[
\cong
\mathbb C[[q_1,q_2,q_3,q_4]]/(q_iq_j:i\ne j).
\tag{9}
\]
This follows by completing the four-point pinch; \(d\) has a simple
zero at each normalized root. Thus “four-branch point” here means
the four coordinate axes model (9). It does not mean an ordinary
quadruple point embedded in a plane, whose local algebra is different.

There is only one such point: \(T_d=\mathbb C[u,d^{-1}]\).
In particular \(T\) cannot be isomorphic to a plane curve ring,
because every local cotangent space of a plane curve has dimension
at most two.

A useful additional distinction is
\[
T/dT\cong
\mathbb C[e,v,w]/(e,v,w)^2,
\tag{10}
\]
which has length four. Here \(dT\) is not the conductor ideal
\(d\mathbb C[u]\).

## 3. The prescribed nodal subcurve and its exact defect module

For the same degree-two map as in the predecessor, after scaling
its two plane coordinates, the nodal curve ring is
\[
A_0=\mathbb C[d,v]\subset T,\qquad
v^2=d^2(d+1).
\tag{11}
\]
To match the original cubic \(\mathsf V^2-\mathsf U^3+3\mathsf U=2\),
take
\[
\mathsf U=3d+1,\qquad
\mathsf V=3a_0^2v,\qquad a_0^4=3.
\]
The normalization of (11) is \(\mathbb C[s]\), where
\[
s=u^2,\qquad d=s^2-1,\qquad v=s(s^2-1).
\tag{12}
\]
Thus the normalized map from the surface quotient is \(u\mapsto u^2\).

Even and odd powers of \(u\) give an exact \(A_0\)-module decomposition
\[
T=A_0\oplus N,\qquad
N=du\,\mathbb C[u^2]\cong\mathbb C[s].
\tag{13}
\]
The isomorphism sends \(F(s)\) to \(duF(u^2)\). It is a module
isomorphism, not an identification of the odd summand with a unital
subring. In particular
\[
T/A_0\cong\mathbb C[s].
\tag{14}
\]

Writing \(e=du,w=du^3\) for its two generators, the relations are
\[
ve=dw,\qquad vw=d(d+1)e.
\tag{15}
\]
They give the exact module presentation
\[
A_0^2
\xrightarrow{
 \begin{pmatrix}v&-d(d+1)\\-d&v\end{pmatrix}}
A_0^2\longrightarrow N\longrightarrow0.
\tag{16}
\]
To prove completeness, write a proposed relation
\(\alpha+\beta s=0\) with
\(\alpha=\alpha_0(d)+v\alpha_1(d)\) and
\(\beta=\beta_0(d)+v\beta_1(d)\).
Using \(s^2=d+1\), its even and odd coefficients force
\(\alpha_0=-d(d+1)\beta_1\) and
\(\beta_0=-d\alpha_1\). These are precisely the two columns in (16).

The module \(N\) has generic rank one over \(A_0\).
At its node \(\mathfrak n=(d,v)\), every entry of the presentation
matrix vanishes, and
\[
N/\mathfrak nN\cong\mathbb C^2.
\tag{17}
\]
Thus it is not free there. Its first Fitting ideal is exactly
\((d,v)\).

The scheme-theoretic fiber of \(\operatorname{Spec}T\to
\operatorname{Spec}A_0\) over the node is
\[
T/(d,v)T\cong\mathbb C[e,w]/(e,w)^2.
\tag{18}
\]
It has one underlying point, length three, and two independent
nilpotent directions. There are four points only after normalizing
\(T\). The finite degree-two map is not flat at that point: a finite
flat module there would be free of rank two, whereas (18) has
dimension three.[^flatfinite]

## 4. Why the surface quotient is not flat over its full kernel

There is another exact global module identity:
\[
B=R+Ru^2.
\tag{19}
\]
On every pair in (2), the two values of \(u^2\) are \(1,-1\).
An arbitrary pair of polynomial residues is uniquely
\(c_0(t)+u^2c_1(t)\) on these two lines. Lift the three resulting
pairs of \(c_0,c_1\) from \(R/I=\mathbb C[t]^3\).
The error lies in \(I\subset R\), proving (19).

Multiplying by \(d\) gives
\[
I=(d,v)R.
\tag{20}
\]
Therefore the actual surface fiber over the node of (11) is
\[
R/(d,v)R=R/I=\mathbb C[t]^3.
\tag{21}
\]
This fiber is reduced and has three disjoint affine-line components.
It must not be confused with the fat point (18).

In fact the quotient \(\operatorname{Spec}R\to\operatorname{Spec}T\)
is not flat at any point of the conductor. To see this, localize
at such a point and at \(\mathfrak m\subset T\). The nonzero classes
of \(e,w\) in (18) survive localization, since (18) is supported
only at \(\mathfrak m\). But they become zero in
\(R/(d,v)R\), by (20). A flat local homomorphism is faithfully flat,
and remains injective after tensoring with any module. This
contradicts the displayed nonzero kernel after tensoring with
\(T/(d,v)T\).[^flat]

This is not an obstruction from the known faithful flatness of
affine-three-space quotients. That theorem concerns the ambient
kernel \(C\), and after restriction the smaller ring \(C/(P)\),
not the full kernel \(T\) of the restricted derivation.

## 5. The exact invariant-restriction sequence for an ambient extension

Suppose there is a hypersurface presentation
\[
R\cong W/(P),\qquad W=\mathbb C[X_1,X_2,X_3],
\]
and an LND \(D\) on \(W\) inducing the specified nonzero \(\partial\).
Since \(D(P)\in(P)\), the LND-degree identity forces \(D(P)=0\):
if \(D(P)=Pa\ne0\), additivity of LND degree would give
\(\deg_D P-1=\deg_D P+\deg_D a\), a contradiction.
Put \(C=\ker D\). The standard affine-three-space kernel theorem
gives \(C\cong\mathbb C^{[2]}\).[^lnd]

The restriction injection is
\[
C/(P)C\hookrightarrow T,
\tag{22}
\]
because \(C\cap PW=PC\): if \(Pb\) is invariant, then
\(PDb=0\), and hence \(b\in C\).
However, (22) is **necessarily not surjective**, by (8).
More locally, the image can span at most two of the four
cotangent directions at \(\mathfrak m\).

There is a precise module measuring this failure. Define
\[
\mathcal H=W/D(W)
\]
as a \(C\)-module, not as a quotient ring: \(D(W)\) is generally
not an ideal of \(W\). Then
\[
0\longrightarrow C/(P)C
\longrightarrow T
\xrightarrow{\ \partial_P\ }\mathcal H[P]
\longrightarrow0,
\qquad
\mathcal H[P]=\{q\in\mathcal H:Pq=0\}.
\tag{23}
\]
For a lift \(a\in W\) of an invariant \(\bar a\in T\), write
\(Da=Pb\) and set \(\partial_P(\bar a)=[b]\).

This is an elementary exact sequence. Replacing \(a\) by \(a+Pc\)
changes \(b\) by \(Dc\), so the map is well defined.
Its kernel consists precisely of invariant lifts: if \(b=Dc\),
then \(a-Pc\in C\). Conversely, if \(P[b]=0\), choose
\(a\) with \(Da=Pb\); its residue is invariant and maps to \([b]\).
The construction is \(C/(P)C\)-linear.

For an ambient realization compatible with the prescribed nodal
map (11), the image of (22) must be exactly \(A_0\).
Equations (14), (16), and (23) then force
\[
\boxed{\mathcal H[P]\cong \mathbb C[s]\quad
       \text{as an }A_0\text{-module}.}
\tag{24}
\]
Thus an acceptable ambient derivation must carry a nonzero
\(P\)-torsion obstruction module of rank one, with the exact
two-generator nodal presentation (16). In particular, neither
\(P\)-torsion-freeness of \(W/D(W)\) nor surjective invariant
restriction is available to such a construction.

Nonzero obstruction modules are possible even for primitive LNDs
on affine three-space. For example,
\[
D_0=X\partial_Y+2Y\partial_Z,\qquad P=X
\]
has kernel \(\mathbb C[X,XZ-Y^2]\). On \(X=0\), the restricted
kernel is \(\mathbb C[Y]\), whereas the image of the ambient
kernel is \(\mathbb C[Y^2]\). The class of \(Y\) maps under (23)
to \([1]\), since \(D_0Y=X\). This class is nonzero: \(D_0\)
vanishes on \(X=Y=0\), so it cannot send a polynomial to one.
This countercontrol prevents treating (24) alone as an impossibility.
The prescribed nonfree nodal module remains an additional requirement.

## 6. The fixed divisor and primitivity of a possible extension

The fixed locus of (4) on the surface is the affine line
\(F_0=\{u=0\}\), which lies outside the conductor.
It is an effective Cartier divisor. Its divisor class has exact
order four:
\[
4F_0=\operatorname{div}_R(d+1).
\tag{25}
\]
For exactness of the order, a function whose divisor is supported
only on \(F_0\) pulls back on the smooth normalization to
\(c u^k\). Here one uses \(B^*=\mathbb C^*\), already computed
in the [global embedding note](nodal-embedding-pass21.md).
Its membership in \(R\) forces its values at \(1,-1,i,-i\)
to agree, so \(4\mid k\). This also rules out smaller principal
positive multiples of the Cartier divisor.

Despite its fixed curve, the descended \(\partial\) has no
nonunit common coefficient in \(R\). Indeed any such coefficient
could vanish only on \(F_0\), because the derivation is nonzero
elsewhere. It would therefore be \(cu^{4k}\), with \(k\ge1\).
But the pass-23 label
\[
g=a(u)+b(u)y,\qquad
b(u)=\frac{1-i}{4}(u+1)(u+i)
\]
satisfies
\[
\partial g=uA(u)b(u),
\tag{26}
\]
which has order exactly one at \(u=0\). It cannot be divisible
by \(u^{4k}\).

Accordingly, if an ambient extension factors as \(D=G D_{\rm prim}\),
its restriction has \(\bar G\in R^*=\mathbb C^*\).
The primitive part is again an LND and fixes \(P\); after constant
rescaling it still induces the given \(\partial\).[^lnd]
Thus an ambient realization, if it exists, can and must be studied
through a primitive extension, with its fixed curve not removed
by a global nonunit coefficient on the surface.

## 7. Free degree modules do not force a free obstruction module

There is a concrete limit to using freeness of degree modules and
principality of their higher images. Those module-theoretic properties
alone do not imply local freeness of the torsion module in (23).
The following countercontrol is deliberately a module with a locally
nilpotent operator, not an asserted polynomial algebra with a derivation.

Let \(C_*=\mathbb C[d,v]\), \(P_*=v^2-d^2(d+1)\), and take the
free module \(F=\bigoplus_{j\ge0}C_*E_j\). Define the \(C_*\)-linear
operator
\[
\begin{split}
N E_0&=0,\quad N E_1=P_*E_0,\\
N E_2&=dE_0+P_*E_1,\quad
N E_3=vE_0+P_*E_2,\\
N E_j&=P_*E_{j-1}\quad(j\ge4).
\end{split}
\tag{27}
\]
It is locally nilpotent. Its actual degree modules and higher images
are, for every \(j\ge0\),
\[
\ker N^{j+1}=\bigoplus_{k=0}^{j}C_*E_k,\qquad
N^j(\ker N^{j+1})=P_*^jC_*E_0.
\tag{28}
\]
The first assertion follows from the nonzero leading coefficient
\(P_*^{j+1}\) on any basis vector of higher degree. Thus the degree
modules have exactly the free ranks \(j+1\), and the higher-image
ideals are all principal.

Put \(M_0=\operatorname{coker}_{C_*}
\begin{pmatrix}P_*&d&v\\0&P_*&0\\0&0&P_*\end{pmatrix}\),
with generators \(E_0,E_1,E_2\). Then
\[
F/NF=M_0\oplus\bigoplus_{j\ge3}A_0E_j.
\]
The \(P_*\)-torsion \(H_0=M_0[P_*]\) fits into
\[
0\longrightarrow A_0E_0\longrightarrow H_0
\longrightarrow\operatorname{Syz}_{A_0}(d,v)\longrightarrow0.
\tag{29}
\]
To verify this, a vector \((b_0,b_1,b_2)\) represents a torsion
class precisely when \(db_1+vb_2\) vanishes modulo \(P_*\).
Project to \((\bar b_1,\bar b_2)\). Its kernel reduces to
\(A_0E_0\) using \(P_*E_1=-dE_0\) and
\(P_*E_2=-vE_0\). The latter copy of \(A_0\) is injective,
as is immediate from the triangular presentation.

The syzygy module in (29) is isomorphic to \(\mathbb C[s]\):
its vectors are \(F(s)(-v,d)\), and \(F=1,s\) give two
generators over \(A_0\). For example, in
\(\alpha+s\beta=0\), the conditions
\(\beta,s\beta\in A_0=\mathbb C+d\mathbb C[s]\)
force \(\beta\in d\mathbb C[s]\).
Accordingly \(H_0\) is generated by
\[
E_0,\quad k_1=vE_1-dE_2,\quad
k_2=d(d+1)E_1-vE_2.
\tag{30}
\]
It has generic rank two over \(A_0\), but needs exactly three
generators at the node. The quotient in (29) needs two there.
Also \(E_0\) remains nonzero in \(M_0/(d,v)M_0\), since every
entry of its presentation matrix lies in \((d,v)\).
Thus \(E_0\notin(d,v)H_0\), giving a third independent class.
This proves nonfreeness and hence nonflatness at the node.
The entire \((F/NF)[P_*]\) is likewise nonflat, since it contains
\(H_0\) as a direct summand.

The missing algebra hypothesis is visible rather than concealed.
The first four basis elements can be realized in \(C_*[\sigma]\) as
\[
E_0=1,\quad E_1=P_*\sigma,\quad
E_2=P_*^2\sigma^2/2+d\sigma,\quad
E_3=P_*^3\sigma^3/6+P_*d\sigma^2/2+v\sigma,
\]
with \(N=\partial_\sigma\). Continuing by integration realizes all
the module formulas. But their \(C_*\)-span is not a subalgebra:
\[
E_1^2=2E_2-(2d/P_*)E_1
\]
does not belong to that span, because \(P_*\nmid d\).
Consequently (27)–(30) refute only an inference from degree-module
freeness and principal higher-image ideals by themselves. Whether
the additional multiplication constraints of an actual polynomial
three-ring exclude the required module (24) is a precise remaining
question. No claim that this operator realizes an ambient derivation
is made.

## 8. Outcome and exact verification boundary

The three singular lines on the surface and the single four-branch
point on its invariant curve are different objects. Their quotient
maps have different scheme fibers, and the intermediate quotient
is genuinely nonflat. The needed ambient invariant restriction
must have the exact defect (24) for the specified nodal map.
These calculations close the shortcut that would identify
\(T\) with the plane curve ring \(C/(P)\); they do not establish
an \(\mathbb A^3\) embedding obstruction.

A standalone exact checker reconstructs the kernel-curve presentation,
both Artinian fibers, the normalization module and its relations,
the squared-parameter conductor interpolation, the descended action
and fixed-divisor controls, the actual ambient countercontrol, and
the filtered-module nonfreeness control:

~~~sh
/opt/anaconda3/bin/python research/nodal_hypersurface_checks_pass24.py
~~~

All eight unittest methods passed in 0.115 seconds.

The quotient, ideal-contraction, Cartier-divisor, and general exact
sequence proofs above are the written arguments. The finite checks
do not claim to formalize every possible ambient extension.
No old proof, registry, public claim, or external contact is changed.

## Primary sources actually used

[^lnd]: N. Dasgupta and S. A. Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/html/2306.00510v2), Section 2 immediately before Definition 2.3 (the LND degree and factorial closure), Theorem 2.8 (the Miyanishi kernel theorem), Theorem 2.10(i) (faithful flatness over the ambient kernel), and the Introduction's paragraph on primitive replicas. These statements were read in the primary author text. They apply to the hypothetical polynomial three-ring, not directly to the nonnormal surface.

[^flatfinite]: Stacks Project, [Lemma 10.78.2, finite presented flat modules](https://stacks.math.columbia.edu/tag/00NX), including its proof of local freeness. The finite module here is over the Noetherian nodal curve ring.

[^flat]: Stacks Project, [Lemma 10.39.17, flat local maps are faithfully flat](https://stacks.math.columbia.edu/tag/00HR), with Lemma 10.39.16 read as well; and [Lemma 10.82.15, universal injectivity and ideal contraction](https://stacks.math.columbia.edu/tag/05CK), including its full proof.
