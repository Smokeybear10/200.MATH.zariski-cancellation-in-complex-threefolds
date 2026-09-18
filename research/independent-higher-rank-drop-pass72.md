# Original-ring recognition for a rank-drop moving quartic

The independent moving quartic with joint action-and-defect rank two
supplies the same rational companion identities as the dependent
common-power quartic. Its original highest-column identity also supplies
the exact good-partial cancellation required by the terminal pass71
endpoint. Thus this rank-drop quartic is recognized without applying
a polynomial-four-ring theorem to an invariant localization.

The analogous quintic calculation recognizes its nonterminal residual
pairs, but does not satisfy two essential hypotheses of that terminal
endpoint. Both failures are recorded explicitly below.

Subsequent pass72 results complete that remaining quintic terminal
case by a different argument. The [third-image lemma](quintic-rank-drop-third-image-pass72.md)
refines the acceleration bound, and the
[terminal quintic theorem](terminal-quintic-recognition-pass72.md)
uses the good fixed-base partial instead of trying to make the bad
output good. The two failures in Section 4 remain valid failures
of the unchanged quartic step; they are not a claim that the
terminal case remains unrecognized after those later results.

## 1. Actual original frame and normalization

Let
\[
B=k[Q_1,Q_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}(B),\quad Es_*=1,
\]
with actual coordinate partials satisfying
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,
\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Write \(V_i=\operatorname{ad}_E^2T_i\) for the bad indices.
Assume the independent moving-top rank-drop sector:
\[
\operatorname{rank}_K(V_X,V_Y)=2,
\qquad\operatorname{rank}_K(E,V_X,V_Y)=2,
\qquad K=\operatorname{Frac}B,
\]
\[
E^mx=cg^m,\quad E^{m+1}x=0,\quad
E^{m-1}(X,Y)=(g^{m-1},0),\quad c=e_1,
\quad g\in\ker E\setminus k,
\quad m\in\{4,5\}.
\tag{2}
\]
The [original full-image theorem](two-quadratic-top-line-pass42.md),
Sections 1--3, supplies these common powers after actual constant
changes within the good and bad pairs. Its zero preceding-bad-vector
alternative is already recognized and is not part of (2).

On \(B_g\) put \(\delta=E/g\). The exact rescaling formula is
\[
\widetilde V_i=g^{-2}V_i+2g^{-3}([E,T_i]g)E,
\qquad
\operatorname{rank}_K(\widetilde V_X,\widetilde V_Y)=1.
\tag{3}
\]
Their line is independent of \(\delta\), and all four normalized
adjoint bounds in (1) remain valid with \(E\) replaced by \(\delta\).
Also \(\delta^mx=c\) and
\(\delta^{m-1}(X,Y)=(1,0)\). These are exactly the rescaling
and rank assertions of pass42, Section 5.

No coordinate partial is presumed locally nilpotent on \(B_g\).
Nor is the normalized defect pair given a global primitive polynomial
factorization. Choose a nonzero normalized defect as \(D\), and write
\(\widetilde V_X=aD,\widetilde V_Y=bD\), with rational coefficients.
One coefficient is one. The adjoint bounds imply
\([\delta,D]=0\) and \(\delta a=\delta b=0\).

## 2. The rational companion and its first image

Put
\[
h_j=\delta^jx,\quad P=h_1,\quad J=\operatorname{Jac}P,
\quad d=D(x),\quad \ell=(0,0,a,b),\qquad
M=\begin{pmatrix}J&-d/2\\\ell&0\end{pmatrix}.
\]
The actual divided flow on \(B_g\), its inverse, and its conjugated
original partials give inverse polynomial matrices over \(K[t]\).
The Schur determinant and full block coefficients therefore give
\[
M^5=0,\quad (M^j)_{\mathrm{UL}}=\operatorname{Jac}h_j/j!,
\]
\[
j!M^j\big|_{\mathrm{base}}
=\binom{\operatorname{Jac}h_j}{j\ell\operatorname{Jac}h_{j-1}},
\qquad
j!M^j\binom P0=\binom{h_{j+1}}{j\ell h_j}.
\tag{4}
\]
In particular the lower row in this identity is not
\(d(\ell h_{j-1})\). The variable row is not differentiated.
This is the rational companion construction already written in
[the cubic rank-drop proof](cubic-rank-drop-nonconstant-speed-pass69.md),
Section 2; it requires neither a primitive normalized LND nor a
polynomial presentation of \(B_g\).

