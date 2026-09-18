# The centered return has a polynomial fixed ring but no finite global cover

The normalized return is a reflection over the original invariant ring.
Its polynomial fixed functions form a polynomial extension of that
ring. The associated morphism is generically quadratic, but it is
finite globally only when the reduced return denominator is a unit.
In the proper good-speed-ideal branch that condition never holds.

The normalized invariant pair is coprime, not necessarily unimodular.
An existing actual sliced action with proper speed ideal exhibits this
distinction. None of these conclusions recognizes the original kernel
or removes a nonzero class of the acceleration modulo the speed ideal.

## 1. Normalize using the original slice

Retain the actual hypotheses and return from the
[regular-locus proof](rank-one-return-regular-locus-pass85.md). In
particular B=C[x_1,x_2,x_3,z], E is locally nilpotent, E(s)=1,
a_i=E(x_i) are invariant, b=E(z), E(b)=q, E(q)=0 and q is nonzero.
Put A=ker E. The original slice gives B=A[s]. Choose
\[
\begin{gathered}
g=\gcd(q,b),\qquad h=q/g,\qquad
v=b/g-hs,\qquad w=z-bs+qs^2/2,\\
h,v,g,w\in A,\qquad \gcd_A(h,v)=1,\qquad
b=g(hs+v),\quad q=gh.
\end{gathered}
\tag{1}
\]
Indeed g and h are invariant factors of q, as proved using E-degree
in the regular-locus note. Then E(b/g)=h, which gives E(v)=0;
the product rule gives E(w)=0. Since h and b/g are coprime in B,
the same holds for h and v.

For clarity, A is a UFD here without a recognition assumption.
A factor of an invariant polynomial in B is invariant, by the same
additivity of E-degree. Thus a factorization in the UFD B of a
nonzero element of A has all its factors in A. Its irreducible
factors remain irreducible in A, and uniqueness is inherited from B.
The units are the nonzero complex constants. This also justifies the
gcd notation in (1). No claim A=C^[3] is used.

The rational return fixes every element of A and satisfies
\[
\rho^*(s)=-s-2v/h,\qquad
T=hs^2+2vs\in B,\qquad \rho^*(T)=T,
\qquad z=w+(g/2)T.
\tag{2}
\]
The last identity follows by expanding the definition of w. In
particular, the centered variable s+v/h is a rational variable, not
a globally regular slice. Throughout, polynomial fixed functions
mean f in B satisfying rho^*(f)=f in Frac(B); rho is not presumed
to preserve B.

## 2. Exact descent of the polynomial fixed functions

Let K=Frac(A). The coordinate r=hs+v is transcendental over K and
changes sign under rho. Thus the rational fixed field is K(r squared)
and the polynomial fixed ring in K[s] is K[r squared]. Since
r squared=v squared+hT and h is a nonzero element of K, these are
K(T) and K[T], respectively. We claim
\[
B\cap\operatorname{Fix}_{\operatorname{Frac}(B)}(\rho^*)=A[T].
\tag{3}
\]
It remains to descend the coefficients of a polynomial in K[T].
Write a fixed f in B as D^(-1) times sum c_j T^j, with c_j and
D in A, D nonzero, and with no irreducible factor common to D
and all c_j. Suppose an irreducible p divides D. In the domain
(A/(p))[s], the reduction of T is nonconstant: its coefficients
h and 2v cannot both vanish because gcd(h,v)=1. At least one c_j
also remains nonzero. Consequently sum c_j T^j remains nonzero,
by the degree of a nonzero polynomial composed with a nonconstant
polynomial over a domain. But sum c_j T^j=Df would reduce to zero.
This contradiction proves D is a unit, establishing (3).

The element T is transcendental over A, so A[T] is indeed a
polynomial extension of A. Abstractly it is isomorphic to A[s]=B.
This observation does not cancel a variable or identify A itself
with a polynomial three-ring.

## 3. The generically quadratic morphism and its nonfinite fibers

