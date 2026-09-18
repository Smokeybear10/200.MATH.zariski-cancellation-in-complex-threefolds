# Quadratic divisor filtration: an exact conic control

For an explicit quadratic constant-extension conic, the entire
degree filtration can be computed, not merely guessed from the
first few derivative orders. Its jth image has valuation
e times ceil(j/2). The calculation is a control for the actual
DVR classification pursued separately, not a proof that every
actual divisor admits this presentation.

Two contrasting families identify relevant hypotheses. Multiplying
the derivation by the uniformizer changes the valuation while
preserving the conic ring, but kills its special-fiber action.
A cubic constant extension can have a smooth flat primitive model
with no nonconstant second-degree residue; its valuation sequence
is different. Neither is a counterexample preserving all the
quadratic actual-divisor hypotheses.

## 1. The explicit quadratic constant extension

Let k=C(s), V=k[p]_(p), and K=k(p). For any integer e>=1 set
\[
\begin{gathered}
B_e=V[r,t]/(p^e t-r^2-s),\qquad
N(r)=p^e,\quad N(t)=2r,\quad N|_V=0,\\
(B_e)_K=K[r],\qquad
N|_{K[r]}=p^e\partial_r,\qquad
B_e/pB_e=k[r]/(r^2+s)[t].
\end{gathered}
\tag{1}
\]
The polynomial r^2+s is irreducible over C(s): a square cannot
have odd s-adic valuation. Thus the special fiber is a polynomial
line over the quadratic extension k'=k(sqrt(-s)).

The displayed presentation injects into K[r] by t=(r^2+s)/p^e.
Indeed it is monic in r, so each element has a unique expression
A(t)+rB(t) with A,B in V[t]. Distinct terms t^i and rt^i
have distinct degrees 2i and 2i+1 after this substitution.
Consequently a nonzero expression cannot map to zero.

The derivation preserves the defining relation and is locally
nilpotent after this injection. The ring is V-flat, being free
over V[t] and therefore free over V. The relative partial
derivatives p^e and -2r generate the unit ideal: the relation
expresses the unit s as p^e t-r^2. The hypersurface is therefore
smooth over the regular DVR and is regular itself. The same
unit-ideal calculation applies to the two values N(r),N(t), so
N is fixed-point-free on this intrinsic ring. On the special
fiber its action is 2r partial_t, a nonzero translation over k'.

## 2. Full modules and image ideals for every degree

Let F_j=ker(N^(j+1)|B_e). Unique monic normal forms and the
distinct leading degrees used above prove
\[
\begin{gathered}
F_j=
\bigoplus_{\,2i\le j} Vt^i
\ \oplus
\bigoplus_{\,2i+1\le j} Vrt^i,\\
\operatorname{rank}_V F_j=j+1,\qquad
\ker(N|B_e)=V.
\end{gathered}
\tag{2}
\]
This is an arbitrary-element statement: terms of different
displayed degrees cannot cancel, so membership in F_j is
equivalent to the indicated finite truncation. It does not
follow merely from generic linear independence of a proposed
list or from a finite collection of test elements.

For j=2i or 2i+1, only the unique basis element of degree j
can contribute to N^j F_j. Its leading term and the generic
operator in (1) give
\[
\begin{gathered}
N^{2i}(t^i)=(2i)!\,p^{ei},\qquad
N^{2i+1}(rt^i)=(2i+1)!\,p^{e(i+1)},\\
I_j:=N^jF_j
 =j!\,p^{e\lceil j/2\rceil}V
 =p^{e\lceil j/2\rceil}V,\qquad
v_p(I_j)=e\lceil j/2\rceil .
\end{gathered}
\tag{3}
\]
For j=0 this means I_0=V. The factorials are units because the
coefficient field has characteristic zero. The first valuations
are 0,e,e,2e,2e,3e,3e,4e,4e. In particular t is a genuine
second-degree element with nonconstant special-fiber residue;
this is an actual algebra element, not a formal local coordinate.
Although N has no fixed point, I_1=p^eV shows that it has no
slice with derivative one in B_e. This is compatible with the
nontrivial residue constant extension.

