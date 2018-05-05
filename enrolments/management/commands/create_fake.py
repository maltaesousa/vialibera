from django.core.management.base import BaseCommand, CommandError
from enrolments.models import Course, Student
from faker import Faker
import datetime, random

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

    for i in range(options['n'][0]*5):
      student = Student(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        address = fake.street_address(),
        zipcode = random.randint(1000,9999),
        city = fake.city(),
        mail = fake.email(),
        phone_number = random.randint(700000000,799999999),
        birthdate = fake.date_between(end_date='-18y')
      )
      student.save()
      self.stdout.write(self.style.SUCCESS('Successfully faked "%s"' % student))
