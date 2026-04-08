def fib(n):
    fibarr = [0,1]

    for _ in range(2,n+1):
        fibarr.append(fibarr[_-1] + fibarr[_-2])

    return(fibarr[n])

print(fib(10))