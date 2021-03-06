class Bird:
    pass


class Duck(Bird):
    def quack(self):
        print('Quack!')


def alert(birdie):
    birdie.quack()


def alert_duck(birdie: Duck):
    birdie.quack()


def alert_bird(birdie: Bird):
    birdie.quack()


if __name__ == '__main__':
    daffy = Duck()
    alert(daffy)
    alert_duck(daffy)
    alert_bird(daffy)
