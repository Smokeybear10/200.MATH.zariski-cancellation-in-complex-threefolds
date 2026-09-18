# Reducible fibers force source gluing, not an arbitrary positive lattice basis

The remaining cubic profiles with a multiplicity-four or multiplicity-five
component require multibranch gluing in the actual intermediate quotient
curve. The profiles are not excluded by the integral support lattice
alone: explicit finite reduced curve covers admit the required gluing,
and positive integral bases satisfy the resulting necessary identities.
These controls do not construct the exceptional surface, its map to that
curve, or an original polynomial action.

## 1. Actual component columns and their support

Retain the actual nonconical setting, fully retained exceptional curve
and finite factorization of
[ramification92](nonconical-irreducible-fiber-ramification-pass92.md).
Fix a closed exceptional value b. Let r be the number of normalized
base branches, q the number of normalized source points above them,
and c the number of irreducible components \(C_i\) of the whole
reduced fiber. Partition the q source points by their base branches;
their ramification indices \(e_a\) satisfy
\(\sum_{a\text{ over }j}e_a=N_j\in\{2,3\}\).

Use the positive complex orientations of the component Thom classes.
The exact support diagram gives columns \(v_i\) with
\[
\begin{gathered}
T:\mathbb Z^q\to\mathbb Z^r,\qquad T(e_a^{\rm std})=e_a w_j,
\qquad L=T^{-1}(\mathbb Z\mathbf1),\\
(v_1,\ldots,v_c)\text{ is an integral basis of }L,\qquad
Tv_i=\mu_i\mathbf1,\qquad c=q-r+1.
\end{gathered}
\tag{1}
\]
Here \(\mu_i\) is the generic scheme multiplicity of the actual
component, not the multiplicity of the fixed scheme. The basis in
(1) is supplied by those actual components; it cannot be replaced
by an arbitrary basis and then asserted to come from an action.

Two further facts retain geometric information. First every entry
of \(v_i\) is nonnegative. At a general point of \(C_i\), take a
small transverse complex surface. Its intersection with the reduced
exceptional divisor is a complex curve germ. The boundary Thom cycle
is the sum of the positively oriented links of its branches. Each
branch maps, after normalization, to a source-curve puncture with
positive holomorphic winding degree. Adding these degrees gives the
coefficient in question; a puncture not met has coefficient zero.

Second \(\kappa(C_i)\) is one actual point \(z_i\in\theta^{-1}(b)\),
because the latter set is finite and \(C_i\) is irreducible. Its
column is supported only on normalization points lying over \(z_i\).
This follows by taking the above neighborhood small enough to avoid
the other actual points of Z. Thus distinct points of Z give disjoint
blocks of possible column support, even if their normalization points
have the same image b.

Put \(m_j=\gcd\{e_a:a\text{ over }j\}\). The actual basis gives
the useful identity
\[
\boxed{\quad
\gcd_i\mu_i=\operatorname{lcm}_j m_j,
\qquad \gcd(m_j,m_k)=1\ (j\ne k),
\qquad (v_i)_a>0\Longrightarrow a\text{ lies over }z_i.
\quad}
\tag{2}
\]
Indeed \(T(L)=\operatorname{im}T\cap\mathbb Z\mathbf1
=\operatorname{lcm}_j(m_j)\mathbb Z\mathbf1\).
The other description of this image from its actual basis is
\(\gcd_i(\mu_i)\mathbb Z\mathbf1\). Pairwise coprimality is the
retained integral cokernel calculation. The support and positivity
are separate geometric requirements, not consequences of that gcd.

## 2. Profiles with a multiplicity-one companion

Consider \((\mu_1,\mu_2)=(1,M)\), with \(M=4\) or 5.
The component count gives \(q=r+1\). Each base branch must have
at least two normalized preimages: otherwise its single index is
\(N_j\ge2\), and its row of \(Tv_1=\mathbf1\) cannot hold.
Hence \(q\ge2r\), so \(r=1,q=2\). The only index lists are
\((1,1)\) and \((1,2)\), after ordering an unramified point first.
Positivity and \(Tv_1=1\) make \(v_1=(1,0)^t\), after swapping
the points if necessary in the first case. Since here \(L=\mathbb Z^2\),
the other column has the exact form
\[
T=(1,e),\quad e\in\{1,2\},\qquad
v_1=\binom10,\qquad
v_2=\binom{M-e}{1},\qquad M-e>0.
\tag{3}
\]
Its second entry is one because the determinant is a unit and the
entry is nonnegative. Both source normalization points occur in
\(v_2\), so they must be glued to the **same actual point of Z**.
The multiplicity-one component maps there as well. If those two
source points remain distinct in Z, either profile is impossible.
There is one analytic base branch, not necessarily a smooth embedded
base curve.

