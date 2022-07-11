# with open('notex.txt', 'w') as file:
#    file.write('Some todo....')
# to write support of with statement (see ^^^) in our own object
class ManagedFile():
    def __init__(self, filename):
        print("init")
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, ext_traceback):
        if self.file:
            self.file.close()
        print('exc:', exc_type, exc_value)
        if exc_type == AttributeError:
            print('exception has been handled')
        print('exit')
        return True


with ManagedFile("notes.txt") as file:
    print('Do some stuff...')
    file.write("Some todoo....")
    file.somemethod()
print('continue, e.g. no exceptions')

# =============================================
# To do it with function

from contextlib import contextmanager


@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()


with open_managed_file('notes1.txt') as f:
    f.write('written in the function')
