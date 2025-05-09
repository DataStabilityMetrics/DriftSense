
# 📦 Installation Guide

Welcome to the **DriftSense** installation guide. Follow the instructions below to install the package and set up your environment for using the binning and stability evaluation utilities.

---

## ✅ Requirements

Before installing the package, ensure the following dependencies are available:

- `Python 3.7+`
- `numpy`
- `scikit-learn`
- `pytest` *(optional, for testing purposes)*

---

## 📥 Installation Steps

### Option 1: Install via pip (recommended for stable version)

```bash
pip install DriftSense
```

---

### Option 2: Clone from GitHub and install locally

```bash
git clone https://github.com/DataStabilityMetrics/DriftSense.git
cd DriftSense
pip install -r requirements.txt
```

---

## 🧪 Running Tests

To ensure DriftSense is installed correctly, run the unit tests:

```bash
pytest tests/
```

> ✅ All test cases cover various binning strategies and edge conditions, such as NaNs, empty input, and invalid types.

---

## 📚 Next Steps

- Go to the [Usage Guide](./usage/index.md) for tutorials and code examples in ML evaluation or monitoring system
- Explore [API Reference](./reference/api_index.md) to integrate it into ML evaluation or monitoring system
- Check out the [Home Page](./index.md) for a conceptual overview of the drift or stability metrics
