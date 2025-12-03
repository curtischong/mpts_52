# %%
import pandas as pd

# %%
# Try to load the mp_time_split dataset
# The dataset is provided by matbench-genmetrics library
# Try multiple possible locations
urls_to_try = [
    "https://raw.githubusercontent.com/sparks-baird/matbench-genmetrics/main/data/mp_time_split.csv",
    "https://raw.githubusercontent.com/sparks-baird/matbench-genmetrics/main/matbench_genmetrics/data/mp_time_split.csv",
]

df = None
for url in urls_to_try:
    try:
        print(f"Trying to download from: {url}")
        df = pd.read_csv(url)
        print(f"Dataset downloaded successfully! Shape: {df.shape}")
        break
    except Exception as e:
        print(f"Failed: {e}")
        continue

if df is None:
    # If direct download fails, try using the library's API
    try:
        from matbench_genmetrics.mp_time_split import get_mp_time_split_df

        df = get_mp_time_split_df()
        print(f"Dataset loaded via library API! Shape: {df.shape}")
    except ImportError:
        try:
            import matbench_genmetrics

            # Try to access dataset through pystow
            import pystow

            # The dataset might be cached by pystow
            df_path = pystow.join("matbench_genmetrics", "data", "mp_time_split.csv")
            if df_path.exists():
                df = pd.read_csv(df_path)
                print(f"Dataset loaded from cache! Shape: {df.shape}")
            else:
                raise FileNotFoundError("Dataset not found in cache")
        except Exception as e:
            print(f"All methods failed. Error: {e}")
            raise

# %%
# Display basic information about the dataset
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
df.head()

# %%
# Display more detailed information
print("\nDataset info:")
df.info()

# %%
# Display summary statistics
print("\nSummary statistics:")
df.describe()

# %%
# Display the full dataset (or a sample if it's very large)
if len(df) > 1000:
    print(f"\nDataset has {len(df)} rows. Showing first 1000 rows:")
    print(df.head(1000))
else:
    print(f"\nFull dataset ({len(df)} rows):")
    print(df)

# %%
