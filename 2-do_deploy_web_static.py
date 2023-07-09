from fabric.api import env, run, put
from os.path import exists

# Define the remote hosts
env.hosts = ['<IP web-01>', '<IP web-02>']

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
