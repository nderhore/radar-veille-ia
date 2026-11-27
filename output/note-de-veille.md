# Note de veille du radar d'innovation IA (arrêté au 2026-11-27)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 2564 signaux récents, 12843 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **Quantization 1-4 bits** (Agir, 0–6 mois) : Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?
- **Interpretability** (Agir, 0–6 mois) : Décider (KIQ-4.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : Agent-Native Desktop Experience, Github Copilot, Prompt injection
- Rapprochements du centre : aucun
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |
|---|---|---|---|---|---|---|---|---|
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.318 | stable |
| Quantization 1-4 bits | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.257 | stable |
| Interpretability | Confiance & Régulation | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.225 | stable |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.153 | stable |
| Prompt injection | Confiance & Régulation | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.141 | nouveau |
| AI Act | Confiance & Régulation | Préparer | 5 | incrémentale | 5/5 | 3/5 | 0.435 | stable |
| Speculative decoding | Infrastructure & Outillage | Préparer | 5 | incrémentale | 4/5 | 3/5 | 0.305 | stable |
| Computer use | Agents & Applications | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.222 | stable |
| On-device AI | Infrastructure & Outillage | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.209 | stable |
| Ai--Manus2 Ai Manus | Modèles & Techniques | Explorer | 4 | radicale | 5/5 | 2/5 | 0.470 | stable |
| Agent-Native Desktop Experience | Agents & Applications | Explorer | 4 | radicale | 5/5 | 2/5 | 0.437 | nouveau |
| Finding Running Steering | Agents & Applications | Explorer | 4 | radicale | 5/5 | 2/5 | 0.437 | stable |
| Github Repositories | Agents & Applications | Explorer | 4 | radicale | 5/5 | 2/5 | 0.437 | stable |
| Github Copilot | Agents & Applications | Explorer | 4 | radicale | 5/5 | 2/5 | 0.437 | nouveau |
| Weight-Space Programming | Modèles & Techniques | Explorer | 4 | incrémentale | 4/5 | 3/5 | 0.492 | stable |

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

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 70 documents récents contre 279 sur la période de référence : sujet en progression (G² = 2.9, non significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/erkamyaman/rust-anything>
- <https://github.com/bookwjitchieni1986/blender-ai-mcp-addon>
- <https://github.com/nexu-io/opengame>
- <https://github.com/erkamyaman/safe-anything>
- <https://github.com/w01fb0ss/PiBot>

### Quantization 1-4 bits

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 63 documents récents contre 383 sur la période de référence : sujet stable (G² = -2.2). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/sybil-solutions/inference-optimisation-skill>
- <https://arxiv.org/abs/2611.34924>
- <https://github.com/manuelgscom/inside-llm>
- <https://arxiv.org/abs/2506.13771>
- <https://github.com/hiruhiru2005/sync-strata>

### Interpretability

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 32 documents récents contre 145 sur la période de référence : sujet en progression (G² = 0.3, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://github.com/manuelgscom/inside-llm>
- <http://arxiv.org/abs/2611.34930v1>
- <http://arxiv.org/abs/2611.34158v1>
- <http://arxiv.org/abs/2611.34019v1>
- <http://arxiv.org/abs/2611.33966v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 36 documents récents contre 223 sur la période de référence : sujet stable (G² = -1.5). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/ntu0831/RAG-MCP-Server>
- <https://github.com/yzsind/mydb>
- <https://github.com/harshabolla/genai-agentic-ai-interview-questions>
- <http://arxiv.org/abs/2611.34762v1>
- <http://arxiv.org/abs/2611.34188v1>

### Prompt injection

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 32 documents récents contre 188 sur la période de référence : sujet stable (G² = -0.7). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**KIQ adressées.** KIQ-4.2 : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**Preuves.**
- <https://github.com/1276486/ZERO-X-Bypass-Jailbreak>
- <https://github.com/tjcrims0nx/OpenMind-Jailbreak-Lab>
- <http://arxiv.org/abs/2611.34278v1>
- <http://arxiv.org/abs/2611.34188v1>
- <http://arxiv.org/abs/2611.34121v1>

### AI Act

*Confiance & Régulation, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 70 documents récents contre 54 sur la période de référence : sujet en forte accélération (G² = 102.0, significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Expérimenter (KIQ-4.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### Speculative decoding

*Infrastructure & Outillage, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 29 documents récents contre 94 sur la période de référence : sujet en progression (G² = 3.9, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Expérimenter (KIQ-3.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/sybil-solutions/inference-optimisation-skill>
- <https://github.com/enwove/flyx>
- <http://arxiv.org/abs/2611.34492v1>
- <http://arxiv.org/abs/2611.34092v1>
- <http://arxiv.org/abs/2611.33985v1>

### Computer use

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 17 documents récents contre 97 sur la période de référence : sujet stable (G² = -0.2). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/w01fb0ss/PiBot>
- <https://openai.com/index/advancing-computer-use-for-healthcare-teams/>
- <https://github.com/seira-bot/seira>
- <https://retrocomputing.stackexchange.com/questions/12158/did-the-apollo-guidance-computer-really-use-60-of-the-worlds-ics-in-1963>
- <https://blog.mozilla.org/addons/2026/11/20/developer-spotlight-webbrain/>

### On-device AI

*Infrastructure & Outillage, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 26 documents récents contre 109 sur la période de référence : sujet en progression (G² = 0.7, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Expérimenter (KIQ-3.2) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <https://github.com/sybil-solutions/inference-optimisation-skill>
- <https://github.com/shani-hamer/riverse-ai-agent>
- <https://github.com/hiruhiru2005/sync-strata>
- <https://github.com/enwove/flyx>
- <https://github.com/aether-aiagent/aether>

### Ai--Manus2 Ai Manus

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 43 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 154.8, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### Agent-Native Desktop Experience

*Agents & Applications, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 18 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 64.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Approfondir (KIQ-2.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/trackersnailgrip/GitHub-Copilot-app>
- <https://github.com/trackboatwrightplan/GitHub-Copilot-app>
- <https://github.com/toppatronweave/GitHub-Copilot-app>
- <https://github.com/TrapBladesmith/GitHub-Copilot-app>
- <https://github.com/TurquoiseConsultant/GitHub-Copilot-app>

### Finding Running Steering

*Agents & Applications, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 18 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 64.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Approfondir (KIQ-2.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/trackersnailgrip/GitHub-Copilot-app>
- <https://github.com/trackboatwrightplan/GitHub-Copilot-app>
- <https://github.com/toppatronweave/GitHub-Copilot-app>
- <https://github.com/TrapBladesmith/GitHub-Copilot-app>
- <https://github.com/TurquoiseConsultant/GitHub-Copilot-app>

### Github Repositories

*Agents & Applications, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 18 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 64.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Approfondir (KIQ-2.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/trackersnailgrip/GitHub-Copilot-app>
- <https://github.com/trackboatwrightplan/GitHub-Copilot-app>
- <https://github.com/toppatronweave/GitHub-Copilot-app>
- <https://github.com/TrapBladesmith/GitHub-Copilot-app>
- <https://github.com/TurquoiseConsultant/GitHub-Copilot-app>

### Github Copilot

*Agents & Applications, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 18 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 64.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Approfondir (KIQ-2.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/trackersnailgrip/GitHub-Copilot-app>
- <https://github.com/trackboatwrightplan/GitHub-Copilot-app>
- <https://github.com/toppatronweave/GitHub-Copilot-app>
- <https://github.com/TrapBladesmith/GitHub-Copilot-app>
- <https://github.com/TurquoiseConsultant/GitHub-Copilot-app>

### Weight-Space Programming

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 15 documents récents contre 7 sur la période de référence : sujet en forte accélération (G² = 28.9, significatif). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://tabbyml.github.io/weight-space-playground/>
- <http://arxiv.org/abs/2611.33031v1>
- <http://arxiv.org/abs/2611.31233v1>
- <http://arxiv.org/abs/2611.27425v1>
- <http://arxiv.org/abs/2611.27089v1>

## 5. Méthodologie et limites

- Fenêtre récente : 14 jours ; fenêtre de référence : 60 jours.
- Seuils : fréquence ≥ 5 documents, G² ≥ 10.83 (sujets découverts).
- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : momentum 0.35, diffusion 0.25, impact 0.2, nouveaute 0.2.
- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.
