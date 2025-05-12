from typing import Union, Dict, Tuple
import pandas as pd

from .calculate_feature_drift import calculate_feature_drift


def calculate_all_features_drift(
    reference_df: pd.DataFrame,
    new_df: pd.DataFrame,
    bins: Union[int, Dict[str, list]] = 10,
    method: str = 'equal_freq'
) -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]:
    
    """
    Compute drift/stability for all features in the dataframe.

    Parameters:
    - reference_df (DataFrame): Baseline dataset.
    
    - new_df (DataFrame): New dataset. Monitoring/Test/Validation.
    
    - bins (int or dict): Number of bins (for numerical) or category handling.
    
    - method (str): Binning method ('equal_width', 'equal_freq', 'adaptive', 'kmeans', 'domain').

    Returns:
    
    - Tuple containing:
    
        1. DataFrame with Drift (CSI/PSI) values for all features.
        
        2. Dictionary of Drift (CSI/PSI) dataFrames for all features.
        
    """

    if not isinstance(reference_df, pd.DataFrame) or not isinstance(new_df, pd.DataFrame):
        raise ValueError("Both inputs should be pandas DataFrames.")

    csi_results = []
    detailed_csi_dfs = {}

    for col in reference_df.columns:
        if col not in new_df.columns:
            continue  # Skip columns missing in new dataset

        reference = reference_df[col].dropna()
        actual = new_df[col].dropna()

        # Skip if column is empty in either dataset
        if len(reference) == 0 or len(actual) == 0:
            continue

        ## ADD CHUNK HERE - FOR SPECIFIC BINNING FOR ALL COLUMNS
        if method == 'domain':
            # Expecting dict of bins: {col_name: bin_edges or categories}
            if not isinstance(bins, dict) or col not in bins:
                raise ValueError(f"Bins for column '{col}' must be provided as a list in a dictionary for method='domain'")

            domain_bins = bins[col]
            drift_output = calculate_feature_drift(reference, actual, bins=domain_bins, method=method)
        else:
            drift_output = calculate_feature_drift(reference, actual, bins=bins, method=method)
        
        csi_results.append({"Feature": col, "Binning Strategy": drift_output["Binning Strategy"], "Drift": drift_output['Drift Score']})
        
        detailed_csi_dfs[col] = drift_output['Drift DataFrame']
        #except Exception as e:
        #    print(f"Skipping column {col} due to error: {e}")
    csi_results = pd.DataFrame(csi_results).sort_values(by="Drift", ascending=False).reset_index()
    #detailed_csi_dfs = pd.DataFrame(detailed_csi_dfs)   
    return csi_results, detailed_csi_dfs
