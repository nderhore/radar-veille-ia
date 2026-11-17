# Note de veille du radar d'innovation IA (arrêté au 2026-11-17)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 2342 signaux récents, 12279 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **On-device AI** (Agir, 0–6 mois) : Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?
- **Quantization 1-4 bits** (Agir, 0–6 mois) : Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : Various Tools, Running Various, Supports Running, Speculative decoding
- Rapprochements du centre : On-device AI
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |
|---|---|---|---|---|---|---|---|---|
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.359 | stable |
| On-device AI | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 4/5 | 0.328 | rapproché du centre |
| Quantization 1-4 bits | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.220 | stable |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.195 | stable |
| Interpretability | Confiance & Régulation | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.210 | stable |
| General-Purpose Ai Agent | Modèles & Techniques | Préparer | 5 | radicale | 4/5 | 3/5 | 0.496 | stable |
| AI Act | Confiance & Régulation | Préparer | 5 | incrémentale | 4/5 | 3/5 | 0.461 | stable |
| Computer use | Agents & Applications | Préparer | 5 | incrémentale | 4/5 | 3/5 | 0.241 | stable |
| Speculative decoding | Infrastructure & Outillage | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.223 | nouveau |
| Various Tools | Modèles & Techniques | Explorer | 4 | radicale | 4/5 | 2/5 | 0.464 | nouveau |
| Sandbox Environment | Modèles & Techniques | Explorer | 4 | radicale | 4/5 | 2/5 | 0.464 | stable |
| Ai Manus | Modèles & Techniques | Explorer | 4 | radicale | 4/5 | 2/5 | 0.464 | stable |
| Running Various | Modèles & Techniques | Explorer | 4 | radicale | 4/5 | 2/5 | 0.464 | nouveau |
| Supports Running | Modèles & Techniques | Explorer | 4 | radicale | 4/5 | 2/5 | 0.464 | nouveau |
| Mixture of Experts | Modèles & Techniques | Explorer | 4 | incrémentale | 3/5 | 3/5 | 0.198 | stable |

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

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 73 documents récents contre 250 sur la période de référence : sujet en forte accélération (G² = 11.6, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/hitkeeen/blender-ai-mcp-addon>
- <https://github.com/andrew-babo/muse4ai>
- <https://github.com/agentes-chat/agentes-chat>
- <https://github.com/JosssphZhou/poki>
- <https://github.com/credoksopho1984/blender-ai-copilot-studio>

### On-device AI

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 23 documents récents contre 109 sur la période de référence : sujet en progression (G² = 0.4, non significatif). Présent dans : recherche, code ouvert, communauté, presse ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <https://github.com/sybil-solutions/inference-optimisation-skill>
- <https://github.com/sdalberto/ia-da-sobrevivencia/blob/main/README.en.md>
- <http://arxiv.org/abs/2611.21178v1>
- <http://arxiv.org/abs/2611.21053v1>
- <http://arxiv.org/abs/2611.20686v1>

### Quantization 1-4 bits

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 55 documents récents contre 382 sur la période de référence : sujet stable (G² = -3.0). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/sybil-solutions/inference-optimisation-skill>
- <https://github.com/huawei-csl/MACaQ>
- <https://github.com/manuelgscom/inside-llm>
- <http://arxiv.org/abs/2611.21584v1>
- <http://arxiv.org/abs/2611.21303v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 26 documents récents contre 242 sur la période de référence : sujet stable (G² = -7.8). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/pnyn96/mindact-agent>
- <http://arxiv.org/abs/2611.20261v1>
- <http://arxiv.org/abs/2611.20045v1>
- <http://arxiv.org/abs/2611.20012v1>
- <http://arxiv.org/abs/2611.19900v1>

### Interpretability

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 31 documents récents contre 151 sur la période de référence : sujet en progression (G² = 0.3, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://github.com/manuelgscom/inside-llm>
- <http://arxiv.org/abs/2611.21449v1>
- <http://arxiv.org/abs/2611.21348v1>
- <http://arxiv.org/abs/2611.21175v1>
- <http://arxiv.org/abs/2611.20835v1>

### General-Purpose Ai Agent

*Modèles & Techniques, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 91 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 343.0, significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Expérimenter (KIQ-1.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### AI Act

*Confiance & Régulation, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 92 documents récents contre 23 sur la période de référence : sujet en forte accélération (G² = 239.2, significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Expérimenter (KIQ-4.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### Computer use

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 7 documents récents contre 100 sur la période de référence : sujet stable (G² = -8.1). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/agentes-chat/agentes-chat>
- <https://retrocomputing.stackexchange.com/questions/12158/did-the-apollo-guidance-computer-really-use-60-of-the-worlds-ics-in-1963>
- <http://arxiv.org/abs/2611.18562v1>
- <http://arxiv.org/abs/2611.16107v1>
- <http://arxiv.org/abs/2611.14766v1>

### Speculative decoding

*Infrastructure & Outillage, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 20 documents récents contre 88 sur la période de référence : sujet en progression (G² = 0.7, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Expérimenter (KIQ-3.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/sybil-solutions/inference-optimisation-skill>
- <https://github.com/inclusionAI/ASpec>
- <http://arxiv.org/abs/2611.21003v1>
- <http://arxiv.org/abs/2611.20771v1>
- <http://arxiv.org/abs/2611.20565v1>

### Various Tools

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 90 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 339.2, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### Sandbox Environment

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 90 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 339.2, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### Ai Manus

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 90 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 339.2, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### Running Various

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 90 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 339.2, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### Supports Running

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 90 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 339.2, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/topapothecarycanal/ai--manus2.0>
- <https://github.com/toppatronweave/ai--manus2.0>
- <https://github.com/topconstableinlet67/ai--manus2.0>
- <https://github.com/violetkomodolimit/ai--manus2.0>
- <https://github.com/trackersnailgrip/ai--manus2.0>

### Mixture of Experts

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 38 documents récents contre 199 sur la période de référence : sujet en progression (G² = 0.1, non significatif). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://www.silasdata.com/llm-playground-inside-architectures/>
- <http://arxiv.org/abs/2611.21072v1>
- <http://arxiv.org/abs/2611.21003v1>
- <http://arxiv.org/abs/2611.20663v1>
- <http://arxiv.org/abs/2611.20419v1>

## 5. Méthodologie et limites

- Fenêtre récente : 14 jours ; fenêtre de référence : 60 jours.
- Seuils : fréquence ≥ 5 documents, G² ≥ 10.83 (sujets découverts).
- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : momentum 0.35, diffusion 0.25, impact 0.2, nouveaute 0.2.
- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.
