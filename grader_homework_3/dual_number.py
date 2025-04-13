import numpy as np

class Dual:
    def __init__(self, real, dual=0.0):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real + other.real, self.dual + other.dual)
        else:
            return Dual(self.real + other, self.dual)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real - other.real, self.dual - other.dual)
        else:
            return Dual(self.real - other, self.dual)

    def __rsub__(self, other):
        return Dual(other - self.real, -self.dual)

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.real * other.real,
                        self.real * other.dual + self.dual * other.real)
        else:
            return Dual(self.real * other, self.dual * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Dual):
            real = self.real / other.real
            dual = (self.dual * other.real - self.real * other.dual) / (other.real ** 2)
            return Dual(real, dual)
        else:
            return Dual(self.real / other, self.dual / other)

    def __rtruediv__(self, other):
        return Dual(other, 0) / self

    def __pow__(self, power):
        if isinstance(power, Dual):
            raise NotImplementedError("Dual exponent not supported")
        real = self.real ** power
        dual = power * (self.real ** (power - 1)) * self.dual
        return Dual(real, dual)

    def __neg__(self):
        return Dual(-self.real, -self.dual)

# Math functions
def sin(x):
    if isinstance(x, Dual):
        return Dual(np.sin(x.real), x.dual * np.cos(x.real))
    return np.sin(x)

def cos(x):
    if isinstance(x, Dual):
        return Dual(np.cos(x.real), -x.dual * np.sin(x.real))
    return np.cos(x)

def exp(x):
    if isinstance(x, Dual):
        real = np.exp(x.real)
        return Dual(real, x.dual * real)
    return np.exp(x)

def log(x):
    if isinstance(x, Dual):
        return Dual(np.log(x.real), x.dual / x.real)
    return np.log(x)
