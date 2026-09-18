# Closure of the constant-top degree-six cubic-column case

The constant-top degree-six case left in
[the pass 39 one-cubic-column theorem](whole-frame-recognition-pass39.md)
has a polynomial-kernel conclusion. The proof uses the full auxiliary
rows of the companion matrix, not just its upper-left block. They force
an affine relation among the next invariant coefficients. That relation
constructs a second, explicit nice LND with an ambient-coordinate slice.
Its commutation with the original action reduces the remaining kernel
calculation to the classical three-variable kernel theorem.

This closes this specified degree-six branch. It does not close the
nonconstant degree-five branch, prove that an arbitrary sliced action
has the required frame, or solve complex threefold cancellation. No
novelty or expert-verification claim is made.

## 1. Exact hypotheses and the theorem

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E\in\operatorname{LND}(B)\setminus\{0\},\qquad
T_i=\partial_{x_i}.
\]
Assume
\[
\operatorname{ad}_E^2T_i=0\quad(i\leq3),\qquad
\operatorname{ad}_E^4T_4=0,
\quad V:=\operatorname{ad}_E^3T_4\ne0.
\tag{1}
\]
Write
\[
h_j=E^j x,\quad P=h_1,\quad J=\operatorname{Jac}P,
\quad U=\operatorname{ad}_E^2T_4,\quad u=U(x),\quad v=V(x).
\]
We treat exactly the residual case
\[
h_6=c\in\mathbb C^4\setminus\{0\},\qquad
c_4=0,\qquad (h_4)_4=\lambda\in\mathbb C^*.
\tag{2}
\]
The inherited companion identities give \(h_7=0\) and
\((h_5)_4=0\). They are also immediate from the definitions in (2)
for the relevant iterates. No assertion about local nilpotence of the
middle field \(U\) is assumed.

**Theorem.** Under (1) and (2),
\[
\ker E\simeq\mathbb C^{[3]}.
\tag{3}
\]
A separate slice assumption is unnecessary for this branch:
\[
\sigma=\frac{(h_3)_4}{\lambda}\in B,
\qquad E(\sigma)=1.
\tag{4}
\]
Thus this theorem applies in particular to the sliced residual case
in the pass 39 note.

All Jacobian ranks below are taken over \(\operatorname{Frac}B\).
Constant vectors are also used to denote constant vector fields:
\(T_b=\sum b_iT_i\).

## 2. Full companion rows produce two invariant coefficients

Put \(F_t=\exp(tE)x\). Actual conjugation of the coordinate partials
gives
\[
\mathcal C(t)=I-tJ+\frac{t^2}{2}u e_4^{\mathsf t}
                    +\frac{t^3}{6}v e_4^{\mathsf t},
\qquad \operatorname{Jac}(F_t)\mathcal C(t)=I.
\tag{5}
\]
The companion matrix is
\[
M=\begin{pmatrix}
J&-u/2&-v/6\\
e_4^{\mathsf t}&0&0\\
0&1&0
\end{pmatrix}.
\tag{6}
\]
The Schur complement of the lower block in \(I-tM\) is
\(\mathcal C(t)\). The polynomial flow has Jacobian determinant
one, so \(\det(I-tM)=1\), \(M^6=0\), and
\[
(M^r)_{1:4,1:4}=\frac{\operatorname{Jac}h_r}{r!}.
\tag{7}
\]
These are the actual-flow identities proved in pass 39; no arbitrary
nilpotent matrix is being substituted for the action.

The last two rows carry additional information. For \(r\geq2\),
their first four entries are respectively
\[
(M^r)_{5,1:4}=\frac{d(h_{r-1})_4}{(r-1)!},\qquad
(M^r)_{6,1:4}=\frac{d(h_{r-2})_4}{(r-2)!}.
\tag{8}
\]
This follows by multiplying the last rows of (6); the symbol \(d\)
in (8) denotes the full row of ordinary partial derivatives.

The matrix \(M^5\) has rank at most one. Its upper-left block is
\(\operatorname{Jac}h_5/120\), and its last row, restricted to
the first four columns, is \(\lambda\,d\sigma/6\). Since
\(E\sigma=1\), that row is nonzero. All rows of
\(\operatorname{Jac}h_5\) are therefore proportional to
\(d\sigma\). Evaluation on \(E\), using \(Eh_5=c\), fixes
the proportionalities and yields
\[
h_5=c\sigma+d,\qquad d\in\mathbb C^4,\quad d_4=0.
\tag{9}
\]
Here and below an unadorned vector \(d\) is the constant vector in
(9), rather than the differential symbol used in row formulas.

