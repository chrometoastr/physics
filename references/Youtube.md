# Youtube Video References

## Table of Contents

- [eigenchris](#eigenchris)
  - [Playlist: Tensor Calculus](#playlist-tensor-calculus)
    - [Tensor Calculus 0](#tensor-calculus-0)
- [Faculty of Kahn](#faculty-of-kahn)
  - [Playlist: Tensor Calculus](#playlist-tensor-calculus-1)
    - [Introducing Dual Vectors: Intuition and Definition](#introducing-dual-vectors-intuition-and-definition)
    - [The Metric Tensor: Introduction and Examples](#the-metric-tensor-introduction-and-examples)

## eigenchris

### Playlist: [Tensor Calculus](https://www.youtube.com/playlist?list=PLJHszsWbB6hpk5h8lSfBkVrpjsqvUGTCx)

#### [Tensor Calculus 0]()

This introduction video kicks off a series on tensor calculus, defined as the study of how tensors change over space (0:17). Before diving into the calculus, the video reviews basic tensor algebra (0:24), covering different types of tensors such as vectors (arrows), covectors (stacks), linear maps (spatial transforms), and the metric tensor (measuring lengths and angles) (0:32).

The video explains that since the same tensor can have different components in different coordinate systems, we use forward and backward transforms to convert between them (2:27).

Tensor calculus extends these concepts to tensor fields—infinite collections of tensors that change at every point in space (3:52). This includes:

- Scalar fields (like temperature or voltage) (4:12)
- Vector fields (like electric or gravitational fields) (4:33)
- Covector fields (differential forms) (5:10)
- Metric tensor fields (crucial for map projections or distorted space) (5:24)

Applications of Tensor Calculus:

- Electromagnetism: Combining electric and magnetic fields into a single Faraday tensor to simplify Maxwell's equations (6:52).
- Continuum Mechanics: Using the Cauchy stress tensor to study deformations and internal stresses in materials (7:29).
- General Relativity: Utilizing various tensor fields to describe how mass and energy curve space-time, creating gravity (8:24).

Prerequisites for the series:

- Multivariable Calculus: Partial derivatives, gradients, and line integrals (9:53).
- Linear Algebra: Vectors, linear combinations, and matrix multiplication (10:30).
- Tensor Algebra: Specifically, understanding coordinate transforms, which the creator provides in a previous series, Tensors for Beginners (10:41).

The series aims to clarify the reinterpretation of mathematical symbols used in calculus when applied to tensors (11:45).

## [Faculty of Kahn](https://www.youtube.com/@FacultyofKhan)

### Playlist: [Tensor Calculus](https://www.youtube.com/playlist?list=PLdgVBOaXkb9D6zw47gsrtE5XqLeRPh27_)

#### [Introduction to Tensors (#1)](https://www.youtube.com/watch?v=uaQeXi4E7gA&list=PLdgVBOaXkb9D6zw47gsrtE5XqLeRPh27_&index=1)

This video by the *Faculty of Khan* serves as an introductory conceptual guide to **tensors**, explaining them through the lens of physics and geometry. The video defines a tensor as a mathematical object that requires a certain number of **basis vectors** to specify its components in an M-dimensional space.

**Key concepts covered:**

- **Scalars (Rank 0 Tensors):** (0:00 - 0:49) A scalar, such as temperature, has magnitude but no direction, requiring zero basis vectors to define it. It has M to the power of 0 (1) component.
- **Vectors (Rank 1 Tensors):** (0:50 - 2:54) A vector, such as displacement, has both magnitude and direction. It requires one basis vector per component and has M to the power of 1 (3) components in 3D space.
- **Rank 2 Tensors (Stress Tensor):** (2:55 - 7:13) Using the example of a steel beam under stress, the creator explains that to specify force per unit area at a point, you need two basis vectors: one for the orientation of the surface and one for the direction of the force. This results in 9 components in 3D (3 squared).
- **Defining Tensors:** (7:14 - 9:49) The video formalizes the definition, noting that a tensor of rank n has n indices, M to the power of n components, and adheres to specific transformation rules. The creator clarifies that while matrices are used to represent rank-2 tensors, they are not identical, as tensors possess deeper physical significance and transformation properties.
- **Rank 3 Tensors:** (9:50 - 10:32) Briefly introduced as objects that can be represented by 3D arrays, requiring three basis vectors per component and having 3 to the power of 3 (27) components.


#### [Introducing Dual Vectors: Intuition and Definition (#10)](https://m.youtube.com/watch?v=wZ2G-b-Ttww&pp=0gcJCcUKAYcqIYzv)

This video introduces dual vectors (also known as covectors or one-forms) in the context of tensor analysis, defining them not just as arrows, but as functions that operate on regular vectors to produce a real number (0:24-0:44).

Key Concepts & Intuition:

- Definition as a Function: A dual vector is a linear function that takes a vector as input and spits out a scalar (0:42-1:45).
- Tensor Analysis Context: In this field, a dual vector acts on a contravariant vector to return an inner product (3:57-4:17).
- Geometric Interpretation: Geometrically, a dual vector can be visualized as a set of parallel lines or surfaces. The value of the function is determined by how many of these lines a regular vector crosses from its start to its end (5:53-7:55).
- The Gradient: The gradient of a function is a prime example of a dual vector, representing how fast a function changes in the direction of a vector (8:09-8:56).
- Ultimately, the video concludes that a dual vector is a covariant vector, defined by components that transform according to the covariant transformation law (9:42-10:02).

#### [Dual Basis Vectors (#12)](https://www.youtube.com/watch?v=-ceIPtjAe5c&list=PLdgVBOaXkb9D6zw47gsrtE5XqLeRPh27_&index=12)

This video from the *Faculty of Khan* provides an introduction to the concept of **dual basis vectors** within the framework of tensor calculus. The explanation focuses on how these vectors relate to regular basis vectors and their practical utility in tensor analysis.

**Key concepts covered in the video:**

- **Defining the Dual Basis:** The video explains that just as a regular vector *V* can be expressed as a linear combination of basis vectors (e sub i), a dual vector can be expressed using a set of dual basis vectors (e super j) (0:05-1:20).
- **The Mathematical Definition:** The dual basis is defined by the property that when a dual basis vector (e super j) operates on a regular basis vector (e sub i), the result is the **Kronecker delta**. This means the result is 1 if the indices match and 0 if they differ (4:26-5:30).
- **Projection of Components:** One of the primary applications of dual basis vectors is their ability to isolate or "project out" specific components of contravariant vectors (6:03-6:43).
- **Relationship to Metric Tensors:** The video concludes by demonstrating that the **inverse metric tensor** (G super KI) can be defined as the inner product of dual basis vectors, contrasting with the regular metric tensor (G sub iJ), which is the inner product of regular basis vectors (7:21-7:45).

#### [The Metric Tensor: Introduction and Examples (#16)](https://www.youtube.com/watch?v=8HZdnOmsJlg&list=PLdgVBOaXkb9D6zw47gsrtE5XqLeRPh27_&index=16)

This video provides an introduction to the metric tensor, a fundamental concept in tensor calculus and physics used to calculate arc lengths and define geometry in various coordinate systems. The presenter explains that the metric tensor essentially acts as a modifier for distance in different spaces.

Here are the key takeaways:

- Arc Length in Cartesian Coordinates: (0:07 - 1:09) The video starts by deriving the arc length formula in rectangular coordinates using the Pythagorean theorem, treating an infinitesimal segment DS as the hypotenuse of a triangle formed by DX and DY.
- Arc Length in Polar Coordinates: (1:10 - 2:14) The concept is extended to polar coordinates, where the arc length element is sqrt(DR^2 + (R DTheta)^2), highlighting how the coordinate system affects distance calculations.
- Introduction to the Metric Tensor: (2:15 - 5:23) The presenter generalizes these concepts into $N$-dimensions. The metric tensor, denoted by components $G_{ij}$, is introduced as the coefficient that accounts for how coordinate differentials ($DX^i$, $DX^j$) contribute to the total distance $DS$. It is crucial for calculating distances, angles, and volumes in curved spaces.
- Examples of Metric Tensors:
  - Cartesian: (5:40 - 8:16) In 3D Cartesian coordinates, the metric tensor is equivalent to the identity matrix (ones on the diagonal, zeros elsewhere).
  - Cylindrical: (8:17 - 9:55) For cylindrical coordinates, the metric tensor components reflect the radial distance dependence ($R^2$ in the angular component).
  - Spherical: (9:56 - 11:15) The metric tensor for spherical coordinates is also derived, showing its components based on distance from the origin and angular positions.
- Conclusion: (11:16 - 11:48) The video concludes by reinforcing that the metric tensor defines the geometric properties of a space.

## [Dialect](https://www.youtube.com/@dialectphilosophy)

### Playlist: [Differential Geometry](https://www.youtube.com/playlist?list=PL__fY7tXwodm9pFqWGrkjIvJMOedSYIti)

#### [Conceptualizing the Christoffel Symbols: An Adventure in Curvilinear Coordinates](https://www.youtube.com/watch?v=TvFvL_sMg4g&list=PL__fY7tXwodm9pFqWGrkjIvJMOedSYIti&index=1)

This video from Dialect offers an intuitive exploration into the mathematical machinery of General Relativity by conceptualizing the Christoffel Symbols using polar coordinates.

Key Takeaways and Highlights:

- Cartesian vs. Polar Land (0:54): The video uses an analogy of "Cartesian Land" (real space) versus "Polar Land" (a map projection) to explain how coordinates can misrepresent true distance and direction.
- The Metric Tensor (3:31): Introduced as a "bar scale" for basis vectors, the metric tensor tells us how much real-world distance corresponds to coordinate distances at any given point. It reveals that the Theta ruler grows in length as you move further from the origin.
- The Levi-Civita Connection (10:16): This concept explains how to properly fit together infantesimal pieces of a manifold. It relates the rate of change of one basis vector along a direction to the change of another basis vector along a different direction, highlighting how growing or shrinking in one dimension requires curving into another.
- Calculating Christoffel Symbols (14:15): The video explicitly calculates the eight Christoffel symbols for polar coordinates, illustrating precisely how the real-world basis vectors ($ER$ and $ETheta$) change as they are transported across different coordinate directions.
- Polar Geodesics (21:14): Armed with these symbols, the video explains how to calculate the straightest possible paths, or geodesics, through curved space-time.

#### [An Introduction to Curvilinear Coordinates in Differential Geometry](https://www.youtube.com/watch?v=2V__naEkXVY&list=PL__fY7tXwodm9pFqWGrkjIvJMOedSYIti&index=2)

This video from Dialect provides an introduction to curvilinear coordinates, explaining how they are used to describe surfaces and why they are essential for understanding the mathematics of General Relativity (0:00). Unlike straight Cartesian grids, curvilinear coordinates map lines that represent constant values from a flat parametric space onto a curved surface or space (1:15).

Key Concepts Covered:

- Position Vectors & Mapping (2:42): Every point in the space is described by a vector reaching from an origin, with Cartesian components expressed as functions of parametric variables (like u and v).
- Basis Vectors (3:28): By taking partial derivatives of the position vector, the video defines basis vectors that act as velocity vectors for points moving along coordinate curves (5:37).
- Metric Tensor (7:53): The dot products of these basis vectors form the metric tensor, which allows us to calculate Euclidean distances and lengths within the parametric system (7:55).
- Coordinate Acceleration (8:00): Moving along coordinate curves causes the basis vectors to change. The rates of change of these vectors are categorized as coordinate acceleration.
- Christoffel Symbols (11:47): By decomposing these acceleration vectors into components of the parametric basis, the video derives the Christoffel symbols, which quantify how the basis vectors change relative to each other (12:09).
- Polar Coordinates Example (14:42): The concepts are applied to a 2D polar coordinate system to illustrate how these symbols relate to physical concepts like centripetal acceleration and coordinate flow (15:00).
- Geodesics (19:12): The video explains how Christoffel symbols help determine the paths that correspond to straight lines (geodesics) in a curved system (19:15).

#### [The Christoffel Symbols In Riemannian Geometry](https://www.youtube.com/watch?v=2992Bqfas_c&list=PL__fY7tXwodm9pFqWGrkjIvJMOedSYIti&index=3)

This video from Dialect provides a visceral, 3D animated exploration of the Christoffel Symbols in Riemannian Geometry, aiming to make abstract concepts concrete and physically intuitive for studies in differential geometry and General Relativity (0:00 - 0:50).

Key Concepts Covered:

- Physical Intuition (2:17 - 6:49): The video explains how basis vectors translate coordinate movements into actual distances on a manifold, and how Christoffel Symbols describe how these basis vectors change direction and magnitude across the curved surface.
- Curved Manifolds (6:49 - 13:17): When moving from flat to curved surfaces, basis vectors no longer lie entirely within the manifold. The video shows how to decompose changes in basis vectors into components tangent (within the surface) and normal (perpendicular) to the manifold.
- Intrinsic Method (14:49 - 27:04): To understand a surface without referring to an external 3D space, the Metric Tensor is introduced. The video derives the Christoffel formula using the metric tensor and the Levi-Civita connection, which ensures coordinate curves close properly.
- Example: The 2-Sphere (13:17 - 14:49, 27:04 - 31:20): The video applies these concepts to a unit sphere, showing how to calculate the specific Christoffel symbols from the metric, identifying it as a specific case of coordinate curvature.The video concludes by questioning how to distinguish between local flatness and global curvature, setting the stage for future discussions on parallel transport and intrinsic curvature (31:20 - 34:01).

#### [The Nature of Geodesics](https://www.youtube.com/watch?v=m6WY6VtPYrk&list=PL__fY7tXwodm9pFqWGrkjIvJMOedSYIti&index=4)

This video from Dialect explains the concept of geodesics—often defined as the "straightest possible path" on a surface—without relying on advanced mathematics. Instead, it uses intuitive, visual analogies to explain how paths are determined on curved surfaces.

Key Takeaways:

- Straightness Relative to the Surface (1:58): A geodesic isn't necessarily a straight line in 3D space, but rather a path that matches the curvature profile of the surface itself. If you were driving a car on the surface and didn't have to turn the steering wheel, you are driving on a geodesic (3:22).
- Local Flatness (4:37): A key concept in differential geometry is that any surface, no matter how curved, looks flat if you zoom in close enough (4:50). This allows us to judge if a path is straight relative to that tiny, flat area.
- Intrinsic vs. Extrinsic Curvature (7:13): The video distinguishes between shapes like a cone (purely extrinsic curvature, can be unwrapped flat) and a sphere (which has intrinsic curvature and cannot be flattened without distortion).
- Unwrapping and Refolding (10:55): To find a geodesic on a complex surface like a sphere, the video demonstrates approximating it with small, flat, polygonal pieces. By unwrapping and refolding adjacent pieces, you can determine the straightest possible path to continue moving forward (12:08).

The video concludes by setting up future topics, including the mathematical geodesic equation, parallel transport, and curvature tensors (13:08).

#### [Understanding Parallel Transport & Connections in Differential Geometry](https://www.youtube.com/watch?v=MRU2D6sLpU0&list=PL__fY7tXwodm9pFqWGrkjIvJMOedSYIti&index=5)

This video from Dialect provides an accessible introduction to the concepts of parallel transport and connections in differential geometry, bridging the gap between flat and curved spaces (0:00). It highlights these concepts as essential tools for understanding Riemannian curvature and general relativity (0:30).

Key concepts covered:

- Parallel Transport: Defined simply as moving a vector from one point to another while preserving its direction relative to a surface (0:55). On a flat surface, this is straightforward, but on curved surfaces, the vector must twist to remain parallel to the surface itself (1:57).
- The Riemannian Trick: To understand transport on a curved surface, the video explains how to project paths onto flat surfaces (e.g., using cylinders or cones) to make the geometry easier to visualize (3:43).
- Geodesics: Moving a vector along a geodesic (the shortest path between two points on a curved surface) is equivalent to moving it in a straight line on a flat surface, resulting in no twisting (6:38).
- The Levi-Civita Connection: This specific type of connection is introduced as one that is metric compatible (preserves lengths and angles) and torsion-free (preserves parallelism), forming the foundation of general relativity (9:36).
- Implications for Curvature: The mismatch that occurs when a vector is parallel transported along different paths to the same point is the key to measuring a surface's intrinsic curvature (14:15).

### Playlist: [The Metric Tensor]([https://www.youtube.com/playlist?list=PL__fY7tXwodmfntSAAyBDxZ4_eE3ZwbFE](https://www.youtube.com/playlist?list=PL__fY7tXwodmfntSAAyBDxZ4_eE3ZwbFE)

#### [Demystifying The Metric Tensor in General Relativity](https://www.youtube.com/watch?v=Hf-BxbtCg_A&list=PL__fY7tXwodmfntSAAyBDxZ4_eE3ZwbFE&index=1)

This video demystifies the **metric tensor**, a fundamental concept in *General Relativity*, by using a familiar analogy: a **bar scale** on a topographical map.

Here are the key takeaways:

- **The Metric as a Bar Scale:** Just as a map uses a scale to convert map distances to real-world distances, the metric tensor does this for space-time, accounting for how matter and energy warp it (0:54-2:04).
- **Topography and Stretching:** In hilly terrain, a flat map scale is inaccurate. Similarly, the metric must adjust based on local curvature. The video explains how topographic contour lines map to real-world vertical distances, illustrating that the metric is not constant but varies across space (2:05-4:53).
- **The Components of the Tensor:** In two dimensions, you need three numbers to map a surface accurately: how much the *x-axis* is stretched, how much the *y-axis* is stretched, and the **angle of skew** between them. For 4D space-time, this generalizes to **ten components** (5:35-8:50, 11:37-12:13).
- **Manifolds vs. Coordinates:** The video distinguishes between the physical *manifold* (the actual space) and the *coordinate system* (the map used to measure it) (12:37-13:38).

#### [The Meaning of the Metric Tensor](https://www.youtube.com/watch?app=desktop&v=Dn0ZZRVuJcU)

This video from *Dialect* explains the **metric tensor** as the crucial, yet often misunderstood, mathematical foundation of **General Relativity**. The core concept presented is that physicists are essentially **spacetime cartographers** (1:18), making a map of a curved 4D universe on a flat, 4D coordinate system.

Here are the key takeaways:

- **The Metric as a Bar Scale:** A metric tensor acts as a **bar scale** (4:09) at every single point on a map. It translates **coordinate distances** on the map to **proper distances** (true physical distances) on the real, curved manifold (4:15).
- **Spacetime Interval:** Unlike a regular map, this metric deals with the **spacetime interval** (6:12). It tells us how fast or slow **clocks are ticking** (6:35) across the universe relative to a local reference clock, accounting for both spatial stretching and time dilation.
- **The 10 Numbers (Tensor):** To separate information about how space and time change across the map, we need more thanone number. The **metric tensor** requires **10 numbers** (7:06) at each point to account for stretching, shrinking, and **skewing** (angle changes) of the coordinate grid (8:22).
- **Dimensional Examples:** The video illustrates this process using a **2D map of Earth** (8:39), demonstrating how latitude and longitude require shrinking near the poles (10:25). It then expands this concept to a **3D metric** (13:58), where tiny, distorted cubes are used to measure the properties of a 3D space.

#### [The Spacetime Metric](https://www.youtube.com/watch?app=desktop&v=neiJ1SLMrfM&list=PL__fY7tXwodmfntSAAyBDxZ4_eE3ZwbFE&index=3)

This video, the final part of a trilogy, explains how the **metric tensor** is used to accurately describe distances and angles in **four-dimensional spacetime** for General Relativity. It bridges the gap between intuitive 3D geometry and the abstract geometry required to understand gravitational physics.

##### Key Concepts

- **The Map Analogy (0:00 - 3:56):** To describe distance on a skewed or curved surface (like a map of the *Earth*), you need more than just coordinate differences (dx, dy). You need a **metric tensor** to act as a sophisticated scale to calculate true surface distances and angles.
- **Spacetime Maps (4:28 - 7:13):** In physics, we create **spacetime maps** to order **world events**. However, these maps are often projections that don't match the true, curved geometry of spacetime caused by gravity.
- **Formulating the Metric (9:07 - 11:57):** The metric tensor allows us to translate flat map coordinates into true local distances. For a 4D spacetime map, this requires **10 unique numbers** to account for all possible stretching (lengths) and skewing (angles) of the coordinate axes.
- **Interpreting the Components (13:57 - 16:11):**
  - **Diagonal components** of the tensor represent how much coordinate lengths (like time or distance) need to be resized.
  - **Off-diagonal components** represent how much the angles between coordinate axes are skewed from orthogonality.
- **The Spacetime Metric (16:11 - 18:22):** Unlike physical space, the spacetime interval formula involves a **negative sign** (hyperbolic geometry), reflecting that one dimension (time) behaves differently than the others.

##### Conclusion

The **metric tensor** allows observers to calculate the true spacetime distance between events, even if they are far away from the events being measured. Analyzing how this metric changes across a map reveals the underlying nature of spacetime curvature.