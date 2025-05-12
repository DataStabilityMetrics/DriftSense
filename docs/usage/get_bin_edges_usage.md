# Feature Binning

This section explains how to bin features using the available methods in `DriftSense`.

---

## Equal Width Binning Example 1

```python
from driftsense import get_bin_edges
get_bin_edges([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5], bins=3, method="equal_width")
```

**Output:**
```text
array([1., 2.33333333, 3.66666667, 5.])
```

---

## Equal Frequency Binning Example 1
```python
from driftsense import get_bin_edges
get_bin_edges([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5], bins=3, method="equal_freq")

```

**Output:**
```text
array([1., 2.66666667, 4., 5.])
```

---

## Adaptive Binning Example

```python
from driftsense import get_bin_edges
import numpy as np

data = np.array([1.2, 3.4, 2.1, 5.7])
target = np.array([0, 0, 1, 1])

edges = get_bin_edges(data, bins=3, method="adaptive", target=target)
print(edges)
```

**Output:**
```text
[1.64999998 2.75]
```

---

## Related Links
- [API: get_bin_edges](../reference/get_bin_edges.md)
