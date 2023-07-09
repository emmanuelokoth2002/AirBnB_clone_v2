#!/usr/bin/python3
"""
creates and distributes an archive to your web servers, using the function
deploy
"""
from fabric.api import env, run, put
from os.path import exists
from datetime import datetime
from fabric.contrib import files

# Define the remote hosts
env.hosts = ['52.91.152.63', '54.144.45.151']


def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""
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


def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if not exists(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/")

    # Extract the archive to the /data/web_static/releases/ directory
    archive_filename = archive_path.split('/')[-1]
    archive_folder = archive_filename.split('.')[0]
    release_path = "/data/web_static/releases/" + archive_folder
    run("mkdir -p {}".format(release_path))
    run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))
    run("rm /tmp/{}".format(archive_filename))

    # Move the contents of the extracted folder to the release folder
    run("mv {}/web_static/* {}/".format(release_path, release_path))
    run("rm -rf {}/web_static".format(release_path))

    # Delete the existing symbolic link and create a new one
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(release_path))

    return True


def deploy():
    """Create and distribute an archive to the web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
