# A sliced invariant-replica boundary for leading-term removal

## 1. Statement and scope

This note gives an explicitly polynomially rectified sliced extension for
which a proposed leading-term removal by a base polynomial fails. It concerns
an invariant replica of the homogeneous DG derivation, not the irreducible
base derivation itself. No assertion about an unfinished irreducible-base
argument is needed.

For a locally nilpotent derivation \(V\), \(\deg_V b\) means the largest
\(j\) with \(V^j b\ne0\), with \(\deg_V0=-\infty\). Ordinary derivation
degree instead refers to the usual homogeneous grading of the base ring.

For every integer \(n\geq1\), put

\[
\begin{aligned}
f&=xz-y^2,& r&=x^{2n+1}+yf^n,\\
g&=zf^{2n}+2x^{2n}yf^n+x^{4n+1},&
H_0&=\operatorname{Jac}(f,g,\cdot),\\
M&=4n+1,& N&=8n+2,& s&=4n+2.
\end{aligned}                                                    \tag{1}
\]

For any integer \(q\geq1\), define

\[
a=f^s,\qquad c=fg^2,\qquad H=aH_0,\qquad
P=z^q,\qquad \psi=cH_0P,\qquad
E=H+(1+\psi)\partial_t.                                           \tag{2}
\]

The following claims are proved below.

1. There are explicit finite polynomial coordinates \(Z_1,Z_2,Z_3,U\)
   of \(B=\mathbb C[x,y,z,t]\) such that \(EZ_i=0\) and \(EU=1\).
   In particular, \(\ker E=\mathbb C[Z_1,Z_2,Z_3]\).
2. The ordinary homogeneous degrees are
   \(d=\deg H=12n+4\) and \(\ell=\deg\psi=d+q\), whereas
   \(\deg_H\psi=qN-1\).
3. For every ordinary homogeneous \(Q\in\mathbb C[x,y,z]\) of degree
   \(q\), including \(Q=0\),
   \(\deg_H(\psi-HQ)=qN-1\). More strongly, no polynomial shear
   \(t\mapsto t-Q(x,y,z)\), with no homogeneity restriction on \(Q\),
   lowers the \(E\)-degree of \(t\).
4. In the actual linear coordinate frame
   \((x+z,y+z,z,t)\), the positive \(E\)-degree tuple is
   \((N,N,N,qN)\), and its weighted Euler derivation has exact
   all-ring \(E\)-filtration shift one.

Thus sliceness and the sharp degree equality do not by themselves extend a
leading-removal assertion from an irreducible derivation to all its invariant
replicas. This is not a cancellation counterexample: the entire kernel is
explicitly polynomial. It is not a globally degree-minimal frame, nor does
the argument exclude degree-lowering operations that change the base.

## 2. A finite polynomial repair lemma

The following elementary construction supplies the whole coordinate map,
including its inverse. Let \(R=\mathbb C[x_1,\ldots,x_m]\), let
\(D\in\operatorname{LND}(R)\), and suppose

\[
0\ne a\in\ker D,\qquad c\in\ker D,\qquad P\in R,
\qquad c^K\in aR\quad\hbox{for some }K\geq1.
                                                                    \tag{3}
\]

On \(B=R[t]\), set

\[
\mathcal E=aD+(1+cDP)\partial_t.
                                                                    \tag{4}
\]

This is locally nilpotent. Its restriction to \(R\) is the invariant replica
\(aD\); its repeated values on \(t\) terminate because the repeated \(D\)-values
of \(DP\) terminate. Local nilpotence on these algebra generators implies
local nilpotence on \(B\).

Write \(\Theta_w(Q)\) for the finite polynomial \(\exp(TD)(Q)\), first
formed with an independent parameter \(T\), then evaluated at \(T=w\).
This convention is essential. It does not assert that the
variable-coefficient derivation \(wD\) is locally nilpotent or that its
exponential equals this substitution.

Define

\[
w=cP-at,\qquad Z_i=\Theta_w(x_i),\qquad
T_0=t-\frac{cP}{a}=-\frac wa\in B_a.
                                                                    \tag{5}
\]

The \(Z_i\) lie in \(B\). Since \(\mathcal Ew=-a\), the finite-flow chain
rule gives

\[
\mathcal EZ_i=0,\qquad \mathcal ET_0=1,\qquad
a(Z)=a,\qquad c(Z)=c.
                                                                    \tag{6}
\]

