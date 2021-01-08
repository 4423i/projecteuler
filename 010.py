def eratosthenes(n):
    table = [0]*(n+1)
    prime_list = []

    for i in range(2, n+1):
        if table[i] == 0:
            prime_list.append(i)
            for j in range(i+i, n+1, i):
                table[j] = 1

    return prime_list
print(sum(eratosthenes(2000000)))
print(sum(eratosthenes(10)))