import random
from math import gcd

class Elgamal:
    def __init__(self, g, p):
        self.g = g
        self.p = p
        self.generate_keys()

    def generate_keys(self):
        self.prkey = random.randint(2, self.p - 2)
        self.pukey = pow(self.g, self.prkey, self.p)

    def sign(self, message):
        while True:
            k = random.randint(2, self.p - 2)
            if gcd(k, self.p - 1) == 1:
                break
        r = pow(self.g, k, self.p)
        k_inv = pow(k, -1, self.p - 1)
        s = (k_inv * (message - self.prkey * r)) % (self.p - 1)
        return (r, s)

    def verify(self, signature, message):
        r, s = signature
        v1 = (pow(self.pukey, r, self.p) * pow(r, s, self.p)) % self.p
        v2 = pow(self.g, message, self.p)
        return v1 == v2

# Example usage
g = 2
p = 467
el = Elgamal(g, p)
signature = el.sign(15)
print("Signature:", signature)
print("Verification:", el.verify(signature, 15))
