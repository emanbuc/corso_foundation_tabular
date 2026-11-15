# Modulo 3 — Caso realistico: campagna di marketing bancario (70 min)

Si predice quali clienti di una banca sottoscriveranno un deposito dopo una telefonata, per decidere chi chiamare con un budget limitato.

## Il dataset

Bank Marketing ([UCI](https://archive.ics.uci.edu/dataset/222/bank+marketing), disponibile anche su OpenML). Circa 45.000 righe, 16 variabili miste numeriche e categoriche, classe positiva attorno al 12%. È abbastanza grande da non entrare comodamente in una T4 come contesto unico, e questo è voluto.

!!! warning "Da verificare al caricamento"
    Dimensioni e quota della classe positiva sono riportate a memoria.

**Perché è realistico:** classi sbilanciate, variabili categoriche, una variabile con leakage, un vincolo di memoria e una decisione economica a valle.

## Scaletta

1. **Inquadramento (5 min).** Dalla domanda di business alla metrica: non accuratezza, ma PR-AUC e guadagno atteso per chiamata.
2. **Esplorazione e leakage (10 min).** La variabile `duration` (durata della chiamata) è nota solo a chiamata conclusa. Si mostra il punteggio con e senza: il primo è irrealistico. Va rimossa.
3. **Protocollo di valutazione (5 min).** Split stratificato train/validation/test, fissato una volta. Stesso split per tutti i modelli.
4. **Baseline (10 min).** Regressione logistica e LightGBM di default, poi LightGBM con tuning breve.
5. **TFM con contesto limitato (15 min).** Contesto da 2.000, 5.000 e 10.000 righe campionate dal train. Si confronta campionamento casuale e stratificato, e si misura memoria GPU e tempo.
6. **Calibrazione e soglia (10 min).** Curva di affidabilità e Brier score. Scelta della soglia con una matrice costi-benefici: costo della chiamata contro margine del deposito.
7. **Interpretabilità (10 min).** Valori SHAP su poche decine di righe con `tabicl[shap]`, a livello globale e per singolo cliente. Confronto con l'importanza delle variabili di LightGBM.
8. **Discussione (5 min).** Quale modello va in produzione, e con quali costi di esercizio?

## Tabella dei risultati da compilare in aula

| Modello | PR-AUC | ROC-AUC | Brier | Tempo totale (s) | Memoria GPU (GB) |
| --- | --- | --- | --- | --- | --- |
| Regressione logistica |  |  |  |  |  |
| LightGBM di default |  |  |  |  |  |
| LightGBM con tuning |  |  |  |  |  |
| TFM, contesto 2.000 |  |  |  |  |  |
| TFM, contesto 5.000 |  |  |  |  |  |
| TFM, contesto 10.000 |  |  |  |  |  |

!!! success "Messaggio finale del modulo"
    Il TFM dà un risultato competitivo in pochi minuti e senza tuning, ma su dataset di questa taglia il boosting resta un concorrente serio. La scelta dipende da tempo di sviluppo, latenza e costo della GPU.

**Varianti del caso:** churn di clienti, rischio di credito, abbandono del personale. La scaletta resta identica.
