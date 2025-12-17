import sys
# Example: expects a number and returns next quantum fibonacci number (replace with real Q.F.S.T.D.S logic)
def quantum_fibonacci(n):
    a, b = 0, 1
    for _ in range(int(n)):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    if len(sys.argv) > 1:
        seq = quantum_fibonacci(sys.argv[1])
        print(seq)
    else:
        print("0")
