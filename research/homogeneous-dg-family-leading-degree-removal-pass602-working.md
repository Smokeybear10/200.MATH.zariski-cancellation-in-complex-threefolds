# Leading-degree removal for the full ordinary-homogeneous DG family

## 1. Exact bounded conclusion

Let \(n\ge1\), and take arbitrary complex coefficients
\(c_0,\ldots,c_n\), with \(c_0\ne0\). On the actual ring
\(R=\mathbb C[x,y,z]\), set
\[
\begin{gathered}
 F(x,f)=\sum_{j=0}^{n}c_jx^{2(n-j)}f^j,
 \qquad f=xz-y^2,\qquad r=xF(x,f)+yf^n,\\
 a=2n+1,\qquad M=4n+1,\qquad N=8n+2=2M,\\
 g=\frac{f^{2n+1}+r^2}{x},\qquad
 H=\operatorname{Jac}(f,g,\cdot).
\end{gathered}
\tag{1}
\]
The Jacobian convention uses the ordered rows \(f,g,\cdot\).
This is the entire family \(F(x,f)=S(x^2,f)\), with \(S\)
homogeneous of degree \(n\) and nonzero \(x^{2n}\) coefficient.
Its derivation is ordinary homogeneous of degree \(4n\).

For every integer \(q\ge1\), put \(\ell=4n+q\). If an ordinary
homogeneous polynomial \(\psi\in R_\ell\) satisfies
\[
 \deg_H\psi=qN-1,
\tag{2}
\]
then there is a nonzero complex number \(\alpha\) such that
\[
 \deg_H\bigl(\psi-H(\alpha z^q)\bigr)<qN-1.
\tag{3}
\]
The zero remainder is allowed, with degree \(-\infty\). All
coefficients \(c_1,\ldots,c_n\) are retained. In particular the
conclusion is not restricted to \(F=x^{2n}\).

The proof gives an explicit coefficient rule. After the actual linear
normalization below, expand \(\psi/z^\ell\) in the monic-key basis
of Section 4. If \(\beta\ne0\) is its coefficient at
\(Y^{4n}K\), then
\[
 \alpha=\frac{\beta}{qNc_0}.
\tag{4}
\]
The same number works with the original, unnormalized coordinate
\(z\), not just the new coordinate introduced in the proof.

This is a selected leading-degree removal statement. It does not
remove all of \(\psi\), assert membership in \(H(R)+\ker H\),
recognize an arbitrary extension kernel, or cover all homogeneous
rank-three LNDs. It does not assert a decrease of a globally minimal
coordinate complexity. The proof is self-contained for (3); identifying
the family with the published rank-three examples is separate.

## 2. Whole polynomial input and intrinsic degree

The quotient in (1) is the whole polynomial
\[
 g=zf^{2n}+2yF(x,f)f^n+xF(x,f)^2.
\tag{5}
\]
Direct Jacobian differentiation gives
\[
 Hf=Hg=0,\qquad Hr=-gf^n,\qquad Hx=-2rf^n.
\tag{6}
\]
In particular \(H\ne0\). Both \(f\) and \(g\) are nonzero;
for the latter, setting \(y=z=0\) in (5) gives
\(c_0^2x^{4n+1}\).

The following are full identities in the localization at \(fg\):
\[
 x=\frac{f^a+r^2}{g},\qquad
 y=\frac{r-xF(x,f)}{f^n},\qquad
 z=\frac{g-2rF(x,f)+xF(x,f)^2}{f^{2n}}.
\tag{7}
\]
Thus
\(R_{fg}=\mathbb C[f^{\pm1},g^{\pm1},r]\).
Transcendence degree shows that \(f,g,r\) are algebraically
independent. On this Laurent polynomial ring,
\(H=-gf^n\partial_r\), so it is locally nilpotent. Since its
original Jacobian formula preserves \(R\), it is an LND of \(R\).
These arguments work for \(n=1\) as well as \(n\ge2\).

In \(\mathbb C(f,g)[r]\), all terms of \(F\) with \(j>0\)
have lower \(r\)-degree than its \(c_0x^{2n}\) term. Formula (7)
therefore gives the exact degrees and leading coefficients
\[
\begin{array}{c|c|c}
 &\deg_r&\text{leading coefficient in }r\\ \hline
 x&2&g^{-1}\\
 y&2a&-c_0f^{-n}g^{-a}\\
 z&N&c_0^2f^{-2n}g^{-M}.
\end{array}
\tag{8}
\]
For the last row, one may use either the last formula of (7),
or \(xz=f+y^2\) and the first two rows. All displayed leading
coefficients are nonzero. The LND degree on \(R\) is exactly
this polynomial \(r\)-degree. Hence
\(\deg_H(x,y,z)=(2,4n+2,N)\).

The degree extends to a valuation on \(\operatorname{Frac}R\)
by setting \(\nu(P/Q)=\deg_HQ-\deg_HP\) for nonzero polynomials.
Additivity follows either from the highest Leibniz coefficient or
from (7). The usual minimum rule holds, with equality when the
minimum term in a finite sum is unique. All later rational
expressions are used only in this valuation field; they are not
declared ambient coordinates.

