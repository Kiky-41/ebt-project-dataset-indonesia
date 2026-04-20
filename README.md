# 🌿 Dataset: EBT Project Success Determinants in Indonesia (2002–2024)
[![DOI](https://zenodo.org/badge/1215570272.svg)](https://doi.org/10.5281/zenodo.19657441)

Curated multi-source dataset of financially closed renewable energy (EBT) projects in Indonesia, constructed for machine learning analysis of project success determinants under evolving policy regimes.

This dataset supports research on blended finance, green macroprudential policy, and sustainable energy investment in Indonesia.

---

## 📄 Related Publication

Ikhsan, R.R.N., Raharjo, J., Yustika, L.M. (2026)
*Consensus Machine Learning and SHAP-Based Evidence on the Determinants of Renewable Energy Project Success in Indonesia under Policy Regime Change*
*(under review — manuscript available upon reasonable request)*

---

## 🚀 Features

- 📦 **34 financially closed EBT projects** — full population, World Bank PPI Database, 2002–2024
- 🔢 **73 engineered features** from 10 integrated data sources
- 🏗️ **4-dimension composite success score** (composite_v3, scale 0–100)
- 🧠 **Machine learning ready** — RF, GBM, and Kernel SHAP compatible
- 📅 Covers **4 policy eras**: FIT, BPP-I, BPP-II, BPP-III
- ⚡ **6 technology types**: Geothermal, Hydro, MicroHydro, Solar, Wind, Bioenergy

---

## 🧠 Dataset Overview

The composite success score is theory-driven across four dimensions:

$$S = 0.25 \, D_1 + 0.30 \, D_2 + 0.20 \, D_3 + 0.25 \, D_4$$

| Dimension | Weight | Description |
|-----------|--------|-------------|
| D1 — Financial Viability | 25% | BPP headroom, debt fraction, contract duration, cost per MW, FX volatility |
| D2 — Governance & Sponsorship | 30% | MDB support, sponsor strength, competitive procurement, ownership type |
| D3 — Scale & Technology | 20% | Installed capacity, technology maturity, LCOE, years in operation |
| D4 — Regulatory & Grid Access | 25% | Policy regime (FIT/BPP), PLN credit score, grid accessibility |

---

## 📊 Key Statistics

| Statistic | Value |
|-----------|-------|
| Projects | 34 (financial close 2002–2024) |
| Total capacity | 3,170 MW (range: 0.4–647 MW) |
| Total investment | USD 4.8B (cumulative) |
| Features (post-engineering) | 73 |
| ML primary features | 27 |
| Composite score mean (SD) | 45.0 (27.5), range 0–100 |
| MDB-backed projects | 7 (mean score: 69.3) |
| Non-MDB projects | 27 (mean score: 38.7) |

**Success classification (empirical tercile thresholds):**

| Class | Threshold | Count |
|-------|-----------|-------|
| Successful | composite_v3 ≥ 63.6 | 11 (32%) |
| At Risk | 31.1 ≤ composite_v3 < 63.6 | 12 (35%) |
| Failed | composite_v3 < 31.1 | 11 (32%) |

**By policy era:**

| Era | n | Mean Score | Failed (%) |
|-----|---|-----------|-----------|
| FIT (pre-2017) | 21 | 51.5 | 19.0% |
| BPP-I (2017–2019) | 8 | 43.0 | 37.5% |
| BPP-II (2020–2021) | 1 | 43.9 | 0.0% |
| BPP-III (2022+) | 4 | 15.4 | **100%** |

---

## 📂 Project Structure

```text
ebt-project-dataset-indonesia/
├── data/
│   └── ppi_master_v2.csv       # Main dataset (34 projects × 73 features)
├── notebooks/
│   └── Finale_v2_0.ipynb       # Analysis notebook (RF + GBM + Kernel SHAP)
├── README.md
└── .gitignore
```

---

## ⚙️ Requirements

- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- SHAP
- Matplotlib
- Jupyter Notebook

Install all dependencies:

```bash
pip install numpy pandas scikit-learn shap matplotlib jupyter
```

---

## ▶️ Usage

Clone and run the notebook:

```bash
git clone https://github.com/Kiky-41/ebt-project-dataset-indonesia.git
cd ebt-project-dataset-indonesia
jupyter notebook
```

Open `notebooks/Finale_v2_0.ipynb` and run all cells.

---

## 📊 Data Sources

The dataset integrates 10 primary sources:

| No. | Source | Primary Content |
|----|--------|----------------|
| 1 | World Bank PPI Database | 34 EBT projects: finance, capital structure, technology, sponsor |
| 2 | RUPTL PLN 2025–2034 | 198 planned projects, capacity and investment by region |
| 3 | LPEM-FEB UI WP052 (2020) | BPP tariff analysis, WACC benchmarks |
| 4 | ESDM Handbook 2024 | National energy statistics, installed capacity by technology |
| 5 | IRENA Outlook Indonesia (2022) | LCOE benchmarks, EBT potential by province |
| 6 | OJK Sustainable Finance Roadmap | Green finance framework and taxonomy |
| 7 | PLN Audited Financial Statements | Interest coverage ratio, net revenue, credit quality |
| 8 | Bank Indonesia Daily Exchange Rate | 5,633 USD/IDR daily observations (2002–2024) |
| 9 | RUKN 2025 | National transmission plan, grid balance by region |
| 10 | PLN Statistics 2022 | Grid density, electrification ratio, network length by region |

---

## 📊 Dataset

> ⚠️ The full dataset (`ppi_master_v2.csv`) is currently **not publicly released** as the associated paper is under review.

To request access:
- Contact the corresponding author: rfkrhmn@telkomuniversity.ac.id
- Raw project data is publicly available at the [World Bank PPI Database](https://ppi.worldbank.org)
- Bank Indonesia exchange rate data: [https://www.bi.go.id](https://www.bi.go.id)

The dataset will be made publicly available upon paper acceptance.

**Dataset schema (selected features):**

| Feature | Dimension | Description |
|---------|-----------|-------------|
| sponsor_strength | D2 | Composite governance score (CS = 0.928) |
| financing_struct_score | D1 | Capital stack quality index (CS = 0.903) |
| ownership_type | D2 | Project ownership classification (CS = 0.856) |
| bpp_headroom_BI | D1 | BPP tariff headroom relative to WACC |
| grid_accessibility | D4 | Regional grid accessibility proxy |
| pln_credit_at_fc | D4 | PLN credit score at financial close |
| composite_v3 | Target | Composite success score (0–100) |

---

## 📌 Reproducibility

This repository contains the analysis code and dataset schema.
Full reproduction of published results requires the complete `ppi_master_v2.csv` dataset, available upon reasonable request from the corresponding author.

---


## 🔗 DOI (Zenodo)

After creating a GitHub release, Zenodo will automatically generate a DOI for this repository.

---

## 📜 License

Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## 🙌 Acknowledgements

This work is based on research in renewable energy project finance, interpretable machine learning, and Indonesia's energy transition policy.

---

## ⭐ Support

If you find this repository useful:
- ⭐ Star this repo
- 🍴 Fork and contribute
- 📢 Share with the research community
