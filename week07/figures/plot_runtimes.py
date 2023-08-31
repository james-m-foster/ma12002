import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

filename = "measured_runtimes.txt"

data = pd.read_csv(filename)

print (data.head())

degree = np.asarray(data["n"])
t_naive = np.asarray(data["naive"])
t_horner = np.asarray(data["horner"])
t_naive_fast_power = np.asarray(data["naive_fast_power"])

def plot_all(labels):
    p1, = plt.plot(degree,t_naive,
                  linewidth=2,
                  color="blue",
                  marker='o',
                  markersize=6,
                  markeredgewidth=2,
                  markerfacecolor="white")
    p2, = plt.plot(degree,t_horner,
                   linewidth=2,
                   color="red",
                   marker='s',
                   markersize=6,
                   markeredgewidth=2,
                   markerfacecolor="white")
                   
    p3, = plt.plot(degree,t_naive_fast_power,
                   linewidth=2,
                   color="green",
                   marker='*',
                   markersize=6,
                   markeredgewidth=2,
                   markerfacecolor="white")
    if labels:
        p1.set_label("naive")
        p2.set_label("Horner\'s rule")
        p3.set_label("naive + fast_power")
                   


plt.clf()

ax = plt.gca()

# Standard scale
plt.figure(figsize=(8,4))
plt.subplot(1, 2, 1)
ax = plt.gca()
ax.set_ylim(-5,200)
plot_all(True)
ax.set_xlabel("polynomial degree $n$")
ax.set_ylabel("runtime in milliseconds")
plt.legend(loc="upper left")

# Logarithmic scale
plt.subplot(1, 2, 2)
ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylim(1.E-2,1000)
plt.plot()
plot_all(False)
ax.set_xlabel("polynomial degree $n$")
plt.plot([200,800],[0.08,4*0.08],
         linewidth=2,
         linestyle='--',
         color='black',
         label=r'$\propto n$ (linear growth)')
plt.plot([200,800],[1,16],
         linewidth=2,
         linestyle=':',
         color='black',
         label=r'$\propto n^2$ (quadratic growth)')
plt.legend(loc='upper left')

plt.savefig("poly_runtimes.png",bbox_inches="tight")
