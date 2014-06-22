Services
================

Services represent the main items that are checked.

Fields
---------
- name : Name of service
- description : Description of service
- resource_uri : URI that represents the service
- slug : Internal and unique id of service
- current-event : The current event of the service

Sample Output
----------
```
URL: http://localhost:8000/api/v1/services/?format=json&name=service1
{'meta': {'limit': 20,
          'next': None,
          'offset': 0,
          'previous': None,
          'total_count': 1},
 'objects': [{'category': {'description': 'category1',
                           'name': 'category1',
                           'resource_uri': '/api/v1/categories/1/',
                           'slug': 'category1'},
              'current-event': {'informational': False,
                                'message': 'All services operational.',
                                'service': 'service1',
                                'start': '2012-11-27T17:36:02.163648',
                                'status': 'Up'},
              'description': 'service1',
              'name': 'service1',
              'resource_uri': '/api/v1/services/1/',
              'slug': 'service1'}]}
```



