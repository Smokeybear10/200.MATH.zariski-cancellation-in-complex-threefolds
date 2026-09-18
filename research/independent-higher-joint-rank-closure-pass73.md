# Original recognition for the higher moving joint-rank-three sectors

The remaining independent moving quartic and quintic sectors are
recognized. When the original action and its two defect fields have
joint rank three, division by the actual common factor preserves
defect rank two. The full six-dimensional companion then makes both
successive residual pairs complex constants. Its resulting rational
symmetry satisfies the original-ring quartic or quintic endpoint,
without asserting that the localized ring is a polynomial four-ring.

This is a supplied-frame theorem. It does not supply a frame for
an arbitrary sliced action. In particular, its conclusion is not
unrestricted cancellation.

## 1. Actual hypotheses and the inherited common-power normalization

Let
\[
B=k[Q_1,Q_2,X,Y],\quad k=\mathbb C,\quad K=\operatorname{Frac}B,
\quad E\in\operatorname{LND}_k(B),\quad E(s_*)=1.
\]
The displayed generators are actual polynomial coordinates, and their
genuine partials satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Write \(V_i=\operatorname{ad}_E^2T_i\) for \(i=X,Y\).
Assume
\[
\operatorname{rank}_K(V_X,V_Y)=2,\qquad
\operatorname{rank}_K(E,V_X,V_Y)=3,
\]
\[
m\in\{4,5\},\qquad E^{m+1}x=0,\qquad E^mx
\text{ is nonconstant},\quad x=(Q_1,Q_2,X,Y)^t.
\tag{2}
\]

**Theorem.** Under (1)--(2), \(E\) fixes an actual ambient
coordinate and
\[
\ker E\simeq\mathbb C^{[3]}.
\tag{3}
\]

The complete [highest-vector and rescaling proof](two-quadratic-top-line-pass42.md),
Sections 1--5, first separates a zero bad preceding top. That branch
already has a commuting actual good constant direction and is
recognized by the one-good-output theorem. In the other branch,
constant changes within the good pair and within the bad pair give
\[
0\ne g\in\ker E\setminus k,\qquad
E^mx=cg^m,\qquad E^{m-1}(X,Y)=(g^{m-1},0),\qquad c=e_1.
\tag{4}
\]
These are genuine constant polynomial coordinate changes. They preserve
the supplied bounds and both ranks in (2). The nonzero constant
directions in the two separate output planes can be normalized
independently.

Put \(\delta=E/g\) on \(B_g\), \(h_j=\delta^jx\), \(P=h_1\),
and \(J=\operatorname{Jac}P\), using the actual coordinate partials.
The same source gives the normalized adjoint bounds in (1), with
\(E\) replaced by \(\delta\), and
\[
h_m=c,\qquad Lh_{m-1}=\ell=(1,0)^t,\qquad
\mathcal D=[\,\widetilde V_X(x)\mid\widetilde V_Y(x)\,],
\quad \operatorname{rank}_K\mathcal D=2,
\tag{5}
\]
where \(\widetilde V_i=\operatorname{ad}_\delta^2T_i\) and
\(L\) is the constant selector of the two bad coordinates.
Indeed,
\[
\widetilde V_i=g^{-2}V_i+2g^{-3}([E,T_i]g)E.
\]
Any relation between the two normalized columns would contradict
the joint rank three in (2). No normalized defect is asserted to
be a primitive polynomial derivation of the original ring.

## 2. Why the full companion calculation remains valid

The actual \(\delta\) is an LND of \(B_g\). Each original partial
preserves \(B_g\), but need not be an LND there. The normalized
adjoint bounds give the polynomial coefficient matrix
\[
C(t)=I-tJ+\frac{t^2}{2}\mathcal D L.
\]
Conjugating those derivations by the actual divided flow and applying
them to \(\exp(t\delta)x\) gives both inverse Jacobian identities.
This uses the chain rule on \(K=k(Q_1,Q_2,X,Y)\), not exponentials
of the localized partials. Both matrices belong to
\(\operatorname{Mat}_4(B_g[t])\), so their determinants are units
of \(B_g[t]\). Evaluation at \(t=0\) gives \(\det C(t)=1\).

