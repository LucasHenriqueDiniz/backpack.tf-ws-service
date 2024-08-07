import logging
from logger import configure_logging
from src.bptf_websocket import BptfWebSocket
from json import load
from asyncio import run


async def main():
    logger = logging.getLogger(__name__)

    with open("config.json", "r") as f:
        config = load(f)

    WEBSOCKET_URL = config["websocket_url"]  # Websocket URL
    MONGO_URI = config["mongo_uri"]  # MongoDB URI
    DATABASE_NAME = config["database_name"]  # Database name
    COLLECTION_NAME = config["collection_name"]  # Collection name
    PRINT_EVENTS = config[
        "print_events"
    ]  # This is the value that will be passed to configure_logging 0 = CRITICAL, 1 = error, 2 = warning, 3 = info, 4 = debug
    BPTF_TOKEN = config["bptf_token"]  # Your BPTF token
    PRIO_ITEMS = config["prioritized_items"]  # List of prioritized items

    # Configure logging with the value of PRINT_EVENTS from config.json if not 0
    configure_logging(PRINT_EVENTS)

    bptf = BptfWebSocket(
        MONGO_URI,
        DATABASE_NAME,
        COLLECTION_NAME,
        WEBSOCKET_URL,
        BPTF_TOKEN,
        PRIO_ITEMS,
    )

    try:
        logger.info("Starting websocket...")
        await bptf.start_websocket(WEBSOCKET_URL)

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)

    finally:
        logger.info("Closing connection...")
        await bptf.close_connection()


if __name__ == "__main__":
    run(main())
