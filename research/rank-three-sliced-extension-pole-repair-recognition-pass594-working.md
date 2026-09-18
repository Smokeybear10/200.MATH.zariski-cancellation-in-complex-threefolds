# Polynomial repair of a rank-three sliced-extension lift

## 1. Exact recognition result

For the concrete rank-three extension defined below, the supplied slice
\(u\) is an actual coordinate of \(B=\mathbb C[x,y,z,t]\), and
\(\ker E\cong\mathbb C^{[3]}\). The proof corrects a specific
localized automorphism by a second localized automorphism. Their
composition and its inverse both preserve the entire polynomial ring.

The earlier bounded audit593 correctly found that the first map alone
has a pole and did not establish recognition. That pole calculation
remains valid. The correction here supplies the missing completion for
this example, superseding that audit's unresolved endpoint. Neither
source is a counterexample to cancellation. No general recognition
theorem or novelty claim is asserted.

All localizations below serve the proof of a whole-ring automorphism.
No map on a smaller local-slice subalgebra is promoted to an ambient
automorphism without checking every ambient generator and the inverse.

## 2. Base data, full slice and natural localized lift

Let
\[
 R=\mathbb C[x,y,z],\quad B=R[t],\quad
 f=xz-y^2,\quad r=x^5+yf^2,
 \quad g=\frac{f^5+r^2}{x}
       =zf^4+2x^4yf^2+x^9.
\tag{1}
\]
In particular \(g\) is polynomial. Define
\[
 H=\operatorname{Jac}(f,g,\mathord\cdot),\qquad
 E=H+(1-fgr)\partial_t,
\tag{2}
\]
initially extending \(H\) by \(H(t)=0\).
The retained primary input is that \(H\) is an irreducible rank-three
LND, with kernel \(\mathbb C[f,g]\) and minimal local slice \(r\).
It is the member \(E(2,2,t_1^4)\) in
[Dasgupta--Gaifullin, Section 5, Theorem 5.7](https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=10094&wshow=paper).
The concrete identities used in this proof are
\[
 Hf=Hg=0,\qquad Hr=-f^2g,\qquad Hx=-2f^2r,
 \qquad xg=f^5+r^2.
\tag{3}
\]
They also follow by direct differentiation of the Jacobian in (2).
The extension \(E\) is locally nilpotent: it agrees with \(H\) on
\(R\), and its successive derivatives of \(t\) after the first are
successive \(H\)-derivatives of the polynomial \(1-fgr\).

Set
\[
 v=ft-r^2/2,\qquad q=-fgv-r,
 \qquad u=t+grv+\frac{fg^2}{2}v^2.
\tag{4}
\]
These are whole polynomials, and
\[
 Ev=f,\qquad Eq=0,\qquad fu=v+q^2/2,
 \qquad Eu=1.
\tag{5}
\]
The first two equations follow from (3). Expanding \(q^2\) gives
the third. Differentiating it and cancelling the nonzero \(f\) in
the domain gives the fourth without inverting \(f\).

On \(B_f=B[f^{-1}]\), introduce
\[
 L=H/f-gr\partial_t.
\tag{6}
\]
Since \(Hf=0\), \(H/f\) is an LND of \(R_f\), and its extension
\(L\) is an LND of \(B_f\). In particular,
\[
 Lv=0,\quad Lt=-gr,\quad L^2t=fg^2,\quad L^3t=0,
 \quad Lr=-fg,\quad Lx=-2fr,\quad L^2x=2f^2g.
\tag{7}
\]
Thus the invariant replica \(-vL\) is locally nilpotent on this
localized ring. Its genuine exponential
\[
 \Phi=\exp(-vL)\in\operatorname{Aut}_{\mathbb C}(B_f)
\tag{8}
\]
has inverse \(\exp(vL)\), fixes \(f,g\), and satisfies
\[
 \Phi(t)=u,\qquad r_1:=\Phi(r)=r+fgv,
 \qquad x_1:=\Phi(x)=x+2frv+f^2gv^2.
\tag{9}
\]
For the remaining base coordinates, these are exact identities in
\(B_f\):
\[
 \Phi(y)=\frac{r_1-x_1^5}{f^2},\qquad
 x_1\Phi(z)=f+\Phi(y)^2.
\tag{10}
\]
The first map alone is not polynomial on \(B\). Indeed,
\[
 r_1-x_1^5=f^2y+f(g-10x^4r)v\pmod{f^2B},
\tag{11}
\]
and modulo \(f\), \(r=x^5\), \(g=x^9\), \(v=-x^{10}/2\).
Therefore
\[
 \Phi(y)\in f^{-1}B\setminus B,
 \qquad f\Phi(y)\equiv\frac92x^{19}\pmod f.
\tag{12}
\]
The nonzero residue in (12), not an assumption of regularity, determines
the correction below.

