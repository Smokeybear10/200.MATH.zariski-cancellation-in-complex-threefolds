# Monic normalization of an exact nonlinear two-stage presentation

Private source-dependent proof, September 17, 2026. General cancellation
remains UNSOLVED. This note normalizes an already supplied exact global
presentation while keeping the actual kernel and the same local slice.
It does not produce such a presentation for an arbitrary action, prove
normality of an exceptional curve, or exclude the nonlinear rank-three
case. Novelty is UNKNOWN.

## 1. Exact input and output

Work over k=C. Let R=k^[3], let D be a nonzero locally nilpotent
derivation, and let A=ker(D)=k[a,b] be its actual embedded kernel.
Let f be irreducible nonconstant in A. Suppose Dr=f^2 and that
T,Y,Z mapping to r,y,z give the exact A-algebra presentation

    R=A[T,Y,Z]/(fY-G(T), fZ-H(T,Y)),                    (1)

where G is in A[T] and H in A[T,Y]. The displayed ideal is the
full defining ideal. There is no localization or subsequent saturation.
Neither monicity of G nor a domain assumption on (A/f)[T]/Gbar
is imposed. Exact equality pl(D)=f^2 A is not part of the main input.

Set

    C=A/fA,
    B=C[T,Y]/(Gbar,Hbar),
    K=Frac(C), L=Frac(B), t=rbar in B.                  (2)

The finite-flat result of the accepted
[629](nonlinear-two-stage-residue-degree-and-ramification-pass629-working.md)
supplies the following specific facts: C and B are domains, C embeds
in B, B is finite locally free over C, and R/fR=B[z]. Its proof uses
the actual cylinder factor in Kaliman's finiteness theorem, followed
by flatness over the regular A and base change. It does not assume
that C is normal. These are the geometric inputs to this note.

Let M be the monic minimal polynomial of t over K. Put

    n=[K(t):K],  m=[L:K(t)].                           (3)

Then n,m are positive integers. There are actual elements y1,w of R
and polynomials G1 in A[T], K1 in A[T,Y] such that

    G1 is monic of T-degree n,
    deg_T K1<n,  deg_Y K1<m,
    R=A[T,Y,W]/(fY-G1(T), fW-Y^m-K1(T,Y)),             (4)

with T,Y,W mapping to r,y1,w. If K1=0, its degree bounds use the
usual convention deg(0)=-infinity. The relations in (4) again give
the entire defining ideal. All changes have polynomial recovery
formulas in the actual rings, not merely inverses on a localization.

Moreover

    G1bar=M,
    S=C[t]=C[T]/(M) is a domain free of C-rank n,
    B is free of S-rank m and of C-rank nm.             (5)

The intrinsic degree-one conclusion is

    R=A[r,q] for some q in R  if and only if  m=1.      (6)

Here r is the SAME actual element as in (1). If the additional
assumption pl(D)=f^2 A holds, then n>=2. This inequality is not
inferred from Dr=f^2 alone. No assertion m=1, normality of B, or
polynomiality of any unnamed intermediate threefold is made.

## 2. Minimal-polynomial coefficients without normality

Since B is a finite locally free C-domain, its rank N is a positive
constant on the connected Spec(C). Localizing at C minus zero gives
the field L, of K-dimension N. Multiplication by t on B has a monic
characteristic polynomial chi(T) in C[T] of degree N. Indeed the
matrix characteristic polynomials on local free charts agree on
overlaps and glue over the affine base. Cayley-Hamilton also holds
on these charts and hence globally. No free basis for B over C has
yet been assumed.

On L the characteristic polynomial is

    chi(T)=M(T)^m,  N=nm.                              (7)

For example, a K(t)-basis of L identifies multiplication by t with
m copies of its action on K(t), whose characteristic polynomial is
its minimal polynomial M. Write

    M(T)=T^n+c1 T^(n-1)+...+cn,  ci in K.

For 1<=j<=n, comparison of the coefficient of T^(N-j) in (7)
has the triangular form

    [T^(N-j)]chi = m cj + P_j(c1,...,c_(j-1)),          (8)

