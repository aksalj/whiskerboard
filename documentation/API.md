Welcome to Wiki
================

This wiki will document the REST-API for Whiskerboard.


# Endpoints

Endpoints show all api endpoints and their corresponding schema. Schemas display available options and data types for the endpoint.

### Fields

- `list_endpoint` : URI endpoint of endpoint
- `schema` : URI of schema for endpoint

### Sample

```shell
$ curl http://localhost:8000/api/v1/?format=json
```

```json
{
    "categories": {
        "list_endpoint": "/api/v1/categories/",
        "schema": "/api/v1/categories/schema/"
    },
    "events": {
        "list_endpoint": "/api/v1/events/",
        "schema": "/api/v1/events/schema/"
    },
    "services": {
        "list_endpoint": "/api/v1/services/",
        "schema": "/api/v1/services/schema/"
    },
    "statuses": {
        "list_endpoint": "/api/v1/statuses/",
        "schema": "/api/v1/statuses/schema/"
    }
}
```

```shell
$ curl http://localhost:8000/api/v1/categories/schema/?format=json
```

```json
{
    "allowed_detail_http_methods": ["get", "post", "put", "delete", "patch"],
    "allowed_list_http_methods": ["get", "post", "put", "delete", "patch"],
    "default_format": "application/json",
    "default_limit": 20,
    "fields": {
        "description": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: 'Hello World'",
            "nullable": false,
            "readonly": false,
            "type": "string",
            "unique": false
        },
        "name": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: 'Hello World'",
            "nullable": false,
            "readonly": false,
            "type": "string",
            "unique": false
        },
        "resource_uri": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: 'Hello World'",
            "nullable": false,
            "readonly": true,
            "type": "string",
            "unique": false
        },
        "slug": {
            "blank": false,
            "default": "No default provided.",
            "help_text": "Unicode string data. Ex: 'Hello World'",
            "nullable": false,
            "readonly": false,
            "type": "string",
            "unique": false
        }
    },
    "filtering": {
        "name": 1
    }
}
```

# Services

Services represent the main items that are checked.

### Fields

- `name` : Name of service
- `description` : Description of service
- `resource_uri` : URI that represents the service
- `slug` : Internal and unique id of service
- `current-event` : The current event of the service

### Sample

```shell
$ curl http://localhost:8000/api/v1/services/?format=json&name=service1
```

```json
{
    "meta": {
        "limit": 20,
        "next": null,
        "offset": 0,
        "previous": null,
        "total_count": 1
    },
    "objects": [
        {
            "category": {
                "description": "category1",
                "name": "category1",
                "resource_uri": "/api/v1/categories/1/",
                "slug": "category1"
            },
            "current-event": {
                "informational": false,
                "message": "All services operational.",
                "service": "service1",
                "start": "2012-11-27T17:36:02.163648",
                "status": "Up"
            },
            "description": "service1",
            "name": "service1",
            "resource_uri": "/api/v1/services/1/",
            "slug": "service1"
        }
    ]
}
```

# Categories

Categories organize `Services` into groups.

### Fields

- `name` : Name of category
- `description` : Description of category
- `resource_uri` : URI that represents the category
- `slug` : Internal and unique id of the category

### Sample

```shell
$ curl http://localhost:8000/api/v1/categories/?format=json&name=category1
```

```json
{
    "meta": {
        "limit": 20,
        "next": null,
        "offset": 0,
        "previous": null,
        "total_count": 1
    },
    "objects": [
        {
            "description": "category1",
            "name": "category1",
            "resource_uri": "/api/v1/categories/1/",
            "slug": "category1"
        }
    ]
}
```


# Events

Events represent all events for a specific service.

### Fields

- `message` : Message in regard to this event
- `resource_uri` : URI that represents the event
- `informational` : Notes if this is an informational event
- `start` : date and time the event was first registered
- `service` : URI of service this event relates to
- `status` : status of event (relates to Status)

### Sample

```shell
$ curl http://localhost:8000/api/v1/events/?format=json&__slug=service1
```

```json
{
    "meta": {
        "limit": 20,
        "next": "/api/v1/events/?offset=20&limit=20&__slug=service1&format=json",
        "offset": 0,
        "previous": null,
        "total_count": 295
    },
    "objects": [
        {
            "informational": false,
            "message": "All services operational.",
            "resource_uri": "/api/v1/events/295/",
            "service": "/api/v1/services/1/",
            "start": "2012-11-27T17:36:02.163648",
            "status": {
                "description": "The service is up",
                "image": "tick-circle",
                "name": "Up",
                "resource_uri": "/api/v1/statuses/2/",
                "severity": 10,
                "slug": "up"
            }
        }
    ]
}
```



# Statuses

Statuses are a list of statuses available for an event.

### Fields

- `name` : Name of status
- `description` : Description of status
- `image` : Name of image that represents the status
- `resource_uri` : URI that represents the status
- `slug` : Internal and unique id of the status
- `severity` : Notes severity of status (unused)


### Sample

```shell
$ curl http://localhost:8000/api/v1/statuses/?format=json&name=Up
```

```json
{
    "meta": {
        "limit": 20,
        "next": null,
        "offset": 0,
        "previous": null,
        "total_count": 1
    },
    "objects": [
        {
            "description": "The service is up",
            "image": "tick-circle",
            "name": "Up",
            "resource_uri": "/api/v1/statuses/2/",
            "severity": 10,
            "slug": "up"
        }
    ]
}
```