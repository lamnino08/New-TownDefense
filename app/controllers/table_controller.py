from django.shortcuts import render
from app.models.table import Table

def view_table_status(request):
    tables = Table.objects.all()
    return render(request, 'table/view_table_status.html', {'tables': tables})

def update_table_status(request, table_id):
    table = Table.objects.get(pk=table_id)
    table.is_available = True
    table.save()
    return redirect('table_status')
