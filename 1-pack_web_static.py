#!/usr/bin/python3
"""
A Fabric script that generates a '.tgz' archive from the contents of the
+'web_static' folder of the AirBnB Clone repo, using the function 'do pack'.
"""

from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """Function that generates a .tgz archive"""
    try:
        c_date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        arch_file = "versions/web_static_{}.tgz".format(c_date)
        local("tar -cvzf {} web_static".format(arch_file))
        return arch_file
    except Exception:
        return None
