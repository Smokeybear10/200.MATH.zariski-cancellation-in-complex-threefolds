# Exact-field chain extraction and dense-frame recognition

**Status: complete working proof under the stated retained actual
dense-frame hypotheses, after independent saved-artifact reconstruction
of the new arbitrary-chain obstruction156.**
This note proves the exact formal-axis chain extraction needed for that
application. It uses repeated degree divisibility over the original
coefficient field, not an assumed descent of a plane automorphism.

Using that separately proved obstruction and the retained actual hypotheses,
every normalized dense three-good frame of fixed-good minimum
\(\mu\ge2\) has a graph as its generic embedded line. The retained
graph-recognition proof153 then gives a polynomial kernel.
This is a statement about the supplied coordinate profile.
Arbitrary entry into that profile and the full cancellation conjecture
remain unsolved. No154 or155 result is changed by this new156 work.

## 1. Actual inputs and the separate algebraic input

Retain the actual dense chart, minimizing shear and leading normalization:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX\ne0,\qquad
\deg_EW=m=\mu\ge2,\qquad d=m+1,\\
\text{the good speeds have rank two and dense homogeneous cone},\\
\tau=EY/s,\quad \rho=EZ/s,\quad
L/\mathbb C(\tau,\rho)\text{ finite separable},\\
A_L=L[v],\quad L[y,z]=L[v],\qquad
Y=y+\tau X,\quad Z=z+\rho X,\\
\ker(L[U,V]\longrightarrow L[v])=(g),\qquad
\Phi\in L^*g,\quad \deg\Phi=\deg g=d,\\
f_m=\gamma\tau^d,\qquad \Phi_d=-\gamma U^d,\qquad
\gamma\in\mathbb C^*,\\
\Psi(y,z)=v+\beta_0,\quad \beta_0\in L,\qquad
\Psi_U=\Phi_\tau,\quad \Psi_V=\Phi_\rho,\quad
\deg\Psi\le d .
\end{gathered}
\tag{1}
\]
These are the actual139/145/153 inputs.[^1]
In particular the whole first tail is associated with the generic
kernel, not merely divisible by its selected irreducible component.
The improved bound on \(\Psi\) uses the vanishing of its possible
degree-\(d+1\) term, a derivative of that order of \(f_m\).
The coefficient partial \(\partial_\tau\) is a derivation of the
exact finite separable field \(L\).
The ratios \(\tau,\rho\) are algebraically independent over
\(\mathbb C\), as part of the actual dense chart.

The additional, separately proved input is the following
differential-field obstruction, denoted \(\mathsf{Chain}\).
For a characteristic-zero field \(F\) with a derivation \(\delta\),
extended to fix formal \(U,V\), take \(n\ge3\) and polynomials
\(\mathcal A_i\in F[T]\), each of degree at least two. Set
\[
\begin{gathered}
P_0=U,\qquad P_1=V-\mathcal A_1(U),\\
P_i=P_{i-2}-\mathcal A_i(P_{i-1})\quad(2\le i\le n-1),\\
G=\mathcal A_n(P_{n-1})+\lambda P_{n-2}+\nu,\qquad
\lambda\in F^*,\quad \nu\in F .
\end{gathered}
\tag{2}
\]
The input \(\mathsf{Chain}\) states that there are no
\(\alpha\in F^*,\beta,c\in F\) with
\(\delta G=\partial_U(\alpha P_{n-1}+\beta+cG)\).
The new [arbitrary-chain proof156](arbitrary-chain-gradient-obstruction-pass156-working.md)
provides exactly this assertion.
No part of its proof, including its leading-coefficient gate, is
silently assumed to follow from the extraction argument below.

## 2. The exact-field degree-reduction step

The classical AMS degree theorem is used only in its following form:
for two nonconstant polynomials generating \(F[v]\) in characteristic
zero, one of their degrees divides the other. The statement holds
over the field \(F\) itself, without algebraic closure.[^2]

Suppose \(p,q\in F[v]\), \(F[p,q]=F[v]\), and
\(1<a:=\deg p<b:=\deg q\).
There is a polynomial \(C\in F[T]\) with
\[
\deg C=b/a\ge2,\qquad
0<\deg(q-C(p))<a,\qquad F[p,q-C(p)]=F[v].
\tag{3}
\]
Here \(a\mid b\) by AMS. More explicitly, start with residual \(q\).
While its degree \(D\) is at least \(a\), AMS gives \(a\mid D\).
Subtract a scalar multiple of \(p^{D/a}\) with the same leading
coefficient. The scalar is a ratio of two nonzero coefficients
in \(F\), so this takes neither a field extension nor a root.
Each subtraction lowers \(D\) strictly and preserves the generated ring.

