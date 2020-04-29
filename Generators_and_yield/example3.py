from example2 import infinite_sequence as inf_seq

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


# main ...
for i in inf_seq():
    pal = is_palindrome(i)
    if pal:
        print(pal)