Consequently the six-dimensional matrix
\[
M=\begin{pmatrix}J&-\mathcal D/2\\ L&0\end{pmatrix}
\]
satisfies the exact identities
\[
M^6=0,\qquad (M^j)_{\rm UL}=\frac{\operatorname{Jac}h_j}{j!},
\]
\[
j!M^j\binom P0=\binom{h_{j+1}}{jLh_j},\qquad
j!M^j\big|_{\text{base columns}}
=\binom{\operatorname{Jac}h_j}{j\operatorname{Jac}(Lh_{j-1})}.
\tag{6}
\]
These follow by the same Schur elimination and coefficient comparison
as [the complete companion proof](two-quadratic-defects-pass39.md),
Sections 2--3. The bottom-left block of \(M^j\) is
\(L(M^{j-1})_{\rm UL}\), which proves the full lower rows.

The rank-preserving block lemma also applies over \(K\): the injective
\(\mathcal D\) and surjective \(L\) exclude a nonzero right or left
kernel vector supported only in the auxiliary plane. Thus, when
\(MN=NM=0\), the upper-left block and \(N\) have the same rank.
Starting from \(M^6=0\), the zero Jacobians at and above the
constant \(h_m\) therefore give
\[
M^m=0,\qquad M^{m-1}\ne0,\qquad
\operatorname{rank}M^{m-1}=1,\qquad
\operatorname{rank}M^{m-2}=2.
\tag{7}
\]
Nonvanishing follows from (6), whose velocity column at power
\(m-1\) has upper component \(c/(m-1)!\).
There is one block of size \(m\); the remaining blocks have total
size \(6-m\). This gives both ranks in (7). For \(m=5\), it
also gives Jordan type \((5,1)\) and \(\operatorname{rank}M^2=3\).

No polynomial presentation of \(B_g\) has been inferred. The common
constants of its four ordinary partials are still \(k\), since
their common constants on the original rational field \(K\) are \(k\).
This exact constant-field fact replaces any polynomial-ring
assumption in the integrations below.

## 3. The first full image forces a constant residual pair

The vector
\[
v=\binom{c}{(m-1)\ell}
=(m-1)!M^{m-1}\binom P0
\]
spans the rank-one image in (7). Comparing all four base columns
of that same power in (6), and choosing a nonzero component of
\(c\), yields an actual element \(\sigma\in B_g\) and constants
\(e\in k^4,\ \mu\in k^2\) with
\[
h_{m-1}=c\sigma+e,\qquad
Lh_{m-2}=\ell\sigma+\mu,\qquad
\delta\sigma=1,\qquad Le=\ell.
\tag{8}
\]
For example, choose \(\sigma=(h_{m-1})_1\), since \(c=e_1\).
The upper rows show that all other components of
\(h_{m-1}-c\sigma\) have zero ordinary differential. The lower
rows then show the same for \(Lh_{m-2}-\ell\sigma\).
Thus both integration constants are genuinely complex constants,
not arbitrary \(\delta\)-invariants.

The full velocity identities also give
\[
Jc=\frac{m-1}{2}\mathcal D\ell,\qquad
Je=\frac{c}{m-1}-\frac{\sigma}{2}\mathcal D\ell
                         +\frac{m-2}{2}\mathcal D\mu.
\tag{9}
\]
For the second identity apply \(M\) to the velocity column at
power \(m-2\) in (6), then substitute (8). The first identity
is the normalized highest velocity identity.

If \(\mu=t_0\ell\), \(t_0\in k\), put
\[
S_0=T_e+\frac{\sigma-(m-2)t_0}{m-1}T_c.
\tag{10}
\]
Here \(T_v\) denotes differentiation in the genuine constant
direction \(v\). Since \([\delta,T_v](x)=-Jv\), (9) proves
\([\delta,S_0]=0\). Its coordinate coefficients have
\(\delta\)-degree at most one. Applying this commutation to
\(h_{m-1}=c\sigma+e\) gives \(S_0\sigma=0\), hence
\(S_0^2x=0\).

The independent constant directions \(c,e\) can be completed
to an actual constant coordinate frame. In that frame \(S_0\)
has two output directions, translation coefficient one, and
coefficient \((\sigma-(m-2)t_0)/(m-1)\) with constant
\(\delta\)-derivative \(1/(m-1)\). Its varying output partial
is exactly \(T_c\), which remains good for the original \(E\).
The [rational two-direction theorem](rational-two-direction-recognition-pass69.md)
therefore applies with the original \(g\) and slice \(s_*\).
It proves (3) and an actual invariant coordinate. In particular
there is no attempt to use a localized coordinate-section theorem.

It remains to assume that \(\ell,\mu\) are independent, equivalently
\(\mu=(\mu_1,\mu_2)^t\) with \(\mu_2\ne0\).

## 4. The second full image forces the next pair to be constant

