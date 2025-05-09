import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from typing import Union, List, Optional

def get_bin_edges(reference: Union[List[float], np.ndarray], 
                      bins: Union[int, List[float]] = 10, 
                      method: str = "equal_width", 
                      target: Optional[Union[List[int], np.ndarray]] = None
                     ) -> Union[np.ndarray, List[float]]:
    """
    Compute bin edges for numerical variables or categorical variables based on the specified binning method.

    This function is used for binning continuous variables into discrete intervals, 
    commonly used in statistical metrics for stability evaluation (such as CSI - Characteristic Stability Index or PSI - Population Stability Index).
    
    This function supports multiple binning strategies.


    Parameters:
    -----------
    - reference : array-like
        The input data (typically from the expected or reference dataset) to compute bin edges on.
        Should be numeric for most methods, but may be categorical for 'domain' binning.
        
    - bins : int or list
        Number of bins to create (if method is numeric), or a list of bin edges/categories (only used if `method="domain"`).
        If method is numeric ('equal_width', 'equal_freq', etc.), this is the number of bins.
        If method='domain', this must be a list of bin edges or category labels.

    - method : str, default="equal_width"
    
        The binning strategy to use. Supported options:
        
         - "equal_width" : Divides the numeric range into equal-width intervals.
        
         - "equal_freq"  : Divides numeric data such that each bin contains an approximately equal number of samples.
        
         - "adaptive"    : Uses a Decision Tree classifier to find splits that best separate the numeric data.
        
         - "kmeans"      : Applies k-means clustering and uses the cluster centers as bin edges for numeric data.
        
         - "domain"      : Accepts a user-defined list of bin edges or category labels directly (numeric or categorical).

    - target : array-like, optional
        
        Required if method='adaptive'. Target variable used to guide DecisionTree-based binning.
    
    Returns:
    --------
    list or np.ndarray

        The list of bin edges (or categorical bin labels) to be used for binning.

    Raises:
    -------
    - ValueError:
        
	If the input is empty, or if method is invalid.
        
    - TypeError:

        If the input is not numeric where required, or if domain bins are improperly formatted.

    Examples:
    ---------
    >>> get_bin_edges([1, 2, 3, 4, 5], bins=2, method="equal_width")
    array([1., 3., 5.])

    >>> get_bin_edges([10, 20, 30, 40, 50], bins=2, method="equal_freq")
    array([10., 30., 50.])

    >>> get_bin_edges([1, 2, 3, 4, 5], bins=[0, 2, 5], method="domain")
    [0, 2, 5]
    """

    # ---- Domain Binning: supports categorical or numeric ----
    if method == "domain":
        # Validate bins is list-like
        if not isinstance(bins, (list, np.ndarray)):
            raise TypeError("For method='domain', 'bins' must be a list or NumPy array.")
        if len(bins) < 2:
            raise ValueError("At least two bin edges/categories are required for 'domain' binning.")
        # Return user-defined order as-is (no sorting)
        return  np.asarray(bins)
    
    # Convert to NumPy array for consistency
    reference = np.asarray(reference)

    # Handle empty input
    if reference.size == 0:
        raise ValueError("Input 'reference' data must not be empty.")

    # Validate that reference data contains only numeric values
    if method != "domain" and not np.issubdtype(reference.dtype, np.number):
        raise TypeError("Input 'reference' data must contain only numeric values.")

    # ---- Binning Methods ----
    # Remove NaNs if present (skip for 'domain' since bins are user-defined)
    if method not in ["domain", "adaptive"]:
        reference = reference[~np.isnan(reference)]

        # Check again after removing NaNs
        if reference.size == 0:
            raise ValueError("Input 'reference' data contains only NaN values.")
    
    # ---- Equal Width Binning ----
    if method == "equal_width":
        reference = reference[~np.isnan(reference)]
        if reference.size == 0:
            raise ValueError("Input 'reference' data contains only NaN values.")
            
        # Create equally spaced intervals from min to max
        return np.linspace(min(reference), max(reference), bins + 1)

    # ---- Equal Frequency Binning ----
    elif method == "equal_freq":
        reference = reference[~np.isnan(reference)]
        if reference.size == 0:
            raise ValueError("Input 'reference' data contains only NaN values.")
        # Use percentiles to ensure each bin has approximately the same number of samples
        return np.percentile(reference, np.linspace(0, 100, bins + 1))
    
    # ---- Adaptive Binning (TREE-BASED) ----
    elif method == "adaptive":
        if target is None:
            raise ValueError("For method='adaptive', a target variable must be provided.")

        reference = np.asarray(reference)
        target = np.asarray(target)

        if reference.shape[0] != target.shape[0]:
            raise ValueError("reference data and target data must have the same length.")

        if np.any(np.isnan(target)):
            raise ValueError("Target contains NaNs, which are not allowed.")

        # Remove rows where reference data is NaN
        valid_mask = ~np.isnan(reference)
        reference_clean = reference[valid_mask]
        target_clean = target[valid_mask]

        if reference_clean.size == 0:
            raise ValueError("Input 'reference' data contains only NaN values.")
        
        # Reshape for sklearn input
        X = reference_clean.reshape(-1, 1)
        # target to let tree find splits
        y = target_clean
        
        # Fit decision tree
        tree = DecisionTreeClassifier(max_leaf_nodes=bins, random_state=42)
        tree.fit(X, y)
        # Extract and return sorted thresholds
        thresholds = tree.tree_.threshold
        print(thresholds)
        return np.sort(thresholds[thresholds > 0])  # Remove invalid splits (-2) 

    # ---- K-Means Based Binning -----
    elif method == "kmeans":
        reference = reference[~np.isnan(reference)]
        if reference.size == 0:
            raise ValueError("Input 'reference' data contains only NaN values.")

        # Apply k-means clustering
        data = np.array(reference).reshape(-1, 1)
        kmeans = KMeans(n_clusters=bins, random_state=42)
        kmeans.fit(data)
        # Use sorted cluster centers as split points
        return np.sort(kmeans.cluster_centers_.flatten())
    
    # ---- Invalid Binning Method -----
    else:
        raise ValueError(f"Invalid binning method: '{method}'. "
                         "Choose from 'equal_width', 'equal_freq', 'adaptive', 'kmeans', or 'domain'.")