Here and below, evaluation at \(Z\) means substitution of all the \(Z_i\).
The localized map \((x,t)\mapsto(Z,T_0)\) is an automorphism of \(B_a\).
In independent target symbols \((X,\tau)\), its inverse is

\[
x_* =\Theta_{a(X)\tau}(X),\qquad
t_* =\tau+\frac{c(X)}{a(X)}P(x_*).
                                                                    \tag{7}
\]

Indeed, substituting (5) in (7) composes the finite flow at parameters
\(w\) and \(aT_0=-w\). Conversely, (7) gives
\(cP(x_*)-at_*=-a\tau\), so the reverse flow composition recovers
\(X\), and \(T_0\) recovers \(\tau\). These are both whole localized
composition identities, not merely field identities.

### 2.1. Finite correction on the divisor

Let

\[
\phi_0(Q)=\Theta_{cP}(Q),\qquad \Delta=\phi_0-\mathrm{id},\qquad
h=\sum_{j=0}^{K-1}(-\Delta)^j(cP)\in R.
                                                                    \tag{8}
\]

The map \(\phi_0\) is a ring endomorphism obtained by evaluating the
polynomial flow. It fixes \(a,c\). Taylor expansion gives
\(\Delta(R)\subset cR\), and therefore
\(\Delta(c^jR)\subset c^{j+1}R\). On \(R/aR\), the induced additive
operator \(\overline\Delta\) has \(\overline\Delta^K=0\).
Consequently \(\overline\phi_0\) is a ring automorphism: its additive
inverse is the finite geometric sum
\(\sum_{j=0}^{K-1}(-\overline\Delta)^j\), and an inverse to a bijective
ring homomorphism is automatically a ring homomorphism.

In particular,

\[
\phi_0(h)\equiv cP\pmod{aR},\qquad
h(Z)\equiv cP\pmod{aB}.
                                                                    \tag{9}
\]

The second congruence uses \(Z\equiv\Theta_{cP}(x)\pmod a\).
It follows that

\[
U=t+\frac{h(Z)-cP}{a}
  =T_0+\frac{h(Z)}a\in B,\qquad \mathcal EU=1.
                                                                   \tag{10}
\]

The displayed division is exact polynomial divisibility; the divisor
\(a=0\) is not discarded. This proof also permits nonreduced \(R/aR\).

### 2.2. The inverse is polynomial in both directions

Let \(\mathcal F\) be the endomorphism of \(B\) with coordinate images
\((Z,U)\). It fixes \(a\). On \(B_a\), it is (5) followed by the shear
\(T_0\mapsto T_0+h(Z)/a\), so its entire localized inverse is

\[
\begin{aligned}
\tau_*&=U-\frac{h(X)}{a(X)},\\
x_*&=\Theta_{a(X)U-h(X)}(X),\\
t_*&=U+\frac{c(X)P(x_*)-h(X)}{a(X)}.
\end{aligned}                                                      \tag{11}
\]

Both compositions are the identities by (7) and the inverse shear. The
base entries \(x_*\) in (11) are already polynomial. To prove that the last
entry, and all inverse images, are polynomial as well, work on the divisor.

Modulo \(a\), equation (4) becomes

\[
\overline{\mathcal E}
 =(1+\bar c\,\overline{DP})\partial_t.
                                                                   \tag{12}
\]

Its multiplier is a unit: \((\bar c\,\overline{DP})^K=0\).
Equation (10) therefore implies
\(\partial_t\bar U=(1+\bar c\,\overline{DP})^{-1}\).
Over the characteristic-zero algebra \(R/aR\), this says that \(\bar U\)
is affine in \(t\), with this unit leading coefficient. The base map is
\(\overline\phi_0\), already proved an automorphism. Thus the full
induced map \(\overline{\mathcal F}\) on \((R/aR)[t]\) is an automorphism.

For completeness, let \(b\in B\) and write
\(\mathcal F_a^{-1}(b)=Q/a^j\) with \(j\geq0\) minimal. If \(j>0\),
then \(\mathcal F(Q)=a^jb\). Injectivity of
\(\overline{\mathcal F}\) forces \(Q\in aB\), contradicting minimality.
Thus every inverse image lies in \(B\). Injectivity of \(\mathcal F\)
follows from its localized inverse, since \(B\hookrightarrow B_a\).
The two identities for (11) consequently hold in \(B\), and

