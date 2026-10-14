"""
Figure 3 (fig3_invertedU): Prediction 1.

At a FIXED budget, along the allocation path  nu D^2 = S - mu q^2, deterrence is
    Omega(q) = q * sqrt((S - mu q^2) / nu),   q in (0, sqrt(S/mu)]
which peaks at
    q^dagger     = sqrt(S / (2 mu))
    Omega^dagger = (S/2) sqrt(mu nu)
Adverse-selection intensity is the mirror image of deterrence and is therefore
U-shaped in q; it is plotted here as  AS(q) = 1 - Omega(q)/Omega^dagger.

Parameters: S=1, mu=2, nu=0.5  ->  q^dagger=0.5, Omega^dagger=0.5.
Left : deterrence inverted-U in q.  Right: adverse-selection intensity U-shaped.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

S, mu, nu = 1.0, 2.0, 0.5
qmax = np.sqrt(S / mu)
q = np.linspace(1e-6, qmax * (1 - 1e-9), 400)
Om = q * np.sqrt(np.maximum(S - mu * q ** 2, 0.0) / nu)
qd = np.sqrt(S / (2 * mu))
Od = (S / 2.0) * np.sqrt(mu * nu)
AS = 1.0 - Om / Od

qd_s = "{:.3f}".format(qd)
Od_s = "{:.3f}".format(Od)

fig, (axL, axR) = plt.subplots(1, 2, figsize=(9, 3.8))

axL.plot(q, Om, color="#1f4e79", lw=2)
axL.plot(qd, Od, "o", color="crimson", ms=7, zorder=5)
axL.annotate(r"$q^{\dagger}$=" + qd_s + "\n" + r"$\Omega^{\dagger}$=" + Od_s,
             (qd, Od), xytext=(qd + 0.04, Od - 0.14), fontsize=8, color="crimson",
             arrowprops=dict(arrowstyle="->", color="crimson", lw=0.8))
axL.set_xlabel("detection frequency  q")
axL.set_ylabel(r"deterrence  $\Omega(q)$")
axL.set_title("Deterrence is inverted-U in q (fixed budget)", fontsize=9)
axL.set_xlim(0, qmax * 1.05)
axL.set_ylim(0, Od * 1.18)
axL.grid(alpha=0.3)

axR.plot(q, AS, color="#8e44ad", lw=2)
axR.plot(qd, 0.0, "o", color="crimson", ms=7, zorder=5)
axR.annotate(r"$q^{\dagger}$=" + qd_s, (qd, 0), xytext=(qd + 0.04, 0.18),
             fontsize=8, color="crimson",
             arrowprops=dict(arrowstyle="->", color="crimson", lw=0.8))
axR.set_xlabel("detection frequency  q")
axR.set_ylabel("adverse-selection intensity")
axR.set_title("Adverse selection is U-shaped in q", fontsize=9)
axR.set_xlim(0, qmax * 1.05)
axR.set_ylim(-0.03, 1.05)
axR.grid(alpha=0.3)

fig.suptitle(r"Fig.3  Prediction 1  ($S$=1, $\mu$=2, $\nu$=0.5;  "
             + r"$q^{\dagger}$=" + qd_s + ", " + r"$\Omega^{\dagger}$=" + Od_s + ")",
             fontsize=10)
fig.tight_layout(rect=[0, 0, 1, 0.95])
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, "figures"), exist_ok=True)
fig.savefig(os.path.join(here, "figures", "fig3_invertedU.pdf"))
print("fig3 saved; q^dagger =", round(qd, 4), " Omega^dagger =", round(Od, 4),
      " qmax =", round(qmax, 4))
