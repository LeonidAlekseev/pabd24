import time
from multiprocessing import Pool
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
ENDPOINT = 'http://31.129.100.203:8000/predict'
HEADERS = {"Authorization": f"Bearer {config['APP_TOKEN']}"}


# Run for save test logs
# python test/test_parallel.py > log/io_bounded_prod.txt
# python test/test_parallel.py > log/cpu_bounded_prod.txt
# python test/test_parallel.py > log/cpu_multithread_prod.txt


def do_request(area: int) -> str:
    data = {
        'area': area,
        'mode': 'test',
        # 'tname': 'io_bounded',
        # 'tname': 'cpu_bounded',
        'tname': 'cpu_multithread',
        'tn': 1_000_000,
        # 'tn': 300_000_000,
    }
    t0 = time.time()
    resp = requests.post(
        ENDPOINT,
        json=data,
        headers=HEADERS
    ).text
    t = time.time() - t0
    return f'Waited {t:0.2f} sec ' + resp 


def test_10():
    with Pool(10) as p:
        print(*p.map(do_request, range(10, 110, 10)))
    

if __name__ == '__main__':
    test_10()
