# DriftSense 📊

Welcome to the **DriftSense** documentation!

The `DriftSense` package is designed to calculate the drift or stability of data distributions across datasets. This is a critical metric for evaluating changes in data distributions over time and ensuring the continued validity of AI/ML models.

---

## 🔍 Overview

This package enables:

- Binning of features using multiple strategies
- Evaluation of feature, target, and model stability
- Regulatory compliance support (e.g., SR11/7 in banking)

---


## 🚀 Features

- This library supports multiple binning strategies:
  - 🔢 **Equal Width Binning** - Evenly spaced bins between the min and max of the data.
  - 📈 **Equal Frequency (Quantile) Binning** - Each bin contains roughly the same number of data points.
  - 🌳 **Adaptive Binning** - Supervised binning using decision trees, requiring a target variable.
  - 🎯 **K-Means Clustering** - Binning using clustering especially K-Means Clustering.
  - 📦 **Domain-defined bins** - User specified binnings for numeric or categorical.

- Handles missing values (`NaN`) safely
- Suitable for numeric and categorical variables
- Lightweight and dependency-friendly

---

## 📦 Requirements

To use this package, you’ll need the following dependencies installed:

- `numpy`
- `scikit-learn`
- `pytest` *(optional, for testing)*

---

## 📥 Installation Steps

### Option 1: Install via pip (recommended for stable version)

```bash
pip install DriftSense
```

---

### Option 2: Clone from GitHub and install locally

```bash
git clone https://github.com/datastabilitymetrics/DriftSense.git
cd DriftSense
pip install -r requirements.txt
```

---

## 📚 Get Started

Quickly explore powerful tools to ensure **data stability**, detect and monitor **data drift**, **model drift** — all in one seamless package.

[📚 Usage Guide](./docs/usage/index.md)				

[🛠️ API Reference](./docs/reference/api_index.md)


## 🧠 Usage Example

```python
from driftsense import get_bin_edges

# Example 1: Equal Width
bins = get_bin_edges([1, 2, 3, 4, 5], bins=2, method="equal_width")
print(bins)  
# [1. 3. 5.]

# Example 2: Adaptive binning with a target
data = [1, 2, 3, 4, 5]
target = [0, 0, 1, 1, 1]
bins = get_bin_edges(data, bins=2, method="adaptive", target=target)
print(bins)
```
## 🧪 Run Unit Tests

```python
pytest tests/
```
All test cases are located in the tests/ directory and cover various binning methods and edge cases, including:

- Empty input
- Invalid types
- Missing values
- Categorical bins

## 📚 Documentation Navigation

- [📚 Usage Guide](./docs/usage/index.md)	

- [🛠️ API Reference](./docs/reference/api_index.md)

- [🛠️ Contributing](./docs/CONTRIBUTING.md)

- [🧪 Unit Tests](./docs/tests/)

- [📜 License](./docs/LICENSE)


## Why DriftSense?

- Easy to integrate in ML pipelines
- Powerful stability/drift metrics
- Open source and community driven


## 🙋 FAQ

Q: What happens if I pass NaNs to the function?
A: NaNs are automatically filtered for all methods except domain.

Q: Is this tool suitable for categorical variables?
Yes — use method="domain" and pass a list of category labels.

Q: Can I use this for live model monitoring?
A: Absolutely! It's designed for robust performance and interpretability.

Q: What’s the difference between equal_freq and equal_width?
A:
    - equal_width: Divides the range evenly.
    - equal_freq: Each bin contains roughly the same number of samples.