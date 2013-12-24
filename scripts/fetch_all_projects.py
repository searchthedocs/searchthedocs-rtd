import json
import requests
import grequests

import logging

logging.basicConfig(level=logging.DEBUG)


def fetch_all_projects():
    """
    Fetch the names of all projects using the v1 project API.
    Grossly inefficient - we need an API that can return a
    list of all project names quickly.
    """

    url_format = (
        'http://readthedocs.org/api/v1/project/?format=json'
        '&limit=100&offset={0}')
    project_names = []

    # Make initial request to see how many total requests we need to set up.
    resp = requests.get(url_format.format(0))
    project_results = resp.json()

    project_names.extend(parse_project_objects(project_results['objects']))

    total_count = project_results['meta']['total_count']
    # Determine the largest offset needed to fetch all projects
    max_offset = (total_count/100) * 100
    print max_offset

    urls = [url_format.format(offset)
            for offset in xrange(100, max_offset + 1, 100)]

    rs = (grequests.get(u) for u in urls)
    for resp in grequests.imap(rs, size=5):
        project_results = resp.json()
        project_names.extend(parse_project_objects(project_results['objects']))

    with open('project_list.json', 'w') as f:
        f.write(json.dumps({
            'project_names': project_names,
        }))


def parse_project_objects(project_obj_seq):
    return [p['name'] for p in project_obj_seq]

if __name__ == '__main__':
    fetch_all_projects()

