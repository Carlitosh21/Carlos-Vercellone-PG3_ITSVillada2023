import requests
from tabulate import tabulate

base_url = "https://jsonplaceholder.typicode.com"
response = requests.get(f"{base_url}/posts")
posts = response.json()

headers = ["ID", "Título", "Body", "ID Usuario"]
rows = [[post["id"], post["title"], post["body"], post["userId"]] for post in posts]
print(tabulate(rows, headers=headers))


#Hago para que cuando se haga unmetodo get se cree un archivo html al cual si lo ejecutamos con la extension "Live Server" podremos ver los datos extraidos en una pagina web local

cards_html = ""
for post in posts:
    card_html = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{post["title"]}</h5>
            <p class="card-text">{post["body"]}</p>
            <p class="card-text">User ID: {post["userId"]}</p>
        </div>
    </div>
    """
    cards_html += card_html


with open("resultados.html", "w") as file:
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Resultados</title>
        <style>
            .card {{
                margin: 10px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .card-title {{
                font-size: 1.25rem;
                margin-bottom: 0.5rem;
            }}
            .card-text {{
                font-size: 1rem;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <h1>Resultados</h1>
        <div class="container">
            {cards_html}
        </div>
    </body>
    </html>
    """
    file.write(html)



