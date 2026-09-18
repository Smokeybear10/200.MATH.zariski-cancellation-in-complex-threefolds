# Five remaining degree pairs in the rebuilt cubic repeated-root chart

Status: bounded working reduction for a supplied actual full initial
kernel. In the rebuilt chart \(q=\rho^2-t^3\), the possible projected
degree pairs are reduced to
\[
(\deg_vy,\deg_v\theta)=(1,2),(1,3),(2,3),(3,6),(4,6).
\]
The two additional pairs \((2,4)\) and \((2,5)\) are excluded here by
the complete evaluated gradient and scalar determinant.
None of the five displayed pairs is recognized or excluded in this note.

The final section gives an exact formal \((3,6)\) configuration showing
why the conductor, cubic center and coarse cofactor conditions alone
cannot finish the reduction. It is not an actual sliced frame.

## 1. Actual input and the rebuilt potentials

Assume the actual globally sliced hypotheses of
[237](repeated-root-rebuilt-chart-line-exclusion-pass237-working.md),
after its actual bad-slot exchange and reconstruction of the literal
selected partial:
\[
\begin{gathered}
\mathscr B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker(\text{full leading evaluation})=(X^2Z-W^2+XY^3),\\
N=[u^3](\partial_Z|_A)\ne0,\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
t,\rho\text{ algebraically independent},\quad
[L:\mathbb C(t,\rho)]<\infty,\quad q=\rho^2-t^3,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\theta X+\rho X^2,\quad L[y,z,w]=L[v].
\end{gathered}                                                    \tag{1}
\]
Capital letters remain actual polynomial coordinates. No old selected
derivation or coefficient field is carried through the bad-slot exchange.
The coefficient partials extend uniquely to \(L\) and fix \(v\).

Retaining every lower potential \(k,n,\ell,m\in L\), universal184 gives
\[
\begin{gathered}
f=V^2-3tU^2+k_tU+k_\rho V+n,\quad
\mathcal R=2V+k_\rho,\quad c=f_\rho,\\
S=-U^3+H_2(k)+H_1(n),\quad
Q=H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m,\\
T=\ell-S,\quad
\mathcal H=T^2+\mathcal R cT+\mathcal R^2Q,\quad
\mathcal H_6=U^6,\\
\sigma=-3t^2y+2\rho\theta+k,\quad z=2\rho w+f(y,\theta),\\
R=2\theta+k_\rho,\quad Rw=T(y,\theta),\quad
w^2+c(y,\theta)w+Q(y,\theta)=0 .
\end{gathered}                                                    \tag{2}
\]
The sextic is nonzero: \(T\) has leading cubic \(U^3\), while the other
two summands of \(\mathcal H\) have total degree at most five.
By237, \(R\ne0\) and \(y\notin L\).

Put \(\mathcal O=L[v]\) and \(\mathcal C=L[y,\theta]\).
The monic equation for \(w\), its linear return, and the whole-line
equality in (1) give
\[
\mathcal O=\mathcal C+\mathcal Cw,\qquad
R\mathcal O\subset\mathcal C,\qquad
\operatorname{Frac}\mathcal C=L(v).
\tag{3}
\]
Let \(G\) generate the height-one plane evaluation kernel.
The exact-field characteristic-polynomial argument of235 applies to
this finite birational parametrization. Since \(\mathcal H_6=U^6\),
it gives
\[
\begin{gathered}
G_d=\gamma U^d,\quad \gamma\in L^*,\qquad
1\le i:=\deg_vy<d:=\deg_v\theta=\deg G\le6,\\
\mathcal H=GQ_1,\quad
0\ne q_1:=Q_1(y,\theta)\mid R^3 .
\end{gathered}                                                    \tag{4}
\]
In particular \(d\ge2\). Normality of \(\mathcal C\) is not assumed.

We use the precise evaluated identities, with coefficient derivatives
taken before evaluation,
\[
\begin{gathered}
B_1=f_t(y,\theta),\quad C_1=f_\rho(y,\theta)+2w,\\
\mathcal H_V(y,\theta)=q_1G_V(y,\theta)
              =-R(C_1^2+R\Lambda_\rho),\\
Rw_v=-B_1y_v-C_1\theta_v,\qquad
J_0=[dy\wedge(R\,d\theta+B_1dt+C_1d\rho)\wedge dw]
                   _{dt\wedge d\rho\wedge dv}=-(EX)^3\in L^* .
\end{gathered}                                                    \tag{5}
\]
Here \(\Lambda_\rho=\ell_\rho-S_\rho(y,\theta)
-\mathcal R_\rho(y,\theta)w\).
The general local theorem in
[238](repeated-root-return-excess-order-bound-pass238-working.md)
therefore applies, and in particular gives
\[
i\le2\quad\Longrightarrow\quad q_1\mid R.
\tag{6}
\]

