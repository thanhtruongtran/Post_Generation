from urllib.parse import urlparse


def extract_db_details(url):
    url = urlparse(url)
    db_name = url.path[1:]
    host = url.hostname
    password = url.password
    port = url.port
    user = url.username
    return db_name, host, password, port, user