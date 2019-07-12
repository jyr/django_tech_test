# Urbvan Docker Compose

|Service| Service Name | Host | Port |
|---|---|---|---|
| Web | web | urbvan-dev.com | 80 |
| Proxy | app | api.urbvan-dev.com | 8000 |

## Setting everything up

1. Add the following entries to your `/etc/hosts` file.

  ```
  # Services

  127.0.0.1  urbvan-dev.com
  127.0.0.1  api.urbvan-dev.com
```
2. Install docker https://www.docker.com/get-docker
3. Install docker-compose https://docs.docker.com/compose/install/
4. Start the **docker-compose** service.

## Basic Usage

- Build all services `docker-compose up --build`

- Start all services `docker-compose up`

- Stop all services `docker-compose stop`

### Development and Test Environments preparation

**NOTES:**

* By default uses development Environment.
* Recommendation: set Environment explicit like this `--settings=urbvan.settings.development` or `--settings=urbvan.settings.test`

```
$docker-compose exec app /bin/sh -c -l "./manage.py migrate"
$docker-compose exec app /bin/sh -c -l "./manage.py showmigrations"
$docker-compose exec app /bin/sh -c -l "./manage.py createsuperuser"
$docker-compose exec app /bin/sh -c -l "./manage.py add_group 'API Manager'"
$docker-compose exec app /bin/sh -c -l "./manage.py add_group 'Developer'"
$docker-compose exec app /bin/sh -c -l "./manage.py add_group 'Client'"
$docker-compose exec app /bin/sh -c -l "./manage.py add_user my_user_name my_own_password"
```


### Django commands on Docker
```
$docker-compose exec app /bin/sh -c -l "./manage.py test --settings=urbvan.settings.test"
$docker-compose exec app /bin/sh -c -l "./manage.py shell"
```


## Django commands

```
$./manage.py runserver --settings=urbvan.settings.development
```

### Example: Django migrations
```
$./manage.py makemigrations --settings=urbvan.settings.development
$./manage.py migrate --settings=urbvan.settings.development
$./manage.py migrate --database=read --settings=urbvan.settings.development
$./manage.py migrate --database=write --settings=urbvan.settings.development
```

### Example: Django console
```
$./manage.py shell
$./manage.py shell --settings=urbvan.settings.test
```

### Example: Django tests
```
$./manage.py migrate --settings=urbvan.settings.test
$./manage.py test --settings=urbvan.settings.test
$./manage.py test --settings=urbvan.settings.test apps.stations.test
$./manage.py test --settings=urbvan.settings.test apps.stations.tests.tests_endpoints
$./manage.py test --settings=urbvan.settings.test apps.stations.tests.tests_endpoints.StationEndpointTest
$./manage.py test --settings=urbvan.settings.test apps.stations.tests.tests_endpoints.StationEndpointTest.test_post_a_station

```

## Author

Jyr Gaxiola - jyr.gaxiola@gmail.com
