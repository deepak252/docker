from references.seed_countries import seed_countries
from references.seed_media_channels import seed_media_channels

from core.seed_panelists import seed_panelists
from core.seed_companies import seed_companies
from core.seed_users import seed_users
from core.seed_products import seed_products
from core.seed_product_media import seed_product_media

if __name__ == "__main__":
    # disable_checks()
    # seed_countries()
    # seed_media_channels()

    # seed_companies()
    # seed_panelists()
    # seed_users()
    # seed_products()
    seed_product_media()


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