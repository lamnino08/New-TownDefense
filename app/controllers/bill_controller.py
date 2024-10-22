from django.shortcuts import get_object_or_404, redirect, render
from app.models.bill import Bill

def checkout(request, bill_id):
    bill = Bill.objects.get(bill_id=bill_id)
    bill.is_payed = True
    bill.save()
    return redirect('bill_detail', bill_id=bill.bill_id)

def bill_detail(request, bill_id):
    bill = get_object_or_404(Bill, bill_id=bill_id)
    return render(request, 'bill/detail.html', {'bill': bill})
