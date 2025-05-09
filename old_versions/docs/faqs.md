
# 💬 Frequently Asked Questions (FAQs)

Here are some of the most commonly asked questions about the `DriftSense` package.

---

### ❓ Q1: What is the purpose of the DriftSense package?
**A:** The package is designed to monitor the stability or drift of features, targets, and model predictions over time using techniques like CSI (Characteristic Stability Index) and PSI (Population Stability Index). This is especially critical in regulated industries like banking and finance.

---

### ❓ Q2: What are CSI and PSI?
**A:** CSI and PSI are statistical indices used to quantify the shift between two distributions. CSI is typically used for continuous/categorical data comparisons while PSI is often used for model monitoring in production systems.

---

### ❓ Q3: Do I need to bin the features before calculating stability?
**A:** Yes. Stability metrics such as CSI and PSI require input distributions to be binned. You can use functions like `get_bin_edges()` or `get_bin_edges_csi()` provided in the package.

---

### ❓ Q4: Can I use this package for both classification and regression models?
**A:** Yes. For classification, you can monitor class-wise prediction drift. For regression, you can bin prediction ranges and then apply CSI/PSI.

---

### ❓ Q5: What happens if I pass NaN values to the functions?
**A:** NaN values are automatically filtered out for most functions except domain-specific binning. It's recommended to clean or preprocess your data before applying stability checks.

---

### ❓ Q6: How often should I monitor for drift?
**A:** It's common practice to monitor data drift weekly or monthly, depending on the criticality of the system. Regulatory guidelines may also mandate monitoring frequencies.

---
