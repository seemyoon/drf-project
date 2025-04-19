import time

from django.core.management import BaseCommand
from django.db import OperationalError, connection
# IMPORTANT CONNECTION WITHOUT 's
from django.db.backends.mysql.base import DatabaseWrapper

connection: DatabaseWrapper = connection


class Command(BaseCommand):  # Creates a custom Django command
    def handle(self, *args, **options):  # method that is executed when the command is run
        self.stdout.write('Waiting for database...')  # Outputs a message to the console
        con_db = False

        while not con_db:
            try:
                connection.ensure_connection()  # try to connect to db, if will be an error throw in OperationalError
                con_db = True
            except OperationalError:  # we will have an error, if our connection is failed
                self.stdout.write("Database unavailable, wait 3 seconds")
                time.sleep(3)

        self.stdout.write(self.style.SUCCESS('Database available'))
