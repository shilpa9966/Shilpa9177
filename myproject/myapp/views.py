from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def generate_pdf(request):
    # Sample data for PDF
    context = {
        'title': 'Test PDF',
        'message': 'Hello! This PDF was generated from Django.'
    }

    # Load template and render with context
    template = get_template('pdf_template.html')
    html = template.render(context)

    # Create PDF response with correct content-type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="test.pdf"'

    # Generate PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors while generating PDF')
    return response

# Create your views here.
