# Base expression class and operator overloading
class Expr:
    def __call__(self, **context):
        raise NotImplementedError

    def d(self, wrt):
        raise NotImplementedError

    def __neg__(self):
        return Product(Const(-1), self)

    def __pos__(self):
        return self

    def _wrap(self, other):
        return other if isinstance(other, Expr) else Const(other)

    def __add__(self, other):
        return Sum(self, self._wrap(other))

    def __radd__(self, other):
        return Sum(self._wrap(other), self)

    def __sub__(self, other):
        return Sum(self, Product(Const(-1), self._wrap(other)))

    def __rsub__(self, other):
        return Sum(self._wrap(other), Product(Const(-1), self))

    def __mul__(self, other):
        return Product(self, self._wrap(other))

    def __rmul__(self, other):
        return Product(self._wrap(other), self)

    def __truediv__(self, other):
        return Fraction(self, self._wrap(other))

    def __rtruediv__(self, other):
        return Fraction(self._wrap(other), self)

    def __pow__(self, other):
        return Power(self, self._wrap(other))

    def __rpow__(self, other):
        return Power(self._wrap(other), self)


# Implement class for two types of expressions: Const – a constant and Var – a variable. For convinience next we will use not a constructors of classes but their one-letter synonyms
class Const(Expr):
    def __init__(self, value):
        self.value = value

    def __call__(self, **context):
        return self.value

    def d(self, wrt):
        return Const(0)

    def __str__(self):
        return str(self.value)


class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __call__(self, **context):
        return context[self.name]

    def d(self, wrt):
        return Const(1 if isinstance(wrt, Var) and wrt.name == self.name else 0)

    def __str__(self):
        return self.name


V = Var
C = Const


# Implement classes for binary operations: Sum, Product, and Fraction. Binary operations by definition work with exactly two operands
class BinOp(Expr):
    def __init__(self, expr1: Expr, expr2: Expr) -> None:
        self.expr1, self.expr2 = expr1, expr2


class Sum(BinOp):
    def __call__(self, **context):
        return self.expr1(**context) + self.expr2(**context)

    def d(self, wrt):
        return Sum(self.expr1.d(wrt), self.expr2.d(wrt))

    def __str__(self):
        return f"(+ {self.expr1} {self.expr2})"


class Product(BinOp):
    def __call__(self, **context):
        return self.expr1(**context) * self.expr2(**context)

    def d(self, wrt):
        return Sum(
            Product(self.expr1.d(wrt), self.expr2),
            Product(self.expr1, self.expr2.d(wrt)),
        )

    def __str__(self):
        return f"(* {self.expr1} {self.expr2})"


class Fraction(BinOp):
    def __call__(self, **context):
        return self.expr1(**context) / self.expr2(**context)

    def d(self, wrt):
        num = Sum(
            Product(self.expr1.d(wrt), self.expr2),
            Product(Const(-1), Product(self.expr1, self.expr2.d(wrt))),
        )
        den = Power(self.expr2, Const(2))
        return Fraction(num, den)

    def __str__(self):
        return f"(/ {self.expr1} {self.expr2})"


# Implement a class Power for an operation of an exponentiation operation
class Power(BinOp):
    def __call__(self, **context):
        return self.expr1(**context) ** self.expr2(**context)

    def d(self, wrt):
        exponent_value = self.expr2()
        return Product(
            Product(
                Const(exponent_value),
                Power(self.expr1, Const(exponent_value - 1)),
            ),
            self.expr1.d(wrt),
        )

    def __str__(self):
        return f"(** {self.expr1} {self.expr2})"
