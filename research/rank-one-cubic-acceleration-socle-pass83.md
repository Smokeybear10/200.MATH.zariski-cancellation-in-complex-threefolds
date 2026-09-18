# The cubic acceleration detects isolated good-speed zeros

In the actual rank-one quadratic sliced four-variable setting, the class
of the acceleration cubed is supported exactly at the isolated points
of the three-variable good-speed scheme. At each such point it is a
nonzero socle generator. Consequently, improving the known fourth-power
bound to the third power is equivalent to excluding those isolated
points. This note alone does not exclude such a point or prove first-
or second-power membership. The companion proof linked below now
supplies the isolated-point exclusion by a separate argument.

## 1. Actual hypotheses and the good-coordinate ideal

Retain actual polynomial coordinates and a supplied polynomial slice:
\[
B=\mathbb C[x_1,x_2,x_3,z],\qquad E\in\operatorname{LND}(B),
\qquad E(s)=1,\qquad E^2x_i=0,\quad E^2z=q,\quad E(q)=0.
\tag{1}
\]
Put a_i=E(x_i), b=E(z), T=partial_z, and I=(a_1,a_2,a_3)B.
If I=B all membership conclusions are immediate. Otherwise set
\[
R=\mathbb C[x_1,x_2,x_3],\qquad I_0=I\cap R,\qquad
f_i=a_i(x,0),\quad q_0=q(x,0),\quad b_0=b(x,0).
\tag{2}
\]
The exact ideal and quotient gates are proved in the
[divisorial note](rank-one-acceleration-divisorial-ideal-pass82.md)
and [speed-quotient note](rank-one-speed-quotient-pass82.md).
Here is the part needed below. The slice gives b(Ts)=1 modulo I.
Reducing E(a_i)=0 and E(q)=0 modulo I therefore gives T(a_i),T(q)
in I. A T-stable ideal in R[z] is extended from R: repeated
differentiation extracts the leading coefficient of any of its
polynomials, and subtraction then extracts every coefficient.
Evaluation at z=0 identifies its generators. Thus, with every
nilpotent retained,
\[
I=I_0[z],\qquad I_0=(f_1,f_2,f_3)R,\qquad
q-q_0\in I,\qquad b_0\in(R/I_0)^*.
\tag{3}
\]
The third assertion follows by coefficient extraction from T(q) in
I_0[z]. The fourth follows by evaluating b(Ts)=1 modulo I at zero.
Neither assertion uses reducedness of the speed scheme.

## 2. The actual determinant identifies the cubic class

Let L be the three-by-three matrix of good-coordinate derivatives of
the a_i, reduced modulo I, and let d be T(b) modulo I. The original
flow, not a formally prescribed quotient matrix, is
(x+t a,z+t b+t squared q/2). Its Jacobian determinant is one.
Its last column modulo I has zero entries above 1+td, so
\[
1=(1+td)\det(\operatorname{Id}_3+tL),\qquad
\det L=-d^3,\quad d^4=0,\quad \overline q=\overline b\,d.
\tag{4}
\]
These are the exact coefficient comparisons in the
[ambient nilpotence bound](rank-one-ambient-nilpotence-bound-pass82.md).
Specializing at z=0 is legitimate by (3), and the good derivatives of
a_i specialize to the derivatives of f_i. If
J_f=det(partial f_i/partial x_j), this yields
\[
q_0^4\in I_0,\qquad
q_0^3\equiv -b_0^3 J_f\pmod{I_0}.
\tag{5}
\]
In particular, the cubic acceleration class and the Jacobian class
differ by a unit. No derivative of an arbitrarily chosen set of
generators is substituted for this actual specialization.

## 3. The exact field-valued local source gate

