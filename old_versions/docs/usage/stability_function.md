# 📊 Stability Functions Usage Guide

This page explains how to use the key stability functions available in the `DriftSense` package. These functions help measure **data drift**, also called **stability**, for features, targets, and model predictions.


These functions are essential for understanding how your data, features, and model outputs change over time or across different datasets.

---

## 🔍 Overview

The package supports different types of stability assessments:

1. **Target Stability / Drift**  
   Measures the change in the target variable distribution.

2. **Feature Stability / Drift**  
   Assesses the distributional shift of individual features.

3. **Model Prediction Stability / Drift**  
   Evaluates the stability of model predictions over time.

---


## ⚙️ Available Functions

### 1. `calculate_feature_stability()`

Compares the distribution of a feature in reference and current datasets using a selected binning method.

```python
from driftsense import calculate_feature_drift

stability_score = calculate_feature_drift(
    reference_data=ref_df["feature_1"],
    current_data=curr_df["feature_1"],
    method="equal_width",  # or "quantile", "adaptive", etc.
    bins=5
)
print("Drift/Stability Score:", stability_score)
```

---

### 2. `calculate_all_features_stability()`

Calculates stability scores for **all numeric features** in your dataset.

```python
from driftsense import calculate_all_features_drift

stability_df = calculate_all_features_drift(
    reference_data=ref_df,
    current_data=curr_df,
    method="quantile",
    bins=10
)
print(stability_df.head())
```

---

### 3. `create_drift_report()`

Generates a HTML report including summarised drift/stability score with binning method used, drift detection flag, bin-wise drift/stability scores for each feature / target at granular level, and warnings for unstable features.

```python
from driftsense import generate_drift_report

create_drift_report(
    reference_data=ref_df,
    current_data=curr_df,
    method="adaptive",
    bins=4,
    output_path="Drift_Stability_Report.html"
)
```

---

## 🧠 Notes

- Binning strategy significantly affects the result; choose based on use case.
- Adaptive binning requires a target variable.
- Feature stability/drift values above a threshold (e.g., 0.1 or 0.2) may indicate drift.

---

### ✅ Usage Example

```python
import numpy as np
from driftsense import calculate_feature_drift

expected = np.array([0.25, 0.25, 0.25, 0.25])
actual = np.array([0.10, 0.20, 0.30, 0.40])

value = calculate_feature_drift(expected, actual)
print(f"Drift/Stability Value (CSI): {value:.4f}")
```

---

## 📊 Feature Stability Across Time

To evaluate feature drift between two datasets:

```python
from driftsense import calculate_feature_drift

# input_distributions: already binned distributions
feature_drift_score = calculate_feature_stability(expected_dist, actual_dist)

print("Feature Drift/Stability (CSI):", feature_drift_score)
```

---

## 📊 Target or Model Drift Example

```python
from DriftSense import calculate_target_stability

# Compare target or model prediction distributions over time
target_drift = calculate_target_stability(expected_target_bins, actual_target_bins)

print("Target Drift:", target_drift)
```

---

## 📌 Notes

- Drift values > 0.2 generally indicate significant drift.
- Drift methods require **binning** to be performed. You can use `get_bin_edges()` to see what bins are generated using vrious binning strategies.
- Target and model drift are often monitored **weekly/monthly** in regulated industries. In some cases, it gets monitored quarterly or semiannually. 
  This monitoring frequency is dependent on the business usage of the model.

---

## 🧪 Recommended Monitoring Thresholds

| Stability Metric | Threshold        | Interpretation                 |
|------------------|------------------|--------------------------------|
| Drift < 0.1        | Stable            | No action needed               |
| 0.1 ≤ Drift ≤ 0.2  | Moderate Drift    | Investigate if recurring       |
| Drift > 0.2        | High Drift        | Immediate attention required   |

---

## 🔗 Related Links

- [Feature Binning](../binningstrategies.md)
- [Feature Stability API Reference](../reference/calculate_all_features_drift.md)
- [Get Bin Edges API](../reference/get_bin_edges.md)
