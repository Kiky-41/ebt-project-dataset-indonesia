# EBT Project Success Determinants in Indonesia (2002-2024)

[![DOI](https://zenodo.org/badge/1215570272.svg)](https://doi.org/10.5281/zenodo.19657441)

Manuscript (under review, 2026): **Ikhsan, Raharjo, Yustika**, *Consensus Machine Learning and SHAP-Based Evidence on the Determinants of Renewable Energy Project Success in Indonesia under Policy Regime Change* (manuscript available on reasonable request, rfkrhmn@telkomuniversity.ac.id). Sources: **World Bank PPI Database** (34 financially closed EBT projects), **RUPTL PLN 2025-2034** (198 planned projects), **LPEM-FEB UI WP052**, **ESDM Handbook 2024**, **IRENA Outlook Indonesia 2022**, **OJK Sustainable Finance Roadmap**, **PLN audited statements**, **Bank Indonesia daily USD/IDR** (5,633 observations 2002-2024), **RUKN 2025**, **PLN Statistics 2022**. Local: `Data/ppi_master_v2.csv` (not redistributed until acceptance).

Related repos: [vlim-economic-dispatch](https://github.com/Kiky-41/vlim-economic-dispatch), [eic-agc-generator-scheduling](https://github.com/Kiky-41/eic-agc-generator-scheduling), [emfo-sca-ded-optimization](https://github.com/Kiky-41/emfo-sca-ded-optimization), [grasp-bls-eed-uc](https://github.com/Kiky-41/grasp-bls-eed-uc), [sca-ba-dg-placement](https://github.com/Kiky-41/sca-ba-dg-placement), [energy-consumption-forecasting-gru](https://github.com/Kiky-41/energy-consumption-forecasting-gru), [doa-power-systems](https://github.com/Kiky-41/doa-power-systems), [jamali-power-system-dataset](https://github.com/Kiky-41/jamali-power-system-dataset), [power-system-optimization-test-systems](https://github.com/Kiky-41/power-system-optimization-test-systems).

| File | Contents |
|---|---|
| `requirements.txt` | numpy, pandas, scikit-learn, shap, matplotlib, jupyter |
| `CITATION.cff` | Machine-readable citation (DOI 10.5281/zenodo.19657441) |

Note: this repo currently ships documentation and schema only; full `ppi_master_v2.csv` (34 projects x 73 features) is on request. Raw project data is public at the World Bank PPI Database; FX at bi.go.id.

| Item | Value |
|---|---|
| Projects | 34 (financial close 2002-2024), 3,170 MW total (0.4-647 MW), USD 4.8B cumulative |
| Features | 73 engineered, 27 primary for ML |
| Target | `composite_v3` 0-100, mean 45.0 (SD 27.5); Successful >=63.6 (11), At Risk 31.1-63.6 (12), Failed <31.1 (11) |
| Policy eras | FIT pre-2017 (21, mean 51.5, 19.0 percent failed); BPP-I 2017-2019 (8, 43.0); BPP-II 2020-2021 (1, 43.9); BPP-III 2022+ (4, 15.4, 100 percent failed) |
| MDB backing | 7 projects, mean 69.3 vs 27 non-MDB mean 38.7 |

## Headline findings
- Composite `S = 0.25 D1 + 0.30 D2 + 0.20 D3 + 0.25 D4` across financial viability, governance and sponsorship, scale and technology, regulatory and grid access.
- Sponsor strength, financing structure, and ownership type rank top in consensus RF and GBM with Kernel SHAP; BPP headroom, grid accessibility, and PLN credit at financial close complete the core set.
- Regime break is stark: FIT-era success collapses under BPP-III in this sample (n=4, all failed); interpretation is limited by small n and selection into financial close.

## Method
Consensus RF plus GBM with Kernel SHAP; 4-dimension theory-driven score; 10-source merge with FX volatility, BPP tariff headroom vs WACC, and regional grid proxies. Analysis logic is in local `Finale_v2_0.ipynb`.

## Limitations
1. Full data withheld until paper decision; schema above is the contract for the release.
2. n=34; BPP-II (n=1) and BPP-III (n=4) cells are too small for inference; reported as description.
3. PPI covers financial close, not construction or operation outcomes.

## Reproduce (after data release)
`pip install -r requirements.txt`, open the analysis notebook, point to `ppi_master_v2.csv`, Run All.

License: CC-BY-4.0. Cite DOI 10.5281/zenodo.19657441.
