from references.seed_countries import seed_countries
from references.seed_media_channels import seed_media_channels

from core.seed_panelists import seed_panelists
from core.seed_companies import seed_companies

if __name__ == "__main__":
    # disable_checks()
    # seed_countries()
    # seed_media_channels()

    # seed_panelists()
    seed_companies()


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