In particular \(M^5\ne0\), so its Jordan form over the fraction
field is a single block of size six. Thus \(\operatorname{rank}M^4=2\).
The first four columns of \(M^4\) contain the rows of
\(\operatorname{Jac}h_4/24\), \(\lambda\,d\sigma/6\), and
\(d q/2\), where \(q=(h_2)_4\). Consequently
\[
\operatorname{rank}\operatorname{Jac}(h_4,\sigma,q)\leq2.
\tag{10}
\]
Define
\[
\tau=q-\frac{\lambda\sigma^2}{2},\qquad
k=h_4-\frac{c\sigma^2}{2}-d\sigma.
\tag{11}
\]
Then \(E\tau=E k=0\), and \(k_4=\lambda\). Elementary row
operations in (10) give rank at most two for the joint map
\((k,\sigma,\tau)\). Its \(d\sigma\) row is independent of
all the invariant rows because its value on \(E\) is one. Hence
\[
\operatorname{rank}\operatorname{Jac}(k,\tau)\leq1.
\tag{12}
\]
The joint map, rather than just \(k\) alone, is essential.

## 3. Good partials force the invariant relation to be affine

Set \(W_i=[E,T_i]\) for \(i\leq3\). Conjugation gives
\((T_i+tW_i)(F_t(x_j))=\delta_{ij}\).
The coefficient of \(t^4\) in its fourth component, using the
constant value \((h_4)_4=\lambda\), first gives
\(W_i\sigma=0\). The coefficient of \(t^3\) in that component,
and the coefficient of \(t^5\) in the full vector identity, give
\[
W_i\tau=-\frac{\lambda}{3}T_i\sigma,
\qquad
W_i k=-\frac{c}{5}T_i\sigma.
\tag{13}
\]
Every coefficient follows from the actual Taylor factorials.

There is at least one good index \(i\) for which
\(T_i\sigma\ne0\). Otherwise \(\sigma=\phi(x_4)\) for a
univariate polynomial \(\phi\), and
\[
1=E\sigma=\phi'(x_4)E(x_4)
\]
would make both factors nonzero constants in the polynomial ring.
Then \(E^2(x_4)=0\), contrary to \(E^4(x_4)=\lambda\ne0\).
For this index, (13) shows \(W_i\tau\ne0\), so \(d\tau\ne0\).

By (12), each \(dk_j\) is a rational multiple of \(d\tau\).
Evaluate the proportionality on the chosen \(W_i\) and use (13).
The multiplier is the constant \(3c_j/(5\lambda)\). It follows that
\[
k=\frac{3c}{5\lambda}\tau+e,
\qquad e\in\mathbb C^4,\quad e_4=\lambda.
\tag{14}
\]
Indeed the differential of the difference is zero, and the common
kernel of the four ordinary partials on \(B\) is \(\mathbb C\).
This proof uses no polynomial-curve parameter or curve-factorization
theorem. It also rules out a constant \(\tau\) in this configuration.

## 4. The resulting nice commuting field is polynomial

The actual identity \(\mathcal C(t)P(F_t)=P\) has the following
three relevant coefficients. Its coefficient of \(t^6\) gives
\[
Jc=\frac{10\lambda}{3}v.
\tag{15}
\]
Its coefficient of \(t^5\) is
\[
\frac c{120}-\frac{Jh_5}{24}
      +\frac{\lambda u}{12}
      +\frac{\lambda\sigma v}{12}=0.
\]
Using (9) and (15), this becomes
\[
Jd=\frac c5+2\lambda u-\frac{4\lambda\sigma}{3}v.
\tag{16}
\]
The coefficient of \(t^4\) gives
\[
Jh_4=\frac{h_5}{4}+\frac{3\lambda\sigma}{2}u+qv.
\]
Substitute (9), (11), (14), (15), and (16) to obtain
\[
Je=\frac{c\sigma}{20}+\frac d4-\frac{\lambda\sigma}{2}u
            +\left(\frac{\lambda\sigma^2}{6}-\tau\right)v.
\tag{17}
\]

Define the polynomial vector and its derivation
\[
z=e+\frac\sigma4d+
       \left(\frac{\sigma^2}{20}+\frac{3\tau}{10\lambda}\right)c,
\qquad Z=z\mathbin{\cdot}\partial.
\tag{18}
\]
Since \(E\sigma=1\) and \(E\tau=0\),
\[
E(z)=\frac d4+\frac{\sigma c}{10}.
\]
Equations (15)--(17) give exactly the same value for \(Jz\).
Thus
\[
[E,Z]=0,\qquad Z(x_4)=\lambda.
\tag{19}
\]
The second assertion uses \(c_4=d_4=0\) and \(e_4=\lambda\).

