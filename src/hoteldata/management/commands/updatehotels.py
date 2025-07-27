from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Update hotel data"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Sucessfully did nothing. (TODO: implement)")
        )
