"""
Figure 4 (fig4_window): Prediction 4.

Cycle state g with  R = R0 e^{r g},  B = B0 e^{b g},  C = C0 e^{-c g}. The
critical belief is
    sigma*(g) = (R0 e^{r g} + C0 e^{-c g}) / ((1 - tau) B0 e^{b g})
which is U-shaped when r > b. The net reform gain  NG(g) = B - C - R  is
inverted-U. The reform window is the intersection
    { sigma*(g) < 1/2 }  intersect  { B > C + R } ,
an intermediate interval centered in the mild-downturn region.

Parameters (stated in the text): R0=1, r=0.7, B0=4, b=0.3, C0=0.5, c=0.3, tau=0.2.
Numeric window (sigma* < 1/2) is about (-1.06, 0.53), trough at g ~ -0.29.

Left : sigma*(g) U-shaped with the feasible window shaded.
Right: net reform gain B - C - R inverted-U with the {B>C+R} region shaded.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

R0, r = 1.0, 0.7
B0, b = 4.0, 0.3
C0, c = 0.5, 0.3
tau = 0.2


def sigma(g):
    return (R0 * np.exp(r * g) + C0 * np.exp(-c * g)) / ((1 - tau) * B0 * np.exp(b * g))


def netgain(g):
    return B0 * np.exp(b * g) - C0 * np.exp(-c * g) - R0 * np.exp(r * g)


def roots(func, level, grid):
    y = func(grid) - level
    idx = np.where(np.sign(y[:-1]) != np.sign(y[1:]))[0]
    out = []
    for i in idx:
        lo, hi = grid[i], grid[i + 1]
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            if (func(lo) - level) * (func(mid) - level) <= 0:
                hi = mid
            else:
                lo = mid
        out.append(0.5 * (lo + hi))
    return out


g = np.linspace(-5, 4, 800)
s = sigma(g)
ng = netgain(g)
win = roots(sigma, 0.5, g)          # sigma* = 1/2
ngpos = roots(netgain, 0.0, g)      # B - C - R = 0

fig, (axL, axR) = plt.subplots(1, 2, figsize=(9, 3.8))

axL.plot(g, s, color="#1f4e79", lw=2, label=r"$\sigma^{*}(g)$")
axL.axhline(0.5, color="grey", ls="--", lw=1)
axL.text(3.9, 0.52, "1/2", fontsize=8, color="grey", ha="right")
if len(win) == 2:
    axL.axvspan(win[0], win[1], color="seagreen", alpha=0.15, label="feasible window")
    for wv in win:
        axL.axvline(wv, color="seagreen", ls=":", lw=1)
    axL.text(0.5 * (win[0] + win[1]), 0.06,
             "window\n({:.2f}, {:.2f})".format(win[0], win[1]),
             ha="center", fontsize=8, color="seagreen")
gt = np.linspace(-5, 4, 40000)
trough = gt[np.argmin(sigma(gt))]
axL.plot(trough, sigma(trough), "o", color="crimson", ms=6, zorder=5)
axL.annotate("trough g$\\approx${:.2f}".format(trough), (trough, sigma(trough)),
             xytext=(trough - 0.3, sigma(trough) + 0.22), fontsize=8, color="crimson",
             arrowprops=dict(arrowstyle="->", color="crimson", lw=0.8))
axL.set_xlabel("cycle state  g")
axL.set_ylabel(r"critical belief  $\sigma^{*}(g)$")
axL.set_title("Threshold U-shaped; window in the mild downturn", fontsize=9)
axL.legend(fontsize=7, loc="upper center")
axL.grid(alpha=0.3)
axL.set_ylim(0, 1.6)

axR.plot(g, ng, color="#8e44ad", lw=2, label=r"$B-C-R$")
axR.axhline(0, color="grey", ls="--", lw=1)
if len(ngpos) == 2:
    axR.axvspan(ngpos[0], ngpos[1], color="orange", alpha=0.15,
                label=r"$\{B>C+R\}$")
for wv in win:
    axR.axvline(wv, color="seagreen", ls=":", lw=1)
axR.set_xlabel("cycle state  g")
axR.set_ylabel("net reform gain  $B-C-R$")
axR.set_title("Net reform gain inverted-U", fontsize=9)
axR.legend(fontsize=8)
axR.grid(alpha=0.3)

fig.suptitle(r"Fig.4  Prediction 4  ($R_0$=1, $r$=0.7, $B_0$=4, $b$=0.3, "
             r"$C_0$=0.5, $c$=0.3, $\tau$=0.2)", fontsize=10)
fig.tight_layout(rect=[0, 0, 1, 0.95])
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, "figures"), exist_ok=True)
fig.savefig(os.path.join(here, "figures", "fig4_window.pdf"))
print("fig4 saved; sigma*=1/2 roots (window) =", np.round(win, 3),
      " trough g =", round(float(trough), 3))
