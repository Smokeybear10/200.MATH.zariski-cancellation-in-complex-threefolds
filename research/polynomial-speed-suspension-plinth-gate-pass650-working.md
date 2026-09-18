# An exact plinth gate for a family of changed quotient actions

Date: September 18, 2026.

Changing the cylinder's additive action is a genuine remaining route.
This note tests the family \(\Delta=P(u)D+f\partial_u\) completely:
for nonconstant scalar \(P\), its full plinth is exactly \(f\ker\Delta\).
All members have isomorphic quotient algebras. If the base is semirigid,
the standard plinth-compatible lifting construction from these actions
cannot move its common invariant ring. This is a method restriction,
not a classification of all cylinder actions or a cancellation result.
Novelty is UNKNOWN; no priority claim is made for this elementary argument.

## 1. Hypotheses, global flow, and localized kernel

Let \(k\) be a characteristic-zero field, \(R\) a finitely generated
\(k\)-domain, \(D\in\operatorname{LND}_k(R)\), and
\(0\ne f\in\ker D\). Put \(B=R[u]\), extending \(D(u)=0\).
Let \(P\in k[u]\) be nonconstant. Define
\[
 H'=P,\qquad H(0)=0,\qquad n=\deg H\ge2,
 \qquad \Delta=P(u)D+f\partial_u.
 \tag{1}
\]
No normality or factoriality assumption is imposed. In particular,
finite generation of the kernel \(K=\ker\Delta\) is not assumed.

There is an explicit global polynomial flow. For an independent
parameter \(T\), set
\[
 A_T(u)=\frac{H(u+fT)-H(u)}f\in R[u,T].
 \tag{2}
\]
The division is exact term by term by the binomial formula. The flow
sends \(u\) to \(u+fT\) and every \(a\in R\) to
\[
 \sum_{j\ge0}\frac{A_T(u)^j}{j!}D^j(a).
 \tag{3}
\]
The sum is finite and all its time coefficients are polynomial.
The addition law follows from
\(A_{T+S}(u)=A_T(u)+A_S(u+fT)\), since \(D\) kills all the
coefficients involved. Its derivative at zero is \(\Delta\).
Thus \(\Delta\) is an LND on the original, unlocalized \(B\).

In \(B_f=R_f[u]\), the automorphism
\[
 \Theta=\exp\left(-\frac{H(u)}fD\right),\qquad \Theta(u)=u
 \tag{4}
\]
has inverse obtained by changing the sign. Its coefficient is
\(D\)-invariant, so these are finite polynomial exponentials over
\(R_f\). Direct differentiation gives
\[
 \Delta\Theta(a)=0\quad(a\in R_f),\qquad \Delta(u)=f,
 \qquad K_f=\Theta(R_f)\subseteq R_f[H(u)].
 \tag{5}
\]
Equivalently, \(\Delta=\Theta(f\partial_u)\Theta^{-1}\).
Localization commutes with the kernel here because \(\Delta(f)=0\).

## 2. The whole kernel and the full plinth

The leading coefficient of \(H\) is a unit in \(k\). Polynomial
division therefore gives a free-module decomposition
\[
 R[u]=\bigoplus_{i=0}^{n-1}u^iR[H(u)].
 \tag{6}
\]
Uniqueness can also be seen from distinct highest \(u\)-degrees
modulo \(n\). The same decomposition holds after inverting \(f\).
Comparison of its coefficients gives
\[
 R[u]\cap R_f[H(u)]=R[H(u)],\qquad K\subseteq R[H(u)].
 \tag{7}
\]

Define \(\operatorname{pl}(\Delta)=\Delta(B)\cap K\). Then
\[
 \boxed{\operatorname{pl}(\Delta)=fK.}
 \tag{8}
\]
Indeed, take \(r\in B\) and \(h=\Delta(r)\in K\). In \(B_f\),
\[
 r=\frac hf u+k_0,\qquad k_0\in K_f\subseteq R_f[H(u)].
 \tag{9}
\]
Since \(n\ge2\), the coefficient of the independent basis element
\(u\) in (6) is exactly \(h/f\). But \(r\in R[u]\), so this
coefficient belongs to \(R[H(u)]\). It is invariant, and hence
\(h/f\in K\). This proves one inclusion in (8); the reverse
follows from \(\Delta(uq)=fq\) for \(q\in K\).

