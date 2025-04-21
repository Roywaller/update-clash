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
    for _ in range(7):  # 最多尝试 7 天
        url, content = get_content(current_date)
        if content:
            with open('clash.yaml', 'w', encoding='utf-8') as file:
                file.write(content)
            # 将获取的链接保存到 README.md
            with open('README.md', 'w', encoding='utf-8') as readme_file:
                readme_file.write("当前更新链接   " + url + "\n")
            break
        current_date -= timedelta(days=1)


if __name__ == "__main__":
    main()
    