Both
\[
v=\binom{c}{(m-1)\ell},\qquad
w_1=\binom{e}{(m-2)\mu-\sigma\ell}
\]
belong to \(\operatorname{im}M^{m-2}\); obtain \(w_1\) by
subtracting \(\sigma v\) from \((m-2)!M^{m-2}(P,0)^t\).
Their upper bad projections \(0,\ell\) make them independent.
They span that full image by (7).

The upper bad rows of each base column in (6), at \(j=m-2\),
are \(\ell\,d\sigma\). Thus its coefficient on \(w_1\)
is the corresponding derivative of \(\sigma\). Choosing the
nonzero first component of \(c\) now defines \(\tau\in B_g\)
directly from \(h_{m-2}-e\sigma\). The remaining ordinary
derivatives vanish, and hence
\[
h_{m-2}=c\tau+e\sigma+v_0,\quad
v_0\in k^4,\quad Lv_0=\mu,\quad\delta\tau=\sigma.
\tag{11}
\]
The lower rows of the same columns give the entire vector equality
\[
(m-2)d(Lh_{m-3})
=(m-1)\ell\,d\tau+
             ((m-2)\mu-\sigma\ell)\,d\sigma.
\]
Integration with respect to all four actual partials gives
\[
Lh_{m-3}
=\ell\left(\frac{m-1}{m-2}\tau-\frac{\sigma^2}{2(m-2)}\right)
       +\mu\sigma+\nu,\qquad \nu\in k^2.
\tag{12}
\]
There is no variable auxiliary coefficient being differentiated
as if it were constant: \(L\) is the original constant selector,
and the variable \(-\sigma\ell\) is retained in the displayed
full-image vector and in this integration.

Write
\[
u_0=\tau-\sigma^2/2,\qquad \delta u_0=0,\qquad
\nu=\nu_1\ell+\nu_2\mu,\quad \nu_1,\nu_2\in k.
\tag{13}
\]
The two consecutive residual pairs are therefore both complex
constant pairs. This is the step that differs from the
one-dimensional normalized-defect reduction.

## 5. The rational correction and the original-slice unit gate

Apply \(M\) to the velocity column at power \(m-3\) in (6).
Its upper part, together with (8)--(13), gives
\[
Jv_0=
\frac{c\sigma}{(m-1)(m-2)}+\frac e{m-2}
-\frac{(m-1)u_0}{2(m-2)}\mathcal D\ell
-\frac{\sigma}{2}\mathcal D\mu+\frac{m-3}{2}\mathcal D\nu.
\tag{14}
\]
This is the full two-defect identity, not a replacement of the
two columns by one line. It is the algebraic identity proved
in [the higher constant-top proof](independent-higher-constant-closure-pass68.md),
equations (15)--(16), with the actual normalized derivation.

Set
\[
\beta=\frac{\sigma-(m-3)\nu_2}{m-2},\qquad
\gamma=\frac{\sigma^2-(m-3)\nu_2\sigma}{(m-1)(m-2)}
                  +\frac{u_0}{m-2}-\frac{m-3}{m-1}\nu_1,
\]
\[
S=T_{v_0}+\beta T_e+\gamma T_c.
\tag{15}
\]
Substituting (9),(14) and \(\mathcal D\nu=
\nu_1\mathcal D\ell+\nu_2\mathcal D\mu\) proves
\([\delta,S]=0\). The \(T_e,T_c\) coefficients cancel by
\(\delta\beta=1/(m-2)\) and
\(\delta\gamma=(2\sigma-(m-3)\nu_2)/((m-1)(m-2))\);
the two separate defect coefficients cancel as in (14).

All coordinate coefficients of \(S\) have \(\delta\)-degree at
most two. Commutation with \(\delta\), first applied to (8)
and then to (11), gives
\[
S\sigma=0,\qquad
Su_0=\begin{cases}1/3,&m=4,\\0,&m=5,\end{cases}
\qquad
\begin{cases}S^2x=c/6,\ S^3x=0,&m=4,\\
S^2x=0,&m=5.\end{cases}
\tag{16}
\]
For the second equality,
\(S(h_{m-2})=\delta^{m-2}(Sx)=c\,\delta^{m-2}\gamma\).
It does not set the quartic value equal to the quintic value.

These finite iterates do not by themselves make \(S\) an LND
on an arbitrary localization. Here the original slice provides
the missing unit gate. All polynomial functions of the original
coordinates have finite \(S\)-iterates by the Leibniz rule.
Thus \(\exp(tS)g\) and \(\exp(tS)s_*\) are polynomials over \(K\).
Commutation and \(\delta s_*=1/g\) give
\[
\exp(tS)(1/g)=\delta(\exp(tS)s_*)\in K[t].
\]
The formal exponential preserves products, so this polynomial
and \(\exp(tS)g\) multiply to one. Units of \(K[t]\) are
constant, yielding
\[
Sg=0,\qquad [E,S]=0,\qquad S\in\operatorname{LND}(B_g).
\tag{17}
\]
For the last assertion, \(S\) preserves \(B_g\), fixes \(g^{-1}\),
and has finite iterates on its actual coordinate generators.
No global polynomiality, global slice, or polynomial presentation
of \(\ker S\) is inferred from (17).

