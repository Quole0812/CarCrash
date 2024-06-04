import csv

def read_csv(file_path):
    extracted_data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            extracted_data.append({
                'State': row['STATE'],
                'ST_Case': row['ST_CASE'],
                'VE_Total': row['VE_TOTAL'],
                'Person': row['PERSONS'],
                'County': row['COUNTY'],
                'Day': row['DAY'],
                'Month': row['MONTH'],
                'Year': row['YEAR'],
                'Latitude': row['LATITUDE'],
                'Longitude': row['LONGITUD']
            })
    return extracted_data

def read_csv_newyear(file_path):
    extracted_data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            extracted_data.append({
                'State': row['STATE'],
                'ST_Case': row['ST_CASE'],
                'VE_Total': row['VE_TOTAL'],
                'County': row['COUNTY'],
                'Day': row['DAY'],
                'Month': row['MONTH'],
                'Year': row['YEAR'],
                'Latitude': row['LATITUDE'],
                'Longitude': row['LONGITUD']
            })
    return extracted_data