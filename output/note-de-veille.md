# Note de veille du radar d'innovation IA (arrêté au 2026-10-07)

| Rubrique | Valeur |
|---|---|
| Émetteur | Cellule veille et prospective, direction technique |
| Destinataires | CODIR, Direction technique, Product managers |
| Version du protocole | 1.0.0 |
| Méthode de qualification | heuristique |
| Corpus | 3612 signaux récents, 8552 signaux de référence |
| Classification | Diffusion restreinte (interne) |

## 1. Synthèse exécutive

- **Model Context Protocol** (Agir, 0–6 mois) : Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?
- **Computer use** (Agir, 0–6 mois) : Décider (KIQ-2.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?
- **Mixture of Experts** (Agir, 0–6 mois) : Décider (KIQ-1.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

## 2. Mouvements depuis le radar précédent

- Entrées nouvelles : Decision Models, Class-Incremental Learning, On-Policy Distillation, Computer use, Small Language Models, Watermarking, Model Context Protocol, Quantization 1-4 bits, Mixture of Experts, Diffusion LLM, RAG, Agent-to-Agent (A2A), Prompt injection, World Models, Machine unlearning
- Rapprochements du centre : aucun
- Éloignements : aucun

## 3. Tableau du radar

| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice |
|---|---|---|---|---|---|---|---|
| Model Context Protocol | Agents & Applications | Agir | 7 | incrémentale | 4/5 | 4/5 | 0.276 |
| Computer use | Agents & Applications | Agir | 7 | incrémentale | 3/5 | 4/5 | 0.378 |
| Mixture of Experts | Modèles & Techniques | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.197 |
| RAG | Infrastructure & Outillage | Agir | 7 | incrémentale | 3/5 | 3/5 | 0.180 |
| Quantization 1-4 bits | Infrastructure & Outillage | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.220 |
| Prompt injection | Confiance & Régulation | Agir | 7 | incrémentale | 2/5 | 3/5 | 0.162 |
| Agent-to-Agent (A2A) | Agents & Applications | Préparer | 5 | incrémentale | 2/5 | 3/5 | 0.175 |
| Decision Models | Modèles & Techniques | Explorer | 4 | incrémentale | 5/5 | 3/5 | 0.531 |
| Class-Incremental Learning | Infrastructure & Outillage | Surveiller | 3 | radicale | 1/5 | 2/5 | 0.443 |
| On-Policy Distillation | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.409 |
| Small Language Models | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.317 |
| Watermarking | Confiance & Régulation | Surveiller | 3 | incrémentale | 1/5 | 3/5 | 0.305 |
| Diffusion LLM | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.184 |
| World Models | Modèles & Techniques | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.161 |
| Machine unlearning | Confiance & Régulation | Surveiller | 3 | incrémentale | 1/5 | 2/5 | 0.137 |

## 4. Fiches d'analyse

### Model Context Protocol

*Agents & Applications, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 36 documents récents contre 176 sur la période de référence : sujet en recul relatif (G² = -18.1) : sujet probablement banalisé, à vérifier avant tout investissement. Présent dans : recherche, code ouvert, communauté, presse ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/feder-cr/invisible_playwright_mcp>
- <https://github.com/arielshad/3d-asset-server>
- <https://github.com/VoltAgent/official-mcp-servers>
- <https://github.com/graygnatconsole/mcp-audit-tool>
- <https://github.com/breakstageaxe61/genspark-claw>

### Computer use

*Agents & Applications, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 33 documents récents contre 60 sur la période de référence : sujet en progression (G² = 1.6, non significatif). Présent dans : recherche, code ouvert, communauté, presse ; maturité estimée TRL 7. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Décider (KIQ-2.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**KIQ adressées.** KIQ-2.1 : Quels processus métier deviennent automatisables de bout en bout par des agents ?

**Preuves.**
- <https://github.com/feder-cr/invisible_playwright_mcp>
- <https://www.stagehand.dev/evals>
- <https://twitter.com/kylejeong/status/2102108924677927169>
- <https://github.com/ironbee-ai/ironbee-express>
- <http://arxiv.org/abs/2610.07444v1>

### Mixture of Experts

*Modèles & Techniques, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 56 documents récents contre 149 sur la période de référence : sujet stable (G² = -0.5). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Décider (KIQ-1.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://github.com/Yamz-Labs/kyojin>
- <http://arxiv.org/abs/2610.08680v1>
- <http://arxiv.org/abs/2610.08173v1>
- <http://arxiv.org/abs/2610.07774v1>
- <http://arxiv.org/abs/2610.07767v1>

### RAG

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 54 documents récents contre 255 sur la période de référence : sujet en recul relatif (G² = -24.3) : sujet probablement banalisé, à vérifier avant tout investissement. Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/heaven999b/hello-agent-system>
- <https://github.com/Perruer/keelflow>
- <http://arxiv.org/abs/2610.08463v1>
- <http://arxiv.org/abs/2610.08452v1>
- <http://arxiv.org/abs/2610.08205v1>

### Quantization 1-4 bits

*Infrastructure & Outillage, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 114 documents récents contre 300 sur la période de référence : sujet stable (G² = -0.8). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 7. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Décider (KIQ-3.1) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**KIQ adressées.** KIQ-3.1 : Quelle trajectoire du coût d'inférence par million de tokens à 18 mois ?

**Preuves.**
- <https://github.com/Dreamer-Toby/STEPQuant>
- <https://github.com/Yamz-Labs/kyojin>
- <https://github.com/IterateAI/lifeboat-releases>
- <http://arxiv.org/abs/2610.08403v1>
- <http://arxiv.org/abs/2610.08164v1>

### Prompt injection

*Confiance & Régulation, Agir (0–6 mois), TRL 7*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 62 documents récents contre 150 sur la période de référence : sujet stable (G² = -0.0). Présent dans : recherche, code ouvert ; maturité estimée TRL 7. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Décider (KIQ-4.2) : instruire au prochain comité radar une décision d'investissement ou d'industrialisation, avec chiffrage du gain attendu et désignation d'un responsable. Question à éclairer : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**KIQ adressées.** KIQ-4.2 : Quelles nouvelles classes d'attaques menacent nos systèmes à base de LLM ?

**Preuves.**
- <https://github.com/Justinuse1/pojia-breaker>
- <https://github.com/e2sy/jailbreak-archives>
- <http://arxiv.org/abs/2610.08773v1>
- <http://arxiv.org/abs/2610.08678v1>
- <http://arxiv.org/abs/2610.07532v1>

### Agent-to-Agent (A2A)

*Agents & Applications, Préparer (6–18 mois), TRL 5*

**Analyse.** Axe KIT-2 « Agents autonomes et automatisation des processus métier ». 7 documents récents contre 22 sur la période de référence : sujet stable (G² = -0.4). Présent dans : recherche, code ouvert, communauté ; maturité estimée TRL 5. Enjeu pour l'organisation : Nouvelles offres d'automatisation de bout en bout pour nos clients ; menace sur nos prestations à faible valeur ajoutée.

**Action recommandée.** Expérimenter (KIQ-2.2) : lancer une preuve de concept limitée (4 à 6 semaines) sur un cas d'usage interne, avec un critère de succès mesurable. Question à éclairer : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**KIQ adressées.** KIQ-2.2 : Quels standards d'interopérabilité entre agents s'imposent (MCP, A2A, etc.) ?

**Preuves.**
- <https://github.com/useagenthq/threads>
- <https://arstechnica.com/security/2026/10/vulnerability-in-agents-from-google-and-others-exposes-structural-flaw-in-mcp/>
- <http://arxiv.org/abs/2610.04053v1>
- <http://arxiv.org/abs/2610.00392v1>
- <http://arxiv.org/abs/2609.34017v1>

### Decision Models

*Modèles & Techniques, Explorer (18–36 mois), TRL 4*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 8 documents récents contre 2 sur la période de référence : sujet en forte accélération (G² = 10.9, significatif). Présent dans : recherche, communauté ; maturité estimée TRL 4. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Approfondir (KIQ-1.1) : rédiger une fiche d'analyse, identifier 2 ou 3 acteurs ou laboratoires de référence et renforcer la collecte sur ce sujet. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <https://blog.cloudflare.com/clef-decision-models/>
- <https://github.com/PostHog/jeeves>
- <https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails>
- <http://arxiv.org/abs/2610.07716v1>
- <http://arxiv.org/abs/2610.03324v1>

### Class-Incremental Learning

*Infrastructure & Outillage, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-3 « Infrastructure, inférence, coûts et outillage MLOps/LLMOps ». 5 documents récents contre 0 sur la période de référence : sujet en forte accélération (G² = 12.2, significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Baisse du coût d'inférence et hébergement souverain : marge des offres IA et réponse aux exigences clients.

**Action recommandée.** Surveiller (KIQ-3.2) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**KIQ adressées.** KIQ-3.2 : Quelles technologies permettent une IA souveraine ou embarquée (on-device) ?

**Preuves.**
- <http://arxiv.org/abs/2610.04963v1>
- <http://arxiv.org/abs/2609.39839v1>
- <http://arxiv.org/abs/2609.39550v1>
- <http://arxiv.org/abs/2609.39390v1>
- <http://arxiv.org/abs/2609.34503v1>

### On-Policy Distillation

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 35 documents récents contre 28 sur la période de référence : sujet en forte accélération (G² = 18.6, significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.2) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quand un petit modèle (< 10 Md de paramètres) atteindra-t-il le niveau de nos modèles actuels ?

**KIQ adressées.** KIQ-1.2 : Quand un petit modèle (< 10 Md de paramètres) atteindra-t-il le niveau de nos modèles actuels ?

**Preuves.**
- <http://arxiv.org/abs/2610.07654v1>
- <http://arxiv.org/abs/2610.06804v1>
- <http://arxiv.org/abs/2610.05373v1>
- <http://arxiv.org/abs/2610.04950v1>
- <http://arxiv.org/abs/2610.04596v1>

### Small Language Models

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 37 documents récents contre 47 sur la période de référence : sujet en progression (G² = 8.0, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.2) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quand un petit modèle (< 10 Md de paramètres) atteindra-t-il le niveau de nos modèles actuels ?

**KIQ adressées.** KIQ-1.2 : Quand un petit modèle (< 10 Md de paramètres) atteindra-t-il le niveau de nos modèles actuels ?

**Preuves.**
- <http://arxiv.org/abs/2610.08680v1>
- <http://arxiv.org/abs/2610.08063v1>
- <http://arxiv.org/abs/2610.07816v1>
- <http://arxiv.org/abs/2610.07553v1>
- <http://arxiv.org/abs/2610.07276v1>

### Watermarking

*Confiance & Régulation, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 19 documents récents contre 24 sur la période de référence : sujet en progression (G² = 4.2, non significatif). Présent dans : recherche, presse ; maturité estimée TRL 3. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Surveiller (KIQ-4.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <http://arxiv.org/abs/2610.08668v1>
- <http://arxiv.org/abs/2610.05712v1>
- <http://arxiv.org/abs/2610.05323v1>
- <http://arxiv.org/abs/2610.04763v1>
- <http://arxiv.org/abs/2610.04169v1>

### Diffusion LLM

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 17 documents récents contre 28 sur la période de référence : sujet en progression (G² = 1.4, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.04953v1>
- <http://arxiv.org/abs/2610.04938v1>
- <http://arxiv.org/abs/2610.06940v1>
- <http://arxiv.org/abs/2610.02665v1>
- <http://arxiv.org/abs/2610.02657v2>

### World Models

*Modèles & Techniques, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-1 « Modèles de fondation et architectures d'apprentissage ». 50 documents récents contre 100 sur la période de référence : sujet en progression (G² = 1.1, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Qualité et coût des modèles intégrés à nos offres ; dépendance aux fournisseurs de modèles.

**Action recommandée.** Surveiller (KIQ-1.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**KIQ adressées.** KIQ-1.1 : Quelle architecture est en passe de remplacer le Transformer dense sur nos cas d'usage ?

**Preuves.**
- <http://arxiv.org/abs/2610.08773v1>
- <http://arxiv.org/abs/2610.08033v1>
- <http://arxiv.org/abs/2610.07599v1>
- <http://arxiv.org/abs/2610.05912v1>
- <http://arxiv.org/abs/2610.05861v1>

### Machine unlearning

*Confiance & Régulation, Surveiller (> 36 mois), TRL 3*

**Analyse.** Axe KIT-4 « Sécurité, fiabilité, conformité réglementaire et éthique de l'IA ». 22 documents récents contre 43 sur la période de référence : sujet en progression (G² = 0.6, non significatif). Présent dans : recherche ; maturité estimée TRL 3. Enjeu pour l'organisation : Conformité (AI Act, RGPD) et sécurité de nos produits IA : condition d'accès aux marchés santé et public.

**Action recommandée.** Surveiller (KIQ-4.1) : maintenir le sujet en liste de surveillance et le réévaluer à la prochaine revue trimestrielle. Question à éclairer : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**KIQ adressées.** KIQ-4.1 : Quelles obligations de l'AI Act s'appliquent à nos produits et à quelle échéance ?

**Preuves.**
- <http://arxiv.org/abs/2610.07197v1>
- <http://arxiv.org/abs/2610.02418v1>
- <http://arxiv.org/abs/2610.01962v1>
- <http://arxiv.org/abs/2609.39882v1>
- <http://arxiv.org/abs/2609.39279v1>

## 5. Méthodologie et limites

- Fenêtre récente : 14 jours ; fenêtre de référence : 60 jours.
- Seuils : fréquence ≥ 5 documents, G² ≥ 10.83 (sujets découverts).
- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : momentum 0.35, diffusion 0.25, impact 0.2, nouveaute 0.2.
- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.
