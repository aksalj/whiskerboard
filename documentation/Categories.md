Categories
================

Categories organize Services into a group.

Fields
---------
- name : Name of category
- description : Description of category
- resource_uri : URI that represents the category
- slug : Internal and unique id of the category

Sample Output
----------
```
URL: http://localhost:8000/api/v1/categories/?format=json&name=category1
{'meta': {'limit': 20,
          'next': None,
          'offset': 0,
          'previous': None,
          'total_count': 1},
 'objects': [{'description': 'category1',
              'name': 'category1',
              'resource_uri': '/api/v1/categories/1/',
              'slug': 'category1'}]}

```

