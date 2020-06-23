from factordb.factordb import FactorDB
from Crypto.Util.number import getPrime, inverse, long_to_bytes
import binascii

n = "replace"
c="replace"
e='repalce'

f = FactorDB(n)
f.connect()

phi =1
for i in f.get_factor_list():
    phi = phi * (i-1)


d = inverse( e, phi )

m = pow( c, d, n )
print(long_to_bytes(m))
