# Complete two-gate classification for the two-root double cover

Status: working differential theorem, pending independent reconstruction.
For \(q^2=t(1-t)\), the two nondegenerate necessary square-completion
gates have exactly three coefficient families:
\[
f=cq,\qquad f=\frac{cq}{t},\qquad f=\frac{cq}{t-1},
\qquad c\in\mathbb C^* .
\tag{1}
\]
This classifies necessary differential equations over every allowed
finite algebraic coefficient field. It does not establish actual
normalization, realization, recognition or exclusion of these families.

## 1. Exact field, equations and nonzero gates

Let \(K/\mathbb C(t)\) be finite, contain \(q\) with \(q^2=t(1-t)\),
and carry the unique extension of \(d/dt\). Its constants are
\(\mathbb C\). Let \(f\in K\). Primes mean this derivative. Put
\[
\begin{gathered}
d=q'''/6=\frac{1-2t}{16q^5},\qquad
D_0=d'f/4+df',\qquad f f''D_0\ne0,\\
R=1/f,\qquad
\Delta=-\frac{f''}{2f^3},\qquad
\nu=\frac{(f'')^2}{8f^3D_0},\qquad
p_2=-\frac{\Delta}{R\nu},\qquad
p=\frac{2R'}R-\frac{\nu'}{\nu}.
\end{gathered}
\tag{2}
\]
The two equations are the same general-\(q\) square gates used in
[classification195](weight-four-square-root-two-gate-classification-pass195-working.md):
\[
\begin{gathered}
\mathscr E=20D_0f'''-3d(f'')^2-12f''D_0'=0,\\
L_3=\frac{R\nu''/4-R'\nu'/2-\nu R''/2
                         -R\nu p^2/2-\nu^2p_2}{3Rp_2},\\
J_3=-RL_3'+R'L_3-\nu\nu'/2-p(3RL_3+\nu^2)=0 .
\end{gathered}
\tag{3}
\]
All denominators in (2)--(3) are nonzero field elements. In the actual
two-root frame, these are necessary equations after
[reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md).
The present theorem is a differential statement, independent of
any inference that a formal solution is an actual frame.

## 2. Scaled logarithmic jets

