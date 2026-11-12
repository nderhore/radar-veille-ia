# Note de veille du radar d'innovation IA (arrêté au 2026-11-12)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 2290 signaux récents, 12325 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **On-device AI** (Agir, 0–6 mois) : Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?
- **Quantization 1-4 bits** (Agir, 0–6 mois) : Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : Various Tools, Quantization 1-4 bits
- Rapprochements du centre : aucun
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |
|---|---|---|---|---|---|---|---|---|
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.392 | stable |
| On-device AI | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 4/5 | 0.294 | stable |
| Quantization 1-4 bits | Infrastructure & Outillage | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.238 | nouveau |
| Prompt injection | Confiance & Régulation | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.237 | stable |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.183 | stable |
| Mixture of Experts | Modèles & Techniques | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.227 | stable |
| General-Purpose Ai Agent | Modèles & Techniques | Préparer | 5 | radicale | 3/5 | 3/5 | 0.464 | stable |
| AI Act | Confiance & Régulation | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.441 | stable |
| Computer use | Agents & Applications | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.180 | stable |
| Speculative decoding | Infrastructure & Outillage | Préparer | 5 | incrémentale | 2/5 | 3/5 | 0.194 | stable |
| Supports Running Various | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.428 | stable |
| Sandbox Environment | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.428 | stable |
| Ai Manus | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.428 | stable |
| Various Tools | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.428 | nouveau |
| Ai-Manus Ai | Modèles & Techniques | Explorer | 4 | radicale | 3/5 | 2/5 | 0.401 | stable |

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

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 69 documents récents contre 234 sur la période de référence : sujet en forte accélération (G² = 12.8, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/andrew-babo/muse4ai>
- <https://github.com/agentes-chat/agentes-chat>
- <https://github.com/JosssphZhou/poki>
- <https://github.com/Balanov/shim>
- <https://github.com/HerdBuilderEstimate/roblox-studio-mcp>

### On-device AI

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 13 documents récents contre 111 sur la période de référence : sujet stable (G² = -2.3). Présent dans : recherche, code ouvert, communauté, presse ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <https://github.com/wangzan101/Mika>
- <https://github.com/sdalberto/ia-da-sobrevivencia/blob/main/README.en.md>
- <https://huggingface.co/blog/qvac/botpsy>
- <http://arxiv.org/abs/2611.14356v1>
- <http://arxiv.org/abs/2611.13960v1>

### Quantization 1-4 bits

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 64 documents récents contre 393 sur la période de référence : sujet stable (G² = -0.4). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/huawei-csl/MACaQ>
- <http://arxiv.org/abs/2611.14413v1>
- <http://arxiv.org/abs/2611.14059v1>
- <http://arxiv.org/abs/2611.13730v1>
- <http://arxiv.org/abs/2611.13410v1>

### Prompt injection

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 36 documents récents contre 187 sur la période de référence : sujet en progression (G² = 0.2, non significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**KIQ adressées.** KIQ-4.2 : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**Preuves.**
- <https://github.com/JosssphZhou/poki>
- <https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/>
- <https://github.com/codexlx/contextshield>
- <https://github.com/SilentGuard-SG/silentguard>
- <http://arxiv.org/abs/2611.13578v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 31 documents récents contre 257 sur la période de référence : sujet stable (G² = -4.7). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/pnyn96/mindact-agent>
- <https://github.com/glincker/awesome-selfhosted-ai>
- <https://github.com/pwnedlabs/ai-security-labs>
- <http://arxiv.org/abs/2611.14263v1>
- <http://arxiv.org/abs/2611.13966v1>

### Mixture of Experts

*Modèles & Techniques, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 40 documents récents contre 196 sur la période de référence : sujet en progression (G² = 0.6, non significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Décider (KIQ-1.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/ZhuLinsen/LiteMoE>
- <https://www.silasdata.com/llm-playground-inside-architectures/>
- <http://arxiv.org/abs/2611.14425v1>
- <http://arxiv.org/abs/2611.14083v1>
- <http://arxiv.org/abs/2611.13730v1>

### General-Purpose Ai Agent

*Modèles & Techniques, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 32 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 121.5, significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Expérimenter (KIQ-1.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>
- <https://github.com/jfpereirasantos4-arch/ai-manus>

### AI Act

*Confiance & Régulation, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 36 documents récents contre 19 sur la période de référence : sujet en forte accélération (G² = 72.0, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Expérimenter (KIQ-4.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>
- <https://github.com/jfpereirasantos4-arch/ai-manus>

### Computer use

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 9 documents récents contre 99 sur la période de référence : sujet stable (G² = -4.5). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/agentes-chat/agentes-chat>
- <https://github.com/davidcitahernandez-debug/computer-use-agent-vault>
- <http://arxiv.org/abs/2611.06854v1>
- <http://arxiv.org/abs/2611.05620v1>
- <http://arxiv.org/abs/2611.03634v1>

### Speculative decoding

*Infrastructure & Outillage, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 19 documents récents contre 87 sur la période de référence : sujet en progression (G² = 0.6, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Expérimenter (KIQ-3.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/inclusionAI/ASpec>
- <http://arxiv.org/abs/2611.14399v1>
- <http://arxiv.org/abs/2611.12737v1>
- <http://arxiv.org/abs/2611.12464v1>
- <http://arxiv.org/abs/2611.11371v1>

### Supports Running Various

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 117.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>
- <https://github.com/jfpereirasantos4-arch/ai-manus>

### Sandbox Environment

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 117.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>
- <https://github.com/jfpereirasantos4-arch/ai-manus>

### Ai Manus

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 117.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>
- <https://github.com/jfpereirasantos4-arch/ai-manus>

### Various Tools

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 31 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 117.7, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/quyetcao/ai-manus>
- <https://github.com/Abdul-Rehman7826/ai-manus>
- <https://github.com/tireddwarf99/manus-ai>
- <https://github.com/tireddwarf99/ai_manus>
- <https://github.com/jfpereirasantos4-arch/ai-manus>

### Ai-Manus Ai

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 17 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 64.4, significatif). Présent dans : code ouvert ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

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
