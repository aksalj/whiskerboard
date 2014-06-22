Events
================

Events represent all events for a specific service.

Fields
---------
- message : Message in regard to this event
- resource_uri : URI that represents the event
- informational : Notes if this is an informational event
- start : date and time the event was first registered
- service : URI of service this event relates to
- status : status of event (relates to Status)

Sample Output
----------
```
URL: http://localhost:8000/api/v1/events/?format=json&__slug=service1
{'meta': {'limit': 20,
          'next': '/api/v1/events/?offset=20&limit=20&__slug=service1&format=json',
          'offset': 0,
          'previous': None,
          'total_count': 295},
 'objects': [{'informational': False,
              'message': 'All services operational.',
              'resource_uri': '/api/v1/events/295/',
              'service': '/api/v1/services/1/',
              'start': '2012-11-27T17:36:02.163648',
              'status': {'description': 'The service is up',
                         'image': 'tick-circle',
                         'name': 'Up',
                         'resource_uri': '/api/v1/statuses/2/',
                         'severity': 10,
                         'slug': 'up'}},
```

