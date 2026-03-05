import os
import time
import logging
import config

logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_file_server():
    try:
        if os.path.exists(config.FILE_SERVER_PATH):
            logging.info(f"File server reachable: {config.FILE_SERVER_PATH}")
            return True
        else:
            logging.error(f"Network path not found: {config.FILE_SERVER_PATH}")
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

        time.sleep(config.CHECK_INTERVAL)


if __name__ == "__main__":
    monitor()
