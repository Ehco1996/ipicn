import os
import datetime

import requests

from ipicn import constants as c


class Updater:
    @classmethod
    def download_mmdb(cls, force_update: bool = False) -> None:
        print("check mmdb file ...")
        exists = os.path.exists(c.MMDB_FILE_NAME)
        if exists:
            dt = datetime.datetime.fromtimestamp(os.path.getctime(c.MMDB_FILE_NAME))
            print(f"mmdb already exists, created_date: {dt}")
        if not exists or force_update:
            open(c.MMDB_FILE_NAME, "wb").write(
                requests.get(
                    c.MMDB_UPDATE_URL, allow_redirects=True, timeout=200
                ).content
            )
            print(f"download mmdb from {c.MMDB_FILE_NAME}")
