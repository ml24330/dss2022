import sqlite3


def QueryAll():
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.execute("SELECT * FROM listings")
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


def InsertListings(listings):
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.executemany("INSERT OR IGNORE INTO listings VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", listings)

    conn.commit()
    conn.close()


def ClearAll():
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.execute("DELETE FROM listings")

    conn.commit()
    conn.close()


def DropTable():
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

    c.execute("DROP TABLE listings")

    conn.commit()
    conn.close()
