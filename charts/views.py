from django.shortcuts import render

from table.models import (
    AhciCategory, AhciJournal, Ahci,
    Erih,
    JcrCategory, JcrJournal, JcrScore, JcrScoreMore, JcrGroup
)

from django.db.models import Avg, Count, Max, Min


def ahci(request):
    apexcharts_1 = [[], []]
    apexcharts_2 = []

    for item in AhciCategory.objects.annotate(Count("ahcijournal")):  # For all years
        apexcharts_1[0].append(item.category)
        apexcharts_1[1].append(item.ahcijournal__count)

    for item in AhciCategory.objects.all():
        data_values = []
        for year in [2011, 2012, 2013, 2014, 2015]:
            data_values.append(item.ahci_set.filter(year=year).count())

        apexcharts_2.append({"name": item.category, "data": data_values})
        data_values = []

    # data.sort(key=lambda x: x[1], reverse=True)
    # data.sort(key=lambda x: x[1])

    output = {
        "apexcharts_1": apexcharts_1,
        "apexcharts_2": apexcharts_2,
    }

    return render(request, "charts/ahci.html", output)


def erih(request):
    apexcharts_1 = [[
        "Anthropology",
        "Archaeology",
        "Art and Art History",
        "Classical Studies",
        "Gender Studies",
        "History",
        "History & Philosophy of Science",
        "Linguistics",
        "Literature",
        "Musicology",
        "Oriental and African studies",
        "Pedagogical & Educational Research",
        "Philosophy",
        "Psychology",
        "Religious Studies and Theology",
    ], []]
    apexcharts_2 = []
    apexcharts_3 = []
    apexcharts_4 = []
    apexcharts_5 = []

    for item in apexcharts_1[0]:
        number = Erih.objects.filter(discipline=item).count()
        apexcharts_1[1].append(number)

    for item in apexcharts_1[0]:
        data_values = []
        for cat in ["NAT", "INT1", "INT2", None]:
            data_values.append(Erih.objects.filter(discipline=item, cat_2007=cat).count())

        apexcharts_2.append({"name": item, "data": data_values})
        data_values = []

    for item in apexcharts_1[0]:
        data_values = []
        for cat in ["NAT", "INT1", "INT2", None]:
            data_values.append(Erih.objects.filter(discipline=item, cat_2011=cat).count())

        apexcharts_3.append({"name": item, "data": data_values})
        data_values = []

    for cat in ["NAT", "INT1", "INT2", None]:
        data_values = []
        for item in apexcharts_1[0]:
            data_values.append(Erih.objects.filter(cat_2007=cat, discipline=item).count())

        apexcharts_4.append({"name": cat if cat is not None else "N/A", "data": data_values})
        data_values = []

    for cat in ["NAT", "INT1", "INT2", None]:
        data_values = []
        for item in apexcharts_1[0]:
            data_values.append(Erih.objects.filter(cat_2011=cat, discipline=item).count())

        apexcharts_5.append({"name": cat if cat is not None else "N/A", "data": data_values})
        data_values = []

    output = {
        "apexcharts_1": apexcharts_1,
        "apexcharts_2": apexcharts_2,
        "apexcharts_3": apexcharts_3,
        "apexcharts_4": apexcharts_4,
        "apexcharts_5": apexcharts_5,
    }

    return render(request, "charts/erih.html", output)


def jcr_scores(request):
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

    apexcharts_1 = [
        {"name": "AIS", "data": []},
        {"name": "RIS", "data": []},
        {"name": "RIF", "data": []},
    ]

    apexcharts_2 = [
        {"name": "AIS", "data": []},
        {"name": "RIS", "data": []},
        {"name": "RIF", "data": []},
    ]

    for year in years:
        apexcharts_1[0]["data"].append(JcrScore.objects.filter(year=year).aggregate(Max("ais"))["ais__max"])
        apexcharts_1[1]["data"].append(JcrScore.objects.filter(year=year).aggregate(Max("ris"))["ris__max"])
        apexcharts_1[2]["data"].append(JcrScore.objects.filter(year=year).aggregate(Max("rif"))["rif__max"])

    for year in years:
        apexcharts_2[0]["data"].append(JcrScore.objects.filter(year=year).aggregate(Avg("ais"))["ais__avg"])
        apexcharts_2[1]["data"].append(JcrScore.objects.filter(year=year).aggregate(Avg("ris"))["ris__avg"])
        apexcharts_2[2]["data"].append(JcrScore.objects.filter(year=year).aggregate(Avg("rif"))["rif__avg"])

    output = {
        "apexcharts_1": apexcharts_1,
        "apexcharts_2": apexcharts_2,
    }

    return render(request, "charts/jcr_scores.html", output)
