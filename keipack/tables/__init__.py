# Imports go here!
from .keipeople import KeiPerson
from .keimessages import KeiMessage
from .keiunlocks import KeiUnlocks

# Enter the tables of your Pack here!
available_tables = [
    KeiPerson,
    KeiMessage,
    KeiUnlocks,
]

# Don't change this, it should automatically generate __all__
__all__ = [table.__name__ for table in available_tables]
