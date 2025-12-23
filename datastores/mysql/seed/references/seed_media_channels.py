from config.db import get_connection

def seed_media_channels():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        data = [
            ("Direct Mail",None), 
            ("Email",None),
            ("Online Display",None),
            ("UX Media",None),
            ("SEM",None),
        ]
        cursor.executemany(
            "INSERT INTO media_channels (name,type) VALUES (%s,%s)", 
            data
        )
        conn.commit()
        cursor.close()
        conn.close()

        print(f"seed_media_channels done ✅: {len(data)} rows")

    except Exception as e:
        print("ERROR seed_media_channels - ", e)