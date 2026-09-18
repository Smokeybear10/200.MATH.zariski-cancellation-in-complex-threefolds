# The leading sextic of a general rank-two binary-quartic frame

Status: bounded working actual-chart reduction. For a supplied full
initial kernel \(ZW-F_4(X,Y)\), the leading sextic of the universal
eliminant factors into six linear forms indexed by unordered pairs
of projective roots of \(F_4\). Their multiplicities are determined
exactly by the root multiplicities of \(F_4\).

Under the additional actual condition \(R\ne0\), the projected plane
curve is birational to the selected line, and its degree is bounded
by the largest pair multiplicity. In particular, a squarefree binary
quartic forces a projected line and \(L[y,\vartheta]=L[v]\).
The zero-return branch and original-coordinate recognition are not
settled here.

## 1. Supplied frame and the exact chart

Let \(F_4\in\mathbb C[\mathsf X,\mathsf Y]\) be nonzero and
homogeneous of degree four. Assume the actual globally sliced frame
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e_0=E^2Z/2,\quad h_0=E^2W/2,\\
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 =(a\tau,b\tau,e_0\tau^2,h_0\tau^2),\\
\ker\theta_0=(\mathsf Z\mathsf W-F_4(\mathsf X,\mathsf Y)).
\end{gathered}
\tag{1}
\]
The four capital-letter generators are original polynomial
coordinates, \(\tau\) is independent, and the displayed ideal is
the entire weighted initial kernel. The degrees are degrees in the
actual slice variable, not ordinary coefficient degrees.
No globally minimal frame is assumed.

Put \(s(t)=F_4(1,t)\), a nonzero polynomial of degree at most four.
The freshly read [universal184](weight-four-universal-chart-potentials-pass184-working.md)
applies with the literal original pivot \(\partial_Z\), since the
initial polynomial has nonzero \(\mathsf Z\)-partial. It supplies
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\\
t=b/a,\quad \rho=h_0/a^2,\quad q=e_0/a^2=s(t)/\rho,\quad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\quad
L[y,z,w]=L[v],\quad J_0=-a^3\in L^* .
\end{gathered}
\tag{2}
\]
In particular \(t,\rho\) are algebraically independent. The coefficient
partials extend uniquely and commute on \(L\), then fix \(v\).
The exact field \(L\) need not be rational, and \(a\) need not be a
unit of the original ring.

For \(c\in L\), use the coefficient Taylor polynomials
\[
H_j(c;U,V)=\sum_{i=0}^j
\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{3}
\]
The formal variables \(U,V\) are fixed under all coefficient
derivatives. For \(k,n,\ell,m\in L\), define
\[
\begin{gathered}
\mathfrak f=H_2(q)+H_1(k)+n,\qquad
\mathcal R=\mathfrak f_V,\qquad
S=H_3(q)+H_2(k)+H_1(n),\\
T=\ell-S,\qquad
Q=H_4(q)+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m .
\end{gathered}
\tag{4}
\]
The three universal identities needed below are
\[
\begin{gathered}
z=q_\rho w+\mathfrak f(y,\vartheta),\qquad
Rw=T(y,\vartheta),\qquad R=\mathcal R(y,\vartheta),\\
\frac{s(t)}{\rho^3}w^2
 +\mathfrak f_\rho(y,\vartheta)w+Q(y,\vartheta)=0 .
\end{gathered}
\tag{5}
\]
The quadratic coefficient is nonzero in \(L\).

## 2. Birationality is an actual nonzero-return consequence

For this section and the degree conclusions assume \(R\ne0\)
as a polynomial in \(v\). This means nonidentically zero, not
root-free. Set
\[
\mathcal C=L[y,\vartheta]\subset\mathcal O=L[v].
\tag{6}
\]
The first equation of (5) and the full return \(L[y,z,w]=L[v]\)
give \(\mathcal O=\mathcal C[w]\). Dividing the last equation of
(5) by the scalar \(s(t)/\rho^3\) gives a monic quadratic equation
for \(w\) over \(\mathcal C\). Hence
\[
\mathcal O=\mathcal C+\mathcal Cw,\qquad
R\mathcal O\subset\mathcal C.
\tag{7}
\]
This is a module equality, not a claim that \(1,w\) are a free basis.

