# Nontransverse cubic excess with a noncomplex initial ratio

## 1. Statement and the actual hypotheses

This note excludes one branch of the supplied actual chart264. It does not
assert that an arbitrary sliced locally nilpotent derivation enters that chart.
The full hypotheses of264,296,535 and the necessary cubic-excess reduction554
are retained. In particular, the ambient ring and the original slice are
\[
 \mathcal B=\mathbf C[X,Y,Z,W]=\mathcal A[u],\qquad Eu=1,
 \qquad X=a_0u+x_0,\quad a_0\ne0.
\tag{1}
\]
The original degree profile is \((1,2,2,2)\), and its **entire** initial
kernel is \((\mathsf X^2\mathsf Z-\mathsf Y^2)\). The selected derivation is
the literal \(N=[u^4]\partial_Z|_{\mathcal A}\ne0\), with
\(Na_0=Nt=Ns=0\). Put \(L=\operatorname{Frac}\ker_{\mathcal A}N\).
The chart supplies an intrinsic parameter \(v_{\rm old}\), not an ambient
coordinate, and the exact returns
\[
 \begin{gathered}
 Nv_{\rm old}=1,\qquad L[\mathcal A]=L[v_{\rm old}]
       =L[y,\sigma,\theta],\qquad
 \operatorname{Frac}\mathcal A=L(v_{\rm old}),\\
 \mathbf C(y,z_{\rm int},w)=\operatorname{Frac}\mathcal A,
 \qquad L[y,z_{\rm int},w]=L[v_{\rm old}].
 \end{gathered}
\tag{2}
\]
Here \(z_{\rm int}\) is the literal original \(Z\)-intercept, not a later
subtracted intercept. The field \(L\) is finite over \(\mathbf C(t,s)\).
All original return, selected-partial, full-scalar and moving-level assumptions
remain in force.

