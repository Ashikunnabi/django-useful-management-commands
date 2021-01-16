from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Set fixtures to setup default data in database.'

    def handle(self, *args, **options):
        print('[+] Feature: ', end='')
        call_command('loaddata', 'fixtures/feature.json')
        print('[+] Permission: ', end='')
        call_command('loaddata', 'fixtures/permission.json')
        print('[+] Role: ', end='')
        call_command('loaddata', 'fixtures/role.json')
        print('[+] Tenant: ', end='')
        call_command('loaddata', 'fixtures/tenant.json')
        print('[+] User: ', end='')
        call_command('loaddata', 'fixtures/user.json')

