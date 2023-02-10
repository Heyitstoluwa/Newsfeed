import sqlite3
from sqlite3 import Error

# creating a new database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_news(conn, news):
    """
    Create a new news
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO news(id, title, date_published, img_url, content, categories, source)
            VALUES(?,?,?,?,?,?) '''
    curr = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid

def main():
    # r is used to specify that it is a string
    database = r"C:\Users\User\Desktop\news feed projects\database\newsDatabase.db"

    # to create a new connection
    conn = create_connection(database)

if __name__ == '__main__':
    main()
    
