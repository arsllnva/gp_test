import requests
import psycopg2

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

posts = response.json()

conn = psycopg2.connect(
    host="localhost",
    port=5434,
    database="db_gp",
    user="postgres",
    password="Hello130905"
)

cursor = conn.cursor()

cursor.execute("truncate table stg.posts")

for post in posts:

    cursor.execute("""
                   insert into stg.posts (user_id, id, title, body)
                   values (%s, %s, %s, %s)
    """, (
        post["userId"],
        post["id"],
        post["title"],
        post["body"]
    ))

conn.commit()

cursor.close()
conn.close()

print("Данные успешно загружены в stg.posts")