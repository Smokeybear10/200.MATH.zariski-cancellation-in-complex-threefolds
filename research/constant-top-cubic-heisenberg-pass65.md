# An exact Heisenberg correction in the constant-top cubic branch

The normalized cubic reduction supplies an additional polynomial LND,
not just a rational middle-coefficient correction. The full lower
flow coefficients force it to kill the entire two-variable defect
kernel. An actual compatible-slice projection then gives a global
commuting LND, but it adds no fourth generic direction and supplies
no new intrinsic slice by moving the common curve parameter.

This is a reduction, not a new recognition subcase.
This note does not alter the preceding
[constant-top cubic proof](constant-top-cubic-pass65.md).

## 1. The exact normalized inputs

Retain its unrecognized \(\ell\ne0\) normal form, after the permitted
constant changes of the good and bad coordinate pairs:
\[
B=k[x_1,x_2,x_3,x_4],\quad k=\mathbb C,\quad A=\ker E,\quad
E^3x=(1,0,0,0)^{\mathsf t},
\]
\[
E^2x=(f-F(t),U(t),1,0)^{\mathsf t},\qquad
Ef=1,\quad Et=0,\quad Ex_3=f,
\]
\[
\ker(E,V_3,V_4)=k[t],\qquad
\ker(V_3,V_4)=k[t,f].
\tag{1}
\]
Both defects are independent LNDs, and \(E,V_3,V_4\) commute.
The original adjoint bounds still hold in this actual frame.
Write \(W_i=[E,T_i]\).

The normalized identity \(Jc=\mathcal V\ell\), with
\(c=(1,0,0,0)^{\mathsf t}\) and \(\ell=(1,0)^{\mathsf t}\), gives
\[
W_1=-V_3.
\tag{2}
\]
In particular the following construction is attached to the actual
normalization, not to an arbitrary selected middle field.

## 2. Laurent conjugation produces a genuine LND

Let \(u\) be an external parameter killed by all fields.
The derivation \(uT_3+T_1/2\) is an LND on \(B[u,u^{-1}]\),
because it is a constant-in-the-ambient-variables combination of
commuting actual partials. Conjugate by the actual automorphism
\(\exp(E/u)\). The adjoint bounds and (2) give exactly
\[
\begin{aligned}
\exp(\operatorname{ad}_{E/u})(uT_3+T_1/2)
&=uT_3+W_3+\frac{V_3}{2u}
  +\frac{T_1}{2}+\frac{W_1}{2u}\\
&=uT_3+N,\qquad N=W_3+\frac12T_1.
\end{aligned}
\tag{3}
\]
This is an LND on the Laurent ring and preserves \(B[u]\).
Its restriction is locally nilpotent by injectivity of localization.
Specializing the stable ideal \((u)\) proves
\[
N\in\operatorname{LND}(B).
\tag{4}
\]
This argument does not rely on pointwise specialization of a family
with an unproved uniform nilpotence bound.

The first bracket is
\[
[E,N]=V_3/2.
\]
To obtain the central commutators, use the actual polynomial family
\[
\exp(z\operatorname{ad}_E)(T_3+zT_1/2)=T_3+zN.
\]
It commutes with \(\exp(z\operatorname{ad}_E)T_1=T_1-zV_3\).
The coefficient of \(z^2\) gives \([N,V_3]=0\).
It also commutes with
\(\exp(z\operatorname{ad}_E)T_4=T_4+zW_4+z^2V_4/2\);
the coefficient of \(z^3\) gives \([N,V_4]=0\).
Thus, setting \(C_0=V_3/2\),
\[
[E,N]=C_0,\qquad [E,C_0]=[N,C_0]=0,\qquad
[N,V_4]=0.
\tag{5}
\]
All fields named in (5) are polynomial LNDs of the original ring.

## 3. The full lower coefficients force zero motion

Let \(h_2=E^2x\) and \(P=Ex\). In the actual identity
\(\operatorname{Jac}(\exp(zE)x)C(z)=I\), the good first column
has coefficient \(T_1+zW_1\). Its \(z^2\) coefficient gives
\(T_1h_2=-2W_1P=2V_3P\).
The bad third column has coefficient \(T_3+zW_3+z^2V_3/2\);
its \(z^3\) coefficient gives \(W_3h_2=-V_3P\). Consequently
\[
T_1h_2=2V_3P,\qquad W_3h_2=-V_3P,\qquad
Nh_2=0.
\tag{6}
\]

