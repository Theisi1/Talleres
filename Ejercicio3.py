#fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    x,y = 0,1
    for i in range(1, n):
        z = x + y
        x, y = y, z
    return y

#Prueba de escritorio

print("Fibonacci 11 : ", fibonacci(11))
print("Fibonacci 84 : ", fibonacci(84))
print("Fibonacci 1531 : ", fibonacci(1531))

#Grafica de la serie de Fibonacci
import matplotlib.pyplot as plt

def fib_iterative(n):
    if n == 0:
        return 0
    x, y = 0, 1
    for i in range(1, n):
        z = x + y
        x, y = y, z
    return y

# Calcular serie y cocientes
N = 20
fibs = [fib_iterative(i) for i in range(1, N + 1)]
ratios = [fibs[i] / fibs[i - 1] for i in range(1, len(fibs))]

# Graficar
plt.plot(range(2, N + 1), ratios, marker='o')
plt.axhline(y=(1 + 5**0.5)/2, color='r', linestyle='--', label='Número áureo ≈ 1.618')
plt.xlabel('n')
plt.ylabel('fib(n)/fib(n-1)')
plt.title('Convergencia de la razón de Fibonacci al número áureo')
plt.legend()
plt.grid(True)
plt.show()


