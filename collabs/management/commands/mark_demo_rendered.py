from django.core.management.base import BaseCommand
from collabs.models import CollabSub

class Command(BaseCommand):
    
    
    help = 'Marks a response as having its demo rendered'

    def add_arguments(self, parser):
        parser.add_argument('response_id', type=int, help='The ID of the response to mark as having its demo rendered')
        parser.add_argument('demo_file_path', type=str, help='The path to the rendered demo file')

    def handle(self, *args, **options):
        response_id = options['response_id']
        try:
            response = CollabSub.objects.get(pk=response_id)
            response.demoCreated = True
            file_path = options['demo_file_path']
            cleaned_demo_path = file_path.replace('.', '')
            response.demo_file_url = cleaned_demo_path
            response.save()
            self.stdout.write(self.style.SUCCESS(f"Demo created flagged true for response {response_id} marked as True."))
        except CollabSub.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Response with ID {response_id} does not exist."))
