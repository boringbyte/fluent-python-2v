from dataclasses import dataclass, field


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=True, repr=False)


@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


if __name__ == '__main__':
    print(HackerClubMember.__doc__)
