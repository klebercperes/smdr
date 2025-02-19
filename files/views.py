from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import csv
from .models import SMDRData
from .forms import CSVUploadForm

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def upload_customers_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                SMDRData.objects.create(
                    station_number=row.get('station_number', 0),
                    co=row.get('co', 0),
                    time=row.get('time', '00:00:00'),
                    start=row.get('start', '1970-01-01 00:00:00'),
                    direction=row.get('direction', ''),
                    cli=row.get('cli', ''),
                    number=row.get('number', ''),
                    cost=row.get('cost', 0.0),
                    account_code=row.get('account_code', '')
                )
            return redirect('dashboard')
    else:
        form = CSVUploadForm()
    return render(request, 'upload_customers_csv.html', {'form': form})