The commutation is now applied to the actual iterates defining
\(\sigma\) and \(\tau\), not to formal placeholders:
\[
Z\sigma=\frac{E^3(Zx_4)}{\lambda}=0,
\qquad
Z\tau=E^2(Zx_4)-\lambda\sigma Z\sigma=0.
\tag{20}
\]
Therefore \(Z(z)=0\). In particular \(Z^2(x_i)=0\) on every
ambient generator. The Leibniz rule makes \(Z\) an LND on \(B\):
the \((r+1)\)-st iterate kills any product of at most \(r\)
coordinate generators. Equivalently its genuine polynomial flow is
\(x\mapsto x+t z(x)\), with inverse \(x\mapsto x-t z(x)\).
This is the nice property that was not justified for the uncorrected
highest coefficient fields in previous controls.

## 5. Coordinate-slice recognition and an explicit splitting

Put \(t_0=x_4/\lambda\) and \(R=\ker Z\). The slice theorem
gives \(B=R[t_0]\). Since \(t_0\) is also an actual ambient
coordinate, the quotient calculation is
\[
R\simeq B/(t_0)\simeq\mathbb C^{[3]}.
\tag{21}
\]
For an explicit coordinate realization, let
\[
y_i=x_i-t_0 z_i\quad(1\leq i\leq3).
\tag{22}
\]
The slice projection \(\pi(f)=\sum_{j\geq0}(-t_0)^jZ^j(f)/j!\)
maps \(x_i\) to \(y_i\), maps \(x_4\) to zero, and has image
\(R\). Hence \(R=\mathbb C[y_1,y_2,y_3]\). One can also see
the inverse directly: \(Z\sigma=Z\tau=0\) means that \(z_i\)
equals its value on the section \((y_1,y_2,y_3,0)\), and
\[
x_i=y_i+t_0 z_i(y_1,y_2,y_3,0),\qquad x_4=\lambda t_0.
\tag{23}
\]
These are polynomial identities, not a Jacobian-only assertion.

Commutation in (19) makes \(D=E|_R\) an LND of \(R\).
By (4) and (20), \(\sigma\in R\) and \(D\sigma=1\), so
\(D\ne0\). The classical three-variable kernel theorem gives
\[
K:=\ker D\simeq\mathbb C^{[2]},\qquad R=K[\sigma].
\tag{24}
\]
The first assertion is the established Miyanishi theorem, explicitly
recalled as Theorem 2.8 in Dasgupta and Gaifullin; the second is the
slice theorem.[^kernel]

Finally \(p=E(t_0)\) belongs to \(R\), since
\(Z(p)=E(Zt_0)=E(1)=0\). Write its finite polynomial expansion
\[
p=\sum_{j=0}^N p_j\sigma^j,\quad p_j\in K,\qquad
H=\sum_{j=0}^N\frac{p_j}{j+1}\sigma^{j+1}\in R.
\]
Then \(D(H)=p\), and
\[
\xi=t_0-H\in\ker E,\qquad
B=K[\sigma,\xi],\qquad E=\partial_\sigma,
\qquad \ker E=K[\xi]\simeq\mathbb C^{[3]}.
\tag{25}
\]
No assertion that an arbitrary slice on \(\mathbb C^{[4]}\) is
an ambient coordinate has been used. The second action's coordinate
slice, the genuine coordinate-three-ring, and its inherited slice
are the separate gates that make this conclusion possible.

## 6. Verification and boundary

The complete proof has been separately reconstructed in this pass by
the main agent and two other AI agents. That is independent AI review,
not expert review. The independently implemented standalone checker
[cubic_degree_six_checks_pass40.py](cubic_degree_six_checks_pass40.py)
imports only `unittest` and `sympy`. Its five methods passed in
0.396 seconds in the implementing agent's run. After a separate full
file read, this proof's author independently reran all five methods:
they passed in 0.395 seconds.

The controls cover the full companion auxiliary rows on an actual
lower-degree action, the top Taylor factors and corrected commutator,
the rank-one differential ratio and its missing-rank negative control,
an actual nice coordinate-slice inverse, and a genuine commuting
polynomial integration/splitting. The coefficient method also checks
the corresponding constant-top degree-five factors, without claiming
that a localized rational field is a polynomial action. Such finite
controls do not replace the universal proof, and this note does not
claim to have constructed an actual degree-six example.

The result is a closure of the case (1)--(2). Other one-cubic-column
cases must retain their own hypotheses. In particular this proof does
not turn a field with rational coefficients on an invariant open set
into a polynomial LND on all of \(\mathbb A^4\).

[^kernel]: Nikhilesh Dasgupta and Sergey Gaifullin,
[*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510),
arXiv:2306.00510v2, Theorem 2.5 on PDF p. 5 and Theorem 2.8 on
PDF p. 6, both complete statements directly read in this pass.
Theorem 2.8 is explicitly credited there to Miyanishi. These are
established external inputs, not new theorems asserted here.
