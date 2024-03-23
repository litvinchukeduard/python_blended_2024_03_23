from AddressBook import AddressBook
from abc import ABC, abstractmethod
from LoggerSingleton import LoggerSingleton

# import logging

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='myapp.log', level=logging.DEBUG)

logger = LoggerSingleton()

class Bot(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def bye(self):
        pass


class UkrainianBot(Bot):
    def add(self, args, addressBook):
        if addressBook is None:
            logger.fatal('Address book is None')
            return
        if len(args) == 0:
            logger.error(f"Can not add a user without a name and a phone ({args})")
            return
        elif len(args) == 1:
            logger.warning(f"args received {args}, but expected two")
            name, = args
            phone = ''
        else:
            name, phone = args
        addressBook.update({name: phone})
        logger.info("user added")
        logger.debug(f"user ({name, phone}) was added to dict: {addressBook}")
        print("Користувача додано.")

    def all(self, addressBook):
        if addressBook is None:
            logger.fatal('Address book is None')
            return
        print(addressBook)

    def bye(self):
        print("Допобачення!")

class EnglishBot(Bot):
    def add(self, args, addressBook):
        name, phone = args
        addressBook.update({name: phone})
        print("User added.")

    def all(self, addressBook):
        print(addressBook)

    def bye(self):
        print("Good bye!")

def main_cli():
    addressBook = AddressBook()
    ukrainian_bot = UkrainianBot()
    while True:
        command, *args = input(">>> ").strip().split(' ')
        if command == 'add':
            ukrainian_bot.add(args, addressBook)
        elif command == 'all':
            addressBook = None
            ukrainian_bot.all(addressBook)
        elif command in ['bye', 'exit']:
            ukrainian_bot.bye()
            break

if __name__ == '__main__':
    main_cli()