There is also a useful quotient-algebra identification. On \(R[v]\)
put \(L=D+f\partial_v\). The injection
\(\iota:R[v]\to R[u]\), fixing \(R\) and sending \(v\) to
\(H(u)\), satisfies
\[
 \Delta\iota=P(u)\iota L.
 \tag{10}
\]
Because \(P\ne0\), (7) and the domain property imply
\[
 K=\iota(\ker L).
 \tag{11}
\]
Thus these nonconstant choices of \(P\) all re-embed the same
abstract quotient of the constant-speed extension. Equation (8)
does NOT assert that \(L\) has that same plinth.

The nonconstant hypothesis matters. For \(R=k[a,b]\),
\(D=\partial_a\), \(f=b\), and \(P=1\), the field
\(\Delta=\partial_a+b\partial_u\) has slice \(a\), so its
plinth is its entire kernel, not the proper ideal \(bK\).
The case of a unit \(f\) causes no exception in (8).

## 3. Why this particular lifting route cannot move a semirigid base

More generally, fix a subring \(C\subseteq\operatorname{ML}(R)\).
Every intrinsic LND of \(R\) kills \(C\), so (4) fixes it pointwise.
Let \(\epsilon\in\operatorname{LND}_k(K)\) satisfy
\[
 \ker\epsilon\cap\operatorname{pl}(\Delta)\ne\{0\}.
 \tag{12}
\]
By (8) a nonzero element in this intersection is \(fq\) with
\(q\in K\). Factorial closure of an LND kernel gives
\(\epsilon(f)=0\). Therefore \(\epsilon\) extends as an LND
to \(K_f\). Transporting by (5) gives an LND \(\eta\) on
\(R_f\) that kills \(f\). Since \(R\) is finitely generated,
one common power \(f^N\) clears the images of its algebra generators:
\[
 f^N\eta(R)\subseteq R.
 \tag{13}
\]
This restriction is an LND, because \(\eta(f)=0\) and
\((f^N\eta)^j=f^{Nj}\eta^j\). It kills \(C\) by the definition
of \(\operatorname{ML}(R)\). Injectivity of localization then
gives \(\eta(C)=0\), and transport gives \(\epsilon(C)=0\).
Only finite generation of \(R\), not of \(K\), was used.

The standard lifting construction takes a nonzero \(h\) in (12),
chooses \(r\) with \(\Delta(r)=h\), extends \(\epsilon\) to
\(B_h=K_h[r]\) by killing \(r\), and multiplies by a common
power of \(h\) to obtain an LND on \(B\). Every such output kills
\(C\). The construction and its exact premise are stated in
[Gaifullin--Petrov, Section 7 and Proposition 7.2](https://arxiv.org/html/2607.13593v1#S7).
Their preceding full construction and the proposition were read
directly; no theorem about all cylinder actions is being invoked.

For a nonrigid semirigid base and \(D\ne0\), take
\(C=\operatorname{ML}(R)=\ker D\).
This route cannot produce a cylinder action moving that common
invariant ring. It does not rule out \(\epsilon\) that moves \(f\),
other quotient actions, or other lifting methods. Adjoining further
variables to \(R\) would also require a new ML hypothesis; it is
not silently covered by the semirigid-base conclusion.

## 4. Verification and status

Root derived the quadratic case; General and Jet independently
checked the full polynomial-speed proof, including the free-module
intersection, the whole plinth rather than a selected image element,
and invariant-denominator clearing. General supplied (10)--(11).
The written argument covers arbitrary nonconstant \(P\), not just
monomials or bounded degrees. No saved checker was executed.

General and Jet subsequently read all173 saved lines at SHA256
e097a8ab88d88907390a0571b89723e8fc9dc374096c17f5576b68f1daa0a472
and reported CLEAN. Full EOF reads were5b7a5d andaff02a; final
unchanged hashes were4bc0fb ande24a64. Root's fresh02ab4e,
General's freshaab726, and Jet's freshac41fa andb1e8a3 checked
whole flows, inverses and nonmonomial controls. The free-module
proof, not those examples, establishes the universal result.

The proof tests a specified changed-action construction and does not prove that a
semirigid cancellation candidate exists or that every possible
cylinder action kills \(C\). The general cancellation goal remains
UNSOLVED; these checks are not human expert review or formal
certification.
