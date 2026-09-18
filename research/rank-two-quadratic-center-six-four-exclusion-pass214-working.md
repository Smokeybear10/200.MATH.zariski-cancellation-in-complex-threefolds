# Excluding the degree-six/four rank-two projection

Status: bounded working exclusion. In the actual rank-two chart with
\(q=1/\rho\), the exceptional projected degree pair
\((\deg_v y,\deg_v\vartheta)=(6,4)\) is impossible. The proof uses
the full sextic potentials, the monic characteristic polynomial at
infinity, and an elementary norm-residue obstruction over the exact
finite coefficient field. It does not infer that the plane ring is
normal or recognize the remaining original action.

## 1. Actual hypotheses and the selected monic relation

Retain the actual hypotheses and constructions of
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md)
and [center degree pruning213](rank-two-squarefree-center-degree-pruning-pass213-working.md),
both freshly read through their complete proofs. Thus
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4),\\
q=1/\rho,\quad F=\mathbb C(t,\rho)\subset L,\quad [L:F]<\infty,\\
O=L[v],\quad C=L[y,\vartheta]\subset O,\quad
\operatorname{Frac}C=L(v),\quad
R=2\rho^{-3}\vartheta+k_\rho\ne0.
\end{gathered}
\tag{1}
\]
The original generators are polynomial coordinates, and the displayed
initial ideal is the full kernel. The selected original partial and
actual return in212 supply these fields and rings, not a formal
parametrization. The variables \(t,\rho\) are algebraically independent.
Their partial derivatives extend uniquely and commute on the finite
separable field \(L\). No rationality of \(L\) is assumed.

The actual potentials also retain \(L[y,z,w]=O\),
\(\mathbb C(y,z,w)=L(v)\), and the calibrated determinant
\(J_0=-a^3\in L^*\), where \(a=EX\). In particular212 proves the
birational plane return in (1), the conductor inclusion \(RO\subset C\),
and the selected-factor statements used below. None is inferred from
a generic polynomial pair alone.

Assume for contradiction that
\[
d:=\deg_v y=6,\qquad e:=\deg_v\vartheta=4.
\tag{2}
\]
Let \(G(U,V)\) generate the irreducible plane evaluation kernel.
By212, \(\deg G=d=6\) and \(\deg_U G=e=4\).
By the integral argument in213, normalize \(G\) to be monic in \(U\):
\(O\) is free of rank four over \(L[\vartheta]\), and the
characteristic polynomial of multiplication by \(y\) equals its
minimal polynomial by \(L(\vartheta)(y)=L(v)\).
Thus this monic characteristic polynomial is exactly \(G\).

## 2. Explicit weighted coefficients of the sextic

For independent formal variables \(U,V\), write
\(H_j(b)=\sum_{i=0}^j b_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).
The full212 polynomial is
\[
\begin{aligned}
\mathcal R&=2\rho^{-3}V+k_\rho,\\
S&=-\rho^{-4}V^3+\tfrac12k_{tt}U^2+k_{t\rho}UV
   +\tfrac12k_{\rho\rho}V^2+n_tU+n_\rho V,\\
T&=\ell-S,\qquad
c_0=-3\rho^{-4}V^2+k_{t\rho}U+k_{\rho\rho}V+n_\rho,\\
Q&=\rho^{-5}V^4+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\mathcal H&=\rho^{-3}T^2+\mathcal R c_0T+\mathcal R^2Q,
\qquad \mathcal H(y,\vartheta)=0.
\end{aligned}
\tag{3}
\]
Here \(k,n,\ell,m\in L\), and all derivatives in (3) are coefficient
derivatives before evaluation. In particular no lower potential is
set to zero.

The exact total degree is six, with top form
\(-\rho^{-11}V^6\). The coefficient of \(U^4\) is
\(k_{tt}^2/(4\rho^3)\), independent of \(V\).
If \(k_{tt}=0\), its derivatives \(k_{ttt},k_{tt\rho}\) also vanish
and the U-degree of \(\mathcal H\) is at most two. Since \(G\) divides
\(\mathcal H\) and has U-degree four, this cannot happen. Consequently
\[
h:=k_{tt}\ne0,\qquad
A_0:=\frac{h^2}{4\rho^3}\ne0,\qquad
\mathcal H=A_0G.
\tag{4}
\]
The last equality uses equality of total degrees, followed by the
monic U-fourth coefficient; there is no nonconstant cofactor here.

