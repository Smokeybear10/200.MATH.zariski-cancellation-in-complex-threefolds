# A degree-two nonsliced top still does not supply three good coordinates

This actual pair of sliced coordinate derivations has a primitive,
nonsliced degree-two top with a quadratic full divisor constant
extension. It has no polynomial slice for the second derivation in
the first derivation's invariant ring. Nevertheless its entire space
of common affine first integrals is only two-dimensional:
\(\ker T\cap\ker E^2=\mathbb C\oplus\mathbb Cu\).
Thus the pair cannot occur with three \(E\)-affine coordinates fixed
by \(T\). It is a countercontrol to a proposed realization shortcut,
not a counterexample to selected-divisor triviality or cancellation.

## 1. Two genuine sliced coordinate actions

Let
\[
\mathcal B=\mathbb C[u,a,b,c]=\mathcal A[u],\qquad
\mathcal A=\mathbb C[a,b,c],\qquad
E=\partial_u,\qquad
T=u\partial_a+(1+u^2a)\partial_b+u^2b\partial_c.
\tag{1}
\]
The order \(u,a,b,c\) makes both derivations triangular and locally
nilpotent. The first has slice \(u\). For the second put
\[
\begin{gathered}
W=b-\frac{u a^2}{2},\qquad P=a-uW,\\
Q=c-\frac{u^2W^2}{2}-\frac{u^3P^2W}{2}
       -\frac{u^4PW^2}{2}-\frac{u^5W^3}{6}.
\end{gathered}
\tag{2}
\]
Then \(TW=1\) and \(Tu=TP=TQ=0\).
There is a full polynomial coordinate certificate:
\[
\begin{gathered}
\mathcal B=\mathbb C[u,P,Q,W],\\
a=P+uW,\qquad
b=W+\frac{u(P+uW)^2}{2},\\
c=Q+\frac{u^2W^2}{2}+\frac{u^3P^2W}{2}
       +\frac{u^4PW^2}{2}+\frac{u^5W^3}{6}.
\end{gathered}
\tag{3}
\]
Substitution of (2) in (3) recovers the original variables.
Conversely the first two inverse formulas give
\(b-ua^2/2=W\) and \(a-uW=P\), after which the last one
gives \(Q\). Thus both inverse orders hold.

Differentiating (3) with \(u,P,Q\) fixed gives
\(Ta=u,\ Tb=1+u^2a\), and
\[
Tc=u^2W+\frac{u^3(P+uW)^2}{2}=u^2b.
\]
Hence \(T\) is precisely the coordinate partial
\(\partial_W\) in (3), and \(\ker T=\mathbb C[u,P,Q]\).
This conclusion uses the polynomial inverse, not a Jacobian converse.
The displayed coordinate frame does not have three \(E\)-affine
coordinates.

## 2. The exact primitive top and its full residue extension

On \(\mathcal A\), write
\[
T|_{\mathcal A}=\partial_b+u\partial_a+u^2L,\qquad
L=a\partial_b+b\partial_c,\qquad
[E,T]=\partial_a+2uL,\quad [E,[E,T]]=2L.
\tag{4}
\]
Thus \(L=[u^2](T|_{\mathcal A})\) is the exact nonzero
degree-two top. It is an LND, with \(Lb=a,\ Lc=b,\ L^2c=a\).
The coefficients \(a,b\) have gcd one, so primitive content
division leaves \(L\) unchanged. Every value lies in the proper
ideal \((a,b)\mathcal A\); hence \(L\) has no polynomial slice.

Its full invariant ring is
\[
S=\ker_{\mathcal A}L=\mathbb C[a,H],\qquad H=2ac-b^2.
\tag{5}
\]
Indeed, after inverting \(a\), the ring is
\(\mathbb C[a,a^{-1},H,b]\) and \(L=a\partial_b\).
Suppose \(a^{-m}F(a,H)\) is a polynomial in \(a,b,c\), with
\(m\ge0\) minimal. If \(m>0\), reduction modulo \(a\)
gives \(F(0,-b^2)=0\). Substitution \(H\mapsto-b^2\)
is injective on \(\mathbb C[H]\), so \(F\) is divisible
by \(a\), contradicting minimality. This proves (5).
It is the same primitive triangular top used in the retained
pair27, with a different sliced lifting here.[^1]

Let \(D=S_{(a)}\) and \(k=\operatorname{Frac}(S/aS)=\mathbb C(H)\).
The full divisor fiber, not merely a two-generator projected order, is
\[
\mathcal A_D/a\mathcal A_D
\simeq k[b,c]/(b^2+H)=\ell[c],\qquad
\ell=k[b]/(b^2+H),\qquad [\ell:k]=2.
\tag{6}
\]
The polynomial \(b^2+H\) is Eisenstein at the prime \(H\)
over \(\mathbb C[H]\), so it is irreducible over \(k\).
The reduced action is \(b\partial_c\). Here \(b\) is a unit
in \(\ell\), because \(b^2=-H\in k^*\); its invariant
field is exactly \(\ell\), and \(c/b\) is a residue slice.
Thus (6) is a genuine full divisor constant extension for the
primitive top.

## 3. There is no \(E\)-invariant \(T\)-slice

