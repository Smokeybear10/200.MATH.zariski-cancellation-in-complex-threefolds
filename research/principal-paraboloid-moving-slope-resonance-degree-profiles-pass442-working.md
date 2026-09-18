# Eleven necessary degree profiles at the moving-slope resonance

Working necessary result: retain the full actual264 chart with
k=s+f, n=nu*s+n0, and nu' nonzero. At the resonance f'''=6nu',
the polynomial quadric generators of441 have eleven possible
positive-degree profiles, together with a separate q=0 boundary.
A nonzero constant q is impossible. Combining this result with441
bounds the ORIGINAL intrinsic degrees by deg(sigma)<=4,
deg(y)<=6 and deg(theta)<=8, without a condition on f'''.
The q=0 boundary itself forces the resonance by a gradient minor.

These are necessary restrictions on a supplied actual chart.
No surviving profile is asserted to occur. The argument does not
recognize the original kernel or turn the coefficient-field changes
into complex polynomial coordinate changes.

## 1. Exact hypotheses and the full transformed equation

Retain EVERY hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
including the original globally sliced four-ring, exact time degrees
(1,2,2,2), the entire weighted initial kernel
mathsf X^2 mathsf Z-mathsf Y^2, the literal selected derivation,
both return statements and the nonzero calibrated full scalar.
As in the fully read
[441](principal-paraboloid-arbitrary-longitudinal-moving-slope-quadric-degrees-pass441-working.md),
write
\[
\begin{gathered}
O=L[v]=L[y,\sigma,\theta],\qquad
[L:\mathbb C(t,s)]<\infty,\qquad Nv=1,\\
F=\ker_L\partial_s,\qquad
k=s+f,\qquad n=\nu s+n_0,\qquad
f,\nu,n_0\in F,\qquad b=\nu'\ne0.
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and have joint constants C.
Primes on elements of F mean their t-derivatives. No assertion
F=C(t) is made. In particular the derivative of the resonance below
is an identity in the exact field, not an assumed rational ansatz.

Here is the precise polynomial change from441. Put
\[
A=f''-2\nu,\qquad B=n_t-\nu f',\qquad E_0=\ell_s+\nu^2.
\tag{2}
\]
For independent formal U,P,V, center x=U+(AP+B)/2 and write
the full third level as
\[
H-h=x^2+(bP-E_0)V+R_3(P).
\tag{3}
\]
The complete R3 is441(6), including its coefficient-field level h.
Divide it in L[P], before evaluation, to define
\[
R_3(P)=(bP-E_0)T_2(P)+\rho,\qquad \deg T_2\le2.
\tag{4}
\]
The formal polynomial change and its inverse are
\[
\begin{aligned}
p&=P-E_0/b,&q&=V+T_2(P),&x&=U+(AP+B)/2,\\
P&=p+E_0/b,&V&=q-T_2(P),&U&=x-(AP+B)/2.
\end{aligned}
\tag{5}
\]
After evaluation use x,p,q for the elements of O. By441, with d=-rho,
\[
x^2+bpq=d,\qquad O=L[x,p,q],\qquad p\notin L.
\tag{6}
\]
The last assertion uses the direct constant-sigma exclusion440.
No denominator b*sigma-E0 has been introduced into O.

Let tau substitute the inverse(5), and define the FULL fourth level
\[
\Phi=\tau\left(Q-q_0-\frac{f''}{2}(H-h)\right).
\tag{7}
\]
Here H,Q,h,q0 are the genuine polynomials and levels of
[438](principal-paraboloid-moving-transverse-slope-fourth-potential-pass438-working.md).
Thus (7), not an unspecified lower-degree remainder, defines every
coefficient used below. In particular all h_t,h_s and q0 terms are
retained. The complete support proved in441 is
\[
\begin{aligned}
\Phi={}&\alpha p^2x+b xq+u_1px+
\delta p^4+\kappa p^3+\epsilon p^2q+F_2q^2\\
&+c_{20}p^2+c_{11}pq+c_{10}p+c_{01}q+c_{00}.
\end{aligned}
\tag{8}
\]
The subscript on F2 distinguishes this coefficient from the field F.
There is NO additional constant multiple of x. This is essential
at the constant-q boundary. In fact the entire x coefficient is
bq+(bP-E0)(T2'(P)-2P-f'), where this prime is a formal P-derivative.
It equals bq+alpha*p^2+u1*p after translating P.

The two evaluated gradients of x^2+bpq-d and Phi have minors
generating O, and both equations vanish. Subtracting the multiple
in(7) preserves their gradient wedge. The polynomial automorphism
(5) has polynomial inverse Jacobian, so its second exterior power
preserves the ideal of evaluated minors. These facts are established
in441 before either resonance branch is considered.

Add the resonance assumption
\[
\alpha=\frac{f'''}3-2b=0.
\tag{9}
\]
Since f''''=6b', the exact coefficients441(12) become
\[
\boxed{
\delta=-\frac{b'+2\ell_{ss}}4,\qquad
\epsilon=-2\delta,\qquad
F_2=-\frac{\ell_{ss}}2=\delta+\frac{b'}4.}
\tag{10}
\]
All other coefficients in(8) remain their full values from(7).
They are not free numerical parameters, and no extra differential
identities for them will be assumed.

## 2. The degree bounds that will be used

The elementary whole-line dimension argument of
[299, Sections2--4](principal-paraboloid-generic-degree-bound-pass299-working.md)
applies to any two vanishing equations of total degrees at most
D1,D2 whose evaluated gradient minors generate O. It gives
\[
\max(\deg_vx,\deg_vp,\deg_vq)\le D_1D_2.
\tag{11}
\]
Briefly, removing their polynomial gcd does not remove the actual
line: the minors force that gcd to evaluate to a unit. The reduced
coprime homogeneous equations give an upper bound D1*D2*n+O(1)
on the dimension of evaluated total-degree-at-most-n polynomials.
Whole generation O=L[x,p,q] gives the lower bound D*(n-C+1),
where D is the largest intrinsic degree. This proves(11) over L.
It does not require these equations to generate the whole ideal.

Initially (6),(8) have total degrees at most two and four, so
\[
\max(\deg_vx,\deg_vp,\deg_vq)\le8.
\tag{12}
\]
If coefficient comparisons make the FULL Phi have total degree
at most two, the same argument improves this bound to four.
Zero polynomials are ignored when taking these maxima.

## 3. Constant q, including the zero boundary

Suppose first q=q_c in L*. Equation(6) gives
p=(d-x^2)/(b*q_c), and whole generation gives O=L[x]. Thus x is
an affine intrinsic parameter. All terms in Phi other than
b*x*q_c+u1*p*x are even polynomials in this parameter. Its odd part is
\[
x\left(bq_c+\frac{u_1(d-x^2)}{bq_c}\right).
\tag{13}
\]
The cubic coefficient would force u1=0, leaving the nonzero
coefficient b*q_c of x. Therefore nonzero constant q is impossible.

If q=0, then x^2=d implies x=xi in L. Whole generation gives
O=L[p], hence deg_v p=1. The evaluated gradient of the quadric
is (2xi,0,bp). Its entries must generate a unit ideal since the
gradient minors do. If xi=0 this ideal would be contained in (p),
which is proper. Consequently
\[
x=\xi\in L^*,\qquad d=\xi^2,\qquad \deg_vp=1.
\tag{14}
\]
In fact this boundary forces the resonance even if(9) is not
assumed. In the full support(8), its level identity implies that
the evaluated p-partial is zero. The other two evaluated partials
are alpha*p^2+u1*p and b*xi+epsilon*p^2+c11*p+c01. The sole
possibly nonzero gradient minor, up to sign, is therefore
\[
-b\alpha p^3+(2\xi\epsilon-bu_1)p^2+
2\xi c_{11}p+2\xi(b\xi+c_{01}).
\]
Its unit condition forces alpha=0 since b is nonzero. Thus the
q=0 candidate retained in441's nonresonant list cannot occur.
This assertion uses only441's general support and minor ideal.

Because p is transcendental over L, evaluating(8) at q=0 forces
delta=kappa=c20=c00=0 and u1*xi+c10=0. Equation(10) also gives
epsilon=0. At this stage the only possibly nonzero gradient minor,
up to sign, is
\[
-b u_1p^2+2\xi c_{11}p+2\xi(b\xi+c_{01}).
\tag{15}
\]
It must be a unit of L[p]. Thus the complete necessary boundary
ledger is
\[
\boxed{
\delta=\epsilon=\kappa=u_1=c_{20}=c_{11}=c_{10}=c_{00}=0,
\qquad b\xi+c_{01}\ne0.}
\tag{16}
\]
In particular F2=b'/4 in this boundary. Neither a realization nor
an exclusion of this remaining q=0 case is asserted.

This boundary also identifies the exceptional evaluated linear
remainder of438. Its remainder R is the coefficient of U in
Q-q0-f''(H-h)/2, so (5),(8) give
\[
r:=R(\sigma,\theta)=u_1p+bq
\quad\hbox{under the resonance},\qquad
r=0\ \Longleftrightarrow\ q=0.
\tag{17}
\]
For the nontrivial implication, if r=0 and u1 is nonzero, then
q=-u1*p/b and x^2-u1*p^2=d. Over an algebraic closure of L,
factor the left side as
(x-sqrt(u1)*p)(x+sqrt(u1)*p). If d is nonzero both factors are
units of the polynomial line, forcing p constant. If d=0, one
factor vanishes identically and x,p,q are all multiples of p.
The full evaluated quadric gradient is then contained in (p),
contradicting its unit ideal after this field extension. Thus
u1=0 and q=0. The converse follows from(16). This does not
identify the original ambient coordinate ring with a plane.

## 4. Positive degrees and the lower/equal cases

It remains to take q nonconstant. Then x is nonconstant as well:
otherwise the nonconstant product p*q would be constant by(6).
Write
\[
a=\deg_vp\ge1,\qquad c=\deg_vx\ge1,\qquad e=\deg_vq\ge1.
\]
The quadric and(12) give
\[
2c=a+e,\qquad a,c,e\le8.
\tag{18}
\]
The complete list of potentially nonzero term degrees in Phi is
\[
\begin{array}{c|rrrrrrrrrr}
\text{term}&xq&px&p^4&p^3&p^2q&q^2&p^2&pq&p&q\\\hline
\text{degree}&c+e&a+c&4a&3a&2a+e&2e&2a&a+e&a&e.
\end{array}
\tag{19}
\]
The coefficient of xq is b, which never vanishes. At each step
a uniquely highest nonzero term is impossible. A coefficient
forced to vanish is removed before the next comparison; in
particular delta=0 always removes epsilon as well by(10).

If e<a, successive comparisons force
\[
\delta=\epsilon=\kappa=c_{20}=u_1=c_{11}=0.
\tag{20}
\]
Indeed the degrees 4a,3a,2a,a+c,a+e are successively greater
than every surviving competing degree. The remaining equation is
b*x*q+F2*q^2+c10*p+c01*q+c00=0. Its xq term has degree greater
than 2e and e, so it must balance c10*p. Therefore
a=3e, c=2e and c10 is nonzero. Moreover this FULL remaining
equation is quadratic. Equation(11) with D1=D2=2 forces a<=4.
Thus this case has only
\[
(a,c,e)=(3,2,1).
\tag{21}
\]
In particular the bound eight alone would leave (6,4,2), but the
two-quadratic bound removes it.

If e=a, then c=a. First p^4 gives delta=epsilon=0, and then
p^3 gives kappa=0. The FULL Phi again has total degree at most
two, so
\[
(a,c,e)=(j,j,j),\qquad 1\le j\le4.
\tag{22}
\]

## 5. The intermediate cases a<e<=2a

Suppose a<e<2a. The term p^4 is uniquely highest initially,
so delta=epsilon=0. By(10), F2=b'/4.

If b' is nonzero, q^2 has greater degree than xq and every
remaining term except possibly p^3. It cannot be eliminated.
Consequently 2e=3a and kappa is nonzero. Equation(18) gives
c=5a/4. Integrality and the bound eight leave exactly
\[
(a,c,e)=(4,5,6),\qquad b'\ne0,\qquad \kappa\ne0.
\tag{23}
\]
If b'=0, the q^2 term is absent. The mandatory xq term is
higher than every remaining term except possibly p^3, so
c+e=3a and kappa is nonzero. Hence e=5a/3,c=4a/3, giving
\[
(a,c,e)=(3,4,5),\qquad b'=0,\qquad \kappa\ne0.
\tag{24}
\]
Both (23),(24) also retain delta=epsilon=0. These comparisons
give necessary cases, not sufficient coefficient conditions.

If e=2a, then c=3a/2. Integrality and e<=8 leave
\[
(a,c,e)=(2,3,4)\quad\text{or}\quad(4,6,8).
\tag{25}
\]
Here delta is necessarily nonzero. Otherwise epsilon=0, after
which q^2 would be uniquely highest until F2=0. Then xq has
degree 7a/2, strictly greater than p^3 and all remaining terms,
a contradiction.

## 6. The upper cases e>2a

Now q^2 is uniquely highest, so F2=0, equivalently ell_ss=0.
By(10), delta=-b'/4 and epsilon=b'/2. If b'=0, both vanish
and the mandatory xq term is uniquely highest, impossible.
Thus b' is nonzero.

For 2a<e<3a, the term epsilon*p^2*q is uniquely highest:
its degree exceeds c+e by (3a-e)/2, and exceeds 4a and all
other remaining degrees. For e>3a it is instead xq that is
uniquely highest; it also exceeds 4a. Both strict ranges are
impossible. Therefore e=3a and c=2a. The bound eight gives
\[
\boxed{
(a,c,e)=(1,2,3)\quad\text{or}\quad(2,4,6),\qquad
\ell_{ss}=0,\quad b'\ne0.}
\tag{26}
\]

## 7. Exhaustive necessary list and an original-degree corollary

Under(1) and the resonance(9), the q nonzero branch has exactly
the following exhaustive NECESSARY list:
\[
\boxed{
\begin{aligned}
(\deg_vp,\deg_vx,\deg_vq)\in\{
 &(3,2,1),(1,1,1),(2,2,2),(3,3,3),(4,4,4),\\
 &(4,5,6),(3,4,5),(2,3,4),(4,6,8),(1,2,3),(2,4,6)\}.
\end{aligned}}
\tag{27}
\]
The coefficient gates in(20)--(26) remain necessary within this
list. The q=0 case is precisely the necessary boundary(14),(16);
nonzero constant q has been excluded. No assertion of existence
or sufficiency is contained in the word "list."

The nonresonant list441(21) has the same upper bounds
a<=4,c<=6,e<=8; its q=0 candidate was excluded in Section3 here.
Since alpha is either
zero or nonzero in L, the two lists together show, under(1) with
NO resonance condition,
\[
\deg_vp\le4,\qquad \deg_vx\le6,\qquad \deg_vq\le8,
\tag{28}
\]
where the zero q case is understood separately. Returning through
the evaluated inverse(5),
\[
\sigma=p+E_0/b,\qquad y=x-(A\sigma+B)/2,\qquad
\theta=q-T_2(\sigma),\qquad \deg T_2\le2.
\]
Coefficients here are in L and have intrinsic degree zero. Possible
cancellation only lowers degrees. We obtain the scoped corollary
\[
\boxed{
1\le\deg_v\sigma\le4,\qquad
\deg_v y\le6,\qquad \deg_v\theta\le8.}
\tag{29}
\]
A zero y or theta is simply ignored in the corresponding upper
bound. This conclusion concerns the supplied moving-slope chart,
not arbitrary polynomial generators of an unknown kernel.

## 8. Dependency and unresolved-entry boundary

The direct input is441's exact polynomial quadric transformation,
full fourth support, unit gradient-minor ideal, and degree-eight
bound. Its nonresonant profile list is used only for(28),(29).
The improvement to four when the full fourth level is quadratic
uses the abstract dimension proof299, read completely here. The
actual hypotheses and prior derivation of those inputs are retained;
this note is not a recursive review of all their ancestors.

The degree argument is the sequence of written inequalities, not
a finite coefficient search. Fresh unsaved87a95e checked the
resonance coefficient identity, the exact constant-q odd part,
and the q=0 gradient-minor ledger, with zero residuals. The
current441 and299 were read through EOF before writing.
Fresh unsaved065bd2 also checked the generic q=0 minor before
assuming resonance, including its cubic coefficient -b*alpha.

All coefficient functions, their exact derivative constraints, the
full nonzero scalar, both actual returns and original-ring entry
still matter. A finite list of intrinsic degrees is not a finite
classification of numerical or rational-function examples. No
original coordinate change, realization, general recognition,
cancellation, historical novelty or formal certification is claimed.
No saved checker was executed, imported, compiled or rerun.
