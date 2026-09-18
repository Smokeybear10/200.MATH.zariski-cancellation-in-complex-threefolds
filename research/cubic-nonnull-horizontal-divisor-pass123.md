# A varying-residue divisor cannot support the third speed

In the supplied actual non-null cubic framework, the scalar potential
identity proved separately below implies that no irreducible divisor of
the third speed Y can have a nonconstant finite residue of h=P/Y.
This excludes the polynomial-speed control saved in122 at the divisor
s=0. It does not exclude divisors over a constant value of h or over
h=infinity. Its scalar-potential input is proved in the companion
[potential-pole note123](cubic-nonnull-potential-pole-pass123.md).

## 1. Actual hypotheses and the additional scalar identity

Retain the actual setting of
[the non-null divisor restriction122](cubic-nonnull-divisor-restriction-pass122.md):

\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
S=\mathbb C[s,t]\subset B,\qquad K=\operatorname{Frac}S,\\
b=(g,P,Y)^t\in S^3,\qquad h=P/Y,\qquad Y\ne0,\\
L/\mathbb C(h)\text{ finite},\qquad
D=a_3h^3+a_2h^2+a_1h+a_0,\qquad a_3\in\mathbb C^*,\quad a_0,a_1,a_2\in\mathbb C,\\
g^2-DY^2=1,\qquad
Q(h)=\begin{pmatrix}
-1&0&0\\
0&D''/2&(D'-hD'')/2\\
0&(D'-hD'')/2&D-hD'+h^2D''/2
\end{pmatrix}.
\end{gathered}
\tag{1}
\]

All entries of Q are polynomials in h with complex coefficients.
The derivation prime on L is the unique extension of d/dh. The
actual invariant plane S is factorially closed in B. In particular,
every irreducible p in S remains prime in B and pB intersect S=pS.
For p dividing Y, the retained122 restriction gives p dividing
g squared minus one, so g is a p-adic unit and its residue is 1 or -1.

The additional proved input from the companion potential-pole note is
the actual rational identity

\[
z+\frac q2 x^tQ(h)x+qC_0x_1
 =\lambda\frac gY+c
   -qa'x_2-q(a-ha')x_3,
\qquad
q,\lambda\in\mathbb C^*,\quad C_0\in\mathbb C,\quad a,c\in L.
\tag{2}
\]

Here x=(x1,x2,x3) transposed and all four displayed original
coordinates are genuine polynomial coordinates of B. The scalar
potential calculation establishing (2) is separate from this note.
The argument below uses only (1), (2), and the retained prime gate;
it does not replace the actual coordinate hypothesis by a speed tuple.

## 2. A valuation trivial on the smaller field stays trivial

Let nu be any valuation on a field containing a finite algebraic
extension L/F, and assume nu is trivial on F. Then nu is trivial
on L as well. Indeed, for any nonzero alpha in L, take its monic
minimal polynomial over F, whose constant coefficient is nonzero:

\[
\alpha^d+c_{d-1}\alpha^{d-1}+\cdots+c_1\alpha+c_0=0,
\qquad c_0\ne0,
\qquad \nu(c_i)=0\text{ whenever }c_i\ne0.
\tag{3}
\]

If nu(alpha)>0, the constant term is the unique term of least
valuation. If nu(alpha)<0, the leading term alpha to the dth power
is the unique term of least valuation. Neither is possible in a
vanishing sum. Thus nu(alpha)=0. This proof makes no normality,
unramifiedness, or equality L=F assumption.

Now let p be an irreducible polynomial of S. Suppose h is regular
in S_(p), and its residue in Frac(S/(p)) is nonconstant over C.
That residue is transcendental over C, since C is algebraically
closed. Every nonzero complex polynomial in h therefore has
nonzero residue. Consequently nu_p is trivial on C(h), and (3)
makes it trivial on L. In particular every nonzero element of
L, including a, a', and c when nonzero, is p-regular.

## 3. The single pole in the scalar identity

Assume in addition p divides Y. In the localization B_(pB), every
original coordinate is regular. The restriction of its valuation
to K equals nu_p: elements of S not divisible by p remain outside
pB because pB intersect S=pS. Since h is regular, all entries of
Q(h) are regular. Section2 makes a, a', c and a-ha' regular too.

Thus every term in (2), except possibly lambda g/Y, is regular.
But g is a unit and lambda is a nonzero complex constant, so

\[
\nu_{pB}(\lambda g/Y)=-\nu_p(Y)<0.
\quad\text{Hence no }p\mid Y\text{ can satisfy }
\nu_p(h)=0\text{ with }\overline h\notin\mathbb C.
\tag{4}
\]

This contradicts (2), since a term of negative valuation cannot
equal a sum of regular terms. Equivalently, every divisor of Y
on which h is finite must have a constant complex residue of h.
If nu_p(h)>0 that residue is already zero. The new content is
the exclusion of a varying, nonzero residue when nu_p(h)=0.

## 4. The122 polynomial control fails this additional gate

For the control in Section6 of the retained122 note, write

\[
H=st,\quad U=H^2+2,\quad
g=H^2+1,\quad P=st^2U,\quad Y=st^4U^2,\quad
h=\frac1{t^2U}.
\qquad
\nu_s(Y)=\nu_s(P)=1,\quad
\overline g=1,\quad\overline h=\frac1{2t^2}\notin\mathbb C.
\tag{5}
\]

The residue computation takes place in C(t), the residue field
of S_(s); in particular t is a unit there. Thus (4) applies at
p=s and shows that this speed tuple cannot extend to the supplied
actual cubic framework satisfying (2). Its exact norm, unit-row,
metric and strict-divisor identities remain valid. They were only
coefficient controls, and are not invalidated by this additional
actual-potential obstruction.

No numerical test is needed for the valuation proof. The finite
algebraic identities of the control were checked in122. The full
non-null cubic case remains open in this note. Files through122
are unchanged.
