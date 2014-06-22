Statuses
================

Statuses are a list of statuses available for an event.

Fields
---------
- name : Name of status
- description : Description of status
- image : Name of image that represents the status
- resource_uri : URI that represents the status
- slug : Internal and unique id of the status
- severity : Notes severity of status (unused)


Sample Output
----------
```
URL: http://localhost:8000/api/v1/statuses/?format=json&name=Up
{'meta': {'limit': 20,
          'next': None,
          'offset': 0,
          'previous': None,
          'total_count': 1},
 'objects': [{'description': 'The service is up',
              'image': 'tick-circle',
              'name': 'Up',
              'resource_uri': '/api/v1/statuses/2/',
              'severity': 10,
              'slug': 'up'}]}
```

