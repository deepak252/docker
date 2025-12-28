from config.db import get_connection

def seed_countries():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = [
            ("India","IN"), ("USA","US"), ("UK","GB"),
            ("Germany","DE"), ("Canada","CA")
        ]
        cursor.executemany(
            "INSERT IGNORE INTO countries (name, iso_code) VALUES (%s,%s)",
            data
        )
        conn.commit()
        cursor.close()
        conn.close()

        print(f"seed_countries done ✅: {len(data)} rows")

    except Exception as e:
        print("ERROR seed_countries - ", e)

# def seed_countries():
#     conn = get_connection()
#     cursor = conn.cursor()

#     users_data = []

#     for _ in range(TOTAL_USERS):
#         users_data.append((
#             random_string(12),   # name
#             random_email()       # email
#         ))

#     batch_insert(cursor, INSERT_USER_SQL, users_data, batch_size=2000)
#     conn.commit()

#     cursor.close()
#     conn.close()

#     print(f"✅ Seeded {TOTAL_USERS} users")


# if __name__ == "__main__":
#     seed_users()

