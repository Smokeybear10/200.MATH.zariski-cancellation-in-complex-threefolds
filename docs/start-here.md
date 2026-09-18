# Start with points and formulas

[Home](../README.md) · [Current status](current-status.md) · [Review guide](review-guide.md)

## 1. What is ordinary three-dimensional space?

It is the collection of points you can label with three independently
chosen numbers, such as **(2, 3, 1)**. Think left/right, forward/back,
and up/down. The labels are called coordinates.

"Independent" means that no equation forces one coordinate to depend on
the others. You can choose x, y, and z freely. A number line uses one
coordinate; a plane uses two; ordinary three-dimensional space uses three.

This is a real-number picture to introduce the idea. The actual research
uses complex numbers, but the idea of independent coordinates is the same.

## 2. What is a polynomial formula?

Examples are `x + y`, `x² + 3y + 1`, and `2xy - z³`.
You combine constants and variables using addition, subtraction,
multiplication, and nonnegative whole-number powers. Dividing by a
variable, taking its square root, or applying sine does not give a
polynomial formula. Fractions as coefficients, such as `x²/2`, are allowed.

## 3. How can different formulas describe the same space?

Relabel each point using this rule:

```text
Old label: (x, y, z)
New label: (x, y + x², z)

(2, 3, 1) becomes (2, 7, 1).
```

Nothing has been lost. To recover the old label, subtract the square
of the first number from the second:

```text
(u, v, w) becomes (u, v - u², w).

(2, 7, 1) becomes (2, 3, 1).
```

Both directions use polynomial formulas. This is a polynomial change of
coordinates: different labels for the same algebraic space.

Another example is the parabola `y = x²`. Its points are `(t, t²)`.
They look like a curved line in the plane, but one freely chosen number
t describes every point, and reading the first coordinate recovers t.
So a complicated-looking description need not mean a different algebraic
space.

## 4. What is the research question?

Start with an unknown algebraic space, called X. Give each point one
extra, completely independent coordinate. Suppose this larger space can
be described exactly as ordinary four-dimensional coordinate space.

Must X itself have been ordinary three-dimensional coordinate space?

That is the working cancellation question in this project. Formally:

$$
X\times\mathbb A^1_{\mathbb C}\cong\mathbb A^4_{\mathbb C}
\quad\Longrightarrow\quad X\cong\mathbb A^3_{\mathbb C}.
$$

Here a dimension means a **complex algebraic dimension**. Three complex
coordinates correspond to six real dimensions, so a physical 3D picture
is only an analogy.

The allowed changes of coordinates must be algebraic, with algebraic
inverses. In the affine setting we work with polynomial formulas. A
picture that looks the same, a numerical match, or a reversible continuous
deformation does not establish the required equivalence.

### Why not just remove the extra coordinate?

Because its identity may be hidden by complicated polynomial formulas.
Calling a polynomial "the fourth coordinate" does not prove that three
other polynomials complete it to an invertible coordinate system.

The ring version asks whether

$$
A[t]\cong\mathbb C[x_1,x_2,x_3,x_4]
\quad\Longrightarrow\quad A\cong\mathbb C[u,v,w].
$$

The ring A records polynomial functions on the unknown space. Adding t
means adjoining one genuinely independent variable. The challenge is to
recover a polynomial coordinate system for A, not merely to rename t.

## 5. What does the latest result actually say?

Think of a translation as a clean sliding motion along a number line.
A vector field describes a possible direction of motion at each point.
Not every polynomial vector field generates a polynomial translation.

Note703 proves a conditional statement. In its precise retraction setup,
if one nonzero vector field commutes with **all the raw projected
coordinate directions**, then it generates a polynomial additive action
and has a slice. That slice separates a genuine independent coordinate
from the rest of the ring.

The word "if" matters. We have not shown that a suitable nonzero field
can always be found. The note also gives a polynomial example where no
nonzero field meets that condition in the supplied frame.

Note702 examines another direct way of extracting a useful field. In its
specific example, changing the slice by any polynomial, taking constant
combinations of the ambient directions, and removing common factors still
does not make that method work. A nonlinear combination does work there.

These are results about sufficient conditions and failed methods. They
neither solve nor disprove the general cancellation question.

<details>
<summary>Definitions of words used in the proof notes</summary>

| Term | Meaning in these notes |
| --- | --- |
| Affine space | Ordinary algebraic coordinate space with independent coordinates. |
| Cylinder | X with an additional independent coordinate, written X times the affine line. |
| Coordinate frame | A collection of coordinates giving an actual polynomial description with an inverse. |
| Derivation / vector field | An algebraic rule for infinitesimal change, obeying the product rule. |
| Locally nilpotent derivation (LND) | Repeated application eventually kills each polynomial, possibly after different numbers of applications. It generates a polynomial additive action. |
| Slice | A polynomial v with D(v)=1 for an LND D. It supplies a translation coordinate. |
| Commuting fields | Fields whose algebraic commutator is zero; their infinitesimal operations are order-independent. |
| Retraction | An algebra map back onto a subring that leaves that subring unchanged. |

</details>

## How much confidence should a reader place in this?

The latest notes have complete written arguments, separate AI reviews,
and supporting exact symbolic checks. Those checks are useful, but they
are not human peer review or proof-assistant verification. Novelty has
not been established. GitHub preserves the work; it does not certify it.

For the exact assumptions and evidence, continue to [current status](current-status.md).
For the initial explanation with sources and elementary proofs, see
[the first investigation](../research-note.md), especially Sections 2–4.
