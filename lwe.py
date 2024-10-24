import random

# Please make sure to read below
# The noise added to the public key (b) is generated from a uniform distribution within a limited range defined by error_bound. 
# Since the noise is not derived from robust sources, decryption will fail to give correct output sometimes.
# Thus keep in mind that you will not always get correct output
# However, lowering the error bound will increase your chance of getting correct decrypted output. (But it will reduce the security)
# Even if you keep error bound as 1 you will sometimes get wrong decrypted output. So i think best to keep it at 5

# Parameters for lattice-based encryption
n = 10          # Dimension of lattice (small for simplicity)
q = 97          # A small prime modulus (usually larger in real systems)
error_bound = 5 # Error bound for "noise" added to the ciphertext (small for simplicity)

def get_random_int(mod):
    return random.randint(0, mod - 1)

# Helper function to generate a random vector
def get_random_vector(size, mod):
    return [get_random_int(mod) for _ in range(size)]

# Function to compute the dot product of two vectors
def dot_product(a, b, mod):
    product = 0
    for i in range(len(a)):
        product = (product + a[i] * b[i]) % mod
    return product

# Function to generate a private key (secret vector s) and a public key (matrix A, vector b)
def key_generation():
    # Generate a random secret vector s
    s = get_random_vector(n, q)

    # Generate a random matrix A
    A = [get_random_vector(n, q) for _ in range(n)]

    # Generate the public key vector b = A * s + noise
    b = []
    for i in range(n):
        noise = get_random_int(error_bound)  # Small random noise
        b.append((dot_product(A[i], s, q) + noise) % q)

    return A, s, b

# Function to encrypt a bit message (0 or 1)
def encrypt(message, A, b):
    # Generate a random vector e (encryption randomness)
    e = get_random_vector(n, 2)  # Binary vector e

    # Compute the ciphertext (c1 = A * e mod q)
    c1 = [dot_product(A[i], e, q) for i in range(n)]
    c2 = (dot_product(b, e, q) + message * (q // 2)) % q

    return c1, c2

# Function to decrypt the ciphertext
def decrypt(ciphertext, s):
    c1, c2 = ciphertext

    # Decrypt the message using c2 - c1 * s
    inner_product = dot_product(c1, s, q)
    decrypted_value = (c2 - inner_product + q) % q

    # If the decrypted value is closer to q/2, the original message was 1, otherwise it was 0
    if decrypted_value > q // 4 and decrypted_value < 3 * q // 4:
        return 1
    else:
        return 0

# Main execution
if __name__ == "__main__":
    # Step 1: Key Generation
    A, s, b = key_generation()

    # Display the keys
    print("Private key (s):", s)
    print("Public key (A and b):")
    print("Matrix A:")
    for row in A:
        print(row)
    print("Vector b:", b)

    # Step 2: Encryption
    message = int(input("Enter a bit message to encrypt (0 or 1): "))
    ciphertext = encrypt(message, A, b)

    # Display the ciphertext
    print("Ciphertext (c1, c2):")
    print("c1:", ciphertext[0])
    print("c2:", ciphertext[1])

    # Step 3: Decryption
    decrypted_message = decrypt(ciphertext, s)
    print("Decrypted message:", decrypted_message)