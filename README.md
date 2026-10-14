# Replication Package

**"Why Corrective Institutions Fail: A Rational-Action Model of Adverse Selection in Organizational Promotion"**

This package reproduces the four figures of the manuscript. The article is a
purely parametric rational-action model: every numerical example and figure is
generated directly from the closed-form expressions and the parameter values
stated in the text. **No external data are used.**

## Files

| Script | Output | Reproduces | Parameters (all from the text) |
|---|---|---|---|
| `fig1_replicator.py` | `figures/fig1_replicator.pdf` | Figure 1 / Proposition 3 (phase portrait) | `alpha=0.5, beta=1.0, eps=0.2, gamma=0.6`; unstable threshold `p* = 0.933` |
| `fig2_deterrence.py` | `figures/fig2_deterrence.pdf` | Figure 2 / Proposition 6 + Table 1 (supervision paradox) | `S=1, mu=2, nu=0.5`; deterrence `0.500 -> 0.135` as `kappa: 0 -> 5` |
| `fig3_invertedU.py` | `figures/fig3_invertedU.pdf` | Figure 3 / Prediction 1 (inverted-U deterrence) | fixed budget `S=1, mu=2, nu=0.5`; `q^dagger=0.5, Omega^dagger=0.5` |
| `fig4_window.py` | `figures/fig4_window.pdf` | Figure 4 / Prediction 4 (hump-shaped reform window) | `R0=1, r=0.7, B0=4, b=0.3, C0=0.5, c=0.3, tau=0.2`; window `~ (-1.06, 0.53)`, trough `g ~ -0.29` |

## Requirements

Python 3.8+ with `numpy` and `matplotlib` (see `requirements.txt`).

## Run

```bash
pip install -r requirements.txt
python fig1_replicator.py
python fig2_deterrence.py
python fig3_invertedU.py
python fig4_window.py
```

Each script writes its PDF into `figures/` and prints the key numbers it used.
Total run time is a few seconds.

## Notes on each figure

- **Figure 1.** Replicator dynamic `dp/dt = p(1-p)[(alpha+beta)p + eps - beta - gamma]`.
  `p=0` and `p=1` are locally stable; the interior threshold `p*` is unstable.
  A population starting at `p0 = 0.9` (below `p*`) still converges to `p=0`.

- **Figure 2.** Interior optimum `q*(k) = (-mu k + sqrt(mu^2 k^2 + 8 mu S))/(4 mu)`,
  `D*(k) = sqrt(mu q*(q*+k)/nu)`, `Omega*(k) = q* D*`. Reproduces Table 1 exactly:
  `(k, q*, D*, Omega*) = (0, 0.500, 1.000, 0.500), (1, 0.309, 1.272, 0.393),
  (2, 0.207, 1.352, 0.280), (5, 0.096, 1.401, 0.135)`.

- **Figure 3.** Along the fixed-budget path `nu D^2 = S - mu q^2`,
  `Omega(q) = q sqrt((S - mu q^2)/nu)` peaks at `q^dagger = sqrt(S/(2 mu))`.
  Adverse-selection intensity is plotted as the mirror image `1 - Omega(q)/Omega^dagger`.

- **Figure 4.** `sigma*(g) = (R0 e^{r g} + C0 e^{-c g}) / ((1-tau) B0 e^{b g})`.
  The feasible window is `{sigma*(g) < 1/2} intersect {B > C + R}`; the left panel
  shades the belief condition, the right panel shades the resource condition.
