# Note de veille du radar d'innovation IA (arrêté au 2026-10-15)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 3213 signaux récents, 9822 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Prompt injection** (Agir, 0–6 mois) : Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?
- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **On-device AI** (Agir, 0–6 mois) : Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : Verifiable Rewards
- Rapprochements du centre : aucun
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |
|---|---|---|---|---|---|---|---|---|
| Prompt injection | Confiance & Régulation | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.265 | stable |
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.244 | stable |
| On-device AI | Infrastructure & Outillage | Agir | 7 | incrémentale | 3/5 | 4/5 | 0.272 | stable |
| Mixture of Experts | Modèles & Techniques | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.229 | stable |
| Quantization 1-4 bits | Infrastructure & Outillage | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.207 | stable |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.176 | stable |
| Ai Coding | Agents & Applications | Préparer | 5 | incrémentale | 4/5 | 3/5 | 0.427 | stable |
| Computer use | Agents & Applications | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.263 | stable |
| Decision Models | Modèles & Techniques | Explorer | 4 | incrémentale | 4/5 | 3/5 | 0.593 | stable |
| About Ai | Confiance & Régulation | Explorer | 4 | radicale | 3/5 | 3/5 | 0.466 | stable |
| World Models | Modèles & Techniques | Explorer | 4 | incrémentale | 2/5 | 3/5 | 0.169 | stable |
| Verifiable Rewards | Agents & Applications | Surveiller | 3 | radicale | 1/5 | 2/5 | 0.409 | nouveau |
| Small Language Models | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.239 | stable |
| Diffusion LLM | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.209 | stable |
| Watermarking | Confiance & Régulation | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.179 | stable |

Lecture des colonnes :

