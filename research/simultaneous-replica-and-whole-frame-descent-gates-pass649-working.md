# Two exact tests for nonlinear frame repair

Date: September 18, 2026.

Two proposed repairs of a rank-one-leading ambient coordinate frame fail
for different reasons. First, adding individually valid invariant replicas
can cancel all positive slice degrees and give a tangent, divergence-free
field commuting with the sliced action, without giving an LND. Second,
an actual elementary coordinate change can lower the selected partial's
degree while increasing the whole frame's height and descending sorted
degree tuple. Both controls take place on actual polynomial cylinders.
Neither is a cancellation counterexample or an obstruction to all repairs.

Here an LND is a locally nilpotent derivation. On
\(B=A[u]=\mathbb C[a,b,c,u]\), the filtration shift of a polynomial
derivation is the maximum of the \(u\)-degrees of its horizontal
coefficients and the degree of its vertical coefficient minus one.
Zero coefficients are ignored. For the fields below this equals their
highest nonzero horizontal degree \(q\). The frame height is
\(H=\sum_i(q_i+1)\), not the ordinary degree of a coordinate map.

## 1. Exact descent does not certify a sum's local nilpotence

Start in \(B=\mathbb C[x,y,z,t]\), and put
\[
 \ell=x+y-2z,\qquad
 E=\ell(\partial_x-\partial_y)+\partial_t.
 \tag{1}
\]
The derivation fixes \(\ell\), sends \(t\) to one, and is LND.
The following is a whole polynomial coordinate change:
\[
 a=x-t\ell,\quad b=y+t\ell,\quad c=z,\quad u=t.
 \tag{2}
\]
Writing \(L=a+b-2c\), its inverse is
\[
 x=a+uL,\quad y=b-uL,\quad z=c,\quad t=u.
 \tag{3}
\]
Both compositions are the identity, since \(\ell=L\) under either
substitution. In these coordinates \(E=\partial_u\) and
\(A=\ker E=\mathbb C[a,b,c]\).

Let \(T_x,T_y,T_z,T_t\) be the four ORIGINAL coordinate partials.
Their entire expressions, including the vertical components, are
\[
\begin{aligned}
 T_x&=(1-u)\partial_a+u\partial_b,\\
 T_y&=-u\partial_a+(1+u)\partial_b,\\
 T_z&=2u\partial_a-2u\partial_b+\partial_c,\\
 T_t&=-L\partial_a+L\partial_b+\partial_u.
\end{aligned}
\tag{4}
\]
They are commuting coordinate LNDs and their coefficient determinant
is one. Set \(D_0=-\partial_a+\partial_b\). Their shifts are
\((1,1,1,0)\), with intrinsic leading coefficients
\[
 D_0,\quad D_0,\quad -2D_0,\quad LD_0.
 \tag{5}
\]
Since \(D_0(L)=0\), every primitive top in this displayed frame is
\(D_0\) up to a nonzero constant. This assertion is about the four
displayed partials, not every constant combination of them.

Consider the three replicas
\[
\begin{aligned}
 U&=-(y+z)T_x=(uL-b-c)T_x,\\
 V&=-(x+z)T_y=(-uL-a-c)T_y,\\
 W&=-(x+y)T_z=-(a+b)T_z.
\end{aligned}
\tag{6}
\]
Each multiplier is killed by its OWN original coordinate partial.
Thus each replica is an LND: its flow is the corresponding coordinate
translation by the multiplier times an independent action parameter.
This is an entire polynomial flow, not a leading-symbol certificate.

Their degrees and intrinsic tops are
\[
\begin{array}{c|c|c}
 &q&\text{intrinsic top}\\ \hline
 U&2&LD_0\\
 V&2&-LD_0\\
 W&1&2(a+b)D_0.
\end{array}
\tag{7}
\]
The degree-two terms in \(U+V\) cancel. Its remaining degree-one
top is \(-2(a+b)D_0\), which cancels with the top of \(W\).
Substitution in (4) gives the whole sum
\[
 S=U+V+W
   =-(b+c)\partial_a-(a+c)\partial_b-(a+b)\partial_c.
 \tag{8}
\]
In particular,
\[
 S(u)=0,\qquad [S,E]=0,\qquad
 \operatorname{div}_{da\,db\,dc\,du}S=0.
 \tag{9}
\]
But \(S(a-b)=a-b\), so \(S^n(a-b)=a-b\ne0\) for every
\(n\ge1\). Therefore \(S\) and its restriction to \(A\) are
NOT locally nilpotent. Valid replicas, complete leading cancellation,
slice tangency, exact commutation with \(E\), and volume preservation
together still fail to certify the required additive action.

### A successful repair on the same example

The example does not obstruct simultaneous repair. The following
combinations of the same original partials are exactly
\[
\begin{aligned}
 P_a&=(1+u)T_x-uT_y=\partial_a,\\
 P_b&=uT_x+(1-u)T_y=\partial_b,\\
 P_c&=-2uT_x+2uT_y+T_z=\partial_c.
\end{aligned}
\tag{10}
\]
Every multiplier here depends only on \(u=t\), which all three
active original partials kill. The summands therefore commute and
their sums are LNDs. Alternatively (3) proves the entire identities.
These give three independent intrinsic translations commuting with
\(E\). Thus an additional valid nilpotence certificate succeeds here.
No such choice is proved to exist on an unknown stable factor.

