# Modulo 1 — Teoria: inferenza ammortizzata (50 min)

Una rete addestrata su dati campionati da un prior impara ad approssimare la predittiva bayesiana di quel prior. Il modulo lo dimostra su un caso in cui la risposta esatta è nota.

## Scaletta

1. **Dal training per dataset al training sul prior (10 min).** Un modello classico apprende da un dataset. Una PFN apprende da milioni di dataset a *come si apprende* da un dataset. L'addestramento si paga una volta, l'inferenza è un forward pass.
2. **L'obiettivo (10 min).** Si campiona un dataset dal prior, si nasconde una parte delle etichette, si minimizza la cross-entropy sulle etichette nascoste. Il minimo di questa loss è la distribuzione predittiva a posteriori.
3. **Esempio E0: la moneta (20 min, lab).** Prior: una moneta con probabilità di testa estratta da una Beta(α, β). Contesto: n lanci. Compito: predire il lancio successivo. Si addestra una rete minuscola in circa un minuto e si confronta la sua uscita con la formula esatta.
4. **Cosa generalizza e cosa no (10 min).** Si interroga la rete con sequenze fuori dal prior, per esempio più lunghe di quelle viste. Messaggio: il modello è buono quanto il prior da cui ha imparato.

## Formule

Obiettivo di addestramento:

$$
\mathcal{L}(\theta) = \mathbb{E}_{D \sim p(D)} \left[ -\log q_\theta(y_{\text{test}} \mid x_{\text{test}}, D_{\text{train}}) \right]
$$

Predittiva esatta per la moneta, con k teste su n lanci:

$$
p(y_{n+1} = 1 \mid y_{1:n}) = \frac{\alpha + k}{\alpha + \beta + n}
$$

!!! info "Grafico da commentare"
    Uscita della rete contro formula esatta, al variare di k e n. I punti devono cadere sulla diagonale.

## Esercizio

- [ ] Riaddestrare con Beta(0.5, 0.5) al posto di Beta(1, 1) e verificare che la rete segua la nuova formula: stessa architettura, prior diverso, modello diverso.
