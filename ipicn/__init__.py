import socket

import geoip2.database
from geoip2.errors import AddressNotFoundError
import ipaddress
from ipicn.updater import Updater
from ipicn import constants as c

Updater.download_mmdb(force_update=False)
geo_reader = geoip2.database.Reader(c.MMDB_FILE_NAME)


def is_in_china(ip_or_domain: str, update_database=False) -> bool:
    global geo_reader

    if update_database:
        Updater.download_mmdb(force_update=True)
        geo_reader.close()
        geo_reader = geoip2.database.Reader(c.MMDB_FILE_NAME)

    ip = socket.gethostbyname(ip_or_domain)
    if ipaddress.ip_address(ip).is_private:
        return True
    try:
        geo_reader.country(ip)
        return True
    except AddressNotFoundError:
        return False
