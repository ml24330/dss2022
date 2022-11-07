from db_utils import QueryAllFinished, UpdateItem
from ScrapeItem import ScrapeItem

tables = ["clock_uk", "clock_us", "book_uk", "book_us"]

for table in tables:

    listings = QueryAllFinished(table)
    error = 0

    print(f'found {len(listings)} listings that have completed for table {table}')

    for listing in listings[:100]:
        price, bids = ScrapeItem(listing[5])
        if price == -2 or bids == -2:
            error += 1
        print(f'updated item {listing[0]}: final price={price}, final bids={bids}')
        UpdateItem(table, listing[0], price, bids) 

    print(f'successfully updated {len(listings)-error}/{len(listings)} completed listings from table {table}')