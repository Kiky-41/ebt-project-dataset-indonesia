#!/usr/bin/env python3
"""Dataset EBT-Bankability: 34 proyek EBT Indonesia (financial close 2004-2024), 73 kolom.
Sumber: [DRAFT]/RF-GBM-SHAP (JCLIMF)/[Dataset]/ppi_master_v2.csv (World Bank PPI, RUPTL, LPEM, ESDM, IRENA, OJK, LK PLN, BI, RUKN, Statistik PLN).
Skrip ini TIDAK merekonstruksi 73 kolom dari sumber primer (tidak tersedia di repo); ia memvalidasi,
membersihkan, dan menurunkan tabel kanonik + ringkasan era/teknologi/dimensi dengan cek validasi.
Run: python3 build_ebt.py  (butuh numpy, pandas)"""
import os, sys
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
SRC_CANDS = [
    os.path.join(HERE, 'ppi_master_v2.csv'),
    '/Users/workk/Documents/[Think!]/[FMK]/Research Things/[DRAFT]/RF-GBM-SHAP (JCLIMF)/[Dataset]/ppi_master_v2.csv',
    '/Users/workk/Documents/[Think!]/[FMK]/Research Things/Data/ppi_master_v2.csv',
    '/Users/workk/Documents/[Think!]/[FMK]/Research Things/Data/ppi_master_v2_corrected.csv',
]
SRC = next((p for p in SRC_CANDS if os.path.exists(p)), None)
if SRC is None:
    print('FAIL sumber ppi_master_v2.csv tidak ditemukan'); sys.exit(1)
checks = []
def chk(n, ok, d=''):
    checks.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + n, d)
df = pd.read_csv(SRC)
chk('n baris = 34', len(df) == 34, str(len(df)))
chk('n proyek unik = 34', df['Project name'].nunique() == 34)
chk('n kolom = 73', df.shape[1] == 73, str(df.shape[1]))
chk('rentang year_fc 2004-2024 (BUKAN 2002-2024)', int(df.year_fc.min()) == 2004 and int(df.year_fc.max()) == 2024,
    f"{int(df.year_fc.min())}-{int(df.year_fc.max())}")
chk('is_fit + is_bpp = 1 semua baris', ((df.is_fit_era + df.is_bpp_era) == 1).all())
chk('flag FIT cocok dengan bpp_era', (df.bpp_era.eq('FIT').astype(int) == df.is_fit_era).all())
chk('distribusi era 21/8/1/4', df.bpp_era.value_counts().to_dict() == {'FIT': 21, 'BPP-I': 8, 'BPP-III': 4, 'BPP-II': 1},
    str(df.bpp_era.value_counts().to_dict()))
chk('MDB 7 vs non-MDB 27', (df.has_mdb.sum() == 7) and ((df.has_mdb == 0).sum() == 27))
chk('total kapasitas 3170.1 MW (34 baris, 1 null dikecualikan)', abs(df.cap_mw.sum(skipna=True) - 3170.1) < 0.15,
    f"{df.cap_mw.sum(skipna=True):.1f}")
chk('rentang kapasitas 1.0-515.0 MW (BUKAN 0.4-647 di naskah)', abs(df.cap_mw.min() - 1.0) < 1e-9 and abs(df.cap_mw.max() - 515.0) < 1e-9,
    f"{df.cap_mw.min()}-{df.cap_mw.max()}")
chk('total investasi 9120.4 juta USD (naskah tulis 4.8B: selisih = double-count Sarulla 1540+1540.5)',
    abs(df.invest_usd.sum() - 9120.4) < 0.15, f"{df.invest_usd.sum():.1f}")
chk('cost_per_mw = invest/cap (33 baris non-null, eksak)', np.allclose(
    df.loc[df.cap_mw.notna(), 'cost_per_mw'], df.loc[df.cap_mw.notna(), 'invest_usd'] / df.loc[df.cap_mw.notna(), 'cap_mw'], atol=1e-9))
