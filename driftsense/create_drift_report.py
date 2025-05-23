from typing import Dict
import pandas as pd

def create_drift_report(
    summary_df: pd.DataFrame,
    detailed_dfs: Dict[str, pd.DataFrame],
    file_path: str = "Drift_Report.html",
    drift_threshold: float = 0.25
) -> None:
    
    """
    Save the summary and detailed Drift DataFrames into a single HTML file with Pass/Fail test.

    Parameters:
    - summary_df (DataFrame): Summary Drift values per feature.
    
    - detailed_dfs (dict): Dictionary of detailed Drift DataFrames.
    
    - file_path (str): Path where the output HTML file will be saved to.
    
    - drift_threshold (float): Drift threshold for test pass/fail.

    Returns:
    - None (writes an HTML file to disk)
    
    """
    
    # Add Pass/Fail column
    summary_df = summary_df.copy()
    summary_df["Test Result"] = summary_df["Drift"].apply(lambda x: "Pass" if x <= drift_threshold else "Fail")

    with open(file_path, "w") as f:
        f.write("<html><head><title>Drift Report</title>")
        f.write("""
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            h2 { color: #2a6592; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 40px; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
            th { background-color: #f2f2f2; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            .pass { background-color: #d4edda; color: #155724; font-weight: bold; }
            .fail { background-color: #f8d7da; color: #721c24; font-weight: bold; }
        </style>
        """)
        f.write("</head><body>")

        # Summary Table with conditional formatting
        f.write("<h2>Drift Summary</h2>")
        f.write("<table>")
        f.write("<tr><th>Feature</th><th>Drift</th><th>Test Result</th></tr>")
        for _, row in summary_df.iterrows():
            css_class = "pass" if row["Test Result"] == "Pass" else "fail"
            f.write(
                f"<tr>"
                f"<td>{row['Feature']}</td>"
                f"<td>{row['Drift']:.4f}</td>"
                f"<td class='{css_class}'>{row['Test Result']}</td>"
                f"</tr>"
            )
        f.write("</table>")

        # Detailed Drift per feature
        for feature, df in detailed_dfs.items():
            f.write(f"<h2>Drift Detail for Feature: {feature}</h2>")
            f.write(df.to_html(index=False, float_format="%.4f", border=0))

        f.write("</body></html>")

    print(f"Drift report with results saved to: {file_path}")
