from fetch_data import FetchData
from database_manager import DatabaseManager
from CSVreader import read_csv
from database_manager_CSV import DatabaseManagerCSV
import os


def main():
    # base_url = "https://crashviewer.nhtsa.dot.gov/CrashAPI/crashes/GetCaseList?states={state}&fromYear=2014&toYear=2024&minNumOfVehicles=1&maxNumOfVehicles=15&format=json"
    # db_name = 'crash_data.db'
    # db_manager = DatabaseManager(db_name)
    # db_manager.connect()
    # db_manager.create_table()
    # db_manager.close()
    #
    # for state in range(1, 57):
    #     # Modify the URL for the current state
    #     url = base_url.format(state=state)
    #     # fetch data
    #     fetcher = FetchData(url)
    #     data = fetcher.get_data()
    #     if data:
    #         # Set up the database
    #         db_manager.connect()
    #         db_manager.insert_data(data)
    #         db_manager.close()

    print("Database 1 populated successfully.")

    csv_file_path = 'resources/accident{year}.CSV'  # Replace with your CSV file path
    database_name = 'crash_data.db'
    table_name = 'crash_dataCSV1015'
    table_name2 = 'crash_dataCSV1523'

    db_manager = DatabaseManagerCSV(database_name)
    db_manager.connect()
    # db_manager.create_table(table_name)
    db_manager.create_table_newyear(table_name2)
    db_manager.close()

    # for year in range(2010, 2015):
    #     # Check both lowercase and uppercase extensions
    #     file_path_lower = csv_file_path.format(year=year)
    #     file_path_upper = file_path_lower.replace('.csv', '.CSV')
    #
    #     # Determine which file exists
    #     if os.path.exists(file_path_lower):
    #         file_path = file_path_lower
    #     elif os.path.exists(file_path_upper):
    #         file_path = file_path_upper
    #     else:
    #         print(f"File not found: {file_path_lower} or {file_path_upper}")
    #         continue
    #
    #     print(f"Reading file: {file_path}")
    #     data = read_csv(file_path)
    #     if data:
    #         db_manager.connect()
    #         db_manager.insert_data(table_name, data)
    #         db_manager.close()
    # print("Database 2 populated successfully.")

    for year in range(2015, 2023):
        # Check both lowercase and uppercase extensions
        file_path_lower = csv_file_path.format(year=year)
        file_path_upper = file_path_lower.replace('.csv', '.CSV')

        # Determine which file exists
        if os.path.exists(file_path_lower):
            file_path = file_path_lower
        elif os.path.exists(file_path_upper):
            file_path = file_path_upper
        else:
            print(f"File not found: {file_path_lower} or {file_path_upper}")
            continue

        print(f"Reading file: {file_path}")
        data = read_csv(file_path)
        if data:
            db_manager.connect()
            db_manager.insert_data_newyear(table_name2, data)
            db_manager.close()

    print("Database 3 populated successfully.")


if __name__ == "__main__":
    main()
