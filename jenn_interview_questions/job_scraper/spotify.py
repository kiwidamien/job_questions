import requests
import pandas as pd
from pprint import pprint
import time

def download_spotify_jobs_single_page(initial_page=1, per_page=50):
    URL = 'https://www.spotifyjobs.com/wp-admin/admin-ajax.php'
    payload = {'action': 'get_jobs', 'pageNr': initial_page,
               'perPage': per_page, 'category':343}
    response = requests.post(URL, data=payload)
    if response.status_code != 200:
        raise EOFError(f'Returned with response code {response.status_code}')
    return response.json()

def download_spotify_jobs():
    results = []
    current_page, per_page = 1, 50
    while True:
        new_responses = download_spotify_jobs_single_page(current_page, per_page)
        if 'data' in new_responses and 'items' in new_responses['data']:
            new_jobs = new_responses['data']['items']
            results.extend(new_jobs)
            if len(new_jobs) < per_page:
                return results
            time.sleep(1)
            current_page += 1
            print(f'current page is {current_page}')
        else:
            print('keys not in response, exiting')
            return []

def simplify_job(job_object):
    """Flattens information for a single job from spotify (original object nested)"""
    return {
        'title': job_object.get('title'),
        'url': job_object.get('url'),
        'locations': [loc['name'] for loc in job_object.get('locations', [])],
        'categories': [cat['name'] for cat in job_object.get('categories', [])]
    }


if __name__ == '__main__':
    simple_jobs = [simplify_job(job) for job in download_spotify_jobs()]
    jobs_frame = pd.DataFrame(simple_jobs)
    print(jobs_frame.head())

    jobs_frame.to_csv('spotify.csv', index=False)
