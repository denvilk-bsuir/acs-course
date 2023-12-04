import datetime


def to_read_format(datetime: datetime.datetime):
    return datetime.strftime("%H:%M %d/%m/%Y")