\[
B=\mathbb C[Z_1,\ldots,Z_m,U],\qquad
\mathcal E\mathcal F=\mathcal F\partial_t,\qquad
\ker\mathcal E=\mathbb C[Z_1,\ldots,Z_m].
                                                                   \tag{13}
\]

If \(a\) is a unit, the localized construction already takes place in \(B\)
and no denominator argument is necessary. The case \(c=0\) causes no
exception. This is a finite construction for each supplied \(D,a,c,P,K\),
not an existence argument that presupposes generators of an unknown kernel.

## 3. The whole homogeneous base and the sliced replica

For (1), direct differentiation yields

\[
\begin{aligned}
H_0x&=-2f^nr,\\
H_0y&=2(2n+1)x^{2n}r-g,\\
H_0z&=2x^{2n-1}\bigl(f^{n+1}+Myr\bigr),\\
H_0f&=H_0g=0,\qquad H_0r=-f^ng.
\end{aligned}                                                      \tag{14}
\]

The identity \(xg=f^{2n+1}+r^2\) follows from (1). In particular,

\[
R_{fg}=\mathbb C[f,f^{-1},g,g^{-1},r],\qquad
H_0=-f^ng\partial_r,\qquad R=\mathbb C[x,y,z].
                                                                   \tag{15}
\]

One can verify the ring equality and algebraic independence by its full
inverse formulas

\[
x=\frac{f^{2n+1}+r^2}{g},\qquad
y=\frac{r-x^{2n+1}}{f^n},\qquad
z=\frac{g-2x^{2n}r+x^M}{f^{2n}}.
                                                                   \tag{16}
\]

For independent \(f,g,r\), these formulas satisfy \(xz-y^2=f\), the
defining equation for \(r\), and the polynomial equation for \(g\).
Thus no algebraic relation between \(f,g\) is being assumed or inferred
from generic points only. Equation (15) also proves local nilpotence on
\(R\), since localization is injective and every element has finite
\(r\)-degree there.

The \(r\)-degrees in (16), or the finite flow

\[
r(T)=r-f^ngT,\qquad
x(T)=x-2f^nrT+f^{2n}gT^2,
                                                                   \tag{17}
\]

give the exact orders
\(\deg_{H_0}(x,y,z)=(2,4n+2,N)\). Their leading coefficients are
nonzero in the localization, hence also nonzero in the original domain.
All three coefficients in (14) are ordinary homogeneous of degree
\(4n+1\), so \(H_0\) has ordinary derivation degree \(4n\).

For (2), \(a,c\in\ker H_0\) and

\[
c^s=f^sg^{2s}=ag^{2s}\in aR.
                                                                   \tag{18}
\]

Apply Section 2 with \(D=H_0\), \(K=s\), and \(P=z^q\). This gives the
promised finite, whole polynomial rectification, with \(h,Z,U\) defined
exactly by (5), (8), and (10), and the whole inverse (11). No coefficient
field extension, ambient coordinate promotion, or pre-existing recognition
theorem is needed for this conclusion.

Invariant replication does not change nilpotence orders:
\(H^jQ=a^jH_0^jQ\). The ordinary degrees now satisfy

\[
\deg a=2s,\quad \deg c=2+2M=2s,\quad
d=\deg H=4n+2s=12n+4,\quad
\ell=\deg\psi=d+q,\quad \deg_H\psi=qN-1.
                                                                   \tag{19}
\]

Every polynomial and nonvanishing assertion in (19) is in the original
ring. In fact \(\psi\in fR\setminus f^2R\): on the prime divisor \(f\),
\(\bar g=x^M\) and
\(\overline{H_0(z^q)}=2qM x^{4n}y z^{q-1}\ne0\).
Thus the explicitly sliced extension need not have its nonconstant
coefficient divisible by the full replica factor \(f^s\).

## 4. Failure of all fixed-base polynomial shears

Among ordinary degree-\(q\) monomials, only \(z^q\) has \(H\)-degree
\(qN\). Replacing at least one \(z\) by \(y\) or \(x\) lowers that degree
by at least \(4n\). Therefore every homogeneous degree-\(q\) polynomial
has the form

\[
Q=\lambda z^q+Q_<,\qquad \lambda\in\mathbb C,
\qquad \deg_H Q_<\leq qN-4n.
                                                                   \tag{20}
\]

The degree inequality allows \(Q_<=0\). Since \(a,c\) are invariants,

