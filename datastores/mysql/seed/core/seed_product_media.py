import random
from config.db import get_connection
from common.utils import random_media_type, random_media_url
from common.execution_timer import execution_timer
from common.db_utils import execute_batch

# NUM_ROWS = 500
BATCH_SIZE = 100

def generate_product_media(
    product_id = random.randint(1, 4000)
):
    media_type = random_media_type()
    return (
        product_id,  # product_id (FK-safe range)
        media_type,
        random_media_url(media_type)
    )


# def fetch_product_ids(cursor):
#     cursor.execute("SELECT id FROM products")
#     return [row[0] for row in cursor.fetchall()]

def seed_product_media(start_product_id=1, end_product_id=5000):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # generate a list of all product IDs
        product_ids = list(range(start_product_id, end_product_id + 1))

        # optionally, multiply media per product
        all_rows = []
        for pid in product_ids:
            num_media = random.randint(1, 1)  # 1-1 media per product
            for _ in range(num_media):
                all_rows.append(generate_product_media(pid))

        total_rows = len(all_rows)
        with execution_timer(f"seed_product_media done ✅ [Total {total_rows}]"):
            # batch insert
            for offset in range(0, total_rows, BATCH_SIZE):
                batch = all_rows[offset : offset + BATCH_SIZE]
                with execution_timer(f"Batch {offset//BATCH_SIZE + 1} | Size {len(batch)}"):
                    execute_batch(
                        cursor,
                        conn,
                        "INSERT IGNORE INTO product_media (product_id, media_type, media_url) VALUES (%s,%s,%s)",
                        batch
                    )

        cursor.close()
        conn.close()
    except Exception as e:
        print("ERROR seed_product_media - ", e)

