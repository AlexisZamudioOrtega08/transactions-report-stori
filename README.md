# Welcome to transactions-report-stori

This is an API for sending a report of transactions to a mail address.

### The API contains one endpoint:
```method: POST host:5000/api/statements```

The above endpoint requieres a query parameter to be parsed.

| Query Parameters| Type        | Description                                     |
| :-------------  | :---------- | :---------------------------------------------- |
| `email`         | `str`       | **Required**. Email of user to receive the mail |


#### Requests example:

  - ```host:5000/api/statements?email=example@email.com```


## Author
- [X] [@alexiszamudio](https://github.com/AlexisZamudioOrtega08)