from dataclasses import dataclass


@dataclass
class ClubMember:
    name: str
    guests: list  # = [] This is wrong in data class. Assigning multable objects to members


if __name__ == '__main__':
    ClubMember