The two-sided block lemma applies because \(d,\ell\ne0\).
For \(m=4\), the zero upper block of \(M^4\) implies \(M^4=0\),
and the nonzero upper component of \(M^3(P,0)^t\) forces Jordan
type \((4,1)\). For \(m=5\), \(M^4(P,0)^t\ne0\) forces type
\((5)\). In both cases the highest nonzero full image is a line,
its upper block has rank one, and it contains the direction \(c\).
Thus
\[
h_{m-1}=c\sigma+e,\quad
\sigma\in B_g,\quad e\in k^4,\quad e_B=(1,0),
\quad\delta\sigma=1.
\tag{5}
\]
For example take \(\sigma=(h_{m-1})_1\). The other components
have zero derivatives under all four actual rational coordinate
partials, whose common constant field on \(K\) is \(k\).

The highest velocity coefficient gives
\[
Jc=\frac{m-1}{2}(\ell e)d=\frac{m-1}{2}ad.
\tag{6}
\]
If \(\widetilde V_X=0\), choose \(a=0,b=1\). Then
\([\delta,T_c]=0\). The actual constant partial \(T_c\) has
finite iterates on \(g,s_*\). Commutation and
\(\delta s_*=1/g\) make both \(\exp(tT_c)g\) and its inverse
polynomial in \(t\). Hence \(T_cg=0\) and \([E,T_c]=0\).
The original one-good-output recognition lemma, using the other
original good direction, recognizes \(\ker E\).
This argument is valid for both values of \(m\).

Henceforth \(\widetilde V_X\ne0\); choose
\(D=\widetilde V_X\), \(a=1,b=\eta\), so \(\ell e=1\).

## 3. Complete original-ring bridge in degree four

Assume \(m=4\). All inputs to Sections 2--6 of the
[common-power quartic calculation](common-power-moving-quartic-reduction-pass70.md)
have now been established: the actual original frame and slice,
the actual invariant polynomial \(g\), the normalized rank-one
line with row \((1,\eta)\), its commutation with \(\delta\),
the constant normalized fourth top, and the companion identities
(4)--(6). The primitive original dependent decomposition in that
note's Section 1 is not used after supplying these inputs.

For clarity the successive original-ring recognition gates are:
\[
(h_2)_B=e_B\sigma+(F,G),\quad
dF+\eta\,dG=0,\quad \delta F=\delta G=0,
\]
\[
S=T_e+\frac{\sigma-2(F+\eta G)}{3}T_c,
\quad [\delta,S]=0,\quad S\sigma=SF=SG=0.
\tag{7}
\]
Here and below \(dF\) is ordinary differentiation, not the
defect column. If \(G\notin k\), Lie differentiation of (7)
gives \(S\eta=0\); if \(G=0\), (7) gives \(F\in k\).
Both cases give \(S^2x=0\), and the
[rational two-direction theorem](rational-two-direction-recognition-pass69.md)
applies to the original \(E,s_*,g\), with good partial \(T_c\).

Otherwise \((F,G)=\mu\in k^2\), \(\mu_2\ne0\). The second
full image gives
\[
h_2=c\tau+e\sigma+v_0,\quad \delta\tau=\sigma,
\quad (v_0)_B=\mu,
\]
\[
Z_B=P_B-e_B\left(\frac{3\tau}{2}-\frac{\sigma^2}{4}\right)
                -\mu\sigma,\qquad dZ_1+\eta\,dZ_2=0.
\tag{8}
\]
The functions \(Z_B\) are killed by both \(\delta,S\).
A nonconstant pair therefore again forces \(S\eta=0\) and
gives original-ring rational recognition.

For a constant second pair, the exact three-direction construction
in pass70 gives the same rational \(S_3\), bounded coordinate
iterates, and original-slice unit argument. In particular
\(S_3g=0\), \([E,S_3]=0\), and \(S_3\) is an LND of \(B_g\).
These statements are not yet a global coordinate-section theorem.

Instead apply the actual constant coordinate changes and polynomial
shear of the [parabolic form](terminal-quartic-parabolic-form-pass71.md).
Its \(a\) and \(w\) partials remain original good directions,
and \(E^2w=0\) follows from (8), since the dual \(w\) kills
\(c,e,v_0\). The original velocities give
\[
N=g\beta=\frac{Ez-2\nu_2g}{2}\in B,\qquad
U=3g\kappa=Eb-g(z/2+c_0)\in B,
\]
\[
T=gS_3=(U/3)\partial_a+N\partial_b+g\partial_z,
\quad T^2(a,b,z,w)=0.
\tag{9}
\]
These polynomiality statements use only actual original velocities
and the normalized lower layers. They do not use dependence of the
original defects.

The additional original-partial identity must also be checked,
not inferred from the normalized companion. Original pass42,
equation (9), applied to (2) gives
\[
g[E,T_c]=-\frac32 V_X.
\tag{10}
\]
In the parabolic coordinates \(\partial_a=T_c\), while
\(\partial_b=T_e-(\nu_2/3)T_c\). Because \(e_B=(1,0)\),
its original second adjoint is exactly \(V_X\). Thus (10)
is precisely the missing actual good-partial hypothesis of the
[terminal recognition theorem](terminal-quartic-recognition-pass71.md).
All its other hypotheses are (7)--(9) and the supplied original
slice. That theorem applies to \(E\) on \(B\), not to \(\delta\)
on \(B_g\). Consequently
\[
\boxed{\text{Under (1)--(2) with }m=4,
\quad\ker E\simeq\mathbb C^{[3]}.}
\tag{11}
\]

