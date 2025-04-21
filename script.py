import requests
from datetime import datetime, timedelta


def get_content(date):
    url = f"https://free.datiya.com/uploads/{date.strftime('%Y%m%d')}-clash.yaml"
    try:
        response = requests.get(url)
        if response.status_code == 200 and response.text.strip():
            return url, response.text
    except requests.RequestException:
        pass
    return None, None


def main():
    current_date = datetime.now()
    for _ in range(7):
        url, content = get_content(current_date)
        if content:
            with open('clash.yaml', 'w', encoding='utf-8') as file:
                file.write(content)
            print(url)
            break
        current_date -= timedelta(days=1)


if __name__ == "__main__":
    main()
    
