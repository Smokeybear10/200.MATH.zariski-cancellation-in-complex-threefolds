# Invariant extensions: slice-degree lowering under higher-image saturation

Date: September 17, 2026.

Status: author working note, subject to independent saved-source review.
This is a conditional slice criterion. It does not establish the criterion for
an arbitrary locally nilpotent derivation of a three-variable polynomial ring.
No cancellation, coordinate-entry, or novelty claim is made.

This note rederives and consolidates a result already retained in
[Higher-image torsion and the affine-slice question, Sections 2–3](invariant-affine-slice-pass16.md).
That earlier note contains the exact slice recurrence, invariant polynomial,
higher-image torsion obstruction, and saturation-based degree lowering used
here. This is not new mathematical progress on the necessity direction.

## 1. Statement and notation

Let $k$ be a field of characteristic zero, let $R$ be a commutative
$k$-domain, and let $H\ne0$ be a locally nilpotent $k$-derivation of $R$.
Set

\[
 K=\ker H,\qquad
 \mathcal F_n=\ker H^{n+1},\qquad
 I_n=H^n(\mathcal F_n)=H^n(R)\cap K\quad(n\ge0).
 \tag{1}
\]

Here $I_0=K$, and $I_1=H(R)\cap K$ is the plinth ideal. The equality of
the two descriptions of $I_n$ follows because $H^n(r)\in K$ is equivalent
to $H^{n+1}(r)=0$. Each $I_n$ is an ideal of $K$, since $H$ kills its
coefficients in $K$.

For $a\in K$, extend $H$ to $R[v]$ by $H(v)=0$, and define

\[
 E=H+a\partial_v.
 \tag{2}
\]

The two summands commute and are locally nilpotent, so $E$ is locally
nilpotent. For example, the binomial expansion of $E^N$ kills a given
polynomial once $N$ exceeds the sum of bounds for the two summands on its
finitely many coefficients and powers of $v$.

For nonzero $a$, impose the higher-image saturation hypothesis

\[
 aK\cap I_n=aI_n\qquad\text{for every }n\ge2.
 \tag{3}
\]

Equivalently, multiplication by $a$ is injective on $K/I_n$, for every
$n\ge2$. Indeed, if $ac\in I_n$, (3) writes $ac=ab$ with $b\in I_n$;
cancellation in the domain gives $c=b\in I_n$. The reverse implication is
immediate. In particular, (3) implies

\[
 a^j c\in I_n,\quad c\in K,\quad j\ge1
 \quad\Longrightarrow\quad c\in I_n
 \qquad(n\ge2).
 \tag{4}
\]

Theorem. If $a\ne0$ and (3) holds, the following conditions are equivalent:

1. $E$ has a polynomial slice in $R[v]$.
2. $E$ has a slice $r+jv$, with $r\in R$ and $j\in K$.
3. $aK+I_1=K$.

Moreover, starting with any slice, the proof lowers its $v$-degree by
subtracting $E$-invariant polynomials until the degree is at most one.
For $a=0$, the same three conditions are equivalent without a saturation
assumption. If $a\in K^*$, they hold with slice $a^{-1}v$.

No finite generation, normality, polynomiality of $K$, or dimension
assumption is used in this theorem.

## 2. The exact slice recurrence

Let

\[
 S=\sum_{i=0}^{m}r_i v^i\in R[v],\qquad E(S)=1,
 \qquad r_m\ne0.
 \tag{5}
\]

For $m\ge1$, coefficient comparison gives the complete recurrence

\[
 Hr_0+ar_1=1,\qquad
 Hr_i=-(i+1)ar_{i+1}\ (1\le i<m),\qquad Hr_m=0.
 \tag{6}
\]

Thus $c:=r_m\in K\setminus\{0\}$. When $m\ge2$, applying $H$ to the first
equation and then using the second starts the identities

\[
 H^2r_0=2a^2r_2,\qquad
 H^j r_0=(-1)^j j!a^j r_j\quad(2\le j\le m),\qquad
 H^{m+1}r_0=0.
 \tag{7}
\]

The middle formula follows inductively from (6). Its first case is $j=2$,
not $j=1$: the constant $1$ in (6) must not be dropped.

For $a\ne0$, the last nonzero term in (7) is

\[
 H^m r_0=(-1)^m m!a^m c\ne0.
 \tag{8}
\]

Consequently $r_0\in\mathcal F_m$, $a^m c\in I_m$, and (4) gives

