#!/usr/bin/python3
"""
A Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean
"""
import os
from fabric.api import *

env.hosts = ['18.209.180.79', '100.25.152.221']


def do_clean(number=0):
    """
    Function that Delete the out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    Returns:
        int: The number of archives cleaned remotely.
    """
    number = 1 if int(number) == 0 else int(number)

    # Clean local archives
    try:
        archives = sorted(os.listdir("versions"))
        [archives.pop() for i in range(min(number, len(archives)))]
        with lcd("versions"):
            [local("rm ./{}".format(a)) for a in archives]
    except Exception:
        pass

    # Clean remote archives
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        archives.sort(reverse=True)  # Newest first
        to_keep = archives[:number]
        to_delete = archives[number:]
        if to_delete:
            run("rm -rf {}".format(" ".join(to_delete)))

        return len(to_delete)


if __name__ == "__main__":
    result = do_clean()
    print(result)
