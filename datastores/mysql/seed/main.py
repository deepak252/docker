from references.seed_countries import seed_countries
from references.seed_media_channels import seed_media_channels

from core.seed_panelists import seed_panelists

# def batch_insert(sql, data):
#     cursor.executemany(sql, data)
#     conn.commit()

# def disable_checks():
#     cursor.execute("SET autocommit=0")
#     cursor.execute("SET foreign_key_checks=0")
#     cursor.execute("SET unique_checks=0")

# def enable_checks():
#     cursor.execute("SET foreign_key_checks=1")
#     cursor.execute("SET unique_checks=1")
#     conn.commit()

if __name__ == "__main__":
    # disable_checks()
    # seed_countries()
    # seed_media_channels()

    seed_panelists()


    # seed_companies()
    # seed_products()
    # seed_panelists()
    # seed_campaigns()
    # seed_product_media()

    # seed_responses()
    # seed_metrics()

    # enable_checks()

    # cursor.close()
    # conn.close()
    print("✅ Seeding completed")