\[
 c\in I_m\qquad(m\ge2).
 \tag{9}
\]

This is the only step requiring higher-image saturation.

## 3. An invariant polynomial with the prescribed leading coefficient

By (9), and because nonzero integers are units in $k$, choose
$b\in\mathcal F_m$ with the normalization

\[
 H^m b=(-1)^m m!c.
 \tag{10}
\]

Define the finite polynomial

\[
 Q_{m,b}(v)=
 \sum_{j=0}^{m}\frac{(-1)^j}{j!}
 a^{m-j}H^j(b)v^j\in R[v].
 \tag{11}
\]

This formula divides only by nonzero integers, never by $a$. It can be
viewed in $R_a[v]$ as $a^m\exp(-vH/a)(b)$, but the displayed polynomial
formula is sufficient and stays in the original ring.

Applying $H$ to the $j$-th summand gives

\[
 \frac{(-1)^j}{j!}a^{m-j}H^{j+1}(b)v^j.
 \tag{12}
\]

For $0\le j<m$, applying $a\partial_v$ to the $(j+1)$-st summand gives
the negative of (12). The remaining $H$-term at $j=m$ vanishes because
$H^{m+1}b=0$. Therefore the whole polynomial satisfies

\[
 E(Q_{m,b})=0,\qquad
 [v^m]Q_{m,b}=\frac{(-1)^m}{m!}H^m b=c.
 \tag{13}
\]

It follows that $S-Q_{m,b}$ is still an $E$-slice and has $v$-degree
strictly less than $m$. It cannot be the zero polynomial because its
$E$-derivative is $1$.

Repeat this step whenever the current degree is at least two. Each step
uses (3) only at that current degree, so the process reaches degree at most
one after finitely many subtractions. In particular, for a supplied slice
of degree $m$, saturation for $2\le n\le m$ already suffices. The theorem
uses every $n\ge2$ to avoid assuming a degree bound for an unknown slice.

The proof is an algebraic existence argument with choices of preimages
$b\in\mathcal F_m$. It does not claim an effective procedure for computing
all image ideals or finding those preimages in an arbitrary presentation.

## 4. The affine-linear endpoint and both directions

For a slice $S=r+jv$, direct coefficient comparison gives

\[
 Hj=0,\qquad Hr+aj=1.
 \tag{14}
\]

Thus $j\in K$, $Hr=1-aj\in K\cap H(R)=I_1$, and $aK+I_1=K$.
If the degree has fallen to zero, the same conclusion holds with $j=0$.

Conversely, if $1=aj+p_0$ with $j\in K$ and $p_0\in I_1$, choose
$r\in R$ with $Hr=p_0$. Then (14) holds, so $r+jv$ is a slice.
This sufficiency direction does not require (3).

For $a=0$, a slice $S=\sum r_i v^i$ satisfies $Hr_0=1$ by its constant
coefficient. Hence $I_1=K$, and $r_0\in R$ itself is a slice. This proves
the $a=0$ assertion without using cancellation by $a$. For a unit
$a\in K^*$, $E(a^{-1}v)=1$, and $aK+I_1=K$ directly. Saturation is
automatic in that case as well.

## 5. A principal-image-ideal corollary

Assume now that $K$ is a UFD, $I_1=pK$, and every $I_n$ for $n\ge2$
is principal. Take nonzero $a\in K$ such that

\[
 \gcd(a,p)=1.
 \tag{15}
\]

Then (3) holds, and the theorem proves

\[
 H+a\partial_v\text{ has a slice}
 \quad\Longleftrightarrow\quad (a,p)K=K.
 \tag{16}
\]

Here $p\ne0$. To see that a nonzero plinth element always exists, choose
$r\in R\setminus K$ of positive $H$-degree $e$. The element
$H^{e-1}r$ is a local slice with nonzero invariant derivative $H^e r$.

To prove the corollary, choose $s\in R$ with $Hs=p$. Since $p\in K$,
$H^2s=0$ and the Leibniz rule gives $H^n(s^n)=n!p^n$. Therefore, for all
$n\ge1$,

\[
 p^nK\subset I_n\subset I_1=pK.
 \tag{17}
\]

The second inclusion follows because an invariant element $H^n(r)$, for
$n\ge1$, also equals $H(H^{n-1}r)\in H(R)\cap K$.

Write $I_n=p_nK$. Equation (17) implies $p\mid p_n$ and $p_n\mid p^n$.
Thus every prime factor of $p_n$ is a prime factor of $p$. By (15),
$a$ and $p_n$ are coprime. Unique factorization now gives

