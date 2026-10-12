# Note 16

## Objects and classes

*Every* value in Python is an *object*. For example, the int `5` and the string
`'hello'` are objects.

Every object is an *instance* of some *class* (also known as a type). Evaluating
`type(5)` and `type('hello')` will return `<class 'int'>` and `<class 'str'>`,
respectively.

Programming languages cannot foresee all the kinds of program you might wish to
write. In particular, they cannot foresee all the types you might wish to use in
your programs. This observation is why most programming language provides ways
to extend its functionality and in particular a means to create your own types.

What does it takes to create a new data type in Python? To answer this question,
let us consider a data type modeling a body in classical mechanics using
Newton's law. This law stipulates that the gravitational potential at a point
due to a given body of mass $m$ at distance $r$ is given by $V = -G m/r$, where
$G$ is the universal gravitational constant
($6.67430 \times 10^{-11} \text{m}^3\text{kg}^{-1}\text{s}^{-2}$).

Here is a draft of a class called `Body` modeling a body in a two-dimensional
plane:

```python
import math

class Body:
    """Captures a body's mass and position in a two-dimensional plane.

    Attributes:
    * mass (float): The body's mass in kilograms (kg)
    * rx (float): The body's position on the x axis in meters (m)
    * ry (float): The body's position on the y axis in meters (m)
    """

    def __init__(self, mass : float, x0 : float, y0 : float) -> None:
        self.m = mass
        self.rx = x0
        self.ry = y0

    def potential_at(self, x : float, y : float):
        """Computes the potential at position (x, y) exerted by *this* body."""
        G = 6.67430e-11
        dx = x - self.rx
        dy = y - self.ry
        r = math.sqrt(dx**2 + dy**2)
        return G*self.m/r
```

With this definition, we are now in position to create many *instances* (or
*objects*) of this class (or type) as follows:

```python
earth = Body(5.972e14, 0., 0.)
moon = Body(7.348e22, 384400., 0.)
```

By convention, class names start with upper-case letters. `self.m`, `self.rx`,
and `self.ry` are *attributes* of the class. `__init__` and `potential_at` are
*methods* associated with the class. Methods always take at least one argument,
conventionally called `self`, that refers to the current instance being acted
upon. `__init__` is a special method often referred to as an initializer. It
describes how one instance (or object) of the class is to be initialized.

To create an instance of a class, one simply uses the class' name followed by
the required parameters enclosed in a pair of parentheses. The parentheses are
mandatory, even if the creation of an object does not require any parameters.
