
# app.py
from db import (
    init_db,
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)

def print_users(title: str):
    print(f"\n📋 {title}")
    users = get_all_users()
    if not users:
        print("(no users)")
    for u in users:
        print(u)

def main():
    # 1) Initialize DB/table
    init_db()

    # 2) Create
    alice_id = create_user("Alice", 30)
    bob_id = create_user("Bob", 25)
    carol_id = create_user("Carol", 40)

    print_users("After create")

    # 3) Read (one)
    print("\n🔎 Get Alice by id:")
    print(get_user_by_id(alice_id))

    # 4) Update
    updated = update_user(bob_id, age=26)
    print(f"\n✏️ Update Bob age -> success? {updated}")
    updated = update_user(carol_id, name="Caroline", age=41)
    print(f"✏️ Update Carol -> success? {updated}")

    print_users("After updates")

    # 5) Delete
    deleted = delete_user(bob_id)
    print(f"\n🗑️ Delete Bob -> success? {deleted}")

    print_users("Final users")

if __name__ == "__main__":
    main()
