from config.db import get_connection
from common.utils import random_company_name, random_country_id, random_industry
from common.execution_timer import execution_timer
from common.db_utils import execute_batch

NUM_ROWS = 5000
BATCH_SIZE = 1000

def generate_company():
    return (
        random_company_name(),    # name
        random_industry(),        # industry
        random_country_id(),      # country_id
    )

def seed_companies():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        with execution_timer(f"seed_companies done ✅ [Total {NUM_ROWS}]"):
            for offset in range(0, NUM_ROWS, BATCH_SIZE):
                batch_size = min(BATCH_SIZE, NUM_ROWS - offset)
                data = [ generate_company() for _ in range(batch_size) ]

                with execution_timer(f"seed_companies | Batch {offset//BATCH_SIZE + 1} | Size {batch_size} | "):
                    execute_batch(
                        cursor, 
                        conn,
                        "INSERT IGNORE INTO companies (name, industry, country_id) VALUES (%s,%s,%s)",
                        data
                    )
            
        cursor.close()
        conn.close()
    except Exception as e:
        print("ERROR seed_companies - ", e)

