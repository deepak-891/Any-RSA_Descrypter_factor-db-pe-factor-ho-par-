from factordb.factordb import FactorDB
from Crypto.Util.number import getPrime, inverse, long_to_bytes
import binascii

n = "replace"
c="replace"
e='repalce'

f = FactorDB(n)
f.connect()
l =f.get_factor_list()
phi =1
for i in l:
    phi = phi * (i-1)


d = inverse( e, phi )

m = pow( c, d, n )
print(long_to_bytes(m))
