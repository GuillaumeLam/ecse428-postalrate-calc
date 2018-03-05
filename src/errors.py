class Errors:
    @staticmethod
    def no_args(args):
        if args <= 1:
            raise Exception

    @staticmethod
    def missing_args(args):
        if args < 15:
            raise Exception

    @staticmethod
    def too_many_args(args):
        if args > 15:
            raise Exception