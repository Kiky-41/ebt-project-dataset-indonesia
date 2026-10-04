# EBT Project Success in Indonesia (2002-2024)

[![DOI](https://zenodo.org/badge/1215570272.svg)](https://doi.org/10.5281/zenodo.19657441) [![License](https://img.shields.io/badge/license-CC--BY--4.0-green)](LICENSE)

Manuscript (under review, 2026): **Ikhsan, Raharjo, Yustika**, *Consensus Machine Learning and SHAP-Based Evidence on the Determinants of Renewable Energy Project Success in Indonesia under Policy Regime Change* (on request, rfkrhmn@telkomuniversity.ac.id). Thirty-four wind, sun, water, and steam bets reached financial close; some thrived, some stalled as tariffs shifted from FIT to BPP eras. This dataset asks what separated them, with receipts from ten public sources.

Related repos: [vlim-economic-dispatch](https://github.com/Kiky-41/vlim-economic-dispatch), [eic-agc-generator-scheduling](https://github.com/Kiky-41/eic-agc-generator-scheduling), [emfo-sca-ded-optimization](https://github.com/Kiky-41/emfo-sca-ded-optimization), [grasp-bls-eed-uc](https://github.com/Kiky-41/grasp-bls-eed-uc), [sca-ba-dg-placement](https://github.com/Kiky-41/sca-ba-dg-placement), [energy-consumption-forecasting-gru](https://github.com/Kiky-41/energy-consumption-forecasting-gru), [doa-power-systems](https://github.com/Kiky-41/doa-power-systems), [jamali-power-system-dataset](https://github.com/Kiky-41/jamali-power-system-dataset), [power-system-optimization-test-systems](https://github.com/Kiky-41/power-system-optimization-test-systems).

| File | Contents |
|---|---|
| `requirements.txt` | numpy, pandas, scikit-learn, shap, matplotlib, jupyter |
| `CITATION.cff` | Machine-readable citation |

Full `ppi_master_v2.csv` (34 projects by 73 features) ships on acceptance; raw projects live at the World Bank PPI Database, FX at bi.go.id.

## Score

$$S = 0.25\,D_1 + 0.30\,D_2 + 0.20\,D_3 + 0.25\,D_4$$

| Dimension | Weight | Story |
|---|---|---|
| D1 Money | 0.25 | tariff headroom, debt, contract length, cost per MW |
| D2 Backers | 0.30 | MDB support, sponsor muscle, procurement, ownership |
| D3 Scale-tech | 0.20 | size, maturity, LCOE, years running |
| D4 Rules-grid | 0.25 | FIT/BPP era, PLN credit, grid reach |

## Results

| Cut | Rule | Count |
|---|---|---|
| Successful | S at least 63.6 | 11 |
| At Risk | 31.1 to 63.6 | 12 |
| Failed | below 31.1 | 11 |

| Era | Projects | Mean S | Failed share |
|---|---|---|---|
| FIT pre-2017 | 21 | 51.5 | 19.0 percent |
| BPP-I 2017-2019 | 8 | 43.0 | 37.5 percent |
| BPP-II 2020-2021 | 1 | 43.9 | 0.0 percent |
| BPP-III 2022 on | 4 | 15.4 | 100 percent |

MDB-backed projects average 69.3 against 38.7 for the rest; sponsors and financing structure top the SHAP list. The BPP-III cell is tiny (n=4), so read it as a warning flag, not a verdict.

## Proposed method

Consensus random forest plus gradient boosting, explained by Kernel SHAP over 27 primary features. Four theory-first dimensions keep the score honest across regimes.

## Reproduce (after release)
`pip install -r requirements.txt`, point the notebook to `ppi_master_v2.csv`, Run All.

License: CC-BY-4.0. Cite DOI 10.5281/zenodo.19657441.
