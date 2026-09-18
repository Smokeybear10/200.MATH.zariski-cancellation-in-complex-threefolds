# A common factor really cancels from an actual return

An actual sliced polynomial action can have a nonunit common factor
of its bad speed and acceleration. That factor can disappear completely
from the return's pole divisor. The example below exercises the exact
reduced denominator in the [regular-locus theorem](rank-one-return-regular-locus-pass85.md);
it is not an action counterexample to ideal membership or recognition.

## 1. A global polynomial slice, with both coordinate inverses

In the actual polynomial ring B=C[a,x,c,z], let
\[
E=a^2\partial_x+(a-1)(1+ax)\partial_z,
\qquad b=E(z)=(a-1)(1+ax),
\qquad q=E^2(z)=a^3(a-1).
\tag{1}
\]
The three good coordinates are (a,x,c). Their second derivatives
vanish, E(q)=0, and q is nonzero. To establish the original global
slice without a localization, define
\[
v=(a-1)(x+ax^2/2)-a^2z,
\quad H_a(V)=-V-aV-aV^2/2,
\quad \sigma=\frac{x-H_a(v)}{a^2}.
\tag{2}
\]
The quotient in (2) is polynomial. Modulo a squared, the map
v=-x+a(x-x squared/2) is inverted by H_a. Thus its numerator
is divisible by a squared in B, not just in a rational function field.
Direct differentiation gives E(v)=0 and E(sigma)=1.

The map (a,x,c,z) to (a,v,c,sigma) has the explicit inverse
\[
\begin{gathered}
x=H_A(V)+A^2T,\qquad a=A,\qquad c=C,\\
z=\frac{(A-1)(x+Ax^2/2)-V}{A^2}.
\end{gathered}
\tag{3}
\]
Here x in the last numerator means the first displayed polynomial.
The inverse congruence (A-1)(H_A(V)+A H_A(V) squared/2)=V
modulo A squared makes this quotient polynomial too. In one
composition, (2) immediately recovers x and then z; in the other,
(3) immediately recovers v and then sigma. The coordinates a and c
are fixed in both orders. Consequently these are actual polynomial
coordinate maps, and E is exactly partial_sigma in them. This proves
local nilpotence and the global slice, rather than inferring either
from generic freeness.

## 2. The cancelled divisor and the remaining genuine pole

The actual good-speed ideal is I=(a squared). It is proper. Moreover
b[-1-a(1-x)] equals 1 modulo a squared, so b is a unit in B/I.
The common factor a-1 is also a unit there since
(a-1)(-1-a)=1-a squared. Coprimality of a and 1+ax gives
\[
\begin{gathered}
\gcd(b,q)=a-1,\qquad h=q/\gcd(b,q)=a^3,\\
\tau=-2b/q=-\frac{2(1+ax)}{a^3},\qquad
\rho=(a,-x-2/a,c,z).
\end{gathered}
\tag{4}
\]
Thus the rational return is regular along the entire divisor a=1,
even though both b and q vanish there. Its restriction is the
polynomial reflection x to -x-2. This is the restriction of the
reduced rational return, not a pointwise evaluation of the undefined
unreduced expression 0/0 or a unique second intersection on that fiber.

At a=0 the x component has reduced numerator -ax-2, which is a unit
at every point of that divisor. Its pole cannot cancel. Therefore
\[
\operatorname{Reg}(\rho)=D(a)=D(h),\qquad
V(I)=V(a),\qquad D(q)=D(a(a-1))\subsetneq D(h).
\tag{5}
\]
This proves the exact domain for this example directly. It does not
replace the separate all-action regular-locus proof. The return
preserves q, negates b, satisfies sigma composed with rho minus sigma
equal to tau, squares to the identity, and has determinant minus one.
It still has a genuine pole at every good-speed zero.

## 3. An actual coprime pair with common zeros

The second control is the retained two-speed action, not a new family.
Starting with the translation partial_s on C[s,a,b,c], its actual frame
and polynomial inverse are
\[
\begin{gathered}
(A,X,Y,Z)=(a,b+as,c+bs,s+(b+as)(c+bs)),\\
s=Z-XY,\qquad a=A,\qquad b=X-As,\qquad c=Y-bs.
\end{gathered}
\tag{6}
\]
The inverse equations are evaluated in the displayed order and are
polynomials. Both compositions are the identity. Differentiating the
forward map gives good speeds (0,a,b), bad speed 2abs+1+ac+b squared,
and acceleration 2ab. In the actual invariant ring C[a,b,c], the
normalized pair and fixed polynomial from the
[centered-return proof](rank-one-centered-return-quotient-pass85.md) are
\[
\begin{gathered}
h=2ab,\qquad v=1+ac+b^2,\qquad
T=hs^2+2vs,\qquad Z=bc+T/2,\\
\rho^*(s)=-s-2v/h,\qquad \rho^*(T)=T.
\end{gathered}
\tag{7}
\]
Neither a nor b divides v, so gcd(h,v)=1. However, h and v vanish
at a=0,b=i, with c arbitrary. This proves their ideal is proper.
Those points are not speed zeros, because b is nonzero. There T is
the constant zero map in s. At the speed zeros a=b=0, one instead
has v=1 and T=2s, a linear isomorphism. For comparison a=b=1,c=0
gives a genuine quadratic polynomial in s. These calculations do not
evaluate the rational reflection on h=0 or assert its regularity there.

## 4. Finite verification and scope

The standalone [two-method checker](return_denominator_checks_pass85.py)
uses unittest and SymPy only. The first method checks both polynomial inverse orders,
the transported translation, all required velocity layers, the full
ideal-unit identities, gcd cancellation, the rational involution and
slice displacement, the return determinant, and the two divisor
specializations after cancellation. The second checks the retained
two-speed coordinate inverse pair, its velocity layers, normalized
gcd, centered reflection identities, and the three displayed fiber
types. These are exact calculations for two actual actions. They do
not establish the general fixed-ring descent or finiteness theorem.
No numerical enumeration proves the general regular-locus theorem,
and no solver or earlier checker is imported.

Before the second method was added, the first author run passed its
one method in 0.177 seconds, with
complete tool output in chunk b6e392 and no failed assertion. The
checker SHA-256 was
56e7eeef167488c0bbfc6722921c146b9f7a20b6d2d0c879270fd3774b56b12c.
After adding the centered-pair method, the full two-method author run
passed in 0.200 seconds, with complete output in chunk fb5477 and no
failed assertion. The final checker SHA-256 is
807f5f306f75c802ffb807d257a876204cd91a63895f21061910fe0ca519244e.
The complete saved checker and mathematical note received an author
EOF reread; this is separate from any later independent review.

The action was proposed as a modification of the retained triangular
control. Jet and Root independently obtained the same truncated
polynomial inverse. No claim of a historically new action family is
made. This note does not resolve universal speed membership or
coordinate reduction. Files through pass84 are unchanged. Canonical
capture and integration, if performed, belong to Root and are separate
from the author runs. The historical one-method run is not an extra
method in the final two-method suite.