In the notation of the preceding cubic proof,
\(h_2=(\sigma,U(t),1,0)^{\mathsf t}\), where
\(\sigma=f-F(t)\) and \(U\) is nonconstant. Thus (6) implies
\(N\sigma=0\) and \(U'(t)Nt=0\).
Characteristic zero and the domain property give
\[
\boxed{Nt=0,\qquad N\sigma=0,\qquad Nf=0,\qquad N(k[t,f])=0.}
\tag{7}
\]
The last statement also follows by combining the first and third
equalities with the exact defect-kernel presentation.

Commutation alone would only have given \(Nt\in k\) and
\(Nf\in k[t]\). The full equations (6) are stronger: both are
zero. A proposed recognition branch based on nonzero \(Nt\)
is therefore empty under the actual cubic hypotheses.

## 4. The compatible-slice projection is locally nilpotent

The actual slice \(f\) satisfies \(C_0f=0\), so the
[compatible Heisenberg projection, pass43 Section 4](quadratic-heisenberg-repair-pass43.md#4-a-heisenberg-projection-with-a-compatible-slice)
applies on \(B\) itself with \((\delta,L,C,\sigma)=(E,N,C_0,f)\).
It gives
\[
R=N-fC_0\in\operatorname{LND}(B),\qquad
[E,R]=[C_0,R]=0,\qquad Rf=0.
\tag{8}
\]
Here the projection coefficient \(Nf\) is zero by (7).
There is no localization or denominator removal in (8).

Here is the local-nilpotence gate in this instance. Since
\(B=A[f]\), the nonzero \(C_0\), which kills \(f\), has a nonzero
restriction to \(A\). On \(S=A\cap\ker C_0\), the restriction of
\(R\) equals that of \(N\). The Heisenberg commutators make \(S\)
stable under \(N\), so this restriction is locally nilpotent.

The centralizer lemma in pass43 Section 3 then applies to \(R|_A\).
Its proof selects a local slice of \(C_0|_A\), applies the highest
nonzero \(R\)-iterate to its plinth value to make that value
\(R\)-invariant, and uses the local-slice polynomial presentation.
This proves local nilpotence on \(A\); adjoining the variable \(f\),
which \(R\) kills, proves it on \(B\).
The argument is not the false rule that every polynomial
slice-corrected derivation is locally nilpotent.

Finally
\[
Rt=0,\qquad [V_4,R]=0.
\tag{9}
\]
For the second equality use \([N,V_4]=[C_0,V_4]=0\) and \(V_4f=0\).
Thus the original action has a genuine intrinsic LND \(R|_A\),
with zero allowed, not a presumed slice on a defect field.

## 5. No new direction or slice is supplied by this correction

The field \(N\) adds no fourth fraction-field direction:
\(E,V_3,V_4\) are independent, all four fields kill the nonconstant
\(t\), and the derivations annihilating \(t\) form a
three-dimensional space over \(\operatorname{Frac}B\).
The intrinsic restrictions of \(V_3,V_4\) are independent:
they kill \(f\), and \(B=A[f]\), so a rational relation on \(A\)
would be the same relation on \(B\).
They annihilate \(t\). The field \(R|_A\) also annihilates \(t\),
so it lies in their two-dimensional span over
\(\operatorname{Frac}A\), with zero permitted.

This is a generic dependence conclusion, not a claim that the
polynomial correction vanishes identically or is a polynomial
combination of the two defects. The construction does not supply
an intrinsic slice or generation by these fields.

The field \(N\) need not be a coordinate partial. Its annihilation
of \(t\) does not establish the omitted-constant-direction premise
of the recognition criterion in the preceding cubic note.

## Proof and source scope

The polynomial Laurent cancellation (3) is the constant-coefficient
specialization of the mechanism in pass43 Section 2, justified here
by the cubic normalization (2) and the actual commutators (5).
It is not claimed as a new general construction.
The projection mechanism likewise is the previously established
Heisenberg lemma; its complete centralizer and projection proofs
were reread before applying it here.

The initial draft used only (5) to obtain \(Nt=\kappa\in k\) and
\(Nf=q(t)\), and described recognition conditional on
\(\kappa\ne0\). Jet's full independent audit identified the unused
good \(z^2\) and bad \(z^3\) coefficients in (6). The author and
main investigator independently rederived those identities and
corrected the note: \(\kappa=q=0\) in every actual instance here.
The former nonzero-\(\kappa\) implication was formally conditional
but vacuous in this sector, and is not retained as a recognition
advance. The LND construction and compatible projection remain valid.

The earlier cubic normal form remains unchanged.
No numerical suite or metadata update is attached to this
all-instance deduction.
