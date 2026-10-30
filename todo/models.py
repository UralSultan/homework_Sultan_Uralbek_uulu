from django.db import models

STATUS_CHOICES = [
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
]

class Task(models.Model):
    description = models.TextField('Description')
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField('Due Date', blank=True, null=True)
    detail_descriptions = models.TextField('Detail Descriptions', blank=True, null=True)

    class Meta:
        ordering = ['due_date', 'id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.description[:50]