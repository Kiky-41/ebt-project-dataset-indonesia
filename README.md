# Dataset — EBT project bankability in Indonesia: success determinants under tariff-regime change (financial close 2004–2024)

[![DOI](https://zenodo.org/badge/1215570272.svg)](https://doi.org/10.5281/zenodo.19657441) [![License](https://img.shields.io/badge/license-CC--BY--4.0-green)](LICENSE)

Sources: **World Bank PPI Database** (34 closed EBT projects), **RUPTL PLN 2025–2034** (198 planned), **LPEM-FEB UI WP052**, **ESDM Handbook 2024**, **IRENA Outlook 2022**, **OJK Roadmap**, **PLN audited statements**, **Bank Indonesia USD/IDR daily** (2002–2024), **RUKN 2025**, **PLN Statistics 2022**. Full `ppi_master_v2.csv` (34 × 73) ships on acceptance; the tables below are generated locally by `build_ebt.py` (not committed until publication). Run `python3 build_all.py`; 18 build checks + 3 ML checks, all pass.

| File | Contents |
|---|---|
| `ebt_projects_2002_2024.csv` | Canonical 34-project table: type, FC year, capacity, investment, era, MDB, D1–D4, composite_v3, tercile class (31.1/63.6), raw label |
| `ebt_era_summary.csv` | Mean composite_v3/v2/v1 by era: FIT 51.5, BPP-I 43.0, BPP-II 43.9 (n=1), BPP-III 15.4 (n=4) |
| `ebt_technology_summary.csv` | By technology: Hydro 67.4 highest, Bioenergy 6.0 lowest; capacity (MW) and investment (USD m) totals |
| `ebt_dimension_corr.csv` | D1–D4 correlation vs composite_v3: D2 0.79 highest, then D3 0.54, D4 0.49, D1 0.46 |
| `ebt_missing_report.csv` | Missingness: debt_frac 14, contract_yr 18, cap_mw/cost_per_mw 1 (Metis 2023), label 1 (Atadei), tariff_cap_usd_c_BI 34/34, invest_idr_triliun 4, grid_interconnect 1 |
| `ml_ebt_backtest.csv` | LOO predictions per project: null, era-mean, ridge on D1–D4 |
| `ml_ebt_scores.csv` | LOO scores: null MAE 23.4/RMSE 28.0, era-mean 21.2/26.5, ridge D1–D4 0.6/0.7 (identity, not skill) |

## Headline findings

- MDB-backed projects (n=7) mean 69.3 vs unbacked (n=27) 38.7; D2 governance has the highest single-dimension correlation (0.79).
- Era break is descriptive: FIT 51.5 vs BPP-III 15.4 (36.1-point gap) but BPP-III n=4; reported as description, not inference.
- composite_v3 is an exact linear identity of D1–D4 (S=−104.91+0.7471·D1+0.8965·D2+0.5977·D3+0.7471·D4; max resid <1e-9; weights differ from the 0.25/0.30/0.20/0.25 in the manuscript). Ridge R²≈1 reflects this identity, not predictive skill; the honest baseline is era-mean.

## Companion paper (under review, 2026)

**Ikhsan, Raharjo, Yustika**, *Governance, Regulation, and Renewable Energy Project Bankability in Indonesia: Cross-Sectoral Evidence for Utility Policy and Infrastructure Financing* (under review, 2026; on request, rfkrhmn@telkomuniversity.ac.id). This dataset supports the paper; full methods, RF/GBM+SHAP results, and policy discussion are in the manuscript.

## ML (`ml_ebt.py`, LOO-CV n=34)

Numpy+pandas. Outputs: `ml_ebt_backtest.csv`, `ml_ebt_scores.csv`.

- **LOO baseline**: era-mean MAE 21.2 vs null 23.4 (R² 0.05).
- **Identity check**: OLS of composite_v3 on D1–D4 gives max resid <1e-9, so ridge-on-D1–D4 R² 0.999 is not primary-feature predictive skill.

License: CC-BY-4.0. Cite DOI 10.5281/zenodo.19657441.
