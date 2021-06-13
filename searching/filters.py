import django_filters
from users.models import Profile


class AlumniFilterDirectorate(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ('college',
                  'course',
                  'passing_year',
                  'roll_number'
                  )


class AlumniFilterCollege(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ('course', 'passing_year', 'roll_number')
