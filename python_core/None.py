list = [None]
if list[0] is None:
    print("is None")    # this will be for case None
elif list[0] is not None:
    print("is not None")
else:
    print("Something else")

if list[0]:
    print("list[0]")
elif not list[0]:       # this will be for case None
    print("not list[0]")
else:
    print("Something else")
''' ========================= '''
list = [False]
if list[0] is False:
    print("is False")    # this will be for case False
elif list[0] is not False:
    print("is not False")
else:
    print("Something else")

if list[0]:
    print("list[0]")
elif not list[0]:       # this will be for case False (different than for None)
    print("not list[0]")
else:
    print("Something else")
