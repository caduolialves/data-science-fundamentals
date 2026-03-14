import json
import os
from playwright.sync_api import sync_playwright

"""

Web scraper para extrair repositórios em destaque do GitHub.
O scraper acessa a página de tendências do GitHub, extrai informações
sobre os repositórios em destaque, como nome, linguagem de programação,
número de estrelas e forks, e salva esses dados em um arquivo JSON.

Para rodar este código, certifique-se de ter o Playwright instalado e configurado corretamente.
Certifique-se também de ter o navegador Chrome instalado, que é necessário para o Playwright funcionar.

Comando para instalar o Playwright:
    
    pip install playwright


"""

BASE_URL = "https://github.com/trending?since=monthly"

def run(playwright):

    # Definindo o navegador
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser context
    context = browser.new_context(
        user_agent="your-custom-user-agent",
        viewport={"width": 800, "height": 600},
        bypass_csp=True
    )

    page = context.new_page()
    page.goto(BASE_URL)

    # Extraindo os dados
    repo_trendings = page.locator("article.Box-row")

    data = []

    for i in range(repo_trendings.count()):
        repo = repo_trendings.nth(i)

        name = repo.locator("h2 a")
        language = repo.locator('span[itemprop="programmingLanguage"]')
        stars = repo.locator('a[href$="/stargazers"]')
        forks = repo.locator('a[href$="/forks"]')

        repository = {
            "name": name.inner_text().strip(),
            "language": language.inner_text().strip() if language.count() > 0 else None,
            "stars_total": stars.inner_text().strip() if stars.count() > 0 else None,
            "forks": forks.inner_text().strip() if forks.count() > 0 else None,
            "url": f"https://github.com{name.get_attribute('href')}"
        }

        data.append(repository)

    print(data)

    os.makedirs("data", exist_ok=True)

    with open("data/trending_repositories.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    # Fechando o navegador
    browser.close()

with sync_playwright() as playwright:
    run(playwright)            
