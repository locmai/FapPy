from mcontroller.models import Masturbation
from mcontroller.constants import METRICS_CHECK


class DataHandler:
    def csv_data_handler_self(current_user):
        all_masturbations = Masturbation.objects.filter(m_user=current_user.id)
        data_raw = [["reason", "method", "duration", "date"]]
        for m in all_masturbations:
            data_raw.append([m.m_reason, m.m_method, m.m_duration, m.m_date])
        return data_raw