## 6. Actual coordinates and the quartic original-ring endpoint

The constant directions \(c,e,v_0\) are independent because their
bad projections are \(0,\ell,\mu\). Choose a second original
constant good direction \(c_2\) independent of \(c\). Coordinates
dual to \((c,e,v_0,c_2)\) are denoted \((a_0,b,z,w)\). In particular
\[
z=Y/\mu_2,\qquad b=X-(\mu_1/\mu_2)Y,\qquad
T_c=\partial_{a_0},\quad T_e=\partial_b,\quad
T_{v_0}=\partial_z,\quad T_{c_2}=\partial_w.
\tag{18}
\]
The two indicated good partials are genuine original good ones.
The original highest identity, before division, is
\[
g[E,T_c]=-\frac{m-1}{2}V_X.
\tag{19}
\]
Indeed, writing \(J_E=\operatorname{Jac}(Ex)\) and
\(\mathcal V=[V_X(x)\mid V_Y(x)]\), the original identity
\(J_E(E^mx)=(m-1)\mathcal V L(E^{m-1}x)/2\),
with (4), gives \(gJ_Ec=(m-1)V_X(x)/2\).
The original second adjoint of \(T_e\) is \(V_X\), since
its bad components are precisely \((1,0)\).

For \(m=4\), (11) gives \(\delta^2w=0\) directly.
Equations (11)--(12) and (15) are exactly the terminal identities
of the [parabolic-form proof](terminal-quartic-parabolic-form-pass71.md).
For clarity the original-ring gates can be reconstructed explicitly.
Make the actual polynomial shear
\[
a=a_0-z^2/12+(\nu_2/3)b,\qquad
\widehat\beta=(\sigma-\nu_2)/2,\qquad
\kappa=\frac{\sigma^2}{6}+\frac{u_0}{2}
                  -\frac{\nu_1}{3}-\frac z6-\frac{\nu_2^2}{6}.
\]
It fixes \(b,z,w\), with polynomial inverse reversing the
correction. Equations (15)--(17) yield
\[
S=\partial_z+\widehat\beta\partial_b+\kappa\partial_a,\quad
S\widehat\beta=S\kappa=0,\quad
\delta\widehat\beta=1/2,\quad\delta\kappa=\widehat\beta/3.
\tag{20}
\]
Let \(h=3\kappa-\widehat\beta^2\) and
\(c_0=2\nu_1+\nu_2^2/2\). The actual velocities from (12) are
\(\delta z=2\widehat\beta+2\nu_2\) and
\(\delta b=\widehat\beta^2+h+z/2+c_0\).
Consequently the two cleared coefficients are actual polynomials:
\[
N=g\widehat\beta=(Ez-2\nu_2g)/2\in B,\qquad
U=3g\kappa=Eb-g(z/2+c_0)\in B.
\tag{21}
\]
The new partials satisfy
\(\partial_a=T_c\) and
\(\partial_b=T_e-(\nu_2/3)T_c\).
Thus \(\operatorname{ad}_E^2\partial_b=V_X\), while
\(\partial_a\) is original-good and (19) has coefficient
\(-3/2\). Also \(E^2w=g^2\delta^2w=0\).
Equations (17),(20)--(21) therefore verify every hypothesis
of the **abstract original-ring theorem**, Section 1 of
[terminal quartic recognition](terminal-quartic-recognition-pass71.md).
That theorem does not assume dependent defects. It proves (3)
and an actual invariant coordinate in this quartic branch.

## 7. The quintic third image and its original-ring endpoint

For \(m=5\), the companion has Jordan type \((5,1)\).
Its entire square image has dimension three. By (6),(8),(11),
the following full vectors belong to it:
\[
\begin{aligned}
v&=24M^4\binom P0=\binom c{4\ell},\\
w_1&=6M^3\binom P0-\sigma v=\binom e{3\mu-\sigma\ell},\\
w_2&=2M^2\binom P0-\tau v-\sigma w_1\\
&=\binom{v_0}{2Lh_2-4\tau\ell-\sigma(3\mu-\sigma\ell)}.
\end{aligned}
\tag{22}
\]
Their upper vectors \(c,e,v_0\) are independent. They therefore
span the full square image, and its upper projection is
\(Kc+Ke+Kv_0\). The differential row of the actual \(w\)
in (18) kills that plane. The upper-left block in (6) now gives
\[
d(\delta^2w)=0,\qquad
\delta^2w=\lambda\in k,\qquad E^2w=\lambda g^2.
\tag{23}
\]
All four ordinary partials are used. The two auxiliary entries
of each vector in (22) have been retained. No rank equality
between \(M^2\) and its upper-left block alone is assumed.

