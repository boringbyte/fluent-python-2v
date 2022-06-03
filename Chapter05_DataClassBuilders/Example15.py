from dataclasses import dataclass, field


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)


if __name__ == '__main__':
    ClubMember
