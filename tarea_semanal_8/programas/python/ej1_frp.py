
from pytc2.general import s
from pytc2.remociones import isFRP

Z6 = (s + 4) / (16*s + 12)

print("Z6(s) =", Z6)
print("¿Z6(s) es FRP?")

if isFRP(Z6):
    print("SI")
else:
    print("NO")
