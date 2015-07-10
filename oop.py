# my postgres dummy
postgres = []


class Database:
    # convention: init all used members in constructor
    def __init__(self, user, password):
        self.db = None
        self.user = user
        self.password = password

    def open_connection(self, user, password):
        self.db = postgres.openConnection(user, password)

    def insert(self, sql):
        self.db.execute(sql)

    def close(self):
        self.db.close()

    @staticmethod
    def f():
        pass

        # pure functions: no state, no side-effects, idempotent

    # classmethod: factory method which can be overridden
    @classmethod
    def create(cls, user, password):
        print "classmethod in Database"
        return cls(user, password)


class Database2(Database):
    @classmethod
    def create(cls, user, password):
        print "classmethod in Database2"
        if not Database2.is_blacklisted(user):
            return cls(user, password)
        else:
            None

    @staticmethod
    def is_blacklisted(user):
        pass


db = Database("bla", "fasel")
Database.f()
db2 = Database.create("bla", "fasel")
db2 = Database2.create("bla", "fasel")