The inclusion of the fixed polynomial ring has the exact presentation
\[
A[T]\ \subseteq\ B=A[s]
\simeq A[T,S]/(T-hS^2-2vS).
\tag{4}
\]
The presentation is justified by eliminating T; it uses no assertion
that an invariant-base coordinate system is an ambient coordinate
system. Over K, the extension K(s)/K(T) has degree two. For example,
r changes sign nontrivially and has fixed field K(T), as above.

The map is finite if and only if h is a unit of A. The reverse
implication is immediate from the quadratic monic relation after
dividing by h. For the forward implication, finiteness would make
s integral over A[T]. A monic polynomial in S annihilating it lies
in the principal kernel in (4). In the domain A[T][S], its leading
S coefficient is therefore -h times the leading S coefficient of
the other factor. Since the polynomial is monic, h must be a unit.
We have proved
\[
B\text{ is finite over }A[T]\quad\Longleftrightarrow\quad h\in A^*,
\qquad B_h\text{ is free of rank two over }A_h[T].
\tag{5}
\]
After inverting h the reflection is a regular involution and its
fixed ring is A_h[T]. Globally, (3) is an intersection statement for
a rational involution, not a finite-group quotient of an action on B.

The fiber behavior over any residue field k of A is explicit:
\[
\begin{array}{ll}
\bar h\ne0:& T=\bar hS^2+2\bar vS\text{ is a degree-two map},\\
\bar h=0,\ \bar v\ne0:& T=2\bar vS\text{ is a linear isomorphism},\\
\bar h=\bar v=0:& T=0\text{ is the constant map}.
\end{array}
\tag{6}
\]
In the last case the fiber over T=0 is a whole affine line, while
the fibers over nonzero values of T are empty.

Write I_A=(a_1,a_2,a_3)A, so I=I_A B. At every base speed zero,
the earlier radical containment q in radical(I) and the slice unit
condition make g and v nonzero in its residue field and make h zero.
Indeed g divides the quotient-unit b; then q=gh makes h zero,
and b=g(hs+v) reduces to gv. Thus all these points belong to the
linear-fiber case of (6), not the constant-map case. If I is proper,
the regular-locus result makes h a nonunit. Consequently the map
in (4) is not globally finite in the proper-speed-ideal branch.
This change in fiber degree does not remove the nilpotent class of
q in B/I and does not supply first-power membership.

## 4. Coprimality does not force a unit parameter pair

The retained actual two-speed frame gives a complete control. Start
with polynomial coordinates (s,a,b,c) and the translation partial_s,
and take the actual polynomial coordinate map
\[
(A,X,Y,Z)=(a,b+as,c+bs,s+(b+as)(c+bs)).
\tag{7}
\]
Its inverse is s=Z-XY, a=A, b=X-As, c=Y-bs. These expressions are
polynomial and substitution verifies both inverse orders. The
transported derivation has speeds (0,a,b,1+aY+bX), acceleration
q=2ab, and original supplied slice s=Z-XY. Its actual invariant
ring is C[a,b,c], and its speed ideal is the proper ideal (a,b)B.

For the normalized quantities in (1), this example gives
\[
g=1,\qquad h=2ab,\qquad v=1+ac+b^2,\qquad w=bc,
\qquad \gcd(h,v)=1,\quad (h,v)A\ne A.
\tag{8}
\]
Coprimality follows since neither a nor b divides v. Properness of
the pair follows at a=0,b=i, with c arbitrary. Those common zeros
are not speed zeros. At the speed zeros a=b=0 one has v=1, exactly
the linear-fiber situation in (6). Here q already lies in I squared;
the example is not a counterexample to first- or square-power
membership. Its complete actual checks are retained in the
[pass84 checker](strict_slice_checks_pass84.py), not newly executed.

Root proposed the normalized invariant pair and the relative
reflection question. Geometry derived the polynomial fixed-ring
descent and elementary finiteness criterion; Root supplied the
explicit z reconstruction and highlighted the relevant linear fibers.
No new source theorem, numerical method, coordinate-lowering step,
or general cancellation conclusion is claimed. This is an AI-checked
working proof, not expert or formal verification or a novelty claim.
