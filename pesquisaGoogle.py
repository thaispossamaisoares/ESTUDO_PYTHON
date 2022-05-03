from tracemalloc import stop
from google import search

for resultado in search('"casa" youtube', stop=3):
    print (resultado)