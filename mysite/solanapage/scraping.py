# solanapage/scraping.py
import requests

def fetch_solana_news():
    news = []
    api_key = "d4b6969745e945cda48360752a325b8a"  # Ваш API ключ
    url = f"https://newsapi.org/v2/everything?q=solana&language=en&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
        data = response.json()

        # Получаем список статей, ограничиваем до 10
        articles = data.get('articles', [])[:10]
        
        # Сортировка новостей по времени (по убыванию, где первая - самая свежая)
        articles.sort(key=lambda article: article['publishedAt'], reverse=True)

        for article in articles:
            # Преобразуем время в удобный формат
            published_at = article.get('publishedAt', '')
            title = article.get('title', '')
            link = article.get('url', '')
            description = article.get('description', 'No description available.')
            
            news.append({
                "title": title,
                "link": link,
                "description": description,
                "published_at": published_at
            })

        return news
    except Exception as e:
        print(f"Error fetching Solana news: {e}")
        return []
