# Note de veille du radar d'innovation IA (arrêté au 2026-11-05)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 2664 signaux récents, 11942 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **On-device AI** (Agir, 0–6 mois) : Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?
- **Prompt injection** (Agir, 0–6 mois) : Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : Speculative decoding
- Rapprochements du centre : On-device AI
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |
|---|---|---|---|---|---|---|---|---|
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.475 | stable |
| On-device AI | Infrastructure & Outillage | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.294 | rapproché du centre |
| Prompt injection | Confiance & Régulation | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.240 | stable |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.187 | stable |
| Mixture of Experts | Modèles & Techniques | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.141 | stable |
| Quantization 1-4 bits | Infrastructure & Outillage | Agir | 7 | incrémentale | 1/5 | 3/5 | 0.120 | stable |
| Claude Code | Agents & Applications | Préparer | 5 | incrémentale | 5/5 | 3/5 | 0.442 | stable |
| Code Codex | Agents & Applications | Préparer | 5 | incrémentale | 5/5 | 3/5 | 0.424 | stable |
| Ai Coding | Agents & Applications | Préparer | 5 | incrémentale | 4/5 | 3/5 | 0.432 | stable |
| Coding Agent | Agents & Applications | Préparer | 5 | incrémentale | 4/5 | 3/5 | 0.407 | stable |
| Agent-to-Agent (A2A) | Agents & Applications | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.173 | stable |
| Computer use | Agents & Applications | Préparer | 5 | incrémentale | 3/5 | 3/5 | 0.163 | stable |
| AI Act | Confiance & Régulation | Explorer | 4 | incrémentale | 1/5 | 3/5 | 0.145 | stable |
| State Space Models | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.152 | stable |
| Speculative decoding | Infrastructure & Outillage | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.122 | nouveau |

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

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 79 documents récents contre 212 sur la période de référence : sujet en forte accélération (G² = 16.4, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/andyhuo520/digital-human-koubo>
- <https://github.com/andrew-babo/muse4ai>
- <https://github.com/Balanov/shim>
- <https://github.com/hevnsnt/CVEngine>
- <https://github.com/muaaz9329/cheap-ag>

### On-device AI

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 15 documents récents contre 113 sur la période de référence : sujet stable (G² = -3.5). Présent dans : recherche, code ouvert, presse ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <https://github.com/wangzan101/Mika>
- <https://huggingface.co/blog/phonon-tts>
- <http://arxiv.org/abs/2611.04797v1>
- <http://arxiv.org/abs/2611.02601v1>
- <http://arxiv.org/abs/2611.01377v1>

### Prompt injection

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 40 documents récents contre 187 sur la période de référence : sujet stable (G² = -0.0). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**KIQ adressées.** KIQ-4.2 : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**Preuves.**
- <https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/>
- <https://github.com/codexlx/contextshield>
- <http://arxiv.org/abs/2611.06682v1>
- <http://arxiv.org/abs/2611.06553v1>
- <http://arxiv.org/abs/2611.06147v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 49 documents récents contre 253 sur la période de référence : sujet stable (G² = -0.5). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/wanghao-SunSky/cs329z-chinese>
- <https://github.com/glincker/awesome-selfhosted-ai>
- <https://github.com/pwnedlabs/ai-security-labs>
- <https://github.com/harrytted/ai-agent-interview-playbook>
- <http://arxiv.org/abs/2611.06715v1>

### Mixture of Experts

*Modèles & Techniques, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 43 documents récents contre 191 sur la période de référence : sujet en progression (G² = 0.1, non significatif). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Décider (KIQ-1.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/ZhuLinsen/LiteMoE>
- <https://github.com/zhangshuibai/molten>
- <http://arxiv.org/abs/2611.06257v1>
- <http://arxiv.org/abs/2611.06147v1>
- <http://arxiv.org/abs/2611.05984v1>

### Quantization 1-4 bits

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 80 documents récents contre 385 sur la période de référence : sujet stable (G² = -0.1). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/zhangshuibai/molten>
- <http://arxiv.org/abs/2611.06859v1>
- <http://arxiv.org/abs/2611.06257v1>
- <http://arxiv.org/abs/2611.05799v1>
- <http://arxiv.org/abs/2611.05304v1>

### Claude Code

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 26 documents récents contre 30 sur la période de référence : sujet en forte accélération (G² = 24.6, significatif). Présent dans : code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/andyhuo520/digital-human-koubo>
- <https://github.com/DenisSergeevitch/ex-ussr-kinship-research>
- <https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce>
- <https://github.com/ChannelCooperStart/capri-ai>
- <https://github.com/jmanico/grim-prompter>

### Code Codex

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 14 documents récents contre 12 sur la période de référence : sujet en forte accélération (G² = 17.4, significatif). Présent dans : code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/andyhuo520/digital-human-koubo>
- <https://github.com/ChannelCooperStart/capri-ai>
- <https://github.com/jmanico/grim-prompter>
- <https://github.com/Moh4696/open-3d-skills>
- <https://github.com/aa1143/NamiAgent>

### Ai Coding

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 22 documents récents contre 35 sur la période de référence : sujet en forte accélération (G² = 13.9, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.2) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/sarpstar/cinecode>
- <https://github.com/jmanico/grim-prompter>
- <https://github.com/enmerasoftware/ai-design-check>
- <https://github.com/jefferysha0627/agent-office-3d>
- <https://github.com/Sheernox/cedr>

### Coding Agent

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 19 documents récents contre 29 sur la période de référence : sujet en forte accélération (G² = 12.8, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.2) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/blakeandersonw/ai-app-playbook>
- <https://github.com/sarpstar/cinecode>
- <https://github.com/Sheernox/cedr>
- <https://github.com/onurozcan/omux>
- <https://github.com/DukeDeSouth/m7-mcp-oss>

### Agent-to-Agent (A2A)

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 5 documents récents contre 27 sur la période de référence : sujet stable (G² = -0.1). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.2) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/Cygnux-Labs/PCM-protocol>
- <http://arxiv.org/abs/2611.03066v1>
- <http://arxiv.org/abs/2610.39109v1>
- <http://arxiv.org/abs/2610.38398v1>
- <http://arxiv.org/abs/2610.37415v1>

### Computer use

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 14 documents récents contre 101 sur la période de référence : sujet stable (G² = -2.6). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/davidcitahernandez-debug/computer-use-agent-vault>
- <http://arxiv.org/abs/2611.06854v1>
- <http://arxiv.org/abs/2611.05620v1>
- <http://arxiv.org/abs/2611.03634v1>
- <http://arxiv.org/abs/2611.03238v1>

### AI Act

*Confiance & Régulation, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 6 documents récents contre 21 sur la période de référence : sujet en progression (G² = 0.4, non significatif). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Approfondir (KIQ-4.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://www.arxo.io/findings/ARXO-2026-0413/>
- <http://arxiv.org/abs/2611.03121v1>
- <http://arxiv.org/abs/2611.02561v1>
- <http://arxiv.org/abs/2610.41437v1>
- <http://arxiv.org/abs/2610.35671v1>

### State Space Models

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 15 documents récents contre 49 sur la période de référence : sujet en progression (G² = 1.4, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2611.06084v1>
- <http://arxiv.org/abs/2611.04449v1>
- <http://arxiv.org/abs/2611.03101v1>
- <http://arxiv.org/abs/2610.41994v1>
- <http://arxiv.org/abs/2610.39418v1>

### Speculative decoding

*Infrastructure & Outillage, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 22 documents récents contre 83 sur la période de référence : sujet en progression (G² = 0.8, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Surveiller (KIQ-3.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <http://arxiv.org/abs/2611.06425v1>
- <http://arxiv.org/abs/2611.05724v1>
- <http://arxiv.org/abs/2611.05345v1>
- <http://arxiv.org/abs/2611.04055v1>
- <http://arxiv.org/abs/2611.04032v1>

## 5. Méthodologie et limites

- Fenêtre récente : 14 jours ; fenêtre de référence : 60 jours.
- Seuils : fréquence ≥ 5 documents, G² ≥ 10.83 (sujets découverts).
- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : momentum 0.35, diffusion 0.25, impact 0.2, nouveaute 0.2.
- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.
