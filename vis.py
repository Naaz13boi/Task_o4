import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

def eda_and_visualize_with_polars(file_path, pdf_path="eda_report.pdf"):
    df = pl.read_csv(file_path)
    # Remove UNITID from numerical columns
    num_cols = [
        col for col, dtype in zip(df.columns, df.dtypes)
        if dtype in (pl.Float32, pl.Float64, pl.Int32, pl.Int64, pl.UInt32, pl.UInt64)
        and col != "UNITID"
    ]

    print("Numerical columns detected:", num_cols)
    print("=" * 40)

    stats = {
        "mean": [],
        "median": [],
        "min": [],
        "max": [],
    }

    # Collect stats for each column
    for col in num_cols:
        col_data = df[col].drop_nulls()
        stats["mean"].append(col_data.mean())
        stats["median"].append(col_data.median())
        stats["min"].append(col_data.min())
        stats["max"].append(col_data.max())

        # Print stats
        print(f"Column: {col}")
        print(f"  Min: {col_data.min()}")
        print(f"  Max: {col_data.max()}")
        print(f"  Mean: {col_data.mean()}")
        print(f"  Median: {col_data.median()}")
        # Mode calculation
        value_counts = col_data.value_counts().sort("count", descending=True)
        max_count = value_counts["count"][0]
        modes = value_counts.filter(pl.col("count") == max_count)[col].to_list()
        if len(modes) == 1:
            print(f"  Mode: {modes[0]}")
        else:
            print(f"  Mode: {modes} (multiple modes)")
        print("-" * 30)

    # Start PDF export
    with PdfPages(pdf_path) as pdf:

        # Bar charts for mean, median, min, max
        plt.figure(figsize=(14, 8))
        plt.subplot(2, 2, 1)
        sns.barplot(x=num_cols, y=stats["mean"])
        plt.title("Mean of Numerical Columns")
        plt.xticks(rotation=90)

        plt.subplot(2, 2, 2)
        sns.barplot(x=num_cols, y=stats["median"])
        plt.title("Median of Numerical Columns")
        plt.xticks(rotation=90)

        plt.subplot(2, 2, 3)
        sns.barplot(x=num_cols, y=stats["min"])
        plt.title("Min of Numerical Columns")
        plt.xticks(rotation=90)

        plt.subplot(2, 2, 4)
        sns.barplot(x=num_cols, y=stats["max"])
        plt.title("Max of Numerical Columns")
        plt.xticks(rotation=90)

        plt.tight_layout()
        pdf.savefig()
        plt.close()

        # Boxplots for each column
        pd_df = df.select(num_cols).to_pandas()
        plt.figure(figsize=(14, 6))
        sns.boxplot(data=pd_df)
        plt.title("Boxplot of Numerical Columns")
        plt.xticks(rotation=90)
        plt.tight_layout()
        pdf.savefig()
        plt.close()

        # Correlation heatmap
        corr = pd_df.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        pdf.savefig()
        plt.close()

        # --- Custom Sum Comparison Chart ---
        total_col = "EFYTOTLT"
        compare_cols = [
            "EFYAIANT", "EFYASIAT", "EFYBKAAT", "EFYHISPT", "EFYNHPIT", "EFYWHITT"
        ]
        compare_cols = [col for col in compare_cols if col in df.columns]

        total_sum = df[total_col].sum()
        sums = [df[col].sum() for col in compare_cols]
        percentages = [s / total_sum * 100 for s in sums]
        labels = compare_cols

        labels = ["EFYTOTLT (Total)"] + labels
        percentages = [100.0] + percentages

        plt.figure(figsize=(10, 6))
        sns.barplot(x=labels, y=percentages)
        plt.title("Sum Comparison as Percentage of Total (EFYTOTLT)")
        plt.ylabel("Percentage of Total (%)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        pdf.savefig()
        plt.close()

        # Optionally, add histograms for each column (can be commented out if too many columns)
        #for col in num_cols:
        #    plt.figure(figsize=(6, 4))
        #    sns.histplot(pd_df[col].dropna(), kde=True)
        #    plt.title(f"Histogram of {col}")
        #    plt.xlabel(col)
        #    plt.ylabel("Frequency")
        #    plt.tight_layout()
        #    pdf.savefig()
        #    plt.close()

    print(f"All plots have been saved to {pdf_path}")

# Example usage:
eda_and_visualize_with_polars("D:/Data/Task_4_data/effy2023.csv", pdf_path="eda_report.pdf")