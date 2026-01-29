# Extract Table 19(b) from page 45
import camelot
import pandas as pd

pdf_path = "/workspaces/LEI-data-extractor/LEI reports/LEI NOV 2025.pdf"

tables = camelot.read_pdf(
    pdf_path,
    pages="45",
    flavor="lattice"  # use borders
)

print(f"Tables found: {len(tables)}")

# Inspect extracted tables
for i, table in enumerate(tables):
    print(f"\n--- Table {i} ---")
    print(table.df.head())

df = tables[0].df

df.to_csv(
    "table_19b_jkia_landed_passengers_raw.csv",
    index=False
)
