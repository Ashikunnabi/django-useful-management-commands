import os
from django.core.management.base import BaseCommand
from django.conf import settings
from myapp.models import UploadedFile

class Command(BaseCommand):
    help = "Syncs file storage with the database by finding unreferenced files."

    def handle(self, *args, **kwargs):
        media_root = settings.MEDIA_ROOT
        db_files = set(UploadedFile.objects.values_list('file', flat=True))
        
        file_system_files = set()
        for root, _, files in os.walk(media_root):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), media_root)
                file_system_files.add(rel_path)

        orphaned_files = file_system_files - db_files

        for orphan in orphaned_files:
            full_path = os.path.join(media_root, orphan)
            os.remove(full_path)
            self.stdout.write(self.style.WARNING(f"Deleted orphaned file: {orphan}"))

        self.stdout.write(self.style.SUCCESS(f"Completed sync. {len(orphaned_files)} orphaned files removed."))
