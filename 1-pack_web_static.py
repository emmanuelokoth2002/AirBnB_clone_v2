#!/usr/bin/python3
"""
This module contains a Fabric function to create a .tgz
archive from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The path of the created archive file, or
        None if the archive creation failed.
    """
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_" + timestamp + ".tgz"
    archive_path = "versions/" + archive_name

    local("mkdir -p versions")

    command = "tar -czvf {} web_static".format(archive_path)
    result = local(command)

    if result.failed:
        return None
    else:
        return archive_path
