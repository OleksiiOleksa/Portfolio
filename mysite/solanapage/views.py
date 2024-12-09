from django.shortcuts import render

def solana_page(request):
    return render(request, 'solanapage.html')