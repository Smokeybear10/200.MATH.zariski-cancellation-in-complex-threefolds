# Tensor agreement and the missing descent hypotheses

The universal generator pencil gives a nilpotent difference on a
tensor square. This has an established relative weak-normalization
interpretation, but it does not supply either integrality or descent
to the coefficient ring. Those are separate mathematical obligations.

## 1. The exact consequence in the present notation

Let R be a characteristic-zero domain, A=R[c] a domain, and h in A.
The [pencil lemma](universal-generator-pencil-pass88.md) proves
\[
A[\tau]=R[\tau,c+\tau h]
\quad\Longrightarrow\quad
h\in A\cap\operatorname{Frac}(R),\qquad
h\otimes_R1-1\otimes_Rh\in\sqrt{(0)}\subset A\otimes_R A.
\tag{1}
\]
The proof works on the whole tensor square, including its zero
divisors. It does not identify the two images before reduction.

For the actual complex-algebra application and its chain C to R
to A, write
\[
\Delta(a)=a\otimes_{\mathbb C}1-1\otimes_{\mathbb C}a,
\qquad
\varphi:A\otimes_{\mathbb C}A\longrightarrow A\otimes_R A.
\tag{2}
\]
The second assertion in (1) says exactly that Delta(h) belongs
to the radical of ker(phi). Thus h belongs to the relative
C-weak normalization of R in A as defined by da Silva, Definition
1.5. That definition permits general ring morphisms. Membership
in the set it defines is not an assertion that h is integral over
R, or that the set equals R.[^relative]

By contrast, the classical relative weak normalization and weakly
subintegral extensions in Vitulli, Definitions 3.3 and 3.4, have
an integral extension as an explicit premise. Her Definition 3.7
likewise formulates relative weak normality under that premise.
They cannot be applied here by silently treating a generically
algebraic extension as an integral one.[^classical]

## 2. Two distinct failed implications

In the [cusp control](universal-generator-pencil-pass88.md),
R=C[v squared,v to the fifth], A=C[v], and h=v cubed. The
difference in (1) is nonzero but square-zero. Thus reduction of
the tensor square loses information relevant to exact descent.

In the [Laurent control](nonintegral-generator-pencil-control-pass88.md),
R=C[v squared,v cubed], A=C[v,v inverse], and h=v inverse.
Here A is a localization of R, so its tensor square over R is A
itself and the two images of h agree exactly. Nevertheless h is
not integral over R. The proper ideal (v squared,v cubed)
becomes the unit ideal, so the localization is not faithfully flat.
This is also consistent with da Silva's Example 1.18, which treats
localizations as radicial morphisms, without claiming they are
integral.[^relative]

The [polynomial-ring control](normal-generator-pencil-coordinate-boundary-pass88.md)
is stronger: S=C[a,t], R=S[a squared times c], A=S[c], h=ac.
It satisfies the pencil, with both R and A normal polynomial
three-rings and S to A faithfully flat, but h is not integral over
R. It even has an actual sliced four-dimensional cylinder and
the required constant-acceleration algebra identities. Its proposed
z fails to be an ambient coordinate, as a nonconstant unit on its
zero fiber proves. This identifies a specific missing geometric
hypothesis, not a counterexample to cancellation.

## 3. The usable conditional implications

If R is integrally closed in its fraction field and h has
independently been proved integral over R, the first assertion
of (1) does imply h in R. Normality without integrality does not.

Alternatively, if R to A is faithfully flat and the two images
of h agree in the unreduced tensor square, ordinary faithfully
flat descent gives h in R. A nilpotent difference is not exact
agreement. In the actual invariant-plane construction it is the
different extension S to A that has been proved faithfully flat;
that property cannot be reassigned to R to A.

The remaining task is therefore geometric: exploit the original
four-coordinate presentation or establish a genuine additional
descent premise. Renaming (1) as a relative weak-normalization
condition does not discharge that task.

## Sources

[^relative]: Thiago da Silva, [*The contraction property on the relative weak normalization and Lipschitz saturation of algebras*](https://arxiv.org/html/2410.18942v7), arXiv:2410.18942v7, March 25, 2025. Introduction, Definition 1.5 and Example 1.18. The versioned text distinguishes the radical in weak normalization from the integral closure of an ideal in Lipschitz saturation. Only these definitions and the localization example are used here, not the paper's contraction theorems.

[^classical]: Marie A. Vitulli, [*Weak Normality and Seminormality*](https://pages.uoregon.edu/vitulli/WeakAndSeminormality.pdf), Section 3.1, Definitions 3.3, 3.4 and 3.7, displayed pages 19--20. Author-hosted survey, also [arXiv:0906.3334](https://arxiv.org/abs/0906.3334). The cited definitions were checked for their integrality hypotheses; this is not a reconstruction of all historical weak-normalization theorems.
