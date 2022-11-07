from QueryAPI import QueryAPI
from db_init import Init

# EBAY-GB, wall clocks. Stored in table `clock_uk`

Init("clock_uk")
QueryAPI("EBAY-GB", "wall clock", "clock_uk")


# EBAY-GB, Harry Potter books. Stored in table `book_uk`

Init("book_uk")
QueryAPI("EBAY-GB", "harry potter book", "book_uk")


# EBAY-US, Harry Potter books. Stored in table `book_us`

Init("book_us")
QueryAPI("EBAY-US", "harry potter book", "book_us")


# EBAY-US, wall clocks. Stored in table `clock_us`

Init("clock_us")
QueryAPI("EBAY-US", "wall clock", "clock_us")
