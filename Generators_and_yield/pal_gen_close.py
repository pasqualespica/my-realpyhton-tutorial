from infinite_palindromes import infinite_palindromes as inf_pal

pal_gen = inf_pal()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))
