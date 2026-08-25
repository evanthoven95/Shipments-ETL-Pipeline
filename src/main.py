from src import ingest
from src import transform

INPUT_FILE='data/raw/shipments.csv'
OUTPUT_OUTLIERS='output/outliers.csv'
OUTPUT_JSON='output/summary.json'

def main():
    cleaned_shipments=ingest.clean_data(INPUT_FILE)
    filtered_shipments,outliers=ingest.filter_outliers(cleaned_shipments)
    ingest.write_csv(outliers,OUTPUT_OUTLIERS)
    summary=transform.build_summary(filtered_shipments)
    transform.write_json(summary, OUTPUT_JSON)
    
if __name__=='__main__':
    main()