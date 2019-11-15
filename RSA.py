import random


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def NWD(x, y):
    while y != 0:
        pom = y
        y = x % y
        x = pom
    return x


def isCoPrime(x, y):
    if NWD(x, y) == 1:
        return True
    return False


if __name__ == '__main__':
    p = random.randrange(1000, 10000)
    while not isPrime(p):
        p = random.randrange(1000, 10000)
    print (p)
    q = random.randrange(1000, 10000)
    while not isPrime(q):
        q = random.randrange(1000, 10000)
    print (q)
    n = p * q
    print(n)
    phi = (p - 1) * (q - 1)
    print(phi)
    e = random.randrange(1,phi)
    while not isPrime(e) & isCoPrime(e, phi):
        e = random.randrange(1,phi)
    print (e)
    d = random.randrange(1,phi)
    while ((e * d)-1) % phi != 0:
        d = random.randrange(1,phi)
    print (d)
    m1 = "Confusion In HerEyesThatSaysItAllShe'sLostControl"
    c = m1 ** e % n
    m2 = c ** d % n
    print ("Message: " + m1 + "\n" + "Encrypted text: " + c + "\n" + "Decrypted text: " + m2 + "\n")
