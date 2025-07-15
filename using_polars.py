import polars as pl

def eda_on_csv_with_polars(file_path):
    # Read the CSV file into a Polars DataFrame
    df = pl.read_csv(file_path)
    
    # Select only numerical columns
    num_cols = [col for col, dtype in zip(df.columns, df.dtypes)
                if dtype in (pl.Float32, pl.Float64, pl.Int32, pl.Int64, pl.UInt32, pl.UInt64)]
    
    print("Numerical columns detected:", num_cols)
    print("=" * 40)
    
    for col in num_cols:
        col_data = df[col].drop_nulls()
        print(f"Column: {col}")
        print(f"  Min: {col_data.min()}")
        print(f"  Max: {col_data.max()}")
        print(f"  Mean: {col_data.mean()}")
        print(f"  Median: {col_data.median()}")
        # Mode: Polars does not have a built-in mode, so we compute it manually
        value_counts = col_data.value_counts().sort("count", descending=True)
        max_count = value_counts["count"][0]
        modes = value_counts.filter(pl.col("count") == max_count)[col].to_list()
        if len(modes) == 1:
            print(f"  Mode: {modes[0]}")
        else:
            print(f"  Mode: {modes} (multiple modes)")
        print("-" * 30)

# Example usage:
eda_on_csv_with_polars("D:/Data/Task_4_data/effy2023.csv")