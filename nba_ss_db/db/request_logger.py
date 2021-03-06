from datetime import datetime
from .. import db


def log_request(api_request, table_name):
    """
    Logs the api_request with a time stamp to the table
    called "scrape_log".
    """
    curr_time = datetime.now().strftime('%Y-%m-%d %X %f')
    db.utils.execute_sql("""INSERT INTO scrape_log VALUES (?, ?, ?);""", params=(curr_time, api_request, table_name))

def already_scraped(api_request):
    """
    Returns True if the api_request has already been scraped.
    This is determined by whether or not the api_request str
    exists within the table "scrape_log.
    """
    api_request_log = db.utils.execute_sql("""SELECT * FROM scrape_log WHERE api_request = ? LIMIT 1;""", params=(api_request, ))
    return len(api_request_log.rows) != 0


def get_last_scraped(api_request):
    """
    Returns True if the api_request has already been scraped.
    This is determined by whether or not the api_request str
    exists within the table "scrape_log.
    """
    api_request_date_query = db.utils.execute_sql("""SELECT MAX(date) FROM scrape_log WHERE api_request = ?;""", params=(api_request, ))
    return api_request_date_query.rows[0][0]