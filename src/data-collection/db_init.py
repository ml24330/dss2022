import sqlite3

def Init(table):
    conn = sqlite3.connect("listings.db")

    c = conn.cursor()

    try:
        c.execute(f"""
            CREATE TABLE {table} (
            id integer,
            title text,
            globalId text,
            categoryId integer,
            categoryName text,
            url text,
            location text,
            shippingType text,
            shippingLocations text,
            shippingTime integer,
            startTime text,
            endTime text,
            returnsAccepted integer,
            conditionId integer,
            listingIsTopRated integer,
            sellerFeedbackScore integer,
            sellerPositivePercent real,
            sellerName text,
            sellerIsTopRated integer,
            price real,
            currency text,
            bids integer,
            UNIQUE(id)
        )""")

        print(f'created table named {table}')

        conn.commit()

    except Exception as e: 
        print(f'error, {e}')

    conn.close()