# A rank cap for dependent quadratic low flow

With dependent defects, no complex constant defect relation, and
flow degree two, the displayed leading fields have joint rank at
most two. The full five-dimensional companion excludes rank three
without a hypothesis on the bad-speed Jacobian or projective direction.
This in particular excludes the last low-flow sector in the frozen
pass65 case map.

This closes the specified remaining low-flow sector. It does not
recognize every higher-flow two-quadratic frame or prove that an
arbitrary sliced action admits such a frame.

## 1. Actual hypotheses

Work over \(k=\mathbb C\). Let
\[
B=k[x_1,x_2,X,Y]=A[s_*],\qquad
E\in\operatorname{LND}_k(B),\quad Es_*=1,\quad A=\ker E.
\tag{1}
\]
All four displayed generators are actual polynomial coordinates.
Write \(T_i\) for their coordinate partials and assume
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{2}
\]
Define \(V_X=\operatorname{ad}_E^2T_X\) and
\(V_Y=\operatorname{ad}_E^2T_Y\).
Retain the remaining hypotheses of
[the frozen low-flow synthesis](low-flow-synthesis-pass65.md):
\[
E^3x=0,\qquad h:=E^2x\ne0,\qquad
V_X=aD,\quad V_Y=bD,
\tag{3}
\]
where \(D\) is a nonzero primitive polynomial LND,
\([E,D]=0\), and \(a,b\in\ker E\cap\ker D\) have no nonzero
complex constant linear relation. The primitive decomposition is
the one established in
[pass42](dependent-quadratic-defects-pass42.md).
Put \(W_i=[E,T_i]\) for \(i=1,2\), and define
\[
f=EX,\quad g=EY,\qquad
\mathfrak q=\dim_K\operatorname{span}\{E,W_1,W_2,D\},
\qquad K=\operatorname{Frac}B.
\tag{4}
\]
Ranks of polynomial fields mean ranks of their coefficient vectors.
The theorem proved below is \(\mathfrak q\le2\).
Suppose for contradiction that \(\mathfrak q\ge3\).

