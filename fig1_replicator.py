"""
Figure 1 (fig1_replicator): Population dynamics / phase portrait.
Reproduces Figure 1 of "Why Corrective Institutions Fail" (Proposition 3).

Replicator dynamic for the diligent share p:
    dp/dt = p(1-p)[(alpha+beta) p + eps - beta - gamma]
Parameters (as stated in the text, section "Population dynamics"):
    alpha=0.5, beta=1.0, eps=0.2, gamma=0.6
Interior (unstable) threshold:
    p* = (beta+gamma-eps)/(alpha+beta) = 0.9333...
p=0 and p=1 are locally stable; p* separates the basins. A population starting
at p0=0.9 (below p*) still slides to p=0.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

alpha, beta, eps, gamma = 0.5, 1.0, 0.2, 0.6
pstar = (beta + gamma - eps) / (alpha + beta)


def f(p):
    return p * (1 - p) * ((alpha + beta) * p + eps - beta - gamma)


def trajectory(p0, t):
    p = np.empty_like(t)
    p[0] = p0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        k1 = f(p[i - 1])
        k2 = f(p[i - 1] + 0.5 * dt * k1)
        k3 = f(p[i - 1] + 0.5 * dt * k2)
        k4 = f(p[i - 1] + dt * k3)
        p[i] = p[i - 1] + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
    return p


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.8))

# Left: phase line f(p)
pg = np.linspace(0, 1, 400)
ax1.plot(pg, f(pg), color="#1f4e79", lw=2)
ax1.axhline(0, color="grey", lw=0.8)
for pv, stable in [(0.0, True), (1.0, True), (pstar, False)]:
    ax1.plot(pv, 0, "o", ms=9, mfc=("black" if stable else "white"),
             mec="black", zorder=5)
ax1.annotate("p=0 stable", (0, 0), xytext=(0.04, -0.30), fontsize=8,
             arrowprops=dict(arrowstyle="->", lw=0.8))
ax1.annotate("p=1 stable", (1, 0), xytext=(0.70, 0.10), fontsize=8,
             arrowprops=dict(arrowstyle="->", lw=0.8))
ax1.annotate("p*={:.3f} unstable".format(pstar), (pstar, 0),
             xytext=(pstar - 0.03, 0.45), fontsize=8, ha="center",
             arrowprops=dict(arrowstyle="->", lw=0.8))
ax1.annotate("", xy=(0.32, 0), xytext=(0.50, 0),
             arrowprops=dict(arrowstyle="->", color="crimson", lw=1.4))
ax1.annotate("", xy=(0.98, 0), xytext=(0.84, 0),
             arrowprops=dict(arrowstyle="->", color="seagreen", lw=1.4))
ax1.set_xlabel("diligent share  p")
ax1.set_ylabel("dp/dt")
ax1.set_title(r"Phase line:  $\dot{p}=p(1-p)[(\alpha+\beta)p+\varepsilon-\beta-\gamma]$",
              fontsize=9)
ax1.set_xlim(-0.02, 1.02)

# Right: time trajectories
t = np.linspace(0, 20, 2000)
for p0, col in [(0.50, "#c0392b"), (0.90, "#c0392b"),
                (0.95, "#c0392b"), (0.99, "#2e7d32")]:
    ax2.plot(t, trajectory(p0, t), color=col, lw=1.6, label="p0={}".format(p0))
ax2.axhline(pstar, color="grey", ls="--", lw=1)
ax2.text(19.6, pstar, " p*={:.3f}".format(pstar), va="center",
         fontsize=8, color="grey", ha="right")
ax2.set_xlabel("time  t")
ax2.set_ylabel("diligent share  p(t)")
ax2.set_title("Trajectories (p0=0.9 < p* still collapses to 0)", fontsize=9)
ax2.set_xlim(0, 20)
ax2.set_ylim(-0.02, 1.02)
ax2.legend(fontsize=7, loc="center right")

fig.suptitle(r"Fig.1  Population dynamics  ($\alpha$=0.5, $\beta$=1.0, "
             r"$\varepsilon$=0.2, $\gamma$=0.6)", fontsize=10)
fig.tight_layout(rect=[0, 0, 1, 0.95])
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, "figures"), exist_ok=True)
fig.savefig(os.path.join(here, "figures", "fig1_replicator.pdf"))
print("fig1 saved; p* =", round(pstar, 4))
