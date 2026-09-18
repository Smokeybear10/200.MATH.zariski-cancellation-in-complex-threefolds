# Explicit polynomial clearing of the terminal quintic symmetry

In the terminal moving-quintic rank-drop case, four powers of the
actual invariant \(g\) clear the entire nice rational symmetry.
The coefficients can be written using actual second iterates of
the two bad coordinates. Their exact original-derivation chain
and the obstruction to lowering that clearing power are explicit.

This does not provide a global slice for the cleared field or
recognize the original kernel.

## 1. Actual coordinates and terminal identities

Retain the original action, slice, and terminal constant-residual
case of [the higher rank-drop reduction](independent-higher-rank-drop-pass72.md),
Section 4. In particular \(E\) is an actual sliced polynomial LND,
\(0\ne g\in\ker E\), and \(\delta=E/g\) acts on \(B_g\).
The terminal normalized layers are
\[
h_4=c\sigma+e,\qquad h_3=c\tau+e\sigma+v_0,
\qquad \delta\sigma=1,\quad\delta\tau=\sigma,
\]
\[
(h_2)_B=e_B\left(\frac{4\tau}{3}-\frac{\sigma^2}{6}\right)
                  +\mu\sigma+\nu_1e_B+\nu_2\mu,
\quad e_B=(1,0),\quad\mu=(\mu_1,\mu_2),\quad\mu_2\ne0.
\tag{1}
\]
The constants \(c=e_1,e,v_0\) satisfy \((v_0)_B=\mu\).
Set \(u_0=\tau-\sigma^2/2\).
The fully established rational symmetry is
\[
S=T_{v_0}+\beta T_e+\gamma T_c,
\quad \beta=\frac{\sigma-2\nu_2}{3},\quad
\gamma=\frac{\sigma^2}{12}-\frac{\nu_2\sigma}{6}
                      +\frac{u_0}{3}-\frac{\nu_1}{2},
\]
\[
[\delta,S]=0,\quad S\sigma=Su_0=0,\quad S^2x=0,
\quad Sg=0,\quad [E,S]=0.
\tag{2}
\]
Here \(Sg=0\) was proved by the original-slice unit argument,
not assumed from normalized commutation. The field is an LND
of \(B_g\), but need not preserve \(B\).

Choose a second original good constant direction \(c_2\) and
use actual coordinates dual to \((c,e,v_0,c_2)\), denoted
\((a_0,b,z,w)\). In particular
\[
z=Y/\mu_2,\qquad b=X-(\mu_1/\mu_2)Y,
\qquad T_c=\partial_{a_0},\quad T_e=\partial_b,
\quad T_{v_0}=\partial_z.
\]
Both \(\partial_{a_0}\) and \(\partial_w\) are original good
partials. Taking the two bad linear combinations in (1) gives
\[
\delta^2z=\sigma+\nu_2,\qquad
\delta^2b=\frac{\sigma^2}{2}+\frac{4u_0}{3}+\nu_1.
\tag{3}
\]
These are actual rational identities whose products by \(g^2\)
are original polynomial second iterates.

## 2. A constant shear and its coefficient rates

Make the actual constant shear
\[
a=a_0-\frac{\nu_2}{2}b,
\qquad a_0=a+\frac{\nu_2}{2}b,
\tag{4}
\]
fixing \(b,z,w\). Then
\[
S=\partial_z+\beta\partial_b+\kappa\partial_a,
\quad\kappa=\gamma-\frac{\nu_2}{2}\beta
=\frac{\sigma^2}{12}-\frac{\nu_2\sigma}{3}
 +\frac{u_0}{3}-\frac{\nu_1}{2}+\frac{\nu_2^2}{3}.
\tag{5}
\]
Since \(S\beta=S\gamma=0\), all three displayed coefficients
are fixed by \(S\). Direct differentiation gives
\[
\delta\beta=\frac13,\qquad
\delta\kappa=\frac\beta2,\qquad
h:=\kappa-\frac34\beta^2\in\ker\delta\cap\ker S.
\tag{6}
\]
The two actual good partials remain \(\partial_a=T_c\) and
\(\partial_w=T_{c_2}\). The new \(b\)-partial is
\(T_e+(\nu_2/2)T_c\), so its original second adjoint is still
\(V_X\). The original top identity therefore remains
\[
\operatorname{ad}_E^2\partial_a=0,
\qquad g[E,\partial_a]=-2V_X,
\qquad \operatorname{ad}_E^2\partial_b=V_X.
\tag{7}
\]
No additional good-partial cancellation is asserted.

## 3. Actual polynomial numerators and one explicit bound

