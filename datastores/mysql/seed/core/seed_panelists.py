from config.db import get_connection
from common.utils import random_name, name_to_email, random_country_id, random_gender, random_age

NUM_PANELISTS = 50_000
BATCH_SIZE = 10_000

def generate_panelist():
    gender = random_gender()
    name = random_name(gender)
    email = name_to_email(name)
    return (
        name,
        email,
        # random_email(),
        random_age(),
        gender,
        random_country_id(),
    )

def seed_panelists():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        data = [
            generate_panelist() for _ in range(NUM_PANELISTS)
        ]
        # print(data)
        for i in range(0, len(data), BATCH_SIZE):
            cursor.executemany(
                "INSERT IGNORE INTO panelists (name, email, age, gender, country_id) VALUES (%s,%s,%s,%s,%s)",
                data[i:i+BATCH_SIZE]
            )
            conn.commit()
        cursor.close()
        conn.close()
        print(f"seed_panelists done ✅: {len(data)} rows")
    except Exception as e:
        print("ERROR seed_panelists - ", e)

