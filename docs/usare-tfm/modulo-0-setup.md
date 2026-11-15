# Modulo 0 — Setup dell'ambiente Colab (10 min)

Tutto il corso gira su Colab gratuito con GPU T4 (16 GB di memoria video), a patto di tenere il contesto entro 10.000 righe e 100 colonne.

## Installazione

```bash
pip install tabicl "tabicl[shap]" lightgbm optuna
```

## Checklist

- [ ] Runtime → Cambia tipo di runtime → GPU T4.
- [ ] Eseguire E1 una volta prima della lezione: i pesi si scaricano al primo `fit`.
- [ ] Fissare le versioni dei pacchetti nel notebook: le API cambiano spesso.

Per gli accorgimenti sulla memoria e il piano B in caso di problemi, vedi [Ambiente e hardware](ambiente.md).
