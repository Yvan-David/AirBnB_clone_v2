#!/usr/bin/python3
""" ziping a directory using fabric """

from fabric.api import local


def do_pack():
    """ function to zip a directory """

    local("tar -zctf web_static_20230523085000.tgz web_static/")
