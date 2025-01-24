def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = 100
fib_series = fibonacci(100)
print(f"Fibonacci series up to F({n}): {fib_series}")