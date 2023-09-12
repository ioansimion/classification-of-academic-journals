from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import (
    AhciCategory, AhciJournal, Ahci,
    Erih,
    JcrCategory, JcrJournal, JcrScore, JcrScoreMore, JcrGroup
)


def redirect_home(request):
    return redirect('table:home')


def base(request):
    return render(request, "table/base.html", {})


def home(request):
    return render(request, "table/home.html", {})


def paginate(request, results, output):
    requested_page = output["requested_page"] = 1  # Initially we are on the first page
    results_start = 0  # So we start at element 0
    results_end = number_of_results = 100  # And we have 100 results per page

    copy_of_GET = request.GET.copy()  # We will use this

    if request.GET.get("results"):
        results_end = number_of_results = int(request.GET.get("results"))

    if number_of_results != 100:
        output["number_of_results"] = number_of_results

    if request.GET.get("page"):
        requested_page = int(request.GET.get("page"))
        output["requested_page"] = requested_page

        # Update results range based on the current page
        results_start = number_of_results * (requested_page - 1)
        results_end = number_of_results * requested_page
        copy_of_GET.pop("page")  # Get rid of the page in GET

    output["data"] = results.all()[results_start:results_end]
    output["total_results"] = f"{results.count():,}"
    total_pages = results.count() // number_of_results + 1
    output["total_pages"] = total_pages

    generated_pages = range(requested_page - 2, requested_page + 3)  # General case

    # This block must be after total_pages variable
    if requested_page < 3:  # First two pages
        if total_pages > 5:
            generated_pages = range(1, 6)
        else:
            generated_pages = range(1, total_pages + 1)

    elif requested_page > total_pages - 2:  # Last two pages
        if total_pages > 5:
            generated_pages = range(total_pages - 4, total_pages + 1)
        else:
            generated_pages = range(1, total_pages + 1)

    # We create page links
    links = []

    # This block must be after the above one
    for number in generated_pages:
        copy_of_GET.update({"page": number})  # Unfortunately, page query will be placed at the end
        links.append("?" + copy_of_GET.urlencode())
        copy_of_GET.pop("page")

    copy_of_GET.update({"page": 1})
    output["first_page"] = "?" + copy_of_GET.urlencode()
    copy_of_GET.pop("page")

    copy_of_GET.update({"page": total_pages})
    output["last_page"] = "?" + copy_of_GET.urlencode()
    copy_of_GET.pop("page")

    copy_of_GET.update({"page": requested_page + 1})
    output["next_page"] = "?" + copy_of_GET.urlencode()
    copy_of_GET.pop("page")

    copy_of_GET.update({"page": requested_page - 1})
    output["previous_page"] = "?" + copy_of_GET.urlencode()
    copy_of_GET.pop("page")

    output["pages_links"] = zip(generated_pages, links)


def ahci(request):
    output = {}  # Output is a dictionary

    results = Ahci.objects

    if request.GET.get("search"):
        searched_string = request.GET.get("search")
        output["searched_string"] = searched_string
        results = results.filter(journal__title__icontains=searched_string) |\
            results.filter(journal__issn__icontains=searched_string) |\
            results.filter(category__category__icontains=searched_string)
        output["filters_are_applied"] = True

    if request.GET.get("category"):
        requested_categories = AhciCategory.objects.filter(category__in=request.GET.getlist("category"))
        output["requested_categories"] = [item.category for item in requested_categories]
        results = results.filter(category__in=requested_categories)
        output["filters_are_applied"] = True

    if request.GET.get("year"):
        requested_years = request.GET.getlist("year")
        output["requested_years"] = requested_years
        results = results.filter(year__in=requested_years)
        output["filters_are_applied"] = True

    if request.GET.get("sort"):
        requested_sort = request.GET.getlist("sort")
        output["requested_sort"] = requested_sort
        results = results.order_by(*requested_sort)
        output["filters_are_applied"] = True

    output["all_categories"] = [item.category for item in AhciCategory.objects.all()]
    output["all_years"] = ['2011', '2012', '2013', '2014', '2015']

    paginate(request, results, output)

    print(output.keys())

    return render(request, "table/ahci.html", output)


