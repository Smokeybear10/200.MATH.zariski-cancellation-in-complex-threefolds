# The binary Euler numerator at a ramified parameter fiber

At a proper zero of the binary parameters, the cleared Euler
numerator is a nonzero socle generator on the whole local
parameter fiber. The Euler expression itself need not be regular.
If it is regular, however, its residue is forced to be a nonzero
constant multiple of the fourth velocity.

This distinguishes the exact scheme-theoretic nonvanishing from
an unjustified cancellation of the ramification determinant.
It neither proves that the parameter map is étale everywhere
over zero nor bounds the intrinsic content from above.

## 1. Actual base data and the local complete intersection

Retain the actual nice sliced action and independent common
invariants of the
[binary conormal reduction](binary-conormal-obstruction-pass77.md).
Write \(S=\ker D=\ker\delta\simeq\mathbb C[u,v]\),
\(\delta=Q|_A=hD\), \(B=A[s]\), and assume the retained
faithful flatness of \(S\subset A\).
The parameters p,q are algebraically independent, coprime
actual elements of S. The transverse velocities are homogeneous
binary forms \(P_i=h_i(p,q)\) of degree e, for \(i\le3\).
Also \(P_4\in S\), since both E and Q kill every velocity.

Fix a maximal ideal \(\mathfrak m\) of S containing p,q.
Set \(R=S_{\mathfrak m}\), \(I=(p,q)R\), and write
\[
\Delta=p_uq_v-p_vq_u\ne0,\qquad
R/I\text{ is an Artinian local complete intersection}.
\tag{1}
\]
Indeed, a common height-one prime divisor of p,q in S would
give a common divisor in B. It remains a nonunit there by
faithful flatness. Thus no such prime exists. Every proper
zero of the pair on the plane is isolated, and in R the
two elements form a regular sequence with radical
\(\mathfrak mR\). Algebraic independence in characteristic zero
makes \(\Delta\ne0\).

The original slice implies \(P_4\in R^*\). Otherwise all four
velocities would belong to \(\mathfrak mB\), contradicting
the slice identity and faithful flatness.
No global finiteness of the map defined by p,q is needed.

## 2. Rational derivatives and the cleared numerator

The field \(\operatorname{Frac}S\) is a finite separable extension
of \(\mathbb C(p,q)\). Its unique extensions of the two
parameter derivations are explicitly
\[
\partial_p=\frac{q_v\partial_u-q_u\partial_v}{\Delta},
\qquad
\partial_q=\frac{-p_v\partial_u+p_u\partial_v}{\Delta}.
\tag{2}
\]
These are derivations of the field. They are not asserted to
preserve R. Let \(\mathcal E=p\partial_p+q\partial_q\) and put
\[
\begin{aligned}
\gamma&=eP_4-\mathcal E(P_4)=\Gamma/\Delta,\\
\Gamma&=eP_4\Delta
 -p(P_{4,u}q_v-P_{4,v}q_u)
 -q(p_uP_{4,v}-p_vP_{4,u})\in R.
\end{aligned}
\tag{3}
\]
In particular \(\Gamma\equiv eP_4\Delta\pmod I\).

The characteristic-zero Jacobian socle theorem gives
\[
\begin{gathered}
0\ne\overline\Delta,\qquad
\operatorname{Soc}(R/I)=(\overline\Delta)
                       =(\overline\Gamma),\\
(I:\Delta)=(I:\Gamma)=\mathfrak mR.
\end{gathered}
\tag{4}
\]
Here the bar means the class on the whole Artinian scheme,
not on its reduction. The socle theorem applies after completing
the regular local ring to \(\mathbb C[[u-u_0,v-v_0]]\);
the Artinian quotient and its displayed Jacobian do not change.
The residue characteristic is zero, and e and \(P_4\) are units.
The annihilator of a nonzero socle generator in an Artinian
local ring is exactly its maximal ideal.[^socle]

One useful consequence does not require the whole parameter
map to be étale. For any \(f\in R\), the numerator
\(\Delta\mathcal E(f)\) belongs to I by (2). Consequently
\[
\mathcal E(f)\in R\ \Longrightarrow\
\mathcal E(f)\in\mathfrak mR;\qquad
\gamma\in R\ \Longrightarrow\
\gamma\equiv eP_4\pmod{\mathfrak mR},\quad \gamma\in R^*.
\tag{5}
\]
The first implication is precisely the colon identity in (4).
For the second, use \(f=P_4\).
Thus regularity would suffice for the needed unit conclusion.
Nonvanishing of the cleared numerator alone does not supply
that regularity.

## 3. Exact use in the two-by-two velocity factorization

This paragraph records identities, not an additional regularity
assumption. Over \(\operatorname{Frac}B\), let U be the
four-by-two matrix with rows \((P_{i,p},P_{i,q})\), let
V be the two-by-four ordinary Jacobian of p,q, and set
\(C=VU\), \(r=(p,q)^t\), \(\tau=(Tp,Tq)^t\).
Then \(J=UV\). Both U and V have rank two: the transverse
binary outputs have transcendence degree two, and p,q are
independent.