\[
 aK\cap p_nK=ap_nK=aI_n,
 \tag{18}
\]

which is (3).

The gcd condition is not the conclusion $(a,p)K=K$. In a UFD of dimension
at least two, coprime elements can generate a proper ideal, for example the
two variables of $k[s,t]$. The corollary allows that case and concludes
that the extension then has no slice.

In the three-variable polynomial setting, principality of the plinth ideal
alone does not supply the extra assumption that all higher $I_n$ are
principal. Neither that extra assumption nor (3) is asserted for arbitrary
three-variable locally nilpotent derivations here. No conclusion for the
common-divisor cases omitted by (15) follows from this corollary.

## 6. Primary antecedent and the remaining boundary

The direct internal antecedent is
[invariant-affine-slice-pass16.md, Sections 2–3](invariant-affine-slice-pass16.md),
read completely through its 276-line EOF for this note. Its Section 2 proves
the same conditional lowering theorem, including the sufficiency of saturation
only through the degree of a supplied slice. Its normalization chooses
$H^m h=c$ and subtracts $(-1)^m m!Q_{m,h}$; (10) incorporates that scalar into
$b$ instead. The arguments are the same. Section 5 above records the elementary
principal-image/gcd consequence with its extra assumptions explicitly stated.

Gene Freudenburg, *Actions of $SL_2(k)$ on affine $k$-domains and fundamental
pairs*, arXiv:2108.12021v2, Section 7.1, Proposition 7.1, studies an invariant
extension $D'=D+a\partial_u$ under the hypothesis
$aA\cap I_n=aI_n$ for every $n\ge0$. It identifies the extended kernel
using the degree modules of $D$.

Primary links:

- [Full text, Section 7.1 and Proposition 7.1](https://arxiv.org/html/2108.12021v2#S7.SS1).
- [Versioned arXiv record](https://arxiv.org/abs/2108.12021v2).

The hypothesis and the finite Taylor polynomials are therefore established
antecedents, not new terminology or a claimed discovery. The proof above is
self-contained and uses saturation only for $n\ge2$, as the retained pass 16
already did, because degree zero and degree one are handled directly.
External priority of the precise formulation has not been established:
novelty is UNKNOWN. Internal priority belongs to the retained pass 16, and
this note must not be counted as discovery of a new theorem.

Without saturation, the exact recurrence (6) only gives
$Hr_0+ar_1=1$, and it does not make $r_1$ invariant. It also gives
$a^m c\in I_m$, but it does not permit removing the factor $a^m$.
These are the missing implications in applying this argument to an
arbitrary $H\in\operatorname{LND}(\mathbb C^{[3]})$.

The archive also contains the stronger claims in
[general-invariant-affine-pass17.md](general-invariant-affine-pass17.md) and
[pointwise-plinth-pass17.md](pointwise-plinth-pass17.md). Their geometric
argument and primary-source hypotheses are a separate audit task. This note
neither revalidates nor withdraws those claims and must not replace that
stronger retained work. Its conditional algebraic proof alone does not settle
the full criterion.

Even where the theorem applies, it supplies an affine-linear slice, not a
polynomial presentation of its kernel. If $E(r+jv)=1$, the slice theorem
gives $R[v]=(\ker E)[r+jv]$; it does not by itself identify $\ker E$
with a polynomial ring. No arbitrary four-dimensional coordinate entry,
global degree-minimization result, or cancellation theorem follows here.

## 7. Verification and review status

The argument was checked directly through the recurrence and the complete
telescoping cancellation in (11)–(13). A fresh, unsaved symbolic calculation
on the universal nilpotent cable $H(z_i)=z_{i-1}$, $H(z_0)=0$, verified
the whole invariant polynomial and its leading coefficient for every
$m=2,\ldots,8$. This calculation was recorded as `f031d6`; it supports the
uniform proof and does not replace it.

A second fresh calculation, recorded as 907f43, checked the entire abstract
slice recurrence for $m=2,\ldots,8$, including $H^2r_0=+2a^2r_2$ and the sign
$(-1)^m$ in (8). The full retained pass-16 read was recorded as d640b7 and
d19ac7. No result from its separate geometric discussion or localized
countercontrol is needed for the theorem proved here.

No saved checker was executed, imported, or compiled. No canonical source
was changed. Independent saved-source review remains required before this
note is accepted into the canonical record.