The residual cannot become constant, because that would give
\(F[v]=F[p]\), impossible when \(\deg p>1\).
Eventually (3) holds. The first subtraction has power \(b/a\)
and nonzero coefficient; later subtractions use smaller powers.
Thus the degree of the total polynomial \(C\) is exactly \(b/a\).
The procedure is finite by the strict decrease of positive integers.
It proves (3) using only repeated applications of the stated AMS input.

## 3. Extraction of a finite alternating chain in the fixed axes

The pure leading form and exact implicit-degree equality in (1)
give the same fixed-axis degrees as in graph-recognition153:
\[
\deg_v z=d,\qquad 0<e_0:=\deg_v y<d .
\tag{4}
\]
The unique point at infinity is \([0:1:0]\).
If \(y\) were constant, the implicit equation would have degree one,
contrary to \(d\ge3\). No coefficient-dependent affine change
of \(U,V\) is used to obtain (4).

If \(e_0=1\), the graph case is already reached.
Otherwise apply (3) over \(F=L\), first with \(p=y,q=z\).
This produces \(\mathcal A_1\in L[T]\) of degree at least two
such that the evaluated polynomial
\(P_1(y,z)=z-\mathcal A_1(y)\) has positive degree \(e_1<e_0\).
Use the same formal notation \(P_0=U,P_1=V-\mathcal A_1(U)\).

If \(e_1>1\), apply (3) again, now to the smaller
\(P_1(y,z)\) and larger \(P_0(y,z)\). Continue this way.
The current formal recurrence and generic degrees are
\[
P_i=P_{i-2}-\mathcal A_i(P_{i-1}),\qquad
e_i:=\deg_v P_i(y,z),\qquad
0<e_i<e_{i-1},\qquad \deg\mathcal A_i\ge2.
\tag{5}
\]
The evaluated adjacent pair always generates \(L[v]\).
Strictly decreasing positive degrees eventually give a linear
parameter \(P_{n-1}(y,z)\), for some \(n\ge2\):
\[
P_{n-1}(y,z)=a v+b,\quad a\in L^*,\ b\in L,\qquad
e_{n-2}>1 .
\tag{6}
\]
Indeed if the current smaller degree remained greater than one,
another application of (3) would decrease it.
All coefficients of every \(\mathcal A_i\) belong to the same \(L\).

Each recurrence is also an invertible formal-plane step:
from \((P_{i-1},P_i)\), recover
\(P_{i-2}=P_i+\mathcal A_i(P_{i-1})\).
Together with \(V=P_1+\mathcal A_1(P_0)\), this gives
\(L[U,V]=L[P_{n-2},P_{n-1}]\).
This is a formal description of a polynomial relation in the
original \(U,V\), not an original four-ring coordinate change.

## 4. The literal first tail and its canonical complement

Since the final evaluated parameter in (6) is linear in \(v\),
there is \(B_n\in L[T]\) of degree \(e_{n-2}\ge2\) such that
\(P_{n-2}(y,z)=B_n(P_{n-1}(y,z))\).
The whole generic kernel is therefore generated by
\(P_{n-2}-B_n(P_{n-1})\). Association in (1) gives a scalar
\(\lambda\in L^*\) with
\[
\begin{gathered}
\Phi=\lambda\{P_{n-2}-B_n(P_{n-1})\}
 =\mathcal A_n(P_{n-1})+\lambda P_{n-2}+\nu,\\
\mathcal A_n=-\lambda B_n,\qquad \nu=0,\qquad
\deg\mathcal A_n\ge2 .
\end{gathered}
\tag{7}
\]
Allowing a separate constant \(\nu\) is harmless, but unnecessary
for this extraction. The equation is exactly in the original formal
axes, with all coefficient partials still interpreted there.

Write \(a_i=\deg\mathcal A_i\) and
\(D_i=\deg_{U,V}P_i\), to distinguish formal-plane degree from
the generic \(v\)-degrees \(e_i\).
The formal recurrence gives
\(D_0=1,\ D_i=\prod_{j=1}^i a_j\) for \(i\ge1\):
the term \(\mathcal A_i(P_{i-1})\) has strictly larger
degree than \(P_{i-2}\). The same comparison in (7) gives
\[
d=\deg\Phi=\prod_{j=1}^n a_j,\qquad
\deg_{U,V}P_{n-1}=d/a_n<d .
\tag{8}
\]
There is no cancellation of these leading terms because every
\(a_i\ge2\) and every leading coefficient is nonzero in \(L\).

