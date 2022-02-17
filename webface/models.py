# from datetime import datetime
from pony.orm import PrimaryKey, Required, Optional, Database, Set


db = Database()
db.bind(provider="sqlite", filename="./database.sqlite", create_db=True)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    nick = Required(str, unique=True)
    passwd = Required(str)
    note = Optional(str)
    addressess = Set('Addresses')


class Addresses(db.Entity):
    id = PrimaryKey(int, auto=True)
    url = Required(str)
    shorcut = Required(str)
    user = Optional(User)

db.generate_mapping(create_tables=True)

"""
shorcut = "".join([random.choice(string.ascii_letters) for i in range(7)])
"""