- **Quadrant** : axe de surveillance (KIT) auquel le sujet se rattache.
- **Anneau** : horizon de décision (Agir 0–6 mois, Préparer 6–18 mois, Explorer 18–36 mois, Surveiller > 36 mois), et non note de qualité.
- **TRL** : maturité technologique de 1 à 9 (ISO 16290), estimée d'après les types de sources.
- **Type** : incrémentale (améliore l'existant), radicale (approche nouvelle), rupture (modifie le marché).
- **Impact** : écho chez les praticiens, mesuré par l'engagement (étoiles, points).
- **Confiance** : solidité du constat, croissante avec la diversité des types de sources.
- **Indice** : indice de rupture entre 0 et 1, qui sert à trier les sujets d'un même radar.
- **Mouvement** : évolution de l'anneau depuis le radar précédent.

## 4. Fiches d'analyse

### Prompt injection

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 42 documents récents contre 175 sur la période de référence : sujet stable (G² = -2.8). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**KIQ adressées.** KIQ-4.2 : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**Preuves.**
- <https://github.com/onehumanbeing/esp32-iphone-agent>
- <http://arxiv.org/abs/2610.19971v1>
- <http://arxiv.org/abs/2610.19587v1>
- <http://arxiv.org/abs/2610.19422v1>
- <http://arxiv.org/abs/2610.19372v1>

### Model Context Protocol

*Agents & Applications, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 52 documents récents contre 176 sur la période de référence : sujet stable (G² = -0.2). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/i12bp8/decomp.wtf>
- <https://github.com/arielshad/3d-asset-server>
- <https://github.com/LingCore/WinShun>
- <https://github.com/sepehr071/awesome-iran-mcp>
- <https://github.com/mcpdelta/mcpdelta>

### On-device AI

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 24 documents récents contre 106 sur la période de référence : sujet stable (G² = -2.4). Présent dans : recherche, code ouvert, communauté, presse ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <https://www.liquid.ai/blog/lfm2-5-24b-a2b>
- <https://www.xda-developers.com/im-not-paying-20-for-chatgpt-claude-or-gemini-because-a-free-local-llm-does-everything-i-need/>
- <https://github.com/ja1chen/actell>
- <https://github.com/scs0209/laya-guard>
- <http://arxiv.org/abs/2610.20136v1>

### Mixture of Experts

*Modèles & Techniques, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 56 documents récents contre 165 sur la période de référence : sujet en progression (G² = 0.2, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Décider (KIQ-1.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/Yamz-Labs/kyojin>
- <http://arxiv.org/abs/2610.20418v1>
- <http://arxiv.org/abs/2610.20399v1>
- <http://arxiv.org/abs/2610.20353v1>
- <http://arxiv.org/abs/2610.19423v1>

### Quantization 1-4 bits

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 98 documents récents contre 340 sur la période de référence : sujet stable (G² = -0.7). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/Yamz-Labs/kyojin>
- <http://arxiv.org/abs/2610.20353v1>
- <http://arxiv.org/abs/2610.20303v1>
- <http://arxiv.org/abs/2610.20136v1>
- <http://arxiv.org/abs/2610.19901v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 46 documents récents contre 263 sur la période de référence : sujet en recul relatif (G² = -16.0) : sujet probablement banalisé, à vérifier avant tout investissement. Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/RayenMlayeh/jevcrawl>
- <https://github.com/liaosiliangCodeLife/harness-mate-plat>
- <https://bart.degoe.de/rag-with-a-small-language-model-in-the-browser/>
- <http://arxiv.org/abs/2610.20067v1>
- <http://arxiv.org/abs/2610.19830v1>

### Ai Coding

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 17 documents récents contre 15 sur la période de référence : sujet en forte accélération (G² = 12.5, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/>
- <https://github.com/JinHo-von-Choi/anti-samcheonpo>
- <https://github.com/vakandi/opencode-rust>
- <https://github.com/huacnlee/gpui-shell-benchs>
- <https://github.com/ringozzt/rea-research>

### Computer use

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 27 documents récents contre 72 sur la période de référence : sujet en progression (G² = 0.6, non significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/onehumanbeing/esp32-iphone-agent>
- <https://github.com/tony3liu/eido>
- <https://news.ycombinator.com/item?id=50016052>
- <https://github.com/ironbee-ai/ironbee-express>
- <http://arxiv.org/abs/2610.20584v1>

### Decision Models

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 15 documents récents contre 6 sur la période de référence : sujet en forte accélération (G² = 21.0, significatif). Présent dans : recherche, communauté, presse ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://blog.cloudflare.com/clef-decision-models/>
- <https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails>
- <https://opper.ai/jevman-benchmark/>
- <https://news.ycombinator.com/item?id=50072702>
- <http://arxiv.org/abs/2610.19536v1>

### About Ai

*Confiance & Régulation, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 6 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 17.1, significatif). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Approfondir (KIQ-4.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://fortune.com/2026/10/01/ai-godfather-yann-lecun-has-zero-concerns-about-human-extinction-says-anthropic-ceo-dario-amodei-is-deuded/>
- <https://deadsimpletech.com/blog/llms-arent-inevitable>
- <https://jesserichardson78.medium.com/calculate-your-probability-of-doom-6bd18de3e0e4>
- <https://news.ycombinator.com/item?id=49973382>
- <https://aihub.remakelearning.org/>

### World Models

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 39 documents récents contre 124 sur la période de référence : sujet stable (G² = -0.0). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/Gen-Verse/RSI-Anything>
- <http://arxiv.org/abs/2610.19955v1>
- <http://arxiv.org/abs/2610.19795v1>
- <http://arxiv.org/abs/2610.18305v1>
- <http://arxiv.org/abs/2610.18082v1>

### Verifiable Rewards

*Agents & Applications, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 6 documents récents contre 1 sur la période de référence : sujet en forte accélération (G² = 11.9, significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Surveiller (KIQ-2.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <http://arxiv.org/abs/2610.20413v1>
- <http://arxiv.org/abs/2610.19868v1>
- <http://arxiv.org/abs/2610.16533v1>
- <http://arxiv.org/abs/2610.15888v1>
- <http://arxiv.org/abs/2610.12598v1>

### Small Language Models

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 32 documents récents contre 65 sur la période de référence : sujet en progression (G² = 4.0, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.2) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quand un petit modèle (< 10 Md de paramètres) atteindra-t-il le niveau de nos modèles actuels ?

**KIQ adressées.** KIQ-1.2 : Quand un petit modèle (< 10 Md de paramètres) atteindra-t-il le niveau de nos modèles actuels ?

**Preuves.**
- <http://arxiv.org/abs/2610.19928v1>
- <http://arxiv.org/abs/2610.19439v1>
- <http://arxiv.org/abs/2610.19382v1>
- <http://arxiv.org/abs/2610.19169v1>
- <http://arxiv.org/abs/2610.18624v1>

### Diffusion LLM

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 17 documents récents contre 33 sur la période de référence : sujet en progression (G² = 2.5, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.19855v1>
- <http://arxiv.org/abs/2610.19053v1>
- <http://arxiv.org/abs/2610.17917v1>
- <http://arxiv.org/abs/2610.17868v1>
- <http://arxiv.org/abs/2610.17780v1>

### Watermarking

*Confiance & Régulation, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 16 documents récents contre 34 sur la période de référence : sujet en progression (G² = 1.6, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Surveiller (KIQ-4.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <http://arxiv.org/abs/2610.18359v1>
- <http://arxiv.org/abs/2610.17810v1>
- <http://arxiv.org/abs/2610.17655v1>
- <http://arxiv.org/abs/2610.15976v1>
- <http://arxiv.org/abs/2610.15725v1>

## 5. Méthodologie et limites

- Fenêtre récente : 14 jours ; fenêtre de référence : 60 jours.
- Seuils : fréquence ≥ 5 documents, G² ≥ 10.83 (sujets découverts).
- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : momentum 0.35, diffusion 0.25, impact 0.2, nouveaute 0.2.
- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.
