# An actual cusp frame can have a nonunit selected plinth

**Status: exact actual countercontrol to a raw selected-derivation shortcut.**

The generic conclusion161 does clear to a global invariant
\(h=aY-bX\) with \(N^2h=0\). It does not imply that the
selected leading derivation \(N\) has a polynomial slice.
The actual family below has the full cusp initial kernel,
a coordinate slice for the original action, and even a global
coordinate \(h\), but the plinth ideal of \(N\) is the
nonunit ideal \((P'(t))\).

This obstruction is entirely the content of the selected
derivation. Its primitive quotient is \(\partial_v\) and
does have a polynomial slice. Thus this family does not
disprove primitive-plinth descent, recognition by a different
derivation, or cancellation. Its invariant ring is already
explicitly polynomial.

## 1. What the generic affine conclusion really clears

First retain the arbitrary actual cusp hypotheses159/161.
Write \(a=EX\), \(b=EY\), \(\tau=b/a\), and
\(y=Y-\tau X\in A_a\), where \(A=\ker E\).
The selected derivation \(N\) fixes \(a,b\), and161 gives
\(N^2y=0\) in the generic localization. Consequently
\[
h:=aY-bX=ay\in A,\qquad
N^2h=0,\qquad c:=Nh\in S:=\ker_A N.
\tag{1}
\]
Indeed \(Eh=ab-ba=0\), and \(N^2h=aN^2y=0\)
in the localization. Since \(A\) is a domain and embeds
in that localization, the last identity holds in \(A\)
itself. No generic parameter has been declared polynomial.[^1]

If \(c\ne0\), equation (1) gives a genuine local slice
\(N(h/c)=1\) in \(A_c\). The elementary slice theorem
then gives \(A_c=S_c[h/c]\): apply the finite Taylor
projection associated with the locally nilpotent derivation
and its slice to each element of \(A_c\). If \(c\) is
a unit, this is already a global slice. If \(c=0\),
the element \(h\) is an invariant of \(N\), not a slice.
Equation (1) alone supplies neither the nonvanishing nor
the unit property of \(c\).

The next sections show that even the case \(c\ne0\),
with \(h\) a global coordinate, need not make the
plinth of the raw selected \(N\) a unit ideal.

## 2. A polynomial family and both inverse orders

Let \(P\in\mathbb C[t]\) have degree \(n\ge2\),
and start with independent coordinates \(x,t,p,v\).
On \(B=\mathbb C[x,t,p,v]\), take \(E=\partial_x\).
Define four polynomials
\[
\begin{gathered}
X=x,\qquad Y=v+P(t)x,\\
Z=p+3P(t)v^2+3P(t)^2vx+P(t)^3x^2,\\
W=t-v^3x+px^2,\qquad H:=XZ-Y^3=px-v^3.
\end{gathered}
\tag{2}
\]
This generalizes the retained zero-\(r\) frame160,
which is the degree-one case \(P(t)=t\).[^2]
The inverse is the following sequential polynomial formula:
\[
\begin{gathered}
x=X,\qquad t=W-X(XZ-Y^3),\qquad v=Y-P(t)X,\\
p=Z-3P(t)v^2-3P(t)^2vX-P(t)^3X^2.
\end{gathered}
\tag{3}
\]
In the forward order, the identity for \(H\) in (2)
recovers \(t\) from \(W-XH\), and then (3) recovers
\(v,p,x\). Conversely, start with independent
\(X,Y,Z,W\) and define \(x,t,v,p\) by (3).
The identities \(Y=v+P(t)X\) and the displayed formula
for \(p\) imply
\(XZ-Y^3=pX-v^3\). The defining identity
\(t=W-XH\) therefore gives \(W=t-v^3X+pX^2\).
The other three forward coordinates follow directly.
Both compositions are the identity, with no inversion of
\(X\), \(P\), or \(P'\).

Thus \(B=\mathbb C[X,Y,Z,W]=A[x]\), where
\(A=\mathbb C[t,p,v]\). The original action has the
actual coordinate slice \(X=x\), so it is free everywhere.
This is not a formal jet or merely a constant-Jacobian map.

## 3. The exact time profile, full initial kernel and field

The exact \(E\)-degrees and ordinary leading coefficients are
\[
\begin{gathered}
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
(a,b,e,d)=(EX,EY,E^2Z/2,E^2W/2)
 =(1,P(t),P(t)^3,p),\\
\ker\bigl(\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
 \longrightarrow A[\eta]\bigr)
 =(\mathsf X\mathsf Z-\mathsf Y^3),
\end{gathered}
\tag{4}
\]
where the map sends the four variables to
\(\eta,P(t)\eta,P(t)^3\eta^2,p\eta^2\), respectively.
For the kernel assertion, the fraction field of the initial
image contains \(\eta,P(t),p\), which are algebraically
independent. The image therefore has transcendence degree
three, and its kernel is a height-one prime. The displayed
cusp polynomial lies in that kernel and is irreducible:
view it as a primitive linear polynomial in \(\mathsf Z\)
over \(\mathbb C[\mathsf X,\mathsf Y,\mathsf W]\).
It consequently generates the full kernel, not only a
selected relation. All four indicated leading coefficients
are nonzero polynomials.

Section 4 will calculate \(S=\ker_A N=\mathbb C[t,p]\).
In particular the actual coefficient data are
\[
\begin{gathered}
L=\operatorname{Frac}S=\mathbb C(t,p),\qquad
\tau=P(t),\qquad \rho=p,\\
[L:\mathbb C(\tau,\rho)]=n,\qquad
y=v,\quad z=p+3\tau v^2,\quad w=t,\quad
\vartheta=-v^3,\quad k=0,\quad n_{159}=\rho,\quad r=0.
\end{gathered}
\tag{5}
\]
The notation \(n_{159}\) distinguishes the chart coefficient
from the integer \(n=\deg P\).
For the asserted field degree, the polynomial equation
\(P(t)-\tau=0\) gives degree at most \(n\).
The powers \(1,t,\ldots,t^{n-1}\) are independent over
\(\mathbb C(P(t),p)\). Otherwise clear denominators to
obtain \(\sum_{i=0}^{n-1}A_i(P(t),p)t^i=0\), with
\(A_i(T,p)\in\mathbb C(p)[T]\) not all zero.
The nonzero summands have distinct leading \(t\)-degrees
\(n\deg_T A_i+i\), so their largest term cannot cancel.
This proves the degree, and separability follows from
characteristic zero. No replacement of \(L\) by
\(\mathbb C(\tau,\rho)\) is made.

## 4. The actual selected partial and its full plinth

Let \(T=\partial_Z\) in the genuine coordinates
\(X,Y,Z,W\). Apply it to the inverse (3), holding
\(X,Y,W\) fixed. Since \(TH=X\), one obtains
\[
\begin{gathered}
Tx=0,\qquad Tt=-x^2,\qquad Tv=P'(t)x^3,\\
Tp=1+3v^2P'(t)x^2,\\
T|_A=\partial_p+x^2\{-\partial_t+3v^2P'(t)\partial_p\}
       +x^3P'(t)\partial_v,\qquad
N:=[x^3]T|_A=P'(t)\partial_v.
\end{gathered}
\tag{6}
\]
For \(Tp\), differentiate \(H=px-v^3\):
\(xTp-3v^2Tv=x\). Substitute the formula for \(Tv\)
and cancel the nonzero polynomial \(x\) in the domain.
The resulting identity holds on the whole polynomial ring,
including at \(x=0\); it is not only a localization formula.
The degree-three coefficient is nonzero because \(P'\ne0\).
It is exactly the selected leading derivation of159.

Because \(P'\) is nonzero and \(B\) is a domain,
\(Nf=0\) for \(f\in A\) is equivalent to
\(\partial_v f=0\). Hence its invariant ring, full
plinth ideal and the global cleared element are
\[
\begin{gathered}
S=\ker_A N=\mathbb C[t,p],\qquad
\operatorname{pl}(N):=N(A)\cap S=P'(t)S,\\
h=aY-bX=Y-P(t)X=v,\qquad Nh=P'(t),\qquad N^2h=0.
\end{gathered}
\tag{7}
\]
Indeed \(\partial_v:A\to A\) is surjective as a
\(\mathbb C\)-linear map, by termwise integration of
polynomials in \(v\). Thus \(N(A)=P'(t)A\), and
intersection with \(S\) is \(P'(t)S\) by comparing
the coefficients of powers of \(v\).
This computes the entire plinth, not a bounded-degree sample.

For \(\deg P\ge2\), \(P'\) is a nonconstant polynomial
and (7) is a proper ideal of \(S\). Therefore \(N\)
has no global polynomial slice. Its generic normalized
parameter \(v/P'(t)\) does satisfy \(N(v/P')=1\),
but is not in \(A\), since \(P'\) does not divide
the independent variable \(v\).
The generic statement161 is nevertheless exact:
\(y=v=P'(t)\{v/P'(t)\}\) is affine in that normalized
parameter, and the global \(h\) is itself a coordinate.

## 5. The limitation is raw content, not primitive descent

In the displayed polynomial coordinates of \(A\), the
content of \(N\) is \(P'(t)\). Dividing it out gives
\[
D:=N/P'(t)=\partial_v,\qquad Dv=1,
\qquad A=S[v].
\tag{8}
\]
Thus the example disproves the implication from an actual
cusp frame and \(N^2(aY-bX)=0\) to a unit plinth for
the raw selected \(N\), even when that cleared invariant
is a coordinate and \(E\) has a coordinate slice.
It does not disprove the corresponding assertion for a
primitive selected quotient. Nor does it realize a nontrivial
divisor residue field: all full fibers of \(A=S[v]\)
are already affine lines over their residue fields.

The parameter \(P\) can have arbitrary degree, and taking
\(P(t)=t^n\) gives plinth \((nt^{n-1})\). Degree one
recovers a unit \(P'\) and the original160 boundary.
Every member remains an explicitly recognized polynomial
kernel, so this is not a cancellation counterexample.

## Sources and verification scope

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md)
   and [nongraph exclusion161](cusp-nongraph-quartic-exclusion-pass161-working.md)
   supply the general statement cleared in (1).
2. [Zero-r cusp reduction160](cusp-zero-r-generic-graph-pass160-working.md),
   Section 4, supplies the degree-one seed generalized in (2).

All inverse, kernel, field-degree and plinth calculations for
this family are proved directly above. They require no new
classification theorem. Finite symbolic controls, if supplied
separately, do not prove the all-polynomial assertions.
This is a working deduction with AI reconstruction, not human
expert review, proof-assistant certification or a novelty claim.
No161 or earlier source is changed.

[^1]: Source 1, with all its actual-frame hypotheses. The extension of
\(N\) to the invariant localization is legitimate because \(Na=0\).
[^2]: Source 2. Only the specified degree-one family is being generalized.
