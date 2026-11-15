# Modulo 2 — Esempi didattici (70 min)

Cinque notebook brevi, ciascuno costruito attorno a una sola idea e a un grafico da commentare. Tutti girano su una GPU T4 di Colab; i primi due anche su CPU.

## I notebook

| # | Notebook | Dati | Idea da far emergere | Durata (min) |
| --- | --- | --- | --- | --- |
| E1 | [Primo modello senza training](https://colab.research.google.com/github/emanbuc/corso_foundation_tabular/blob/main/notebooks/usare-tfm/E1_primo_modello.ipynb) | `load_breast_cancer` (569 × 30) | `fit` è istantaneo, il lavoro avviene in `predict`; nessun iperparametro | 10 |
| E2 | [Frontiere di decisione](https://colab.research.google.com/github/emanbuc/corso_foundation_tabular/blob/main/notebooks/usare-tfm/E2_frontiere_decisione.ipynb) | `make_moons`, `make_circles` in 2D | Come cambia la frontiera passando da 20 a 500 punti di contesto; confronto visivo con regressione logistica, kNN, random forest | 15 |
| E3 | [Regressione e incertezza](https://colab.research.google.com/github/emanbuc/corso_foundation_tabular/blob/main/notebooks/usare-tfm/E3_regressione_incertezza.ipynb) | Sinusoide 1D con rumore eteroschedastico e un "buco" nei dati; poi California Housing (campione da 5.000 righe) | L'intervallo predittivo si allarga dove mancano dati; differenza tra stima puntuale e distribuzione | 15 |
| E4 | [TFM contro boosting](https://colab.research.google.com/github/emanbuc/corso_foundation_tabular/blob/main/notebooks/usare-tfm/E4_tfm_vs_boosting.ipynb) | Adult (OpenML), sotto-campioni da 100 a 10.000 righe | Curva di apprendimento: TFM, LightGBM di default, LightGBM con 20 trial di tuning. Si misura anche il tempo totale | 20 |
| E5 | [KV cache e latenza](https://colab.research.google.com/github/emanbuc/corso_foundation_tabular/blob/main/notebooks/usare-tfm/E5_kv_cache_latenza.ipynb) | Stesso dataset di E4 | Tempo di predizione con e senza cache del contesto; costo in memoria | 10 |

## Scheletro comune, da E1

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from tabicl import TabICLClassifier

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, stratify=y, random_state=0)

clf = TabICLClassifier()          # nessun iperparametro da scegliere
clf.fit(X_tr, y_tr)               # memorizza il contesto, scarica i pesi al primo uso
proba = clf.predict_proba(X_te)   # l'in-context learning avviene qui
print(roc_auc_score(y_te, proba[:, 1]))
```

Per E5 basta `TabICLClassifier(kv_cache=True)`: la cache si costruisce in `fit` e viene riusata a ogni `predict`.

## Esercizi per i partecipanti

- [ ] E2: aggiungere il 20% di etichette sbagliate e osservare se la frontiera si deforma.
- [ ] E3: spostare il "buco" ai bordi del dominio e commentare l'estrapolazione.
- [ ] E4: trovare la dimensione del contesto oltre la quale LightGBM con tuning raggiunge il TFM, se accade.

!!! note "Nota per il docente"
    In E3 l'API per quantili e intervalli dipende dalla versione di `tabicl` installata. Va verificata sulla documentazione prima della lezione.
