#!/usr/bin/python3
"""creates and distributes an archive to web servers.
using the function deploy
"""

from datetime import datetime
from fabric.api import *
import os.path


env.hosts = ['101.188.67.134', '101.188.67.134']


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
