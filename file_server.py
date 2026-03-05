import os
import time
import logging
import socket

# Configuration
FILE_SERVER_PATH = r"\\fileserver\shared"
CHECK_INTERVAL = 60   # seconds
LOG_FILE = "file_server_monitor.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_file_server():
    """
    Check if the network file server path is accessible
    """
    try:
        if os.path.exists(FILE_SERVER_PATH):
            logging.info(f"File server reachable: {FILE_SERVER_PATH}")
            return True
        else:
            logging.error(f"Network path not found: {FILE_SERVER_PATH}")
            return False

    except Exception as e:
        logging.error(f"Error checking file server: {str(e)}")
        return False


def monitor():
    logging.info("Starting File Server Monitoring")

    while True:
        status = check_file_server()

        if not status:
            print("ALERT: File server not reachable!")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    monitor()
