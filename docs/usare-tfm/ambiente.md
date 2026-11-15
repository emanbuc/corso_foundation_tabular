# Ambiente e hardware

Tutto il corso gira su Colab gratuito con GPU T4 (16 GB di memoria video), a patto di tenere il contesto entro 10.000 righe e 100 colonne. L'installazione e la checklist iniziale sono nel [modulo 0](modulo-0-setup.md).

## Accorgimenti per restare nella memoria

| Leva | Effetto | Quando usarla |
| --- | --- | --- |
| Sotto-campionare il contesto | Memoria e tempo calano più che linearmente | Sempre oltre 10.000 righe |
| Ridurre `n_estimators` | Meno membri nell'ensemble, tempo proporzionale | Nelle demo dal vivo |
| Ridurre `batch_size` | Meno membri elaborati insieme, meno memoria | In caso di errore out-of-memory |
| Predire a blocchi | Limita le righe di test per chiamata | Test set grandi |
| Disattivare `kv_cache` | Libera la memoria della cache | Quando non si ripetono predizioni |

I parametri `n_estimators`, `batch_size` e `kv_cache` sono quelli documentati da `tabicl` ([PyPI](https://pypi.org/project/tabicl/)).

## Piano B

- **Senza GPU:** E1 ed E2 girano su CPU. Per E3–E5 e il modulo 3 si riduce il contesto a 1.000–2.000 righe.
- **Senza rete o con Colab saturo:** notebook già eseguiti con gli output salvati, da commentare.
- **Con TabPFN al posto di TabICL:** la documentazione indica una GPU da circa 8 GB come sufficiente per molti casi ([GitHub](https://github.com/PriorLabs/TabPFN)). Licenza e token vanno sistemati prima della lezione.
