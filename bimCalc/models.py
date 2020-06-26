from django.db import models


class Project(models.Model):
    types = (
        ('', 'Choose..'),
        ('R', 'Residential'),
        ('C', 'Commercial'),
        ('In', 'Industrial'),
        ('If', 'Infrastructure'),
        ('E', 'Educational'),
        ('M', 'Medical'),
    )

    size = (
        ('', 'Choose..'),
        ('Large', 'Large >100M'),
        ('Medium', 'Medium >50:100M'),
        ('Small', 'Small <50M')
    )

    choices = (
        ('', 'Choose..'),
        ('Very', 'Very High'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    )

    type = models.CharField(max_length=25, choices=types)
    project_size = models.CharField(max_length=6, choices=size)
    cost = models.IntegerField()
    duration = models.IntegerField()
    document_work = models.CharField(max_length=6, choices=choices)
    reduced_rework = models.CharField(max_length=6, choices=choices)
    fewer_claims = models.CharField(max_length=6, choices=choices)
    COST_PERCENT = models.FloatField(default=30.4)
    DURATION_PERCENT = models.FloatField(default=21.1)

    def __str__(self):
        return self.type

    def get_types(self):
        return self.types.all()

    def get_type_percent(self, type):
        percent = 0
        if type == 'R' or type == 'If' or type == 'M':
            percent = 1
        elif type == 'C':
            percent = 0.75
        elif type == 'In':
            percent = 0.5
        else:
            percent = 0.75

        percent = percent * 0.15
        return percent

    def get_size_percent(self, size):
        percent = 0
        if size == 'Large':
            percent = 1
        elif size == 'Medium':
            percent = 0.75
        else:
            percent = 0.5

        percent = percent * 0.4
        return percent

    def get_attributes_percent(self, label):
        percent = 0
        if label == 'Very':
            percent = 1
        elif label == 'High':
            percent = 0.75
        elif label == 'Medium':
            percent = 0.5
        else:
            percent = 0.25

        percent = percent * 0.15
        return percent







