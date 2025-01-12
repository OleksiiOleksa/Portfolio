# solanapage/ecosystem.py
import requests

def fetch_ecosystem_projects():
    url = "https://api.coingecko.com/api/v3/coins/solana/tickers"  # Пример: используем CoinGecko для списка бирж
    projects = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        tickers = data.get('tickers', [])
        for ticker in tickers[:10]:  # Ограничиваемся 10 проектами
            projects.append({
                "name": ticker.get('market', {}).get('name', 'Unknown'),
                "link": ticker.get('trade_url', '#'),
                "description": f"Trading pair: {ticker.get('base')} / {ticker.get('target')}",
                "category": "Exchange"
            })

        # Пример дополнительных проектов
        projects.extend([
            {"name": "Phantom Wallet", "link": "https://phantom.app/", "description": "Popular Solana Wallet", "category": "Wallet"},
            {"name": "Magic Eden", "link": "https://magiceden.io/", "description": "Leading NFT Marketplace", "category": "NFT"}
        ])

        return projects
    except Exception as e:
        print(f"Error fetching ecosystem projects: {e}")
        return []
