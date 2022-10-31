from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from db_utils import InsertListings, QueryAll
import os
from dotenv import load_dotenv

load_dotenv()

try:
    api = Connection(appid=os.environ.get("APP_ID"), config_file=None)

    listings = []

    res = api.execute("findItemsAdvanced", {
        "keywords": "camera", 
        "itemFilter": [
        {
            "name": "ListingType",
            "value": "Auction"
        }
        ],
        "outputSelector": ["SellerInfo"],
        "paginationInput": { "entriesPerPage": "100" }
    })

    page_count = res.reply.paginationOutput.totalPages

    for num in range(1,min(101, int(page_count)+1)):

        print(f'starting query number {num}...')

        response = api.execute("findItemsAdvanced", {
            "keywords": "camera", 
            "itemFilter": [
            {
                "name": "ListingType",
                "value": "Auction"
            }
            ],
            "outputSelector": ["SellerInfo"],
            "paginationInput": { "entriesPerPage": "100", "pageNumber": num }
        })

        for idx, item in enumerate(response.reply.searchResult.item):

            id = item.itemId
            title = item.title
            globalId = item.globalId
            categoryId = item.primaryCategory.categoryId
            categoryName = item.primaryCategory.categoryName
            url = item.viewItemURL
            location = item.location
            shippingType = item.shippingInfo.shippingType
            shippingLocations = item.shippingInfo.shipToLocations
            shippingTime = item.shippingInfo.handlingTime if hasattr(item.shippingInfo, "handlingTime") else -1
            startTime = item.listingInfo.startTime
            endTime = item.listingInfo.endTime
            returnsAccepted = 1 if item.returnsAccepted == 'true' else 0
            conditionId = item.condition.conditionId if hasattr(item, "condition") else -1
            listingIsTopRated = 1 if item.topRatedListing == 'true' else 0
            sellerFeedbackScore = item.sellerInfo.feedbackScore
            sellerPositivePercent = item.sellerInfo.positiveFeedbackPercent
            sellerName = item.sellerInfo.sellerUserName
            sellerIsTopRated = 1 if item.sellerInfo.topRatedSeller == 'true' else 0
            price = item.sellingStatus.convertedCurrentPrice.value if hasattr(item.sellingStatus, "convertedCurrentPrice") else -1
            # price = -1
            currency = -1
            bids = -1

            listing = (
                id, title, globalId, categoryId, categoryName, url, location, shippingType, shippingLocations,
                shippingTime, startTime, endTime, returnsAccepted, conditionId, listingIsTopRated, 
                sellerFeedbackScore, sellerPositivePercent, sellerName, sellerIsTopRated, price, currency, bids
            )

            listings.append(listing)

        InsertListings(listings)
        print(f'database now has {len(QueryAll())} entries')

    


except ConnectionError as e:
    print(e)
    print(e.response.dict())