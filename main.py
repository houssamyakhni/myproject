import psycopg2

connection=psycopg2.connect(
    host = "localhost",
    port="5432",
    database="master",
    username="postgres",
    password="HFY2002&HFY"
)