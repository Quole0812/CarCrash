import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS crashes (
            st_case INTEGER PRIMARY KEY AUTOINCREMENT,
            state INTEGER,
            state_name TEXT,
            county_name TEXT,
            crash_date TEXT,
            total_vehicles INTEGER,
            fatals INTEGER,
            peds INTEGER,
            persons INTEGER
        )
        ''')
        self.conn.commit()

    def insert_data(self, data):
        for case in data['Results'][0]:
            try:
                self.cursor.execute('''
                INSERT INTO crashes (state, state_name, county_name, crash_date, total_vehicles, fatals, peds, persons)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    int(case['State']),
                    case['StateName'],
                    case['CountyName'],
                    case['CrashDate'],
                    int(case['TotalVehicles']),
                    int(case['Fatals']),
                    int(case['Peds']),
                    int(case['Persons'])
                ))
            except sqlite3.IntegrityError as db_err:
                print(f"Database error occurred: {db_err}")
                continue
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()