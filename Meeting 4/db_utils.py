import sqlite3

def QueryAll(table):
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.execute(f'SELECT * FROM {table}')
    res = c.fetchall()

    conn.close()

    return res


def Query(exp):
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.execute(exp)
    res = c.fetchall()

    conn.close()

    return res


def InsertListings(table, listings):
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.executemany(f'INSERT OR IGNORE INTO {table} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', listings)

    conn.commit()
    conn.close()


def ClearAll(table):
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.execute(f'DELETE FROM {table}')

    conn.commit()
    conn.close()


def QueryAllFinished(table):
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.execute(f'SELECT * FROM {table} WHERE endTime < datetime("now") AND price = -1')

    res = c.fetchall()
    
    conn.close()
    
    return res


def UpdateItem(table, id, price, bids):
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()
    
    c.execute(f"""
        UPDATE {table}
        SET price=?,
            bids=?
        WHERE
            id=?
    """, (price, bids, id))

    conn.commit()
    conn.close()
