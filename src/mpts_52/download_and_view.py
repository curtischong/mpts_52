# %%
from matbench_genmetrics.mp_time_split.splitter import MPTimeSplit

# %%
# Load the mp_time_split dataset
# The dataset is provided by matbench-genmetrics library
# It downloads a pre-processed snapshot from figshare
print("Loading mp_time_split dataset...")
mpts = MPTimeSplit()
df = mpts.load(dummy=False, force_download=False)
if df is None:
    raise RuntimeError("Failed to load dataset")
print(f"Dataset loaded successfully! Shape: {df.shape}")

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
# Save the largest structures as .cif files
from pathlib import Path

output_dir = Path("structures")
output_dir.mkdir(exist_ok=True)

print("Calculating structure sizes...")
structure_sizes = []
for idx in range(len(df)):
    structure = df.iloc[idx].structure
    num_atoms = len(structure)
    material_id = df.iloc[idx].material_id
    structure_sizes.append((idx, num_atoms, material_id))

structure_sizes.sort(key=lambda x: x[1], reverse=True)

num_to_save = min(10, len(df))
largest_indices = structure_sizes[:num_to_save]

print(f"\nSaving {num_to_save} largest structures:")
for i, (idx, num_atoms, material_id) in enumerate(largest_indices):
    structure = df.iloc[idx].structure
    filename = output_dir / f"{material_id}.cif"
    structure.to(filename=str(filename), fmt="cif")
    print(
        f"Saved structure {i + 1}/{num_to_save}: {material_id} ({num_atoms} atoms) -> {filename}"
    )

print(f"\nAll structures saved to {output_dir}/")

# %%
