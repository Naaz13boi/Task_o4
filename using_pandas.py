import pandas as pd

def eda_on_csv_with_pandas(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Select only numerical columns
    num_df = df.select_dtypes(include='number')
    num_cols = num_df.columns.tolist()
    
    print("Numerical columns detected:", num_cols)
    print("=" * 40)
    
    for col in num_cols:
        col_data = num_df[col].dropna()
        print(f"Column: {col}")
        print(f"  Min: {col_data.min()}")
        print(f"  Max: {col_data.max()}")
        print(f"  Mean: {col_data.mean()}")
        print(f"  Median: {col_data.median()}")
        # Mode can return multiple values, so handle accordingly
        modes = col_data.mode()
        if len(modes) == 1:
            print(f"  Mode: {modes.iloc[0]}")
        else:
            print(f"  Mode: {modes.tolist()} (multiple modes)")
        print("-" * 30)

# Example usage:
eda_on_csv_with_pandas("D:/Data/Task_4_data/effy2023.csv")