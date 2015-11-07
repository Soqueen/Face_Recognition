from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import ImageForm

# Create your views here.

def save_file(file, path=""):
    """ Save file helper.
    """

    filename = file._get_name()
    fd = open("{}/{}{}".format(settings.MEDIA_ROOT, str(path), str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()

def home(request):
    img_type = ["png", "jpg", "jpeg", "gif", "bmp"]
    template = "home.html"
    feedback = ""
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart() and request.FILES.get("image").name.split(".")[1].lower() in img_type:
            save_file(request.FILES["image"])          
            success = True
            context = {
                "feedback": "success"
            }            
            return render(request, template, context)
        else:
            context = {
                "feedback": "invalid type"
            }                
            return render(request, template, context)
    else:
        form = ImageForm()

    return render_to_response(template, RequestContext(request, {'form': form})) 