The allowed finite coefficient extension and moving affine intrinsic change
give \(L'\supset L\), \(x=\rho v_{\rm old}+\zeta\), with
\(\rho\in L'^*\), and
\[
 \begin{split}
 \sigma&=x^2+c,\\
 \theta&=ax^3+bx^2+dx+e,\\
 y&=rx^4+qx^3+y_2x^2+y_1x+y_0,\qquad ar\ne0.
 \end{split}
\tag{3}
\]
All coefficients lie in \(L'\); both coefficient derivatives are extended
to fix \(x\). Thus \(Nx=\rho\), not necessarily one. No square root is
descended to the original field. Set
\[
 m=k_s\ne0,\quad p=m_t,\quad h=m_s\ne0,\quad
 \upsilon=\frac{ha^2+4r}{m}\ne0,\qquad
 T_0=2t+\frac1r\notin\mathbf C.
\tag{4}
\]
The exact necessary equations from554 are
\[
 r_s=\upsilon_s=0,\qquad a_s=-\frac{\upsilon}{a},\qquad
 h_s=\frac{3h\upsilon}{a^2},\qquad ha^2+4r=m\upsilon.
\tag{5}
\]
Write \(F_0=\ker(\partial_s:L'\to L')\). This is an exact finite extension
of \(\mathbf C(t)\); it is not assumed to equal \(\mathbf C(t)\).
Its \(t\)-constants are \(\mathbf C\). In particular,
\(r,\upsilon,T_0\in F_0\), with \(r\upsilon\ne0\).

**Claim.** No full actual chart satisfies (1)--(5). The proof imposes no
condition on the pair-boundary discriminant, a quartic pair numerator, or
any conic normal form. The complex-\(T_0\) and \(\upsilon=0\) branches are
not hypotheses or conclusions of this note.

## 2. Full potentials, moving derivatives and multiplier

The entire actual rows are
\[
 \begin{split}
 Y&=y+\sigma X+tX^2,\\
 Z&=2ty+\sigma^2+k_t\sigma+m\theta+n
                    +(2t\sigma+k)X+t^2X^2,\\
 W&=w+\theta X+sX^2.
 \end{split}
\tag{6}
\]
Use formal variables \((U,P,V)\), and define, before evaluation,
\[
 \begin{split}
 F(P,V)&=\frac{k_{tt}}2P^2+pPV+\frac h2V^2+n_tP+n_sV,\\
 G(U,P,V)&=\frac{\ell-(2P+k_t)U-F(P,V)}m,\\
 H(U,P,V)&=U^2+F_PU+F_VG
       +\frac{k_{ttt}}6P^3+\frac{p_t}2P^2V
       +\frac{h_t}2PV^2+\frac{h_s}6V^3\\
 &\hspace{12mm}+\frac{n_{tt}}2P^2+n_{ts}PV+\frac{n_{ss}}2V^2
       -\ell_tP-\ell_sV.
 \end{split}
\tag{7}
\]
The genuine identities are \(w=G(y,\sigma,\theta)\) and
\(H(y,\sigma,\theta)=h_0\in L'\). All formal gradients below are taken
before this substitution. The lower functions
\(c,d,e,y_2,y_1,y_0,k,n,\ell,h_0\) remain unrestricted except by the full
equations. In particular, the moving level is not differentiated as zero.

For clarity, the complete cleared multiplier equations from535 are printed
here. Put
\[
 \begin{gathered}
 f=H_U(y,\sigma,\theta),\qquad g=H_V(y,\sigma,\theta),\qquad
 D_f=\frac{2\sigma+k_t}{m},\\
 B_f=\frac{2y+k_{tt}\sigma+p\theta+n_t}{m},\qquad
 \nu=\frac{p\sigma+h\theta+n_s}{m},\\
 A_\beta=4x^2y_t+2x\theta_x y_s+y_x^2
                -2xc_t y_x-c_s y_x\theta_x,\\
 B_\beta=4x^2(\theta_t+B_f)+2xD_fy_x+y_x\theta_x
                +2x(\theta_s+\nu-c_t)\theta_x-c_s\theta_x^2.
 \end{gathered}
\tag{8}
\]
There is a coefficient unit \(\kappa\in L'^*\) such that
\[
 A_\beta=\kappa g,\qquad B_\beta=-\kappa f,\qquad
 J_{t,s,x}(Y,Z,W)=-\frac{a_0^4}{\rho}\in L'^*.
\tag{9}
\]
The last expression is independent of \(x\) and \(X\), not asserted to be
a complex constant. Under the moving affine change above,
\(J_x=J_{v_{\rm old}}/\rho\), the primitive-cross multiplier scales by
\(\rho\), and \(\kappa_x=\kappa_{v_{\rm old}}/\rho^2\).
This is the full denominator-free535 transport. It deletes neither the
critical point \(2x=0\) nor a zero gradient component.

## 3. The actual three-ring and its entire initial equation

The complete second potential (7) gives
\[
 w_6=[x^6]w=-\frac{ha^2+4r}{2m}=-\frac{\upsilon}{2},\qquad
 o=[x^5]w=-\frac{2q+a(p+hb)}m.
\tag{10}
\]
Consequently the literal rows (6) have exact intrinsic degrees
\((4,4,6)\), with initials
\[
 r\eta^4,\qquad (1+2tr)\eta^4=rT_0\eta^4,\qquad
 -\frac{\upsilon}{2}\eta^6.
\tag{11}
\]
In this branch \(T_0\ne0\), since it is noncomplex. No leading \(Z\)-drop
has been silently discarded.

Let \(K=\mathbf C(X)\) and \(R=K[Y,Z,W]\), the actual polynomial ring.
Extend \(N\) to \(\mathcal B=\mathcal A[u]\) by \(Nu=0\), and put
\[
 \Delta=a_0N-(NX)E.
\tag{12}
\]
It fixes \(X\). On \(\mathcal A\) it equals \(a_0N\), and
\(\Delta u=-Nx_0\); thus it is locally nilpotent on the actual ambient
ring and its localization \(R\). Explicitly, the successive derivatives
of \(u\) are \(-a_0^{j-1}N^jx_0\), so this conclusion does not assume
that \(NX\) is an \(N\)-constant. On the finite overfield
\(L'(X)(x)\), it is \(a_0\rho\partial_x\), killing \(L'(X)\).
It is nonzero. The usual local-slice argument for a nonzero LND gives
\(\operatorname{trdeg}_K\ker_R\Delta=2\), and in particular a
nonconstant polynomial invariant. No global slice for \(\Delta\) is used.

The original return gives
\(\operatorname{Frac}R=L(v_{\rm old})(X)\). The field \(L'(X)(x)\) is a
finite separable overfield of this field, not an asserted equal field or
polynomial-ring return. Actual coordinate partials extend uniquely to it.

The first two initials in (11) are algebraically independent over \(K\):
their ratio is the noncomplex element \(T_0\in L'\), transcendental over
\(\mathbf C\), and \(\eta\) is independent of the coefficient field.
A positive source-weight top of a nonconstant \(\Delta\)-invariant
vanishes under the entire initial map. Hence its kernel is nonzero and
has height one. It is generated by an irreducible weighted homogeneous
polynomial, and that polynomial involves \(\widehat W\).

There is also exact descent of this entire kernel to \(\mathbf C\).
The three leaders (11) do not involve the independent actual variable
\(X\). Clear the \(X\)-denominators in any \(K\)-relation and compare
coefficients of \(X\). Each is a complex-coefficient relation. Conversely
every complex relation remains a \(K\)-relation. Thus the whole kernel
over \(K\) is the scalar extension of the complex kernel. The latter is
again a height-one prime, and its homogeneous generator remains a
generator over \(K\).

Here is the required degree bound, on the actual ring. The extended
actual partial \(T_W=\partial/\partial W\), holding \(X,Y,Z\) fixed, is
given by Cramer's rule in \((t,s,x)\). The \(t,s\) cofactors use the
degree-four rows \(Y,Z\), with one \(x\)-derivative, and have degree at
most seven; its \(x\)-cofactor has degree at most eight. The denominator
is the coefficient unit (9). Since \(L'\) is finite separable over
\(\mathbf C(t,s)\), coefficient derivatives are the extended \(t,s\)
derivatives. It follows for every nonzero polynomial in \(L'(X)[x]\) that
\[
 \deg_x(T_W f)\le\deg_x f+7.
\tag{13}
\]
The zero derivative causes no exception to this inequality. Actual
iterates remain polynomials and the same bound applies at every step.

Write the source-weight top of any positive-weight invariant as
\(H_{\rm in}^{\ell}G_0\), where \(H_{\rm in}\nmid G_0\), and call its
weight \(M\). In characteristic zero,
\(\partial_{\widehat W}H_{\rm in}\notin(H_{\rm in})\).
Differentiating exactly \(\ell\) times gives a nonzero residue
\(\ell!H_{{\rm in},\widehat W}^{\ell}G_0\) modulo the **full** kernel.
Every lower source part remains strictly lower in weight. Therefore
\[
 \deg_x T_W^{\ell}f=M-6\ell\le7\ell,\qquad
 \operatorname{wt}H_{\rm in}\le13.
\tag{14}
\]
All weights are even, so the bound is twelve. Independence of the
\(Y,Z\) initials requires at least two nonzero \(W\)-blocks in a
relation. In a homogeneous polynomial of weights \((4,4,6)\), two
\(W\)-exponents differ by a positive even integer. The weight is
therefore at least twelve. At weight twelve the only possibilities are
\(\widehat W^2\) and a homogeneous cubic in \(\widehat Y,\widehat Z\).
The first has nonzero coefficient. Rescaling by a complex constant gives
\[
 H_{\rm in}=\widehat W^2+Q_3(\widehat Y,\widehat Z),\quad
 Q_3\in\mathbf C[\widehat Y,\widehat Z],\quad
 \mathcal P(T):=Q_3(1,T),\quad
 \mathcal P(T_0)=-\frac{\upsilon^2}{4r^3}.
\tag{15}
\]
This is the entire initial kernel, not a selected relation or a
coefficient-field coordinate change.

## 4. A finite presentation reduction forces a transverse constant

Let \(\mathcal F=H_{\rm in}(Y,Z,W)\in R\), an actual polynomial, and set
\(\phi=[x^{11}]\mathcal F\). It is not assumed that \(\mathcal F\) is an
ambient coordinate. Its degree is at most eleven. We prove
\[
 \phi_s=0.
\tag{16}
\]
If \(\phi=0\), this is immediate. Otherwise suppose \(\phi_s\ne0\).
An element algebraic over \(F_0\) is killed by \(\partial_s\), by
separability. Thus \(\phi\) is transcendental over \(F_0\), and
\(\deg_x\mathcal F=11\).

Adjoin a formal source variable \(\widehat V\) representing
\(\mathcal F\), with source weights \((4,4,6,11)\). The original three
initials have field rank two and lie in \(F_0(\eta)\). The fourth initial
\(\phi\eta^{11}\) is transcendental over that field, also after adjoining
the independent \(X\). Hence the entire four-generator initial kernel
has height one. It contains the irreducible \(H_{\rm in}\), so it is
exactly \((H_{\rm in})\).

The actual presentation relation is
\(H_{\rm in}-\widehat V\), whose two displayed weights are twelve and
eleven. For any \(\Delta\)-invariant, a positive highest-weight source
part must lie in the full initial kernel, because
\(\Delta=a_0\rho\partial_x\) and such an invariant has intrinsic degree
zero. If the highest part is \(H_{\rm in}G_1\), subtract
\((H_{\rm in}-\widehat V)G_1\) from its source representative. This
preserves the actual polynomial and strictly lowers its highest source
weight. Repeating terminates at weight zero. It would make every
\(\Delta\)-invariant an element of \(K\), contrary to transcendence
degree two. This proves (16). It is a finite integer-weight reduction
for each polynomial, not a finite SAGBI assertion.

The complete coefficient of degree eleven uses
\(Y_3=q\), \(Z_3=2tq+ma\), and \(W_5=o\); the \(X\)-dependent additions
in (6) do not reach these positions. Thus, putting
\(Q=\mathcal P'(T_0)\),
\[
 \begin{split}
 \phi&=-\upsilon o+r^2\{(3\mathcal P(T_0)-T_0Q)q
                                      +Q(2tq+ma)\}\\
      &=-\upsilon o+\left(-\frac{3\upsilon^2}{4r}-rQ\right)q+r^2maQ,\\
 \phi_s&=-\upsilon o_s+\left(-\frac{3\upsilon^2}{4r}-rQ\right)q_s
                                                -\frac{4r^3Q}{a}.
 \end{split}
\tag{17}
\]
In particular \(\phi\) has no actual \(X\)-dependence. In the last line
we used \(Q_s=0\) and \((ma)_s=-4r/a\), both genuine consequences of
(5). No nonzero assumption on \(Q\), \(q\) or \(o\) has been made.

## 5. Whole high coefficients and their genuine compatibility

The following four equations come from the **complete** expressions
(7)--(9), with the lower coefficients of (3) still present:
\[
 \begin{split}
 E_5&:=mo+2q+a(p+hb)=0,\\
 H_8&:=[x^8](H(y,\sigma,\theta)-h_0)
       =r^2+ha o+\upsilon hb-\frac{\upsilon p}{2}
                                      +\frac{a^2h_t}{2}=0,\\
 B_5&:=[x^5](B_\beta+\kappa f)
       =4a_t+6ab_s+4ba_s+12ar-10o-\frac{2\kappa ha}{m}=0,\\
 A_6&:=[x^6](A_\beta-\kappa g)
       =4r_t+6aq_s+16r^2-\frac{4\kappa hr}{m}=0.
 \end{split}
\tag{18}
\]
For example, the formal derivative is taken before evaluation to obtain
\([x^6]g=4hr/m\). Before using (5), the contributions to \(H_8\) are
\(r^2+ha o+(p+hb)w_6+h_sa^2b/2+h_ta^2/2\).
These statements retain the full support; neither \(H\) nor its formal
gradient is replaced by a truncated on-level relation.

Differentiating the defining equation for \(\upsilon\) gives
\[
 m\upsilon_t+\upsilon p=a^2h_t+2ha a_t+4r_t.
\tag{19}
\]
The temporary coefficient
\(L_*=(2r_t-r^2-m\upsilon_t/2)/(ha)\) allows two consequences of
(18)--(19) to be written without solving for a possibly zero lower
coefficient:
\[
 \begin{gathered}
 o=a_t-\frac{\upsilon b}{a}+L_*,\\
 b_s=\frac{a_t}{a}-\frac{\upsilon b}{a^2}-2r
                          +\frac{5L_*}{3a}+\frac{\kappa h}{3m},\\
 q_s=\frac{2}{3a}\left(\frac{\kappa hr}{m}-r_t-4r^2\right).
 \end{gathered}
\tag{20}
\]
All denominators here were already nonzero in (3)--(4).

Use the entire derivative of the second-potential equation:
\[
 (E_5)_s=h o+m o_s+2q_s+a_s(p+hb)
                         +a(h_t+h_sb+hb_s)=0.
\tag{21}
\]
Substitution of (5), (19) and (20) gives exactly
\[
 o_s=\frac{\upsilon_t+6r\upsilon}{3a}
                              -\frac{\kappa h\upsilon}{3am}.
\tag{22}
\]
This does not differentiate \(p\) at fixed \(m\): the derivative used in
(21) is the genuine \(p_s=h_t\).

For completeness, the other genuine derivative needed here is
\[
 (h_t)_s=(h_s)_t=\frac{3h_t\upsilon}{a^2}
                 +\frac{3h\upsilon_t}{a^2}
                 -\frac{6h\upsilon a_t}{a^3}.
\tag{23}
\]
The full derivative of the second line of (18) is
\[
 \begin{split}
 (H_8)_s={}&(h_sa+ha_s)o+ha o_s+\upsilon h_sb+\upsilon hb_s
      -\frac{\upsilon h_t}{2}+aa_sh_t+\frac{a^2(h_t)_s}{2}.
 \end{split}
\tag{24}
\]
After substituting (5), (19), (20), (22) and (23), the complete right side
of (24), not just selected summands, is
\[
 -\frac{11}{3a^2}\mathscr C,\qquad
 \mathscr C:=r^2\upsilon+2r\upsilon_t-2r_t\upsilon.
 \quad\text{Consequently }\mathscr C=0.
\tag{25}
\]
Equivalently \(\upsilon_t/\upsilon=r_t/r-r/2\). The polynomial form in
(25) is the one used below. No division by \(p\), \(r_t\), \(T_{0,t}\),
\(b\), \(q\), \(o\), or any optional coefficient occurs.

## 6. The division-free endpoint

Differentiate (15) in the genuine \(t\)-direction. The coefficients of
\(\mathcal P\) are complex, so the exact polynomial consequence is
\[
 \mathscr D:=-2r\upsilon\upsilon_t+3\upsilon^2r_t
                   -4r^2Q(2r^2-r_t)=0.
\tag{26}
\]
In particular we have not divided by \(T_{0,t}=2-r_t/r^2\).
Substitute the full \(q_s,o_s\) from (20) and (22) into (17). Direct
collection, retaining every term, gives the cleared identity
\[
 6amr\,\phi_s=-\kappa hr\,\mathscr S+m\mathscr D,
 \qquad \mathscr S:=\upsilon^2+4r^2Q.
\tag{27}
\]
It follows from (16), (26) and \(\kappa hr\ne0\) that
\(\mathscr S=0\). Finally the following is a polynomial identity:
\[
 \mathscr D+\upsilon\mathscr C+(2r^2-r_t)\mathscr S
                                  =3r^2\upsilon^2.
\tag{28}
\]
The left side is zero by (25)--(27), whereas the right side is nonzero.
This is the required contradiction. It retains \(Q=0\),
\(T_{0,t}=0\), \(r_t=0\), \(p=0\), and all zero optional lower
coefficients as honest boundaries; none was divided out.

## 7. Scope and verification record

The conclusion is only the exclusion of the full actual554 branch
\(h\ne0\), \(\upsilon\ne0\), \(T_0\notin\mathbf C\). The complementary
complex-ratio and transverse exclusions are separate sources570 and568.
They are not used to obtain (28). No arbitrary chart-entry theorem,
recognition statement for an unrelated chart, rationality assertion for
\(F_0\), or general cancellation theorem is claimed.

The actual polynomial \(\mathcal F\), the intrinsic parameter \(x\), the
auxiliary source variable \(\widehat V\), and the coefficient functions
were never promoted to ambient coordinates. The finite overfield was used
only for exact coefficient derivations, intrinsic degree and extended actual
partials. The original slice and selected derivation were kept throughout.

The complete direct input sources264,296,535 and554 were read. Fresh unsaved
algebra reconstructed the whole formal \(H\) and its formal gradients, the
entire multiplier polynomials, the actual second potential, and the full
degree-eleven coefficient of the actual initial relation. It also checked
(21)--(25) with genuine mixed derivatives and the complete cleared
identities (27)--(28). Independent outline reconstructions by the parent
and the two peer audits agreed. This evidence is not a replacement for the
proof and is not represented as an independent saved-source review of this
file. No saved checker was executed, imported or compiled. No canonical
file was edited, and no novelty claim is made.
