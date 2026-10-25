
def nhan(a, b, m, poly): #poly là đa thức sinh
    ketqua = 0

    for i in range(m):
        # Neu bit cuoi cua b bang 1
        if b & 1:
            ketqua = ketqua ^ a

        # Kiem tra bit cao nhat cua a
        carry = a & (1 << (m - 1))

        # Nhan a voi x bang cach dich trai
        a = a << 1

        # Neu vuot qua bac cho phep thi rut gon
        if carry:
            a = a ^ poly

        # Chuyen sang bit tiep theo cua b
        b = b >> 1

    return ketqua


print("1. GF(2^4)")
print("2. GF(2^8)")
chon = int(input("Chon truong: "))

if chon == 1:
    m = 4
    poly = 0x13
elif chon == 2:
    m = 8
    poly = 0x11B
else:
    print("Lua chon khong hop le!")
    exit()

a = int(input("Nhap a (he 16): "), 16)
b = int(input("Nhap b (he 16): "), 16)

if a >= (1 << m) or b >= (1 << m):
    print("Gia tri nhap khong hop le!")
else:
    ketqua = nhan(a, b, m, poly)
    print("Ket qua =", hex(ketqua))
