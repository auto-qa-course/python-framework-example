import datetime


class BaseLogger:

    @staticmethod
    def write(log_message='', log_level='INFO'):
        print('{} {}: {}'.format(log_level,
                                 str(datetime.datetime.utcnow()),
                                 log_message))
