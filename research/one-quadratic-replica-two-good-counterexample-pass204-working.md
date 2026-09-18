# A two-good frame defeating every single-replica last-slot correction

Status: explicit all-parameter counterexample to one fixed last-slot
ansatz. For the actual two-good sliced frame below, no polynomial
parameter invariant under \(D_0=X\partial_Z+Z\partial_W\) makes
\(W_J-PZ_J-Q\) invariant, with \(P,Q\in\mathbb C[X,Y]\).
This does not prevent another transformed coordinate from being
invariant: choosing \(J=X\) already makes \(Z_J=Z-X^2\) invariant.
The example has a coordinate slice and a polynomial kernel. It is
not an obstruction to obtaining any invariant coordinate, a
counterexample to cancellation, or a failure of general composite flows.

## 1. Actual frame, inverse, and exact time degrees

Start with independent variables \(u,v,g,w\), and put
\[
\begin{gathered}
B=\mathbb C[u,v,g,w],\qquad E=\partial_u,\\
X=u,\qquad Y=v+gu,\qquad Z=g+u^2,\qquad
W=w+(g+u^2)^4.
\end{gathered}
\tag{1}
\]
These are actual polynomial coordinates, with inverse
\[
u=X,\qquad g=Z-X^2,\qquad
v=Y-X(Z-X^2),\qquad w=W-Z^4.
\tag{2}
\]
Substitution of (1) into (2) returns \(u,g,v,w\).
Conversely (2) first returns \(X\), then
\(Y-X(Z-X^2)+(Z-X^2)X=Y\), then \(Z\), and finally
\(W-Z^4+Z^4=W\). Thus both polynomial inverse orders hold
without a localization or a Jacobian-only inference.

The derivation in these actual coordinates is
\[
E=\partial_X+(Z-X^2)\partial_Y+2X\partial_Z
       +8XZ^3\partial_W.
\tag{3}
\]
It is locally nilpotent because it is the transported coordinate
partial in (1), and \(EX=1\) supplies a global slice. The exact
E-time degrees are \((1,1,2,8)\): the leading coefficients of
\(X,Y,Z,W\) in \(u\) are respectively \(1,g,1,1\), with
\(g\ne0\). In particular \(E^2X=E^2Y=0\) and
\(EY/EX=g\) is nonconstant. None of the four displayed entries
is invariant, although \(A=\ker E=\mathbb C[v,g,w]\).

## 2. The precise one-shot family being tested

In the polynomial ring \(\mathbb C[X,Y,Z,W]\), put
\[
\begin{gathered}
H=2XW-Z^2,\qquad D_0=X\partial_Z+Z\partial_W,\\
\ker_B D_0=\mathbb C[X,Y,H].
\end{gathered}
\tag{4}
\]
The kernel equality is exact in the original ring. Indeed, after
inverting \(X\), the variable \(S=Z/X\) is a \(D_0\)-slice and
\(B_X=\mathbb C[X,X^{-1},Y,H,S]\), with \(D_0=\partial_S\).
An invariant is therefore in \(\mathbb C[X,X^{-1},Y,H]\).
If a polynomial invariant had a least positive denominator power
\(X^n\), its numerator \(F(X,Y,H)\), not divisible by \(X\),
would satisfy \(F(0,Y,-Z^2)=0\). But substitution
\(H\mapsto-Z^2\) defines an injection
\(\mathbb C[Y,H]\hookrightarrow\mathbb C[Y,Z]\).
Hence \(F(0,Y,H)=0\), a contradiction. The opposite kernel
inclusion follows from \(D_0X=D_0Y=D_0H=0\).

For every \(J\in\ker_B D_0\), define
\[
Z_J=Z-XJ,\qquad W_J=W-ZJ+\frac X2J^2,
\qquad I_{J,P,Q}=W_J-PZ_J-Q,
\quad P,Q\in\mathbb C[X,Y].
\tag{5}
\]
Here \(ZJ\) in the expression for \(W_J\) is the product \(Z\cdot J\),
not the subscripted variable \(Z_J\). The first two formulas are
the actual automorphism \(\exp(-JD_0)\), fixing \(X,Y\), with
inverse \(\exp(JD_0)\). Local nilpotence follows from
\((JD_0)^n=J^nD_0^n\). The final change to \(I_{J,P,Q}\)
is a triangular shear with polynomial inverse. Thus
\((X,Y,Z_J,I_{J,P,Q})\) is always an actual polynomial frame.

We prove that \(EI_{J,P,Q}\ne0\) for every choice in (5).
This quantifies over all polynomial invariant parameters \(J\)
and arbitrary-degree \(P,Q\), without a finite degree cutoff.

