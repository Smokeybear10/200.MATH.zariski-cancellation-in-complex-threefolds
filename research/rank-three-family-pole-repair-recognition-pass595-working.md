# Polynomial pole repair for a family of sliced rank-three extensions

## 1. Result and scope

Work over \(\mathbb C\). Let \(m,n\ge2\), let
\(F(X,Z)\in\mathbb C[X,Z]\), and assume
\(F(X,0)\notin\mathbb C\). Define
\[
 \begin{gathered}
 B=\mathbb C[x,y,z,t],\qquad f=xz-y^m,\qquad
 R(x,f)=xF(x,f),\qquad r=R(x,f)+yf^n,\\
 g=\frac{f^{mn+1}+r^m}{x},\qquad
 H=\operatorname{Jac}(f,g,\cdot),\qquad
 E=H+(1-gf^{n-1}r)\partial_t,\\
 v=ft-r^2/2,\qquad
 u=t+gf^{n-2}rv+\frac{g^2f^{2n-3}}2v^2.
 \end{gathered}
\tag{1}
\]
The Jacobian convention uses, in order, the gradients of \(f,g\)
and the argument. The notation \(R(x,f)\) denotes the displayed
polynomial, not an additional coefficient ring.

This source proves that \(E\) is locally nilpotent, \(Eu=1\), and
that the specific polynomial \(u\) is an actual coordinate of \(B\).
Consequently
\[
 \ker E\cong\mathbb C^{[3]}.
\tag{2}
\]
The proof constructs a localized automorphism taking \(t\) to \(u\),
repairs its pole by a second localized automorphism, and proves that
both the repaired map and its inverse are polynomial. It retains
arbitrary coefficients of \(F\), including all dependence on its
second argument. The additional finite terms when \(n=2\) are
computed explicitly.

