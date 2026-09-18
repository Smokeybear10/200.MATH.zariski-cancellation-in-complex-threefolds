# A sharp six-dimensional closure bound for four first-shift spectral weights

## 1. Actual hypotheses and the result

Let
\[
 B=\mathbb C[X_1,X_2,X_3,X_4]=A[u],\qquad
 E=\partial_u,\quad Eu=1,\quad A=\ker E,
 \qquad d_i=\deg_E X_i>0,
 \qquad D=\sum_i d_iX_i\partial_{X_i}.
\tag{1}
\]
The \(X_i\) are actual polynomial coordinates. Assume the exact
whole-ring \(E\)-filtration shift of this Euler derivation is one.
No polynomial presentation of \(A\) is an input.

If \(E\) has at most four distinct adjoint \(D\)-weights, then
every spectral component of \(E\) is locally nilpotent and
\[
 \dim_{\mathbb C}\operatorname{Lie}_{\mathbb C}(D,E)\le6.
\tag{2}
\]
For four weights there are exactly two possibilities for the component
Lie algebra: it is abelian of dimension four, or it is a
five-dimensional two-step nilpotent algebra with one-dimensional center.
The latter integrates to a five-dimensional unipotent action normalized
by the actual Euler torus. Its extension by \(D\) has dimension six.

The bound six is attained by a complete polynomial translation frame
of degrees \((1,2,4,3)\) given below. This is also a first-shift
example with four noncommuting spectral components. Since three
components always commute, four is the least possible number of
distinct weights for such noncommutation under these hypotheses.
This last minimality assertion concerns only the number of spectral
weights, not coordinate degree sums or globally minimizing frames.

The result extends the noncolliding-pair-sum test587 to every
four-weight case, including its repeated sum. It does not settle
five or more weights, general first-shift recognition of \(A\), or
cancellation. In particular the known five-component control583 is
finite dimensional, but does not prove a general bound. No novelty
is claimed. The proof uses the complete first-shift and spectral
contracts576--577 and587, with the needed arguments included here.

## 2. The full first-shift relation

Exact shift one initially gives the genuine coefficient identities
\[
 D|_A=M+uN,\qquad D(u)=b_2u^2+b_1u+b_0,
 \quad M,N\in\operatorname{Der}_{\mathbb C}(A),\quad b_i\in A.
\tag{3}
\]
The induced nonzero degree-one derivation on
\(\operatorname{gr}_E B=A[\eta]\) is locally nilpotent: otherwise
its nonzero iterates on an initial form would force unbounded
\(E\)-degrees among the corresponding iterates of \(D\), contrary
to the finite-dimensional orbit under the actual Euler derivation.
This induced LND takes \(\eta\) to \(b_2\eta^2\), hence kills it.
Indeed, for any LND \(L\) on a characteristic-zero domain, the
additive LND degree rules out \(L(f)=fg\ne0\): its two sides would
have degrees \(\deg_L f-1\) and \(\deg_L f+\deg_L g\).
Consequently \(b_2=0\), and
\[
 [E,D]=N+b_1E,\qquad [E,[E,D]]=0.
\tag{4}
\]
The recovered \(N\) is a nonzero LND on \(A\), extended here to
kill the supplied slice. No slice for \(N\), constancy of \(b_1\),
or local finiteness of \(M\) is assumed.

The monomial formula in the actual source coordinates is
\[
 [D,X^\alpha\partial_{X_i}]
    =\left(\sum_j d_j\alpha_j-d_i\right)
       X^\alpha\partial_{X_i}.
\tag{5}
\]
Thus \(E\) has a finite decomposition into nonzero polynomial
derivations
\[
 E=\sum_{\lambda\in\mathcal S}E_\lambda,
 \qquad [D,E_\lambda]=\lambda E_\lambda,
 \qquad \mathcal S\subset\mathbb Z.
\tag{6}
\]
Grouping (4) by weight gives the whole identity
\[
 \sum_{\substack{\lambda<\mu\\\lambda+\mu=s}}
       (\mu-\lambda)[E_\lambda,E_\mu]=0
 \qquad\text{for every integer }s.
\tag{7}
\]
There are no diagonal contributions. Distinct unordered pair sums
force the corresponding components to commute. In particular this
holds for at most three weights, as proved directly in587.

## 3. Four weights have only one possible collision