Make the actual constant shear \(a=a_0-(\nu_2/2)b\), fixing
\(b,z,w\). The coefficients in (15) become
\[
S=\partial_z+\beta\partial_b+\kappa\partial_a,\qquad
\beta=(\sigma-2\nu_2)/3,\qquad \kappa=\gamma-(\nu_2/2)\beta,
\]
\[
S\beta=S\kappa=0,\qquad \delta\beta=1/3,\qquad
\delta\kappa=\beta/2.
\tag{24}
\]
Here \(Sw=0\) and \(Sg=0\) remain valid. The actual second
bad iterates, from (12), are
\(\delta^2z=\sigma+\nu_2\) and
\(\delta^2b=\sigma^2/2+4u_0/3+\nu_1\).
They give the explicit polynomial clearing
\[
n=g^2\beta=(E^2z-3\nu_2g^2)/3\in B,
\]
\[
Q=g^4\kappa=
\frac{g^2}{4}E^2b-\frac{3n^2}{8}
-\frac{3\nu_2}{2}g^2n
-\left(\frac{\nu_2^2}{2}+\frac{3\nu_1}{4}\right)g^4\in B.
\tag{25}
\]
Thus \(g^4S=g^4\partial_z+g^2n\partial_b+Q\partial_a\)
is polynomial, with all coefficients fixed by it.
This is the same direct algebra as the
[polynomial-clearing proof](quintic-rank-drop-polynomial-symmetry-pass72.md);
no primitive original defect decomposition is used.

The new \(\partial_a=T_c\) remains original-good and
normalized-good. The new \(\partial_b=T_e+(\nu_2/2)T_c\)
has normalized second adjoint
\[
D=\widetilde V_X\ne0,\qquad
[\delta,\partial_a]=-2D,\qquad
\operatorname{ad}_\delta^2\partial_a=0,\qquad
\operatorname{ad}_E^2\partial_a=0.
\tag{26}
\]
Nonvanishing follows from the normalized rank two in (5).
The scalar follows directly from the first identity of (9),
not from incorrectly dropping the correction term in the
original-to-normalized defect formula.

Equations (17),(23)--(26) verify every hypothesis of the
**abstract original-ring theorem**, Section 1 of
[terminal quintic recognition](terminal-quintic-recognition-pass72.md).
Its proof uses these exact scalar and actual good-partial gates,
not a rank-one normalized defect assumption. It recognizes the
original \(E\) with its original slice, proving (3).

## 8. Scope, dependencies, and verification boundary

The zero bad preceding top was already recognized in pass42.
For a nonzero preceding top, (8) leaves exactly a collinear
or a transverse constant pair \((\ell,\mu)\). The collinear
case uses rational69. The transverse case has a constant
second pair by the full two-row image calculation, and goes
to the original-ring quartic71 or quintic72 endpoint.
These alternatives exhaust (1)--(2).

The transfer reuses the algebraic full-image and correction
identities of the higher constant-top proof68. It does **not**
reuse that proof's global coordinate-section recognition step:
the normalized symmetry initially lives only on \(B_g\).
Polynomial coefficient clearing, genuine coordinate changes,
and the original slice are checked separately here before either
terminal endpoint is invoked.

This note proves the higher moving independent joint-rank-three
supplied-frame theorem stated above. Combining it with other
saved results to claim exhaustion of all supplied frames requires
a separate scope audit. Universal existence of such a frame is
not proved. No historical novelty, human referee approval,
proof-assistant verification, external contact, or submission
is asserted.

The author reread the complete companion39, highest-vector42,
higher constant-top68, rational69, both terminal recognition
proofs71/72, and their stated actual polynomial-clearing inputs
while deriving this transfer. The current proof itself adds no
external classification theorem: it inherits the precisely
scoped nice-derivation, plane-LND, and regular-kernel source
gates of those recognition proofs. No fresh full reconstruction
of all historical source proofs is claimed.
Independent full-file audits and any bounded numerical controls
must be recorded only after they occur. This note adds no test
suite, regression count, checkpoint, or frozen-file change.