The field \(H\) is the rank-three family of
[Dasgupta--Gaifullin, Theorem 5.7, version 2](https://arxiv.org/html/2306.00510v2),
with their new invariant renamed \(g\). The stated parameter
conditions are exactly within that theorem. The family construction,
Theorem 5.7 and its proof, and the relevant local-slice Theorem 2.17
were read. Their rank and kernel conclusions identify the input
family; the polynomial repair below does not require a new proof of
that external rank classification. Local nilpotence is also proved
directly below, so no rank argument is used to license an exponential.

The result concerns this specified extension, not arbitrary sliced
extensions of rank-three derivations, arbitrary commuting actions,
or cancellation in dimension four. It makes no novelty claim and
does not claim that all earlier subfamilies were previously unrecognized.
The affine-in-\(t\) and affine-frame obstructions in592 remain
compatible with the nonlinear coordinate construction here.

## 2. Complete polynomial and local-slice input

The apparent division by \(x\) in (1) is exact. Expanding gives
\[
 g=zf^{mn}+
 \sum_{j=1}^{m}\binom mj x^{j-1}F(x,f)^j
                   y^{m-j}f^{n(m-j)}\in B.
\tag{3}
\]
The polynomial \(f=xz-y^m\) is prime: it is primitive and linear in
\(z\) over \(\mathbb C[x,y,t]\), with coprime coefficients
\(x,-y^m\). In particular \(f\nmid x\). Also \(g\ne0\).
For example, in \(B_x=\mathbb C[x,x^{-1},y,f,t]\), its numerator
has nonzero coefficient \(f^{mn}\) at \(y^m\).

Direct Jacobian calculation gives
\[
 Hf=Hg=0,\qquad Hr=-gf^n,\qquad
 Hx=-mr^{m-1}f^n.
\tag{4}
\]
One way to check both signs is to use
\(\operatorname{Jac}(f,r,x)=-xf^n\), and then differentiate
\(g=(f^{mn+1}+r^m)/x\) with respect to \(r\) or \(x\),
holding \(f\) and the other argument fixed.

Here is a direct license for local nilpotence. In the localization
of \(\mathbb C[x,y,z]\) at \(fg\),
\[
 \begin{aligned}
 x&=(f^{mn+1}+r^m)/g,\\
 y&=(r-xF(x,f))/f^n,\\
 z&=\frac{g+\sum_{i=1}^{m}(-1)^i\binom mi
                r^{m-i}x^{i-1}F(x,f)^i}{f^{mn}}.
 \end{aligned}
\tag{5}
\]
Thus that localization equals
\(\mathbb C[f^{\pm1},g^{\pm1},r]\). This equality also shows that
\(f,g,r\) are algebraically independent, by transcendence degree.
On this ring \(H=-gf^n\partial_r\); it is locally nilpotent and
preserves the original polynomial ring. Hence \(H\) is an LND there.
Extending to \(t\) as in (1) is locally nilpotent as well, since
\[
 Et=1-gf^{n-1}r,\qquad E^2t=g^2f^{2n-1},\qquad E^3t=0.
\tag{6}
\]
Local nilpotence on the finitely many polynomial generators implies
local nilpotence on the whole polynomial ring by the Leibniz rule.

Put \(b=-gf^{n-2}\). Then \(Eb=0\), \(Er=f^2b\), and
\[
 Ev=f,\qquad q:=fbv-r\in\ker E,\qquad
 v+q^2/2=fu.
\tag{7}
\]
All these are polynomial identities. Applying \(E\) to the last
one proves \(Eu=1\), since \(f\ne0\) in the domain \(B\).
This step does not yet assume that \(u\) is an ambient coordinate.

## 3. The first localized automorphism

On \(B_f\), define
\[
 L=H/f+br\partial_t.
\tag{8}
\]
It fixes \(f,g,b,v\), and
\(Lr=fb\), \(Lt=br\), \(L^2t=fb^2\), \(L^3t=0\).
The restriction \(H/f\) is locally nilpotent because \(f\) is
invariant. These formulas license local nilpotence on \(B_f\),
and then also of \(-vL\), since \(Lv=0\). Consequently
\[
 \Phi=\exp(-vL)\in\operatorname{Aut}(B_f),\qquad
 \Phi f=f,\quad\Phi g=g,\quad\Phi t=u,\quad
 r':=\Phi r=r+gf^{n-1}v.
\tag{9}
\]
The first transformed coordinate is polynomial:
\[
 X:=\Phi x
 =x+\sum_{j=1}^{m}\binom mj
             r^{m-j}g^{j-1}f^{j(n-1)}v^j\in B,
 \qquad X\equiv x\pmod f.
\tag{10}
\]
To derive (10), apply \(\Phi\) to \(xg=f^{mn+1}+r^m\)
and expand \((r+gf^{n-1}v)^m-r^m\). Cancelling the nonzero
factor \(g\) proves the displayed formula; no inverse of \(g\)
occurs in it, and no locus \(g=0\) is removed from the result.
The coordinate whose pole will be repaired explicitly is
\[
 \Phi y=\frac{N}{f^n},\qquad
 N=r'-R(X,f)
   =yf^n+gf^{n-1}v-[R(X,f)-R(x,f)].
\tag{11}
\]

## 4. Full residue and finite part, with the \(n=2\) terms

Finite \(f\)-adic computations can be made in
\(B_x=\mathbb C[x,x^{-1},y,f,t]\). There \(f\) is an independent
polynomial variable, not an implicit abbreviation during expansion.
All divisibility conclusions about polynomials in \(B\) descend
from \(B_x\): if \(f^k\mid x^jP\) and \(P\in B\), primality
of \(f\) and \(f\nmid x\) imply \(f^k\mid P\) in \(B\).

Write
\[
 s(x)=R(x,0),\qquad s_1(x)=[f]R(x,f),\qquad
 \epsilon=\begin{cases}1,&n=2,\\0,&n\ge3.\end{cases}
\tag{12}
\]
Both \(s\) and \(s_1\) are divisible by \(x\). Primes in the
next formulas mean ordinary derivatives with respect to \(x\).
Define polynomial first jets and auxiliary coefficients by
\[
 \begin{aligned}
 G_0&=s^m/x,& G_1&=m s^{m-1}s_1/x,\\
 M_0&=m s^{m-1},&M_1&=m(m-1)s^{m-2}s_1,\\
 v_0&=-s^2/2,&v_1&=t-ss_1,\\
 T_0&=G_0-M_0s',&T_1&=G_1-M_1s'-M_0s_1',\\
 d_1&=M_0v_0,&e_1&=M_0v_1+M_1v_0,\\
 d_2&=\binom m2 s^{m-2}G_0v_0^2,&&\\
 C&=v_0T_0
   =\frac m2s^{m+1}s'-\frac{s^{m+2}}{2x}.&&
 \end{aligned}
\tag{13}
\]
Every division by \(x\) in this ledger is exact in
\(\mathbb C[x]\). In particular \(C\in x^{m+1}\mathbb C[x]\)
and \(C/x\) is polynomial. No division by \(s,C,s'\), or a
coefficient of \(F\) is used.

Since \(n\ge2\), the whole first jets in \(B_x\) are
\[
 r\equiv s+s_1f,\qquad
 g\equiv G_0+G_1f,\qquad
 v\equiv v_0+v_1f\pmod{f^2}.
\tag{14}
\]
The \(y\) term in \(r\) begins at \(f^n\). Its contributions
to \(g,v\) also begin too late to change (14). Substituting
the entire sum (10), with no lower coefficient of \(F\) set to
zero, gives
\[
 X-x\equiv f^{n-1}d_1+f^n(e_1+\epsilon d_2)
                                      \pmod{f^{n+1}}.
\tag{15}
\]
Indeed the \(j=2\) summand can survive only when \(n=2\).
All \(j\ge3\) terms have order at least
\(3(n-1)\ge n+1\). The complete Taylor difference needed in
(11) is
\[
 R(X,f)-R(x,f)
 \equiv s'(X-x)+f s_1'(X-x)
       +\epsilon\frac{s''}{2}f^2d_1^2
                                      \pmod{f^{n+1}}.
\tag{16}
\]
Higher \(x\)-Taylor terms and all unused higher \(f\)-jets have
order at least \(n+1\). In particular this is not an ansatz
truncating \(F\): the discarded terms cannot affect the required
residue or constant term, for every \(m,n\) in scope.

Combining (11), (14)--(16) yields the full congruence
\[
 \begin{aligned}
 N&\equiv Cf^{n-1}+f^n(y+A_{\rm pre})\pmod{f^{n+1}},\\
 A_{\rm pre}&=v_1T_0+v_0T_1
             -\epsilon(s'd_2+s''d_1^2/2).
 \end{aligned}
\tag{17}
\]
In particular \(N-Cf^{n-1}\in f^nB\), by the divisibility
descent above. Thus \(\Phi y\) has at most a simple \(f\)-pole,
and its entire residue is the polynomial \(C(x)\).

## 5. Repair and polynomiality of every image

Let
\[
 \delta_0=x\partial_y+m y^{m-1}\partial_z,\qquad
 \Gamma=\exp\!\left(-\frac{C(x)}{xf}\delta_0\right),
 \qquad \Psi=\Phi\circ\Gamma.
\tag{18}
\]
The derivation \(\delta_0\) is triangular and locally nilpotent,
and fixes \(x,f,t\). Since \(C/x\) is polynomial, its displayed
invariant multiplier belongs to \(B_f\). Hence \(\Gamma\) and
\(\Psi\) are automorphisms of exactly \(B_f\); an extra
localization at \(x\) is not being assumed here.
Their relevant images are
\[
 \Psi x=X,\qquad \Psi t=u,\qquad \Psi f=f,\qquad
 Y:=\Psi y=\Phi y-C(X)/f.
\tag{19}
\]
Because \(X-x\in fB\), \(C(X)-C(x)\in fB\), so (17)
proves \(Y\in B\). The precise remaining constant term is
\[
 Y\equiv y+A(x,t)\pmod f,\qquad
 A=v_1T_0+v_0T_1
   -\epsilon(s'd_2+s''d_1^2/2+C'd_1).
\tag{20}
\]
The last summand is essential at \(n=2\): it comes from
\((C(X)-C(x))/f\). All second and higher Taylor terms of
\(C(X)\) vanish in that quotient modulo \(f\).

The remaining image \(Z:=\Psi z\) initially belongs
to \(B_f\). Applying \(\Psi\) to \(f=xz-y^m\) gives
\[
 XZ=f+Y^m\in B.
\tag{21}
\]
Since \(X\equiv x\pmod f\), one has \(f\nmid X\).
If \(Z=P/f^k\) for \(P\in B\), (21) implies \(f^k\mid XP\)
and hence \(f^k\mid P\). Therefore \(Z\in B\). The restriction
of \(\Psi\) to \(B\) is now a polynomial endomorphism. This
argument uses primality of \(f\), not an assumption that a
Jacobian determinant alone proves global invertibility.

## 6. Full quotient automorphism and inverse denominator descent

In fact \(A\in x\mathbb C[x,t]\). To see this without assuming
any coefficient nonzero, note that \(T_0,T_1\in x^{m-1}\mathbb C[x]\),
\(d_1\in x^{m+1}\mathbb C[x]\),
\(d_2\in x^{2m+1}\mathbb C[x]\), and
\(C'\in x^m\mathbb C[x]\). These assertions include \(m=2\).
Define
\[
 Q(x,t)=A(x,t)/x\in\mathbb C[x,t],\qquad
 P(x)=-\epsilon\frac{s^{m+3}}{2x}\in\mathbb C[x].
\tag{22}
\]
Formula (1) gives \(u\equiv t+P(x)\pmod f\): only the first
correction to \(t\) survives when \(n=2\), and neither correction
survives when \(n\ge3\). Consequently the whole map modulo \(f\)
is induced by the following polynomial map:
\[
 \beta:\quad
 \begin{cases}
 x\longmapsto x,\\
 t\longmapsto t+P(x),\\
 y\longmapsto y+xQ(x,t),\\
 z\longmapsto z+\big((y+xQ(x,t))^m-y^m\big)/x.
 \end{cases}
\tag{23}
\]
The division in the last line is exact. The equality with
\(\overline\Psi\) for the \(z\) image follows from (21), after
reducing modulo \(f\) and cancelling the nonzero element \(x\)
in the domain \(B/(f)\).

Map (23) fixes \(f\) and has the full polynomial inverse
\[
 \beta^{-1}:\quad
 \begin{cases}
 x\longmapsto x,\\
 t\longmapsto t-P(x),\\
 y\longmapsto y-xQ_-(x,t),\\
 z\longmapsto z+\big((y-xQ_-(x,t))^m-y^m\big)/x,
 \end{cases}
 \qquad Q_-(x,t)=Q(x,t-P(x)).
\tag{24}
\]
Both composition orders give the identity by substitution; in
particular \(\overline\Psi\) is an automorphism of \(B/(f)\).
Injectivity alone would suffice for the next step.

The localized map \(\Psi_f\) already has an inverse. For any
\(h\in B\), write \(\Psi_f^{-1}(h)=p/f^k\), \(p\in B\),
with \(k\ge0\) minimal. If \(k>0\), then \(f\nmid p\), whereas
\(\Psi(p)=f^kh\). Reduction modulo \(f\) contradicts the
injectivity of \(\overline\Psi\). Thus \(k=0\). Applying this
to each polynomial generator proves
\[
 \Psi\in\operatorname{Aut}_{\mathbb C}(B),\qquad \Psi(t)=u.
\tag{25}
\]
This proves the inverse on the whole polynomial ring, not just on
the local-slice subring or away from the exceptional divisor.

## 7. Recognition and exact boundaries

Since \(Eu=1\), the finite Taylor homomorphism
\[
 \pi_E(h)=\sum_{j\ge0}\frac{(-u)^j}{j!}E^j(h)
\tag{26}
\]
maps \(B\) onto \(\ker E\), kills \(u\), and induces an
isomorphism \(B/(u)\cong\ker E\). Equivalently the slice theorem
follows here by the finite Taylor expansion, giving
\(B=(\ker E)[u]\). By (25), \(B/(u)\) is a three-variable
polynomial ring, proving (2).

More concretely, \(\pi_E(X),\pi_E(Y),\pi_E(Z)\) are three
algebraically independent generators of \(\ker E\), because
their residue classes are the three coordinates of \(B/(u)\)
provided by \(\Psi\). This Taylor step is necessary: the fact
\(\Psi(t)=u\) alone does not assert that \(X,Y,Z\) are
\(E\)-invariant or that \(\Psi\) directly conjugates \(E\)
to the original \(\partial_t\).

For the concrete member \(m=n=2,F(x,f)=x^4\), the ledger gives
\[
 s=x^5,\qquad C=\frac92x^{19},\qquad
 A=-9x^9t+\frac{297}{4}x^{33},\qquad P=-x^{24}/2.
\tag{27}
\]
Thus the construction contains the repaired concrete extension
studied separately in594. It does not change the absence of slices
affine in the original \(t\), or the minimum of two for actual
Euler shift over positive affine-linear frames proved in592.
It supplies a genuinely nonlinear coordinate change. With the
three invariant generators just constructed, the actual frame
\((u,\pi_E(X)+u,\pi_E(Y)+u,\pi_E(Z)+u)\) has all \(E\)-degrees
one and weighted Euler shift zero.

The argument never divides by \(s,C,Q,P,g\) in a claimed
polynomial map, and allows all optional lower coefficients or
finite-part corrections to vanish. Localization at \(fg\) was
used only to prove local nilpotence; the two exponential maps
and their repair live in \(B_f\), with explicit denominator
descent to \(B\). No general nonlinear-frame algorithm, arbitrary
rank-three extension recognition, or general cancellation theorem
is asserted.

## 8. Verification record and status

The proof of all \(m,n\) uses the displayed order estimates and
exact polynomial identities, not sampling. Fresh unsaved algebra
also checked the complete residue and finite part with arbitrary
first and second jets, the \(n=2\) correction, the concrete
specialization (27), and representative \(m=2,3\),
\(n=2,3,4\) with unrestricted lower terms in the specified input
polynomials. The generic slice and flow identities and both
quotient inverse orders were checked separately. No saved checker
was executed, imported, or compiled. No canonical source was edited.

This source is held for independent review only after its complete
author EOF review and final hash handoff. It does not certify
an unfinished neighboring source or replace separate acceptance
of earlier results.