Now let the four weights be
\(\alpha<\beta<\gamma<\delta\), and abbreviate
\(F_1=E_\alpha,F_2=E_\beta,F_3=E_\gamma,F_4=E_\delta\).
Two distinct unordered pairs with equal sums cannot share an index.
Of the three ways to divide four ordered weights into two pairs,
\(\alpha+\beta<\gamma+\delta\) and
\(\alpha+\gamma<\beta+\delta\). The only possible repeated
sum is therefore
\[
 \alpha+\delta=\beta+\gamma.
\tag{8}
\]
If it does not occur, all components commute. Suppose it does.
Every other pair commutes, and (7) says exactly
\[
 K:=[F_1,F_4],\qquad
 [F_2,F_3]=-\frac{\delta-\alpha}{\gamma-\beta}K,
 \qquad [F_i,F_j]=0\text{ for the other distinct pairs}.
\tag{9}
\]
All denominators here are nonzero complex integers. The case \(K=0\)
is retained; it is again the commuting case.

If \(K\ne0\), it commutes with every \(F_i\). For example,
\(F_1\) commutes with both \(F_2,F_3\), so Jacobi and the
nonzero proportionality in (9) give \([F_1,K]=0\). The same
argument applies to \(F_4\). Conversely \(F_2,F_3\) each
commute with both \(F_1,F_4\), so they commute with \(K\) as well.
Hence
\[
 \mathfrak n=\operatorname{span}_{\mathbb C}
       \{F_1,F_2,F_3,F_4,K\},
 \qquad [\mathfrak n,\mathfrak n]=\mathbb C K,
 \qquad [\mathfrak n,K]=0.
\tag{10}
\]
This argument does not yet assume that the individual \(F_i\)
or \(K\) are locally nilpotent. That conclusion requires the
actual LND and torus input in the next section.

## 4. Local nilpotence follows from the actual conjugate flows

Let \(\tau_t(X_i)=t^{d_i}X_i\), \(t\in\mathbb C^*\), be the
actual Euler torus. Its conjugates of \(E\) are LNDs and satisfy
\[
 E^{(t)}=\tau_tE\tau_t^{-1}
        =\sum_{\lambda\in\mathcal S}t^\lambda E_\lambda.
\tag{11}
\]
The distinct Laurent monomials are linearly independent on
\(\mathbb C^*\). Therefore finitely many nonzero values of \(t\)
give an invertible evaluation matrix and the corresponding conjugates
span all spectral components. To justify the evaluation claim,
failure of spanning would produce a nonzero Laurent polynomial
vanishing on every nonzero complex number.

In the commuting case, these conjugates commute. Every component
is then a finite linear combination of commuting LNDs, and is an
LND by the multinomial argument: on any polynomial, sufficiently
many factors contain enough copies of one commuting derivation to
annihilate it. Their entire span consists of LNDs.

Consider now \(K\ne0\) in (9). There must be two conjugates
\(U=E^{(t)}\) and \(V=E^{(s)}\) with
\([U,V]=cK\), \(c\in\mathbb C^*\). Otherwise all such
conjugates would commute, and spanning would force all four components
to commute, contrary to \(K\ne0\). The bracket is central by (10).
Thus the full finite conjugation identity is
\[
 \exp(U)V\exp(-U)=V+cK.
\tag{12}
\]
The left side is an LND, being the conjugate of the actual LND \(V\)
by a polynomial automorphism. The two LNDs \(V+cK\) and \(V\)
commute. Their difference is therefore locally nilpotent by the same
commuting multinomial argument. This proves that \(K\) is an LND.

Here is the remaining step for a possibly noncommuting linear
combination. Choose four conjugates \(U_1,\ldots,U_4\) spanning
the four components. Their brackets are central multiples of \(K\).
For arbitrary constants \(z_0,z_1,\ldots,z_4\), put
\[
 Z=z_0K+\sum_{i=1}^4z_iU_i.
\tag{13}
\]
The two-step commutator identities give, in formal power series in
one variable \(t\),
\[
 \exp(tZ)=
   \left(\prod_{i=1}^4\exp(tz_iU_i)\right)
   \exp\left(tz_0K-
            \frac{t^2}{2}\sum_{i<j}z_iz_j[U_i,U_j]\right).
\tag{14}
\]
The product is ordered by increasing \(i\). This elementary central
exponential identity can be checked without any convergence claim:
the logarithmic derivative of the first product is
\(\sum_i z_iU_i+t\sum_{i<j}z_iz_j[U_i,U_j]\).
The last, central factor cancels that linear term and contributes
\(z_0K\). Both sides have initial value the identity, so equality
follows by coefficient recursion in characteristic zero.

