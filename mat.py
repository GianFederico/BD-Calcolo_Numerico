import numpy as np

ITERATION_LIMIT = 1000

# initialize the matrix
A = np.array([[2.4, -0.8, -0.7],
              [0.5, 1.5, 0.7],
              [-0.1, 0.8, 2.1]])
# initialize the RHS vector
b = np.array([0.9, 2.7, 2.8])

print("Sistema di eq.:")
for i in range(A.shape[0]):
    row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b)
for it_count in range(1, ITERATION_LIMIT):
    x_new = np.zeros_like(x)
    print("Iterazione {0}: {1}".format(it_count, x))
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose(x, x_new, rtol=1e-8):
        break
    x = x_new

print("Soluzione: ",x)
error = np.dot(A, x) - b
print("Errore: {0}".format(error))
