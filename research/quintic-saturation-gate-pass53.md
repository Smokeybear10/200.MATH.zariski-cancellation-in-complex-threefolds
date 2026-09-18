# The exact saturation obligation for the quintic algebra

A principal fifth image and a free module \(F_5\) do not establish
generation of the actual intrinsic ring. For the intermediate algebra
\(K_5=R[F_5]\), the precise remaining condition is that the base
parameters remain a regular sequence on the entire algebra, including
its products. Under the already proved divisor equalities, that
condition is equivalent to \(K_5=\mathcal A\).

This is an exact application of the earlier conic and height-one
intersection arguments. It is not a new general classification result,
a proof of the needed regularity, or another finite generation claim.

## 1. Arbitrary intermediate algebras with the actual divisor charts

Let \(R=C_{\mathfrak m}\) be the actual regular local surface
ring, with maximal ideal \(\mathfrak n=(a,b)\), fraction field
\(L\), and faithfully flat actual domain
\(\mathcal A=A\otimes_C R\). Consider any intermediate
\(R\)-subalgebra
\[
R\subseteq K\subseteq\mathcal A
\quad\text{such that}\quad
K_{(\pi)}=\mathcal A_{(\pi)}
\text{ for every height-one prime }(\pi)\subset R.
\tag{1}
\]
The equalities are of embedded algebras. They also imply
\(K_L=\mathcal A_L\). No finite-generation assumption on the
\(R\)-module \(K\) or on \(\mathcal A/K\) is made.

The exact criterion is
\[
\boxed{
K=\mathcal A
\quad\Longleftrightarrow\quad K\text{ is flat over }R
\quad\Longleftrightarrow\quad
(a,b)\text{ is a regular sequence on }K.
}
\tag{2}
\]
The first condition implies the second by actual flatness, and the
second implies the third by tensoring the regular sequence on \(R\).
Also \(\mathfrak nK\ne K\), since \(1\notin\mathfrak n\mathcal A\).
Thus regularity here does not permit a vacuous unit-ideal case.

## 2. The powers argument does not require a finite quotient module

Assume \((a,b)\) is regular on \(K\), and take \(x\in\mathcal A\).
Let \(I\) be the annihilator in \(R\) of the single class
\([x]\in\mathcal A/K\). The cyclic submodule it generates is
\(R/I\), hence is finite even if the whole quotient is not.

At every height-one prime its class vanishes by (1), and it
vanishes generically too. A two-dimensional local domain has no
remaining prime other than \(\mathfrak n\). Hence either
\(I=R\), when \(x\in K\) already, or
\(\sqrt I=\mathfrak n\). In the latter case some power of
\(\mathfrak n\) is contained in \(I\), so for a common \(N\ge1\),
\[
u=a^Nx\in K,\qquad v=b^Nx\in K,\qquad
b^Nu=a^Nv.
\tag{3}
\]

Regularity of \((a,b)\) implies that \(b^N\) is a
nonzerodivisor on \(K/a^NK\). For clarity this fact does
not require finite generation. If \(by\in a^jK\), reduction
modulo \(a\) gives \(y=ay_1\); cancellation of the
nonzerodivisor \(a\) reduces the assertion to
\(by_1\in a^{j-1}K\). Induction proves
\(y\in a^jK\). Thus \(b\), and then each power of \(b\),
is a nonzerodivisor on every \(K/a^jK\).

Apply this to (3). It gives \(u\in a^NK\), say
\(u=a^Nk\) with \(k\in K\). The actual domain then permits
cancellation from \(a^Nx=a^Nk\), proving \(x=k\in K\).
This proves the nontrivial implication in (2).

There is an equivalent explicit failure witness. If \(K\ne\mathcal A\),
one nonzero cyclic class has an \(\mathfrak n\)-primary annihilator.
Taking a nonzero socle element of that finite-length cyclic module
gives an \(x\in\mathcal A\setminus K\) with \(ax,bx\in K\).
Then \(ax\notin aK\), but
\[
b(ax)=a(bx)\in aK.
\tag{4}
\]
Thus \(b\) is a zerodivisor on \(K/aK\). Conversely such a
failure is impossible if \(K=\mathcal A\), by actual flatness.
This witness concerns the full intermediate algebra, not only
its named low-degree generators.

## 3. Application to the complete fifth filtration algebra

In the actual reduced zero-first-jet sector, the
[quartic algebra proof](quartic-fiber-gate-pass52.md) gives
\(K_4=R[F_4]\subset\mathcal A\) and all the divisor equalities
in (1). Therefore \(K_5=R[F_5]\), and indeed any algebra
between \(K_4\) and \(\mathcal A\), satisfies (1).

The separate [quintic construction](quintic-correction-pass53.md) supplies
\(I_5=p^3R\) and \(F_5=F_4\oplus RY\). These identify the
full finite filtration module and its image. They do not show
that products of its members satisfy the cancellation condition
in Section 2. Freeness of \(F_5\) is not an application of
criterion (2) to \(R[F_5]\): the named finite module and its
generated algebra are different objects. No counterexample to
a possible further generation theorem is being asserted.

To prove actual generation by the quintic layer it would suffice,
and by (2) is necessary, to establish that \(b\) acts injectively
on \(K_5/aK_5\). Equivalently, one must exclude the missing
actual elements described in (4). The principal image alone
does not do that. No conclusion here selects whether \(K_5\)
equals \(\mathcal A\).

## 4. Deduplication and limits

The [pass47 flat-conic gate, Section 2](flat-conic-topology-gate-pass47.md)
already proves that a flat module over the invariant UFD equals
its embedded height-one intersection. The
[pass46 minimal-slice note, Section 6](minimal-quadratic-slice-pass46.md)
proves the actual ring's intersection by prime-denominator
cancellation. Passes 48, 51 and 52 use those same local-to-global
ideas for specific cubic or quartic presentations.

The present note isolates the equivalent two-parameter test for
an arbitrary intermediate algebra in this local surface situation.
The powers and cyclic-annihilator proof spells out why no
finite-generation assumption on \(\mathcal A/K\) is needed.
Its role is a precise generation obligation for the full quintic
algebra, not a new freeness theorem or a universal-frame argument.
No new numeric suite, historical novelty claim, or mutation of
files from passes 52 and earlier is made.