Every factor on the right of (14) is polynomial in \(t\) on each
element of \(B\), since the \(U_i\) and \(K\) are LNDs. The
finite product is likewise polynomial on each element; no infinite
orbit assertion is hidden in this statement. Therefore the coefficients
\(Z^j(f)/j!\) on the left eventually vanish for every \(f\in B\).
This proves \(Z\) is locally nilpotent. In particular every
\(F_i\), and indeed every element of \(\mathfrak n\), is an LND.

This proof uses the actual torus-conjugate LNDs. It does not treat
arbitrary spectral projection of an LND as preserving local nilpotence.

## 5. Exact dimension and the normalized unipotent action

Each component belongs to \(\operatorname{Lie}_{\mathbb C}(D,E)\)
by finite spectral interpolation:
\[
 E_\lambda=
 \prod_{\substack{\mu\in\mathcal S\\\mu\ne\lambda}}
   \frac{\operatorname{ad}_D-\mu}{\lambda-\mu}(E).
\tag{15}
\]
In the four-weight noncommuting case this also puts \(K\) in that
Lie algebra. The span \(\mathfrak n\) is stable under \(D\),
because the \(F_i\) have their displayed weights and \(K\)
has weight \(\alpha+\delta\). Hence
\[
 \operatorname{Lie}_{\mathbb C}(D,E)=\mathbb C D\ltimes\mathfrak n.
\tag{16}
\]

The five generators of \(\mathfrak n\) are independent when
\(K\ne0\). The four distinct-weight components are independent.
If their span contained \(K\), its single weight would make it
proportional to the one \(F_i\) of that weight, if such a weight
occurs at all. But centrality of \(K\) would then make that
\(F_i\) central, contrary to its nonzero bracket with its partner
in (9). This also handles coincidence of \(\alpha+\delta\)
with one of the original four weights.

Finally \(D\notin\mathfrak n\), since all elements of
\(\mathfrak n\) are LNDs, whereas the nonzero positive Euler field
is not. Thus the noncommuting case has exact dimension six. If the
components commute, their span has dimension \(|\mathcal S|\)
and the same argument gives dimension \(|\mathcal S|+1\).
These statements prove (2), including every zero-bracket case.

In the noncommuting case the bracket pairing on the four-dimensional
quotient \(\mathfrak n/\mathbb C K\) has two nonzero paired blocks
in (9), so the center of \(\mathfrak n\) is exactly \(\mathbb C K\). The vector space
\(\mathfrak n\) has the polynomial group law
\[
 P*Q=P+Q+\frac12[P,Q].
\tag{17}
\]
This is the five-dimensional two-step unipotent group, equivalently
the five-dimensional Heisenberg group after rescaling a basis.
Formula (14), or the same formula in the component basis, makes
\(P\mapsto\exp(P)\) an algebraic action on the whole affine
four-space. Polynomiality holds also in its parameter coefficients,
by the finite LND flows on the right. No abstract integration
assumption is needed. The actual torus normalizes the action, scaling
each \(F_i\) by its weight and \(K\) by
\(t^{\alpha+\delta}\). In the commuting case the corresponding
group is additive. Neither action by itself is used to recognize
the original invariant ring \(A\).

## 6. A complete actual frame attains dimension six

Work in the known polynomial translation ring
\(\mathbb C[a,b,c,u]\), with \(E=\partial_u\), and take
\[
 X=u,\qquad Y=a+u^2,\qquad Z=b+au+u^4,
 \qquad W=c-\frac12bu+\frac12au^2+u^3.
\tag{18}
\]
The full inverse successively recovers
\[
 u=X,\qquad a=Y-X^2,\qquad b=Z-aX-X^4,
 \qquad c=W+\frac12bX-\frac12aX^2-X^3.
\tag{19}
\]
Substituting in either order first recovers \(u\), then \(a,b\),
then the last coordinate. Both are whole polynomial identities.
The Jacobian is \(-1\) in the ordered old variables \((a,b,c,u)\).
The actual degrees are \((1,2,4,3)\), all with leader one. The
entire weighted Euler field is
\[
 D=2a\partial_a+(4b+au)\partial_b+(3c+bu)\partial_c
           +u\partial_u.
\tag{20}
\]
It satisfies \(D(X)=X,D(Y)=2Y,D(Z)=4Z,D(W)=3W\) on the complete
rows, including both lower terms in \(W\). The product rule bounds
the whole-ring shift by one, and \(D(b)=4b+au\) attains it. Thus
\(\delta=1\). Moreover
\[
 [E,D]=E+N,\qquad N=a\partial_b+b\partial_c,
 \qquad [E,[E,D]]=0.
\tag{21}
\]
The corrected recovered \(N\) is a nonzero LND, is primitive
because \(\gcd(a,b)=1\), and has no slice since
\(N(A)\subset(a,b)\). These facts are not required for the spectral
proof, but clarify that the control does not assume a sliced recovered
direction. Its original \(E\) has the supplied slice \(u\) throughout.

