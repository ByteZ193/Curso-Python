def fibonacci1(n):
    if n < 2:
        return n
    return fibonacci1(n - 2) + fibonacci1(n - 1)


def fibonacci2(n):
    fib = 0
    n1, n2 = 0, 1
    i = 0
    if n < 2:
        return n
    while i < n:
        print(n1)
        fib = n1 + n2
        n1 = n2
        n2 = fib
        i += 1
    return n1

def main():
    print(fibonacci1(6))
    print(fibonacci2(4))

if __name__ == '__main__':
    main()
