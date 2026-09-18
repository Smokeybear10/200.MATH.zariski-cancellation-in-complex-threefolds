# Trace removes the constant-field restriction from base compatibility

For any active first-tail component, the two initial source speed-ratio
identities are equivalent to agreement between formal differentiation
in the slice coordinate and the transported normalized source action.
No assumption that the component has algebraic constant field \(L\)
is needed. A finite field trace replaces the finite-order automorphism
argument used under that extra assumption in143.

The component can still enlarge the coefficient field. The conclusion
fixes all peeling coefficients, including the first evaluated negative
coefficient, but does not fix every element of \(L\) or prove that the
component is the originally selected one. No first-tail primitivity or
global cancellation conclusion is asserted.

## 1. Exact source and component data

Use the actual dense chart139 and active-component construction141.[^1]
The source data include
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
s=EX\ne0,\qquad D=E/s,\\
E^2X=E^2Y=E^2Z=0,\qquad
\tau=EY/s,\quad \rho=EZ/s,\quad K=\mathbb C(\tau,\rho),\\
\tau,\rho\text{ algebraically independent},\qquad
L/K\text{ finite separable},\\
F=\operatorname{Frac}A=\mathbb C(y,z,w_0)=L(v),\qquad
L[y,z]=L[v],\\
Y=y+\tau X,\quad Z=z+\rho X,\quad D=\partial_X\text{ on }F(X),\\
F(X)=\mathbb C(X,Y,Z,W),\qquad
\det\frac{\partial(Y,Z,W)}{\partial(\tau,\rho,v)}=1 .
\end{gathered}
\tag{1}
\]
The determinant fixes \(X\); the two coefficient partials fix \(v\).
Its value at \(X=0\) is part of the actual selected-cofactor calibration.
The field-generation equality uses the actual coordinate inverse,
not only a relative Jacobian identity.

Let \(H_d(f;U,V)\) denote the order-\(d\) homogeneous Taylor
polynomial in the two commuting coefficient partials on \(L\).
Retain the exact signed data
\[
\begin{gathered}
f_0,\ldots,f_m,f_{-1}\in L,\qquad f_m\ne0,\quad m\ge0,\\
\Omega=\sum_{j=0}^{m}H_j(f_j),\qquad w_0=\Omega(y,z),\\
\Phi=-\sum_{j=0}^{m}H_{j+1}(f_j)-f_{-1}\ne0,\qquad
\Psi=-\sum_{j=0}^{m}H_{j+2}(f_j)-H_1(f_{-1}),\\
\ker(L[U,V]\to L[v])=(g),\qquad
\Phi(y,z)=0,\qquad \Psi(y,z)=v+c,\quad c\in L .
\end{gathered}
\tag{2}
\]
Here \(U,V\) are independent variables and all coefficient fields
are kept with their specified embeddings.

For an irreducible factor \(h\mid\Phi\), put
\[
\begin{gathered}
R_h=L[U,V]/(h),\qquad F_h=\operatorname{Frac}R_h,\qquad
y_h=\overline U,\quad z_h=\overline V,\\
w_{0h}=\Omega(y_h,z_h),\qquad v_h=\Psi(y_h,z_h).
\end{gathered}
\tag{3}
\]
Assume \(h\) is active, meaning \(v_h\) is transcendental over \(L\).
Persistence141 supplies \(T_h\), the polynomial \(W_h(X)\), the
Taylor map \(\Theta_h\), and relative Jacobian one, with
\[
Y_h=y_h+\tau X,\quad Z_h=z_h+\rho X,\quad
T_h(X,Y_h,Z_h,W_h)=(0,0,0,1),\quad W_h(0)=w_{0h}.
\]
The \(X=0\) determinant gives the rational source embedding142:[^2]
\[
\begin{gathered}
\sigma_h:F=\mathbb C(y,z,w_0)\hookrightarrow F_h,\qquad
(y,z,w_0)\longmapsto(y_h,z_h,w_{0h}),\\
\det\frac{\partial(y_h,z_h,w_{0h})}
              {\partial(\tau,\rho,v_h)}=1 .
\end{gathered}
\tag{4}
\]
In particular all nonzero rational source denominators have nonzero
images under this embedding.

For the forward implication assume just the two base identities
\[
\sigma_h(\tau)=\tau,\qquad \sigma_h(\rho)=\rho .
\tag{5}
\]
No constant-field equality is added to (5).

