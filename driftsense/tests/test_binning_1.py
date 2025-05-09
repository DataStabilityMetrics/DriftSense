import numpy as np
import pytest
from get_bin_edges_csi import get_bin_edges_csi  # Replace with your actual module name


def test_equal_width_binning():
    expected = [1, 2, 3, 4, 5]
    result = get_bin_edges(expected, bins=2, method="equal_width")
    expected_result = np.array([1.0, 3.0, 5.0])
    np.testing.assert_allclose(result, expected_result, rtol=1e-5)


def test_equal_freq_binning():
    expected = [10, 20, 30, 40, 50]
    result = get_bin_edges(expected, bins=2, method="equal_freq")
    expected_result = np.array([10.0, 30.0, 50.0])
    np.testing.assert_allclose(result, expected_result, rtol=1e-5)


def test_domain_binning():
    expected = [1, 2, 3]
    bins = [0, 2, 5]
    result = get_bin_edges(expected, bins=bins, method="domain")
    assert result == [0, 2, 5]


def test_kmeans_binning():
    data = [1, 2, 3, 10, 11, 12]
    result = get_bin_edges(data, bins=2, method="kmeans")
    assert len(result) == 2
    assert all(isinstance(v, float) for v in result)


def test_domain_invalid_type():
    with pytest.raises(TypeError):
        get_bin_edges([1, 2, 3], bins=3.5, method="domain")


def test_domain_too_few_bins():
    with pytest.raises(ValueError):
        get_bin_edges([1, 2, 3], bins=[1], method="domain")


def test_empty_input_raises():
    with pytest.raises(ValueError):
        get_bin_edges([], bins=2, method="equal_width")


def test_nan_only_input():
    with pytest.raises(ValueError):
        get_bin_edges([np.nan, np.nan], bins=3, method="equal_width")


def test_invalid_method():
    with pytest.raises(ValueError):
        get_bin_edges([1, 2, 3], bins=3, method="unsupported_method")


def test_non_numeric_expected():
    with pytest.raises(TypeError):
        get_bin_edges(["a", "b", "c"], bins=2, method="equal_freq")


def test_adaptive_binning_basic():
    expected = [1, 2, 3, 4, 5, 6, 7]
    target = [0, 0, 1, 1, 1, 0, 0]
    result = get_bin_edges(expected, bins=3, method="adaptive", target=target)
    assert isinstance(result, np.ndarray)
    assert len(result) <= 2  # max_leaf_nodes=3 -> max 2 splits


def test_adaptive_binning_with_nans():
    expected = [1, 2, np.nan, 4, 5, np.nan, 7]
    target = [0, 0, 1, 1, 1, 0, 0]
    result = get_bin_edges(expected, bins=3, method="adaptive", target=target)
    assert isinstance(result, np.ndarray)
    assert len(result) <= 2


def test_adaptive_target_required():
    expected = [1, 2, 3]
    with pytest.raises(ValueError):
        get_bin_edges(expected, bins=2, method="adaptive")


def test_adaptive_target_shape_mismatch():
    expected = [1, 2, 3, 4]
    target = [0, 1]
    with pytest.raises(ValueError):
        get_bin_edges(expected, bins=2, method="adaptive", target=target)
