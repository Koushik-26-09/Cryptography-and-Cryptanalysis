import random

def mod_inverse(a, b):
    # Using extended Euclidean algorithm to find the modular inverse
    a = a % b
    for i in range(1, b):
        if (a * i) % b == 1:
            return i
    return -1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elliptic:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, P):
        if P.x is None and P.y is None:
            return True  # Point at infinity
        return (P.y ** 2) % self.p == (P.x ** 3 + self.a * P.x + self.b) % self.p

    def add_two_points(self, P1, P2):
        if P1.x is None and P1.y is None:
            return P2
        if P2.x is None and P2.y is None:
            return P1

        if P1.x == P2.x and P1.y == P2.y:
            if P1.y == 0:
                return Point(None, None)  # Point at infinity
            m = (3 * P1.x ** 2 + self.a) * mod_inverse(2 * P1.y, self.p) % self.p
        else:
            if P1.x == P2.x:
                return Point(None, None)  # Point at infinity
            m = (P2.y - P1.y) * mod_inverse(P2.x - P1.x, self.p) % self.p

        x3 = (m ** 2 - P1.x - P2.x) % self.p
        y3 = (m * (P1.x - x3) - P1.y) % self.p

        return Point(x3, y3)

    def multiply(self, k, P):
        result = Point(None, None)  # Point at infinity
        addend = P

        while k:
            if k & 1:
                result = self.add_two_points(result, addend)
            addend = self.add_two_points(addend, addend)
            k >>= 1

        return result

class Ecc:
    def __init__(self, curve, G):
        self.curve = curve
        self.G = G
        self.private_key = random.randint(1, self.curve.p - 1)
        self.public_key = self.curve.multiply(self.private_key, self.G)

    def encryption(self, M):
        k = random.randint(1, self.curve.p - 1)
        c1 = self.curve.multiply(k, self.G)
        c2 = self.curve.add_two_points(M, self.curve.multiply(k, self.public_key))
        return c1, c2

    def decryption(self, c1, c2):
        s = self.curve.multiply(self.private_key, c1)
        # Subtract shared secret s from c2: Equivalent to adding the inverse of s
        M = self.curve.add_two_points(c2, Point(s.x, (-s.y) % self.curve.p))
        return M

# Example usage
a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
p = int(input("Enter the prime modulus p: "))

curve = Elliptic(a, b, p)
G = Point(3, 6)  # Example generator point

Ec = Ecc(curve, G)
p1, p2 = Ec.encryption(Point(112, 1))
print(f"Ciphertext: C1 = ({p1.x}, {p1.y}), C2 = ({p2.x}, {p2.y})")

m = Ec.decryption(p1, p2)
print(f"Decrypted message: M = ({m.x}, {m.y})")
