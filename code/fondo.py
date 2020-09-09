import numpy as np
import matplotlib.pyplot as plt

def sincFunction(t1, t0, N = 500):
    t = t1 - t0
    if np.abs(t) < 1e-5:
        x = 1.0
    else:
        x = np.sin(np.pi * t) / (np.pi * t)
    return x
 
def main():
    # global parameters of the function
    ti = -10
    tf = 10
    t0 = 0
    N = 500
    # The sinc function
    t = np.linspace(ti, tf, N)
    x = [sincFunction(t[i], t0) for i in range(len(t))]
    y = np.zeros_like(t)
    times = np.linspace(-5, 5, 11)
    # Graph of the function
    fig, ax = plt.subplots()
    fig.set_size_inches((15, 10))
    for j in range(len(times)):
        x = [times[j] * sincFunction(t[i], times[j]) for i in range(len(t))]
        y += np.asarray(x)
        ax.plot(t, x)
    ax.plot(t, y, linestyle = '-.', linewidth = 2.2)
    plt.savefig("Figure1.pdf", format = "pdf", transparent = True)
    #ax.minorticks_on()
    #ax.grid(b = True, which = 'minor', linestyle = ':')
    #ax.grid(b = True, which = 'major', linewidth = 1.5)
    plt.show()

if __name__ == "__main__":
    main() 