## 2. The exact compositum and the initial parameter scale

Write \(L'=\sigma_h(L)\) and let \(C_h=L L'\) be their compositum
inside \(F_h\). Both \(L\) and \(L'\) are finite extensions of
the same \(K\), and \([L:K]=[L':K]\). Set
\(\widetilde v=\sigma_h(v)\). The actual source field gives
\[
\begin{gathered}
\sigma_h(F)=L'(\widetilde v),\qquad
F_h=L\,\sigma_h(F)=C_h(\widetilde v),\\
C_h\text{ is the relative algebraic closure of }L\text{ in }F_h,\\
d=[C_h:L']=[C_h:L]<\infty .
\end{gathered}
\tag{6}
\]
Indeed \(F_h=L(y_h,z_h)\), while
\(\sigma_h(F)=\mathbb C(y_h,z_h,w_{0h})\) and
\(w_{0h}\in L[y_h,z_h]\). These equalities prove the first line.
The element \(\widetilde v\) is transcendental over \(C_h\), so
the relative algebraic closure assertion follows from the rational
function field \(C_h(\widetilde v)\). The equality of the two
degrees follows by taking degrees over \(K\).

The coefficient partials on \(K\) extend uniquely to \(C_h\).
Transporting the source partials through \(\sigma_h\), and then
extending through \(C_h/L'\), therefore gives the same coefficient
partials, with \(\widetilde v\) fixed. The transported initial
determinant from (1) is one with respect to
\((\tau,\rho,\widetilde v)\). Its initial triple is identical
to that in (4). The chain rule consequently gives
\[
\partial_{v_h}\widetilde v=1,\qquad
\widetilde v=v_h+c_h,\quad c_h\in C_h,\qquad
F_h=C_h(v_h).
\tag{7}
\]
Here the constants of \(\partial_{v_h}\) on \(F_h\) are exactly
\(C_h\). An element transcendental over \(C_h\) and killed by
this derivation would make \(F_h\) algebraic over a field of
constants, contrary to \(\partial_{v_h}v_h=1\).
The unit scale in (7) comes from the two calibrated determinants;
it is not inferred merely from transcendence of both parameters.

## 3. Transport the actual source inverse before taking a trace

Extend \(\sigma_h\) to \(F(X)\) by fixing \(X\), and put
\(W^*=\sigma_h(W)\). The base identities give the same goods
\(X,Y_h,Z_h\). The source inverse and Taylor expression yield
\[
\begin{gathered}
M^*:=\mathbb C(X,Y_h,Z_h,W^*)
     =\sigma_h(F)(X)=L'(\widetilde v,X),\\
F_h(X)=C_h(\widetilde v,X),\qquad [F_h(X):M^*]=d,\\
W^*=\left(\sum_{j=0}^{m}X^j\Theta_h(\sigma_h f_j)\right)_{\ge0},
\qquad
W_h=\left(\sum_{j=0}^{m}X^j\Theta_h(f_j)\right)_{\ge0}.
\end{gathered}
\tag{8}
\]
The Taylor identities are valid because a \(K\)-embedding of
finite separable coefficient fields commutes with the uniquely
extended coefficient partials.

Transport the full source determinant (1), then use (7).
It follows that \(T_hW^*=1\). Thus \(T_h\) restricts on \(M^*\)
to the actual last-coordinate partial, whose constant field is
\(\mathbb C(X,Y_h,Z_h)\).
Importantly, \(M^*\) has not been identified with \(F_h(X)\);
the finite extension in (8) is retained.

Let \(Q=W_h-W^*\in F_h[X]\). Both last-coordinate derivatives
are one, so \(T_hQ=0\). Finite separability implies that a
derivation commutes with field trace: extend it to a normal
closure and sum over embeddings, which commute with the unique
extended derivation. Therefore
\[
\operatorname{Tr}_{F_h(X)/M^*}Q
       \in\mathbb C(X,Y_h,Z_h).
\tag{9}
\]
The trace in (8) is coefficientwise
\(\operatorname{Tr}_{C_h/L'}\), after adjoining the independent
variables \(\widetilde v,X\). In particular it does not increase
the polynomial \(X\)-degree.

## 4. A finite-conjugate averaging lemma

We use an elementary fact valid in characteristic zero.
Let \(a,b\) be conjugate over a field \(K\), contained in a
finite extension \(C/K\), and let \(L'\subset C\) contain \(K\)
and \(b\). If
\[
b=\frac{1}{[C:L']}\operatorname{Tr}_{C/L'}(a),
\]
then \(a=b\).

To prove it, take a finite normal closure \(\Lambda/K\)
containing \(C\). Let \(H=\operatorname{Gal}(\Lambda/L')\).
The right side is
\(|H|^{-1}\sum_{\eta\in H}\eta(a)\).
The orbit of \(a\) under \(\operatorname{Gal}(\Lambda/K)\)
is finite and also contains \(b\). Its \(\mathbb Q\)-linear
span is finite dimensional. Choose a real-valued
\(\mathbb Q\)-linear functional that takes distinct values
on the distinct orbit elements. Such a functional exists
by avoiding finitely many proper linear hyperplanes.

Choose an automorphism \(\gamma\) carrying \(b\) to the unique
maximum of those values on the orbit. Apply \(\gamma\), then
the functional, to the averaging identity. Every summand is
at most that maximum. Equality of their average forces every
summand to attain it. The summand for \(\eta=1\) therefore
gives \(\gamma(a)=\gamma(b)\), so \(a=b\).
This does not require \(C/L'\) or the original coefficient
extension to be normal, nor an ordering of \(K\).

## 5. The leading traced coefficient cannot differ

Suppose some \(f_j\ne\sigma_h f_j\), and choose the largest
such \(j\). Formula (8) shows that \(Q\) has \(X\)-degree \(j\)
and leading coefficient \(a-b\), where
\(a=f_j,\ b=\sigma_h f_j\).
The coefficient of \(X^j\) in its trace is
\[
\kappa=\operatorname{Tr}_{C_h/L'}(a)-d b\in L'.
\tag{10}
\]
By (9), this coefficient lies in \(K\). If the trace's degree
drops below \(j\), the coefficient is zero, which also lies
in \(K\). Otherwise it is the leading coefficient of a
nonzero rational good-coordinate function.
For such a function, substitute
\(Y_h=y_h+\tau X,\ Z_h=z_h+\rho X\) into complex numerator
and denominator polynomials. Their nonzero leading homogeneous
evaluations at \((1,\tau,\rho)\) give a ratio in \(K\).
Algebraic independence of \(\tau,\rho\) prevents a leading
evaluation from vanishing.

Taking trace from \(L'\) to \(K\) in (10) gives zero:
\[
\begin{aligned}
\operatorname{Tr}_{L'/K}\kappa
&=\operatorname{Tr}_{C_h/K}a-d\operatorname{Tr}_{L'/K}b\\
&=d\operatorname{Tr}_{L/K}a-d\operatorname{Tr}_{L'/K}b=0 .
\end{aligned}
\]
The final equality uses that \(\sigma_h:L\to L'\) is a
\(K\)-isomorphism carrying \(a\) to \(b\).
Since \(\kappa\in K\), characteristic zero forces \(\kappa=0\).
The averaging lemma of Section 4 now yields \(a=b\), a
contradiction. Hence
\[
W_h=W^*,\qquad
\sigma_h f_j=f_j\quad(0\le j\le m),\qquad
\sigma_h f_{-1}=f_{-1}.
\tag{11}
\]
For the last equality, apply \(\sigma_h\) to the actual
evaluated identity \(\Phi(y,z)=0\).
After the nonnegative coefficients agree, subtract the
component identity \(\Phi(y_h,z_h)=0\).
Only \(f_{-1}-\sigma_h f_{-1}\) remains.
This evaluation takes place in the common field \(C_h\);
no divisibility between polynomials over mismatched
coefficient subfields is assumed.

The proof includes \(m=0\). It uses neither a positive time
degree nor a nonzero trace leading coefficient.

## 6. Exact derivation comparison

For every active component the target-generator map
\[
\iota_h:\mathbb C(X,Y,Z,W)\hookrightarrow F_h(X),\qquad
(X,Y,Z,W)\longmapsto(X,Y_h,Z_h,W_h)
\]
is injective and has finite separable field extension.
Transport \(E/s\) along it, and extend the derivation uniquely
to \(F_h(X)\).
Under (5), equation (11) identifies its image with \(M^*\)
in (8). The transported derivation fixes \(L'(\widetilde v)\)
and sends \(X\) to one. Its extension fixes \(C_h\), which is
algebraic over \(L'\), and thus is exactly \(\partial_X\)
fixing \(F_h=C_h(\widetilde v)\).

Conversely, if this extended source derivation equals formal
\(\partial_X\), evaluate its values on \(Y_h,Z_h\) at \(X=0\).
They give the two identities in (5). The specialization is
legitimate because their projected rational denominators
are nonzero under the source embedding (4).
Thus the equivalence holds for all active components, with
no restriction on the enlarged constant field:
\[
\boxed{\quad
\sigma_h(\tau)=\tau,\ \sigma_h(\rho)=\rho
\quad\Longleftrightarrow\quad
\text{transported }E/s=\partial_X\text{ on }F_h(X).
\quad}
\tag{12}
\]
In particular \(\sigma_h\) fixes
\(L_0=K(f_0,\ldots,f_m,f_{-1})\).
It need not fix the larger specified field \(L\).

## 7. A separate actual polynomial-projection corollary

The field proof above did not assume a whole-line equality
for the unlocalized component ring. That equality can now
be justified using the additional actual projection input143.[^3]
Choose a primitive element \(e\in\ker_A N\) with \(L=K(e)\).
There is a complex polynomial \(p_e\) such that
\(e=p_e(y,z,w_0)\), because \(e\) is an actual polynomial invariant.
Therefore
\(\sigma_h(e)=p_e(y_h,z_h,\Omega(y_h,z_h))\in R_h\).
The base identities put \(K\) in \(R_h\), and the algebraic
element \(\sigma_h(e)\) generates a field already as a
polynomial algebra over \(K\). Consequently
\(L'=K[\sigma_h(e)]\subset R_h\), and \(C_h=LL'\subset R_h\).
Transporting \(L[y,z]=L[v]\) and adjoining \(L\) now proves
\[
R_h=C_h[\widetilde v]=C_h[v_h].
\tag{13}
\]
Thus the component is a polynomial line over its exact finite
constant extension \(C_h\). It is not asserted to be a polynomial
line over \(L\) when \(C_h\ne L\).
The actual polynomial representative of \(e\) is essential
to this ring argument; the field equality in (6) alone
would not justify (13).

## 8. Scope

The result removes the constant-field assumption from the
base-compatible derivation comparison143.[^4]
It does not prove the two base identities for every active
component, and it does not exclude inactive components.
Nor does it make the source coefficient embedding the identity
on \(L\). The exact coefficient-fixing and generic-fiber
criteria142 remain distinct from automatic first-tail
primitivity.

The target ring already carries the genuine last-coordinate
LND \(T_h\) for every active component. The new argument
uses the actual source inverse before taking a trace;
it does not infer field generation from target local
nilpotence or from a relative Jacobian alone.
No actual extra-factor example, arbitrary coordinate-entry
result, or cancellation proof is supplied.

## Sources

1. [A dense all-degree chart and its formal Taylor peeling139](dense-all-degree-taylor-chart-pass139-working.md)
   and [Formal persistence on a first-tail component141](dense-tail-component-persistence-pass141-working.md).
   Exact actual source field and determinant, Taylor coefficients,
   and the active-component field construction.
2. [Coefficient compatibility selects the actual first-tail component142](dense-tail-coefficient-compatibility-pass142-working.md),
   Sections 1--3. The rational source substitution at \(X=0\).
3. [Actual invariants give a denominator-free coefficient fiber143](polynomial-coefficient-fiber-presentation-pass143-working.md),
   Sections 1--2. Polynomial source representatives for actual
   invariants and a primitive coefficient element inside \(\ker_A N\).
4. [Base-compatible components and the coefficient stabilizer143](dense-base-compatible-component-stabilizer-pass143-working.md),
   Sections 2--4. The initial scaling issue and the earlier
   constant-field-restricted comparison.

The trace, finite-conjugate averaging, and compositum arguments
are proved directly above. No new external classification or
historical novelty claim is invoked.

[^1]: Source 1. The source inverse and its normalization are actual
    premises, not consequences of formal persistence.
[^2]: Source 2. The embedding is not initially assumed to fix \(L\).
[^3]: Source 3. This is used only for the unlocalized ring conclusion.
[^4]: Source 4. The enlarged constant field is retained throughout
    the trace proof.