We will also use the following direct part of its proof. At any geometric
root \(r\) of \(R\), if \(C_1(r)=0\), the determinant forces
\(B_1(r)\ne0\). Since \(R_v=2\theta_v\), a root of multiplicity
\(m_r\) has \(\operatorname{ord}_r\theta_v=m_r-1\).
Both \(Rw_v\) and \(C_1\theta_v\) then have order at least \(m_r\).
Thus the third identity of (5) forces
\[
R(r)=C_1(r)=0
\quad\Longrightarrow\quad
B_1(r)\ne0,\qquad \operatorname{ord}_r y_v\ge m_r .
\tag{7}
\]
All derivatives are formed before root evaluation. No coefficient
partial differentiates a moving root.

## 2. The cubic center and the preliminary seven pairs

Write \(a=k_\rho,\ c=k_{\rho\rho}\) in this section only, and set
\[
\begin{aligned}
p(U)&=-U^3+\frac{k_{tt}}2U^2+
        \left(n_t-\frac{ak_{t\rho}}2\right)U
           +\frac{a^2c}{8}-\frac{an_\rho}{2}-\ell,\\
D(U,V)&=-\frac{k_{t\rho}}2U-\frac{n_\rho}2-\frac c4V+\frac{ca}{8},
\qquad \widetilde w=w-D(y,\theta).
\end{aligned}                                                    \tag{8}
\]
Subtracting the value of \(S-\ell\) at \(V=-a/2\) proves exactly
\[
R\widetilde w=-p(y),\qquad
\deg_v\widetilde w=3i-d,\qquad d\le3i .
\tag{9}
\]
The polynomial \(D\) is affine over \(L\), so
\(\mathcal C+\mathcal C\widetilde w=\mathcal O\).
These are coefficient-field changes of expressions, not ambient maps.

If \(d=3i\), then \(\widetilde w\in L^*\), so (9) gives
\(\theta\in L[y]\). Equation (8) gives \(w\in L[y]\), and (2) gives
\(z\in L[y]\). Consequently \(\mathcal O=L[y]\), forcing \(i=1\).

For completeness the coprime-degree conductor argument of206 gives
another exact restriction. If \(\gcd(i,d)=1\), the ring \(\mathcal O\)
is free of rank \(i\) over \(L[y]\). The characteristic polynomial
of multiplication by \(\theta\) is its monic minimal polynomial:
birationality makes its degree \(i\). Hence
\(\mathcal C=\bigoplus_{j=0}^{i-1}L[y]\theta^j\).
The leading degrees \(ki+jd\), \(k\ge0,\ 0\le j<i\), have distinct
residues modulo \(i\); no cancellation between summands is possible.
The degree semigroup is exactly \(\langle i,d\rangle\), with largest
missing integer \(id-i-d\).
If \(i\ge3\) and \(d>i\), this missing integer is at least \(d\).
But (3) puts \(Rv^{\,id-i-2d}\) in \(\mathcal C\), with exactly that
missing degree, a contradiction. The exponent is nonnegative.

Combining these restrictions with \(1\le i<d\le6\) leaves precisely
\[
(i,d)=(1,2),(1,3),(2,3),(2,4),(2,5),(3,6),(4,6).
\tag{10}
\]
These are necessary degree possibilities, not realizability statements.

## 3. Exact parameter conventions for the two quadratic-first cases

In either case \(i=2\), complete the square by a translation
\[
x=v+\xi_0,\quad \xi_0\in L,\qquad y=a_2x^2+b_2,\quad a_2\in L^* .
\tag{11}
\]
No square root of \(a_2\) is taken. In formal plane calculations write
\(u=(U-b_2)/a_2\), and retain \(\mathcal R=2V+k_\rho\).
These are invertible affine changes over the exact field \(L\) only.
They are not claimed to be original-coordinate automorphisms.

In particular \(x_v=1\), so \(y_v=2a_2x\).
The original coefficient partials need not fix \(x\).
We do not replace them by fixed-\(x\) partials: all uses of (5),(7)
remain in their original derivative convention. Differentiation of
a formal \(G\) with respect to \(V\) fixes \(U\) and all coefficients,
so \(\mathcal R_V=2\) and \(u_V=0\).

