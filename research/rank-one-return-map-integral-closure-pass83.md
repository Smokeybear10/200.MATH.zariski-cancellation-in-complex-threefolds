# The return involution puts acceleration in the integral closure

For an actual sliced polynomial action on complex four-space with three
nice coordinates and one quadratic-time coordinate, the acceleration is
integral over the ideal of the three good speeds. Briancon--Skoda then
gives its third power in that ideal. Combined with the separate Jacobian
socle criterion, this excludes isolated good-speed zeros.

This does not prove first- or second-power membership, construct a nice
coordinate frame, or recognize the original kernel. The return map is a
rational involution, not a claimed polynomial automorphism.

## 1. Actual action and its full speed ideal

Work in the original polynomial coordinates
\[
B=\mathbb C[x_1,x_2,x_3,z],\qquad E\in\operatorname{LND}(B),
\qquad E(s)=1,\qquad E^2x_i=0,\quad E^2z=q,\quad E(q)=0.
\tag{1}
\]
Put a_i=E(x_i), b=E(z), R=\mathbb C[x_1,x_2,x_3], and
I=(a_1,a_2,a_3)B. If I=B, the conclusions are immediate. Assume I is
proper, and use the exact, unreduced quotient results of the
[speed-quotient note](rank-one-speed-quotient-pass82.md):
\[
\begin{gathered}
I=I_0[z],\qquad I_0=(f_1,f_2,f_3)R,\qquad f_i=a_i(x,0),\\
q_0=q(x,0),\qquad b_0=b(x,0),\qquad
q-q_0\in I,\qquad b_0\in(R/I_0)^*.
\end{gathered}
\tag{2}
\]
Here I_0=I\cap R. Briefly, the slice equation makes b a unit modulo I;
E(a_i)=E(q)=0 then gives partial_z(a_i), partial_z(q) in I. Stability
under the actual partial implies coefficient extraction and ideal
extension, without discarding nilpotents. Evaluating the slice equation
at z=0 gives the final unit in (2).

If q_0=0, then q\in I and nothing further is needed. If I_0=0, all
a_i vanish, so E=b partial_z and local nilpotence forces partial_z(b)=0;
then q=0. For the return-map argument assume q_0 is nonzero. In
particular I_0 is nonzero. Properness and (2) also make b_0 nonzero.

## 2. The second intersection with the actual hyperplane

Let t be an independent parameter. The actual polynomial flow is
\[
\Phi_t(x,z)=(x+t a(x,z),\ z+t b(x,z)+t^2q(x,z)/2).
\tag{3}
\]
Starting on the original coordinate hyperplane z=0, its second root in
the last coordinate is t=-2b_0/q_0. Define the rational map of good
coordinate space
\[
\rho(x)=x-\frac{2b_0(x)}{q_0(x)}f(x),\qquad
q_0(\rho_i-x_i)=-2b_0f_i.
\tag{4}
\]
This is justified by substitution in the exact polynomial identities
for the original flow. No rationally rescaled derivation is declared
locally nilpotent. Invariance of a_i and q, together with
b(Phi_t)=b+tq, gives
\[
f(\rho)=f,\qquad q_0(\rho)=q_0,\qquad
b_0(\rho)=-b_0,\qquad \rho\circ\rho=\operatorname{id}.
\tag{5}
\]
The first three identities follow by evaluating at z=0 and the stated
rational time, where the new last coordinate is again zero. The last
follows by substituting those three identities into (4). In particular,
the compositions are defined as rational maps: q_0(rho)=q_0 is nonzero.

Thus rho is a birational involution. It need not extend regularly to
the zero set of q_0. The identity b_0(rho)=-b_0 also shows that a model
with a nonzero constant b_0 cannot be the specialization of an actual
action with q_0 nonzero. A formal flow determinant alone does not
impose this return identity.

## 3. An explicit monic integral equation

Write D=deg(b_0). The nonzero constant case is excluded by (5), so
D>=1. Define H_k as in (6), using all ordered k-tuples of indices.
In particular H_k belongs to I_0 to the kth power. These are frozen
directional Taylor coefficients: the derivatives act only on b_0,
not on the f_i. They are not iterates of the variable-coefficient
derivation sum f_i partial_i.

Taylor expansion of b_0 at x in the direction -2b_0 f/q_0, followed
by the sign identity (5), gives an explicit equation in Frac(R).
Cancel the nonzero factor 2b_0 and multiply by q_0 to the Dth power:
\[
\begin{gathered}
H_k=\sum_{i_1,\ldots,i_k=1}^{3}
f_{i_1}\cdots f_{i_k}
\partial_{i_1}\cdots\partial_{i_k}b_0\in I_0^k,\\
q_0^D+
\sum_{k=1}^{D}
\frac{(-1)^k(2b_0)^{k-1}}{k!}\,H_k q_0^{D-k}=0.
\end{gathered}
\tag{6}
\]
This is an equality in R and is monic in q_0, with its kth
coefficient in I_0^k. It proves directly, without a valuative
criterion, that
\[
\boxed{\ q_0\in\overline{I_0},\qquad q\in\overline I.\ }
\tag{7}
\]
Extending the integral equation from R to B shows q_0 is integral
over I. Since integral closure of an ideal is an ideal and q-q_0
lies in I, the second assertion follows. No arbitrary base-change
commutation theorem is used. Every nonleading coefficient of (6)
lies in I_0, so it also gives q_0^D in I_0 and q^D in I. Thus
D<=2 gives q squared in I. When D=1, (6) simplifies to
q_0=sum_i f_i partial_i(b_0), so q itself belongs to I in that case.

### Independent valuation reconstruction

