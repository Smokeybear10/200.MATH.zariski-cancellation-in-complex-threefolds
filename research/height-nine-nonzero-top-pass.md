# Height nine: the nonzero fourth-coordinate constant closes

The complementary zero-top branch is now also closed under the slice
hypothesis in [the complete mixed-frame report](../deep-pass-13.md).

The remaining branch with
\[
k=E^4(x_4)\ne0,\qquad c=E^5(x)\ne0,\qquad V\ne0
\]
has a polynomial kernel. The key is an explicitly constructed commuting
derivation that fixes the derived slice. It becomes a coordinate partial
while preserving one good partial, which is enough for the established
three-variable criterion. No claim that \(W_4\) is locally nilpotent is
needed.

This closes the nonzero-\(k\) alternative left in
[height-nine-first-pass.md](height-nine-first-pass.md). It does not, by
itself, close that note's zero-\(k\) alternative or raise the universal
height threshold to nine.

## 1. Exact input and the constant directions

Let \(B=\mathbb C[x_1,x_2,x_3,x_4]=K[s_*]\), with
\(E\in\operatorname{LND}(B)\) and \(E(s_*)=1\). Assume
\[
\operatorname{ad}_E^2(\partial_i)=0\quad(i\le3),
\qquad \operatorname{ad}_E^3(\partial_4)=0.
\]
Put \(P=E(x)\), \(J=\operatorname{Jac}P\), and
\(V=[E,[E,\partial_4]]\), with coefficient column \(v=V(x)\).
The previous pass and its
[independent audit](height-nine-first-audit.md) establish
\[
k=E^4(x_4)\in\mathbb C^*,\quad c=E^5(x)\in\mathbb C^4,
\quad c_4=0,\quad Jc=2kv.
\tag{1}
\]
If \(c=0\), (1) forces \(V=0\), and the height-eight theorem applies.
We therefore assume \(c\ne0\) and \(V\ne0\).

The weighted adjugate bound and the affine-line argument in that pass
give, with exactly this normalization,
\[
s=\frac{E^3(x_4)}k,\qquad E(s)=1,\qquad
E^4(x)=cs+d,
\quad d\in\mathbb C^4,\quad d_4=k.
\tag{2}
\]
Its coefficient identity
\(J(E^4x)=c/4+(3/2)ksv\), combined with (1), gives
\[
Jd=\frac c4-\frac k2sv.
\tag{3}
\]

Write \(A=T_c=c\cdot\partial\) and \(B_0=T_d=d\cdot\partial\).
These are independent constant directions, because \(c_4=0\) and
\(d_4=k\ne0\). In particular \(A\ne0\). The exact brackets are
\[
[E,A]=-2kV,\qquad
[E,B_0]=-\frac14A+\frac k2sV.
\tag{4}
\]
The direction \(A\) is a constant linear combination of the first
three original partials, so
\(\operatorname{ad}_E^2(A)=0\).

## 2. A commuting derivation that fixes the derived slice

Define
\[
D_0=4B_0+sA.
\tag{5}
\]
Using (4) and \(E(s)=1\) gives actual commutation, not just a vanishing
double bracket:
\[
[E,D_0]
=-A+2ksV+A-2ksV=0.
\tag{6}
\]
Also \(D_0(x_4)=4k\), because \(c_4=0\). Consequently
\[
D_0(s)=\frac1kD_0(E^3x_4)
=\frac1kE^3(D_0x_4)=0.
\tag{7}
\]
The middle equality uses (6). It does not treat \(E^3\) as a derivation.
Since the coefficient vector of \(D_0\) is \(4d+sc\), (7) implies
\(D_0^2(x_i)=0\) for all four generators. Thus \(D_0\) is a nice LND.
This proves local nilpotence; the constant value on \(x_4\) alone would
not have proved it.

## 3. Polynomial straightening preserves the good direction

Choose linear coordinates \((a,b,z_1,z_2)\) such that
\[
A=\partial_a,\qquad B_0=\partial_b,
\qquad b=x_4/k.
\tag{8}
\]
This is possible because the two constant directions are independent.
Choose \(a\) dual to \(c\), vanishing on \(d\), and choose
\(z_1,z_2\) in the common annihilator of \(c,d\). In these coordinates
(7) is
\[
4s_b+s s_a=0.
\tag{9}
\]

