
# API: get_bin_edges

::: driftsense.get_bin_edges
    options:
      show_source: false
      show_signature: true
      show_root_heading: true
      members_order: source
      docstring_style: google

---

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `data` | `np.ndarray` | ✅ Yes | Input array of numeric values |
| `bins` | `int` | ✅ Yes | Number of bins |
| `method` | `str` | ✅ Yes | Binning method: `"equal"`, `"quantile"`, or `"adaptive"` |
| `target` | `Optional[np.ndarray]` | ❌ Only for `"adaptive"` | Target array used for supervised binning |

---

## Returns

- `np.ndarray`: An array of bin edge values, excluding the min and max of the data.

---

## Usage Examples

### 1. Equal-width Binning

```python
from driftsense import get_bin_edges
import numpy as np

data = np.array([1, 5, 10, 15, 20, 25, 30])
bin_edges = get_bin_edges(data, bins=3, method="equal_width")
print(bin_edges)
```

**Output:**
```text
[1, 10, 20, 30]
```

---

### 2. Equal-frequency (quantile) Binning

```python
bin_edges = get_bin_edges(data, bins=3, method="equal_freq")
print(bin_edges)
```

**Output:**
```text
[ 1.         10.66666667 20.33333333 30.        ]
```

---

### 3. Adaptive Binning with Target Variable

```python
target = np.array([0, 0, 1, 1, 0, 1, 0])
bin_edges = get_bin_edges(data, bins=3, method="adaptive", target=target)
print(bin_edges)
```

**Output (example):**
```text
[ 7.5 17.5]
```

---

## Notes

- If using `"adaptive"`, the `target` argument must be passed. Current release of `DriftSense` supports `adaptive` method for binary target variable only.
- The returned list contains bin *edges*, not bin *counts*.
- NaN values in `data` are automatically filtered out before binning.
- The bin edges returned are always sorted and do not include `min` or `max` bounds.

---

## See Also

- [Drift Usage Guide](../usage/index.md)
