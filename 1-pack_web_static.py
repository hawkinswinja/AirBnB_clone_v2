#!/usr/bin/python3
"""compress files in the web_static folder and stor in versions"""
from fabric.api import local
import time


def do_pack():
    """compress files in web_static
       create directory versions to store compressed file"""
    dest = 'versions/web_static_{}.tgz'.format(time.strftime("%Y%m%d%H%M%S"))
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(dest))
        return dest
    except Exception:
        return None
