"""Database module for managing users in an SQLite database."""
import sqlite3
from typing import List, Optional, Tuple

DB_PATH = "mydatabase.db"
conn = sqlite3.connect(DB_PATH)
cursor=conn.cursor()
    


def init_db() -> None:
    """Create the 'users' table if it doesn't exist."""
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT    NOT NULL,
            age  INTEGER NOT NULL CHECK(age >= 0)
        )
        """
    )
    conn.commit()



def create_user(name: str, age: int) -> int:
    """Insert a new user and return the new row id."""
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    return cursor.lastrowid


def get_user_by_id(user_id: int) -> Optional[Tuple[int, str, int]]:
    """Return one user (id, name, age) or None."""
    cursor.execute("SELECT id, name, age FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


def get_all_users() -> List[Tuple[int, str, int]]:
    """Return all users as a list of tuples (id, name, age)."""
    cursor.execute("SELECT id, name, age FROM users ORDER BY id")
    return cursor.fetchall()


def update_user(user_id: int, name: Optional[str] = None, age: Optional[int] = None) -> bool:
    """
    Update user fields selectively. Returns True if a row was updated.
    Example:
        update_user(3, name="Bob")
        update_user(5, age=41)
        update_user(7, name="Eve", age=22)
    """
    if name is None and age is None:
        raise ValueError("At least one of 'name' or 'age' must be provided.")

    fields = []
    params = []

    if name is not None:
        fields.append("name = ?")
        params.append(name)
    if age is not None:
        fields.append("age = ?")
        params.append(age)

    params.append(user_id)  # for WHERE clause

    sql = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"

    cursor.execute(sql, tuple(params))
    conn.commit()
    return cursor.rowcount > 0


def delete_user(user_id: int) -> bool:
    """Delete a user by id. Returns True if a row was deleted."""
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    return cursor.rowcount > 0
