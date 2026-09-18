# Proper binary parameter fibers force a pole in the fourth velocity derivatives

In the actual nonlinear supplied-good-direction branch, the two
derivatives \(P_{4,p},P_{4,q}\) cannot both be regular at the
generic local ring of any proper parameter-zero component.
This remains true when the whole parameter fiber is nonreduced.

Consequently every base zero of p,q is a ramification point of
the map defined by that pair on the intrinsic plane.
The proof retains the nonreduced associated graded and uses
the characteristic-zero Jacobian socle theorem to prohibit
vanishing of all ambient parameter minors modulo the parameter
ideal. It does not exclude ramified proper fibers.

## 1. Actual setting and the additional condition to exclude

Use exactly the actual hypotheses of the
[reduced-component exclusion](binary-reduced-fiber-exclusion-pass78.md):
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,w]=A[s],\quad
E\in\operatorname{LND}(B),\quad Es=1,\quad E(P)=0,\\
T=\partial_w,\quad [E,[E,T]]=0,\quad Q=[T,E],\quad
0\ne Q|_A=hD,\\
S=\ker D=\ker(Q|_A)\simeq\mathbb C[u,v],\quad
S\subset A\text{ faithfully flat},\\
p,q\in S\text{ independent and coprime in }B,\quad
P_i=h_i(p,q)\ (i\le3).
\end{gathered}
\tag{1}
\]
The binary forms \(h_1,h_2,h_3\) are linearly independent
over \(\mathbb C\), homogeneous of the same degree \(e\ge2\).
Also \(P_4\in S\).
The original slice and good-direction calculations give
\[
I=(p,q)B\ne B,\qquad
\tau=(Tp,Tq)^t\in I^eB^2,\qquad J^3=0,
\quad J=\operatorname{Jac}_x P.
\tag{2}
\]

Let \(\mathfrak n\) be any minimal prime of I, put
\(L=B_{\mathfrak n}\), \(I_L=(p,q)L\), and
\(R_0=L/I_L\). Then L is a regular local ring of dimension
two and p,q are a parameter regular sequence.
The nonzero Artinian local ring R0 is not replaced by its
residue field or reduction.
The condition to be contradicted is
\[
P_{4,p},P_{4,q}\in L.
\tag{3}
\]
The two derivatives are the unique extended parameter
derivations on \(\operatorname{Frac}S/\mathbb C(p,q)\).
They may have poles in general.

## 2. An independence lemma for the three binary Jacobians

For \(1\le i<j\le3\) put
\(K_{ij}=\det\operatorname{Jac}_{\xi,\eta}(h_i,h_j)\).
Then
\[
K_{12},K_{13},K_{23}
\text{ are linearly independent over }\mathbb C.
\tag{4}
\]
To prove this, a nonzero linear relation would correspond to
a nonzero element of \(\bigwedge^2\mathbb C^3\).
Every such element is decomposable, say \(\alpha\wedge\beta\)
with independent rows \(\alpha,\beta\in\mathbb C^3\).
For example, after permuting the basis and dividing by a
nonzero coefficient of \(e_1\wedge e_2\), this follows by
expanding
\((e_1+a e_3)\wedge(e_2+b e_3)\).
The alleged relation would then say
\(\det\operatorname{Jac}(\alpha\mathcal H,\beta\mathcal H)=0\),
where \(\mathcal H=(h_1,h_2,h_3)^t\).

The two resulting forms are nonzero, independent, and
homogeneous of degree e. Euler's identities force their
ratio to have zero \(\xi\)- and \(\eta\)-derivatives when
their Jacobian determinant is zero. In characteristic zero
that ratio belongs to \(\mathbb C\), a contradiction.
The complete elementary ratio proof is given in Section 5
of the reduced-component note.

The independence in (4) persists over every nonzero
complex algebra, including R0 with all its nilpotents.
Indeed the finite coefficient matrix of these three
polynomials has a nonzero complex three-by-three minor.
That minor is a unit after any such scalar extension.
No algebraic closure or reducedness of the coefficient
algebra is needed here.

## 3. The nonreduced associated-graded calculation

Since p,q form a regular sequence, the canonical map gives
\[
\operatorname{gr}_{I_L}L=R_0[\xi,\eta],
\qquad
\xi=\operatorname{in}(p),\quad\eta=\operatorname{in}(q).
\tag{5}
\]
This is the regular-sequence associated graded, not the
maximal-ideal associated graded unless the parameter
quotient happens to be a field.[^graded]

Let V be the two-by-four ordinary Jacobian of p,q, and
let \(V_{\mathrm{tr}}\) be its first three columns.
The fourth column is \(\tau\).
Over \(\operatorname{Frac}B\), let U have rows
\((P_{i,p},P_{i,q})\), and set \(C=VU\).
As before \(J=UV\), U and V have rank two, and \(J^3=0\)
gives \(C^2=0\). Under (3) every entry is in L.
In particular \(\det C=0\) in the domain L.
The exact splitting is
\[
C=V_{\mathrm{tr}}\operatorname{Jac}_{p,q}\mathcal H
  +\tau(P_{4,p},P_{4,q}).
\tag{6}
\]
The two terms have ideal orders at least e-1 and e,
respectively. If \(\overline V_{\mathrm{tr}}\) denotes
the image of \(V_{\mathrm{tr}}\) over R0, the degree
\(2e-2\) part of \(\det C=0\) in (5) gives
\[
0=\det\bigl(\overline V_{\mathrm{tr}}
           \operatorname{Jac}_{\xi,\eta}\mathcal H\bigr)
 =\sum_{i<j}\overline M_{ij}K_{ij}
\quad\text{in }R_0[\xi,\eta].
\tag{7}
\]
Here \(M_{ij}\) are the two-by-two column minors of
\(V_{\mathrm{tr}}\), and the last equality is Cauchy--Binet.
The entries of \(\overline V_{\mathrm{tr}}\) are only
coefficients of the graded polynomial ring; they are not
differentiated along an invented coefficient-field section.
No rank of that matrix over R0 has been assumed.