Because \(R\in\mathcal C\setminus\{0\}\), the middle equation of
(5) also gives \(w\in\operatorname{Frac}\mathcal C\). Thus
\[
\operatorname{Frac}\mathcal C=L(v),\qquad
\mathcal C_R=\mathcal O_R.
\tag{8}
\]
In particular \(\mathcal C\) has transcendence degree one over \(L\).
Both \(y,\vartheta\) cannot be constant: otherwise (5) would make
\(w,z\) constant too, contrary to the actual whole-line return.
The finite normal ring \(\mathcal O\) is the normalization of
\(\mathcal C\) in their common fraction field. None of these
statements asserts normality of \(\mathcal C\) in advance.

## 3. The universal sextic and its scaled polynomial

Eliminating \(w\) from (5), without division in \(\mathcal O\),
gives the formal polynomial
\[
\mathcal H
 =\frac{s(t)}{\rho^3}T^2
   +\mathcal R\mathfrak f_\rho T+\mathcal R^2Q,\qquad
\mathcal H(y,\vartheta)=0.
\tag{9}
\]
It has total degree at most six in \(U,V\). Its degree-six part is
\[
\mathcal H_6=
\frac{q_{\rho\rho}}2H_3(q)^2
 -R_2(H_2(q))_\rho H_3(q)+R_2^2H_4(q),
\qquad R_2=\partial_VH_2(q).
\tag{10}
\]
The minus sign comes from the leading part \(T_3=-H_3(q)\).
All lower potentials have too small a degree to contribute to (10).

