import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from typing import Union, List, Optional

def calculate_feature_drift(
    reference: Union[List[float], np.ndarray], 
    actual: Union[List[float], np.ndarray], 
    bins: Union[int, List[float]] = 10, 
    method: str ="equal_freq"

)-> dict:
    """
    Calculate Characteristic/Population Stability Index (CSI/PSI) for a given variable.
    
    Parameters:
    - reference (array-like): Baseline dataset values.
    - actual (array-like): New dataset values.
    - bins (int or list): Number of bins (if numeric) or predefined categories.
    - method (str): Binning strategy for numerical data ('equal_width', 'equal_freq', 'adaptive', 'kmeans', or 'domain').

    Returns:
    - dict: Feature Drift dataframe containing the actual count, reference count, actual percentage, reference percentage, drift score for each bin and final drift score is aggregate sum of bin-wise drift score.
    """
    reference = np.array(reference)
    actual = np.array(actual)

    # Determine if variable is categorical or numerical
    #is_categorical = reference.dtype == 'object' or len(np.unique(reference)) < bins
    is_categorical = reference.dtype == 'object'


    if is_categorical and method != 'domain':
        # Categorical variable binning
        unique_bins = np.unique(np.concatenate([reference, actual]))
        reference_counts = np.array([np.sum(reference == cat) for cat in unique_bins])
        actual_counts = np.array([np.sum(actual == cat) for cat in unique_bins])
        min_bins, max_bins = unique_bins, unique_bins  # Same for categorical values

    elif is_categorical and method == 'domain':
        # Categorical variable binning
        unique_bins = np.unique(bins)
        reference_counts = np.array([np.sum(reference == cat) for cat in unique_bins])
        actual_counts = np.array([np.sum(actual == cat) for cat in unique_bins])
        min_bins, max_bins = unique_bins, unique_bins  # Same for categorical values    
        
    else:
        # Numerical variable binning
        bin_edges = get_bin_edges(reference, bins, method)
        bin_edges = np.unique(bin_edges)

        # Ensure full coverage by setting first bin to -inf and last to +inf
        if method != 'domain':
            bin_edges[0] = -np.inf
            bin_edges[-1] = np.inf

        reference_counts, _ = np.histogram(reference, bins=bin_edges)
        actual_counts, _ = np.histogram(actual, bins=bin_edges)
        min_bins = bin_edges[:-1]
        max_bins = bin_edges[1:]

    # Normalize counts to proportions
    reference_perc = reference_counts / np.sum(reference_counts)
    actual_perc = actual_counts / np.sum(actual_counts)

    # Avoid division by zero
    epsilon = 1e-10
    reference_perc = np.where(reference_perc == 0, epsilon, reference_perc)
    actual_perc = np.where(actual_perc == 0, epsilon, actual_perc)

    # Compute CSI
    csi_values = (actual_perc - reference_perc) * np.log(actual_perc / reference_perc)

    # Create CSI DataFrame
    csi_df = {
        "Min Bin": min_bins,
        "Max Bin": max_bins,
        "Reference Count": reference_counts,
        "Actual Count": actual_counts,
        "Reference %": reference_perc,
        "Actual %": actual_perc,
        "CSI Value": csi_values
    }

    total_csi = np.sum(csi_values)
    
    return(
        {
        "Binning Strategy": method if not is_categorical or method=='domain' else "categorical",
        "Drift DataFrame": pd.DataFrame(csi_df),
        "Drift Score": total_csi
        }
    )



