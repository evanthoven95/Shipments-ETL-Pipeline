import csv
import statistics

def clean_data(filepath):
    cleaned_shipments=[]
    cleaned_weight=[]
    
    with open(filepath,'r',encoding='utf-8') as data_handler:
        reader = csv.DictReader(data_handler)
        for row in reader:
            origin_title=row['origin'].title()
            row['origin']=origin_title
            cleaned_shipments.append(row)
            if row['weight_kg'] not in ('null',''): 
                cleaned_weight.append(row['weight_kg'])
        cleaned_weight=[float(weight) for weight in cleaned_weight]
        median=statistics.median(cleaned_weight)
    for row in cleaned_shipments:
        if row['weight_kg'] in ('null',''): 
            row['weight_kg']=str(median)
    return cleaned_shipments

def filter_outliers(cleaned_shipments): #CHANGE PARAMETER, NEED TO BE MORE GENERAL
    outliers=[]
    filtered_shipments=[]
    for row in cleaned_shipments:
        if float(row['weight_kg']) > 100:
            outliers.append(row)
        else:
            filtered_shipments.append(row)
    return filtered_shipments,outliers

def write_csv(outliers, output_path):
    with open (output_path, 'w',encoding='utf-8', newline='') as outliers_handler:
        fieldnames=outliers[0].keys()
        writer=csv.DictWriter(outliers_handler,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(outliers)
    