from .models import BioData

def biodata(request):
    return {"biodata": BioData.objects.all()}