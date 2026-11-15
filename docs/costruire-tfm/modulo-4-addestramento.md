# Modulo 4 — L'addestramento (70 min)

Il ciclo di training è quello di un classificatore qualsiasi, con una differenza: ogni batch è un insieme di dataset interi, non di righe.

## Scaletta

1. **Un passo di training (15 min).** Campionare un batch di dataset dal prior. Scegliere a caso il punto di taglio tra righe di contesto e righe di test. Calcolare la cross-entropy solo sulle righe di test.
2. **Configurazione di partenza (10 min).** AdamW, warmup lineare e decadimento a coseno, clipping del gradiente, precisione mista. Come riferimento, l'esempio di nanoTabPFN usa 3 strati, 2.500 passi, batch da 32 dataset e learning rate 4e-3, su tabelle da 150 righe, 5 colonne e 2 classi ([arXiv](https://arxiv.org/abs/2511.03634)).
3. **Primo addestramento (15 min).** Si lancia con il prior P2. Gli autori di nanoTabPFN riportano risultati paragonabili alle baseline classiche dopo circa un minuto su una GPU; su T4 il tempo va misurato, e ci si aspetta qualche minuto.
4. **Diagnostica (20 min).** Tre curve da tenere sotto controllo insieme: loss sul prior, accuratezza su dataset sintetici mai visti, accuratezza su un piccolo dataset reale tenuto da parte.
5. **Salvataggio e interfaccia (10 min).** Checkpoint su Drive e una classe con `fit` e `predict_proba` in stile scikit-learn, per riusare gli strumenti del [Corso 1](../usare-tfm/index.md).

## Scheletro del passo di training

```python
def train_step(model, prior, opt, batch=32, n_rows=150, n_features=5):
    X, y = prior(batch, n_rows, n_features)
    cut = int(torch.randint(20, n_rows - 20, (1,)))      # contesto | test
    logits = model(X, y[:, :cut], n_train=cut)           # (batch, n_rows - cut, 2)
    loss = torch.nn.functional.cross_entropy(
        logits.reshape(-1, 2), y[:, cut:].reshape(-1))
    opt.zero_grad(); loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    opt.step()
    return loss.item()
```

## Problemi tipici e come riconoscerli

| Sintomo | Causa probabile | Verifica |
| --- | --- | --- |
| Loss ferma a 0,69 | Il modello ignora il contesto: maschera o encoder del target sbagliati | Addestrare su un solo dataset ripetuto: deve memorizzarlo |
| Loss sul prior bassa, dati reali scadenti | Prior troppo semplice o troppo lontano dai dati reali | Confrontare P1, P2, P3 nel modulo 5 |
| Loss instabile o NaN | Learning rate alto, valori estremi non tagliati | Ridurre il learning rate, controllare il clipping nell'encoder |
| Buono a 150 righe, scadente a 50 | Taglio contesto/test sempre uguale in training | Rendere casuale il punto di taglio |

## Esercizio

- [ ] Addestrare con numero di colonne variabile da 1 a 5 e verificare che l'accuratezza a 5 colonne non peggiori.
