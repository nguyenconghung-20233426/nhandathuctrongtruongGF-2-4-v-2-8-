
def nhan(a, b, m, poly):  # poly la da thuc sinh
    ketqua = 0

    for i in range(m):
        if b & 1:
            ketqua = ketqua ^ a

        carry = a & (1 << (m - 1))
        a = a << 1

        if carry:
            a = a ^ poly

        b = b >> 1

    return ketqua
