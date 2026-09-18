# Nonzero quartic residues do not realize the distinct-root rank-one sector

Status: working actual-frame exclusion. The nonzero-residue models
\(Z^2-XYW+\lambda X^4+\mu Y^4\) are impossible under the supplied
globally sliced exact1122 and full-initial-kernel hypotheses.
Together with233, this excludes the distinct-root coefficient case
of the rank-one bad-quadratic sector. It does not exclude the remaining
double-root models, nor prove unrestricted cancellation.

## 1. Actual hypotheses, potentials and the previous reduction

Let \(\lambda,\mu\in\mathbb C\), with \((\lambda,\mu)\ne(0,0)\).
Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a_0=EX,\quad b_0=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(a_0T,b_0T,e_0T^2,h_0T^2)\bigr)
 =(\mathsf Z^2-\mathsf X\mathsf Y\mathsf W+
                         \lambda\mathsf X^4+\mu\mathsf Y^4).
\end{gathered}                                                     \tag{1}
\]
The capital letters are actual polynomial coordinates, and the ideal
is the entire initial kernel, not a single known relation.
The literal \(Z\) pivot gives the exact chart from
[235](rank-one-distinct-root-residue-sextic-line-reduction-pass235-working.md):
\[
\begin{gathered}
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
t=b_0/a_0,\quad \rho=h_0/a_0^2,\quad q=e_0/a_0^2,\quad
q^2=t\rho-\lambda-\mu t^4,\quad [L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2,\qquad L[y,z,w]=L[v].
\end{gathered}                                                     \tag{2}
\]
The partials extend uniquely to the finite separable field \(L\) and
fix \(v\). The elements \(t,\rho\) are algebraically independent;
\(X\) is transcendental over \(L(v)\). The full scalar-Jacobian
condition used in235 remains part of this actual chart.

With coefficient Taylor polynomials \(H_j\), all lower potentials
\(k,n,\ell,m\in L\) are retained. Put
\[
\begin{gathered}
f=H_2(q)+H_1(k)+n,\quad S=H_3(q)+H_2(k)+H_1(n),\\
Q=H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
\sigma=q_ty+q_\rho\theta+k,\quad z=q_\rho w+f(y,\theta),\\
R=q_{t\rho}y+q_{\rho\rho}\theta+k_\rho,\quad
Rw+S(y,\theta)=\ell,\\
(q_{\rho\rho}/2)w^2+f_\rho(y,\theta)w+Q(y,\theta)=0 .
\end{gathered}                                                     \tag{3}
\]
Formal coefficient derivatives precede evaluation in these formulas.
The exact derivatives needed below are
\[
q_t=\frac{\rho-4\mu t^3}{2q},\quad
q_\rho=\frac t{2q},\quad
q_{t\rho}=\frac{q^2-\lambda+3\mu t^4}{4q^3},\quad
q_{\rho\rho}=-\frac{t^2}{4q^3},\quad
q_{\rho\rho\rho}=\frac{3t^3}{8q^5}.
                                                                  \tag{4}
\]

For \(R\ne0\),235 proves that \(y,\theta\) parametrize a line and
\(\max(\deg_vy,\deg_v\theta)=1\).
If \(\lambda\mu\ne0\), only \(y\in L\), \(\deg_v\theta=1\) remains.
If exactly one residue is nonzero, there are two further line
directions, specified below. These are consequences of the complete
sextic and actual cofactor divisor, not numerical observations.

## 2. Zero return is impossible when a residue is nonzero

Suppose \(R=0\). Since \(q_{\rho\rho}\ne0\), solve it as
\[
\theta=p_0y+c_0,\qquad
p_0=-q_{t\rho}/q_{\rho\rho}
       =\frac{q^2-\lambda+3\mu t^4}{t^2},\qquad
c_0=-k_\rho/q_{\rho\rho}\in L .
\tag{5}
\]
Here \(p_0\) is held fixed as a coefficient when evaluating a Taylor
polynomial. The quadratic-relation recurrence in235 gives
\[
H_1(q;1,p_0)=q/t,\quad
H_2(q;1,p_0)=-\frac{\lambda+3\mu t^4}{2qt^2},\quad
H_3(q;1,p_0)=\frac{\lambda-\mu t^4}{2qt^3}\ne0.
\tag{6}
\]
For example the squared Taylor expansion has coefficients
\(D_1=2q^2/t\), \(D_2=p_0-6\mu t^2\), \(D_3=-4\mu t\);
the recurrence \(2qH_3=D_3-2H_1H_2\) gives (6).
Its final numerator is nonzero because \(t\) is transcendental
and the two complex residues are not both zero.

The third potential becomes \(S(y,p_0y+c_0)=\ell\).
As a polynomial in \(y\), its degree-three coefficient is exactly
the nonzero final quantity in (6). The \(k,n\) terms have degrees
at most two and one and cannot cancel it. Hence \(y\in L\),
since a nonconstant element of \(L[v]\) cannot satisfy a nonzero
polynomial equation over \(L\). Equation (5) then gives \(\theta\in L\).
The fourth potential has nonzero quadratic coefficient
\(q_{\rho\rho}/2\), and all its other coefficients now lie in \(L\).
The same degree argument forces \(w\in L\). The second potential
forces \(z\in L\), contradicting \(L[y,z,w]=L[v]\).
Thus
\[
R\ne0 .
\tag{7}
\]

## 3. A constant first projection is uniformly impossible

Suppose \(y\in L\), \(\deg_v\theta=1\). This section also works when
both residues vanish; it needs only the derivatives in the \(\rho\)
direction in (4).
The third potential has cubic leading coefficient
\(-q_{\rho\rho\rho}/6\) in \(\theta\), while \(R\) has leading
coefficient \(q_{\rho\rho}\). Therefore
\[
w=\frac{t}{4q^2}\theta^2+\lambda_1\theta+\omega,\qquad
z=\kappa\theta+\zeta,\qquad
\sigma=q_\rho\theta+q_ty+k,\quad
\lambda_1,\omega,\kappa,\zeta\in L .
\tag{8}
\]
The quadratic coefficient of \(z\) vanishes because
\(q_\rho t/(4q^2)+q_{\rho\rho}/2=0\).

Extend \(N\) to \(B=A[u]\) by \(Nu=0\) and form the actual derivation
\[
\mathcal P=a_0N-(NX)E,\quad
\mathcal PX=\mathcal PY=0,\quad [E,\mathcal P]=0 .
\tag{9}
\]
It fixes \(L\). It is locally nilpotent: on the actual localization
\(B_{a_0}=A_{a_0}[X]\), it fixes \(X\) and acts on \(A_{a_0}\)
as the locally nilpotent \(a_0N\), since \(Na_0=0\).
It preserves \(B\), so its restriction is an actual LND.
Put \(\tau=a_0N\theta\in L^*\).
Its coordinate derivatives satisfy
\[
\mathcal PZ=\tau(q_\rho X+\kappa),\quad
\mathcal P^2Z=0,\quad
\mathcal P^2W=\frac{\tau^2t}{2q^2}\ne0,\quad
\mathcal P^3W=0 .
\tag{10}
\]

For completeness the primitive division in228 applies without change
to these new coefficients. Let \(\Delta\) be the gcd of the nonzero
coordinate components of \(\mathcal P\), and \(D=\mathcal P/\Delta\).
Since \(\mathcal P\Delta=\Delta D\Delta\), the LND degree function
forces \(\mathcal P\Delta=0\). Thus \(D\) is an irreducible LND.
Writing \(\mathcal PX_i=\Delta g_i\) with \(\gcd(g_i)=1\),
commutation gives
\(\Delta\mid(E\Delta)g_i\) for every \(i\), hence
\(\Delta\mid E\Delta\). The degree function for \(E\) forces
\(E\Delta=0\), and consequently \([E,D]=0\).
In the common chart \(B_L=L[v][X]\), the common kernel of
\(E=a_0\partial_X\) and \(\mathcal P=a_0\partial_v\) is \(L\).
So \(\Delta\in L^*\), without asserting an original-ring unit.

Set \(\delta=\tau/\Delta\). Then
\[
DZ=\delta(q_\rho X+\kappa),\qquad
D^2W=\frac{\delta^2t}{2q^2}\ne0,\qquad D^2Z=D^3W=0.
\tag{11}
\]
Apply [Dasgupta--Gupta, Lemma2.3(i)](https://arxiv.org/html/1701.03635v1)
over the UFD \(S=\mathbb C[X,Y]\) to \(B=S[Z,W]\).
It gives \(DZ\in S\), \(DW\in S[Z]\).
Since \(D^3W=0\) and \(DZ\ne0\), \(DW\) is at most linear in \(Z\);
therefore \(D^2W\in S\).
This uses the UFD assertion, not a PID slice assertion.

Every nonzero polynomial in \(S\) has E-degree equal to its ordinary
total degree: its top homogeneous part \(p_d\) evaluates to
\(a_0^dp_d(1,t)\ne0\). Thus \(S\cap\ker E=\mathbb C\).
The first expression in (11) has E-degree one, and the second is
E-invariant. There are \(c_0,c_1,c_2,d_0\in\mathbb C\),
\(d_0\ne0\), such that
\[
DZ=c_1X+c_2Y+c_0,\qquad D^2W=d_0,\qquad
\delta q_\rho=c_1+c_2t.
\]
Using (4),(11) gives the impossible identity
\[
(c_1+c_2t)^2
 =\frac{\delta^2t^2}{4q^2}
 =\frac{d_0}{2}t .
\tag{12}
\]
Comparison of the quadratic and linear coefficients in the
transcendental \(t\) forces \(c_2=0\) and \(d_0=0\).
This excludes the constant-first line.

In particular, (7),235 and this section already exclude
every model with \(\lambda\mu\ne0\).

## 4. The other two single-residue directions are nice and impossible

If exactly one residue is nonzero, an actual interchange of \(X,Y\)
lets us assume \(\lambda\ne0,\mu=0\). It preserves the exact profile
and transports the entire initial ideal, interchanging the residues.
Rebuild the literal chart in this convention; do not transplant an
old return condition through the coordinate change.

Choose \(\alpha\in\mathbb C^*\) with \(\alpha^2=\lambda\).
After excluding the constant-first line,235's two double directions
give, for one \(\epsilon\in\{1,-1\}\),
\[
s_\epsilon=\frac{q+\epsilon\mathrm i\alpha}{t},\qquad
\theta=s_\epsilon^2y+c,\qquad c\in L,\qquad \deg_v y=1.
\tag{13}
\]
The two choices match the two factors of the sextic; their sign
labelling is immaterial.
Crucially \(s_\epsilon\) is transcendental over \(\mathbb C\).
Otherwise it belongs to the algebraically closed field \(\mathbb C\),
and
\(\rho=t s_\epsilon^2-2\epsilon\mathrm i\alpha s_\epsilon\)
would contradict the independence of \(t,\rho\).

Holding \(s_\epsilon\) fixed in the formal Taylor direction gives
the exact squared identity
\[
(t+\eta)(\rho+s_\epsilon^2\eta)-\lambda
                         =(q+s_\epsilon\eta)^2.
\tag{14}
\]
Here \(\eta\) is a formal indeterminate, not a field parameter.
The formal square root with constant term \(q\) is unique. Hence
\[
H_1(q;1,s_\epsilon^2)=s_\epsilon,\qquad
H_j(q;1,s_\epsilon^2)=0\ (j\ge2),\qquad
q_{t\rho}+q_{\rho\rho}s_\epsilon^2
                =-\frac{\epsilon\mathrm i\alpha}{2q^2}\ne0 .
\tag{15}
\]

Thus \(R\) has degree one in the affine parameter \(y\).
The third-potential numerator has degree at most two, because
its possible cubic coefficient is \(H_3(q;1,s_\epsilon^2)=0\).
Since \(w\) is polynomial in \(y\), it is affine in \(y\).
The second potential likewise has no quadratic term in \(y\),
because \(H_2(q;1,s_\epsilon^2)=0\). It follows that
\[
w=\lambda_1y+\omega,\quad z=\kappa y+\zeta,\quad
\sigma=s_\epsilon y+\sigma_0,\qquad
\lambda_1,\omega,\kappa,\zeta,\sigma_0\in L .
\tag{16}
\]

Construct \(\mathcal P=a_0N-(NX)E\) as in (9), now without assuming
that it fixes \(Y\), and set \(\tau=a_0Ny\in L^*\).
The same localization proof gives an actual nonzero LND.
Its original-coordinate row is
\[
\mathcal PX=0,\qquad
(\mathcal PY,\mathcal PZ,\mathcal PW)
 =\tau(1,s_\epsilon X+\kappa,s_\epsilon^2X+\lambda_1).
\tag{17}
\]
It fixes \(L,X\), so its square kills every original coordinate.
No field coefficient is being declared regular on its own.

Over \(K_X=\mathbb C(X)\), this is a nonzero nice LND of
\(K_X[Y,Z,W]\).
[Dasgupta--Gupta, Theorem3.1(i)](https://arxiv.org/html/1701.03635v1)
supplies a nonzero fixed linear form. This field assertion does
not require irreducibility. Clearing its \(X\)-denominators gives
\(l,m,n\in\mathbb C[X]\), not all zero, with
\[
l+m(s_\epsilon X+\kappa)+n(s_\epsilon^2X+\lambda_1)=0
                                                     \quad\text{in }L[X].
\tag{18}
\]
Set \(d=\max(\deg l,\deg m+1,\deg n+1)\), assigning degree
\(-\infty\) to a zero polynomial.
The coefficient of \(X^d\) in (18) is
\[
l_d+m_{d-1}s_\epsilon+n_{d-1}s_\epsilon^2=0 .
\tag{19}
\]
At least one coefficient is nonzero and all are complex.
The lower terms \(m\kappa+n\lambda_1\) have degree at most \(d-1\).
Equation (19) contradicts the transcendence just proved.
This excludes the remaining two directions.

## 5. Exhaustion and the remaining goal

Section2 excludes zero return. For nonzero return,235 leaves only
the lines handled in Sections3--4. Thus (1) is impossible for
every nonzero pair of complex residues. The pair \((0,0)\) was
excluded separately by227--233.

Combining this result with the actual normalizations in
[234](rank-one-bad-quadratic-four-model-frontier-pass234-working.md),
every supplied rank-one bad-quadratic kernel whose coefficient
of the remaining bad variable has two distinct linear factors
is excluded. The two unresolved rank-one residual models in that
classification are now
\[
Z^2-X^2W-XY^3,\qquad Z^2-X^2W-Y^4 .
\tag{20}
\]
The absent-variable and zero-residue double-root cases have the
retained recognition conclusions203 and211. This is a statement
inside the supplied exact1122, principal-weight-four class only.
Rank-zero bad quadratic part, other initial kernels, higher
profiles and arbitrary coordinate entry remain outside it.

The actual derivation and primitive-gcd arguments were reconstructed
from228--229, not inferred from a generic-field coordinate.
Both precise published inputs were freshly checked in their primary
source before use. The directional Taylor identities and uniform
constant-first coefficients have independent exact reconstructions.
Execution records and complete-source reviews belong in the ledger.
No human expert review, proof-assistant certification, novelty
clearance, public posting or external contact is claimed.
