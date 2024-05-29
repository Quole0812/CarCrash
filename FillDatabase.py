from fetch_data import FetchData
from database_manager import DatabaseManager

def main():
    base_url = "https://crashviewer.nhtsa.dot.gov/CrashAPI/crashes/GetCaseList?states={state}&fromYear=2014&toYear=2024&minNumOfVehicles=1&maxNumOfVehicles=15&format=json"
    db_name = 'crash_data.db'
    db_manager = DatabaseManager(db_name)
    db_manager.connect()
    db_manager.create_table()
    db_manager.close()

    for state in range(1, 57):
        # Modify the URL for the current state
        url = base_url.format(state=state)
        #fetch data
        fetcher = FetchData(url)
        data = fetcher.get_data()
        if data:
            # Set up the database
            db_manager.connect()
            db_manager.insert_data(data)
            db_manager.close()

if __name__ == "__main__":
    main()