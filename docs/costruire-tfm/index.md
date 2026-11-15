# Corso 2 · Costruire e addestrare un Tabular Foundation Model

In 6 ore i partecipanti scrivono da zero un piccolo tabular foundation model: il generatore di dati sintetici, il transformer e il ciclo di addestramento, tutto su una GPU T4 di Colab.

Il modello finale ha poche centinaia di migliaia di parametri e lavora su tabelle fino a 150 righe e 5 colonne. Non compete con TabPFN o TabICL: serve a capire perché quei modelli funzionano.

## Obiettivi

Al termine i partecipanti sapranno:

- spiegare l'inferenza bayesiana ammortizzata e verificarla contro una soluzione esatta;
- progettare un prior come generatore di dataset, e prevedere come le sue scelte cambiano il modello;
- implementare un transformer con attenzione su righe e su colonne, invariante alle permutazioni;
- addestrarlo, diagnosticarne i problemi e valutarlo su dati reali contro baseline classiche;
- misurare con un'ablation quanto conta il prior rispetto all'architettura.

## Destinatari

Chi ha seguito il [Corso 1](../usare-tfm/index.md), o conosce già l'uso dei TFM. Servono PyTorch di base (moduli, ottimizzatori, ciclo di training) e nozioni di probabilità bayesiana a livello introduttivo.

## Riferimento didattico

nanoTabPFN, una reimplementazione semplificata di TabPFN v2 in meno di 500 righe, pensata per studenti ([arXiv](https://arxiv.org/abs/2511.03634), [GitHub](https://github.com/automl/nanoTabPFN)). Gli autori dichiarano che manca un prior semplificato: è la parte che questo corso fa scrivere ai partecipanti.

## Struttura

Il corso dura 360 minuti, divisibili in due mezze giornate dopo il modulo 3. Ogni modulo produce un file che il successivo importa.

| # | Modulo | Prodotto | Tipo | Durata (min) |
| --- | --- | --- | --- | --- |
| 0 | [Setup](modulo-0-setup.md) | Notebook con GPU attiva | Pratica guidata | 10 |
| 1 | [Teoria: inferenza ammortizzata](modulo-1-inferenza-ammortizzata.md) | PFN "moneta" verificata contro la formula esatta | Lezione + lab | 50 |
| 2 | [Il prior](modulo-2-prior.md) | `prior.py`: generatore di dataset sintetici | Laboratorio | 75 |
| 3 | [Il modello](modulo-3-modello.md) | `model.py`: transformer per tabelle | Laboratorio | 75 |
| 4 | [L'addestramento](modulo-4-addestramento.md) | `train.py` e un checkpoint | Laboratorio | 70 |
| 5 | [Valutazione e ablation](modulo-5-valutazione-ablation.md) | Tabella dei risultati su dati reali | Laboratorio | 60 |
| 6 | [Verifica e chiusura](modulo-6-verifica.md) | Quiz e discussione | Aula | 20 |
