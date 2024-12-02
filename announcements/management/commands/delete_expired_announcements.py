# yourapp/management/commands/delete_expired_announcements.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from announcements.models import Announcement

class Command(BaseCommand):
    help = 'Delete announcements older than 14 days'

    def handle(self, *args, **options):
        cutoff_date = timezone.now() - timedelta(days=14)
        deleted = Announcement.objects.filter(date_posted__lt=cutoff_date).delete()[0]
        self.stdout.write(f'Deleted {deleted} expired announcements')