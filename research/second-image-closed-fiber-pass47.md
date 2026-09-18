# The second-image obstruction is a scalar minimal slice on a closed fiber

In the remaining degree-two frame, the second-image ideal has a
basepoint exactly when the actual minimal local slice becomes a
scalar in the entire scheme-theoretic closed quotient fiber.
Faithful flatness gives this precise obstruction, rather than
automatically excluding it.

The proof uses a socle element of the finite-length obstruction
ideal and an explicit regular-sequence cancellation. No freeness
theorem for the LND filtration and no nonvanishing assertion for
the induced derivation on every closed fiber is used.

## 1. Hypotheses and exact conclusion

Retain the actual intrinsic ring and action from
[the second-image criterion](second-image-gluing-pass46.md):
\[
A[s_*]\simeq\mathbb C^{[4]},\qquad
C=\ker D\simeq\mathbb C[U,V],\qquad
\operatorname{pl}(D)=pC,\qquad Dr=p.
\tag{1}
\]
The action \(D\ne0\) is primitive. The actual inclusion
\(C\subset A\) is faithfully flat and factorially closed,
and \(A\) is a UFD. The preceding degree-two frame arguments
have supplied the full quadratic local models at every prime
factor of \(p\), not merely quadratic residue fields.

Put
\[
F_i=\ker D^{i+1},\qquad
I_2=D^2(A)\cap C=pJ.
\tag{2}
\]
The established conclusions are
\[
F_1=C\oplus Cr,\qquad p\in J,\qquad
J_{(\pi)}=C_{(\pi)}
\quad\text{for every irreducible }\pi\in C.
\tag{3}
\]
Thus \(C/J\) has finite support if it is nonzero.

Fix a closed point \(\mathfrak m=(U-u_0,V-v_0)\) of the
invariant plane. Write
\[
R=C_{\mathfrak m},\quad
\mathfrak n=\mathfrak mR=(u,v),\quad
\mathcal A=A\otimes_C R,\quad
k=R/\mathfrak n=\mathbb C,
\tag{4}
\]
where \(u=U-u_0\) and \(v=V-v_0\).
All localization is at actual invariants. In particular it
commutes with \(F_i\), with the full plinth, and with \(I_2\).
The same symbols \(r,p,D\) denote their images over \(R\).

**Theorem.** Under these hypotheses,
\[
\boxed{\quad
J R\ne R
\quad\Longleftrightarrow\quad
\bar r\in k\subset\mathcal A/\mathfrak n\mathcal A.
\quad}
\tag{5}
\]
The right side concerns the whole quotient ring, including any
nilpotents. It does not mean that \(r\) takes the same value
only on the reduced set of closed points.

Equivalently, \(JR=R\) exactly when the natural map
\[
(F_1\otimes_C R)/\mathfrak n(F_1\otimes_C R)
\longrightarrow\mathcal A/\mathfrak n\mathcal A
\tag{6}
\]
is injective. At a point where it is not injective, the image
of this two-dimensional vector space is the one-dimensional
space of constants.

## 2. A proper second-image ideal supplies a socle relation

Assume \(JR\ne R\). By (3), its radical is
\(\mathfrak n\), so \(R/JR\) is a nonzero Artinian local
ring. Its socle is nonzero: take a nonzero element in the last
nonzero power of its maximal ideal. Consequently there exists
\(z\in R\setminus JR\) such that
\[
uz\in JR,\qquad vz\in JR.
\tag{7}
\]
By the definition of the actual second image, choose
\(a,b\in\mathcal A\) with
\[
D^2a=puz,\qquad D^2b=pvz.
\tag{8}
\]
These elements automatically belong to
\(\ker(D^3:\mathcal A\to\mathcal A)\), because the values
in (8) are invariant.

The difference \(va-ub\) has second derivative zero. The
localized version of \(F_1= C\oplus Cr\) therefore gives
\[
va-ub=\alpha+\beta r,\qquad \alpha,\beta\in R.
\tag{9}
\]

Suppose \(\beta\in\mathfrak n\). The left side of (9)
belongs to \(\mathfrak n\mathcal A\), as does \(\beta r\).
Faithful-flat ideal contraction gives
\[
\alpha\in\mathfrak n\mathcal A\cap R
=\mathfrak n.
\tag{10}
\]
It follows that \(\alpha+\beta r\in\mathfrak n(R+Rr)\).
Choose \(c_1,c_2\in R+Rr\) with
\(\alpha+\beta r=uc_1+vc_2\), and set
\[
a'=a-c_2,\qquad b'=b+c_1.
\]
Since \(D^2c_1=D^2c_2=0\), their second derivatives are still
the values in (8), whereas (9) now becomes
\[
va'=ub'.
\tag{11}
\]