## 3. Correction and polynomiality of every generator

Let
\[
 \delta_0=x\partial_y+2y\partial_z,
 \qquad c=\frac92,
 \qquad \Gamma=\exp\left(-\frac{cx^{18}}f\delta_0\right).
\tag{13}
\]
Here \(\delta_0(x)=\delta_0(t)=\delta_0(f)=0\), and
\(\delta_0\) is triangular and locally nilpotent. Its coefficient
\(-cx^{18}/f\) is invariant. Hence \(\Gamma\) is an automorphism
of \(B_f\), fixing \(x,t,f\), with full coordinate formulas
\[
 \Gamma(y)=y-\frac{cx^{19}}f,
 \qquad
 \Gamma(z)=z-\frac{2cx^{18}y}f+rac{c^2x^{37}}{f^2}.
\tag{14}
\]
The inverse exponential changes the sign of its coefficient. Direct
substitution also verifies \(x\Gamma(z)-\Gamma(y)^2=f\).

Use algebra-map composition, so that
\((\Phi\circ\Gamma)(p)=\Phi(\Gamma(p))\), and put
\[
 \Psi=\Phi\circ\Gamma\in\operatorname{Aut}(B_f).
\tag{15}
\]
It fixes \(f\), and
\[
 \Psi(x)=x_1,\quad \Psi(t)=u,\quad
 \Psi(y)=\Phi(y)-\frac{cx_1^{19}}f.
\tag{16}
\]
The first two images are in \(B\). By (9), \(x_1\equiv x\pmod f\).
Consequently (12) shows that the two residues in the last expression
cancel exactly. Since \(\Phi(y)\) has at most a simple \(f\)-pole,
this proves
\[
 \Psi(y)\in B.
\tag{17}
\]

Polynomiality of \(\Psi(z)\) follows without expanding a large
exponential. Preservation of \(f\) gives the exact relation
\[
 x_1\Psi(z)=f+\Psi(y)^2\in B.
\tag{18}
\]
The polynomial \(f=xz-y^2\) is prime in the UFD \(B\), and
\(f\nmid x_1\), because \(x_1\equiv x\not\equiv0\pmod f\).
But \(\Psi(z)\in B_f\), so any denominator it has is a power of
\(f\). Equation (18) then forces that denominator to cancel. Thus
\(\Psi(z)\in B\). All four images are now polynomial, and
\(\Psi\) restricts to an injective endomorphism of \(B\).
Surjectivity is not inferred from these facts or from a Jacobian
condition. It is proved next.

## 4. Full induced map modulo \(f\)

We compute enough exact \(f\)-adic coefficients to identify the
quotient map, including its inverse. This is legitimate in the chart
\[
 B_x=\mathbb C[x,x^{-1},y,t,f],\qquad z=(f+y^2)/x.
\tag{19}
\]
Reduction modulo \(f\) embeds \(B/(f)\) in its \(x\)-localization,
since \(B/(f)\) is a domain and \(x\ne0\) there. Consequently an
identity checked in this chart between elements of \(B/(f)\) is
an identity on the whole quotient; no fiber is removed from the result.

From the entire formulas (1) and (4), in this chart,
\[
 \begin{aligned}
 r&=x^5+f^2y,\\
 g&=x^9+2x^4yf^2+O(f^4),\\
 v&=-x^{10}/2+ft-x^5yf^2+O(f^4),\\
 x_1&=x-x^{15}f+(2x^5t+x^{29}/4)f^2+O(f^3),\\
 r_1&=x^5-x^{19}f/2+(y+x^9t)f^2+O(f^3).
 \end{aligned}
\tag{20}
\]
Here \(O(f^j)\) denotes membership in the ideal \(f^jB_x\), not
a convergence assertion or omission of unexamined lower coefficients.
Ordinary polynomial multiplication gives
\[
 \begin{aligned}
 x_1^5&=x^5-5x^{19}f+(10x^9t+45x^{33}/4)f^2+O(f^3),\\
 x_1^{19}&=x^{19}-19x^{33}f+O(f^2),\\
 r_1-x_1^5-cfx_1^{19}
   &=f^2\left(y-9x^9t+\frac{297}{4}x^{33}\right)+O(f^3).
 \end{aligned}
\tag{21}
\]
Together with (16), these yield
\[
 \overline{\Psi}(x)=x,\qquad
 \overline{\Psi}(t)=t-x^{24}/2,\qquad
 \overline{\Psi}(y)=y-9x^9t+\frac{297}{4}x^{33}
\tag{22}
\]
in \(B/(f)\). The \(t\)-formula follows directly by reducing the
whole polynomial \(u\) in (4).

