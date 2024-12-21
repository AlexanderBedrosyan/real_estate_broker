from django.db import models


class ConsultationChoices(models.TextChoices):
    INVEST = 'Инвестиции', 'Инвестиции'
    STRATEGY = 'Индивидуална стратегия за твоя бизнес', 'Индивидуална стратегия за твоя бизнес'
    REALESTATE = 'Недвижими имоти', 'Недвижими имоти'