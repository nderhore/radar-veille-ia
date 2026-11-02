# Note de veille du radar d'innovation IA (arrêté au 2026-11-02)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 2658 signaux récents, 11387 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **Prompt injection** (Agir, 0–6 mois) : Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?
- **RAG** (Agir, 0–6 mois) : Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : Code Codex, AI Act, World Models
- Rapprochements du centre : aucun
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |
|---|---|---|---|---|---|---|---|---|
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 5/5 | 3/5 | 0.456 | stable |
| Prompt injection | Confiance & Régulation | Agir | 7 | incrémentale | 4/5 | 3/5 | 0.265 | stable |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.196 | stable |
| Quantization 1-4 bits | Infrastructure & Outillage | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.136 | stable |
| Mixture of Experts | Modèles & Techniques | Agir | 7 | incrémentale | 1/5 | 3/5 | 0.118 | stable |
| Claude Code | Agents & Applications | Préparer | 5 | incrémentale | 5/5 | 3/5 | 0.444 | stable |
| Code Codex | Agents & Applications | Préparer | 5 | incrémentale | 5/5 | 3/5 | 0.398 | nouveau |
| On-device AI | Infrastructure & Outillage | Préparer | 5 | incrémentale | 4/5 | 3/5 | 0.233 | stable |
| Computer use | Agents & Applications | Explorer | 4 | incrémentale | 3/5 | 3/5 | 0.196 | stable |
| AI Act | Confiance & Régulation | Explorer | 4 | incrémentale | 1/5 | 3/5 | 0.121 | nouveau |
| State Space Models | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.180 | stable |
| Diffusion LLM | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.177 | stable |
| Test-time compute | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.126 | stable |
| World Models | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 3/5 | 0.114 | nouveau |
| Speculative decoding | Infrastructure & Outillage | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.095 | stable |

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

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 76 documents récents contre 199 sur la période de référence : sujet en forte accélération (G² = 14.8, significatif). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/andyhuo520/digital-human-koubo>
- <https://github.com/hevnsnt/CVEngine>
- <https://github.com/muaaz9329/cheap-ag>
- <https://github.com/qybaihe/bla>
- <https://github.com/aa1143/NamiAgent>

### Prompt injection

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 38 documents récents contre 184 sur la période de référence : sujet stable (G² = -0.2). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**KIQ adressées.** KIQ-4.2 : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**Preuves.**
- <https://github.com/Alejandros17487/ai-jailbreaks>
- <https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/>
- <https://github.com/AndreSzymanski15/ai-jailbreaks>
- <https://github.com/codexlx/contextshield>
- <http://arxiv.org/abs/2610.41998v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 51 documents récents contre 253 sur la période de référence : sujet stable (G² = -0.5). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/wanghao-SunSky/cs329z-chinese>
- <https://github.com/h9-tec/ai-roadmap-2026>
- <https://github.com/glincker/awesome-selfhosted-ai>
- <https://github.com/pwnedlabs/ai-security-labs>
- <https://github.com/harrytted/ai-agent-interview-playbook>

### Quantization 1-4 bits

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 73 documents récents contre 377 sur la période de référence : sujet stable (G² = -1.4). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/ahtx/kindi>
- <https://github.com/Magnvs7/Promethevs>
- <https://github.com/zhangshuibai/molten>
- <http://arxiv.org/abs/2610.41822v1>
- <http://arxiv.org/abs/2610.41408v1>

### Mixture of Experts

*Modèles & Techniques, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 34 documents récents contre 186 sur la période de référence : sujet stable (G² = -1.2). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Décider (KIQ-1.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/Magnvs7/Promethevs>
- <https://github.com/zhangshuibai/molten>
- <http://arxiv.org/abs/2610.41366v1>
- <http://arxiv.org/abs/2610.41039v1>
- <http://arxiv.org/abs/2610.40541v1>

### Claude Code

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 26 documents récents contre 28 sur la période de référence : sujet en forte accélération (G² = 25.0, significatif). Présent dans : code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

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

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 12 documents récents contre 12 sur la période de référence : sujet en forte accélération (G² = 12.4, significatif). Présent dans : code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.1) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/andyhuo520/digital-human-koubo>
- <https://github.com/ChannelCooperStart/capri-ai>
- <https://github.com/jmanico/grim-prompter>
- <https://github.com/Moh4696/open-3d-skills>
- <https://github.com/aa1143/NamiAgent>