def erih(request):
    output = {}

    results = Erih.objects

    if request.GET.get("search"):
        searched_string = request.GET.get("search")
        output["searched_string"] = searched_string
        results = results.filter(title__icontains=searched_string) |\
            results.filter(issn__icontains=searched_string) |\
            results.filter(discipline__icontains=searched_string) |\
            results.filter(cat_2007__icontains=searched_string) |\
            results.filter(cat_2011__icontains=searched_string)
        output["filters_are_applied"] = True

    if request.GET.get("discipline"):
        requested_disciplines = request.GET.getlist("discipline")
        results = results.filter(discipline__in=requested_disciplines)
        output["requested_disciplines"] = [item for item in requested_disciplines]
        output["filters_are_applied"] = True

    if request.GET.get("cat_2007"):
        requested_cat_2007 = request.GET.getlist("cat_2007")
        results = results.filter(cat_2007__in=requested_cat_2007)
        output["requested_cat_2007"] = [item for item in requested_cat_2007]
        output["filters_are_applied"] = True

    if request.GET.get("cat_2011"):
        requested_cat_2011 = request.GET.getlist("cat_2011")
        results = results.filter(cat_2011__in=requested_cat_2011)
        output["requested_cat_2011"] = [item for item in requested_cat_2011]
        output["filters_are_applied"] = True

    if request.GET.get("sort"):
        requested_sort = request.GET.getlist("sort")
        results = results.order_by(*requested_sort)
        output["requested_sort"] = [item for item in requested_sort]
        output["filters_are_applied"] = True

    output["all_disciplines"] = [
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
    ]
    output["all_categories"] = ["NAT", "INT1", "INT2"]

    paginate(request, results, output)

    return render(request, "table/erih.html", output)


def jcr_scores(request):
    output = {}

    results = JcrScore.objects

    if request.GET.get("search"):
        searched_string = request.GET.get("search")
        output["searched_string"] = searched_string
        results = results.filter(journal__title__icontains=searched_string) |\
            results.filter(journal__issn__icontains=searched_string)
        output["filters_are_applied"] = True

    if request.GET.get("year"):
        requested_year = request.GET.getlist("year")
        results = results.filter(year__in=requested_year)
        output["requested_years"] = [year for year in requested_year]
        output["filters_are_applied"] = True

    if request.GET.get("ais_min"):
        requested_ais_min = request.GET.get("ais_min")
        results = results.filter(ais__gte=requested_ais_min)
        output["requested_ais_min"] = requested_ais_min
        output["filters_are_applied"] = True

    if request.GET.get("ais_max"):
        requested_ais_max = request.GET.get("ais_max")
        results = results.filter(ais__lte=requested_ais_max)
        output["requested_ais_max"] = requested_ais_max
        output["filters_are_applied"] = True

    if request.GET.get("ris_min"):
        requested_ris_min = request.GET.get("ris_min")
        results = results.filter(ris__gte=requested_ris_min)
        output["requested_ris_min"] = requested_ris_min
        output["filters_are_applied"] = True

    if request.GET.get("ris_max"):
        requested_ris_max = request.GET.get("ris_max")
        results = results.filter(ris__lte=requested_ris_max)
        output["requested_ris_max"] = requested_ris_max
        output["filters_are_applied"] = True

    if request.GET.get("rif_min"):
        requested_rif_min = request.GET.get("rif_min")
        results = results.filter(rif__gte=requested_rif_min)
        output["requested_rif_min"] = requested_rif_min
        output["filters_are_applied"] = True

    if request.GET.get("rif_max"):
        requested_rif_max = request.GET.get("rif_max")
        results = results.filter(rif__lte=requested_rif_max)
        output["requested_rif_max"] = requested_rif_max
        output["filters_are_applied"] = True

    if request.GET.get("sort"):
        requested_sort = request.GET.getlist("sort")
        results = results.order_by(*requested_sort)
        output["requested_sort"] = [item for item in requested_sort]
        output["filters_are_applied"] = True

    output["all_years"] = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]

    paginate(request, results, output)

    return render(request, "table/jcr_scores.html", output)


def jcr_scores_more(request):
    output = {}

    results = JcrScoreMore.objects

    if request.GET.get("search"):
        searched_string = request.GET.get("search")
        output["searched_string"] = searched_string
        results = results.filter(journal__title__icontains=searched_string) |\
            results.filter(journal__issn__icontains=searched_string) |\
            results.filter(index__icontains=searched_string) |\
            results.filter(category__category__icontains=searched_string)
        output["filters_are_applied"] = True

    if request.GET.get("category"):
        requested_categories = JcrCategory.objects.filter(category__in=request.GET.getlist("category"))
        results = results.filter(category__in=requested_categories)
        output["requested_categories"] = [item.category for item in requested_categories]
        # requested_categories = request.GET.getlist("category")
        # results = results.filter(category__category__in=requested_categories)
        # output["requested_categories"] = [item for item in requested_categories]
        output["filters_are_applied"] = True

    if request.GET.get("year"):
        requested_year = request.GET.getlist("year")
        results = results.filter(year__in=requested_year)
        output["requested_years"] = [year for year in requested_year]
        output["filters_are_applied"] = True

    if request.GET.get("quartile"):
        requested_quartiles = request.GET.getlist("quartile")
        results = results.filter(quartile__in=requested_quartiles)
        output["requested_quartiles"] = [quartile for quartile in requested_quartiles]
        output["filters_are_applied"] = True

    if request.GET.get("index"):
        requested_indexes = request.GET.getlist("index")
        results = results.filter(index__in=requested_indexes)
        output["requested_indexes"] = [item for item in requested_indexes]
        output["filters_are_applied"] = True
    
    if request.GET.get("ais_min"):
        requested_ais_min = request.GET.get("ais_min")
        results = results.filter(ais__gte=requested_ais_min)
        output["requested_ais_min"] = requested_ais_min
        output["filters_are_applied"] = True

    if request.GET.get("ais_max"):
        requested_ais_max = request.GET.get("ais_max")
        results = results.filter(ais__lte=requested_ais_max)
        output["requested_ais_max"] = requested_ais_max
        output["filters_are_applied"] = True

    if request.GET.get("sort"):
        requested_sort = request.GET.getlist("sort")
        results = results.order_by(*requested_sort)
        output["requested_sort"] = [item for item in requested_sort]
        output["filters_are_applied"] = True

    output["all_categories"] = [item.category for item in JcrCategory.objects.all()]
    output["all_years"] = ["2012", "2013", "2018", "2019"]
    output["all_quartiles"] = ['1','2','3','4']
    output["all_indexes"] = ["SCIE", "SSCI"]

    paginate(request, results, output)

    # Tema
    # output["filters_are_applied"] = "category" in request.GET or "year" in request.GET or "quartile" in request.GET or "index" in request.GET or "sort" in request.GET

    return render(request, "table/jcr_scores_more.html", output)