For \((4,1,1)\), the same single-index argument and
\(q=r+2\) imply \(r\le2\). If \(r=1\), there are three
unramified points of a cubic cover. The two multiplicity-one columns
are distinct standard vectors. The heavy column has entry one at
the remaining point and nonnegative entries totaling three at the
other two, so it forces at least two source points to be glued.
If \(r=2\), both branch groups have two points. At least one
group has indices \((1,1)\): two groups of type \((1,2)\)
would force the two multiplicity-one columns to coincide, violating
their independence.

## 3. The profile (4,2)

Here \(q=r+1\), so exactly one branch group has two points;
all other groups have one point. The split group has indices
\((1,1)\) or \((1,2)\), hence gcd one. Equation (2) says that
the lcm of all group gcds is two. Every single-point group has
index two or three, and their gcds are pairwise coprime. Thus
there is exactly one further group, of index two:
\[
r=2,\quad q=3,\qquad
T=\begin{pmatrix}1&e&0\\0&0&2\end{pmatrix},
\qquad e\in\{1,2\}.
\tag{4}
\]
If both branch cover degrees are two, these may be two analytic
branches of one retained component; distinct global base components
are not forced. Degrees three and two do force distinct components.
The source's support argument at a multibranch base point makes
\(\theta^{-1}(b)\) one point. In particular these three normalized
source points are glued there. This is the exact Step 1 gate of the
retained Kaliman proof, not a general assertion about finite curves.

## 4. Finite-curve and lattice controls

The following covers show that such source gluing is itself possible
for finite reduced curves with affine-line normalizations. They are
not asserted to be the intermediate curves of a threefold action.

For \(n=2\) or 3 set
\[
t=w^n-1,\qquad
C_n=\mathbb C[t]+t\mathbb C[w]\subset\mathbb C[w],\qquad
C_n=\mathbb C[t]\oplus\bigoplus_{j=1}^{n-1}
 \mathbb C[t]\,tw^j.
\tag{5}
\]
This is a ring: products of the displayed summands remain in it.
It is finite free over \(\mathbb C[t]\), has function field
\(\mathbb C(w)\), and has normalization \(\mathbb C[w]\).
For the normalization assertion, w is integral, and inverting t
gives \((C_n)_t=\mathbb C[w]_t\). The ring is a domain, hence
reduced. Over \(t=0\) all n distinct roots of \(w^n=1\) map
to one actual point: elements of \(C_n\) have the same value at
those roots, and the remaining ideal is nilpotent in the finite
fiber algebra. All normalization indices there are one.

For the one-branch controls, take the following candidate columns:
\[
\begin{array}{c|c|c|c}
\text{profile}&Z&T&\text{columns}\\ \hline
(M,1),\ M=4,5&\operatorname{Spec}C_2&(1,1)&
 (M-1,1)^t,\ (1,0)^t\\
(4,1,1)&\operatorname{Spec}C_3&(1,1,1)&
 (2,1,1)^t,\ (1,0,0)^t,\ (0,1,0)^t.
\end{array}
\tag{6}
\]
Each displayed matrix has determinant of absolute value one and
therefore is an entire basis of L. Its weighted column sums are
the stated multiplicities. Every nonzero entry is compatible with
the actual gluing in (5). In particular the first control does
not pretend that its heavy column can meet two distinct actual
points of Z.

For \((4,2)\), take the base nodal union of two axes with ring
\(G=\mathbb C[t,s]/(ts)\). Its normalized covers have parameters
w and a with \(t=w^2-1\) on the first axis and \(s=a^2\) on
the second. Use the reduced curve ring
\[
\begin{gathered}
C_{\rm cross}=
\{(f(w),g(a))\in\mathbb C[w]\times\mathbb C[a]:
 f(1)=f(-1)=g(0)\},\\
t\longmapsto(w^2-1,0),\qquad
s\longmapsto(0,a^2),\\
T=\begin{pmatrix}1&1&0\\0&0&2\end{pmatrix},\qquad
v_1=(1,3,2)^t,\qquad v_2=(1,1,1)^t.
\end{gathered}
\tag{7}
\]
The product normalization is finite over G. Its G-submodule
\(C_{\rm cross}\) is therefore finite too; it is a ring and
reduced as a subring of a product of domains. The normalization
map is finite and birational on each component, since away from
the finitely many identified points the conductor permits every
function on either component separately. Its three normalization
points above the node have one common image, so all nonzero column
entries have compatible support. In the lattice
\(L=\{(x,y,z):x+y=2z\}\), the coordinates (x,z) identify L
with \(\mathbb Z^2\). The two columns become (1,2) and (1,1),
whose determinant is minus one. Their T-images are respectively
\(4\mathbf1\) and \(2\mathbf1\).

