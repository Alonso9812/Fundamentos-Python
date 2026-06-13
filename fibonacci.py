def fibonacci(n):
    n1 = 0
    n2 = 1

    for _ in range(n):
        print(n1, end=' ')
        n1, n2 = n2, n1 + n2

fibonacci(10)
# Output: 0 1 1 2 3 5 8 13 21 34