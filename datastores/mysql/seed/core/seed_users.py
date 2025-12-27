from config.db import get_connection
from common.utils import random_name, name_to_email, random_gender, random_age
from common.execution_timer import execution_timer
from common.db_utils import execute_batch

NUM_ROWS = 50_000
BATCH_SIZE = 10_000

def generate_user():
    gender = random_gender()
    name = random_name(gender)
    email = name_to_email(name)
    return (
        name,
        email,
        'ANALYST',
    )

def seed_users():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        with execution_timer(f"seed_users done ✅ [Total {NUM_ROWS}]"):
            for offset in range(0, NUM_ROWS, BATCH_SIZE):
                batch_size = min(BATCH_SIZE, NUM_ROWS - offset)
                data = [ generate_user() for _ in range(batch_size) ]

                with execution_timer(f"seed_users | Batch {offset//BATCH_SIZE + 1} | Size {batch_size} | "):
                    execute_batch(
                        cursor, 
                        conn,
                        "INSERT IGNORE INTO users (name, email, role) VALUES (%s,%s,%s)",
                        data
                    )
            
        cursor.close()
        conn.close()
    except Exception as e:
        print("ERROR seed_users - ", e)

