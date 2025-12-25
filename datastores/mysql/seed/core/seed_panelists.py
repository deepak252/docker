from config.db import get_connection
from common.utils import random_name, name_to_email, random_country_id, random_gender, random_age
from common.execution_timer import execution_timer
from common.db_utils import execute_batch

NUM_ROWS = 50_000
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

        with execution_timer(f"seed_panelists done ✅ [Total {NUM_ROWS}]"):
            for offset in range(0, NUM_ROWS, BATCH_SIZE):
                batch_size = min(BATCH_SIZE, NUM_ROWS - offset)
                data = [ generate_panelist() for _ in range(batch_size) ]

                with execution_timer(f"seed_panelists | Batch {offset//BATCH_SIZE + 1} | Size {batch_size} | "):
                    execute_batch(
                        cursor, 
                        conn,
                        "INSERT IGNORE INTO panelists (name, email, age, gender, country_id) VALUES (%s,%s,%s,%s,%s)",
                        data
                    )
            
        cursor.close()
        conn.close()
    except Exception as e:
        print("ERROR seed_panelists - ", e)

