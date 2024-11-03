import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return x ** 2


if __name__ == "__main__":
    a = 0
    b = 2

    N = 10000
    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, f(b), N)

    under_curve = y_random < f(x_random)

    rectangle_area = (b - a) * f(b)

    monte_carlo_integral = rectangle_area * np.sum(under_curve) / N

    print("Інтеграл за методом Монте-Карло: ", monte_carlo_integral)

    result, error = spi.quad(f, a, b)
    print("Інтеграл за допомогою функції quad: ", result, "(похибка:", error, ")")

    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.scatter(x_random, y_random, color='blue', s=1, alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

    if np.isclose(monte_carlo_integral, result, atol=0.1):
        print("Метод Монте-Карло дає результат, близький до точного значення.")
    else:
        print(
            "Результат методу Монте-Карло відрізняється від точного значення, збільшіть кількість точок для більшої точності.")
