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

    return random.choice(prime_list)

def smallestGGT(a,b):
    while b!=0:
        c=a%b
        a=b
        b=c
    print("GGT is: "+str(a))
    if(a==1):
        return True
    else:
        return False

    
p = primesInRange(1,2500)
q = primesInRange(1,2500)


N = p * q       # public
print("N: " + str(N))

phi_N = (p-1) * (q-1)
print("Phi_N: " + str(phi_N))

e = random.randint(1,phi_N)     # public

while (smallestGGT(e,phi_N) ==False):
    e = random.randint(1,phi_N)

# smallest ggt of e and phi_N should be 1
# print( smallestGGT(e,phi_N)) 

d*e = 1 % phi_N            # private