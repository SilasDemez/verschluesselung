import random

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)

    return prime_list

  



primes_list = primesInRange(1, 2500) #modulus        
p = random.choice(primes_list)
primes_list.pop()
g = random.choice(primes_list)

a=random.randint(1,p)   # secret random number that is smaller than p, in meantime small number
b=random.randint(1,p)   # secret random number that is smaller than p, in meantime small number

A=pow(g,a) % p
B=pow(g,b) % p

# exchange of A and B

k1 = pow(B,a) % p
k2 = pow(A,b) % p

# k1 = k2

print(k1,k2)