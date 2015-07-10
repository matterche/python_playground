def f(x):
    print "\nf(%d)" % x
    try:
        if x == 1:
            raise IOError()
        elif x == 2:
            badName()
    except (IOError, ValueError):
        print " An I/O error or a ValueError occured"
    except:  # catch all
        print " An unexpected error occurred"
        raise  # re-throw last exception

    else:
        print "else, called when no exception occurred"
    finally:
        print "finally, called also when exceptions occurred"


print("f0 - no exception")
f(0)
print("f1")
f(1)
print("f2")
f(2)