## 2. A selected-row decrease need not decrease a whole coordinate frame

For any integer \(M\ge4\), start with the actual frame
\[
 (X_1,X_2,X_3,X_4)
   =(a,b,c+u^M+(a+b)u,u)
 \tag{11}
\]
on \(B=\mathbb C[a,b,c,u]\), with \(E=\partial_u\).
Its inverse recovers \(a=X_1,b=X_2,u=X_4\) and
\(c=X_3-X_4^M-(X_1+X_2)X_4\). Its coordinate partials are
\[
\begin{aligned}
 T_1&=\partial_a-u\partial_c,&
 T_2&=\partial_b-u\partial_c,\\
 T_3&=\partial_c,&
 T_4&=E-(Mu^{M-1}+a+b)\partial_c.
\end{aligned}
\tag{12}
\]
The shift tuple is \((1,1,0,M-1)\), and all intrinsic tops are
constant multiples of \(\partial_c\).

Make the genuine elementary coordinate change
\[
 X_3'=X_3+P,\qquad
 P=-X_4^M+X_1X_4^{M-1},\qquad X_i'=X_i\ (i\ne3).
 \tag{13}
\]
Since \(P\) omits \(X_3\), its inverse is subtraction of \(P\).
The entire new frame is
\((a,b,c+(a+b)u+au^{M-1},u)\). Its inverse subtracts
\((X_1+X_2)X_4+X_1X_4^{M-1}\) from \(X_3'\).

For \(i\ne3\) the new partial is
\(T_i'=T_i-(T_iP)T_3\), while \(T_3'=T_3\). Explicitly,
\[
\begin{aligned}
 T_1'&=\partial_a-(u+u^{M-1})\partial_c,\\
 T_2'&=T_2,\qquad T_3'=T_3,\\
 T_4'&=E-(a+b+(M-1)au^{M-2})\partial_c.
\end{aligned}
\tag{14}
\]
All four are commuting coordinate LNDs. The selected subtraction
uses \(f=T_4P=-Mu^{M-1}+(M-1)au^{M-2}\), with \(T_3f=0\).
It genuinely decreases the fourth shift from \(M-1\) to \(M-2\).
However the mandatory first companion row increases from one to
\(M-1\). The full tuples and heights are
\[
\begin{aligned}
 (q_i)&=(1,1,0,M-1),& H&=M+5,\\
 (q_i')&=(M-1,1,0,M-2),& H'&=2M+2.
\end{aligned}
\tag{15}
\]
Thus \(H'-H=M-3>0\). The descending sorted tuple increases
lexicographically from \((M-1,1,1,0)\) to
\((M-1,M-2,1,0)\). These identities hold for every \(M\ge4\).
There is no nilpotence or invertibility failure here. The failure is
the inference from a selected row's descent to whole-frame descent.

Again another shear works: choosing only \(P_0=-X_4^M\) gives
shifts \((1,1,0,0)\), lowering the height to six. The control
does not exclude better choices or prove a local minimum.

## 3. Relation to the existing exact gates

[Coordinate-frame minimization](coordinate-frame-minimization-pass.md),
Section 4, already requires the derivative-integrability identities
and degree nonincrease for EVERY changed partial. Section 2 above
is an explicit all-degree control for omitting that latter premise,
not a refutation of the stated sufficient criterion.

[Pass25](commuting-leading-pass25.md) and
[pass26](simultaneous-frame-pass26.md) already distinguish an actual
coordinate operation from an arbitrary polynomial row combination.
Pass26's two-column completion requires an LND in addition to
commutation and unimodularity. Section 1 above tests a different
proposed substitute: certifying the summands individually and then
checking exact descent of their sum. That substitute fails.

[Pass643](primitive-leading-fixed-locus-frame-obstruction-pass643-working.md)
and [pass644](slice-scaling-root-extraction-closure-pass644-working.md)
leave nonlinear recombination outside their extraction obstruction.
The present controls do not close that remaining route. They require
both whole local-nilpotence verification and a whole-frame degree
comparison, rather than permitting either to be inferred from
leading cancellation alone. No literature novelty is claimed.

## 4. Verification and remaining objective

The displayed inverses and identities give complete written proofs.
Jet's fresh unsaved check05ad51 reconstructed (2)--(9), the whole
original frame, every ordered frame bracket, its determinant, and
the successive degrees and tops. Root independently checked those
identities and (10) in fresh unsaved d860c4. The same root calculation
checked (12)--(15), all new brackets and determinants for
\(M=4,\ldots,9\). The uniform claim follows from the formulas,
not from these finite parameter checks. No saved checker was run.

General and Jet subsequently read all237 saved lines at SHA256
2e70dd5fe9dc8269c0375246ca95483fcd5537e9e349dc1bf6a85784b67b4a1f
and reported CLEAN. Their full EOF reads were03b714 andb60f10;
final unchanged hash checks wereea11c1 andbc9648. General's fresh
dac065 and7dea07 and Jet's fresh26ae02 separately checked the
complete controls and positive repairs. These are internal AI-assisted
checks, not expert review or formal proof certification.
The working cancellation implication
\(A[u]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\)
remains UNSOLVED. The next obligation is existence of a successful
global action or frame repair on the actual unknown base, not another
calculation on a base whose polynomial coordinates were supplied.