where P_j is an integer-coefficient polynomial. The reason is that
using cj lowers the degree by j, so the only contribution involving
it uses it in one factor and uses the leading term in the other
m-1 factors. Inductively all ci belong to C: the left side is in
C and the positive integer m is a unit in this complex algebra.
Thus M belongs to C[T]. Integrality alone over a nonnormal C would
not have justified this coefficient assertion; equation (8) does.

The kernel of C[T]->B, T->t, is now exactly (M). Monic division
by M leaves a remainder of degree less than n. If that remainder
vanishes at t, its coefficients vanish after passage to K by
minimality of M, and therefore already vanish in C. This proves
the description of S in (5), including its domain property and
free monic power basis over C.

## 3. Exact ideal membership selects a unit cofactor

Monic division gives a polynomial G2bar in C[T] with

    Gbar=M G2bar.                                     (9)

Since M(t)=0 in the actual algebra B, exactness of (2) gives
polynomials U,V in C[T,Y] satisfying

    M=U Gbar+V Hbar.                                  (10)

This membership is in the displayed ideal, not merely its radical.
Consequently that ideal equals (M,Hbar), and

    B=S[Y]/(h),  h=Hbar modulo M in S[Y].              (11)

The polynomial h is nonzero: otherwise B=S[Y] could not be finite
over C. It is not a nonzero constant, because S already embeds in
B; a unit would also contradict B!=0. Hence h has positive degree.

Reduction of (10) modulo M takes place in the domain S[Y]. It gives
Vbar h=0, and h!=0 therefore forces V=M V1 for some V1 in C[T,Y].
After cancellation of the nonzero M in the domain C[T,Y], (10)
becomes the complete polynomial identity

    1=U G2bar+V1 Hbar.                                (12)

Thus G2bar is a unit in B.

We also need it to be a unit in S, not just in B. The ring B is
finite over S, since it is finite over C. Integrality of Y gives
a monic polynomial P(Y) in the ideal (h) of S[Y]. Writing P=hJ
and comparing leading coefficients in the domain S shows that
the leading coefficient of h is a unit of S. Normalize h by that
unit. Monic polynomial division then proves that B is free over S,
with basis 1,Y,...,Y^(d-1), where d=deg_Y h. On fraction fields this
gives d=[L:Frac(S)]=m, so the degree is exactly the m in (3).

Finally, multiplication by G2bar is an invertible endomorphism of
this free S-module B. Its determinant is G2bar^m, so G2bar^m, and
hence G2bar, is a unit in S. This proves the required unit descent
without any normality assumption on S.

Equations (9)--(12) exclude Gbar=0 automatically. They also explain
why the original algebra C[T]/Gbar is not retained: it may have
other components or nilpotents. It is S=C[t], the actual image,
that has been identified as a monic integral curve algebra.

## 4. The actual first-generator change and first exactness check

Choose a monic lift G1 in A[T] of M, preserving degree n, and a
lift G2 in A[T] of G2bar. Write

    G=G1 G2+fJ,  J in A[T].                            (13)

Because G1(r) vanishes in R/fR, the actual element

    y1=G1(r)/f                                        (14)

belongs to R. This expression denotes divisibility in R, not an
adjoined fraction. The original first equation gives

    y=G2(r)y1+J(r),  R=A[r,y1,z].                     (15)

Let H1(T,Y)=H(T,G2(T)Y+J(T)). The actual elements satisfy
f y1=G1(r), fz=H1(r,y1). We next prove that these are the full
relations, rather than assume a new unsaturated presentation.

Put

    Q1=A[T,Y]/(fY-G1(T)).                              (16)

As a polynomial in Y over the UFD A[T], fY-G1 is primitive,
because G1 is monic in T and is not divisible by f. It is linear
and irreducible over Frac(A[T]), so Gauss's lemma makes Q1 a
domain. Its reduction is

    Q1/fQ1=S[Y],                                      (17)

a domain, so f is prime in Q1. The residue of H1 in this ring is
h(G2bar Y+Jbar). It is nonzero, since G2bar is a unit of S and
this affine substitution is an automorphism of S[Y].

Here is the f-torsion argument used twice below. If Q is a domain,
f is nonzero, Q/fQ is a domain, and h0 modulo f is nonzero, then

    Q[Z]/(fZ-h0) -> Q_f,  Z->h0/f                     (18)

