# Modulo 3 — Il modello (75 min)

Il modello tratta ogni cella della tabella come un token e alterna due attenzioni: tra le colonne di una stessa riga e tra le righe di una stessa colonna. La struttura segue quella di nanoTabPFN ([arXiv](https://arxiv.org/abs/2511.03634)), riscritta in aula pezzo per pezzo.

**Forma dei dati:** un tensore `(batch, righe, colonne + 1, d)`. La colonna in più è il target.

## I componenti

| Componente | Cosa fa | Punto didattico | Durata (min) |
| --- | --- | --- | --- |
| Encoder delle feature | Normalizza ogni colonna con media e deviazione delle sole righe di training, taglia i valori estremi, proietta ogni scalare in un vettore | La normalizzazione usa solo il contesto: nessuna informazione passa dal test | 10 |
| Encoder del target | Proietta le etichette note; per le righe di test inserisce un segnaposto | Come il modello distingue "etichetta nota" da "etichetta da predire" | 10 |
| Attenzione tra colonne | Self-attention lungo l'asse delle colonne, riga per riga | Interazioni tra variabili | 10 |
| Attenzione tra righe | Attenzione lungo l'asse delle righe: il training guarda solo sé stesso, il test guarda solo il training | Qui avviene l'in-context learning | 15 |
| Blocco completo | Le due attenzioni, un MLP, connessioni residue e layer norm | Composizione in 3 strati | 10 |
| Decoder | Legge i token della colonna target nelle righe di test e produce i logit | Uscita solo dove serve | 5 |

I restanti 15 minuti sono dedicati ai test.

## Scelte da motivare in aula

- Nessun embedding posizionale: righe e colonne non hanno ordine, e il modello deve essere invariante alle loro permutazioni.
- La maschera dell'attenzione tra righe impedisce alle righe di test di influenzarsi a vicenda.
- Dimensioni proposte: d = 96, 4 teste, 3 strati. Sono un punto di partenza, da ridurre se il training è lento.

## Test da scrivere prima di addestrare

- [ ] Permutare le righe di training non cambia le predizioni.
- [ ] Permutare le colonne non cambia le predizioni.
- [ ] Modificare una riga di test non cambia le predizioni delle altre righe di test.
- [ ] Il modello accetta tabelle con un numero di colonne diverso senza modifiche al codice.

## Esercizio

Rimuovere la maschera e osservare quale test fallisce. Poi discutere perché in addestramento la loss scenderebbe comunque.
