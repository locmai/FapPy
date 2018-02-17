from mcontroller.models import Masturbation
from datetime import timedelta


class Info(object):
    def __init__(self):
        self.all_m = Masturbation.objects.all()

    @property
    def total_m_times(self):
        return self.all_m.count()

    @property
    def last_date(self):
        return self.all_m.latest("id").m_date

    @property
    def total_duration(self):
        return sum([masturbation.m_duration for masturbation in self.all_m])

    @property
    def longest_time_before_masturbate(self):
        date_max = timedelta.min
        for i in range(self.all_m.count() - 1):
            diff_datetime = self.all_m[i + 1].m_date - self.all_m[i].m_date
            if diff_datetime > date_max:
                date_max = diff_datetime
        return str(self.pretty_time_delta(date_max.total_seconds()))

    def pretty_time_delta(self, seconds):
        sign_string = '-' if seconds < 0 else ''
        seconds = abs(int(seconds))
        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        if days > 0:
            return '%s%dd%dh%dm%ds' % (sign_string, days, hours, minutes, seconds)
        elif hours > 0:
            return '%s%dh%dm%ds' % (sign_string, hours, minutes, seconds)
        elif minutes > 0:
            return '%s%dm%ds' % (sign_string, minutes, seconds)
        else:
            return '%s%ds' % (sign_string, seconds)
