# 🧠 Feature Binning

This section explains how to bin features using the available methods in `DriftSense`.

---

## Equal Width Example

```python
from driftsense import get_bin_edges

edges = get_bin_edges([1, 2, 3, 4, 5], bins=3, method="equal_width")
print(edges)  # [1.0, 3.0, 5.0]
```

---

## Adaptive Binning Example

```python
from driftsense import get_bin_edges_csi
import numpy as np

data = np.array([1.2, 3.4, 2.1, 5.7])
target = np.array([0, 0, 1, 1])

edges = get_bin_edges(data, bins=3, method="adaptive", target=target)
print("Bin edges:", edges)
```

---

## 🔗 Related Links
- [API: get_bin_edges](../reference/get_bin_edges.md)
