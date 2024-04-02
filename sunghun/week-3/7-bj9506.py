import sys
readline = sys.stdin.readline

while True:
    n = int(readline().rstrip())
    if n == -1: break

    factors = [i for i in range(1, n) if n%i == 0]
    if n == sum(factors):
        print(f"{n} = {factors[0]} ", end='')
        for i in factors[1:]:   print(f"+ {i} ", end='')
        print()
    else:
        print(f"{n} is NOT perfect.")
        
