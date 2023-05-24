#!/usr/bin/python3
""" ziping a directory using fabric """

from fabric import connection


def do_pack():
    """ function to zip a directory """
    Connection = connection(host='localhost')
    Connection.local("tar -zctf web_static_20230523085000.tgz web_static/")
