# zadanie_1

def wypisz(n: int) -> None:
    if n < 0:
        return
    print(n)
    wypisz(n-1)

wypisz(5)

# zadanie_2

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n  == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))

# zadanie_3

def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    return number * power(number, n-1)

print(power(5, 5))

# zadanie_4

def reverse(txt: str, l: int) -> str:  # l = len(txt)
    if l < 1:
        return ""
    return txt[l-1] + reverse(txt, l-1)

print(reverse("KUBA", 4))

# zadanie_5

def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# zadanie_6

def prime(n: int, p:int) -> bool:   # p = n-1
    if n < 2 :
        return False
    elif n == 2:
        return True
    else:
        if p <= 1:
            return True
        elif n % p == 0:
            return False
        else:
            return prime(n, p-1)

print(prime(127, 126))

# zadanie_7

def n_sums(n: int, p: int) -> list[int]:  # p = (10**n)-1
    if p <= 10**(n-1)-1:
        return []
    parz = 0
    nieparz = 0
    for x in range(0, n, 2):
        parz += int(str(p)[x])
    for y in range(1, n, 2):
        nieparz += int(str(p)[y])
    if parz == nieparz:
        return [p] + n_sums(n, p-1)
    else:
        return n_sums(n, p-1)

print(n_sums(2, 99))

# zadanie_8
#
# def combinations(n: int) -> list[list[int]]:


# zadanie_9

def remove_duplicates(txt: str, n: int) -> str:   # n = len(txt)
    if n <= 2:
        if txt[0] == txt[1]:
            return txt[0]
        else: 
            return txt[0] + txt[1]
    if txt[0] == txt[1]:
        return "" + remove_duplicates(txt[1::], n-1)
    else:
        return txt[0] + remove_duplicates(txt[1::], n-1)

print(remove_duplicates("KKYYZZ", 6))

# zadanie_10

def balanced_parentheses(n: int, p: int) -> str:   # p = 2
    x = ["(",")"]
    if n % 2 == 1:
        return ""
    elif n == 2:
        return x


print(balanced_parentheses(4, 2))

