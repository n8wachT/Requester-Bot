import sqlite3
from .jsonr import p
dat = sqlite3.connect('data/dat1.db', timeout=0)
d = dat.cursor()


def visualizer(ch):
    d.execute("SELECT * FROM request WHERE userid=?", [ch.id])
    ex = d.fetchone()
    name = ex[0]
    lnk = ex[1]
    tosend = (p["visualizer"] % (name, lnk))
    return tosend


def staffvis(userid):
    d.execute("SELECT * FROM request WHERE userid=?", (int(userid), ))
    ex = d.fetchone()
    name = ex[0]
    lnk = ex[1]
    username = ex[3]
    nameuser = ex[4]
    ur = ex[6]
    if username is None:
        tosend = (p["staffvis"][0] % (ur, nameuser, userid, name, lnk))
    else:
        tosend = (p["staffvis"][1] % (ur, username, name, lnk))
    return tosend


def verdict(userid, what):
    d.execute("SELECT * FROM request WHERE userid=?", (userid, ))
    ex = d.fetchone()
    name = ex[0]
    lnk = ex[1]
    nameuser = ex[4]
    if what is True:
        tosend = (p["verdict"][0] % (nameuser, userid, name, lnk))
    elif what is False:
        tosend = (p["verdict"][1] % (nameuser, userid, name, lnk))
    else:
        tosend = (p["verdict"][2] % (nameuser, userid, name, lnk))
    return tosend