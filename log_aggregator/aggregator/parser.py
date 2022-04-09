import datetime

from apachelogs import LogParser
from django.conf import settings

from .models import LogFile


names = [
    'ip_address', 'l', 'timestamp', 'timezone',
    'request', 'status', 'bytes', 'referer', 'useragent'
]


def save_logs(
    ip_address: str,
    timestamp: datetime.datetime,
    status: int,
    bytes: str,
    referer: str,
    useragent: str,
    request: str,
):
    """ Сохраняет распаршенный логи
    """
    log = LogFile(
        ip_address=str(ip_address),
        timestamp=timestamp,
        status=int(status),
        bytes=str(bytes),
        referer=str(referer),
        useragent=str(useragent),
        request=str(request),
    )
    log.save()
    return log


# local_tz = pytz.timezone('Europe/Moscow')
#
#
# def utc_to_local(utc_dt):
#     """ Преобразует UTC в Europe/Moscow
#     """
#     local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
#     return local_tz.normalize(local_dt)


def parse_log_file() -> (int, dict):
    """ Парсит Лог-файл
    """
    if settings.PATH_APACHE_LOGS is None:
        return 0, {"error": "Нет пути до файла"}
    if settings.MASK_APACHE_LOGS is None:
        return 0, {"error": "Введите маску"}

    parser = LogParser(settings.MASK_APACHE_LOGS)
    logs = []
    with open(settings.PATH_APACHE_LOGS) as fp:
        for entry in parser.parse_lines(fp):
            timestamp = entry.request_time.strftime("%Y-%m-%dT%H:%M:%S")
            log = save_logs(
                ip_address=entry.remote_host,
                timestamp=timestamp,
                status=entry.final_status,
                bytes=entry.bytes_sent,
                referer=entry.headers_in["Referer"],
                useragent=entry.headers_in["User-Agent"],
                request=entry.request_line,
            )
            logs.append(log)

    return len(logs), {}

