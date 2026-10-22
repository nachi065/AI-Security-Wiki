---
title: "Predictive Model Monitoring and Adversarial ML"
author: Nachiket Sathaye
parent: "Domain Standards"
nav_order: 7
description: "Security and monitoring requirements for classic predictive models (classifiers, scoring and forecasting models): input and prediction drift, accuracy decay, fairness shift, and the adversarial ML attacks of evasion, poisoning, extraction, membership inference and inversion."
document_type: AI Security Wiki Standard
version: 1.0
---

# Predictive Model Monitoring and Adversarial ML

> **Purpose:** Set minimum requirements for securing and monitoring classic predictive models: classifiers, scoring, ranking, forecasting and anomaly-detection models that turn structured input into a score or a label. Most of this wiki is written around generative AI and agents; these models are older, often make decisions about people, and fail in different ways.

> **Audience:** Model owners, data scientists, MLOps engineers, model risk management and security architects.

> **How this relates:** The attack vocabulary comes from the predictive AI taxonomy of NIST AI 100-2e2025, mapped to this wiki's controls in the [NIST AI 100-2 Crosswalk](../23_Framework_Crosswalks/14_NIST_AI_100_2_Crosswalk.md) and described in [Foundations section 3](../00_Foundations/03-Threat-Taxonomy.md). This page turns that into requirements and points to the test cases. Illustrative thresholds are marked as such; none comes from a standard.

## 1. Scope

In scope: any model in production that produces a score, class, rank or forecast from structured or semi-structured input, whether built in-house, bought, or embedded in a vendor product. Examples are credit and fraud scoring, claims triage, churn prediction, demand forecasting, CV screening, anomaly detection in security tooling and computer-vision classifiers.

A large language model used as a classifier (for example to route tickets) is in scope for sections 3 and 4 as well as the generative AI standards.

## 2. Why predictive models fail quietly

A predictive model has no error state when the world changes. It keeps returning confident scores while its accuracy falls. Four kinds of change matter:

| Change | What moves | How it shows | Example |
|---|---|---|---|
| Input (data) drift | The distribution of input features | Feature distributions differ from the training or validation baseline | A new product line brings customers unlike those in the training data |
| Concept drift | The relationship between input and the right answer | Accuracy falls even though inputs look similar | Fraudsters change tactics, so old patterns no longer mark fraud |
| Prediction drift | The distribution of the model's own outputs | Approval or alert rates move without a business reason | The share of applications scored high-risk doubles in a month |
| Fairness shift | Outcomes for different groups | Gaps in approval, error or selection rates between groups widen | A new region with a different population is added without retesting |

Concept drift can only be confirmed when true outcomes (labels) arrive, which can take weeks or months for credit or claims. Until then, input and prediction drift are the early warnings.

## 3. Monitoring requirements

