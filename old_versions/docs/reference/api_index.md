# 📖 API Overview

Welcome to the **DriftSense** API Reference Guide. This section provides technical documentation for all core functions in the package.

Use this guide to understand the function signatures, expected parameters, and example usages. This is especially helpful when integrating the package into larger projects or developing automation and monitoring tools.

---

## 📂 Modules Covered

| Module | Description |
|--------|-------------|
| `get_bin_edges` | Utilities for calculating bin edges using various binning strategies. |
| `calculate_feature_drift` | Computes drift or stability score (e.g., CSI or PSI) for feature and target variable. |
| `calculate_all_features_drift` | Computes drift or stability for all features in the dataframe (including predictions). |
| `create_drift_report` | Generates drift or stability report of feature columns and target column in the dataset. |

---

## 🧩 API Documentation Topics

### 🔹 Binning Function

- [`get_bin_edges`](./get_bin_edges.md)  
  Calculate bin edges using strategies like equal width binning, equal frequency binning, adaptive, and more.



### 🔹 Stability Function

- [`calculate_feature_drift`](./calculate_feature_drift.md)  
  Evaluates drift between reference and actual datasets. can be used for features, target variable as well as predictions

- [`calculate_all_features_drift`](./calculate_all_features_drift.md)  
  Evaluates drift for all features columns (e.g. CSI) including target column and predictions (e.g. CSI/PSI) .

### 🔹 Stability Report

- [`create_drift_report`](./create_drift_report.md)
  
  - generates drift or stability report of feature columns and target column in the dataset. 
  
  - Provides the checks to verify the numbers of records matches with the total counts in the individual feature drift calculation.

---

## 📘 Notes

- For adaptive binning strategy, `target` variable are required.
- For domain-specific binning, list of bin edges should be provided.
- Current supports PSI and CSI methods ffor drift metrics. 
- Future releases will include additional methods of drift evaluation. 

---

## 🧭 Navigation

- [Home](../index.md)
- [Usage Guide](../usage/index.md)
- [Installation](../installation.md)
