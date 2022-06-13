from dataclasses import dataclass, field, InitVar

DatabaseType: str


@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database: DatabaseType):
        if self.j is None and database is not None:
            self.j = database.lookup('j')


if __name__ == '__main__':
    my_database = 'MYSQL'
    c = C(10, database=my_database)