Let v be any valuation of Frac(R) nonnegative on R, with values in a
totally ordered abelian group. Set v(0)=infinity and
v(I_0)=min_i v(f_i). Suppose, for a contradiction, that
v(q_0)<v(I_0).
Since q_0 belongs to R, every f_i has strictly positive value.
The actual unit statement (2) supplies h in R with b_0h-1 in I_0.
It follows that v(b_0)=v(h)=0. This works for nonclosed centers as
well; no discrete-value or closed-point assumption is needed.

Equation (4) now gives v(rho_i-x_i)>0 for every i. Consequently each
rho_i lies in the valuation ring and has the same residue as x_i.
Polynomial evaluation therefore gives b_0(rho)-b_0 in the maximal
ideal of that valuation ring. Equation (5), however, identifies this
difference with -2b_0, which is a unit because the valuation ring
contains the complex field. This is a contradiction.

Thus v(q_0)>=v(I_0) for every such valuation. This independently
recovers the first assertion in (7) by the ideal-valuative criterion.
For precision, that criterion follows from the Rees-ring test
[Stacks 00H3](https://stacks.math.columbia.edu/tag/00H3) and the
valuation separation lemma
[Stacks 090P](https://stacks.math.columbia.edu/tag/090P). If q_0 were
not integral over I_0, then q_0t would not be integral over
C=R[I_0t]. The normalization of C in Frac(R)(t) would admit a
containing valuation ring excluding q_0t. Its valuation w has
w(f_it)>=0 and w(q_0t)<0. Restricting w to Frac(R) gives precisely
the strict inequality just excluded. The nonzero ideal ensures
Frac(C)=Frac(R)(t). These valuation sources are inputs only to this
alternative proof, not to the explicit equation (6).

## 4. A local regular-return sufficient condition

There is also a stronger local conclusion when rho extends regularly.
Let m be a complex closed point of V(I_0) at which every component of
rho belongs to R_m. The value b_0(m) is nonzero by (2), while (5)
gives b_0(rho(m))=-b_0(m). Hence rho(m) differs from m. Some
rho_i-x_i is a unit of R_m, so (4) proves
\[
q_0\in I_0R_{\mathfrak m}
\quad\text{if rho is regular at }\mathfrak m\in V(I_0).
\tag{8}
\]
If rho is regular at every good-speed zero, localization detects
q_0 in I_0, hence q in I. A possible counterexample to first-power
membership must therefore have an indeterminacy or pole of this
rational return map at its nonmembership support. Regularity is a
sufficient condition, not a necessary one, and is not proved here.

## 5. The exact Briancon--Skoda consequence

The primary algebraic input is Lipman and Sathaye,
[*Jacobian ideals and a theorem of Briancon--Skoda*, Theorem 1,
printed p.199](https://www.math.purdue.edu/~jlipman/papers-older/%5B1981%5D%20Jacobian%20ideals%20and%20a%20theorem%20of%20Briancon-Skoda.pdf),
Michigan Mathematical Journal 28 (1981), 199--222.

Its auxiliary ideal may be set to zero in a regular Noetherian
domain. For an ideal generated by d+1 elements, it then gives
\[
\overline{J^{d+\lambda}}\subseteq J^\lambda
\qquad(\lambda\ge1).
\tag{9}
\]
Use the actual regular domain R=\mathbb C[x_1,x_2,x_3], the at most
three generators f_i (zero entries can be retained), d=2, and
lambda=1. The elementary power property of integral closure puts
q_0 cubed in the integral closure of I_0 cubed. One can see this
without valuations: R[I_0t] is integral over its third Veronese
ring R[I_0^3t^3], each generator f_it satisfying its cubic equation.
Since q_0t is integral over R[I_0t], its cube is integral over that
Veronese ring. Homogeneous coefficient extraction gives the stated
ideal-integrality property. Therefore
\[
\boxed{\ q_0^3\in I_0,\qquad q^3\in I.\ }
\tag{10}
\]
The passage back to B uses q-q_0 in I. No analytic completion or
assumption that I_0 is primary is needed for this algebraic source.

The separate
[cubic acceleration socle note](rank-one-cubic-acceleration-socle-pass83.md)
proves, using the characteristic-zero field case of Hickel's
Jacobian/socle theorem, that q cubed belongs to I exactly when
V(I_0) has no isolated closed points. Combining that distinct source
gate with (10) excludes all such isolated points. Embedded points
on a positive-dimensional germ are not thereby excluded. In
particular, the full good-speed scheme cannot have a nonempty
zero-dimensional component.

## 6. Source and proof scope

Geometry derived the actual return involution and its local regularity
gate. Root proposed the valuation argument extending that gate to
integral closure and then the shorter Taylor certificate (6).
Geometry and General independently reconstructed both extensions.
The proof above records that collaboration rather than claiming
individual ownership of all steps.

Geometry freshly read the complete displayed proofs of Stacks 00H3
and 090P and the valuation-existence proof used in the latter. The
Lipman--Sathaye PDF was visually read on printed pages 199--203:
Theorem 1, its full deduction from Theorem 1-prime, the statement of
the core Theorem 2, and the auxiliary lemma and its proof. The core
Theorem 2 proofs in Sections 2--3 were not freshly reconstructed.
This is a precise published-theorem application, not a claim to have
read every source dependency. General separately read a complete
selected analytic Briancon--Skoda proof and its descent gate; that
alternative is not needed for (9).

The complete saved socle note was independently read through EOF
by Geometry; no fresh Hickel proof read is claimed in this note.
No numerical test, actual counterexample, unrestricted coordinate
reduction, general cancellation result, or novelty finding is supplied.
All pass82 and earlier files remain unchanged.