Assign weights \(\operatorname{wt}U=6\), \(\operatorname{wt}V=4\).
The largest weights in \(T,\mathcal R,c_0\) are respectively
\(12,4,8\). In \(Q\), the only term of weight greater than sixteen
is \(k_{ttt}U^3/6\), of weight eighteen. It follows directly from
(3) that the only term of \(\mathcal H\) with weight greater than
twenty-four is
\[
\mathcal H_{[26]}=\frac{2k_{ttt}}{3\rho^6}U^3V^2.
\tag{5}
\]
If its coefficient were nonzero, evaluation at (2) would produce
a unique term of degree twenty-six in \(v\). Every other term
has degree at most twenty-four. Thus (3) forces \(k_{ttt}=0\).

The weight-twenty-four contributions can now be read separately.
The highest parts of \(T,\mathcal R,c_0\) are
\(\rho^{-4}V^3-hU^2/2\), \(2\rho^{-3}V\), and
\(-3\rho^{-4}V^2\). The weight-sixteen part of \(Q\) is
\(\rho^{-5}V^4+(h_\rho/2)U^2V\). Hence
\[
\begin{aligned}
(\rho^{-3}T^2)_{[24]}
 &=\frac{h^2}{4\rho^3}U^4-h\rho^{-7}U^2V^3+\rho^{-11}V^6,\\
(\mathcal R c_0T)_{[24]}
 &=3h\rho^{-7}U^2V^3-6\rho^{-11}V^6,\\
(\mathcal R^2Q)_{[24]}
 &=2h_\rho\rho^{-6}U^2V^3+4\rho^{-11}V^6,\\
\mathcal H_{[24]}
 &=\frac{h^2}{4\rho^3}U^4
   +\frac{2(h+\rho h_\rho)}{\rho^7}U^2V^3
   -\rho^{-11}V^6.
\end{aligned}
\tag{6}
\]
This extraction is independent of \(k_t,k_\rho,n,\ell,m\) and all
their remaining lower coefficients.

## 3. Why the weighted initial polynomial is a square

Merely substituting the leading terms of \(y,\vartheta\) into (6)
would give one root of a quadratic, not the repeated root needed
below. The monic characteristic polynomial supplies the stronger
identity, with an elementary formal-branch proof.

Write the two leading coefficients as
\[
y=a_6v^6+\text{lower powers},\qquad
\vartheta=b_4v^4+\text{lower powers},\qquad a_6b_4\ne0,
\qquad c_*:=a_6^2/b_4^3\in L^*.
\tag{7}
\]
Extend coefficient scalars to an algebraic closure \(K\) of \(L\),
and introduce a formal parameter \(s\). Set the independent variable
\(V=s^{-4}\). Substituting \(v=s^{-1}\xi\) into
\(\vartheta(v)=s^{-4}\) gives
\(b_4\xi^4+s b_3\xi^3+\cdots+s^4b_0-1=0\).
Choose \(\beta\in K^*\) with \(\beta^4=b_4^{-1}\).
At \(s=0\) the four roots \(\beta\zeta\), \(\zeta^4=1\),
are simple. Successively solving the coefficient of each power
of \(s\), whose linear coefficient is the nonzero derivative
\(4b_4(\beta\zeta)^3\), gives four series
\(\xi_\zeta(s)\in K[[s]]\) with these constant terms.
They account for all four roots of the degree-four polynomial.
Thus in \(K((s))\) the four branches satisfy
\[
v_\zeta=s^{-1}\xi_\zeta(s),\qquad
s^6y(v_\zeta)=a_6\beta^6\zeta^6+O(s),\qquad \zeta^4=1.
\tag{8}
\]