## 3. The highest W coefficient excludes every H-dependent parameter

Suppose \(m=\deg_H J>0\), and write
\(J=j_m(X,Y)H^m+\cdots\), with \(j_m\ne0\).
The terms \(ZJ\) and \(PZ_J\) have \(W\)-degree at most
\(m\). The term \(W\) has degree one and \(Q\) degree zero.
Thus the sole coefficient of degree \(2m\) in (5) is
\[
[W^{2m}]I_{J,P,Q}
 =2^{2m-1}X^{2m+1}j_m(X,Y)^2=:C_m(X,Y)\ne0.
\tag{6}
\]
Every coefficient of (3) has \(W\)-degree zero. Its
\(\partial_W\) term lowers \(W\)-degree. Consequently
\(EI_{J,P,Q}=0\) would force
\(\partial_XC_m+(Z-X^2)\partial_YC_m=0\).
Comparison in the independent variable \(Z\) first gives
\(\partial_YC_m=0\), hence \((j_m)_Y=0\) in the polynomial
domain. The remaining equation is
\[
(2m+1)j_m+2X(j_m)_X=0.
\tag{7}
\]
For a nonzero polynomial \(j_m=\sum_{k\ge0}c_kX^k\), each
coefficient in (7) is \((2m+1+2k)c_k\). These factors are
nonzero in characteristic zero. This contradiction excludes every
\(H\)-dependent invariant parameter.

It remains to consider \(J\in\mathbb C[X,Y]\), including zero.
In this case (5) has the form
\(I_{J,P,Q}=W-\widetilde PZ-\widetilde Q\), where
\(\widetilde P=J+P\) and
\(\widetilde Q=Q-XJ^2/2-XPJ\) lie in \(\mathbb C[X,Y]\).
Invariance would require
\[
8XZ^3
 =2X\widetilde P+
   \{\widetilde P_X+(Z-X^2)\widetilde P_Y\}Z
       +\widetilde Q_X+(Z-X^2)\widetilde Q_Y.
\tag{8}
\]
The right side has \(Z\)-degree at most two, whereas the left
side has nonzero cubic coefficient \(8X\). This is impossible.
Every parameter choice in (5) has now been excluded for the last slot.

In particular the originally proposed subfamily \(J=\lambda H\),
\(\lambda\in\mathbb C\), fails. For \(\lambda\ne0\), (6)
gives \([W^2]EI_{J,P,Q}=6\lambda^2X^2\); for \(\lambda=0\),
the cubic defect in (8) is \(8X\).

## 4. What this changes, and what it does not

The ansatz (5) contains the successful replica-plus-shear
mechanism of the [monomial203 proof](weight-four-two-root-monomial-coordinate-recognition-pass203-working.md):
its parameter belongs to \(\mathbb C[X,Y,H]\), and the final
correction lies in \(\mathbb C[X,Y]\). Nevertheless that
last-slot construction does not extend to every supplied two-good
frame, even for a translation with an actual coordinate slice.

Here the original inverse already gives invariant coordinates
\(Z-X^2\), \(Y-X(Z-X^2)\), and \(W-Z^4\).
The elementary last-coordinate shear \(W\mapsto W-Z^4\)
already gives an invariant coordinate, outside the final shear
linear in \(Z_J\) permitted by (5). More strongly, the allowed
parameter \(J=X\) gives the invariant \(Z_J=Z-X^2\) in the
other bad slot. Therefore the negative result is specifically about
the fixed final \(W\)-slot. It does not exclude an invariant in
another output slot, an arbitrary polynomial shear in \(Z_J\),
preprocessing, or a longer composition of replicas.

This frame is not a true global E-degree minimizer: (1) has total
degree twelve, while \((u,v,g,w)\) has total degree one.
No conclusion about such global minimizers follows. The earlier
[strict-descent boundary124](unrestricted-entry-frontier-pass124.md)
and selected-top counterexamples32--33 remain separate issues.
Nothing here proves arbitrary coordinate entry, disproves a general
composite-flow reduction theorem, or provides an exotic kernel.

Independent inline exact arithmetic checked both inverse orders,
the transported derivation, exact time degrees and the constant-\(\lambda\)
coefficient identities. The all-degree quantification over \(J,P,Q\)
is established by the written kernel and polynomial-degree arguments,
not by sampling or a finite bound on \(m\).
No checker was authored, executed, imported or compiled. No earlier
source or packet was edited. This is a bounded working countercontrol,
not a novelty claim, human expert certification or formal verification.
