import sys


class Main(object):
    """Main class to encapsulate logic
    """
    def __init__(self, argv=None):
        """Initializer

        Keyword Arguments:
        argv - list of arguments
        """
        self.argv = argv

    def parse_args(self):
        """Return length of argv array, returns 0 if argv is None
        """
        if self.argv is None:
            return 0
        else:
            return len(self.argv)

test=Main('ads')
print test.parse_args()
