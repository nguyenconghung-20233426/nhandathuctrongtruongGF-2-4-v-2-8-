
from main import nhan

# Kiem thu GF(2^4)
print("Kiem thu GF(2^4):")
print("x * x =", hex(nhan(0x2, 0x2, 4, 0x13)))
print("(x+1) * (x+1) =", hex(nhan(0x3, 0x3, 4, 0x13)))
print("7 * 0 =", hex(nhan(0x7, 0x0, 4, 0x13)))

# Kiem thu GF(2^8)
print("\nKiem thu GF(2^8):")
print("x * x =", hex(nhan(0x2, 0x2, 8, 0x11B)))
print("(x+1) * (x+1) =", hex(nhan(0x3, 0x3, 8, 0x11B)))
print("57 * 83 =", hex(nhan(0x57, 0x83, 8, 0x11B)))
