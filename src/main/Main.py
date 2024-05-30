from fetch_data import FetchData
from database_manager import DatabaseManager


def main():
    db_name = 'crash_data.db'
    db_manager = DatabaseManager(db_name)
    db_manager.connect()
    resultState = db_manager.getCrashByState('Alaska')
    print(resultState)


if __name__ == "__main__":
    main()