Here a polynomial-degree argument is decisive. Let
\(R=\mathbb C[z_1,z_2]\), and view \(s\in R[b][a]\). If
\(m=\deg_a s\ge2\), then \(s s_a\) has \(a\)-degree \(2m-1\),
strictly larger than the degree at most \(m\) of \(4s_b\). The domain
property and characteristic zero rule out cancellation. If \(m=1\),
write \(s=r(b)a+u(b)\), with \(0\ne r\in R[b]\). The coefficient
of \(a\) in (9) gives
\[
4r_b+r^2=0.
\]
This is impossible by \(b\)-degree: \(r^2\) has degree twice that of
\(r\), while \(r_b\) has smaller degree or is zero. Hence \(m=0\),
and (9) then gives \(s_b=0\). Therefore
\[
s\in\mathbb C[z_1,z_2].
\tag{10}
\]
No algebraic-coordinate assertion about \(s\) has been used.

Now set
\[
q=a-\frac b4s(z_1,z_2).
\tag{11}
\]
The explicit inverse is \(a=q+bs(z_1,z_2)/4\). Thus
\[
B=\mathbb C[q,b,z_1,z_2],\qquad
D_0=4\partial_b,\qquad A=\partial_q.
\tag{12}
\]
In particular the straightening preserves \(A\) as a coordinate
partial. It does not require that the two other changed partials retain
their former double-bracket identities.

## 4. Three-variable descent and kernel recognition

By (6), \(E\) preserves the actual coordinate three-ring
\[
R_3=\ker D_0=\mathbb C[q,z_1,z_2].
\]
Its restriction \(E_3\) is an LND, and the preserved good partial gives
\[
[E_3,[E_3,\partial_q]]=0.
\]
The single-partial lemma proved in
[height-seven-audit.md, Section 2](height-seven-audit.md) supplies a
coordinate \(p\) of \(R_3\) annihilated by \(E_3\). It is therefore
an ambient coordinate of \(B=R_3[b]\) annihilated by \(E\). That lemma
uses the commuting-LND theorem in its independent case and primitive
normalization followed by Rentschler in its dependent case. The exact
source statement for the independent case is
[Dasgupta and Gaifullin, Proposition 2.14](https://arxiv.org/pdf/2306.00510).
It is not an assertion that every LND on a polynomial three-ring fixes
an ambient coordinate.

Finally \(K\) is regular because \(K[s_*]\) is regular. With the
invariant ambient coordinate \(p\), the hypotheses of
[Bhatwadekar, Gupta and Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1)
hold: a nonzero \(\mathbb C[p]\)-linear LND on \(\mathbb C[p]^{[3]}\)
has a polynomial kernel over \(\mathbb C[p]\) when that kernel is
regular. Hence
\[
K=\mathbb C[p]^{[2]}\simeq\mathbb C^{[3]}.
\]

## 5. Failed shortcut and exact controls

An initially tempting shortcut was to infer \([A,V]=0\) merely because
\(A\) is a good constant direction. That inference is invalid.
The certified commuting fields are the first commutators of the good
partials, not those partials themselves. Jacobi only gives
\[
4[B_0,V]+s[A,V]+A(s)V=0.
\]
The proof above never drops the middle term. It obtains \(A(s)=0\)
from the stronger identity \(D_0(s)=0\) and the polynomial argument.

Seven inline exact SymPy assertions passed using
\(/opt/anaconda3/bin/python\). The positive reduction control was
\[
s=z^2+w,\qquad
D_0=4\partial_b+s\partial_a,\qquad
E=\partial_w+(b/4)\partial_a.
\]
The assertions checked \(E(s)=1\), \(D_0(s)=0\), commutation,
niceness, the explicit coordinate map and inverse in (11), and survival
of the good \(\partial_a\). This control tests the reduction only; it
does not satisfy the full nonzero-top hypotheses, since its fourth
iterate vanishes. The negative control
\(4\partial_b+a\partial_a\) has the coordinate slice \(b/4\) but is
not locally nilpotent: every positive iterate on \(a\) equals \(a\).
The calculation checked its first eight iterates. Those original
inline checks have since been supplemented by the independent
[mixed-height suite](mixed_height_checks.py); current counts and
commands are in [verification-pass-13.json](../verification-pass-13.json).