## 4. The quintic transfer and its exact terminal boundary

For \(m=5\), equations (4)--(6) also transfer the algebraic
full-image calculations of the
[constant quintic proof](dependent-constant-quintic-closure-pass68.md),
with rational row \((1,\eta)\). The first residual pair is
\((h_3)_B=e_B\sigma+(F,G)\), with \(dF+\eta\,dG=0\).
The provisional rational symmetry is now
\[
S=T_e+\frac{\sigma-3(F+\eta G)}{4}T_c,
\quad[\delta,S]=0,\quad S\sigma=SF=SG=0.
\tag{12}
\]
If \(G\notin k\) or \(G=0\), the same Lie-derivative or
constant-pair argument makes this a nice rational two-direction
field. Rational69 applies with coefficient derivative \(1/4\)
and the actual original good partial \(T_c\).

For a constant transverse first pair \(\mu\), the second image
gives
\[
h_3=c\tau+e\sigma+v_0,\qquad\delta\tau=\sigma,
\]
\[
Z_B=(h_2)_B-e_B\left(\frac{4\tau}{3}-\frac{\sigma^2}{6}\right)
                    -\mu\sigma,
\quad dZ_1+\eta\,dZ_2=0.
\tag{13}
\]
Again \(\delta Z_B=SZ_B=0\). A nonconstant second pair gives
\(S\eta=0\) and original rational recognition. These cases use
full rational differentials, not a polynomial-curve theorem on \(B_g\).

Only a constant second pair remains in this calculation. Write
\(Z_B=\nu_1e_B+\nu_2\mu\) and \(u_0=\tau-\sigma^2/2\).
The exact nice three-direction field supplied by the full velocity is
\[
S_3=T_{v_0}+\beta_3T_e+\gamma_3T_c,
\quad \beta_3=\frac{\sigma-2\nu_2}{3},
\quad\gamma_3=\frac{\sigma^2}{12}-\frac{\nu_2\sigma}{6}
                         +\frac{u_0}{3}-\frac{\nu_1}{2},
\]
\[
[\delta,S_3]=0,\quad S_3\sigma=S_3u_0=0,
\quad S_3^2x=0,\quad S_3g=0,\quad [E,S_3]=0.
\tag{14}
\]
Here the original slice again proves \(S_3g=0\); a sufficiently
large invariant power clears its coefficients to a global nice LND.
It does not give a global slice to that replica.

There are two precise reasons that terminal71 does not apply unchanged.
First choose actual dual coordinates \((a,b,z,w)\) for
\((c,e,v_0,c_2)\), with \(c_2\) another good constant direction.
Equation (13) proves only
\[
\delta^3w=0\quad\text{and}\quad E^3w=0,
\tag{15}
\]
not the \(E^2w=0\) needed by the proportional-speed lemma.
No vanishing of the preceding component has been established.

Second the actual coefficient rates and top identity are
\[
\delta\beta_3=\frac13,\qquad
\delta\gamma_3=\frac{\beta_3}{2}+\frac{\nu_2}{6},
\qquad g[E,T_c]=-2V_X.
\tag{16}
\]
Even if proportional speed along \(w\) were obtained separately,
the analogous nonzero-quadratic-coefficient shear would have
\(\gamma_3=L(w)\beta_3+R(w)\), with \(\delta L=1/2\).
Its new partial \(\partial_{b'}=T_e+LT_c\) would therefore satisfy
\[
\operatorname{ad}_E^2\partial_{b'}
=V_X+2g(1/2)[E,T_c]=-V_X\ne0.
\tag{17}
\]
The vanished-coefficient branch would retain \(T_c\), but the
full endpoint requires both branches. Formula (17) is an exact
failure of this particular unchanged cancellation step, not a
counterexample to recognition or to some different coordinate choice.

## Scope and review boundary

The complete pass42 top/rank proof, rational69 rank-drop proof,
moving-quartic70 proof, constant-quintic68 proof, and all three
pass71 structural/recognition arguments were read through EOF
for this transfer. Their rational matrix identities are reused
only after checking their actual original-ring inputs.

This draft adds the rank-drop quartic bridge and the precise quintic
transfer boundary. It does not apply dependent-frame71 directly to
\(B_g\), recognize all independent moving tops, or establish a
universal supplied frame. No new numerical method, source-paper
proof read, full regression, metadata edit, or frozen-file change
is claimed. Independent reviews, if any, are separate evidence.
