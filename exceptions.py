class BookNotFoundError(Exception):
    pass
class MemberNotFoundError(Exception):
    pass
class NoCopiesAvailableError(Exception):
    pass
class BookAlreadyBorrowedError(Exception):
    pass
class BookNotBorrowedError(Exception):
    pass