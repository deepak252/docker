import random
from config.db import get_connection
from common.utils import random_country_id, random_mchannel_id, random_date_recent, random_category, random_sentence, random_date
from common.execution_timer import execution_timer
from common.db_utils import execute_batch

NUM_ROWS = 5000
BATCH_SIZE = 1000

INSERT_PRODUCT_SQL = """
INSERT IGNORE INTO products (
    company_id,
    media_channel_id,
    country_id,
    title,
    description,
    category,
    start_date,
    end_date,
    budget
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

def generate_product():
    start_date = random_date_recent(days=1800)
    end_date = random_date(start_date)
    budget = random.randint(1000, 100000)

    return (
        random.randint(1, 4500),   # company_id
        random_mchannel_id(),   # media_channel_id
        random_country_id(),   # country_id

        random_sentence(3),                  # title (campaign title)
        random_sentence(50),                  # description (campaign title)
        random_category(),                   # category

        start_date,                           # start_date
        end_date,                             # end_date
        budget                      # budget
    )


def seed_products():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        with execution_timer(f"seed_products done ✅ [Total {NUM_ROWS}]"):
            for offset in range(0, NUM_ROWS, BATCH_SIZE):
                batch_size = min(BATCH_SIZE, NUM_ROWS - offset)
                data = [ generate_product() for _ in range(batch_size) ]

                with execution_timer(f"seed_products | Batch {offset//BATCH_SIZE + 1} | Size {batch_size} | "):
                    execute_batch(
                        cursor, 
                        conn,
                        INSERT_PRODUCT_SQL,
                        data
                    )
            
        cursor.close()
        conn.close()
    except Exception as e:
        print("ERROR seed_products - ", e)

