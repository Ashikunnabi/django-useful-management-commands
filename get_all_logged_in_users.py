from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):

    help = 'See all currently logged in (session based) users.'
    user = get_user_model()

    def handle(self, *args, **options):
        users = self.get_all_logged_in_users()
        print(f'{"ID":<20}{"USERNAME":<30}{"EMAIL":<30}{"FULL NAME":<30}')
        [print(f''
               f'{user.id:<20}'
               f'{user.username:30}'
               f'{user.email:30}'
               f'{user.get_full_name():30}'
               f'')for user in users]

        print(f'\nTotal {users.count()} users are currently logged in.')

    def get_all_logged_in_users(self):
        # get all non-expired sessions
        sessions = Session.objects.filter(expire_date__gte=timezone.now())
        user_ids = []

        # Build a list of user ids from that query
        for session in sessions:
            data = session.get_decoded()
            user_ids.append(data.get('_auth_user_id', None))

        # return all logged in users based on id list
        return self.user.objects.filter(id__in=user_ids)




