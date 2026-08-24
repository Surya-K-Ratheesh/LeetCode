from enum import Enum
import random

def main():
    class Size(Enum):
        small = 0
        medium = 1
        large = 2

    class package:
        def __init__(self, pid, size):
            self.id = id
            self.size = size

    class Locker:
        def __init__(self, lid, size):
            self.id = lid
            self.size = size
            self.package = None
            self.pin = None

        def is_available(self):
            return self.package is None

    class LockerSystem:
        def __init__(self):
            self.lockers = {Size.small : [], Size.medium : [], Size.large : []}

        def add_locker(self, locker):
            self.lockers[locker.size].append(locker)

        def find_locker(self, package):
            for size in Size:

                if size.value < package.size.value:
                    continue

                for locker in self.lockers[size]:
                    if locker.is_available():
                        return locker

            return None

        def drop_off(self, package):
            locker = self.find_locker(package)

            if locker is None:
                return None

            locker.package = package
            locker.pin = str(random.randit(1000, 9999))

            return locker.pin

        def pick_up(self, pin):
            for size in Size:
                for locker in self.lockers[size]:

                    if locker.pin == pin:
                        pkg = locker.package
                        locker.package = None
                        locker.pin = None
                        
                        return pkg

            return None

if __name__ == '__main__':
    main()