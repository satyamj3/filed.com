import sqlite3
from sqlite3 import Error


def get_connection():
    """ create a database connection to a SQLite database """
    db_file = r"filed.db"
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
        return None


def create_db_tables():
    conn = get_connection()
    if conn is not None:
        cursor = conn.cursor()
        # creating Song table
        song_table_query = """ CREATE TABLE IF NOT EXISTS song (
            id integer PRIMARY KEY,
            name varchar(100) NOT NULL,
            upload_time datetime NOT NULL,
            duration int NOT NULL
        )
        """
        try:
            cursor.execute(song_table_query)
            conn.commit()
        except Exception as e:
            print('Failed to create Song table', e)

        # creating podcast table
        podcast_table_query = """ CREATE TABLE IF NOT EXISTS podcast (
            id integer PRIMARY KEY,
            title varchar(100) NOT NULL,
            upload_time datetime NOT NULL,
            duration int NOT NULL,
            host varchar(100) NOT NULL,
            participants varchar(1000)
        )
        """
        try:
            cursor.execute(podcast_table_query)
            conn.commit()
        except Exception as e:
            print('Failed to create Podcast table', e)
        # creating audiobook table
        audiobook_table_query = """ CREATE TABLE IF NOT EXISTS audiobook (
            id integer PRIMARY KEY,
            title varchar(100) NOT NULL,
            upload_time datetime NOT NULL,
            duration int NOT NULL,
            author varchar(100) NOT NULL,
            narrator varchar(100) NOT NULL
        )
        """
        try:
            cursor.execute(audiobook_table_query)
            conn.commit()
        except Exception as e:
            print('Failed to create audiobook', e)
        conn.close()


create_db_tables()