By (4), all \(\overline M_{ij}\) in (7) are zero.
Every ambient minor involving column four also belongs
to \(I_L\), because that column is in \(I_L^eL^2\).
Thus
\[
\text{all six two-by-two minors of }V
\text{ belong to }I_L.
\tag{8}
\]
This is membership in the unreduced ideal, not just in
its radical. This strengthening is precisely what permits
the next step.

## 4. Some ambient minor survives on the whole local scheme

The following direct transverse construction contradicts
(8). The residue field \(F=\kappa(\mathfrak n)\) has
transcendence degree two over \(\mathbb C\). Choose two
of the four original coordinate residues which are a
maximal algebraically independent subset.
Call their actual coordinate representatives \(t_1,t_2\)
and the complementary two actual coordinates \(z_1,z_2\).
Then
\[
K=\mathbb C(t_1,t_2)\subset L,\qquad
[F:K]<\infty\text{ separable},\qquad
L=K[z_1,z_2]_{\mathfrak r}
\tag{9}
\]
for a maximal ideal \(\mathfrak r\) with residue F.
All nonzero polynomials in \(t_1,t_2\) avoid
\(\mathfrak n\), which supplies the displayed field
inclusion. Localizing B by those polynomials and then
at the induced prime gives the last equality.
Maximality follows from the finite algebraic residue field.

Thus L is an essentially smooth surface over K, and
\(R_0=L/(p,q)\) is a nonzero finite-dimensional local
complete-intersection K-algebra.
The relative two-by-two Jacobian is
\[
\Theta=p_{z_1}q_{z_2}-p_{z_2}q_{z_1}
\notin (p,q)L.
\tag{10}
\]
These are exactly the original coordinate derivatives
holding \(t_1,t_2\) fixed. Consequently \(\Theta\) is one
of the six ambient minors in (8), up to sign.

For clarity, (10) is the precise transverse Jacobian
lemma of
[primitive-fiber54, Section 2](primitive-fiber-nonvanishing-pass54.md).
Its proof does not identify F with K or presume a
coefficient field in a completion fixing K.
The conormal presentation makes the zeroth Fitting ideal
of \(\Omega_{R_0/K}\) equal to \((\overline\Theta)\).
If it were zero, extend K to an algebraic closure and
take a nonzero local factor of the resulting finite algebra.
The corresponding smooth two-variable local ring has
completion \(\overline K[[Z_1,Z_2]]\), and its Artinian
quotient is unchanged by completion. The characteristic-zero
Jacobian socle theorem makes its relative determinant
nonzero. Fitting ideals commute with scalar extension and
localization, contradicting the assumed zero ideal.
This proves (10), retaining every nilpotent direction.[^socle]

Equations (8) and (10) contradict each other. Condition
(3) is impossible.

## 5. Stronger local and base conclusions

The proved statement is
\[
\boxed{\,
(P_{4,p},P_{4,q})\notin L^2
\quad\text{for every }L=B_{\mathfrak n}
\text{ at a minimal proper parameter-zero prime.}\ }
\tag{11}
\]
This means at least one derivative has a pole in each
such local ring. It does not assert that both have poles.

Let \(\mathfrak m\subset S\) be any maximal ideal
containing p,q. Faithful flatness ensures a minimal
parameter-zero prime \(\mathfrak n\) of B over it.
If \(\Delta=\operatorname{Jac}_{u,v}(p,q)\) were a unit
at \(\mathfrak m\), Cramer's rule would put both fourth
derivatives in \(S_{\mathfrak m}\subset B_{\mathfrak n}\),
contrary to (11). Hence
\[
\Delta\in\sqrt{(p,q)S},\qquad
S_{\mathfrak m}/(p,q)S_{\mathfrak m}
\text{ is nonreduced at every proper zero }\mathfrak m.
\tag{12}
\]
The second conclusion follows from the equivalent conditions
in the ramification-socle note. It is genuinely stronger than
the earlier exclusion of generically reduced components
upstairs, which by itself did not imply base ramification.
The earlier proof remains valid and is left unchanged.

In particular \(P_4\in\mathbb C[p,q]\) is impossible in
the proper-parameter branch. More generally, any additional
argument making both its parameter derivatives regular
at a base zero would exclude that zero.
The present proof does not supply such regularity.
The genuine pole control in the ramification-socle note
explains why the weaker intrinsic plane data do not supply it.

No upper bound on the replica content h, primitive
fixed-point-freeness, or cancellation conclusion follows.
No numerical method, regression, historical novelty, human
expert review or formal verification is claimed.
Frozen passes through77 and shared metadata remain unchanged.

[^graded]: The Stacks Project, [Definition 10.69.1 and its canonical map, 061M](https://stacks.math.columbia.edu/tag/061M), and [Lemma 10.69.2, 00LN](https://stacks.math.columbia.edu/tag/00LN). The selected definition and complete regular-sequence-to-quasi-regular proof were freshly read. This result explicitly allows a nonreduced coefficient ring L/I.

[^socle]: David Eisenbud and Bernd Ulrich, [*Duality and socle generators for residual intersections*](https://arxiv.org/pdf/1309.2050v4), Appendix Section 8 and Theorem 8.1, printed pages 40--41. The complete selected proof was read during the present pass78 ramification audit; the scalar-extension/Fitting application from the saved pass54 proof was freshly reread. This does not claim a new read of every historical dependency cited by that source.