Since \(i=2\), (6) supplies the actual stronger divisor \(q_1\mid R\).
Also
\[
\mathcal H(U,-k_\rho/2)=p(U)^2 .
\tag{12}
\]
We may choose any scalar normalization of the irreducible generator
\(G\), with the inverse normalization for \(Q_1\).

## 4. Excluding the pair \((2,5)\)

Here (9) says \(\widetilde w=c_1(x-s)\), where \(c_1\in L^*\)
and \(s\in L\). Polynomial return gives
\[
p(a_2u+b_2)=(u-s^2)A(u),\quad \deg A=2,\qquad
R=-\frac{(x+s)A(x^2)}{c_1}.
\tag{13}
\]
Indeed the left side evaluated at \(u=x^2\) is even and vanishes at
\(x=s\). It is divisible by \(x^2-s^2\), also when \(s=0\), since
an even polynomial vanishing at zero has multiplicity at least two.
All divisions in (13) are in \(L[u]\).

The full plane ring is \(L[x^2,xA(x^2)]\): subtract the even part
of \(R\) to see both inclusions. An exact irreducible relation is
\[
G(U,V)=\bigl(c_1\mathcal R+sA(u)\bigr)^2-uA(u)^2.
\tag{14}
\]
It is irreducible over \(L(u)\) as a quadratic in \(\mathcal R\),
because \(u\) is not a square there. It is primitive with nonzero
constant leading coefficient in \(\mathcal R\), so Gauss's lemma
gives irreducibility in the plane ring. Its total degree is five
and its top is a nonzero multiple of \(U^5\).

Since \(\deg\mathcal H=6\), its quotient \(Q_1\) has degree one
and pure top a multiple of \(U\), so it is independent of \(V\).
Using (12)--(14) determines it exactly:
\[
Q_1=-(u-s^2),\qquad q_1=s^2-x^2,\qquad
\frac{\mathcal H_V(y,\theta)}R=-4c_1^2x(x-s).
\tag{15}
\]
For the last identity, direct differentiation gives
\(G_V(y,\theta)=-4c_1xA(x^2)\); the factors cancel using (13).
The right side in (15) is polynomial. Its root evaluation therefore
does not presume \(R\) invertible in the line ring.

If \(s\ne0\), the divisor \(q_1\mid R\) makes \(x=s\) a return root.
Equation (15) and (5) give \(C_1(s)=0\). Then (7) forces
\(y_v(s)=0\), contrary to \(2a_2s\ne0\).
Thus \(s=0\).
Now \(q_1=-x^2\mid R=-xA(x^2)/c_1\) forces \(A(0)=0\).
The root \(x=0\) of \(R\) consequently has multiplicity at least three.
Equation (15) still forces \(C_1(0)=0\), so (7) requires
\(\operatorname{ord}_0y_v\ge3\).
But \(y_v=2a_2x\) has order one. This contradiction excludes \((2,5)\).

## 5. Excluding the pair \((2,4)\)

Now \(\widetilde w=Ax^2+Bx+C\), with \(A\ne0\).
Also \(B\ne0\): otherwise \(\widetilde w\in L[x^2]\), and (9)
would put \(R\) in \(L(x^2)\cap L[x]=L[x^2]\), contradicting
\(\operatorname{Frac}\mathcal C=L(x)\).
Define the norm polynomial
\[
\mathcal N(u)=(Au+C)^2-B^2u .
\]
It divides \(p(a_2u+b_2)\). To check the possible common-root issue,
work temporarily over an algebraic closure of \(L\).
The two factors \(Ax^2+Bx+C\) and \(Ax^2-Bx+C\) can share only
the root zero. When \(C=0\), each has that root simply since \(B\ne0\),
and the even polynomial \(p(a_2x^2+b_2)\) has even multiplicity there.
At nonzero roots the factors are relatively prime, with their
multiplicities paired by evenness. Thus their full product divides.
Polynomial division descends the resulting divisibility to \(L[u]\).

