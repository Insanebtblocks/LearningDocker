import psycopg


def get_connection():
    return psycopg.connect(
        host="database",
        port=5432,
        dbname="learningdb",
        user="mario",
        password="mypassword"
    )


def create_users_table():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    username VARCHAR(100) UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                );
            """)

def add_user(username, password_hash):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users (username, password_hash)
                VALUES (%s, %s)
                """,
                (username, password_hash)
            )
def get_user_by_username(username):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM users WHERE username = %s
                """,
                (username,)
            )
            return cursor.fetchone()