Now (1) and (6) show that
\(\Psi-\alpha P_{n-1}-\beta\) belongs to \((\Phi)\), where
\(\alpha=a^{-1}\ne0\) and \(\beta=\beta_0-a^{-1}b\).
Using \(\deg\Psi\le d\) and (8), its quotient by \(\Phi\)
has degree at most zero. Consequently
\[
\Psi=\alpha P_{n-1}+\beta+c\Phi,\quad
\alpha\in L^*,\ \beta,c\in L,\qquad
\partial_\tau\Phi=\partial_U\Psi .
\tag{9}
\]
This proves the exact second-tail gate.
A generic quotient parameter alone would not supply the degree bound
or the coefficient-gradient identity used here.

## 5. The dense-frame recognition implication

For \(n=2\), equation (7) has exactly the fixed-axis two-stage form
\(\mathcal A_2(V-\mathcal A_1(U))+\lambda U+\nu\).
The retained [two-stage exclusion154](two-stage-nongraph-continuation-pass154-working.md)
rules it out under the actual hypotheses (1).

For \(n\ge3\), use the separately stated input \(\mathsf{Chain}\)
with \(F=L,\delta=\partial_\tau\).
Equations (7) and (9) supply every algebraic hypothesis of that
obstruction, including the actual coefficient derivatives.
It rules out this case as well.

Therefore the nongraph
assumption \(e_0>1\) is impossible. The normalized generic line
has \(\deg_v y=1\).
The retained [graph-correction proof153](dense-all-degree-graph-correction-pass153-working.md)
and its [normalized-suspension endpoint](normalized-suspension-recognition-pass153-working.md)
then construct actual polynomial generators of \(A\), so
\(A\simeq\mathbb C^{[3]}\).

This implication uses actual coordinate changes only where they
are proved in the retained normalization and graph arguments.
The intermediate formal-plane steps (5) merely identify the
literal equation to which a coefficient-gradient obstruction applies.

## 6. Scope and review boundary

The AMS extraction, formal degree comparison, and canonical
complement gate are proved here from the stated inputs.
The arbitrary-chain obstruction itself is a distinct new156
proof, independently reconstructed from its complete saved artifact.
The resulting recognition theorem retains all actual hypotheses in (1)
and the explicitly cited historical inputs. The new saved-file reviews
are not a fresh recursive audit of every historical dependency.

This is not a claim that an arbitrary sliced action admits three
good polynomial coordinates. Other original profiles, arbitrary
entry, and the full cancellation conjecture remain unresolved.
The older low-minimum cases are separate retained results;
this argument has stated its range \(m=\mu\ge2\).

There is no historical novelty clearance, human expert review,
formal proof-assistant certification, or new universal conclusion
based only on finite computations. All154 and155 checkpoints
and their claims remain unchanged.

## Sources and exact inputs

1. [Actual chart139](dense-all-degree-taylor-chart-pass139-working.md),
   [exact generic degrees139](dense-generic-embedded-line-pass139-working.md),
   [first-tail primitivity145](common-gauss-integrality-tail-primitivity-pass145-working.md),
   and [leading normalization153](dense-all-degree-leading-normalization-pass153-working.md).
   These supply exactly (1) and (4), including the literal first
   tail and unchanged original formal axes.
2. Leonid Makar-Limanov,
   [*A new proof of the Abhyankar-Moh-Suzuki Theorem*](https://arxiv.org/pdf/1212.0163v1),
   AMS Theorem, printed p. 1. Its characteristic-zero statement
   over the exact coefficient field was freshly read.
   Only the two-degree divisibility result is imported;
   the repeated extraction and its field control are proved here.
3. [Arbitrary-chain obstruction156](arbitrary-chain-gradient-obstruction-pass156-working.md).
   This is the separately proved input \(\mathsf{Chain}\), not a
   consequence silently borrowed from the three-stage special case.
4. [Two-stage exclusion154](two-stage-nongraph-continuation-pass154-working.md)
   and [graph recognition153](dense-all-degree-graph-correction-pass153-working.md),
   with [normalized suspension153](normalized-suspension-recognition-pass153-working.md).
   These are respectively the \(n=2\) obstruction and the actual
   polynomial-kernel endpoint, not formal-plane coordinate claims.

[^1]: Source 1, with its retained full chart and normalization hypotheses.
[^2]: Source 2; see the exact-field proof of the reduction step.