is injective. To prove it, suppose fP=(fZ-h0)L in Q[Z]. Modulo f,
the domain condition gives h0bar Lbar=0, hence L=fL1. Cancellation
of f gives P=(fZ-h0)L1. Thus the quotient has no f-torsion. Its
localization is Q_f, which proves injectivity and its domain property.

Apply (18) with Q=Q1 and h0=H1. The resulting domain maps
surjectively to R by (15), and this map becomes an isomorphism
after inverting f, since both localized rings are A_f[r]. The
f-torsion-free source makes the map injective. Therefore

    R=A[T,Y,Z]/(fY-G1(T), fZ-H1(T,Y))                  (19)

is exact, with Y mapping to y1. This is the first full exactness
check after the generator change.

## 5. A monic last stage with whole polynomial recovery

The residue of H1 in S[Y] has degree m and a unit leading
coefficient. Choose lifts u in A[T], K0 in A[T,Y] with deg_Y K0<m
of its leading and lower coefficients. There are P0,Q0 in A[T,Y]
such that

    H1=uY^m+K0+fQ0+G1 P0.                            (20)

Set, evaluating coefficients at r,y1 when appropriate,

    z1=z-Q0(r,y1)-y1 P0(r,y1).                        (21)

This has the polynomial inverse z=z1+Q0+y1P0. It is a triangular
change of the presentation variable Z, and f y1=G1(r) gives the
exact new last equation

    fz1=u(r)y1^m+K0(r,y1).                            (22)

Since ubar is a unit of S=C[T]/(M), choose v,alpha,beta in A[T]
with

    vu+f alpha+G1 beta=1.                             (23)

Define the actual element

    w0=v(r)z1+alpha(r)y1^m+beta(r)y1^(m+1).            (24)

The complete forward and inverse identities in R are

    fw0=y1^m+v(r)K0(r,y1),
    z1=u(r)w0+alpha(r)K0(r,y1)
                 +beta(r)y1 K0(r,y1).                (25)

For the first, multiply (24) by f and use (22),(23) and fy1=G1.
For the second, substituting (24) makes its right side

    uv z1+(alpha+beta y1)(u y1^m+K0)
      =(uv+f alpha+G1 beta)z1=z1.

In particular these are whole polynomial inverse formulas, not
identities obtained by leaving f inverted. Together with (15),(21)
they give R=A[r,y1,w0].

For the second f-torsion exactness check, take Q=Q1 and
h0=Y^m+vK0 in (18). Its residue is monic of degree m, hence
nonzero in the domain S[Y]. The quotient therefore embeds in
A_f[T], and its surjection to R is an isomorphism after inverting f.
It is already an isomorphism before localization. Thus

    R=A[T,Y,W0]/(fY-G1(T), fW0-Y^m-v(T)K0(T,Y))       (26)

is the full exact presentation. This step rules out an unnoticed
f-torsion component introduced by the non-triangular formula (24).

## 6. The two degree bounds and the residual algebra

Divide v(T)K0(T,Y) by the monic G1(T), treating Y as a coefficient
variable. This gives uniquely

    vK0=G1 P1+K1,
    deg_T K1<n,
    deg_Y P1<m,  deg_Y K1<m.                           (27)

The Y-bounds are preserved because G1 has no Y-dependence and
division is performed independently on each Y-coefficient. They
also hold when one of the polynomials is zero. Now set

    w=w0-y1 P1(r,y1).                                (28)

The inverse is w0=w+y1P1(r,y1), and (25),(27) give

    fw=y1^m+K1(r,y1).                                (29)

This is a triangular change of W0 in the presentation (26), so
it proves the full exact output (4). The explicit recovery of the
original generators is obtained in the polynomial order

    w0=w+y1P1,
    z1=u w0+alpha K0+beta y1K0,
    y=G2 y1+J,
    z=z1+Q0+y1P0.                                    (30)

The maps keep A and r fixed. They do not say that the original
r,y,z were three ambient polynomial coordinates.

