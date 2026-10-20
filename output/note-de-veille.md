# Note de veille du radar d'innovation IA (arrêté au 2026-10-20)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 3068 signaux récents, 10040 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **Prompt injection** (Agir, 0–6 mois) : Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?
- **On-device AI** (Agir, 0–6 mois) : Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : Diffusion LLM, Mixture of Experts, Agent-to-Agent (A2A)
- Rapprochements du centre : aucun
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |
|---|---|---|---|---|---|---|---|---|
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.380 | stable |
| Prompt injection | Confiance & Régulation | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.289 | stable |
| On-device AI | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 4/5 | 0.289 | stable |
| Quantization 1-4 bits | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.235 | stable |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.204 | stable |
| Coding Agents | Agents & Applications | Préparer | 5 | incrémentale | 5/5 | 3/5 | 0.487 | stable |
| Ai Coding | Agents & Applications | Préparer | 5 | incrémentale | 4/5 | 3/5 | 0.421 | stable |
| Agent S | Agents & Applications | Préparer | 5 | radicale | 3/5 | 3/5 | 0.533 | stable |
| Computer use | Agents & Applications | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.303 | stable |
| Decision Models | Modèles & Techniques | Explorer | 4 | incrémentale | 3/5 | 3/5 | 0.571 | stable |
| World Models | Modèles & Techniques | Explorer | 4 | incrémentale | 2/5 | 3/5 | 0.159 | stable |
| Agent-to-Agent (A2A) | Agents & Applications | Explorer | 4 | incrémentale | 1/5 | 3/5 | 0.124 | nouveau |
| Diffusion LLM | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.181 | nouveau |
| Mixture of Experts | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 3/5 | 0.130 | nouveau |
| Small Language Models | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.130 | stable |

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

### Model Context Protocol

