# Modulo 1 — Teoria: da boosting a in-context learning (50 min)

Un TFM sostituisce l'addestramento per dataset con un solo forward pass di un transformer pre-addestrato, che riceve il training set come contesto.

## Scaletta

1. **Il problema (10 min).** Perché i dati tabulari sono diversi da testo e immagini: colonne eterogenee, pochi campioni, nessun ordine. Perché il gradient boosting ha dominato per anni. Perché un LLM non è uno stimatore statistico.
2. **In-context learning su tabelle (10 min).** `fit` memorizza il contesto, `predict` esegue il modello. Analogia con il few-shot prompting, con righe al posto dei token. Conseguenza: niente tuning, ma il costo si paga in inferenza.
3. **Prior-data Fitted Network (15 min).** Il transformer approssima la distribuzione predittiva a posteriori rispetto a un prior definito da dataset sintetici. I dataset nascono da modelli causali strutturali (TabPFN) e da prior ad albero (TabICL): il prior è il vero "bias induttivo" del modello.
4. **Architetture (10 min).** Attenzione alternata su righe e colonne (TabPFN) contro colonne-poi-righe (TabICL). Complessità su n righe e m colonne: O(n²m + nm²) contro O(n² + nm²) ([TabICLv2](https://arxiv.org/abs/2602.11139)). Ensemble tramite permutazioni di colonne e classi.
5. **Limiti (5 min).** Memoria quadratica nelle righe, latenza, dipendenza dalla GPU, prior che non copre ogni dominio, risultati ancora in gran parte in preprint.

## Formule

Distribuzione predittiva che il modello approssima:

$$
p(y_* \mid x_*, D) = \int p(y_* \mid x_*, \varphi)\, p(\varphi \mid D)\, d\varphi
$$

Obiettivo di pre-training sui dataset sintetici:

$$
\mathcal{L}(\theta) = \mathbb{E}_{(D,\,x_*,\,y_*) \sim \text{prior}} \left[ -\log q_\theta(y_* \mid x_*, D) \right]
$$

!!! question "Domanda guida per l'aula"
    Se il modello non vede mai dati reali in pre-training, da dove viene la sua accuratezza?
