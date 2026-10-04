#!/usr/bin/env python3
"""Baseline ML bankability: prediksi composite_v3 dari 4 skor dimensi (D1-D4), LOO-CV.
Kandidat (ditetapkan di muka): null (mean latih), era-mean, ridge D1-D4 (alpha=1).
Bukan reproduksi RF/GBM+SHAP naskah (27 fitur, sklearn/shap, ada di notebook Finale v2.0.ipynb).
Keluaran: ml_ebt_backtest.csv (prediksi LOO per proyek), ml_ebt_scores.csv.
Run: python3 ml_ebt.py  (butuh numpy, pandas)"""
import os, sys
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'ML-Models'))
from ml_common import chk, finish, Ridge, mae, r2
D = pd.read_csv(os.path.join(HERE, 'ebt_projects_2002_2024.csv'))
X = D[['D1', 'D2', 'D3', 'D4']].to_numpy(float); y = D.composite_v3.to_numpy(float); era = D.era.to_numpy()
rows = []
for i in range(len(D)):
    m = np.ones(len(D), bool); m[i] = False
    p_null = float(y[m].mean())
    p_era = float(y[m][era[m] == era[i]].mean()) if (era[m] == era[i]).sum() > 0 else p_null
    p_ridge = float(Ridge(alpha=1.0).fit(X[m], y[m]).predict(X[i:i+1])[0])
    rows.append(dict(project=D.project[i], era=era[i], actual=float(y[i]), null=p_null, era_mean=p_era, ridge_d1d4=p_ridge))
R = pd.DataFrame(rows)
R.to_csv(os.path.join(HERE, 'ml_ebt_backtest.csv'), index=False)
S = pd.DataFrame({c: dict(mae=mae(y, R[c]), rmse=float(np.sqrt(np.mean((y - R[c].to_numpy())**2))), r2=r2(y, R[c]))
    for c in ['null', 'era_mean', 'ridge_d1d4']}).T.round(3)
S.to_csv(os.path.join(HERE, 'ml_ebt_scores.csv'))
print(S.to_string()); print(R.head(5).round(1).to_string(index=False))
chk('LOO 34 baris lengkap, semua finite', len(R) == 34 and np.isfinite(R[['null','era_mean','ridge_d1d4']].to_numpy()).all())
chk('null RMSE dekat SD sampel ddof=1 +-1.0 (LOO-null sedikit lebih besar)', abs(float(np.sqrt(np.mean((y - R.null.to_numpy())**2))) - float(y.std(ddof=1))) < 1.0,
    f"{float(np.sqrt(np.mean((y - R.null.to_numpy())**2))):.2f} vs {float(y.std(ddof=1)):.2f}")
Xa = np.column_stack([np.ones(len(X)), X]); coef, *_ = np.linalg.lstsq(Xa, y, rcond=None)
chk('identitas: composite_v3 linier eksak dari D1-D4 (max resid < 1e-9)', float(np.abs(y - Xa @ coef).max()) < 1e-9,
    'S=%.2f%+.4f*D1%+.4f*D2%+.4f*D3%+.4f*D4' % tuple(coef))
chk('info: R2 LOO ridge ~1 BUKAN skill prediksi (identitas di atas)', True, f"{r2(y, R.ridge_d1d4):.3f}")
finish('ml_ebt')
