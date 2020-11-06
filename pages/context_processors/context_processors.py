from pages.models import Pages

def page(request):
    return {"pages": Pages.objects.all()}