In fact this quotient map has an explicit whole polynomial lift. Set
\[
 C=-9x^8t+\frac{297}{4}x^{32}
\tag{23}
\]
and define the polynomial map
\[
 \beta:(x,y,z,t)\longmapsto
 \left(x,\ y+xC,\ z+2Cy+xC^2,\ t-x^{24}/2\right).
\tag{24}
\]
Its full inverse has the same form with
\[
 G=9x^8t-\frac{279}{4}x^{32},
 \qquad
 \beta^{-1}:(x,y,z,t)\longmapsto
 \left(x,\ y+xG,\ z+2Gy+xG^2,\ t+x^{24}/2\right).
\tag{25}
\]
Both substitution orders follow from
\(G(x,t-x^{24}/2)=-C(x,t)\) and
\(C(x,t+x^{24}/2)=-G(x,t)\).
Moreover \(\beta(f)=f\). Thus \(\beta\) is a genuine automorphism
of \(B\) preserving \((f)\).

The reductions of \(\Psi\) and \(\beta\) agree on \(x,y,t\) by
(22). They also agree on \(z\): apply their preserved relation
\(xz=y^2\) in \(B/(f)\) and cancel its nonzero \(x\). Hence
\[
 \overline\Psi=\overline\beta
 \quad\text{on }B/(f),
\tag{26}
\]
which proves, in particular, injectivity of \(\overline\Psi\) on
the entire quotient, not just on a generic fiber.

## 5. Denominator clearance for the full inverse

We use the following elementary lemma.

**Lemma.** Let \(T\) be a domain and \(0\ne a\in T\). Suppose
\(\sigma\in\operatorname{Aut}(T_a)\) fixes \(a\), sends \(T\)
into \(T\), and induces an injective map on \(T/aT\). Then
\(\sigma(T)=T\).

**Proof.** For \(b\in T\), write
\(\sigma^{-1}(b)=c/a^n\), with \(c\in T\) and \(n\ge0\)
minimal. If \(n>0\), then \(c\notin aT\). Applying \(\sigma\)
gives \(\sigma(c)=a^nb\in aT\), contradicting injectivity of its
reduction modulo \(a\). Thus \(n=0\) and every inverse image lies
in \(T\). This proves the assertion. \(\square\)

Apply the lemma with \(T=B\), \(a=f\), and \(\sigma=\Psi\).
Sections 3--4 verify all its hypotheses. Thus
\[
 \Psi\in\operatorname{Aut}_{\mathbb C}(B),\qquad \Psi(t)=u.
\tag{27}
\]
This proves polynomiality of the entire inverse, not only birational
invertibility. A finite inverse certificate before denominator clearance
is already supplied by the two genuine localized exponentials:
\[
 \Psi^{-1}=\Gamma^{-1}\circ\Phi^{-1}
   =\exp\left(\frac{cx^{18}}f\delta_0\right)\circ\exp(vL)
   \quad\text{on }B_f.
\tag{28}
\]
The lemma proves that the images of every original generator under
(28) belong to \(B\). The two composition identities therefore hold
on the whole polynomial ring, including \(f=0\).

## 6. Kernel recognition and exact scope

Since \(\Psi\) is an ambient automorphism and \(\Psi(t)=u\),
\[
 B/(u)\cong B/(t)\cong\mathbb C^{[3]}.
\tag{29}
\]
Independently, (5) and the slice theorem give
\(B=(\ker E)[u]\) and \(\ker E\cong B/(u)\). Combining them
proves the claimed recognition
\[
 \ker E\cong\mathbb C^{[3]}.
\tag{30}
\]
The argument does not assert that \(\Psi\) itself conjugates
\(\partial_t\) to the original \(E\); that stronger identity is
unnecessary. The actual coordinate slice and the quotient suffice.

This result concerns (1)--(2), with its specified local-slice data and
correction. It does not establish that every rank-three sliced extension
can be repaired, that every positive Euler first-shift frame is recognized,
or that arbitrary complex-threefold cancellation is solved. The initial
failure of \(\Phi\) in audit593 remains a correct calculation; only
the absence of a supplied completion for this concrete example has changed.

Fresh unsaved exact algebra checks the complete factor reductions in
\(B_x/(f^3)\), the coefficient \(297/4\), both full inverse orders
in (24)--(25), and preservation of \(f\). The ideal and denominator
arguments are proofs, not consequences of numerical tests. An attempted
unnecessary full expansion of \(x_1^{19}\) was stopped for size and
replaced by exact quotient-ring arithmetic; it is not counted as a
completed verification. No saved checker was run, imported or compiled.
No earlier or canonical file was edited, and no novelty claim is made.
Final HELD status follows a complete self-review through EOF and a hash.
