# Palenca API test project

### Requirements

- Docker 20.10.6 or higher
- Docker Compose or higher


### Run project


```shell
docker-compose up --build -d
```

It will listen on `http://localhost:8080`

### CURL Request

To get project name
```shell
curl --location --request GET 'http://localhost:8080' \
--data-raw ''
```

To authenticate
```shell
curl --location --request POST 'http://localhost:8080/uber/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "pierre@palenca.com",
    "password": "MyPwdChingon123"
}'
```

To get profile
```shell
curl --location --request GET 'http://localhost:8080/uber/profile/cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5' \
--data-raw ''
```
