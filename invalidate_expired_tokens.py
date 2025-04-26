from django.core.management.base import BaseCommand
from myapp.models import AuthToken  # example token model
from django.utils import timezone

class Command(BaseCommand):
    help = "Deletes expired auth tokens from the database."

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_tokens = AuthToken.objects.filter(expiry__lt=now)
        count = expired_tokens.count()
        expired_tokens.delete()

        self.stdout.write(self.style.SUCCESS(f"Deleted {count} expired tokens."))
