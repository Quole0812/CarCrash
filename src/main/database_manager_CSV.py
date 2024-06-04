import sqlite3


class DatabaseManagerCSV:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name):

        # Create table with ST_Case as the primary key
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                State TEXT,
                ST_Case INTEGER PRIMARY KEY,
                VE_Total INTEGER,
                Person INTEGER,
                County INTEGER,
                Day INTEGER,
                Month INTEGER,
                Year INTEGER,
                Latitude REAL,
                Longitude REAL
            )
        ''')

        self.conn.commit()

    def insert_data(self, table_name, data):
        # Insert data
        for item in data:
            self.cursor.execute(f'''
                INSERT OR REPLACE INTO {table_name} (State, ST_Case, VE_Total, Person, County, Day, Month, Year, Latitude, Longitude)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item['State'],
                item['ST_Case'],
                item['VE_Total'],
                item['Person'],
                item['County'],
                item['Day'],
                item['Month'],
                item['Year'],
                float(item['Latitude']),
                float(item['Longitude'])
            ))

        self.conn.commit()

    def create_table_newyear(self, table_name):
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                State TEXT,
                ST_Case INTEGER PRIMARY KEY,
                VE_Total INTEGER,
                County INTEGER,
                Day INTEGER,
                Month INTEGER,
                Year INTEGER,
                Latitude REAL,
                Longitude REAL
            )
        ''')

        self.conn.commit()

    def insert_data_newyear(self, table_name, data):

        for item in data:
            self.cursor.execute(f'''
                INSERT OR REPLACE INTO {table_name} (State, ST_Case, VE_Total, County, Day, Month, Year, Latitude, Longitude)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item['State'],
                item['ST_Case'],
                item['VE_Total'],
                item['County'],
                item['Day'],
                item['Month'],
                item['Year'],
                float(item['Latitude']),
                float(item['Longitude'])
            ))

        self.conn.commit()



    def close(self):
        if self.conn:
            self.conn.close()