Here is the exact cancellation supplied by flatness. The parameter
\(v\) is a nonzerodivisor on \(R/uR\). Tensoring that
injection with the flat \(R\)-module \(\mathcal A\) makes
\(v\) a nonzerodivisor on \(\mathcal A/u\mathcal A\).
Equation (11) therefore forces \(a'=ut\) for some
\(t\in\mathcal A\). Since \(\mathcal A\) is a domain
and \(u\ne0\), the same equation then gives \(b'=vt\).
Applying \(D^2\) to the first equality yields
\[
uD^2t=puz,\qquad D^2t=pz.
\tag{12}
\]
This contradicts \(z\notin JR\), because the actual localized
second image is \(pJR\).

Thus \(\beta\notin\mathfrak n\), so \(\beta\) is a unit
of \(R\). Equation (9) proves the stronger membership
\[
r+\alpha/\beta\in
\mathfrak n\ker(D^3:\mathcal A\to\mathcal A)
\subset\mathfrak n\mathcal A.
\tag{13}
\]
In particular \(\bar r=-\bar\alpha/\bar\beta\in k\).
This proves the forward implication in (5).

The argument in this section requires (3), faithful flatness,
and a domain, but no assertion about the induced derivation
on the closed fiber. It does not apply the nonzero generic-
divisor derivation statement to a closed point.

## 3. A unit second-image ideal gives full closed-fiber independence

Suppose now that \(JR=R\). Apply the localized form of
the proved second-image equation criterion. There are
\(Y\in\mathcal A\) and \(a_0,b_0\in R\) such that
\[
\mathcal A=R[r,Y]\simeq
R[\mathsf T,\mathsf Y]/
(p\mathsf Y-\mathsf T^2-a_0\mathsf T-b_0),
\qquad DY=2r+a_0.
\tag{14}
\]
For clarity, that criterion localizes without assuming a new
coordinate system: choose \(D^2Y=2p\), integrate twice
using \(F_1\), compare at every height-one prime of \(R\)
using the full quadratic models, and contract coefficients
in the generic monic basis. These are exactly the arguments
of pass 46 over the UFD \(R\) instead of \(C\).

The ring in (14) is free over \(R\), with basis
\[
\{Y^k,rY^k:k\ge0\}.
\tag{15}
\]
Its reduction modulo \(\mathfrak n\) retains the same
vector-space basis. In particular \(1\) and \(\bar r\)
are linearly independent over \(k\). This holds also when
the reduced quadratic polynomial has a repeated root: its
nonzero nilpotent class must not be discarded.

If \(p\) is a unit in \(R\), one can instead use directly
\(\mathcal A=R[r/p]\), with the same independence conclusion.
This completes the reverse implication in (5).

Faithful flatness makes the map from constants
\(k\to\mathcal A/\mathfrak n\mathcal A\) injective.
Since \(F_1\otimes_C R=R\oplus Rr\), any nontrivial
kernel of (6) is therefore exactly a scalar relation for
\(\bar r\). This proves the equivalent formulation.

## 4. Exact remaining obligation

The obstruction is unchanged when the actual minimal slice is
replaced by \(r+c\), \(c\in C\), since that only changes
its closed-fiber scalar by a constant. Thus (5) is not a bad
choice of the additive normalization of the minimal slice.

To prove \(J=C\) by this route, one must now prove that the
image of \(r\) is nonconstant in every full closed fiber.
Faithful flatness guarantees that the constants inject; the
argument above does not upgrade that to injection of
\(C+Cr\). Likewise, primitivity gives a nonzero derivation
on every generic divisor fiber, but does not give one on
every closed fiber.

No actual counterexample to the full cylinder and frame
hypotheses is asserted. Nor does this lemma independently
establish or refute \(J=C\). It gives an exact scheme-theoretic
closed-fiber condition equivalent to the remaining finite
second-image obstruction. Even its removal would yield the
global quadratic equation from pass 46, not automatically
three polynomial generators for \(A\).

The proof uses the inherited exact plinth and local models,
elementary socle theory in an Artinian local ring, and the
explicit faithful-flat regular-sequence cancellation in
(10)--(12). It neither asserts a general image-ideal freeness
theorem nor invokes a new external classification result.
All frozen pass-46 artifacts are left unchanged.
