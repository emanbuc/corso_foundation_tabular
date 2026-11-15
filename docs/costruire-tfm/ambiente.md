# Ambiente e budget di calcolo

Tutto il corso gira su Colab gratuito con GPU T4: il modello è piccolo per scelta e le dipendenze sono solo PyTorch e scikit-learn, già presenti in Colab. La checklist iniziale è nel [modulo 0](modulo-0-setup.md).

## Budget indicativo

Da misurare in una prova prima della lezione.

| Attività | Addestramenti | Obiettivo di tempo per ciascuno |
| --- | --- | --- |
| E0, la moneta | 2 | Circa 1 minuto |
| Primo addestramento del modulo 4 | 1 | Entro 5 minuti |
| Ablation sul prior del modulo 5 | 3 | Entro 5 minuti |

Se i tempi misurati superano gli obiettivi, si riduce prima il numero di passi, poi d, poi il numero di righe per dataset.

## Piano B

- Checkpoint già addestrati per P1, P2 e P3, da distribuire a chi resta indietro o perde la sessione.
- Senza GPU: E0 gira su CPU. Per i moduli 4 e 5 si usano i checkpoint pronti e si addestra solo per poche centinaia di passi a scopo dimostrativo.
- File di soluzione per ogni modulo, così chi non completa un laboratorio può proseguire con il successivo.
