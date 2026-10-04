# EBT Project Success Determinants in Indonesia (2002-2024)

[![DOI](https://zenodo.org/badge/1215570272.svg)](https://doi.org/10.5281/zenodo.19657441) [![License](https://img.shields.io/badge/license-CC--BY--4.0-green)](LICENSE)

Manuscript (under review, 2026): **Ikhsan, Raharjo, Yustika**, *Consensus Machine Learning and SHAP-Based Evidence on the Determinants of Renewable Energy Project Success in Indonesia under Policy Regime Change* (on request, rfkrhmn@telkomuniversity.ac.id). Sources: **World Bank PPI Database** (34 closed EBT projects), **RUPTL PLN 2025-2034** (198 planned), **LPEM-FEB UI WP052**, **ESDM Handbook 2024**, **IRENA Outlook 2022**, **OJK Roadmap**, **PLN audited statements**, **Bank Indonesia USD/IDR daily** (5,633 obs. 2002-2024), **RUKN 2025**, **PLN Statistics 2022**. Full `ppi_master_v2.csv` (34 x 73) ships on acceptance; raw projects at PPI Database, FX at bi.go.id.

Related repos: [vlim-economic-dispatch](https://github.com/Kiky-41/vlim-economic-dispatch), [eic-agc-generator-scheduling](https://github.com/Kiky-41/eic-agc-generator-scheduling), [emfo-sca-ded-optimization](https://github.com/Kiky-41/emfo-sca-ded-optimization), [grasp-bls-eed-uc](https://github.com/Kiky-41/grasp-bls-eed-uc), [sca-ba-dg-placement](https://github.com/Kiky-41/sca-ba-dg-placement), [energy-consumption-forecasting-gru](https://github.com/Kiky-41/energy-consumption-forecasting-gru), [doa-power-systems](https://github.com/Kiky-41/doa-power-systems), [jamali-power-system-dataset](https://github.com/Kiky-41/jamali-power-system-dataset), [power-system-optimization-test-systems](https://github.com/Kiky-41/power-system-optimization-test-systems).

| File | Contents |
|---|---|
| `requirements.txt` | numpy, pandas, scikit-learn, shap, matplotlib, jupyter |
| `CITATION.cff` | Machine-readable citation (DOI 10.5281/zenodo.19657441) |

## Score

$$S = 0.25\,D_1 + 0.30\,D_2 + 0.20\,D_3 + 0.25\,D_4$$

| Dimension | Weight | Content |
|---|---|---|
| D1 Financial viability | 0.25 | BPP headroom, debt fraction, contract length, cost per MW, FX volatility |
| D2 Governance and sponsorship | 0.30 | MDB support, sponsor strength, procurement, ownership |
| D3 Scale and technology | 0.20 | Capacity, maturity, LCOE, years operating |
| D4 Regulatory and grid | 0.25 | FIT/BPP regime, PLN credit, grid access |

| Item | Value |
|---|---|
| Projects | 34 (2002-2024), 3,170 MW (0.4-647 MW), USD 4.8B |
| Features | 73 engineered, 27 primary |
| Target | `composite_v3` 0-100, mean 45.0 (SD 27.5); Successful >=63.6 (11), At Risk 31.1-63.6 (12), Failed <31.1 (11) |
| Eras | FIT pre-2017 (21, 51.5, 19.0 percent failed); BPP-I (8, 43.0); BPP-II (1, 43.9); BPP-III (4, 15.4, 100 percent failed) |
| MDB | 7 backed, mean 69.3 vs 27 unbacked mean 38.7 |

## Headline findings
- Sponsor strength, financing structure, and ownership top consensus RF and GBM with Kernel SHAP; BPP headroom, grid access, and PLN credit complete the core set.
- Regime break is stark in-sample (FIT 51.5 vs BPP-III 15.4) but BPP-III n=4; reported as description, not inference.

## Limitations
1. Full data withheld until decision; schema above is the release contract.
2. BPP-II (n=1) and BPP-III (n=4) cells too small for inference.
3. PPI covers financial close, not construction or operation outcomes.

## Proposed method
Consensus random forest plus gradient boosting with Kernel SHAP over 27 primary features; four theory-first dimensions keep the score comparable across regimes.

## Reproduce (after release)
`pip install -r requirements.txt`, point the notebook to `ppi_master_v2.csv`, Run All.

License: CC-BY-4.0. Cite DOI 10.5281/zenodo.19657441.
