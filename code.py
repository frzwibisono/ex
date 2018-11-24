#/usr/lib/python
import random
import string
base = "811"
berapa = int(raw_input("Mw brp?: "))
def gene(size=9,
chars=string.digits):
        return ''.join(random.choice(chars)
for _ in range(size))
for i in range(berapa):
        print base+gene()
