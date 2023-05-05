import sympy as sym

def Newton(vars, funcs):

    F = sym.Matrix(funcs)
    JacobianInv = sym.Matrix(funcs).jacobian(vars).det()

    pass

vars = ['x', 'y', 'z']
funcs = ['x ** 2 + y ** 2 + z ** 2 - 1',
         '2 * x ** 2 + y ** 2 - 4 * z',
         '3 * x ** 2 - 4 * y + z ** 2']

F = sym.Matrix(funcs)
JacobianInv = sym.Matrix(funcs).jacobian(vars).det()

x, y, z = sym.symbols('x y z')
f = sym.lambdify([x, y, z], F)

print(f(0, 0, 0))