| # | Requirement | Control | Tested by |
|---|---|---|---|
| PM-1 | Record a baseline at validation: feature distributions, prediction distribution, accuracy measures and group outcome rates, with the data and date they came from. | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [TC-L12-033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033) |
| PM-2 | Monitor input drift for the features that matter most to the model, and prediction drift, at a cadence that matches the decision volume (daily for high-volume models). | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [TC-L12-033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033), [TC-L14-016](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-016) |
| PM-3 | Measure accuracy on labelled outcomes as they arrive, and show measures as pending, not unchanged, while labels are delayed. | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034) | [TC-L12-033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033) |
| PM-4 | For models that make or support decisions about people, monitor group outcome and error-rate gaps against the approved thresholds and the validated boundaries in the bias profile. | [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041) | [TC-L03-043](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-043), [TC-L12-033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033) |
| PM-5 | Check data quality at input: missing values, out-of-range values and categories never seen in training. | [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [TC-L12-033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033), [TC-L13-005](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-005) |
| PM-6 | Give every threshold an owner and a defined response: investigate, retrain, restrict use, or roll back to the previous version. | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-025](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-025) | [TC-L12-033](../10_Test_Case_Library/L12-model-layer.md#tc-l12-033), [TC-L14-013](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-013) |
| PM-7 | Revalidate after retraining, and treat a retrained model as a new version for release gating and impact assessment triggers. | [AI-CTRL-033](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-033) | [TC-L14-012](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-012), [TC-L03-031](../10_Test_Case_Library/L03-legal-privacy-and-compliance.md#tc-l03-031) |

### Illustrative starting thresholds

These are starting points to tune, not values from a standard. Set the final thresholds with the model owner and model risk, from the model's own validation results and the cost of a wrong decision.

| Measure | Look when | Act when | Note |
|---|---|---|---|
| Population stability index (PSI) of an important feature or of the score | 0.1 or more | 0.25 or more | These bands are a widely used industry rule of thumb from credit scoring, not a standard. They depend on how the values are binned. |
| Two-sample test on a continuous feature (for example Kolmogorov-Smirnov) | Significant at the chosen level for 3 days running | Significant for 7 days running on a top-ten feature | With large volumes almost any difference is significant, so also look at the size of the difference. |
| Unseen category values | Above 1 percent of daily inputs | Above 5 percent | Usually a change upstream, such as a new product code. |
| Accuracy measure on labelled outcomes (for example AUC or error rate) | Down 2 points from baseline | Down 5 points, or below the minimum approved at validation | Use the measure the model was approved on. |
| Group outcome or error-rate gap | Half-way to the approved threshold | At the approved threshold | The threshold itself is set under [AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041). |

## 4. Adversarial ML requirements

Attackers can target a predictive model directly. The classes below follow NIST AI 100-2e2025's predictive AI taxonomy; the identifiers link to the [NIST AI 100-2 Crosswalk](../23_Framework_Crosswalks/14_NIST_AI_100_2_Crosswalk.md#attack-classes-to-wiki-controls).

| Attack | What it does | Requirement | Control | Tested by |
|---|---|---|---|---|
| Evasion (NISTAML.022, black-box NISTAML.025) | Crafted input that the model misclassifies, such as a fraudulent transaction shaped to score as safe | Test robustness before release on the features an attacker controls; monitor for inputs near the decision boundary; do not rely on one model alone for high-value decisions | [AI-CTRL-034](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-034), [AI-CTRL-005](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-005) | [TC-L12-010](../10_Test_Case_Library/L12-model-layer.md#tc-l12-010), [TC-L12-011](../10_Test_Case_Library/L12-model-layer.md#tc-l12-011), [TC-L12-012](../10_Test_Case_Library/L12-model-layer.md#tc-l12-012) |
| Data poisoning, including clean-label and backdoor poisoning (NISTAML.013, .012, .021, .023, .024) | Training data altered so the model fails generally, or behaves wrongly on a trigger | Control who can change training data and labels; screen for outliers and label flips; keep dataset versions and provenance; watch feedback loops that retrain on the model's own decisions | [AI-CTRL-029](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-029) | [TC-L13-003](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-003), [TC-L13-004](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-004), [TC-L13-005](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-005), [TC-L13-018](../10_Test_Case_Library/L13-training-and-fine-tuning-layer.md#tc-l13-018) |
| Model poisoning (NISTAML.011, .026) | The model file or its training code is altered | Sign model artefacts and verify at deployment; restrict registry write access; scan models | [AI-CTRL-030](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-030), [AI-CTRL-031](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-031) | [TC-L12-003](../10_Test_Case_Library/L12-model-layer.md#tc-l12-003), [TC-L12-005](../10_Test_Case_Library/L12-model-layer.md#tc-l12-005), [TC-L14-003](../10_Test_Case_Library/L14-mlops-llmops-layer.md#tc-l14-003) |
| Model extraction (NISTAML.031) | Repeated queries used to copy the model's behaviour | Authenticate and rate-limit the scoring API; return no more output detail than the use needs; detect systematic query patterns | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036) | [TC-L12-007](../10_Test_Case_Library/L12-model-layer.md#tc-l12-007), [TC-L12-013](../10_Test_Case_Library/L12-model-layer.md#tc-l12-013) |
| Membership inference (NISTAML.033) | Working out whether a person's record was in the training data | For models trained on personal data, measure membership inference success before release against an agreed level; limit confidence detail in outputs; consider training-time protections | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [TC-L12-034](../10_Test_Case_Library/L12-model-layer.md#tc-l12-034) |
| Reconstruction and property inference, including model inversion (NISTAML.032, .034) | Recovering training records, sensitive attributes or properties of the training data from the model's outputs | As for membership inference; test attribute inference for any sensitive attribute the model could reveal | [AI-CTRL-028](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-028), [AI-CTRL-017](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-017) | [TC-L12-034](../10_Test_Case_Library/L12-model-layer.md#tc-l12-034) |
| Energy-latency (NISTAML.014) | Inputs crafted to make inference slow or expensive | Time and resource limits per request; monitor latency outliers | [AI-CTRL-036](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-036), [AI-CTRL-040](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-040) | [TC-L12-022](../10_Test_Case_Library/L12-model-layer.md#tc-l12-022) |

## 5. Evidence to keep

- The validation baseline and the data it came from (PM-1).
- Threshold configuration with owner and approval (PM-2 to PM-6).
- Monitoring history and every breach with its response.
- Robustness and privacy probe results attached to the release gate record.
- The bias profile and its validated boundaries for decision-making models ([AI-CTRL-041](../03_Control_Library/03_AI_Security_Control_Objectives_Library.md#ai-ctrl-041)).

Related register risks: [AI-R17](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md#ai-r17-data-quality-degradation-and-model-drift) (data quality degradation and model drift), [AI-R14](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md#ai-r14-biased-or-discriminatory-ai-outcomes) (biased outcomes) and [AI-R39](../02_Risk_Management/02B_Enterprise_AI_Risk_Register.md#ai-r39-missing-independent-model-validation) (missing independent model validation).
