# Note de veille du radar d'innovation IA (arrêté au 2026-11-09)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 2520 signaux récents, 11930 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **On-device AI** (Agir, 0–6 mois) : Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?
- **Prompt injection** (Agir, 0–6 mois) : Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : AI Act, Sandbox Environment, Running Various Tools, Ai Manus, Supports Running, General-Purpose Ai Agent, Ai-Manus Ai
- Rapprochements du centre : aucun
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |
|---|---|---|---|---|---|---|---|---|
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.398 | stable |
| On-device AI | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 4/5 | 0.295 | stable |
| Prompt injection | Confiance & Régulation | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.278 | stable |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.187 | stable |
| Mixture of Experts | Modèles & Techniques | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.213 | stable |
| AI Act | Confiance & Régulation | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.441 | nouveau |
| Speculative decoding | Infrastructure & Outillage | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.212 | stable |
| Agent-to-Agent (A2A) | Agents & Applications | Préparer | 5 | incrémentale | 2/5 | 3/5 | 0.173 | stable |
| Computer use | Agents & Applications | Préparer | 5 | incrémentale | 2/5 | 3/5 | 0.141 | stable |
| Sandbox Environment | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.433 | nouveau |
| Running Various Tools | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.433 | nouveau |
| Ai Manus | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.433 | nouveau |
| Supports Running | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.433 | nouveau |
| General-Purpose Ai Agent | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.433 | nouveau |
| Ai-Manus Ai | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.404 | nouveau |

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

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 74 documents récents contre 220 sur la période de référence : sujet en forte accélération (G² = 13.3, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/andrew-babo/muse4ai>
- <https://github.com/JosssphZhou/poki>
- <https://github.com/Balanov/shim>
- <https://github.com/HerdBuilderEstimate/roblox-studio-mcp>
- <https://github.com/shanselman/sandbox-mcp>

### On-device AI

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 13 documents récents contre 105 sur la période de référence : sujet stable (G² = -3.2). Présent dans : recherche, code ouvert, communauté, presse ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <https://github.com/wangzan101/Mika>
- <https://github.com/sdalberto/ia-da-sobrevivencia/blob/main/README.en.md>
- <https://huggingface.co/blog/phonon-tts>
- <http://arxiv.org/abs/2611.04797v1>
- <http://arxiv.org/abs/2611.02601v1>

### Prompt injection

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 41 documents récents contre 180 sur la période de référence : sujet en progression (G² = 0.4, non significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**KIQ adressées.** KIQ-4.2 : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**Preuves.**
- <https://github.com/JosssphZhou/poki>
- <https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/>
- <https://github.com/codexlx/contextshield>
- <http://arxiv.org/abs/2611.09734v1>
- <http://arxiv.org/abs/2611.08811v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 41 documents récents contre 249 sur la période de référence : sujet stable (G² = -1.6). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/wanghao-SunSky/cs329z-chinese>
- <https://github.com/pnyn96/mindact-agent>
- <https://github.com/glincker/awesome-selfhosted-ai>
- <https://github.com/pwnedlabs/ai-security-labs>
- <https://github.com/harrytted/ai-agent-interview-playbook>

### Mixture of Experts

*Modèles & Techniques, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 41 documents récents contre 187 sur la période de référence : sujet en progression (G² = 0.2, non significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Décider (KIQ-1.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/ZhuLinsen/LiteMoE>
- <https://www.silasdata.com/llm-playground-inside-architectures/>
- <http://arxiv.org/abs/2611.07654v1>
- <http://arxiv.org/abs/2611.07149v1>
- <http://arxiv.org/abs/2611.07093v1>

### AI Act

*Confiance & Régulation, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 36 documents récents contre 20 sur la période de référence : sujet en forte accélération (G² = 62.9, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Expérimenter (KIQ-4.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/EpicGiantite13205/ai--manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>

### Speculative decoding

*Infrastructure & Outillage, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 21 documents récents contre 83 sur la période de référence : sujet en progression (G² = 0.8, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Expérimenter (KIQ-3.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/inclusionAI/ASpec>
- <http://arxiv.org/abs/2611.08362v1>
- <http://arxiv.org/abs/2611.07959v1>
- <http://arxiv.org/abs/2611.07149v1>
- <http://arxiv.org/abs/2611.06425v1>

### Agent-to-Agent (A2A)

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 6 documents récents contre 23 sur la période de référence : sujet en progression (G² = 0.3, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.2) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/Cygnux-Labs/PCM-protocol>
- <http://arxiv.org/abs/2611.06989v1>
- <http://arxiv.org/abs/2611.03066v1>
- <http://arxiv.org/abs/2610.39109v1>
- <http://arxiv.org/abs/2610.38398v1>

### Computer use

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 11 documents récents contre 99 sur la période de référence : sujet stable (G² = -4.2). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/davidcitahernandez-debug/computer-use-agent-vault>
- <http://arxiv.org/abs/2611.06854v1>
- <http://arxiv.org/abs/2611.05620v1>
- <http://arxiv.org/abs/2611.03634v1>
- <http://arxiv.org/abs/2611.03238v1>

### Sandbox Environment

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 110.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/EpicGiantite13205/ai--manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>

### Running Various Tools

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 110.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/EpicGiantite13205/ai--manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>

### Ai Manus

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 110.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/EpicGiantite13205/ai--manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>

### Supports Running

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 110.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/EpicGiantite13205/ai--manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>

### General-Purpose Ai Agent

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 110.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/EpicGiantite13205/ai--manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>

### Ai-Manus Ai

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 17 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 60.6, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/jfpereirasantos4-arch/ai-manus>
- <https://github.com/osarhiemenaiyevbosa-cloud/ai-manus>
- <https://github.com/viet140612/ai-manus>

## 5. Méthodologie et limites

- Fenêtre récente : 14 jours ; fenêtre de référence : 60 jours.
- Seuils : fréquence ≥ 5 documents, G² ≥ 10.83 (sujets découverts).
- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : momentum 0.35, diffusion 0.25, impact 0.2, nouveaute 0.2.
- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.