## 3. The actual linear normalization of the last coefficient

The following complex linear map has determinant one:
\[
 x'=x,\qquad y'=y+c_nx,\qquad
 z'=z+2c_ny+c_n^2x.
\tag{9}
\]
Its full inverse is
\[
 x=x',\qquad y=y'-c_nx',\qquad
 z=z'-2c_ny'+c_n^2x'.
\tag{10}
\]
It fixes \(f\), since \(x'z'-(y')^2=xz-y^2\), and rewrites
the same \(r\) as
\[
 r=x'\sum_{j=0}^{n-1}c_j(x')^{2(n-j)}f^j+y'f^n.
\tag{11}
\]
It also leaves the displayed formula for \(g\) unchanged, with
the new coordinate expressions. Determinant one preserves the
Jacobian convention for \(H\). Thus this is an actual coordinate
normalization within the family, not a coefficient-field shear.

The map is ordinary linear, so it preserves every ordinary
homogeneous degree. By (8), its added terms have strictly lower
\(H\)-degree than the coordinates to which they are added.
Consequently the degrees and leading coefficients of \(y,z\)
are unchanged. This includes \(c_n=0\), when the map is the identity.

Until Section 6, relabel these coordinates \(x,y,z\). We may
therefore assume \(c_n=0\), keeping every other coefficient
arbitrary. The normalization is needed to make the key polynomial
monic, rather than assuming the monomial-case basis still works.

## 4. A monic key with every remaining coefficient retained

In \(\operatorname{Frac}R\), define
\[
 U=x/z,\quad Y=y/z,\quad V=f/z^2=U-Y^2,\quad
 \rho=r/z^a,\quad G=g/z^M.
\tag{12}
\]
The variables \(Y,V\) are algebraically independent over
\(\mathbb C\), since \(x/z,y/z\) are and \(U=Y^2+V\).
By (8) and invariance of \(f,g\),
\[
 \nu(U)=8n,\quad \nu(Y)=4n,\quad \nu(V)=4M,
 \quad \nu(\rho)=aN-1=8na+M,\quad \nu(G)=MN.
\tag{13}
\]
Put
\[
 P(U,V)=\sum_{j=0}^{n-1}c_jU^{a-2j}V^j,\qquad
 K=V^n+\sum_{j=0}^{n-1}c_jY^{M-4j}V^j.
\tag{14}
\]
Every exponent of \(Y\) in (14) is positive. The key \(K\)
is monic of degree \(n\) in \(V\).

The original defining equation \(r=xF+yf^n\), including all its
coefficients, gives the exact identity
\[
\begin{aligned}
 \rho&=P(Y^2+V,V)+YV^n\\
 &=YK+
 \sum_{j=0}^{n-1}\sum_{l=1}^{a-2j}
 c_j\binom{a-2j}{l}
 Y^{2a-4j-2l}V^{j+l}.
\end{aligned}
\tag{15}
\]
All exponents in this entire tail are nonnegative. Every nonzero
tail monomial has valuation
\[
 8na+4j+l(8n+4)>8na+M=\nu(\rho).
\tag{16}
\]
The strict inequality uses \(l\ge1\) and \(8n+4>M\), and
does not require any \(c_j\), \(j>0\), to be nonzero.
It follows from (15) that
\[
 \nu(K)=\nu(\rho)-\nu(Y)=M^2,
 \qquad \operatorname{in}_{\nu}(\rho)
       =\operatorname{in}_{\nu}(YK).
\tag{17}
\]
Here \(\operatorname{in}_{\nu}\) denotes the actual leading class
in the valuation filtration, not substitution of only selected
terms in the defining polynomials.

Monicity gives the finite, unique polynomial decomposition
\[
 \mathbb C[Y,V]
 =\bigoplus_{j=0}^{n-1}\mathbb C[Y,K]V^j.
\tag{18}
\]
For completeness, adjoining an independent symbol \(T\) and
quotienting \(\mathbb C[Y,T,V]\) by \(K(Y,V)-T\) gives
\(\mathbb C[Y,V]\). Division by this monic polynomial in \(V\)
gives the free basis \(1,V,\ldots,V^{n-1}\) over
\(\mathbb C[Y,T]\), proving (18). No formal completion or
unlicensed division by a nonconstant leading coefficient is used.

## 5. The one-dimensional leading piece at the required value

Let
\[
 L_*=4nN+1.
\tag{19}
\]
For the homogeneous \(\psi\) in (2), division by \(z^\ell\)
gives a polynomial in \(U,Y\), hence in \(Y,V\), and
\[
 \nu(\psi/z^\ell)=\ell N-(qN-1)=L_*.
\tag{20}
\]
A basis monomial from (18) has valuation
\[
 \nu(Y^iV^jK^k)=4ni+4Mj+M^2k,
 \qquad i,k\ge0,\quad 0\le j<n.
\tag{21}
\]
Since \(L_*<2M^2\), only \(k=0,1\) can contribute at or
below \(L_*\). For those two values, reduction modulo four
distinguishes \(k\), because \(M^2\equiv1\pmod4\).
For a fixed \(k\), equality of two values would give
\(n(i-i')+M(j-j')=0\). As \(\gcd(n,M)=1\) and
\(|j-j'|<n\), it follows that \(j=j'\) and \(i=i'\).
Thus all normal-form monomials at or below this cutoff have
distinct valuations.

The equation that (21) equals \(L_*\) forces \(k=1\), and then
\(ni+Mj=4n^2\). Reduction modulo \(n\) forces \(j=0\),
and then \(i=4n\). Consequently the only such monomial is
\(Y^{4n}K\). A unique minimum cannot cancel in a finite sum;
all terms with \(k\ge2\) have value greater than \(L_*\).
Equation (20) and the finite normal form therefore prove
\[
 \operatorname{in}_{\nu}(\psi/z^\ell)
 =\beta\operatorname{in}_{\nu}(Y^{4n}K)
 \quad\text{for a unique }\beta\in\mathbb C^*.
\tag{22}
\]
This argument needs distinct values only below the displayed cutoff.
It makes no assertion of global uniqueness of all valuations or
of a finite generating set for an arbitrary initial algebra.

## 6. Exact derivative coefficient and transport back

Differentiating \(r=xF(x,f)+yf^n\) using (6) and \(Hf=0\)
gives \(Hy=-g+2r\partial_x(xF(x,f))\), where the indicated
partial derivative holds \(f\) fixed. Then \(Hf=0\) also gives
the entire identity
\[
 \frac{Hz}{z^M}
 =\frac{-2YG+4Y\rho P_U(U,V)+2\rho V^n}{U}.
\tag{23}
\]
The divisions here take place only in \(\operatorname{Frac}R\).
They are not changes of ambient coordinates.

From \(U=Y^2+V\) and (13),
\(\operatorname{in}_{\nu}U=\operatorname{in}_{\nu}(Y^2)\).
In \(P_U\), its \(j=0\) term has valuation \(8n(a-1)\);
the other nonzero terms have this value plus \(4j\).
Its leading class is therefore that of \(ac_0Y^{2a-2}\).
Likewise (14) and (17) give
\(\operatorname{in}_{\nu}(V^n)
=-c_0\operatorname{in}_{\nu}(Y^M)\): the other summands have
strictly greater value than \(4nM\).

The first term on the right of (23) has valuation \(L_*+M\).
The second and third have value \(L_*\), with coefficients
\(4ac_0\) and \(-2c_0\), respectively, on
\(\operatorname{in}_{\nu}(Y^{4n}K)\). Their sum is nonzero,
because \(4a-2=N\) and \(c_0\ne0\). Hence
\[
 \operatorname{in}_{\nu}(Hz/z^M)
 =Nc_0\operatorname{in}_{\nu}(Y^{4n}K),
 \qquad
 \operatorname{in}_{\nu}(H(z^q)/z^\ell)
 =qNc_0\operatorname{in}_{\nu}(Y^{4n}K).
\tag{24}
\]
The second identity uses \(\ell=4n+q\) and the full equality
\(H(z^q)=qz^{q-1}Hz\). Equations (22)--(24) prove (3)--(4)
in the normalized coordinates.

Finally restore the original notation \(z'=z+2c_ny+c_n^2x\)
from (9). By (8),
\(\deg_H(z'-z)<N\). The full binomial difference thus gives
\(\deg_H((z')^q-z^q)<qN\), and applying \(H\) gives
\[
 \deg_H\bigl(H((z')^q)-H(z^q)\bigr)<qN-1.
\tag{25}
\]
If the binomial difference is invariant or zero, its derivative
is zero and the same inequality holds by convention. Thus the
same \(\alpha\) cancels the original leading term using the
original \(z^q\). Ordinary homogeneity is preserved throughout,
so the remainder is still homogeneous of degree \(\ell\), unless
zero. This proves the stated actual-coordinate conclusion.

## 7. Scope and verification

The family in (1) is the ordinary-homogeneous subfamily of
[Dasgupta--Gaifullin, Theorem 5.7](https://arxiv.org/html/2306.00510v2).
Its \(m=2\), \(n\ge1\), and \(F(x,0)=c_0x^{2n}\notin\mathbb C\)
satisfy that theorem's hypotheses. The theorem and its complete
proof were read, but no rank classification is needed in the proof
above. In particular nothing here classifies every homogeneous
rank-three LND as belonging to this family.

Fresh unsaved algebra retained all symbolic \(c_j\) in the full
linear shear, its inverse and determinant, the key identity (15),
and the complete tail support for \(n=1,2,3\). Separate whole
localized \(r\)-polynomials for \(n=1,2\) verified every entry
of (8) and the exact coefficient \(Nc_0\) in (24). Those finite
checks support the uniform support and normal-form proofs, rather
than substituting for them. No saved checker was executed, imported,
or compiled. No canonical file or neighboring source was edited.

Only the leading \(H\)-degree in (2) is removed. This does not
provide complete image membership, a terminating recognition
algorithm, a globally minimal-frame descent, or a general
cancellation result. The source is offered for independent review
after complete author EOF review and final hash handoff.
