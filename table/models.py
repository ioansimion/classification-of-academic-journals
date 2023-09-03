from django.db import models

# dir(Ahci_Category)
# 'ahci_journal_set'
# 'ahci_set'
# 'category'
# 'id'

# dir(Ahci_Journal)
# 'ahci_set'
# 'category'
# 'id'
# 'issn'
# 'objects'
# 'title'

# dir(Ahci)
# 'category'
# 'category_id'
# 'id'
# 'journal'
# 'journal_id'
# 'objects'
# 'year'

erih_disciplines = [
    'Anthropology',
    'Archaeology',
    'Art and Art History',
    'Classical Studies',
    'Gender Studies',
    'History',
    'History & Philosophy of Science',
    'Linguistics',
    'Literature',
    'Musicology',
    'Oriental and African studies',
    'Pedagogical & Educational Research',
    'Philosophy',
    'Psychology',
    'Religious Studies and Theology'
]

erih_cat = [
    'NAT',
    'INT1',
    'INT2',
    None
]


# ARTS AND HUMANITIES CITATION INDEX
class AhciCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return "AhciCategory object " + self.category + " :)"


class AhciJournal(models.Model):
    issn = models.CharField(max_length=9)
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(AhciCategory, through="Ahci")

    def __str__(self):
        return self.title


class Ahci(models.Model):
    journal = models.ForeignKey(AhciJournal, on_delete=models.CASCADE)
    category = models.ForeignKey(AhciCategory, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()


# EUROPEAN REFERENCE INDEX FOR THE HUMANITIES
class Erih(models.Model):
    issn = models.CharField(max_length=9)
    title = models.CharField(max_length=250)
    discipline = models.CharField(max_length=200)
    cat_2007 = models.CharField(max_length=4, null=True)
    cat_2011 = models.CharField(max_length=4, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(discipline__in=erih_disciplines), name="confirm_discipline"),
            # Maybe we won't use this after refactoring models
            # models.CheckConstraint(check=models.Q(cat_2007__in=erih_cat) & models.Q(cat_2011__in=erih_cat), name="confirm_cat")
        ]


# JOURNAL CITATION REPORTS
class JcrCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class JcrJournal(models.Model):
    issn = models.CharField(max_length=9, null=True)
    title = models.CharField(max_length=200, null=True)
    # cifre_exacte = models.ManyToManyField(Jcr_Category, through="Jcr_Cifre_Exacte")  # That's a NO-NO, not many to many (6 errors)
    # cifre_exacte_extended = models.ManyToManyField(Jcr_Category, through="Jcr_Cifre_Exacte_Extended")
    # grupe = models.ManyToManyField(Jcr_Category, through="Jcr_Grupe")

    def __str__(self):
        return self.title


class JcrScore(models.Model):
    journal = models.ForeignKey(JcrJournal, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    ais = models.FloatField(null=True)
    ris = models.FloatField(null=True)
    rif = models.FloatField(null=True)


class JcrScoreMore(models.Model):
    journal = models.ForeignKey(JcrJournal, on_delete=models.CASCADE)
    category = models.ForeignKey(JcrCategory, on_delete=models.CASCADE)
    index = models.CharField(max_length=4)
    year = models.PositiveSmallIntegerField()
    ais = models.FloatField()
    quartile = models.PositiveSmallIntegerField(null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(index__in=['SCIE', 'SSCI']), name="confirm_index_cifre")
        ]


class JcrGroup(models.Model):
    journal = models.ForeignKey(JcrJournal, on_delete=models.CASCADE)
    category = models.ForeignKey(JcrCategory, on_delete=models.CASCADE)
    type = models.CharField(max_length=3)
    year = models.PositiveSmallIntegerField()
    index = models.CharField(max_length=4)
    zone = models.PositiveSmallIntegerField()
    top = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(index__in=['SCIE', 'SSCI']), name="confirm_index_grupe"),
            models.CheckConstraint(check=models.Q(type__in=['ais', 'if']), name="confirm_type")
        ]

# 398,536 total deocamdata :))