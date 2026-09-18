# An exact mixed-coefficient integral and the nonvanishing conic obstruction

Working result: in the retained reciprocal conic sector316, one lower
coefficient is determined by a single complex constant and the coefficient
function f=k-ms. The nonzero restricted fourth-gradient coefficient is
also an explicit fourth-order differential expression in f. Its zero
solutions form a four-dimensional complex space, which this sector excludes.

These are necessary conditions inside the existing actual chart. They do
not recognize the remaining conic, restrict f to rational functions in t,
or turn a coefficient-field substitution into an actual coordinate change.

## 1. Exact field and coefficient hypotheses

Retain the full actual conic hypotheses and results of
[316](principal-paraboloid-conic-factor-unit-scalar-rigidity-pass316-working.md),
including its affine selected factor and nonzero restricted coefficient
\(\mathcal C\). Use its exact curve field \(\mathcal F\), finite over
\(\mathbb C(t)\), with t-derivative having constants exactly \(\mathbb C\).
Write
\[
T=t-\tau,\qquad m=d+c/T,\qquad
c,d,\tau\in\mathbb C,\quad c\ne0,\qquad
p=m_t,
\quad \delta=\frac{m m_{tt}}{2p}.
\tag{1}
\]
All primes below mean this exact t-derivative. In particular T'=1.
The symbols T and c+dT are nonzero elements of the coefficient field;
their inverses are not claimed to be original polynomial functions.

The polynomial coefficient bounds315 and the n_ss equation316 give
\[
k=ms+f,\quad f\in\mathcal F,\qquad
n=\frac{p^2-\delta^2}{4}s^2+n_1s+n_0,
\quad n_1,n_0\in\mathcal F.
\tag{2}
\]
Retain the exact definitions
\[
b_P=\frac{k_{tt}}4-\frac{m k_{ttt}}{12p},\quad
b_V=\frac{p-\delta}{2},\quad
\mu=k_{tt}-\frac{k_t p+2n_s}{m}.
\tag{3}
\]
The two equations used here are, respectively, the raw mixed surface
coefficient and the P coefficient of the restricted fourth-gradient identity:
\[
\begin{aligned}
\mathcal R&:=n_{ts}-\frac{2p n_s}{m}-\mu b_V-\delta b_P=0,\\
(b_P)_t-\frac{b_V k_{tt}}m+\frac{4b_Pb_V}m
 &=-\frac{4p\mathcal C}{m\delta},
\qquad \mathcal C\in\mathcal F^*.
\end{aligned}
\tag{4}
\]
No derivatives of a moving line parameter occur in these formal
coefficient identities.

## 2. The entire mixed equation has an exact first integral

Define rational coefficient functions
\[
G=\frac{T^2}{c+dT},\qquad
H=\frac{T(c+dT)}{12c},\qquad
J=\frac{c-dT}{4(c+dT)}-\frac{c+2dT}{12c}.
\tag{5}
\]
Substituting (2),(3) into the first equation of (4), its coefficient
of s vanishes identically. Its remaining coefficient is
\[
\mathcal R=n_1'+\frac{2c+dT}{T(c+dT)}n_1
 +\frac{(c+dT)^2}{12cT}f'''
 +\frac{c-dT}{4T^2}f''
 -\frac{cd}{2T^2(c+dT)}f'.
\tag{6}
\]
This calculation keeps arbitrary f,n_1,n_0 in the exact field.
The coefficient n_0 does not enter the mixed equation.

The integrating factor is G. Direct differentiation gives
\[
\frac{G'}G=\frac{2c+dT}{T(c+dT)},\qquad
H'+J=\frac{c-dT}{4(c+dT)},\qquad
J'+\frac d{6c}=-\frac{cd}{2(c+dT)^2}.
\tag{7}
\]
Consequently the full identity, before imposing the equation, is
\[
G\mathcal R=
\left(Gn_1+Hf''+Jf'+\frac d{6c}f\right)'.
\tag{8}
\]
The constant field of \(\mathcal F\) now proves that there is
\(\zeta\in\mathbb C\) with
\[
\boxed{
n_1=\frac{c+dT}{T^2}
 \left(\zeta-Hf''-Jf'-\frac d{6c}f\right).}
\tag{9}
\]
This is an exact integration, not a rational-function ansatz for f.
It includes d=0, when it reads
\(n_1=c\zeta/T^2-cf''/(12T)-cf'/(6T^2)\).

## 3. The fourth-gradient coefficient depends only on f

The explicit coefficient (3) is
\[
b_P=-\frac d{2T^2}s+B_0,
\qquad B_0=\frac{f''}4+Hf''',\qquad
b_V=\frac d{2T},\quad
\delta=-\frac{c+dT}{T^2}.
\tag{10}
\]
In the second equation of (4), all s terms cancel. Its constant
coefficient on the left is
\[
B_0'+\frac d{2(c+dT)}(4B_0-f'')
 =\frac{c+dT}{12c}(Tf''''+4f''').
\tag{11}
\]
Solving that same equation, with its exact sign, therefore gives
\[
\boxed{
\mathcal C=-\frac{(c+dT)^3}{48c^2T}
                  (Tf''''+4f''').}
\tag{12}
\]
In particular this expression is independent of n_0,n_1 and s.
When d=0, (12) agrees with the exact boundary identity
\((b_P)_t=-4T\mathcal C/c\) used in320.

## 4. The excluded four-dimensional family is exact

All prefactors in (12) are nonzero in \(\mathcal F\). Thus its
vanishing would be equivalent to
\[
Tf''''+4f'''=0,
\quad\text{or equivalently}\quad (T^4f''')'=0.
\tag{13}
\]
The constant field first gives \(T^4f'''=q\in\mathbb C\).
The function \(-q/(6T)\) has third derivative \(q/T^4\).
Subtracting it leaves a function with third derivative zero.
Successive use of the same exact constant field then gives a complex
quadratic polynomial in T. Conversely every such expression plainly
satisfies (13). Hence
\[
\mathcal C=0\quad\Longleftrightarrow\quad
f\in\operatorname{span}_{\mathbb C}\{1,T,T^2,T^{-1}\}.
\tag{14}
\]
The actual conic has \(\mathcal C\ne0\) by316's gradient-minor gate,
so none of these functions is allowed. This does not exclude arbitrary
other f, solve the n_0 and ell equations, or provide original coordinates.

## 5. Verification and scope

Fresh unsaved exact algebra reconstructed the raw mixed equation from
(2),(3), checked (8) with arbitrary coefficient functions, and independently
checked (12), its s-independence and its d=0 specialization. The exact-field
integration and exclusion (14) are the written argument, not finite samples.

This note does not invoke320 to discard d=0 during the algebra. Its formulas
may therefore be checked at that boundary even though320 separately excludes
the corresponding actual conic sector. No saved checker was executed,
imported, compiled or rerun in deriving this note. No previous proof or
canonical index was changed by this derivation. No unrestricted cancellation,
original-coordinate, human-expert or historical novelty claim is made.