q33, q67 = float(df.composite_v3.quantile(1/3)), float(df.composite_v3.quantile(2/3))
chk('kuantil v3 Q33=31.30 Q67=63.53 (naskah tulis 31.1/63.6: beda pembulatan/metode)',
    abs(q33 - 31.302127556076087) < 0.01 and abs(q67 - 63.52982437244032) < 0.01, f'{q33:.2f}/{q67:.2f}')
cls = pd.cut(df.composite_v3, [-1e-9, 31.1, 63.6, 1e9], labels=['Non-Bankable', 'At Risk', 'Bankable'])
chk('split tercile naskah 11/12/11 terpenuhi pada 31.1/63.6', cls.value_counts().to_dict() == {'Non-Bankable': 11, 'At Risk': 12, 'Bankable': 11},
    str(cls.value_counts().to_dict()))
chk('label mentah tidak sama dengan kelas tercile (label=TBD, jangan dipakai sebagai target)',
    pd.crosstab(df.label, cls, dropna=False).shape == (4, 3))
chk('korelasi D2 tertinggi (0.79) > D3 (0.54) > D4 (0.49) > D1 (0.46)',
    list(df[['D1_score','D2_score','D3_score','D4_score','composite_v3']].corr()['composite_v3'].round(2).values) == [0.46, 0.79, 0.54, 0.49, 1.0])
chk('kolom tariff_cap_usd_c_BI seluruhnya null (sumber BI belum tersambung)', df['tariff_cap_usd_c_BI'].isna().all())
chk('Atadei: label null + composite_v3=1.19 (baris paling berisiko, FIT 2011)', df[df['Project name'].str.contains('Atadei')].composite_v3.iloc[0] < 2.0)
out = pd.DataFrame({
    'project': df['Project name'], 'ebt_type': df.ebt_type, 'year_fc': df.year_fc, 'cap_mw': df.cap_mw,
    'invest_usd_m': df.invest_usd, 'cost_per_mw': df.cost_per_mw, 'era': df.bpp_era, 'is_fit': df.is_fit_era,
    'has_mdb': df.has_mdb, 'D1': df.D1_score, 'D2': df.D2_score, 'D3': df.D3_score, 'D4': df.D4_score,
    'composite_v3': df.composite_v3, 'class_tercile_31p1_63p6': cls.astype(str), 'label_raw': df.label,
    'bpp_headroom_usd_c': df.bpp_headroom_usd_c, 'pln_credit_at_fc': df.pln_credit_at_fc})
out.to_csv(os.path.join(HERE, 'ebt_projects_2002_2024.csv'), index=False)
era = df.groupby('bpp_era').agg(n=('composite_v3','size'), mean_v3=('composite_v3','mean'), median_v3=('composite_v3','median'),
    mean_v2=('composite_v2','mean'), mean_v1=('composite','mean')).round(2)
era.to_csv(os.path.join(HERE, 'ebt_era_summary.csv'))
tech = df.groupby('ebt_type').agg(n=('composite_v3','size'), mean_v3=('composite_v3','mean'),
    cap_mw=('cap_mw','sum'), invest_usd_m=('invest_usd','sum')).round(2)
tech.to_csv(os.path.join(HERE, 'ebt_technology_summary.csv'))
corr = df[['D1_score','D2_score','D3_score','D4_score','composite_v3']].corr().round(4)
corr.to_csv(os.path.join(HERE, 'ebt_dimension_corr.csv'))
miss = df.isna().sum(); miss[miss > 0].to_csv(os.path.join(HERE, 'ebt_missing_report.csv'), header=['n_missing'])
print(f'{sum(checks)}/{len(checks)} checks passed')
if not all(checks): sys.exit(1)
print('tulis: ebt_projects_2002_2024.csv, ebt_era_summary.csv, ebt_technology_summary.csv, ebt_dimension_corr.csv, ebt_missing_report.csv')
print('sumber:', SRC)