Modulo f, (15) is an invertible affine change of the Y-generator
over S because G2bar is a unit. The later changes of the free last
variable have invertible coefficient vbar in S or are translations.
Thus the original embedded curve algebra B is unchanged, with

    B=S[Y]/(Y^m+K1bar(T,Y)).                           (31)

The displayed quotient is a domain by its identification with the
original B. Its monic basis over S and the monic basis of S over C
give a C-basis T^i Y^j, 0<=i<n, 0<=j<m. This proves all of (5).
In particular freeness over C is a conclusion stronger than the
finite local freeness initially supplied by629.

## 7. Same-r collapse and the minimal-slice boundary

If m=1, the degree bound in (4) makes K1 independent of Y, and
(29) gives y1=fw-K1(r). Hence R=A[r,w].

Conversely, suppose R=A[r,q] for some q. Reduction modulo f
gives B[z]=S[qbar], where S=C[t] is the actual image selected
above. Localizing at the nonzero elements of S gives

    L[z]=Frac(S)[qbar].                               (32)

The element qbar is transcendental over Frac(S), since the left
side has transcendence degree one over that field. The ground
field is relatively algebraically closed in its rational function
field in one variable. Since L/Frac(S) is finite algebraic and
embeds in this rational function field, it must be trivial. Thus
m=1. This proves (6), with no assumption on the original Gbar.

Now add the exact-plinth assumption pl(D)=f^2 A. If n=1, the
minimal polynomial has the form T-c with c in C. Lift c to a0 in A.
Then r-a0=fv0 for an actual v0 in R. Differentiation gives

    D(v0)=f,                                          (33)

contradicting f not in f^2 A. Therefore n>=2 under precisely
this extra premise. For comparison, R=k[a,b,w], D=partial_w,
r=a^2w, y=aw, z=w gives the exact relations ay=r, az=y.
Here Dr=a^2, n=m=1, and the plinth is the unit ideal. This
elementary control prevents inferring minimality from Dr=f^2.

The separately retained one-generator theorem
[621](global-one-generator-rank-obstruction-pass621-working.md)
implies rank(D)<=2 in the m=1 case. Thus a rank-three candidate
with exact plinth f^2 in this exact-presentation class must have
n,m>=2 after normalization. Neither degree is shown bounded;
the published family retained in629 has arbitrarily large n,m
and exact plinth f^2, but it has rank two. It is not a counterexample
to a rank-three statement.

## 8. Dependencies, checking, and remaining gap

The finite-flat input is the accepted629 at SHA256
6f970db2e89718086b1d52f9c9eac67ecb00a4ab67d149a7a674d9a077e15d98.
Its full geometric scope is essential. The present proof does not
assume a normal base, a monogenic original first-stage algebra, or
a global presentation for an action not satisfying (1).

The characteristic-polynomial selection extends the linear
component-selection argument of
[628](general-linear-two-stage-rank-obstruction-pass628-working.md).
The unit-leading-coefficient and same-r constant-field steps reuse
the ideas in629 and the published m=n=2 control already retained
in [622](global-triangular-presentation-cylinder-obstruction-pass622-working.md).
A bounded archive search did not find this exact nonlinear
normalization proof. That is not a priority determination or a
claim that its elementary ingredients are new.

General independently challenged the argument before this file was
written, and root authorized the write-up. Those argument-level checks
are not saved-source reviews. Fresh unsaved e8f5ee checked the whole unit-center formulas
with an independent placeholder for Y^m and the triangular coefficient
recursion for finite test degrees. Fresh fa7834 checked the unit-center
and final-shift identities, including the final division relation,
plus a full two-variable division control. A final fresh whole-recovery
check included every translation in (30) and returned seven zero
residuals with independent polynomial placeholders. The universal
proofs above, not a bounded experiment, establish the assertions.

No normality of C, S, B or the surface R/fR follows. Normalizing a
PRESENTATION to monic equations is not taking integral closure and
not proving a ring normal. The result does not eliminate the nonlinear
rank-three case or recognize an arbitrary modification. It supplies
no four-variable entry or cancellation proof. No saved checker was
executed, imported, compiled, or edited, and no canonical file was
changed. A complete independent saved-source review is required
before acceptance. No expert review, formal certification, or novelty
claim has occurred.