These controls realize the finite curves and their gluing, and
verify the entire integer basis rather than a sublattice. They
do **not** realize these bases as actual Thom columns: a surface
\(E_\Gamma\), a morphism \(\kappa\), a smooth contractible
threefold, and the required original coordinate inverse have not
been constructed. They therefore show only that the tested
lattice, positivity and curve-gluing conditions do not by themselves
contradict the four profiles.

## 5. An exact remaining geometric gate

There is a useful conditional exclusion independent of the controls:
\[
\boxed{\quad
Z^{\rm norm}\to Z\text{ injective over }\theta^{-1}(b)
\quad\Longrightarrow\quad
\mu_i\le3\text{ for every component over }b.
\quad}
\tag{8}
\]
Indeed a component column must meet every base branch, by its
positive \(\mu_i\) in (1), and must be supported at one point
of Z. The injectivity assumption then forces \(r=1\).
Now \(L=\mathbb Z^q\), while each actual source point permits
only one row of support. A full integral basis with such support
has exactly one column per row, of entry one. Thus
\(\mu_i=e_a\le N_1\le3\).
This condition asks for absence of multiple normalization branches
at actual points of Z; even a unibranch singularity would suffice.
It is not established for the actual exceptional curve.

### A smooth base branch cannot carry an unramified entry one at rank zero

There is a further conditional restriction that uses the actual
rank-zero hypothesis. The local proof92 gives
\(mA_{\mathfrak q_i}\subset(\mathfrak q_iA_{\mathfrak q_i})^2\);
the collapsed-plane proof also gives the exact original-coordinate
inclusion \(mB\subset\mathfrak P^2\). If a retained analytic
base branch \(\Gamma_j\) is smooth at b, then
\[
\boxed{\quad
\operatorname{rank}(d\pi)_{C_i}=0,\quad
\Gamma_j\text{ smooth at }b,\quad (v_i)_a>0,
\quad a\text{ over }j
\quad\Longrightarrow\quad e_a(v_i)_a\ge2.
\quad}
\tag{9}
\]
Only the excluded value one needs proof. It would mean
\(e_a=(v_i)_a=1\). Positivity then says that exactly one branch
of the transverse exceptional curve contributes at a, and its
map to the source normalization has degree one. Choose a linear
function on the base plane whose restriction to the smooth
\(\Gamma_j\) is a local parameter at b. Its pullback along
that normalized transverse branch has order
\(e_a\cdot1=1\). But the rank-zero inclusion puts this base
function in the square of the maximal ideal of the transverse
smooth surface. Along any normalized branch through that point,
both local surface parameters have positive order, so every
element of their square has order at least two. This contradiction
proves (9).

Consequently (M,1) with a split degree-two cover forces its unique
base branch to be singular. The same is true for (4,1,1) in the
one-base-branch, three-unramified-point case. For (4,2) with the
columns in (7), the split branch must be singular if the heavy
column comes from a rank-zero component. The degree-three (1,2)
alternative in (3) has no prohibited entry and is not excluded.
In general the condition is on the **actual** columns, not on
one freely selected control basis.

Thus the smooth-base versions of the controls in Section 4 do
not realize all necessary rank-zero data. The singular-base escape
can nevertheless be seen without changing their finite source
rings or integer columns. In (5)--(6), replace the base line by
the cusp with ring \(\mathbb C[t^2,t^3]\). The same \(C_n\)
is finite over this subring, since \(\mathbb C[t]\) is finite
over it; its base normalization and all normalized indices are
unchanged. For (7), replace the two axes by a cusp and a line
with ring \(\mathbb C[x,y]/(x(y^2-x^3))\), mapping
\(x\mapsto((w^2-1)^2,0)\) and
\(y\mapsto((w^2-1)^3,a^2)\). The product normalization, hence
its submodule \(C_{\rm cross}\), remains finite over this base.
The first normalized base parameter is still \(w^2-1\), and
the second is still \(a^2\). The offending split branch is now
cuspidal. These are again finite-curve controls only, not a
construction of the transverse surface or of an action.

The new necessary restrictions (2)--(4) and conditional gates (8)--(9)
keep the actual component support visible. The next missing input
would have to constrain how \(\kappa\) realizes that support,
or how the original frame restricts gluing. No automatic normality
of Z, action realization, freeness, or cancellation conclusion is
made here.

The full saved ramification92 and total-fiber92 proofs were reread.
The primary Kaliman source and its exact prior read scope are
recorded there: [final author PDF](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
Notation 2.3 and Proposition 3.2, particularly Step 1 and the
support diagram. No new full primary proof read or numerical run
is claimed in this pass. Root supplied the multiplicity-one
branch-count refinement; Geometry supplied the common gcd image,
source-gluing controls and the conditional unibranch-source gate.
Every pass92 and earlier file is unchanged.
