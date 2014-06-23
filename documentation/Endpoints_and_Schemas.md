Endpoints and Schemas
================

Endpoints
--------

Endpoints show all api endpoints and their correspding schema.


Schemas
--------

Schemas display available options and data types for the endpoint


Fields
---------
- list_endpoint : URI endpoint of endpoint
- schema : URI of schema for endpoint

Sample Output (Endpoints)
----------
```
URL: http://localhost:8000/api/v1/?format=json
{'categories': {'list_endpoint': '/api/v1/categories/',
                'schema': '/api/v1/categories/schema/'},
 'events': {'list_endpoint': '/api/v1/events/',
            'schema': '/api/v1/events/schema/'},
 'services': {'list_endpoint': '/api/v1/services/',
              'schema': '/api/v1/services/schema/'},
 'statuses': {'list_endpoint': '/api/v1/statuses/',
              'schema': '/api/v1/statuses/schema/'}}

```

Sample Output (Schema)
----------
```
URL: http://localhost:8000/api/v1/categories/schema/?format=json
{'allowed_detail_http_methods': ['get', 'post', 'put', 'delete', 'patch'],
 'allowed_list_http_methods': ['get', 'post', 'put', 'delete', 'patch'],
 'default_format': 'application/json',
 'default_limit': 20,
 'fields': {'description': {'blank': False,
                            'default': 'No default provided.',
                            'help_text': 'Unicode string data. Ex: "Hello World"',
                            'nullable': False,
                            'readonly': False,
                            'type': 'string',
                            'unique': False},
            'name': {'blank': False,
                     'default': 'No default provided.',
                     'help_text': 'Unicode string data. Ex: "Hello World"',
                     'nullable': False,
                     'readonly': False,
                     'type': 'string',
                     'unique': False},
            'resource_uri': {'blank': False,
                             'default': 'No default provided.',
                             'help_text': 'Unicode string data. Ex: "Hello World"',
                             'nullable': False,
                             'readonly': True,
                             'type': 'string',
                             'unique': False},
            'slug': {'blank': False,
                     'default': 'No default provided.',
                     'help_text': 'Unicode string data. Ex: "Hello World"',
                     'nullable': False,
                     'readonly': False,
                     'type': 'string',
                     'unique': False}},
 'filtering': {'name': 1}}

```
