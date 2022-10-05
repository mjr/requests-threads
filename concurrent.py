import requests

from time import perf_counter
from threading import Thread


def task(id):
    print(f'Starting the task {id}...')
    r = requests.get('https://api.myip.com')
    print(r.status_code)
    print(f'The task {id} completed')


start_time = perf_counter()

threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')