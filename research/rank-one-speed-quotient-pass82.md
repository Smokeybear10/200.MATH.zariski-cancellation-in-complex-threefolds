# The rank-one speed quotient and its nilpotent quadratic motion

The full, possibly nonreduced zero scheme of the three good speeds is
an actual polynomial cylinder in the fourth original coordinate. Its
invariant quotient agrees with the good-coordinate subscheme. On that
cylinder, a quadratic change between the original coordinate and the
supplied slice can have a nonzero nilpotent quadratic coefficient.

This proves an exact scheme statement and isolates a limitation of
quotient-only arguments for acceleration membership. It does not
construct an ambient four-variable action with acceleration outside its
good-speed ideal, and it does not recognize the remaining actions.

## 1. Actual hypotheses and invariant contraction

Work with the original polynomial coordinates and slice:
\[
B=\mathbb C[x_1,x_2,x_3,z]=B_0[z],\qquad
E\in\operatorname{LND}(B),\qquad E(s)=1,
\qquad E^2x_i=0,\quad E^2z=q,\quad Eq=0.
\tag{1}
\]
Put
\[
A=\ker E,\quad a_i=Ex_i,\quad b=Ez,\quad
I_A=(a_1,a_2,a_3)A,\quad I=(a_1,a_2,a_3)B.
\tag{2}
\]
The generators a_i belong to A. The original slice presentation
\(B=A[s]\) consequently gives
\[
I=I_A[s],\qquad I\cap A=I_A,\qquad
C:=B/I=(A/I_A)[\overline s],\qquad
\overline E=\partial_{\overline s}.
\tag{3}
\]
These identities do not replace either ideal by its radical. We assume
\(I\ne B\); the empty speed scheme needs no quotient analysis.

## 2. The exact good-coordinate cylinder

The chain rule applied to the original polynomial slice gives, in C,
\[
1=\overline b\,\overline{\partial_zs}.
\tag{4}
\]
Thus \(\overline b\) is a unit even if C has nilpotents. Let R be the
image of \(B_0\) in C. Define the derivation
\(\delta=\overline b^{-1}\overline E\) on C. It kills R and takes
\(\overline z\) to one. No local nilpotence is assumed for this
rescaled derivation.

The natural map \(R[Z]\to C\), \(Z\mapsto\overline z\), is
surjective, since the original four coordinates generate B. It is
injective: if \(\sum_{j=0}^n r_j\overline z^{\,j}=0\), applying
\(\delta^n\) gives \(n!r_n=0\). R is a complex algebra, so
\(r_n=0\); descending induction kills every coefficient. This remains
valid with nilpotents and zero divisors. Hence
\[
C=R[\overline z],\qquad
\overline E=\overline b(\overline z)\partial_{\overline z},\qquad
\ker\overline E=R=A/I_A.
\tag{5}
\]
The final equality is the equality of the two actual embedded kernels
in (3) and (5). Coefficientwise differentiation over a complex algebra
has exactly the coefficient ring as kernel; multiplication by the unit
\(\overline b\) does not change it. This is not cancellation of an
unknown polynomial variable.

Write \(I_0=I\cap B_0\). The kernel of \(B_0[z]\to R[\overline z]\)
is coefficientwise \(I_0[z]\). Evaluating its displayed generators at
z=0 then gives the exact additional descriptions
\[
I=I_0[z],\qquad
I_0=(a_1(x,0),a_2(x,0),a_3(x,0))B_0,
\qquad \partial_zI\subseteq I.
\tag{6}
\]
One can also prove the stability first: \(E(a_i)=0\) implies
\(b\partial_za_i\in I\); cancel (4) in the quotient and then extract
coefficients by successive \(\partial_z\)-derivatives. The direct
proof above avoids assuming that a rescaled field is an LND.

## 3. What the quadratic hypothesis says over this nonreduced base