*Agents & Applications, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 67 documents récents contre 173 sur la période de référence : sujet en progression (G² = 3.8, non significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/Leonxlnx/earshot>
- <https://github.com/LiCinCan/blender-ai-mcp-addon>
- <https://github.com/cranebeaker/coop-anything>
- <https://github.com/i12bp8/decomp.wtf>
- <https://github.com/finereli/whatsapp-mcp>

### Prompt injection

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 40 documents récents contre 180 sur la période de référence : sujet stable (G² = -2.6). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**KIQ adressées.** KIQ-4.2 : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**Preuves.**
- <https://github.com/onehumanbeing/esp32-iphone-agent>
- <https://github.com/AndreSzymanski15/ai-jailbreaks>
- <https://www.signalscorps.com/blog/prompt-injection-in-http-headers/>
- <http://arxiv.org/abs/2610.26595v1>
- <http://arxiv.org/abs/2610.26438v1>

### On-device AI

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 28 documents récents contre 103 sur la période de référence : sujet stable (G² = -0.1). Présent dans : recherche, code ouvert, communauté, presse ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <https://llmspeed.dev/>
- <https://www.liquid.ai/blog/lfm2-5-24b-a2b>
- <https://www.xda-developers.com/im-not-paying-20-for-chatgpt-claude-or-gemini-because-a-free-local-llm-does-everything-i-need/>
- <https://github.com/ja1chen/actell>
- <https://github.com/scs0209/laya-guard>

### Quantization 1-4 bits

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 81 documents récents contre 346 sur la période de référence : sujet stable (G² = -3.4). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/justxor/deepseek-local-guide-ru>
- <http://arxiv.org/abs/2610.26102v1>
- <http://arxiv.org/abs/2610.25982v1>
- <http://arxiv.org/abs/2610.25460v1>
- <http://arxiv.org/abs/2610.25048v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 51 documents récents contre 257 sur la période de référence : sujet stable (G² = -7.0). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/justxor/deepseek-local-guide-ru>
- <https://github.com/jaikydota/BullFlow>
- <https://github.com/RayenMlayeh/jevcrawl>
- <https://github.com/liaosiliangCodeLife/harness-mate-plat>
- <https://bart.degoe.de/rag-with-a-small-language-model-in-the-browser/>

### Coding Agents

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 52 documents récents contre 96 sur la période de référence : sujet en forte accélération (G² = 12.2, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/Leonxlnx/earshot>
- <https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/>
- <https://www.cockroachlabs.com/blog/experiment-running-hospital-code/>
- <https://github.com/christos-antono/NPCTalk>
- <https://mtlynch.io/why-are-coding-agents-so-dumb/>

### Ai Coding

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 19 documents récents contre 16 sur la période de référence : sujet en forte accélération (G² = 16.6, significatif). Présent dans : code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/>
- <https://github.com/christos-antono/NPCTalk>
- <https://github.com/JinHo-von-Choi/anti-samcheonpo>
- <https://github.com/vakandi/opencode-rust>
- <https://github.com/huacnlee/gpui-shell-benchs>

### Agent S

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 6 documents récents contre 1 sur la période de référence : sujet en forte accélération (G² = 12.6, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/mrsarac/ff-tracking>
- <https://kairos-experiment.com/checks.html>
- <http://arxiv.org/abs/2610.22779v1>
- <http://arxiv.org/abs/2610.20195v1>
- <http://arxiv.org/abs/2610.08722v1>

### Computer use

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 28 documents récents contre 77 sur la période de référence : sujet en progression (G² = 1.0, non significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/onehumanbeing/esp32-iphone-agent>
- <https://github.com/touri-ai/touri>
- <https://github.com/tony3liu/eido>
- <https://news.ycombinator.com/item?id=50016052>
- <http://arxiv.org/abs/2610.26828v1>

### Decision Models

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 16 documents récents contre 10 sur la période de référence : sujet en forte accélération (G² = 18.1, significatif). Présent dans : recherche, communauté, presse ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://opper.ai/jevman-benchmark/>
- <https://news.ycombinator.com/item?id=50072702>
- <http://arxiv.org/abs/2610.26035v1>
- <http://arxiv.org/abs/2610.25947v1>
- <http://arxiv.org/abs/2610.24929v1>

### World Models

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 33 documents récents contre 126 sur la période de référence : sujet stable (G² = -0.3). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/Gen-Verse/RSI-Anything>
- <http://arxiv.org/abs/2610.26844v1>
- <http://arxiv.org/abs/2610.26828v1>
- <http://arxiv.org/abs/2610.25959v1>
- <http://arxiv.org/abs/2610.23344v1>

### Agent-to-Agent (A2A)

*Agents & Applications, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 6 documents récents contre 25 sur la période de référence : sujet stable (G² = -0.2). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Approfondir (KIQ-2.2) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://arstechnica.com/security/2026/10/vulnerability-in-agents-from-google-and-others-exposes-structural-flaw-in-mcp/>
- <http://arxiv.org/abs/2610.21538v1>
- <http://arxiv.org/abs/2610.19818v1>
- <http://arxiv.org/abs/2610.19342v2>
- <http://arxiv.org/abs/2610.19342v1>

### Diffusion LLM

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 16 documents récents contre 37 sur la période de référence : sujet en progression (G² = 1.6, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.26693v1>
- <http://arxiv.org/abs/2610.26040v1>
- <http://arxiv.org/abs/2610.25932v1>
- <http://arxiv.org/abs/2610.24722v1>
- <http://arxiv.org/abs/2610.24717v1>

### Mixture of Experts

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 51 documents récents contre 165 sur la période de référence : sujet en progression (G² = 0.1, non significatif). Présent dans : recherche, presse ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.26754v1>
- <http://arxiv.org/abs/2610.26370v1>
- <http://arxiv.org/abs/2610.25999v1>
- <http://arxiv.org/abs/2610.25991v1>
- <http://arxiv.org/abs/2610.25791v1>

### Small Language Models

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 26 documents récents contre 74 sur la période de référence : sujet en progression (G² = 0.7, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.2) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quand un petit modèle (< 10 Md de paramètres) atteindra-t-il le niveau de nos modèles actuels ?

**KIQ adressées.** KIQ-1.2 : Quand un petit modèle (< 10 Md de paramètres) atteindra-t-il le niveau de nos modèles actuels ?

**Preuves.**
- <http://arxiv.org/abs/2610.26013v1>
- <http://arxiv.org/abs/2610.25516v1>
- <http://arxiv.org/abs/2610.25458v1>
- <http://arxiv.org/abs/2610.24818v1>
- <http://arxiv.org/abs/2610.22906v1>

## 5. Méthodologie et limites

- Fenêtre récente : 14 jours ; fenêtre de référence : 60 jours.
- Seuils : fréquence ≥ 5 documents, G² ≥ 10.83 (sujets découverts).
- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : momentum 0.35, diffusion 0.25, impact 0.2, nouveaute 0.2.
- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.
