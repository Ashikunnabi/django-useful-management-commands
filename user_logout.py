from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):

    help = 'Logout all/specific currently logged in (session based) user(s).'
    user = get_user_model()

    def handle(self, *args, **options):
        print('Available group: '
              '\n1. Single user'
              '\n2. All user (default)'
              '\n3. Exit'
              )

        # get user input
        selected_group = input('Select a group to logout user(s): ')

        if not self.is_valid_input(selected_group):
            # check invalid input input
            print('Invalid selection.')
            return
        if selected_group == '3':
            print('End')
            return

        if selected_group == '1':
            username = input('Please provide username: ')
            self.logout_single_user(username)
            return

        if selected_group == '' or selected_group == '2':
            self.logout_all_users()
            return

    @staticmethod
    def is_valid_input(value):
        if value is '':
            return True
        try:
            # type conversion to integer
            int_value = int(value)
            if int_value not in [1, 2, 3]:
                return False
        except Exception:
            return False
        return True

    def logout_single_user(self, username):

        if not self.user.objects.filter(username=username).exists():
            # if username is not available then stop execution
            print('No active user found with this username.')
            return

        # get all non-expired sessions
        sessions = Session.objects.filter(expire_date__gte=timezone.now())
        user_id = self.user.objects.get(username=username).id
        does_session_expired = False

        # do session expire
        for session in sessions:
            data = session.get_decoded()
            if str(user_id) == data.get('_auth_user_id', None):
                session.expire_date = timezone.now()
                session.save()
                does_session_expired = True
                print(f'"{username}" logged out successfully.')
                break

        if not does_session_expired:
            print('No active user found with this username')

    @staticmethod
    def logout_all_users():
        # log out all currently logged in users
        Session.objects.filter(expire_date__gte=timezone.now()).update(
            expire_date=timezone.now()
        )
        print('All users are logged out successfully')




