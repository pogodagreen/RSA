import random
import time


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def GCD(x, y):
    while y != 0:
        pom = y
        y = x % y
        x = pom
    return x


def isCoPrime(x, y):
    if GCD(x, y) == 1:
        return True
    return False


if __name__ == '__main__':
    start = time.time()
    p = random.randrange(1000, 10000)
    while not isPrime(p):
        p = random.randrange(1000, 10000)
    print ("p", p)
    q = random.randrange(1000, 10000)
    while not isPrime(q):
        q = random.randrange(1000, 10000)
    print ("q", q)
    n = p * q
    print("n", n)
    phi = (p - 1) * (q - 1)
    print("phi", phi)
    e = random.randrange(1, phi)
    while not isPrime(e) & isCoPrime(e, phi):
        e = random.randrange(1, phi)
    print ("e", e)
    d = 2
    for i in range(2, phi):
        if (e * i - 1) % phi == 0:
            d = i
    print ("d", d)
    end = time.time()
    print (end - start)
    start=time.time()
    m1 = "Confusion In HerEyesThatSaysItAllShe'sLostControl"
    print("Message: ",m1)
    c = []
    for a in m1:
        temp = 0
        temp = ord(a)
        temp = temp ** e % n
        c.append(temp)
    print ("Encrypted text: ", c)
    end = time.time()
    print (end - start)
    start=time.time()
    m2 = ""
    for a in c:
        temp = 0
        temp = a ** d % n
        m2 = m2 + chr(temp)
    print("Decrypted text: ", m2)
    end=time.time()
    print (end-start)
