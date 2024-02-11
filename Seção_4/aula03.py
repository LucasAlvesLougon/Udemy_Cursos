def soma(x, y, z=None):
    if z is not None:
        resultado1 = x + y + z
        print(f'{x} + {y} + {z} = {resultado1}')
    else:
        resultado2 = x + y
        print(f'{x} + {y} = {resultado2}')

soma(1, 2, 40)