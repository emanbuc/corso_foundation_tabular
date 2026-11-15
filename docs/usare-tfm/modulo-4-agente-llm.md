# Modulo 4 — TFM come tool di un agente LLM (30 min)

L'LLM decide cosa predire e interpreta il risultato; il TFM fa il calcolo statistico. Nessuno dei due sostituisce l'altro.

## Scaletta

1. **Demo (10 min).** Una funzione `predict_tabular(csv_path, target, task)` che carica i dati, separa le righe senza etichetta, esegue il TFM e restituisce predizioni, probabilità e una metrica in cross-validation. Si espone come tool con il suo schema JSON a un LLM con function calling.
2. **Esercizio (15 min).** Sul dataset del [modulo 3](modulo-3-caso-realistico.md), chiedere all'agente: "quali 100 clienti chiamo domani?". Si osserva la traccia delle chiamate al tool.
3. **Discussione (5 min).** Cosa può andare storto: target sbagliato, leakage non riconosciuto dall'agente, metrica riportata senza validazione, dati sensibili inviati a un servizio esterno.

!!! tip "Regola da lasciare in aula"
    Il tool restituisce sempre una stima di affidabilità insieme alla predizione, e l'agente è istruito a riportarla.

Il modulo è indipendente dal fornitore dell'LLM: serve solo un modello con function calling. La GPU è usata dal solo TFM.
