from django.db import models


class LogFile(models.Model):
    """ Модель лога
    """
    ip_address = models.CharField(
        "IP", max_length=100, blank=True, null=True
    )
    timestamp = models.DateTimeField("Время", null=True, blank=True)
    request = models.CharField(
        "Запрос", max_length=1000, blank=True, null=True
    )
    status = models.PositiveIntegerField("Статус код", null=True, blank=True)
    bytes = models.CharField("Байты", max_length=100, null=True, blank=True)
    referer = models.CharField(
        "Referer", max_length=1000, blank=True, null=True
    )
    useragent = models.CharField(
        "User-Agent", max_length=500, null=True, blank=True
    )

    def __str__(self):
        return f"{self.ip_address}"

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"
