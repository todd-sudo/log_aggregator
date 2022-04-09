from config import celery_app
from .parser import save_logs, parse_log_file
from .models import LogFile


@celery_app.task(
    bind=True,
    name="aggregator.parse_logs_task",
    default_retry_delay=1 * 10,
    max_retries=5,
    soft_time_limit=60 * 5,
    time_limit=60 * 5,
)
def parse_logs_task(self):
    """ Задача для парсинга и сохранения логов в БД
    """
    count_logs, err = parse_log_file()
    if err is not None:
        return err
    return f"Логов сохранено: {count_logs}"


@celery_app.task(
    bind=True,
    name="aggregator.delete_all_logs_task",
    default_retry_delay=1 * 10,
    max_retries=5,
    soft_time_limit=60 * 5,
    time_limit=60 * 5,
)
def delete_all_logs_task(self):
    """ Задача по удалению всех логов
    """
    logs = LogFile.objects.all()
    logs.delete()