The retained nice-slice rank theorem gives \(J^3=0\), while
the supplied good partial gives \(J^2e_4=0\).
Thus \(C^2=0\) and \(C\tau=0\), using the injectivity of U
and surjectivity of V over the field. Euler's identity for
the three transverse rows gives
\(Ur=eP-\gamma e_4\), so \(Cr=-\gamma\tau\), since \(VP=0\).
After clearing the single displayed ramification denominator,
\(\widetilde C=\Delta C\) has entries in the localization
of B by \(S\setminus\mathfrak m\), and
\[
\widetilde C^2=0,\qquad
\widetilde C\tau=0,\qquad
\widetilde C r=-\Gamma\tau.
\tag{6}
\]
The fourth row of \(\Delta U\) is regular by (2), as are
all its other rows. Equation (6) is valid without dividing
by the socle class \(\overline\Delta\) on the closed fiber.
That class is usually a zero divisor.
The earlier rank and adjoint identities used here are proved
in [the nice-slice rank theorem](nice-slice-adjoint-rank-pass74.md).

## 4. What a reduced component would imply before any rank argument

At the selected base point the following are equivalent:
\[
\Delta\in R^*
\quad\Longleftrightarrow\quad I=\mathfrak mR
\quad\Longleftrightarrow\quad R/I\text{ is reduced}.
\tag{7}
\]
The first equivalence is the independence of the two linear
parameter classes in \(\mathfrak mR/(\mathfrak mR)^2\),
followed by Nakayama's lemma. A reduced Artinian local
complex algebra is its residue field, proving the other.
The first condition is also the Jacobian criterion for the
map of smooth planes to be étale at this point.

There is a useful descent gate. Let \(\mathfrak n\) be a
minimal prime of \((p,q)B\) contracting to \(\mathfrak m\).
The local map \(R\to B_{\mathfrak n}\) is flat and local,
hence faithfully flat. If
\(B_{\mathfrak n}/(p,q)B_{\mathfrak n}\) is reduced, its
faithfully flat inclusion of R/I forces R/I to be reduced.
Then (7) makes \(\Delta\) a unit. In particular the rational
derivatives of \(P_4\) become regular at this base point.

This implication uses the whole local scheme of a component.
It does not infer reducedness from a reduced support, nor
assume that every quotient fiber is generically reduced.
Further original-action initial-form arguments must retain
that distinction.

## 5. A genuine pole under the weaker plane data

Take the actual polynomial plane \(S_0=\mathbb C[u,v]\),
the origin, and
\[
p=u,\qquad q=v^2+uv,\qquad P_4=1+v,\qquad
\Delta=u+2v,\qquad
\gamma=e(1+v)-\frac{v^2}{u+2v}.
\tag{8}
\]
The pair is independent and coprime. In fact the parameter
map is finite: v satisfies \(v^2+pv-q=0\), and S0 is free
of rank two over \(\mathbb C[p,q]\).
Its local zero fiber is \(\mathbb C[v]/(v^2)\).
The class of \(P_4\) is a unit there, but \(\gamma\) has
a genuine pole along the prime \(u+2v\), because that prime
does not divide \(v^2\). The exact numerator satisfies
\[
\Gamma=e(1+v)(u+2v)-v^2,\qquad
\overline\Gamma=2e\,\overline v\ne0
\quad\text{in }\mathbb C[v]/(v^2).
\tag{9}
\]
Thus even a finite flat parameter map does not remove this pole.

For the separate intrinsic content comparison one may take
\(A_0=S_0[t]\), \(D_0=\partial_t\), and
\(\delta_N=p^N D_0\) for arbitrary N.
This has smooth factorial total space, a faithfully flat plane
quotient, a primitive field with a slice, and arbitrarily high
content in \((p,q)^N\). These weaker data give no upper content
bound. They are not asserted to realize the required original
nice four-coordinate action, its velocity forms, its omission
properties, or its derived-good-partial identity.

## 6. Scope

The completed local conclusions are the nonzero socle numerator,
the exact colon identities, and the conditional regular-to-unit
implication. The reduced-component descent in Section 4 supplies
an étale gate when its scheme hypothesis is actually available.
No regularity of \(\gamma\), étaleness of the actual proper
parameter branch, primitive freeness, or cancellation theorem
is concluded here.

No numerical method, regression, historical novelty, human expert
review or formal verification is claimed. Frozen passes through77
and shared metadata are unchanged.

[^socle]: David Eisenbud and Bernd Ulrich, [*Duality and socle generators for residual intersections*](https://arxiv.org/pdf/1309.2050v4), Appendix Section 8, parts 1--5 and Theorem 8.1, printed pages 40--41. The complete selected trace/different proof was freshly read for this note. Its complete-intersection specialization identifies the Jacobian class with the socle; the local application and colon consequences are given above. This is not a fresh review of the paper's other residual-intersection theorems or all historical inputs to the different calculation.