The full spectral components of this same derivation \(E\), written
in \((u,a,b,c)\) for readability, are
\[
\begin{aligned}
 E_{-2}&=a\partial_b+\frac12au\partial_c,\\
 E_{-1}&=\partial_u-a\partial_b+
                      \frac12(b-3au)\partial_c,\\
 E_0&=\frac32au\partial_c,\\
 E_1&=-\frac12(au+b)\partial_c.
\end{aligned}
\tag{22}
\]
Direct calculation using (20) gives both
\(E=E_{-2}+E_{-1}+E_0+E_1\) and
\([D,E_\lambda]=\lambda E_\lambda\). These four nonzero
components therefore are the actual source-weight decomposition,
not an arbitrarily chosen decomposition into LNDs.

Their only nonzero unordered brackets are
\[
 [E_{-2},E_1]=-\frac12a\partial_c,
 \qquad [E_{-1},E_0]=\frac32a\partial_c.
\tag{23}
\]
They are central relative to the components and satisfy exactly
\(3[E_{-2},E_1]+[E_{-1},E_0]=0\), the repeated-sum relation
for weights \(-2,-1,0,1\). The central direction has weight
\(-1\), equal to one component weight, yet is independent of it:
\(E_{-1}(u)=1\), while \((a\partial_c)(u)=0\).

For a separate full closure check, put
\[
 L=a\partial_b,\qquad P=b\partial_c,
 \qquad Q=au\partial_c,\qquad C=a\partial_c.
\tag{24}
\]
Then \(\operatorname{Lie}_{\mathbb C}(D,E)\) is exactly the
six-dimensional span of \(D,E,L,P,Q,C\). Indeed
\(N=[E,D]-E=L+P\) and \([N,D]=2L-P\), so
\(L=(N+[N,D])/3\), \(P=N-L\). Next
\(Q=[D,P]-P\) and \(C=[E,Q]\), proving generation. All
nonzero unordered brackets in this basis, besides their negatives,
are
\[
\begin{aligned}
 [D,E]&=-E-L-P,& [D,L]&=-2L-Q,\\
 [D,P]&=P+Q,& [D,C]&=-C,\\
 [E,Q]&=C,& [L,P]&=C.
\end{aligned}
\tag{25}
\]
In particular \([D,Q]=0\); every unlisted distinct pair commutes.
This proves bracket closure of the entire displayed span. Its six
elements are independent, as seen successively from their \(a,u,b\)
components and the distinct vertical coefficients \(b,au,a\).
This is a direct actual verification of sharpness in (2).

The example still does not make spectral components preserve the
original \(A\): for instance
\(E_0(c)=3au/2\notin A\). All elements of the component algebra
are LNDs here also by the nonnegative grading in \(u,b,c\) of
weights \((1,1,2)\) over \(\mathbb C[a]\), which they strictly
lower. The visible coordinate \(u=X\) is already an Euler-homogeneous
slice, and \(A=\mathbb C[a,b,c]\) was explicit from the beginning.
Thus the example is not a recognition or cancellation obstruction.

## 7. Exact scope and verification

This proves individual spectral local nilpotence and finite Lie
closure for every actual first-shift frame with at most four spectral
weights. The fourth weight is genuinely new: (18) shows that the
noncolliding-sum sufficient test587 can fail while the two-step
unipotent conclusion here still holds, with the sharp dimension six.

For five or more weights, neither general finite Lie closure nor
general local nilpotence of every spectral component is proved or
refuted here. No high-shift example is used as evidence for a
first-shift claim. No claim is made that a coordinate slice for one
component is a slice for \(E\), or that the resulting finite-dimensional
action automatically supplies invariant coordinates for \(A\).

Fresh unsaved algebra reconstructs both complete inverse orders of
(18), the Jacobian, every Euler eigen-equation, exact degrees and
shift, all four spectral identities, every component bracket, and
all fifteen unordered brackets in the six-dimensional basis. The
general central-flow argument, including its polynomial dependence
on the flow parameter, is a proof rather than an extrapolation from
the control.

No saved checker was executed, imported or compiled; no canonical file
was edited. This working note makes no claim of general recognition,
global frame minimality, arbitrary coordinate entry, or completion
of cancellation.
