# Modulo 2 — Il prior (75 min)

Il prior è una funzione che restituisce un dataset di classificazione nuovo a ogni chiamata. Si costruisce in tre versioni di complessità crescente, e ogni versione viene poi usata nel [modulo 5](modulo-5-valutazione-ablation.md) per l'ablation.

## Le tre versioni

| Versione | Come genera le etichette | Cosa insegna al modello | Durata (min) |
| --- | --- | --- | --- |
| P1 — Lineare | Pesi casuali, soglia su una combinazione lineare con rumore | Solo frontiere lineari | 15 |
| P2 — MLP casuale | Rete con pesi e attivazione casuali, soglia sulla mediana dell'uscita | Frontiere non lineari, classi bilanciate | 20 |
| P3 — Modello causale | Grafo aciclico casuale: ogni nodo è funzione rumorosa dei genitori; alcune variabili diventano colonne, una il target | Colonne correlate, variabili irrilevanti, relazioni causali e anti-causali | 25 |

I restanti 15 minuti servono a ispezionare i dati generati.

## Passi del laboratorio

1. Definire l'interfaccia comune: `sample(batch, n_rows, n_features) → X, y`, con tensori già sulla GPU.
2. Scrivere P1 e disegnare 9 dataset 2D in una griglia.
3. Scrivere P2, con profondità, larghezza e attivazione estratte a caso per ogni dataset.
4. Scrivere P3: ordine topologico casuale, probabilità di arco come iperparametro.
5. Aggiungere gli iper-prior: livello di rumore, numero di colonne informative, scala delle variabili.
6. Controllo di qualità: su 200 dataset generati, misurare l'accuratezza di regressione logistica e random forest. Un buon prior produce problemi di difficoltà varia, né tutti banali né tutti rumore.

## Scheletro di P2

```python
import torch

def sample_mlp_prior(batch, n_rows, n_features, device="cuda"):
    X = torch.randn(batch, n_rows, n_features, device=device)
    hidden = int(torch.randint(4, 33, (1,)))
    act = [torch.tanh, torch.relu, torch.sin][int(torch.randint(0, 3, (1,)))]
    W1 = torch.randn(batch, n_features, hidden, device=device)
    W2 = torch.randn(batch, hidden, 1, device=device)
    z = act(X @ W1) @ W2                       # (batch, n_rows, 1)
    z = z + 0.1 * torch.randn_like(z)          # rumore sulle etichette
    y = (z > z.median(dim=1, keepdim=True).values).long().squeeze(-1)
    return X, y
```

!!! question "Scelta di progetto da discutere"
    Generare i dati al volo durante il training, oppure pre-generarli su disco. nanoTabPFN carica dati pre-generati ([arXiv](https://arxiv.org/abs/2511.03634)); qui si generano al volo sulla GPU, perché i prior sono semplici e ogni batch è nuovo.

## Esercizi

- [ ] Aggiungere a P2 una colonna categorica, ottenuta discretizzando una colonna numerica.
- [ ] In P3, generare dataset in cui il target è causa delle colonne e non effetto, e confrontarli a occhio con gli altri.
