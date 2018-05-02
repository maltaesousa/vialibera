from django.core.management.base import BaseCommand, CommandError
from enrolments.models import Course, Student
from faker import Faker
import datetime

class Command(BaseCommand):
  help = 'Generates fake data'

  def add_arguments(self, parser):
    parser.add_argument('n', nargs=1, type=int)

  def handle(self, *args, **options):
    fake = Faker()
    for i in range(options['n'][0]):
      datetime_start = fake.date_time_this_year(before_now=False, after_now=True)
      course = Course(
        name = fake.sentence(nb_words=3, variable_nb_words=True),
        description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True),
        price = fake.pydecimal(left_digits=None, right_digits=None, positive=True),
        datetime_start = datetime_start,
        datetime_end = datetime_start + datetime.timedelta(hours=3)
      )
      course.save()
      self.stdout.write(self.style.SUCCESS('Successfully faked "%s"' % course))