import random

def is_prime(num):
    if num<2:
        return False
    for i in range(2,round(num**(0.5))):
        if num%i == 0:
            return False
    return True

def generation_prime(lower,upper):
    while True:
        num=random.randint(lower,upper)
        if is_prime(num):
            return num

def key_gen():
    n=2
    k=2
    G = [[generation_prime(2,20) for i in range(k)] for j in range(n)]
    S = [[generation_prime(2,20) for _ in range(n)] for _ in range(n)]
    P = [[generation_prime(2,20) for _ in range(k)] for _ in range(n)]
    return G,S,P

def is_invert(mat):
    a,b=mat[0]
    c,d=mat[1]
    det = a*d -b*c
    return det==0

def inverse(mat):
    a,b=mat[0]
    c,d=mat[1]
    det = a*d - b*c
    if det!=0:
        invere_mat = [[d/det,-b/det],[-c/det,a/det]]
        return invere_mat

def mat_multiply(A,B):
    result = [[0 for i in range(len(B[0])) ] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j]+=A[i][k]*B[k][j]
    return result

def encryption(message,G):
    message_vector = [[m] for m in message]
    cipher_text_vector = mat_multiply(G,message_vector)
    cipher_text= [m[0] for m in cipher_text_vector]
    return cipher_text

def decryption(cipher_text,G):
    G_in=inverse(G)
    cipher_text_vector=[[m] for m in cipher_text]
    plain_text_vector=mat_multiply(G_in,cipher_text_vector)
    plain_text=[i[0] for i in plain_text_vector]
    return plain_text

message=[18,9]
G,S,P=key_gen()
cipher_text=encryption(message,G)
print(cipher_text)
plain_text=decryption(cipher_text,G)
print(plain_text)