\[
\psi-HQ=(c-\lambda a)H_0(z^q)-aH_0Q_<,\qquad
c-\lambda a=f(g^2-\lambda f^M)\ne0.
                                                                   \tag{21}
\]

The nonvanishing follows from the algebraic independence in (15).
The first summand has \(H\)-degree \(qN-1\), while the second has degree
at most \(qN-4n-1\). Hence no such \(Q\) removes the top.

This also rules out every fixed-base polynomial shear, without a
homogeneity assumption. Set \(L=qN\geq2\). Since \(E|_R=H\) and
\(Et=1+\psi\),

\[
\deg_E(t-Q)<L
\quad\Longleftrightarrow\quad
H^LQ=H^{L-1}\psi.
                                                                   \tag{22}
\]

If \(Q=\sum_jQ_j\) is its ordinary homogeneous decomposition, then
\(H^LQ_j\) has ordinary degree \(j+Ld\) whenever nonzero. The right side
of (22) has degree \(\ell+(L-1)d=q+Ld\). Thus (22) forces
\(H^LQ_q=H^{L-1}\psi\). This contradicts (21), whose difference has
exact \(H\)-degree \(L-1\). Consequently
\(\deg_E(t-Q)\geq L\) for every \(Q\in R\).

The conclusion is specifically about holding the three base coordinates
fixed. The rectification in Section 2 changes them; there is no conflict
between that rectification and (22). Indeed,
\((Z_1+U,Z_2+U,Z_3+U,U)\) is another actual coordinate frame with all four
\(E\)-degrees equal to one. Thus the displayed high-degree frame is not
globally minimal even among all-positive frames.

## 5. Actual first shift, not merely a bracket condition

The linear coordinate frame

\[
(X,Y,Z,t)=(x+z,y+z,z,t),\qquad
(x,y,z,t)=(X-Z,Y-Z,Z,t)
                                                                   \tag{23}
\]

has exact \(E\)-degrees \((N,N,N,L)\). The first three follow from the
strictly smaller degrees of \(x,y\) than \(z\), and the last follows from
\(\deg_H\psi=L-1\). Its actual weighted Euler derivation is

\[
\mathcal D=N(x\partial_x+y\partial_y+z\partial_z)
             +L t\partial_t.
                                                                   \tag{24}
\]

Using (19) and \(L=qN\) gives the whole derivation identities

\[
[E,\mathcal D]=N\ell\partial_t-NdE,
\qquad [E,[E,\mathcal D]]=0.
                                                                   \tag{25}
\]

For any \(b\in B\) of \(E\)-degree \(k\geq0\), the commutator identity
\([E^j,\mathcal D]=j[E,\mathcal D]E^{j-1}\) implies
\(E^{k+2}\mathcal Db=0\). Thus the exact all-ring filtration shift is
at most one. To show equality rather than infer it from (25), put

\[
p_0=f^ng,\qquad w=cP-at,\qquad I=r-p_0w.
                                                                   \tag{26}
\]

Equations (14) and (5) give

\[
EI=0,\qquad \partial_tI=ap_0\ne0,\qquad
E(\mathcal DI)=N\ell ap_0\ne0,\qquad
E^2(\mathcal DI)=0.
                                                                   \tag{27}
\]

Hence an actual invariant of \(E\)-degree zero is sent by \(\mathcal D\)
to degree one. The weighted Euler shift is exactly one in this actual
positive frame.

## 6. Evidence, provenance, and retained limits

The finite nilpotent correction and inverse-denominator mechanism has an
internal predecessor in [pass 22](radical-noninvariant-pass22.md), Section 2.
The present proof is written out for the exact replica coefficients used
here. The DG formulas are likewise explicitly verified above; no new
classification or priority claim is made.

Fresh unsaved algebra checked a complete nonlinear finite-repair example,
including both entire inverse compositions, and reconstructed the entire
DG identities and the invariant witness for \(n=1,2\). These are checks
of the written uniform proofs, not substitutes for them. No saved checker
was executed, imported, or compiled.

The result establishes a bounded negative answer to an unrestricted
replica version of leading-term removal, even with a polynomial slice and
an actual first-shift frame. It does not exclude a stronger assertion with
an irreducibility hypothesis, prove any globally minimal-frame statement,
or advance a counterexample to complex cancellation. Its kernels are
polynomial by the whole coordinate construction in Section 2.
