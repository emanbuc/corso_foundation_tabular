# Modulo 5 — Valutazione e ablation (60 min)

Il modello non ha mai visto dati reali: questo modulo misura quanto trasferisce, e quale parte del merito va al prior.

## Dati reali entro i limiti del modello

Due classi, fino a 5 colonne, contesto fino a 150 righe:

- `make_moons` e `make_circles`, per vedere le frontiere di decisione;
- Breast Cancer di scikit-learn, con 5 colonne scelte;
- Iris e Wine di scikit-learn, ridotti a due classi;
- Banknote Authentication (OpenML), sotto-campionato a 150 righe di contesto.

## Passi del laboratorio

1. **Frontiere di decisione (10 min).** Stesso grafico del [Corso 1](../usare-tfm/modulo-2-esempi-didattici.md), ma con il modello costruito in aula.
2. **Confronto con le baseline (15 min).** Regressione logistica, kNN, random forest, con 10 ripetizioni dello split. Come riferimento superiore, il TFM pre-addestrato usato nel Corso 1.
3. **Ablation sul prior (20 min).** Tre checkpoint addestrati con P1, P2, P3 e stesso budget di passi. Sui dati con frontiera non lineare ci si aspetta che P1 fallisca.
4. **Calibrazione (5 min).** Curva di affidabilità del modello migliore.
5. **Dove si rompe (10 min).** Più di 5 colonne, più di 150 righe, classi sbilanciate, valori mancanti: si prova e si osserva.

## Tabella dei risultati da compilare in aula

Accuratezza media su 10 split.

| Modello | Moons | Circles | Breast Cancer | Iris (2 classi) | Banknote |
| --- | --- | --- | --- | --- | --- |
| Regressione logistica |  |  |  |  |  |
| kNN |  |  |  |  |  |
| Random forest |  |  |  |  |  |
| Nostro modello, prior P1 |  |  |  |  |  |
| Nostro modello, prior P2 |  |  |  |  |  |
| Nostro modello, prior P3 |  |  |  |  |  |
| TFM pre-addestrato (riferimento) |  |  |  |  |  |

!!! question "Ipotesi da verificare con la tabella"
    Con la stessa architettura, cambiare il prior cambia il modello più di quanto faccia aggiungere strati.

## Cosa separa questo modello da uno di frontiera

Regressione, valori mancanti, variabili categoriche, ensemble su più pre-elaborazioni, tabelle grandi, prior molto più ricchi e budget di calcolo di ordini di grandezza superiore. Regressione, valori mancanti ed ensemble mancano anche in nanoTabPFN, per scelta dichiarata ([arXiv](https://arxiv.org/abs/2511.03634)).
