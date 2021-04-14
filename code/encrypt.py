def encrypt(c):
    new_c = str(int("1" + c) * 10000000 + 4880088916693658600666882)
    return str(int(new_c[:13]) + int(new_c[12:]))