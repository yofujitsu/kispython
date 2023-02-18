def main(n):
    if n == 0:
        return 0.04
    if n == 1:
        return 0.72
    if n >= 2:
        return 1 - main(n - 2) ** 2 - main(n - 1) / 60

print(main([0.13, 0.75, -0.14, -0.06, 0.83, 0.79],
           [0.73, 0.11, -0.7, 0.32, 0.18, -0.55]))
print(main([0.98, -0.27, 0.22, 0.49, -0.83, -0.69],
           [0.44, 0.96, -0.74, -0.0, 0.08, -0.91]))
print(main([-0.96, 0.86, 0.82, 0.54, 0.27, 0.88],
           [0.95, -0.84, 0.25, -0.23, -0.76, 0.18]))
print(main([0.69, -0.69, -0.14, 0.41, -0.79, -0.39],
           [-0.56, 0.43, 0.49, 0.25, 0.31, -0.29]))
print(main([0.62, -0.25, 0.05, 0.16, -0.38, 0.59],
           [-0.39, -0.84, 0.16, 0.25, -0.68, 0.62]))