If \(r\in\mathcal A\) satisfied \(Tr=1\), equation (4)
would give
\[
\partial_b r=1,\qquad \partial_a r=0,\qquad Lr=0.
\tag{7}
\]
But \(\partial_a r=0\) puts \(r\) in \(\mathbb C[b,c]\).
Then \(Lr=a r_b+b r_c=0\), with \(a\) independent, gives
\(r_b=0\) and \(r_c=0\). Thus the common polynomial
kernel of \(\partial_a\) and \(L\) is \(\mathbb C\),
contradicting the first equation in (7).
The slice \(W\) in (2) is genuinely not \(E\)-invariant.

## 4. Every affine first integral is already known

Every element of \(\ker E^2\) has a unique form
\(F=F_0+uF_1\), with \(F_i\in\mathcal A\). By (4),
the condition \(TF=0\) is exactly
\[
\partial_bF_0=0,\quad
\partial_aF_0+\partial_bF_1=0,\quad
LF_0+\partial_aF_1=0,\quad LF_1=0.
\tag{8}
\]
The first and last equations give
\(F_0\in\mathbb C[a,c]\) and \(F_1=G(a,H)\).
The second now reads
\((F_0)_a=2bG_H(a,2ac-b^2)\).
Its left side is even in \(b\), while its right side is odd.
They must both vanish. Algebraic independence of \(a,H\)
then gives \(G_H=0\).

Write \(F_0=\phi(c)\) and \(F_1=\psi(a)\).
The third equation is \(b\phi'(c)+\psi'(a)=0\).
The coefficient of \(b\) and the constant coefficient both
vanish, so \(\phi,\psi\) are constants. Conversely constants
and \(u\) plainly satisfy both conditions. Therefore
\[
\ker T\cap\ker E^2=\mathbb C\oplus\mathbb Cu.
\tag{9}
\]

If \(T\) were the bad coordinate partial in a three-good
frame for this same \(E\), each of its three other polynomial
coordinates would lie in (9). They would be algebraically
dependent. This is impossible for coordinates. Changing the
chosen \(T\)-slice or its three kernel generators cannot bypass
the complete classification (9).

Thus two sliced coordinate actions, an exact degree-two primitive
nonsliced top, a full residue extension, and the absence of a common
tangent slice do not suffice to supply the actual three-good gate.
Here the gate fails even without imposing speed rank or density.

## 5. The common-tangent-slice shortcut has a separate obstruction

In an actual dense three-good frame
\(\mathcal B=\mathbb C[X,Y,Z,W]=\mathcal A[u]\), let
\(T=\partial_W\) and \(E=\partial_u\).
If some \(r\in\mathcal A\) satisfies \(Tr=1\), then
\(W-r\in\ker T=\mathbb C[X,Y,Z]\). A fixed-good polynomial
shear of the bad coordinate therefore gives \(r\), whose
\(E\)-degree is zero. In the retained notation,
\(\mu=\min_{F\in\mathbb C[X,Y,Z]}\deg_E(W+F)=0\).
The full divisor bound147 then forces every selected full divisor
constant extension to have degree one.[^2]

This corollary uses the actual three-good frame. It is not
applicable to manufacture that frame for the pair (1).
The no-common-slice proof in Section 3 also shows that this
particular failed realization is not explained just by the
\(\mu=0\) shortcut.

For comparison, the retained pair27 has
\(E=\partial_u,\ T_0=\partial_a+uL\).
It already has \([E,[E,T_0]]=0\), so the dense selected-degree
theorem132 excludes it before a degree-two test arises.[^3]
The new lifting (1) fixes that degree issue, but (9) exhibits
the remaining obstruction. No earlier pair27 result is
reclassified as a canonical selected dense example.

## 6. Exact scope and controls

The companion [checker](nonsliced_top_gate_controls_pass151.py)
checks both coordinate inverse orders, the two actual actions,
their exact coefficient top and finite nilpotence chains,
and the affine coefficient identities. The full invariant-ring,
residue-degree, and all-polynomial classification arguments are
the written proofs above, not extrapolations from finite tests.

This is an actual polynomial pair but not an actual dense
three-good selected frame. It neither disproves the sufficient
selected-divisor assertion isolated150 nor proves it.
Arbitrary three-good entry, global descent, independent human
review, and cancellation remain outside the result.[^4]

## Sources

1. Retained [*A sliced primitive pair with a nonsliced primitive highest adjoint*](primitive-top-slice-pass27.md),
   Sections 1--3. The exact top \(L\), its kernel, and the
   distinction between a genuine coordinate pair and the narrower
   canonical gate. The lifting and affine-first-integral argument
   in the present note are reproduced directly.
2. Retained [*A global divisor-residue bound for dense three-good frames*](dense-all-degree-divisor-residue-bound-pass147-working.md),
   Sections 1--6, together with the fixed-good minimum from145.
   Only the implication \(\mu=0\Rightarrow[\ell_p:k_p]=1\)
   is used in Section 5.
3. Retained [*Dense three-good speeds force exact bad-partial adjoint degree two*](dense-three-good-adjoint-degree-pass132.md).
   Its actual dense-frame degree statement, not a generic
   cofactor calculation, supplies the brief comparison with27.
4. [*The selected-divisor and three-good entry gaps*](selected-divisor-and-entry-gaps-pass150-working.md),
   Sections 1--5. The separate full-divisor and arbitrary-entry
   questions remain unchanged.

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
[^4]: Source 4.