Consequently, for a polynomial \(Q(u)\) of degree one,
\[
p(a_2u+b_2)=\mathcal N(u)Q(u),\qquad
R=-(Ax^2-Bx+C)Q(x^2).
\tag{16}
\]
The exact irreducible plane relation can be chosen as
\[
G(U,V)=
 \bigl(\mathcal R+Q(u)(Au+C)\bigr)^2-B^2uQ(u)^2 .
\tag{17}
\]
Its irreducibility follows as in (14), and its total degree is four
with pure top a nonzero multiple of \(U^4\).
The quotient \(Q_1\) has degree two and pure top a multiple of \(U^2\).
Specializing \(\mathcal R=0\) in (12),(16),(17) gives
\(Q_1(U,-k_\rho/2)=\mathcal N(u)\).
The degree-two tops agree, so \(Q_1-\mathcal N(u)\) has degree
at most one and vanishes on that line. Hence, for \(\gamma\in L\),
\[
\begin{gathered}
Q_1=\mathcal N(u)+\gamma\mathcal R,\qquad
L_1(x)=Ax^2+Bx+C-\gamma Q(x^2),\\
q_1=(Ax^2-Bx+C)L_1(x),\qquad
\frac{\mathcal H_V(y,\theta)}R=-4BxL_1(x).
\end{gathered}                                                    \tag{18}
\]
The last equality follows by differentiating (17), whose evaluated
\(V\)-derivative is \(4BxQ(x^2)\), and then using (16).

By \(q_1\mid R\), cancellation in the domain \(L[x]\) gives
\(L_1\mid Q(x^2)\).
Its odd coefficient is the nonzero \(B\).
If \(L_1\) had degree two, it would be a scalar multiple of the even
quadratic \(Q(x^2)\), which is impossible. It cannot be constant.
Thus \(L_1\) is linear, with a root \(r\in L\).
At this root, \(Q(r^2)=0\), so \(R(r)=0\).
Equations (18),(5),(7) force \(y_v(r)=0\), hence \(r=0\).

It follows that \(Q(u)=q_*u\) with \(q_*\in L^*\), and that \(C=0\).
Equation (16) becomes \(R=-q_*x^3(Ax-B)\), of order exactly three
at zero. Equation (18) gives \(C_1(0)=0\).
Again (7) contradicts \(\operatorname{ord}_0y_v=1\).
This excludes \((2,4)\).

Removing these two pairs from (10) proves the stated five-pair frontier.

## 6. A precise formal \((3,6)\) countercontrol

Over any characteristic-zero field \(L\), take a polynomial parameter \(x\)
and define
\[
\begin{gathered}
y=x^3,\quad P=x^4+x^2,\quad
\theta=(x^6+x^4+x^2)/2,\quad R=2\theta=y^2+P,\\
p(U)=-U^3+U,\qquad \widetilde w=y-x,\qquad
\mathcal C=L[y,\theta]=L[y,P]\subset L[x]=\mathcal O .
\end{gathered}                                                    \tag{19}
\]
Then \(R\widetilde w=-p(y)\) exactly.
Moreover
\[
Rx=yP+y,\quad Rx^2=P^2-y^2,\qquad
x=y-\widetilde w,\quad x^2=P-y^2+y\widetilde w .
\tag{20}
\]
The basis \(1,x,x^2\) of \(\mathcal O\) over \(L[y]\) proves both
\(R\mathcal O\subset\mathcal C\) and
\(\mathcal O=\mathcal C+\mathcal C\widetilde w\).
It also gives the exact birational field equality.
The coprime degree pair \(3,4\) for \(y,P\) shows that \(\mathcal C\)
is proper: degree one is missing from its degree semigroup.
The original pair \((y,\theta)\) has degrees \((3,6)\).

Even the correct pure sextic top and squared cubic center can coexist
with these algebraic return conditions. Setting \(r=2V\), the polynomial
\[
G_0(U,V)=-(r-U^2)^3+3U^2(r-U^2)+U^2+U^4
\tag{21}
\]
vanishes on (19), has pure top \(U^6\), and satisfies
\(G_0(U,0)=p(U)^2\).
It is the irreducible relation: \(P^3-3y^2P-y^2-y^4=0\) is the
degree-three minimal polynomial over \(L(y)\), by birationality and
\([L(x):L(y)]=3\).
Formally taking \(\mathcal H=G_0\), \(Q_1=1\) also meets the coarse
and strict cofactor divisor bounds.

This configuration is not asserted to satisfy the universal lower
potentials, their differentiated identities, or \(J_0\in L^*\).
No actual four-coordinate frame is constructed. Its purpose is only
to disprove an exclusion based solely on the displayed conductor,
center, module-return and leading-cofactor data.

The unresolved pairs still require the full actual equations and an
original-ring endpoint. No generic parameter change above supplies
an ambient coordinate. This note changes no earlier source or packet
and executes no saved checker. The unrestricted cancellation problem,
arbitrary frame entry and historical novelty remain outside its claims.
