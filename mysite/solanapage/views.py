import requests
from django.shortcuts import render
from django.http import JsonResponse
from .scraping import fetch_solana_news
from .ecosystem import fetch_ecosystem_projects
from django.core.cache import cache

def solana_page(request):
    news = fetch_solana_news()
    print("Fetched News:", news)  # Добавляем лог для проверки
    ecosystem_projects = fetch_ecosystem_projects()
    print("Fetched Ecosystem Projects:", ecosystem_projects)  # Лог для проектов
    return render(request, 'solanapage.html', {
        "articles": news,
        "ecosystem_projects": ecosystem_projects
    })

def get_average_price(request):
    days = request.GET.get('days', 7)  # Период, по умолчанию 7 дней

    # Проверяем, есть ли кэшированные данные
    cache_key = f"solana_average_price_{days}days"
    cached_data = cache.get(cache_key)

    if cached_data:
        return JsonResponse(cached_data)  # Возвращаем кэшированные данные

    try:
        url = f"https://api.coingecko.com/api/v3/coins/solana/market_chart?vs_currency=usd&days={days}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        prices = [point[1] for point in data["prices"]]
        average_price = sum(prices) / len(prices)

        # Кэшируем данные на 5 минут (300 секунд)
        cache.set(cache_key, {"success": True, "average_price": round(average_price, 2)}, timeout=300)

        return JsonResponse({"success": True, "average_price": round(average_price, 2)})
    except requests.RequestException as e:
        return JsonResponse({"success": False, "error": str(e)})
    

def solana_news(request):
    api_key = 'd4b6969745e945cda48360752a325b8a'  # Вставьте сюда свой API ключ
    url = f"https://newsapi.org/v2/everything?q=Solana&language=en&sortBy=publishedAt&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный ответ
        articles = response.json().get('articles', [])
    except requests.exceptions.RequestException as e:
        articles = []  # Если ошибка, возвращаем пустой список

    return render(request, 'solanapage.html', {'articles': articles})    
