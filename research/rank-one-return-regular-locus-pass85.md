# The slice determines the exact regular locus of the return

For the actual rank-one quadratic sliced action, regularity of the
rational return is equivalent to regularity of its scalar return time.
Its maximal regular locus is one invariant principal open set. In the
nonzero-acceleration case it contains no point of the good-speed zero
scheme. Thus automatic regularity cannot activate the earlier local
regular-return sufficient condition at any actual speed zero.

This is a restriction on the rational return, not a first-power ideal
membership theorem or a coordinate-reduction result. All files through
pass84 remain unchanged.

## 1. Original action and the scalar recovered by the slice

Use the original polynomial coordinates and supplied global slice:
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z],\qquad E\in\operatorname{LND}(B),
\qquad E(s)=1,\\
a_i=E(x_i),\quad E(a_i)=0,\qquad b=E(z),\quad E(b)=q,
\quad E(q)=0,\quad q\ne0,\qquad I=(a_1,a_2,a_3)B.
\end{gathered}
\tag{1}
\]
The actual flow is Phi_t=(x+t a,z+t b+t squared q/2). Substitution
of t=-2b/q in its polynomial identities gives the rational involution
\[
\rho=(x-2ba/q,z),\qquad
q(\rho)=q,\quad b(\rho)=-b,\quad
s(\rho)-s=-2b/q,\quad \rho^2=\operatorname{id}.
\tag{2}
\]
These are the full-coordinate identities proved in the
[strict-slice note](rank-one-strict-slice-certificate-pass84.md).
No polynomiality of rho at q=0 is presumed. The polynomial b is
nonzero because E(b)=q is nonzero.

For a prime ideal p of B, a rational map into affine four-space is
regular at p exactly when its four coordinate functions belong to B_p.
If b/q belongs to B_p, formula (2) immediately gives this regularity.
Conversely, if all four components belong to B_p, the polynomial
s evaluated on those components also belongs to B_p. The slice
identity in (2), and the invertibility of 2, then give
\[
\rho\text{ is regular at }\mathfrak p
\quad\Longleftrightarrow\quad b/q\in B_{\mathfrak p}.
\tag{3}
\]
The reverse implication uses the original polynomial slice. The fact
that each coordinate displacement contains a good speed is not enough
by itself to recover the scalar denominator.

## 2. An invariant principal open set, with no additional indeterminacy

Choose a greatest common divisor g of b and q in the UFD B, and put
c=b/g and h=q/g. These choices are unique up to nonzero constants.
Then c and h are coprime and b/q=c/h. If h is not in p, this ratio
belongs to B_p. If it belongs to B_p, there exist f in B and t not in p
with c/h=f/t. Thus t c=f h. Coprimality implies h divides t in B,
so h cannot belong to p. Together with (3), this proves
\[
\operatorname{Reg}(\rho)
=D(h)=\operatorname{Spec}B\setminus V(h),
\qquad h=\frac{q}{\gcd(q,b)}.
\tag{4}
\]
This is the maximal regular locus into the original affine target,
not just one sufficient domain of definition. In particular, there
is no further codimension-two indeterminacy outside these divisors.
If h is a unit, the set is all of affine four-space.

The divisor factors are invariant under E. Indeed, for a nonzero
polynomial f define deg_E(f) as the largest n with E^n(f) nonzero.
In a characteristic-zero domain local nilpotence and the product rule
give deg_E(f_1 f_2)=deg_E(f_1)+deg_E(f_2): the unique highest surviving
Leibniz term is nonzero. Since q=g h has E-degree zero, both factors
have degree zero. The same reasoning applies to each irreducible
factor of h. Evaluating their flow invariance at the rational time
in (2) gives
\[
E(g)=E(h)=0,\qquad h(\rho)=h,\qquad
\rho:D(h)\longrightarrow D(h)
\text{ is a regular involution}.
\tag{5}
\]
For precision, the pullback maps B_h to itself because the coordinate
functions are regular there and h pulls back to the same unit h.
The rational identity rho squared equals the identity is consequently
an identity of regular maps on this principal open set. No assertion
is made that this is an automorphism of B before localization.

## 3. Every speed zero lies outside that regular locus

The slice equation is 1=sum a_i partial_i(s)+b partial_z(s), so b
is a unit modulo I. The retained actual-action results give q in
the radical of I. Only this set-theoretic containment is needed here,
not first-power membership or reducedness of B/I.

It also has a short independent check: at a complex speed zero p,
the orbit has fixed good coordinates and last coordinate
z(p)+b(p)t+q(p)t squared/2. Composing the polynomial s with this
orbit gives s(p)+t. If q(p) were nonzero, the degree of this
composition would be either zero or a positive even integer, not
one. Thus q vanishes at every such p, which gives radical containment
over C. The slice equation also gives b(p) nonzero.

At any prime p containing I, therefore, q belongs to p and b is a
unit in B_p. If b/q belonged to B_p, the equation q times (b/q)=b
would make the nonunit q invertible, a contradiction. Equivalently,
g is a local unit because it divides b, whereas h=q/g belongs to p.
Hence
\[
V(I)\subseteq V(h),\qquad
\operatorname{Reg}(\rho)\cap V(I)=\varnothing.
\tag{6}
\]
When I=B this assertion is vacuous. It otherwise excludes regularity
at every speed zero, not merely at points that could support a
nonzero class of q modulo I. It does not assert that V(h) equals
V(I), nor does it discard nilpotents in the speed quotient.

## 4. The original hyperplane return and the earlier sufficient gate

For the specialized return put R=C[x_1,x_2,x_3], J=I intersect R,
f_i=a_i(x,0), b_0=b(x,0), q_0=q(x,0), and r=s(x,0). The retained
[exact speed quotient](rank-one-speed-quotient-pass82.md) gives
I=J[z], J=(f_1,f_2,f_3), b_0 a unit modulo J, and q_0 in the radical
of J. Assume explicitly that q_0 is not the zero polynomial.
The same original flow starting on z=0 gives
\[
\begin{gathered}
\rho_0=x-2b_0f/q_0,\qquad r(\rho_0)-r=-2b_0/q_0,\\
\operatorname{Reg}(\rho_0)
=D\!\left(q_0/\gcd(q_0,b_0)\right)
\subseteq\operatorname{Spec}R\setminus V(J).
\end{gathered}
\tag{7}
\]
The proof is the same local-ring and UFD argument as (3)--(6),
now using the polynomial r. If q_0 is identically zero, this rational
second-intersection formula is not defined and no assertion about
its regular locus is made.

Section 4 of the frozen
[pass83 return proof](rank-one-return-map-integral-closure-pass83.md)
gave a logically valid sufficient condition for local membership:
regularity of rho_0 at a closed point of V(J). Equation (7) shows
that, under the actual supplied-slice hypotheses and q_0 nonzero,
that premise never occurs. This does not falsify the sufficient
implication. It closes the attempt to establish its premise
automatically at actual speed zeros.

Root proposed the slice-recovery argument and the exact UFD regular
locus. Geometry reconstructed the local-ring equivalence, invariant
domain and specialized scope. The proof is elementary; no new source
theorem, numerical method, action family, membership conclusion,
coordinate reduction or general cancellation claim is used. This is
AI proof checking, not expert or formal verification or a novelty claim.
