import requests
import pandas as pd
from pprint import pprint
import time


def _make_spotify_job_request(initial_page=1, per_page=50):
    URL = 'https://www.spotifyjobs.com/wp-admin/admin-ajax.php'
    DATASCIENCE = 343
    payload = {'action': 'get_jobs', 'pageNr': initial_page,
               'perPage': per_page, 'category': DATASCIENCE}
    response = requests.post(URL, data=payload)
    if response.status_code != 200:
        raise EOFError(f'Returned with response code {response.status_code}')
    return response.json()


def _download_spotify_jobs_single_page(initial_page=1, per_page=50):
    result = _make_spotify_job_request(initial_page, per_page)
    if 'data' not in result:
        raise KeyError(f'data not a key in returned result: {pprint(result)}')
    if 'items' not in result['data']:
        raise KeyError(f'items not a key in returned result[data]: {pprint(result)}')
    return result['data']['items']


def download_spotify_jobs():
    """Call to download all spotify jobs.

    Returns nested objects from API call.
    """
    results = []
    current_page, per_page = 1, 50
    while True:
        print(f'current page is {current_page}')
        new_jobs = _download_spotify_jobs_single_page(current_page, per_page)
        results.extend(new_jobs)
        if len(new_jobs) < per_page:
            return results
        time.sleep(1)
        current_page += 1


def simplify_job(job_object):
    """Flattens information for a single job from spotify.

    Takes the original job object, and returns a dictionary with the following keys:
    title: string
    url: string
    locations: list of strings
    categories: list of strings
    is_ny: boolean
    """
    flat_job = {
        'title': job_object.get('title'),
        'url': job_object.get('url'),
        'locations': [loc['name'] for loc in job_object.get('locations', [])],
        'categories': [cat['name'] for cat in job_object.get('categories', [])]
    }
    flat_job['is_ny'] = ('New York' in flat_job['locations'])
    return flat_job

if __name__ == '__main__':
    simple_jobs = [simplify_job(job) for job in download_spotify_jobs()]
    jobs_frame = pd.DataFrame(simple_jobs)
    print(jobs_frame.head())

    jobs_frame.to_csv('spotify.csv', index=False)