Introduce \(z=\rho U/V\) only for computing this homogeneous
polynomial. Primes in the following display are derivatives in \(t\):
\[
\begin{gathered}
P_3=s'''z^3/6-s''z^2/2+s'z-s,\qquad
P_4=s''''z^4/24-s'''z^3/6+s''z^2/2-s'z+s,\\
H_3(q)=V^3P_3/\rho^4,\quad
H_4(q)=V^4P_4/\rho^5,\\
R_2=(V/\rho^3)(-s'z+2s),\qquad
(H_2(q))_\rho=(V^2/\rho^4)(-s''z^2/2+2s'z-3s).
\end{gathered}
\tag{11}
\]
Consequently
\[
\begin{gathered}
\mathcal H_6=\frac{V^6}{\rho^{11}}\Psi_s(\rho U/V),\\
\Psi_s(z)=sP_3^2
 -(-s'z+2s)(-s''z^2/2+2s'z-3s)P_3
 +(-s'z+2s)^2P_4 .
\end{gathered}
\tag{12}
\]
Its apparent division by \(V\) merely records homogenization;
the right side is a polynomial in \(U,V\).

## 4. Six pair factors, with a proof valid at all degenerations

Factor the binary quartic over \(\mathbb C\), absorbing its overall
nonzero scalar into one of its factors:
\[
F_4(X,Y)=\prod_{i=1}^4(a_iX+b_iY),\qquad
\ell_i(t)=a_i+b_it,\qquad s(t)=\prod_{i=1}^4\ell_i(t).
\tag{13}
\]
Each linear form is nonzero. A factor with \(b_i=0\) is allowed:
it represents a projective root at infinity. Repeated proportional
forms are also allowed.

The exact factorization is
\[
\boxed{\displaystyle
\Psi_s(z)=-
\prod_{1\le i<j\le4}
\left\{\ell_i\ell_j-z(\ell_i'\ell_j+\ell_i\ell_j')\right\}.}
\tag{14}
\]
Here is an elementary identity proof. Put
\(u_i=\ell_i'/\ell_i\), and let \(e_j\) be the elementary symmetric
polynomials in the four \(u_i\). Affineness of each \(\ell_i\)
gives \(s^{(j)}/(j!s)=e_j\). Thus, after division by \(s^3\),
the polynomial in (12) is
\[
\begin{gathered}
p_3^2-(2-e_1z)(-e_2z^2+2e_1z-3)p_3
             +(2-e_1z)^2p_4,\\
p_3=e_3z^3-e_2z^2+e_1z-1,\qquad
p_4=e_4z^4-e_3z^3+e_2z^2-e_1z+1 .
\end{gathered}
\tag{15}
\]
Regard the \(u_i\) first as four independent indeterminates.
Fix any pair \(i,j\), and set \(z=1/(u_i+u_j)\).
If \(k,l\) are the complementary pair, write
\[
p=u_iu_jz^2,\qquad A=(u_k+u_l)z,\qquad B=u_ku_lz^2 .
\]
Since \((u_i+u_j)z=1\), the four expressions in (15) become
\[
p_3=p(A-1),\quad p_4=p(1-A+B),\quad
2-e_1z=1-A,\quad -e_2z^2+2e_1z-3=A-p-B-1.
\tag{16}
\]
Their substitution in (15) is zero:
factoring \(p(1-A)^2\) leaves
\(p+(A-p-B-1)+(1-A+B)=0\).
Generically the six pair sums are nonzero and distinct. The
degree of (15) is at most six and its constant term is \(-1\).
It therefore equals \(-\prod_{i<j}(1-(u_i+u_j)z)\).

This equality is a polynomial identity in the four independent
\(u_i\), so it remains valid when some pair sums vanish or coincide.
Multiplication by
\(s^3=\prod_{i<j}\ell_i\ell_j\) proves (14).
Thus no generic-root hypothesis is left in the claimed identity.

Homogenizing (14) gives the especially useful original-form statement
\[
\boxed{\displaystyle
\mathcal H_6=-\rho^{-11}\prod_{i<j}D_{ij}(U,V),\qquad
D_{ij}=\ell_i\ell_jV
       -\rho(\ell_i'\ell_j+\ell_i\ell_j')U .}
\tag{17}
\]
Every \(D_{ij}\) is a nonzero linear form over \(\mathbb C(t,\rho)\):
its \(V\)-coefficient is the nonzero polynomial \(\ell_i\ell_j\).
Therefore \(\mathcal H_6\ne0\) and \(\deg\mathcal H=6\), including
every repeated-root or infinity case.

## 5. Exact multiplicities and projected degree

Two pair factors \(D_{ij},D_{kl}\) are proportional over \(L\)
if and only if
\[
\frac{(\ell_i\ell_j)'}{\ell_i\ell_j}
 =\frac{(\ell_k\ell_l)'}{\ell_k\ell_l}
\quad\Longleftrightarrow\quad
\frac{\ell_i\ell_j}{\ell_k\ell_l}\in\mathbb C^* .
\tag{18}
\]
For the first equivalence compare their nonzero \(V\)-coefficients.
The second uses that the quotient is a rational function of \(t\)
whose derivative is zero. In particular extending to \(L\) creates
no new proportionalities. The products have the same finite roots
and degree exactly when they represent the same unordered multiset
of two projective roots, with infinity counted as well.

If a projective root has multiplicity \(m_i\), pairing two copies
of it contributes \(\binom{m_i}{2}\). Pairing distinct roots of
multiplicities \(m_i,m_j\) contributes \(m_im_j\).
There are no further collisions by (18).

We recall, with proof, the plane-degree fact used to turn this into
an actual-chart restriction. Over a characteristic-zero field \(K\),
let \(K[P(v),Q(v)]\subset K[v]\) have fraction field \(K(v)\).
Its irreducible relation has total degree
\(\max(\deg P,\deg Q)\), and its top homogeneous part is a pure
power of one linear form.

Indeed, an invertible \(K\)-linear change makes
\(\deg P=i<j=\deg Q\). If \(P\) is constant, birationality forces
\(j=1\) and the assertion is immediate. Otherwise \(K[v]\) is
free of rank \(j\) over \(K[Q]\), with basis \(1,v,\ldots,v^{j-1}\).
The characteristic polynomial of multiplication by \(P\) equals
its minimal polynomial, since \(K(P,Q)=K(v)\). It is therefore
the monic irreducible relation, of degree \(j\) in its first variable.

To bound its coefficients, temporarily extend constants algebraically
and write the second variable as \(z_0^{-j}\).
The \(j\) roots of \(Q(v)=z_0^{-j}\) have expansions
\(v=z_0^{-1}(\beta+O(z_0))\), with distinct nonzero \(\beta\).
This follows by solving the simple constant roots recursively.
Each value of \(P(v)\) has pole order at most \(i\).
The coefficient of the first variable to power \(j-r\) consequently
has second-variable degree at most \(\lfloor ir/j\rfloor<r\)
for \(r>0\). All its terms have total degree below \(j\);
the top part is the first variable to power \(j\).
Undo the linear change. The temporary extension proves identities
over the original \(K\), not a new field-return hypothesis.

Apply this fact to \(\mathcal C\) using (8). Let
\(\Gamma\in L[U,V]\) generate its height-one evaluation kernel,
and write \(g=\deg\Gamma\). Since \(\Gamma\mid\mathcal H\), its
pure-power top divides (17). Therefore
\[
g\le\text{multiplicity of one of the pair factors }D_{ij},
\qquad
g=\max(\deg_vy,\deg_v\vartheta).
\tag{19}
\]
This reasoning only uses the proved birationality; it does not
assume that the projected curve is nonsingular or already the line.

The complete partition consequences are:

| Projective root multiplicities of \(F_4\) | Multiplicities in \(\mathcal H_6\) | Bound on \(g\) |
| --- | --- | --- |
| \(1+1+1+1\) | \(1,1,1,1,1,1\) | \(g=1\) |
| \(2+1+1\) | \(2,2,1,1\) | \(g\le2\) |
| \(2+2\) | \(4,1,1\) | \(g\le4\) |
| \(3+1\) | \(3,3\) | \(g\le3\) |
| \(4\) | \(6\) | \(g\le6\) |

More precisely, (19) ties the degree to the chosen leading
direction. For example a simple pair factor permits only a line
even in a repeated-root row of this table.

In particular, under the actual nonzero-return hypothesis,
\[
\boxed{F_4\text{ squarefree}\quad\Longrightarrow\quad
\deg\Gamma=1,\quad L[y,\vartheta]=L[v].}
\tag{20}
\]
The degree fact makes both projected entries affine in \(v\),
with at least one nonconstant. That affine entry generates
\(L[v]\), proving the ring equality in (20).

## 6. Boundary and verification

The factorization (17) is a formal universal identity, independent
of whether the lower data are realized by an actual frame.
The degree and ring conclusions (19)--(20), in contrast, use the
actual whole-line return and \(R\ne0\) in Sections 1--2.
Nothing here handles \(R=0\), and a nonzero \(R\) may have roots.

Even when the projected pair is a line, no coefficient-field
linear combination is declared to be an ambient coordinate.
Further full potentials and original-ring arguments would be needed
for recognition or exclusion. Results for the specialized mixed
quartic \(X^2Y^2\) are not imported into this general \(q=s(t)/\rho\)
argument.

The full universal184 source was freshly read through EOF.
New unsaved inline algebra reconstructed (10)--(12) from the
literal \(H_2,H_3,H_4\), verified the unrestricted four-slope
identity in (15), and checked the single-pair cancellation (16).
These finite identities do not establish actual field return,
the plane-degree theorem, or original-coordinate descent.
No saved checker was executed, imported, or compiled. No219,
earlier proof, index, JSON, or verification packet was changed.
This is a supplied-frame reduction, not arbitrary entry,
unrestricted cancellation, a minimum-profile theorem, expert
certification, or a novelty claim.
