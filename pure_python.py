import csv
from statistics import mean, median, mode, StatisticsError
from collections import Counter



def is_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def eda_on_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        data = list(reader)

    # Transpose data to columns
    columns = list(zip(*data))
    num_cols = []
    num_col_indices = []

    # Detect numerical columns by checking all values (excluding empty strings)
    for idx, col in enumerate(columns):
        if all(is_number(val) for val in col if val.strip() != ''):
            num_cols.append(headers[idx])
            num_col_indices.append(idx)

    print("Numerical columns detected:", num_cols)
    print("=" * 40)

    for col_name, idx in zip(num_cols, num_col_indices):
        col_data = [float(val) for val in columns[idx] if is_number(val)]
        if not col_data:
            print(f"{col_name}: No numerical data found.")
            continue

        print(f"Column: {col_name}")
        print(f"  Min: {min(col_data)}")
        print(f"  Max: {max(col_data)}")
        print(f"  Mean: {mean(col_data)}")
        print(f"  Median: {median(col_data)}")
        try:
            print(f"  Mode: {mode(col_data)}")
        except StatisticsError:
            counts = Counter(col_data)
            max_count = max(counts.values())
            modes = [k for k, v in counts.items() if v == max_count]
            print(f"  Mode: {modes} (multiple modes)")
        print("-" * 30)

# Example usage:
eda_on_csv("D:/Data/Task_4_data/effy2023.csv")