
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
        f *= c
    return(f)


print(fatorial(3, show=False))