The required external result is the field-characteristic-zero case of
[Hickel, Theorem 1.1](https://arxiv.org/pdf/0802.0426), printed page 2.
For n formal power series in n variables generating a proper ideal
over a characteristic-zero field, their Jacobian belongs to that
ideal exactly when its quotient has positive Krull dimension. In the
zero-dimensional case its class is a nonzero generator of the
Artinian quotient's socle.

Apply this only with ground field C. At a complex closed point m of
V(I_0), the faithfully flat completion of R_m is the power-series
ring in the three translated actual good coordinates. Completion
preserves local dimension and detects ideal membership. In dimension
zero, the quotient is already Artinian, so completion does not change
it. The source theorem consequently gives
\[
\begin{cases}
J_f\in I_0R_{\mathfrak m},
 &\dim(R_{\mathfrak m}/I_0R_{\mathfrak m})>0,\\
0\ne\overline{J_f}\text{ generates }
\operatorname{Soc}(R_{\mathfrak m}/I_0R_{\mathfrak m}),
 &\dim(R_{\mathfrak m}/I_0R_{\mathfrak m})=0.
\end{cases}
\tag{6}
\]
In the second case the three generators form a parameter sequence in
the three-dimensional regular local ring. Its quotient is an
Artinian local complete intersection. Its residue field is C.

The source use is deliberately restricted to a field, not a theorem
over nonreduced coefficient rings. The complete displayed Theorem
1.1, the selected residue statements in Section 2, and the relevant
field specializations of the proofs in Section 3 were read. This is
not a complete read of the paper's second half, of Lipman's original
proofs, or of every dependency in the cited arguments. No broader
Artinian-base alternative is required here.

## 4. Exact support, colon ideal, and exponent boundary

Let Z_iso be the finite set of isolated closed points of V(I_0).
An isolated point here means a zero-dimensional local germ of the
underlying zero set. Embedded associated points on a
positive-dimensional germ do not qualify. Finiteness follows from
Noetherianity: each isolated point is an irreducible component.

Combining (5) and (6), at every nonisolated point the class of q_0 cubed
is zero. At each isolated point it is a nonzero socle generator,
because multiplication by the unit -b_0 cubed preserves that property.
Its annihilator in that local ring is exactly its maximal ideal.
Away from V(I_0) the ideal is already the unit ideal. Comparing these
localizations at every maximal ideal of R proves
\[
(I_0:q_0^3)=\bigcap_{\mathfrak m\in Z_{\rm iso}}\mathfrak m.
\tag{7}
\]
The empty intersection is R. Indeed, the right side localizes to
mR_m at an isolated point m, and to the unit ideal everywhere else,
exactly as the colon on the left. Thus the cyclic submodule generated
by q_0 cubed in R/I_0 has reduced support Z_iso and length one at each
of its points. This statement does not discard nilpotents from R/I_0;
it identifies one particular socle submodule inside it.

Since q and q_0 have the same class in (R/I_0)[z], we obtain the precise
actual-action equivalence and local order statement
\[
\boxed{\ q^3\in I\ \Longleftrightarrow\ Z_{\rm iso}=\varnothing.\ }
\qquad
\mathfrak m\in Z_{\rm iso}\ \Longrightarrow
\overline{q_0}^{3}\ne0,\quad\overline{q_0}^{4}=0
\text{ in }R_{\mathfrak m}/I_0R_{\mathfrak m}.
\tag{8}
\]
The same local order holds on its polynomial z-cylinder. In
particular, any actual isolated good-speed point would make the
fourth-power bound sharp and would refute both q in I and q squared
in I. No such point or action is supplied by this proof. Conversely,
excluding isolated points would give only the cubic-power improvement;
it would not by itself prove either of those stronger memberships.

## 5. Limits and provenance

The divisorial result already gives first-power membership when the
speed ideal is principal. The present statement addresses the exact
codimension-three residue of the cubic class, rather than replacing
the divisorial argument or a classification theorem.

Root supplied the actual ambient determinant identity in pass82.
The source theorem is an established Jacobian/socle criterion, not a
new claim here. This note combines those inputs with the actual
good-coordinate ideal and proves the colon/support characterization.
It supplies neither a new recognized family nor unrestricted
cancellation. Local matrices, nilpotent quotient models, and even
Jacobians of three arbitrarily chosen polynomials do not by themselves
realize an E satisfying (1). The missing isolated-point exclusion in
this deduction is now supplied by the
[return-map and integral-closure proof](rank-one-return-map-integral-closure-pass83.md).
Its explicit monic certificate and Briancon--Skoda application prove
q cubed in I; equation (8) then excludes all isolated good-speed
points. This combined conclusion still does not exclude embedded
points on positive-dimensional components, prove first- or
second-power membership, or recognize the kernel.

No checker or full regression is added by this note. It is a written
working deduction with a stated external source gate, not human
expert review, formal proof certification, or an established novelty
claim. All pass82 and earlier files remain unchanged.