Use the identification R=A/I_A inside C. In the actual ring
\(C=R[\overline s]\), the equation \(\overline E^3\overline z=0\)
is coefficientwise. Thus
\[
\overline z=c_0+c_1\overline s+
 \frac{\overline q}{2}\overline s^2,
\qquad
\overline b=c_1+\overline q\,\overline s,
\qquad c_0,c_1,\overline q\in R,\quad
c_1\in R^*,\quad \overline q\in\operatorname{Nil}(R).
\tag{7}
\]
For the last conclusions, evaluate the unit \(\overline b\) at
\(\overline s=0\) to obtain the unit c_1. Reduce next modulo any prime
of R. A unit polynomial over a domain has degree zero, so the image of
\(\overline q\) vanishes in every prime quotient. It is therefore
nilpotent. This recovers radical membership but does not make
\(\overline q=0\).

Conversely, every polynomial in (7) with c_1 a unit and
\(\overline q\) nilpotent is a polynomial variable over R. For an
explicit inverse put
\(v=(\overline z-c_0)/c_1\),
\(\lambda=\overline q/(2c_1)\), and choose N with
\(\lambda^N=0\). Then
\[
v=\overline s+\lambda\overline s^2,\qquad
\overline s=\sum_{k=0}^{N-1}(-1)^k C_k\lambda^k v^{k+1},
\qquad C_k=\frac1{k+1}\binom{2k}{k}.
\tag{8}
\]
The Catalan recurrence \(C_0=1\),
\(C_k=\sum_{j=0}^{k-1}C_jC_{k-1-j}\) verifies that this is the
formal inverse of \(u\mapsto u+\lambda u^2\) in both orders.
Modulo \(\lambda^N\) the series is finite, so both formal identities
are identities in the polynomial ring over R. No localization or
reduced-base substitution is involved.

Equivalently, \(q\in I\) would say that the change (7) is affine in
the slice. It is equivalent to \(\overline b\in R^*\), or to
\(\partial_zb\in I\): in (5),
\(\overline q=\overline b\,\partial_{\overline z}\overline b\)
and \(\overline b\) is a unit. It follows in particular if R is
reduced, but reducedness has not been established in general.

## 4. A sharp quotient-only nilpotent control

For any integer N at least two, set
\[
R_N=\mathbb C[u,v,\varepsilon]/(\varepsilon^N),\qquad
C_N=R_N[s],\qquad \overline E=\partial_s,
\qquad z=s+\frac\varepsilon2s^2.
\tag{9}
\]
Equation (8) gives both polynomial inverse orders and proves
\(C_N=R_N[z]\). The coefficients u,v,epsilon are fixed, the slice s
is global, and \(\overline E^3z=0\). Nevertheless
\(\overline E^2z=\varepsilon\ne0\), with nilpotence order exactly N.
Also \(\overline Ez=1+\varepsilon s\) is a polynomial unit. Thus all
of these quotient-level properties allow arbitrarily thick nonzero
acceleration. In z coordinates the same actual quotient derivation is
the polynomial field \((1+\varepsilon s(z))\partial_z\).

This is a nonreduced-ring control, not a claimed lift to (1). In
particular it does not produce three ambient velocities whose actual
ideal is the displayed coefficient relation \((\varepsilon^N)\),
and does not impose the ambient four-variable divergence or conormal
identities. A proof of q in I may still use those additional data.
Primitive-divisor arguments likewise must be checked in the original
polynomial ring, not inferred from this model.

## 5. Dependency and verification boundary

The special nice case of the cylinder and kernel identification was
already proved in [pass77, Section 2](transverse-ideal-scheme-jets-pass77.md),
which was freshly reread here. There the fourth velocity was separately
E-invariant; that identity forced its image to be constant in the
fourth variable. The present hypothesis only makes its E-derivative
q invariant. The distinction is exactly the possible nilpotent
quadratic term in (7), not an omitted cancellation theorem.

Root supplied the direct rescaled-derivative injectivity proof in
Section 2. The stability-first proof and the nilpotent normal form
were independently reconstructed here. The earlier
[rank-one scope81](rank-one-acceleration-shear-boundary-pass81.md)
is unchanged; its radical and ideal-square statements are not promoted
to scheme membership.

All new steps are elementary polynomial and quotient-ring arguments
given above. No external theorem, source search, numerical suite,
frozen-file edit or shared metadata change is part of this note.
Neither q in I for the full actual class nor a recognition theorem is
claimed. These are written AI reconstructions, not human expert or
formal verification, and no historical novelty is asserted.