The complete highest-column argument in
[pass65](dependent-low-flow-pass65.md#2-two-full-highest-identities-kill-the-bad-top)
already proves
\[
h=(h_1,h_2,0,0)^t,\qquad Ef=Eg=0.
\tag{5}
\]
The actual good and bad conjugated columns show that
\(E,W_1,W_2,V_X,V_Y\) are commuting LNDs and all kill
\(f,g,h_1,h_2\). These are coefficient identities and do not
require independent defects.

Since \(a\ne0\), the primitive field \(D\) also kills
\(f,g,h_1,h_2\).

## 2. The exact five-dimensional companion

Set
\[
P=Ex,\quad J=\operatorname{Jac}P,\quad d=D(x),\quad
\ell=(0,0,a,b),\qquad
M=\begin{pmatrix}J&-d/2\\\ell&0\end{pmatrix}.
\tag{6}
\]
This is the weighted companion of
[pass43, Section 1](dependent-defect-top-line-pass43.md).
The actual inverse-flow identity reads
\[
\left(I-zJ+\frac{z^2}{2}d\ell\right)^{-1}
=\operatorname{Jac}(\exp(zE)x),
\quad
\det\left(I-zJ+\frac{z^2}{2}d\ell\right)=1.
\]
Schur elimination and coefficient comparison give
\[
M^5=0,\qquad (M^j)_{\mathrm{UL}}
=\frac{\operatorname{Jac}(E^jx)}{j!}.
\tag{7}
\]
No ordinary derivative of the variable row \(\ell\) is taken
in this identity.

For clarity, the rank-preserving block gate works with the one
auxiliary coordinate here. Neither the left nor the right kernel
of \(M\) contains a nonzero vector supported only on that
coordinate, because \(d\ne0\) and \(\ell\ne0\).
If \(MN=NM=0\), projecting the image of \(N\) to its first
four coordinates is injective, and restricting the rows of \(N\)
to their first four entries is injective. Therefore
\(\operatorname{rank}N=\operatorname{rank}N_{\mathrm{UL}}\).

Starting with \(M^5=0\), apply this gate to \(M^4\) and then
\(M^3\). Their upper-left blocks vanish by (3),(7). Thus
\[
M^3=0,\qquad
\operatorname{rank}M^2=\operatorname{rank}\operatorname{Jac}h.
\tag{8}
\]

Let \(F=K^4\oplus0\) be the base-coordinate hyperplane in
\(K^5\), and put
\[
U=\operatorname{span}_K\{(W_1(x),0),(W_2(x),0),(d,0)\}.
\]
Adjoining \((P,0)\) gives rank \(\mathfrak q\), so
\(\dim U\ge\mathfrak q-1\).
The first two columns of \(M\) are \((-W_i(x),0)^t\),
and its auxiliary column is \((-d/2,0)^t\). Consequently
\(U\subset\operatorname{im}M\cap F\).
The row \(\ell\ne0\) makes \(\operatorname{im}M\) project
nontrivially to the auxiliary line. Hence
\[
\operatorname{rank}M\ge \dim U+1\ge\mathfrak q\ge3.
\tag{9}
\]

A cube-zero matrix on a five-dimensional vector space has rank
at most three. Therefore \(\mathfrak q=3\).
If \(h\) were constant, (8) would give \(M^2=0\).
A square-zero matrix on a five-dimensional vector space has rank
at most two, contradicting (9). Thus \(h\) is nonconstant.

## 3. The full derivative span forces a constant good direction

Put \(s=\ell P=af+bg\). The actual inverse-flow and velocity
identities give
\[
Jh=\tfrac12s\,d,\qquad
J\operatorname{Jac}h=d\ell J.
\tag{10}
\]
For the first identity compare the quadratic coefficient in
\((I-zJ+z^2d\ell/2)(P+zh)=P\).
For the second compare the cubic coefficient in
\((I-zJ+z^2d\ell/2)(I+zJ+z^2\operatorname{Jac}h/2)=I\).

Let \(\mathcal G\) be the \(K\)-span of \(h\) and every column
of its ordinary ambient Jacobian. By (5),(10),
\[
0\ne\mathcal G
\subset K^2\oplus0,\qquad J(\mathcal G)\subset Kd.
\tag{11}
\]
If \(\dim\mathcal G=2\), it would be the entire actual good
plane over \(K\). Both good columns of \(J\) would then lie in
\(Kd\), so \(W_1,W_2\in KD\), contrary to
\(\mathfrak q=3\). Hence \(\mathcal G=Kh\).

Every ordinary differential column of \(h\) is therefore
proportional to \(h\). All four ordinary coordinate partials
kill every ratio of its nonzero components. Their common constant
field in \(k(x_1,x_2,X,Y)\) is \(k\). Consequently
\[
h=Rc,\qquad R\in B\setminus k,\qquad
0\ne c\in k^2\oplus0.
\tag{12}
\]
Choosing a nonzero constant component of \(c\) makes \(R\)
polynomial. Nonconstancy follows from the preceding exclusion
of constant \(h\). No polynomial-curve theorem, new field,
coordinate change, or claim about an entire common kernel is used.

In particular \(\operatorname{Jac}h=c\,dR\) has rank one,
where \(dR\) is the row of ordinary ambient partial derivatives.
Together with (8)--(9), this gives exactly
\[
\text{Jordan type}(M)=(3,2),\qquad
\dim\ker M=2,\quad \dim\operatorname{im}M^2=1.
\tag{13}
\]
Indeed cube zero and rank-one square require one size-three block;
the remaining two dimensions must form one size-two block to
reach rank at least three.

The first identity in (10) becomes
\[
RJc=\tfrac12s\,d.
\tag{14}
\]
The second, after substituting \(\operatorname{Jac}h=c\,dR\),
then gives
\[
(Jc)dR=d\ell J,\qquad
d\left(\frac{s}{2R}dR-\ell J\right)=0.
\tag{15}
\]
Since the column \(d\ne0\), cancellation in the field \(K\)
proves
\[
\ell J=\frac{s}{2R}dR.
\tag{16}
\]
Division by \(R\ne0\) takes place only in \(K\).
No global divisibility of \(s\) by \(R\) is presumed, and
no derivative of \(a,b\) has been discarded.

## 4. The full image line contradicts the auxiliary row

The first four columns of \(M^2\) are
\[
\binom{\operatorname{Jac}h/2}{\ell J}
=\binom{c}{s/R}\frac12\,dR,
\tag{17}
\]
where (16) supplies the auxiliary entry. This block is nonzero,
and (13) therefore identifies the whole image line:
\[
\operatorname{im}M^2
=K\xi,\qquad \xi=\binom{c}{s/R}.
\tag{18}
\]

Now use the actual coefficient vectors, embedded with zero
auxiliary entry, to form the three-dimensional space
\[
T=\operatorname{span}_K\{(P,0),(W_1(x),0),(W_2(x),0),(d,0)\}
\subset F.
\]
The actual equality \(JP=EP=h\) gives
\[
M(P,0)=(h,\ell P)=R\xi.
\]
For the other three generating vectors, the good and auxiliary
columns used before (9) give exactly
\[
M(W_i(x),0)=-M^2e_i,\qquad
M(d,0)=-2M^2e_5.
\tag{19}
\]
Thus \(T\subset M^{-1}(\operatorname{im}M^2)\). This preimage
has dimension
\(\dim\ker M+\dim\operatorname{im}M^2=2+1=3\), since
\(\operatorname{im}M^2\subset\operatorname{im}M\).
Moreover \(\operatorname{im}M\) is itself a three-dimensional
subspace of that preimage. Consequently
\[
M^{-1}(\operatorname{im}M^2)=\operatorname{im}M,\qquad
T=\operatorname{im}M\subset F.
\tag{20}
\]
This contradicts \(\ell\ne0\), which makes the auxiliary
projection of \(\operatorname{im}M\) nonzero.
The assumption \(\mathfrak q\ge3\) is therefore impossible:
\[
\boxed{\ \mathfrak q\le2.\ }
\tag{21}
\]

## 5. Exact new scope

The rank cap holds under (1)--(3), without a speed-rank or
nonconstant-projective-speed premise. No positive rank-three
example is asserted. The proof uses neither a polynomial-curve
theorem, a Wronskian invertibility hypothesis, nor a claim that
a commuting rational field is locally nilpotent.

In conjunction with the frozen pass65 case map, this recognizes
all cases with flow degree at most two under the supplied
two-quadratic frame: all other low-flow sectors were already
recognized, and the last listed sector is now excluded. The
conclusion concerns the original sliced kernel, not a localized
auxiliary quotient. It does not assert that the polynomial
\(R\) is itself an ambient coordinate.

The higher constant-top and moving-top sectors remain separate.
There is still no theorem here giving the supplied frame for an
arbitrary sliced LND of a polynomial four-ring. Thus this result
does not establish unrestricted complex-threefold cancellation
or an all-profile height-ten bound.

## Sources and verification scope

The final rank-cap proof is algebraic after the inherited actual
highest-column and weighted-companion identities. Their complete
proofs and the rank-preserving block lemma were reread in the linked
pass65/pass43/pass39 notes. Earlier working versions used a
polynomial-curve source and then an invariant-coordinate endpoint;
those external inputs were eliminated by the derivative-span
and full-preimage arguments in the final proof.
Recognition of the other low-flow sectors
retains the source obligations recorded in the frozen pass65
case map.

This note is an all-instance symbolic proof under (1)--(3).
It introduces no finite test, regression total, registry edit,
historical novelty claim, human expert review, external contact,
or proof-assistant verification. Independent proof reconstructions
and any separately assigned finite controls are recorded separately.