Introduce auxiliary symbols
\[
z=2t-1,\qquad
u=2t(t-1)\frac{f'}f,\qquad
v=4t^2(t-1)^2\frac{f''}f,\qquad
G=-4uz+4z^2+1 .
\tag{4}
\]
They are not the projected coordinates or original slice from previous
notes. The element \(z\) is transcendental over \(\mathbb C\).
The nonzero gates imply \(vG\ne0\), since
\[
\frac{d'}d=-\frac{16t^2-16t+5}{2t(t-1)(2t-1)},\qquad
D_0=-\frac{dfG}{2z(z^2-1)} .
\tag{5}
\]
Write \(\partial_z=\frac12\partial_t\).

For a transparent reconstruction, set \(a=d'/d\). Expanding the first
gate in (3) gives
\[
f'''=\frac{3f''\{5f''+5af'+(a'+a^2)f\}}
                 {5(af+4f')}.
\tag{6}
\]
This uses only the already nonzero denominator \(D_0\).
Differentiating (4) and substituting (6) then yields
\[
u_z=\frac{-u^2+2uz+v}{z^2-1},\qquad
v_z=\frac{v(4u^2z-8uz^2+2u-3vz+4z^3-5z)}
            {(z^2-1)G}.
\tag{7}
\]
These are identities for elements of \(K\); no assertion that
\(K=\mathbb C(t,q)\) has been made.

Define
\[
\begin{aligned}
L&=-u+vz+2z,\\
Q&=z^2v^2+(uz+2z^2-1)v-(4z^2-2)u^2\\
 &\hspace{14mm} +(8z^3-3z)u-4z^4+3z^2-1 .
\end{aligned}
\tag{8}
\]
Reduction of the second expression (3) using (6), or equivalently
using the two derivation rules (7), gives the exact factorization
\[
J_3=-\frac{56v^3LQ}{f^4(z^2-1)^2G^5}.
\tag{9}
\]
For checking constants, before replacing \(d^2\), its prefactor is
\(224v^3z^2/[f^4d^2(z^2-1)^7G^5]\).
The identity \(d^2=-4z^2/(z^2-1)^5\) gives (9).
This supplies a short independent way to check the sign and scale.

Since \(K\) is a field and all prefactors are nonzero, at least one
of \(L,Q\) must vanish.

## 3. The linear factor

In the original variables,
\[
\frac{2}{f}
\left\{(2t-1)f+t(1-t)f'
        +2t^2(t-1)^2(2t-1)f''\right\}=L .
\tag{10}
\]
The [complete linear-factor argument201](weight-four-two-root-linear-factor-rigidity-pass201-working.md)
proves that its only nonzero algebraic solutions in \(K\) are \(f=cq\).

Briefly, write \(f=qh\), \(s=1-2t\), and \(p_0=t(1-t)\).
The operator in braces is \(-2p_0^2(qs h')'\).
Thus \(h'=C/(qs)\) for a complex constant \(C\).
The differential \(dt/(qs)\) has residues \(-1,+1\) at
\((t,q)=(1/2,1/2),(1/2,-1/2)\) on the rational conic.
It cannot become an exact differential in a finite extension.
For example, taking normalized field trace of a putative primitive
back to \(\mathbb C(t,q)\) would give a rational primitive with
nonzero residue, which is impossible.
Therefore \(C=0\) and \(h=c\) is complex.

## 4. The quadratic factor and its differentiated consequence

Assume \(Q=0\). To give explicit finite polynomial identities behind
the elimination, define a derivation \(\mathcal D\) on
\(\mathbb C(z,u,v)\) by (7), with \(\mathcal D z=1\).
Set
\[
\begin{gathered}
D_1=z^2-1,\qquad
V_1=v(4u^2z-8uz^2+2u-3vz+4z^3-5z),\\
N=D_1G Q_z+G(-u^2+2uz+v)Q_u+V_1Q_v .
\end{gathered}
\tag{11}
\]
The partial derivatives in (11) are formal polynomial partials.
Thus \(N=D_1G\,\mathcal DQ\) is a polynomial, and an actual
solution of \(Q=0\) also has \(N=0\).

The resultant with respect to \(v\) factors as
\[
\operatorname{Res}_v(Q,N)
=4z^3(z-u)(u-1)(u+1)(z^2-1)G\,H ,
\tag{12}
\]
where
\[
H=(64z^4-37z^2)u^2+
       (-128z^5+72z^3+2z)u+
       64z^6-32z^4-7z^2+2 .
\tag{13}
\]
Equations (11)--(13) are polynomial identities, obtainable by
expanding the Sylvester determinant for the displayed polynomials.
No selection of numerical values is used. Because the resultant
lies in the polynomial ideal generated by \(Q,N\), their common
vanishing implies the vanishing of its displayed value in \(K\).
The factors \(z(z^2-1)G\) are nonzero. Hence
\[
u=z,\qquad u=1,\qquad u=-1,\qquad\text{or}\qquad H=0 .
\tag{14}
\]

## 5. A second exact resultant excludes the residual factor

Suppose \(H=0\). Its discriminant as a polynomial in \(u\) is
\[
\operatorname{disc}_u(H)
=-12z^2(z^2-1)(8z^2-5)^2\ne0 .
\tag{15}
\]
Thus \(H_u\ne0\) at this field root: otherwise \(H,H_u\) would
have a common root, contradicting the nonzero discriminant.
Differentiating \(H(z,u)=0\) in \(K\) gives
\(u_z=-H_z/H_u\). By (7) this forces
\[
v=\frac{V_H}{H_u},\qquad
V_H=(u^2-2uz)H_u-(z^2-1)H_z .
\tag{16}
\]
Write \(Q=z^2v^2+B_Qv+C_Q\), where the two coefficient
polynomials \(B_Q,C_Q\) are explicitly given in (8). Put
\[
M=z^2V_H^2+B_QV_HH_u+C_QH_u^2 .
\tag{17}
\]
This is a polynomial in \(z,u\) and equals \(H_u^2Q(z,u,V_H/H_u)\).
Thus \(H=M=0\) at the putative solution.

A second direct Sylvester-determinant identity is
\[
\begin{aligned}
\operatorname{Res}_u(H,M)
={}&1296z^{12}(z^2-1)^5(4z^2-1)^4\\
 &\quad\cdot(8z^2-5)^4(64z^2-37)^2(121z^2-94).
\end{aligned}
\tag{18}
\]
Every factor is a nonzero polynomial in the transcendental \(z\).
Hence (18) is a nonzero field element, which contradicts
\(H=M=0\). This excludes the last alternative in (14).
In particular no implicit rationality or choice of algebraic
root of \(H\) was needed.

## 6. Integration and verification of the three candidates

The remaining three values of \(u\) determine \(f\) completely:
\[
\begin{array}{c|c|c|c}
u&f&v&G\\ \hline
z&cq&-1&1\\
1&cq/t&1-2z&(2z-1)^2\\
-1&cq/(t-1)&1+2z&(2z+1)^2
\end{array}
\tag{19}
\]
For instance each displayed \(f_0\) has
\(2t(t-1)f_0'/f_0=u\). Thus \((f/f_0)'=0\), which gives
\(f=c f_0\) with \(c\in\mathbb C^*\), inside the exact field.

Conversely, the \(u,v\) pairs in (19) satisfy both rules (7).
They also satisfy \(Q=0\) in (8), including the first row.
Their \(v,G\) entries are nonzero field elements, as are their
\(f\), so all gates (2) hold.
Equation (6), equivalently the second rule (7) after the first
logarithmic identity, gives \(\mathscr E=0\); equation (9)
gives \(J_3=0\).
This proves both necessity and sufficiency of (1).

## Scope and verification obligations

The linear-factor proof includes the finite-extension obstruction
to an algebraic primitive. The quadratic factor is eliminated by the
two exact resultant identities (12),(18), with every possible
denominator or repeated-root gate handled explicitly.
The factorization (9), differential rules, and both resultants have
been computed with exact unsaved algebra, not sampled numerically.
Independent reconstruction and a standalone finite checker are still
needed before freezing this note.

In an actual two-root frame the new theorem leaves three necessary
coefficient families. It does not solve their lower potentials,
scalar Jacobians, exact projected field return, original-coordinate
problem, or establish that any family can occur.
The earlier zero-R recognition is separate.
The unrestricted cancellation goal remains active and unsolved.
No earlier artifact was edited; there is no human expert review,
proof-assistant certification, novelty clearance or external contact.

