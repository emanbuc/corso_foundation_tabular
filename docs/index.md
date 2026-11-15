# Corso Tabular Foundation Model

Due corsi brevi sui Tabular Foundation Model (TFM): nel primo si impara a usarne uno, nel secondo se ne costruisce uno da zero. Tutti i laboratori girano su Colab gratuito con GPU T4.

| | [Corso 1 · Usare un TFM](usare-tfm/index.md) | [Corso 2 · Costruire un TFM](costruire-tfm/index.md) |
| --- | --- | --- |
| **Durata** | 4 ore (240 minuti) | 6 ore (360 minuti), divisibili in due mezze giornate |
| **Cosa si fa** | Si usa un TFM pre-addestrato per classificazione e regressione, lo si valuta contro il gradient boosting e si capisce quando non conviene | Si scrivono il generatore di dati sintetici, il transformer e il ciclo di addestramento di un piccolo TFM |
| **Destinatari** | Sviluppatori e data scientist con Python, pandas e scikit-learn di base | Chi ha seguito il corso 1, o conosce già l'uso dei TFM |
| **Prerequisiti** | Nessuna esperienza di deep learning | PyTorch di base e nozioni introduttive di probabilità bayesiana |
| **Modello di riferimento** | TabICLv2 (`pip install tabicl`) | nanoTabPFN, riscritto in aula pezzo per pezzo |

## Come è organizzato il materiale

- Ogni corso ha una pagina per modulo, con scaletta, tempi, codice di partenza ed esercizi.
- I notebook dei laboratori sono nella cartella `notebooks/` del repository.
- I file prodotti nei laboratori del corso 2 (`prior.py`, `model.py`, `train.py`) e le relative soluzioni sono in `src/costruire_tfm/`.

## Da dove partire

- Per chi non ha mai usato un TFM: [Corso 1, modulo 0](usare-tfm/modulo-0-setup.md).
- Per chi conosce già l'uso dei TFM e vuole capire come funzionano dentro: [Corso 2, modulo 0](costruire-tfm/modulo-0-setup.md).
