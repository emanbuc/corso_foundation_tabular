# Corso 1 · Usare un Tabular Foundation Model

In 4 ore i partecipanti imparano a usare un tabular foundation model (TFM) per classificazione e regressione, a valutarlo contro il gradient boosting e a capire quando non conviene.

## Obiettivi

Al termine i partecipanti sapranno:

- spiegare l'in-context learning su tabelle e il ruolo dei prior sintetici;
- ottenere predizioni e stime di incertezza con poche righe di codice, senza addestramento;
- confrontare in modo corretto un TFM con LightGBM/XGBoost (accuratezza, calibrazione, tempi);
- portare un TFM su un dataset realistico, gestendo sbilanciamento, leakage e limiti di memoria;
- esporre il modello come tool di un agente LLM.

## Destinatari

Sviluppatori e data scientist con Python, pandas e scikit-learn di base. Non serve esperienza di deep learning.

## Modello di riferimento

TabICLv2 (`pip install tabicl`), scelto perché è open source con licenza permissiva, pre-training incluso, e non richiede token ([PyPI](https://pypi.org/project/tabicl/)).

TabPFN è l'alternativa: il codice è Apache 2.0 ma i pesi hanno licenza separata ([GitHub](https://github.com/PriorLabs/TabPFN)), da accettare prima della lezione.

## Struttura

Il corso dura 240 minuti: circa un quinto di teoria, il resto su notebook Colab.

| # | Modulo | Tipo | Durata (min) |
| --- | --- | --- | --- |
| 0 | [Setup dell'ambiente Colab](modulo-0-setup.md) | Pratica guidata | 10 |
| 1 | [Teoria: da boosting a in-context learning](modulo-1-teoria.md) | Lezione frontale | 50 |
| 2 | [Esempi didattici (5 notebook brevi)](modulo-2-esempi-didattici.md) | Laboratorio | 70 |
| 3 | [Caso realistico: campagna di marketing bancario](modulo-3-caso-realistico.md) | Laboratorio | 70 |
| 4 | [TFM come tool di un agente LLM](modulo-4-agente-llm.md) | Demo + esercizio | 30 |
| 5 | [Verifica e chiusura](modulo-5-verifica.md) | Quiz + discussione | 10 |

I moduli 0–3 sono autosufficienti: il modulo 4 si può omettere per una versione da 3 ore e mezza.
