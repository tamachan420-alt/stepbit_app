import sqlite3, os

BASE = os.path.dirname(os.path.dirname(__file__))
SQL_DIR = os.path.join(BASE, 'sql')
DB_DIR = os.path.join(BASE, 'db')
DB_PATH = os.path.join(DB_DIR, 'stepbit_db.sqlite')

def run_sql(path, conn):
    with open(path, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())

def main():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        run_sql(os.path.join(SQL_DIR, 'reset_and_create.sql'), conn)
        run_sql(os.path.join(SQL_DIR, 'sample_data.sql'), conn)
        conn.commit()
        print('DB initialized at:', DB_PATH)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
