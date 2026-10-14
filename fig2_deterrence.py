"""
Figure 2 (fig2_deterrence): The supervision paradox (Proposition 6 / Table 1).

The regulator chooses (q, D) subject to C = mu q^2 + nu D^2 <= S and maximizes
U_R = q D + kappa D (expected deterrence plus political visibility of punishment).
Interior first-order conditions (from the proof) give
    q*(k)     = (-mu k + sqrt(mu^2 k^2 + 8 mu S)) / (4 mu)
    D*(k)     = sqrt( mu q*(q* + k) / nu )
    Omega*(k) = q* D*
Parameters (text and Table 1): S=1, mu=2, nu=0.5, k in [0, 5].
Deterrence falls 0.500 -> 0.135 as k runs 0 -> 5 (73% less deterrence).

Left : deterrence Omega*(k) strictly decreasing (Table-1 points overlaid).
Right: q* falls and D* rises -- the mix slides from detection toward punishment.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

S, mu, nu = 1.0, 2.0, 0.5


def qstar(k):
    k = np.asarray(k, float)
    return (-mu * k + np.sqrt(mu ** 2 * k ** 2 + 8 * mu * S)) / (4 * mu)


def Dstar(k):
    q = qstar(k)
    return np.sqrt(mu * q * (q + k) / nu)


def Omega(k):
    return qstar(k) * Dstar(k)


k = np.linspace(0, 5, 400)
tab_k = np.array([0, 1, 2, 5])
tab_om = Omega(tab_k)

fig, (axL, axR) = plt.subplots(1, 2, figsize=(9, 3.8))

axL.plot(k, Omega(k), color="#1f4e79", lw=2)
axL.plot(tab_k, tab_om, "o", color="crimson", ms=6, zorder=5)
for kk, oo in zip(tab_k, tab_om):
    axL.annotate("{:.3f}".format(oo), (kk, oo), xytext=(kk + 0.10, oo - 0.035),
                 fontsize=7, color="crimson")
axL.set_xlabel(r"visibility weight  $\kappa$")
axL.set_ylabel(r"expected deterrence  $\Omega^{*}=q^{*}D^{*}$")
axL.set_title(r"Deterrence strictly decreasing in $\kappa$", fontsize=9)
axL.set_ylim(0, 0.56)
axL.grid(alpha=0.3)

axR.plot(k, qstar(k), color="#2e7d32", lw=2, label=r"detection  $q^{*}$")
axR.plot(k, Dstar(k), color="#c0392b", lw=2, label=r"punishment  $D^{*}$")
axR.set_xlabel(r"visibility weight  $\kappa$")
axR.set_ylabel("optimal level")
axR.set_title("Mix slides from detection toward punishment", fontsize=9)
axR.legend(fontsize=8)
axR.grid(alpha=0.3)

fig.suptitle(r"Fig.2  Supervision paradox  ($S$=1, $\mu$=2, $\nu$=0.5)", fontsize=10)
fig.tight_layout(rect=[0, 0, 1, 0.95])
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, "figures"), exist_ok=True)
fig.savefig(os.path.join(here, "figures", "fig2_deterrence.pdf"))
print("fig2 saved; Omega*(k=0,1,2,5) =", np.round(Omega(tab_k), 3))
