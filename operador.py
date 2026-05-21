def operador(n1, n2, op):
    if op == '+':
        return(n1 + n2)
    elif op == '-':
        return(n1 - n2)
    elif op == '*':
        return(n1 * n2)
    elif op == '/':
        return(n1 / n2)
    elif op == '%':
        return(n1 % n2)
    elif op == '^':
        return(n1 ** n2)
    else:
        return 'Operador inválido'

print('Soma:' , operador(17, 32, '+'))
print('Subtracao: ' , operador(1236, 612, '-'))
print('Multiplicacao:' , operador(144, 15, '*'))
print('Divisao: ' , operador(512, 128, '/'))
print('Modulo: ' , operador(64, 5, '%'))
print('Potencia: ' , operador(9, 3, '^'))
