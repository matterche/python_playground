# files, sockets, db connections

# 'with' closes automatically resources via existing __exit__ functions
# 'with' calls also __exit__ when exceptions are thrown

# with open("cheat_sheet.py") as f:
#     print f.read()

class Resource:
    def __init__(self):
        pass

    @classmethod
    def open(cls):
        print "open called"
        cls()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "__exit__ called"


with Resource.open() as r:
    print "inside 'with' "