After this scalar extension the characteristic polynomial is the
product over these four branches. Therefore
\[
s^{24}G(s^{-6}Z_0,s^{-4})
 =\prod_{\zeta^4=1}\{Z_0-s^6y(v_\zeta)\}
 \in K[[s]][Z_0].
\tag{9}
\]
This also explicitly proves the weight bound: for a fixed U-power,
different V-powers give different powers of \(s\), so no monomial
of weight greater than twenty-four can occur in \(G\).
Reducing (9) modulo \(s\), the signs \(\zeta^6=\zeta^2\) are
\(+1,+1,-1,-1\). It follows that
\[
G_{[24]}=(U^2-c_*V^3)^2,\qquad
\mathcal H_{[24]}=A_0(U^2-c_*V^3)^2.
\tag{10}
\]
The first identity is a polynomial identity over the exact field
\(L\): its coefficients, including \(c_*\), already lie there.
The algebraic closure was used only to exhibit the four simple
formal branches. This proof uses neither a smooth plane model nor
an assumption that \(C=O\).

## 4. The finite-field residue contradiction

Compare the three coefficients in (6) with the square in (10).
The quadratic in the two monomials \(U^2,V^3\) has discriminant
zero, giving
\[
\begin{gathered}
\left(\frac{2(h+\rho h_\rho)}{\rho^7}\right)^2
 -4\frac{h^2}{4\rho^3}(-\rho^{-11})=0,\\
4(h+\rho h_\rho)^2+h^2=0,\qquad
\frac{\rho h_\rho}{h}=\lambda\in\{-1+i/2,-1-i/2\}.
\end{gathered}
\tag{11}
\]
The last assertion is exact in the field \(L\): the product of the
two distinct linear factors is zero, so one factor vanishes.
There is no sign choice varying from place to place.

Here is an elementary obstruction that applies directly to the finite
extension in (1), without assuming \(L=\mathbb C(t,\rho)\) or first
descending \(h\) to \(\mathbb C(\rho)\).
Let \(n_0=[L:F]\) and \(M=\operatorname{Norm}_{L/F}(h)\in F^*\).
The derivation \(\partial_\rho\) extends uniquely to a normal closure
and commutes with every F-embedding of \(L\) into that closure.
Differentiate the product defining the norm to obtain
\[
\frac{M_\rho}{M}
 =\operatorname{Tr}_{L/F}\left(\frac{h_\rho}{h}\right)
 =\frac{n_0\lambda}{\rho}.
\tag{12}
\]
Regard \(M\) as a rational function of \(\rho\) over \(\mathbb C(t)\).
At \(\rho=0\), write \(M=\rho^jP/Q\), where \(j\in\mathbb Z\)
and \(P,Q\in\mathbb C(t)[\rho]\) are nonzero at zero.
Then \(M_\rho/M=j/\rho+P_\rho/P-Q_\rho/Q\), so the coefficient
of \(\rho^{-1}\) is the integer \(j\).
Equation (12) would make it \(n_0\lambda\), which has nonzero
imaginary part. This is impossible. Thus (2) is excluded.

## 5. Exact consequence and boundary

For the quadratic squarefree center remaining in213, the necessary
degree list is consequently reduced from
\((2,1),(3,2),(6,4)\) to \((2,1),(3,2)\).
This note neither realizes nor recognizes either surviving pair.
Its contradiction does not require an additional use of the scalar
Jacobian after the actual return and exact potentials have been
established; those are retained actual-frame inputs, not conclusions
about an arbitrary formal ansatz.

In particular no lower bound on \(\deg_v(y^2-c_*\vartheta^3)\)
is assumed. The formal Davenport-type pair recorded in213 still
has its displayed degree-three remainder. The obstruction here is
the repeated-root weighted initial polynomial together with the
specific differential coefficients in (6), not that remainder.

The coefficient extraction was also checked by new inline symbolic
arithmetic. No saved checker was executed, imported or compiled,
and no earlier proof, index or verification packet was edited.
The unrestricted cancellation problem, arbitrary entry, original-ring
recognition of the remaining rank-two charts, and novelty questions
remain outside this bounded result.
