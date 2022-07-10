from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'ai/simple_upload_ed.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'ai/simple_upload.html')

def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        return render(request, 'ai/base.html')
