
# Frequently Asked Questions

Here are some of the most commonly asked questions about the `DriftSense` package.

---

### What is the purpose of the DriftSense package?

*The package is designed to monitor the stability or drift of features, targets, and model predictions over time using techniques like CSI (Characteristic Stability Index) and PSI (Population Stability Index).*
*This is especially critical in regulated industries like banking and finance.*

---

### What are CSI and PSI?
*CSI and PSI are statistical indices used to quantify the shift between two data distributions or populations. CSI is typically used for continuous/categorical data comparisons while PSI is often used for model monitoring in production systems.*

---

### Do I need to bin the features before calculating stability?
*No. You do not need to bin the feature before calculating stability or drift. `DriftSense` function uses `get_bin_edges` function internally to compute the bins as per binning methods.* 
*However, you can use function `get_bin_edges()` provided in the package to get the bin values for different binning methods.* 

---

### Can I use this package for both classification and regression models?
*Yes, you can monitor prediction drift for both classification and regression models by applying binning and drift method of choice* 
*You can use `calculate_feature_drift` for single feature or `calculate_all_features_drift` for all features in dataframe including target and prediction (if available)* 

---

### What happens if I pass NaN values to the functions?
*NaN values are automatically filtered out for most functions except domain-specific binning. It's recommended to clean or preprocess your data before applying stability checks.* 

---

### How often should I monitor for drift?
*It's common practice to monitor data drift weekly or monthly, depending on the criticality of the machine learning system. Regulatory guidelines (US SR11/7, PRA) and model materiality may also mandate monitoring frequencies.* 

---
