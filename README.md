# Shipments ETL Pipeline

A Python ETL pipeline that ingests, cleans, and transforms shipment records to produce business metrics. Built as a data engineering technical assessment simulation.

---

## Project Structure

```
test/
├── data/
│   ├── raw/               # Input CSV file
│   └── processed/         # Reserved for intermediate data
├── output/
│   ├── outliers.csv       # Shipments with weight > 100 kg
│   └── summary.json       # Business metrics report
├── src/
│   ├── __init__.py
│   ├── ingest.py          # Data loading, cleaning, and outlier filtering
│   ├── transform.py       # Metric calculations and JSON export
│   └── main.py            # Pipeline orchestration
└── requirements.txt
```

---

## Requirements

- Python 3.8+
- No external dependencies — standard library only

---

## How to Run

Place your input file at `data/raw/shipments.csv`, then run from the project root:

```bash
python -m src.main
```

> Note: the `-m` flag is required so Python resolves the `src` package correctly.

---

## Output

**`output/outliers.csv`**
Shipments with `weight_kg > 100`, removed before metric calculations to avoid skewing results.

**`output/summary.json`**
```json
{
  "shipments_by_status": {},
  "best_carrier": "",
  "top_routes": [],
  "avg_weight_by_carrier": {}
}
```

- `shipments_by_status` — total shipments grouped by status
- `best_carrier` — carrier with the highest delivery success rate (delivered / total)
- `top_routes` — top 3 most frequent origin → destination routes
- `avg_weight_by_carrier` — average shipment weight per carrier, rounded to 2 decimals

---

## Technical Decisions

**Standard library over pandas**
Using `csv`, `statistics`, and `json` directly forces a clear understanding of data structures and control flow. In production with larger datasets, `pandas` or `polars` would be the appropriate choice.

**One function, one responsibility**
Each function in `ingest.py` and `transform.py` does exactly one thing. This makes the pipeline easier to test, debug, and extend independently.

**Outlier removal before metrics**
Shipments with `weight_kg > 100` are filtered out before any calculations. Including them would distort averages and skew carrier performance metrics.

**Null handling via median**
Missing and invalid weight values (`""`, `"null"`) are replaced with the median of valid weights, calculated once before any replacements are made.