import sqlite3

conn = sqlite3.connect("listings.db")

c = conn.cursor()

c.execute("""
    CREATE TABLE listings (
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

conn.commit()

conn.close()