The same proof applies to any DVR V containing Q, uniformizer p,
and unit d in V such that r^2+d has irreducible residue: replace
s by d throughout (1)--(3). No coefficient-field lift is needed
for the monic normal form or the generic degree calculation.
Containing Q, rather than only having fraction-field
characteristic zero, makes every displayed factorial a unit.

## 3. The derivation's primitivity matters

On exactly the same ring replace N by N_h=p^hN for an integer
h>=1. The degree kernels are unchanged since the ring is a
domain, but the derivative images are
\[
\ker(N_h^{j+1})=F_j,\qquad
N_h^j F_j=p^{hj+e\lceil j/2\rceil}V.
\tag{4}
\]
The special-fiber action of N_h is zero, and its value ideal
is p^hB_e rather than the unit ideal. Thus an assertion of (3)
from a conic presentation alone must also normalize the actual
derivation. The replica is not a counterexample to a theorem
requiring a primitive, nonzero special-fiber derivation.

## 4. Omitting the quadratic constant-field gate

For comparison, keep the same V and define the cubic family
\[
\begin{gathered}
C_e=V[r,t]/(p^e t-r^3-s),\qquad
M(r)=p^e,\quad M(t)=3r^2,\\
C_e/pC_e=k[r]/(r^3+s)[t],\qquad
[C(s)(\sqrt[3]{-s}):C(s)]=3.
\end{gathered}
\tag{5}
\]
The cubic is irreducible since a reducible cubic has a root
and s has valuation one, not divisible by three.
Monic normal form gives basis 1,r,r^2 over V[t]. Its distinct
generic degrees again prove injection, local nilpotence and
the complete filtration. The relative partials p^e,3r^2
generate the unit ideal, so this is also a smooth flat intrinsic
model with nonzero primitive special-fiber action.

Writing j=3i+k with 0<=k<3 gives
\[
\begin{gathered}
\ker(M^{j+1})=
 \bigoplus_{\,3i+k\le j,\ 0\le k<3}Vr^kt^i,\\
M^j(r^kt^i)=j!\,p^{e(j-i)},\qquad
v_p\big(M^j\ker(M^{j+1})\big)
 =e\big(j-\lfloor j/3\rfloor\big).
\end{gathered}
\tag{6}
\]
In particular every second-degree residue lies in the constant
field k'=k[r]/(r^3+s), while the first nonconstant residue t has
degree three. At j=3 the image valuation is 2e, but at j=4 it
is 3e, unlike the quadratic value 2e.

This example isolates a limitation, not an unproved
classification counterexample: it changes the constant-field
degree from two to three. It proves that a generic polynomial
line, smooth base-flat algebra and primitive LND do not alone
give the quadratic formula or a nonconstant F_2 residue.
It does not disprove those conclusions after the actual
quadratic constant-field hypothesis is restored. No example
retaining all those hypotheses but violating (3) is asserted.

## 5. Finite checks and source scope

The standalone
[checker](quadratic_divisor_filtration_checks_pass107.py)
has one method. For e=1,...,4 and j=0,...,8 it checks the
quadratic monic normal forms, generic coefficient ranks,
successive derivatives and the exact nonzero leading image.
The same method checks finite replica and cubic contrasts.
The finitely many computations do not prove the all-j module
description or classify actual divisor rings.

The first assertion-bearing author execution used
`/opt/anaconda3/bin/python research/quadratic_divisor_filtration_checks_pass107.py`.
Its one method passed in 1.018 unittest seconds, exit zero
(start chunk 3be311, completion chunk 309b20). Those two output
chunks do not supply an end-to-end process wall-time measurement.

The proofs above use only the written monic-basis and
derivative calculations, together with the standard smooth
hypersurface criterion for the stated regularity observation.
No new primary-source proof read, actual original four-variable
frame, general conic-generation theorem or cancellation
conclusion is claimed. All files through106 remain unchanged.
