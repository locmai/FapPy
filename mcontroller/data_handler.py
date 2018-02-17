from mcontroller.models import Masturbation
from mcontroller.constants import METRICS_CHECK


class DataHandler:
    def csv_data_handler(*argv):
        print(argv)
        all_masturbations = Masturbation.objects.all()
        #del_indexes = []
        # for i in range(len(METRICS_CHECK)):
        #     if METRICS_CHECK[i].get_value_name in argv:
        #         del_indexes.append(i)

        data_raw = []
        data_raw.append(["reason", "method", "duration", "date"])
        for m in all_masturbations:
            data_raw.append([m.m_reason, m.m_method, m.m_duration, m.m_date])

        # data_filtered = []
        # for elem in data_raw:
        #     tmp = []
        #     for i in range(len(elem)):
        #         if i not in del_indexes:
        #             tmp.append(elem[i])
        #     data_filtered.append(tmp)

        return data_raw