Put \(q=E^2z\in B\). Equation (3) gives
\[
n:=g^2\beta=\frac{q-3\nu_2g^2}{3}\in B.
\tag{8}
\]
Expressing \(\kappa\) using the other identity of (3) gives
the actual polynomial
\[
\begin{aligned}
Q:=g^4\kappa
={}&\frac{g^2}{4}E^2b-\frac{3n^2}{8}
       -\frac{3\nu_2}{2}g^2n
       -\left(\frac{\nu_2^2}{2}+\frac{3\nu_1}{4}\right)g^4\\
={}&\frac{g^2}{4}E^2b-\frac{q^2}{24}
       -\frac{\nu_2}{4}g^2q
       +\left(\frac{5\nu_2^2}{8}-\frac{3\nu_1}{4}\right)g^4.
\end{aligned}
\tag{9}
\]
All terms on either right side are actual polynomials. In particular
the rational expressions defining \(\sigma,u_0\) have not simply
been declared regular.

Consequently the complete field has a specific global representative
\[
\boxed{\ T=g^4S=g^4\partial_z+g^2n\partial_b+Q\partial_a
\in\operatorname{Der}_k(B).\ }
\tag{10}
\]
The polynomial coefficients are fixed by \(S\), hence by \(T\).
Thus \(T^2(a,b,z,w)=0\); the polynomial translation flow proves
that \(T\) is a global nice LND. Since \(Eg=0\) and \([E,S]=0\),
\([E,T]=0\). It is nonzero because \(Tz=g^4\ne0\).
The coordinate \(z\) is not given a global slice by this construction.

Equations (6),(8),(9) give the exact original coefficient chain
\[
Eg=0,\qquad En=\frac{g^3}{3},\qquad
EQ=\frac{g^3n}{2},\qquad E^2Q=\frac{g^6}{6},\qquad E^3Q=0.
\tag{11}
\]
In terms of the actual coefficients \(G=g^4\), \(N=g^2n\)
of \(T\), this reads
\[
EG=0,\qquad EN=\frac{gG}{3},\qquad
EQ=\frac{gN}{2},\qquad E^2Q=\frac{g^2G}{6}.
\tag{12}
\]
Also \(Tg=Tn=TQ=Tw=0\), and
\[
H:=Q-\frac34n^2=g^4h\in B,\qquad EH=TH=0.
\tag{13}
\]
These are original-ring identities, not statements on a generic fiber.
They permit applying the nice three-variable linear-invariant statement
over \(k(w)\), if needed separately; they do not make \(E\) linear
over that field when \(Ew\ne0\).

## 4. Exactly what would lower the clearing power

Equation (9) implies
\[
Q\equiv-3n^2/8\pmod{g^2B}.
\tag{14}
\]
Since \(\beta=n/g^2\), \(\kappa=Q/g^4\), and these are
coefficients on genuine coordinate partials, one has
\[
g^2S\text{ is polynomial}\ \Longleftrightarrow\ g^2\mid Q
\ \Longleftrightarrow\ g\mid n,
\]
\[
g^3S\text{ is polynomial}\ \Longleftrightarrow\ g\mid Q
\ \Longleftrightarrow\ g\mid n^2.
\tag{15}
\]
The last implications use (14) and unique factorization in the actual
ring \(B\). They retain every multiplicity of \(g\). In particular
no squarefree replacement of \(g\) is involved.

If a prime \(\pi\mid g\) satisfies \(\pi\nmid n\), then (14)
gives \(v_\pi(Q)=0\) and
\[
v_\pi(\kappa)=-4v_\pi(g).
\tag{16}
\]
In that conditional situation no smaller nonnegative integer power
of \(g\) clears the field at \(\pi\). This is a valuation boundary,
not an assertion that such a prime occurs in an actual full frame.
Conversely the present calculation does not prove \(g\mid n\)
or claim that four powers are necessary in every actual instance.

## Scope and verification

The third-image lemma separately gives
\(\delta^2w=\lambda\in\mathbb C\), hence
\(E^2w=\lambda g^2\); its proof was fully read for the scope of
the surviving good coordinate. This clearing argument does not
require \(\lambda=0\) or supply that conclusion.
The lemma is [the separate full-image result](quintic-rank-drop-third-image-pass72.md).

The exact numerator formulas, their equality, and the two original
derivative identities were independently expanded in a single inline
SymPy diagnostic, with all five remainders zero. This is not a new
standalone suite or test-method count, nor a computational proof of
the full-frame identities. The written actual-ring derivation above
is the justification of polynomiality and local nilpotence.

No original slice was transferred to \(T\); no polynomial kernel,
global coordinate section, or terminal recognition is inferred here.
No frozen pass71 or earlier file, shared metadata, regression record,
or checkpoint was changed.
