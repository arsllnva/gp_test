import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5434,
    database="db_gp",
    user="postgres",
    password="Hello130905"
)

cursor = conn.cursor()

cursor.execute("""
insert into dds.hub_user (user_id, record_source)

select distinct s.user_id, 'jsonplaceholder'
from stg.posts s
where not exists (
               select 1
               from dds.hub_user h
               where h.user_id = s.user_id
               )
""")


cursor.execute("""
insert into dds.hub_post (id, record_source)

select distinct s.id, 'jsonplaceholder'
from stg.posts s
where not exists (
               select 1
               from dds.hub_post h
               where h.id = s.id
               )
""")

cursor.execute("""
insert into dds.link_user_post (user_hk, post_hk, record_source)

select hu.user_hk, hp.post_hk, 'jsonplaceholder'
from stg.posts s
join dds.hub_user hu 
               on hu.user_id = s.user_id

join dds.hub_post hp
               on hp.id = s.id
where not exists(
               select 1
               from dds.link_user_post l
               where l.user_hk = hu.user_hk
               and l.post_hk = hp.post_hk
               )
""")


cursor.execute("""
insert into dds.sat_post_details (post_hk, title, body, record_source)

select hp.post_hk, s.title, s.body, 'jsonplaceholder'
from stg.posts s
join dds.hub_post hp
               on hp.id = s.id
""")

conn.commit()
cursor.close()
conn.close()
print("Данные успешно загружены в DDS")