# Radar d'innovation automatisé : Ruptures technologiques en IA

Chaîne de veille automatisée, de la collecte multi-sources à la restitution d'un radar décisionnel. Elle sert de support à la partie technique du live « Définition du protocole de veille stratégique ».

```
config/protocole.yaml ──► collecte ──► stockage ──► détection ──► qualification ──► restitution ──► diffusion
     (cadrage)            (API)        (SQLite)    (G², indice)    (Claude + humain)  (radar, note)   (alerte)
                                                        ▲                                   │
                                                        └──────── rétroaction analyste ◄────┘
```

## Installation

```bash
python -m venv .venv && source .venv/bin/activate      # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q                                     # 17 tests
```

Variables d'environnement (toutes facultatives) :

| Variable | Rôle | Sans elle |
|---|---|---|
| `ANTHROPIC_API_KEY` | Qualification des sujets par Claude | Repli sur une qualification heuristique, signalée dans les livrables |
| `GITHUB_TOKEN` | Quota de l'API de recherche GitHub relevé (30 requêtes/min au lieu de 10) | Collecte plus lente (attente automatique sur quota) |
| `RADAR_WEBHOOK_URL` | Alerte Slack / Mattermost (webhook entrant) | Alerte affichée dans la console uniquement |

## Utilisation

```bash
python -m radar demo                     # démonstration hors ligne (jeu figé de 12 169 signaux réels)
python -m radar collect                  # collecte incrémentale (premier passage : 74 jours d'historique)
python -m radar analyze                  # détection, qualification, restitution
python -m radar run                      # collect + analyze : la commande à planifier
python -m radar clusters                 # émergence par clustering thématique
python -m radar feedback "decision models" bruit --analyst "J. Martin"
python -m radar stats                    # indicateurs de pilotage du dispositif
```

Options utiles : `--db chemin.db` (base SQLite), `--no-llm` (forcer l'heuristique), `--as-of 2026-10-01` (rejouer une date d'arrêté passée), `--protocol autre.yaml`.

## Livrables (répertoire `output/`)

| Fichier | Destinataire | Contenu |
|---|---|---|
| `radar.html` | CODIR | Radar visuel autonome (SVG), tableau de synthèse, fiches et preuves |
| `note-de-veille.md` | Direction technique | Note formelle : synthèse exécutive, mouvements, fiches, méthodologie et limites |
| `radar.json` | Outils internes | Export complet (intégration tableau de bord, base de connaissances) |
| `radar-zalando.json` | Équipe technique | Format d'entrée du [Zalando Tech Radar](https://github.com/zalando/tech-radar) |
| `radar-byor.csv` | Équipe technique | Format d'entrée de Thoughtworks [Build your own Radar](https://radar.thoughtworks.com/) |
| `clusters.md` | Analystes | Clusters thématiques : pics de volume, nouvelles organisations |

Le répertoire `output/` contient des livrables pré-générés à partir du jeu de démonstration (qualification heuristique), utilisables comme plan de secours pendant le live.

## Architecture du code

| Module | Responsabilité | Notion de cours |
|---|---|---|
| `config/protocole.yaml` | Le protocole de veille, versionné | Cadrage : KIT, KIQ, sources, cotation, seuils |
| `radar/config.py` | Chargement et validation du protocole | Fiabilité : un protocole incohérent ne s'exécute pas |
| `radar/models.py` | `Signal`, `Topic`, `RadarEntry` | Unité d'observation, dédoublonnage intra-source |
| `radar/collectors/` | arXiv, Hacker News, GitHub, RSS | Plan de sourcing, collecte éthique (API, quotas) |
| `radar/store.py` | SQLite : signaux, radars successifs, verdicts, journal | Mémoire longue, traçabilité |
| `radar/detect.py` | Fenêtres R/B, G² de Dunning, indice de rupture, contrôle de couverture | Des signaux faibles aux indicateurs mesurables |
| `radar/clusters.py` | TF-IDF + LSA + k-moyennes, pic de volume, nouvelles organisations | Émergence sans vocabulaire stabilisé |
| `radar/qualify.py` | Claude (sortie JSON contrainte) ou heuristique ; mouvements | Analyse assistée, sécurité, humain dans la boucle |
| `radar/render.py` | HTML/SVG, note Markdown, exports JSON/CSV | Restitution adaptée aux destinataires |
| `radar/notify.py` | Alerte sur mouvements significatifs | Diffusion « push » sobre |
| `.github/workflows/radar.yml` | Planification quotidienne et hebdomadaire | Industrialisation |

## Indice de rupture

Pour chaque terme candidat *t* (technologie suivie ou n-gramme découvert) :

```
IR(t) = Pertinence × Fiabilité × ( 0,35·Momentum + 0,25·Diffusion + 0,20·Impact + 0,20·Nouveauté )
```

| Indicateur | Calcul | Attribut d'émergence (Rotolo et al., 2015) |
|---|---|---|
| Momentum | ln(1 + G²₊) / ln(1 + G²max) | Croissance relativement rapide |
| Diffusion | types de sources distincts en R / 5 | Cohérence et convergence |
| Impact | centile moyen d'engagement (top 5, par source) | Impact prééminent |
| Nouveauté | n_R / (n_R + n_B) | Nouveauté radicale |
| Pertinence | part des preuves rattachées à un axe du protocole | (cadrage) |
| Fiabilité | cotation moyenne des sources des preuves | (qualité de l'information) |

Filtres appliqués aux termes découverts : au moins 5 documents en R, G² ≥ 10,83 (p < 0,001), au moins 2 émetteurs indépendants. Les sources dont l'historique ne couvre pas la moitié de la période de référence sont exclues du calcul (biais de troncature).

## Ajouter une source

1. Créer `radar/collectors/ma_source.py` avec une classe héritant de `Collector` et une méthode `collect(since) -> list[Signal]`.
2. L'enregistrer dans `REGISTRY` (`radar/collectors/__init__.py`), et son quota dans `RATE_LIMITS`.
3. Déclarer la source, son type et sa cotation de fiabilité dans `config/protocole.yaml`.
4. Vérifier les conditions d'utilisation de l'API et consigner la vérification dans le protocole.

Pistes : OpenAlex (`api.openalex.org`, bibliométrie et citations), Semantic Scholar, Espacenet / OPS de l'OEB (brevets), Product Hunt (lancements de produits), EUR-Lex (réglementation).

## Données de démonstration

`samples/signals_demo.jsonl.gz` contient 12 169 signaux réellement collectés le 7 octobre 2026 (période du 25 juillet au 7 octobre 2026) via les API publiques d'arXiv, Hacker News, GitHub et cinq flux RSS. Les résumés sont tronqués à 600 caractères. Ce jeu est réservé à un usage pédagogique ; les métadonnées arXiv sont diffusées sous licence CC0.
