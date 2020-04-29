from infinite_palindromes import infinite_palindromes as inf_pal

pal_gen = inf_pal()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
