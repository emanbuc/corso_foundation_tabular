# Corso Tabular Foundation Model

Materiale didattico per due corsi sui Tabular Foundation Model (TFM), con il sito del corso pubblicato su GitHub Pages.

| Corso | Durata | Cosa si fa | Prerequisiti |
| --- | --- | --- | --- |
| **1 · Usare un TFM** | 4 ore | Si usa un TFM pre-addestrato (TabICLv2) per classificazione e regressione e lo si confronta con il gradient boosting | Python, pandas, scikit-learn di base |
| **2 · Costruire un TFM** | 6 ore | Si scrive da zero un piccolo TFM: prior, transformer, ciclo di addestramento | Corso 1, PyTorch di base |

## Struttura del repository

```
.
├── docs/                    # Pagine del sito (Markdown)
│   ├── index.md             # Home
│   ├── usare-tfm/           # Corso 1: una pagina per modulo
│   ├── costruire-tfm/       # Corso 2: una pagina per modulo
│   └── javascripts/         # Configurazione MathJax per le formule
├── notebooks/               # Notebook Colab dei laboratori
│   ├── usare-tfm/
│   └── costruire-tfm/
├── src/costruire_tfm/       # File prodotti nei laboratori del corso 2 e relative soluzioni
├── mkdocs.yml               # Configurazione e menu del sito
├── requirements.txt         # Dipendenze per generare il sito
└── .github/workflows/pages.yml   # Pubblicazione automatica su GitHub Pages
```

## Anteprima del sito in locale

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
```

`mkdocs build --strict` genera il sito in `site/` e fallisce se ci sono link interni rotti.

## Pubblicazione su GitHub Pages

1. Creare un repository vuoto su GitHub e collegarlo:

   ```bash
   git remote add origin https://github.com/<utente>/<repository>.git
   git push -u origin main
   ```

2. Su GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. In `mkdocs.yml` togliere il commento a `site_url`, `repo_url` e `repo_name` e inserire i valori reali.

A ogni push su `main` il workflow `.github/workflows/pages.yml` rigenera e pubblica il sito su `https://<utente>.github.io/<repository>/`.

## Aggiungere o modificare contenuti

- Ogni pagina del sito è un file Markdown in `docs/`. Il menu è definito nella sezione `nav` di `mkdocs.yml`.
- Le formule si scrivono in LaTeX tra `$$ ... $$` (blocco) o `$ ... $` (in linea).
- I notebook vanno in `notebooks/<corso>/` con i nomi indicati nei rispettivi `README.md`.
