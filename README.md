# Django with MongoDB
[video](https://www.youtube.com/watch?v=mUPQii90K5A&t=2442s&ab_channel=FaradayAcademy)
Spaced repetition learning back-end with MongoDB.
You can see the DRF Postgres version of this [here](https://github.com/faraday-academy/spaced-repetition-django) and a GraphQL Postgres version [here](https://github.com/gwenf/django-graphql-srl).

## Endpoints

`/cards`
`/cards/:id`

`/decks`
`/decks/:id`

`decks/:id/cards`


## installation

```shell
python3 -m venv venv
source venv/bin/activate
poetry install
```

```shell
mongosh -u "root" -p "123456" --authenticationDatabase "admin"
use admin
db.createCollection("spacedlearning")
show collections
db.spacedlearning.insert({name: "novie", age: 23})
```