def jcr_groups(request):
    output = {}

    results = JcrGroup.objects

    if request.GET.get("search"):
        searched_string = request.GET.get("search")
        output["searched_string"] = searched_string
        results = results.filter(journal__title__icontains=searched_string) |\
            results.filter(journal__issn__icontains=searched_string) |\
            results.filter(type__icontains=searched_string) |\
            results.filter(index__icontains=searched_string) |\
            results.filter(category__category__icontains=searched_string)
        output["filters_are_applied"] = True

    if request.GET.get("type"):
        requested_types = request.GET.getlist("type")
        results = results.filter(type__in=requested_types)
        output["requested_types"] = [item for item in requested_types]
        output["filters_are_applied"] = True

    if request.GET.get("index"):
        requested_indexes = request.GET.getlist("index")
        results = results.filter(index__in=requested_indexes)
        output["requested_indexes"] = [item for item in requested_indexes]
        output["filters_are_applied"] = True

    if request.GET.get("category"):
        requested_categories = JcrCategory.objects.filter(category__in=request.GET.getlist("category"))
        results = results.filter(category__in=requested_categories)
        output["requested_categories"] = [item.category for item in requested_categories]
        # requested_categories = request.GET.getlist("category")
        # results = results.filter(category__category__in=requested_categories)
        # output["requested_categories"] = [item for item in requested_categories]
        output["filters_are_applied"] = True

    if request.GET.get("zone"):
        requested_zones = request.GET.getlist("zone")
        results = results.filter(zone__in=requested_zones)
        output["requested_zones"] = [zone for zone in requested_zones]
        output["filters_are_applied"] = True

    if request.GET.get("year"):
        requested_year = request.GET.getlist("year")
        results = results.filter(year__in=requested_year)
        output["requested_years"] = [year for year in requested_year]
        output["filters_are_applied"] = True

    if request.GET.get("sort"):
        requested_sort = request.GET.getlist("sort")
        results = results.order_by(*requested_sort)
        output["requested_sort"] = [item for item in requested_sort]
        output["filters_are_applied"] = True

    output["all_types"] = ["ais", "if"]
    output["all_indexes"] = ["SCIE", "SSCI"]
    output["all_categories"] = [item.category for item in JcrCategory.objects.all()]
    output["all_zones"] = ['1','2','3']
    output["all_years"] = ["2015", "2016", "2017", "2018", "2019"]

    paginate(request, results, output)

    return render(request, "table/jcr_groups.html", output)


def jcr_journal_detail(request, journal_id):
    output = {}

    try:
        journal = JcrJournal.objects.get(id=journal_id)

        jcrscore_data = journal.jcrscore_set.all()
        jcrscoremore_data = journal.jcrscoremore_set.all()
        jcrgroup_data = journal.jcrgroup_set.all()

        if AhciJournal.objects.filter(issn=journal.issn).exists():
            ahcijournal = AhciJournal.objects.get(issn=journal.issn)
            ahci_data = ahcijournal.ahci_set.all()
            output['ahci_data'] = ahci_data

        if Erih.objects.filter(issn=journal.issn).exists():
            erih_data = Erih.objects.filter(issn=journal.issn)
            output['erih_data'] = erih_data

        output['journal'] = journal
        output['jcrscore_data'] = jcrscore_data
        output['jcrscoremore_data'] = jcrscoremore_data
        output['jcrgroup_data'] = jcrgroup_data

    except ObjectDoesNotExist:
        print("Journal was not found. Will display an error page.")

    return render(request, 'table/jcr_journal_detail.html', output)