### On-device AI

*Infrastructure & Outillage, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 19 documents récents contre 110 sur la période de référence : sujet stable (G² = -1.2). Présent dans : recherche, code ouvert ; maturité estimée TRL 5. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Expérimenter (KIQ-3.2) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <https://github.com/wangzan101/Mika>
- <https://github.com/haplollc/Vesalius>
- <http://arxiv.org/abs/2610.39758v1>
- <http://arxiv.org/abs/2610.39343v1>
- <http://arxiv.org/abs/2610.38329v1>

### Computer use

*Agents & Applications, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 17 documents récents contre 96 sur la période de référence : sujet stable (G² = -0.8). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Approfondir (KIQ-2.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://getopposable.com/blog/computer-use-on-the-phone>
- <http://arxiv.org/abs/2610.41397v1>
- <http://arxiv.org/abs/2610.40246v1>
- <http://arxiv.org/abs/2610.39282v1>
- <http://arxiv.org/abs/2610.36877v1>

### AI Act

*Confiance & Régulation, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 5 documents récents contre 20 sur la période de référence : sujet en progression (G² = 0.1, non significatif). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Approfondir (KIQ-4.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <https://www.arxo.io/findings/ARXO-2026-0413/>
- <http://arxiv.org/abs/2610.41437v1>
- <http://arxiv.org/abs/2610.35671v1>
- <http://arxiv.org/abs/2610.31588v1>
- <http://arxiv.org/abs/2610.30051v1>

### State Space Models

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 16 documents récents contre 46 sur la période de référence : sujet en progression (G² = 2.1, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.41994v1>
- <http://arxiv.org/abs/2610.39418v1>
- <http://arxiv.org/abs/2610.38578v1>
- <http://arxiv.org/abs/2610.38255v1>
- <http://arxiv.org/abs/2610.38095v1>

### Diffusion LLM

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 17 documents récents contre 50 sur la période de référence : sujet en progression (G² = 2.1, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.41574v1>
- <http://arxiv.org/abs/2610.40847v1>
- <http://arxiv.org/abs/2610.39293v1>
- <http://arxiv.org/abs/2610.38775v1>
- <http://arxiv.org/abs/2610.36940v1>

### Test-time compute

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 20 documents récents contre 71 sur la période de référence : sujet en progression (G² = 0.8, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.42149v1>
- <http://arxiv.org/abs/2610.41089v1>
- <http://arxiv.org/abs/2610.40927v1>
- <http://arxiv.org/abs/2610.39006v1>
- <http://arxiv.org/abs/2610.40700v1>

### World Models

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 32 documents récents contre 137 sur la période de référence : sujet en progression (G² = 0.1, non significatif). Présent dans : recherche, presse ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.42146v1>
- <http://arxiv.org/abs/2610.41273v1>
- <http://arxiv.org/abs/2610.40927v1>
- <http://arxiv.org/abs/2610.40798v1>
- <http://arxiv.org/abs/2610.38980v1>

### Speculative decoding

*Infrastructure & Outillage, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 20 documents récents contre 78 sur la période de référence : sujet en progression (G² = 0.3, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Surveiller (KIQ-3.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <http://arxiv.org/abs/2610.40613v1>
- <http://arxiv.org/abs/2610.40287v1>
- <http://arxiv.org/abs/2610.39761v1>
- <http://arxiv.org/abs/2610.38981v1>
- <http://arxiv.org/abs/2610.38331v1>

## 5. Méthodologie et limites

- Fenêtre récente : 14 jours ; fenêtre de référence : 60 jours.
- Seuils : fréquence ≥ 5 documents, G² ≥ 10.83 (sujets découverts).
- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : momentum 0.35, diffusion 0.25, impact 0.2, nouveaute 0.2.
- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.
