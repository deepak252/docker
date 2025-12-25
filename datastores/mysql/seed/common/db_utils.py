from itertools import islice

# def batch_iterator(iterable, batch_size):
#     """
#     Splits an iterable into batches
#     """
#     it = iter(iterable)
#     while True:
#         batch = list(islice(it, batch_size))
#         if not batch:
#             break
#         yield batch

def execute_batch(cursor, conn, sql, data):
    """
    Executes batch insert and commits
    """
    cursor.executemany(sql, data)
    conn.commit()


# def disable_db_checks(cursor):
#     """
#     Disable checks for fast bulk inserts
#     """
#     cursor.execute("SET autocommit=0")
#     cursor.execute("SET foreign_key_checks=0")
#     cursor.execute("SET unique_checks=0")


# def enable_db_checks(cursor, conn):
#     """
#     Re-enable checks after bulk insert
#     """
#     cursor.execute("SET foreign_key_checks=1")
#     cursor.execute("SET unique_checks=1")
#     conn.commit()
