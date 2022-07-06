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

### If you want to try the API, you can use the following URL:
```method: GET host:5000/api/statements```

### Dokcer image creation.
Go to root folder and run the following commands
  - ```docker image build -t transactions-stori-report .```
  - ```docker run -p 5000:5000 -d transactions-stori-report```


## Author
- [X] [@alexiszamudio](https://github.com/AlexisZamudioOrtega08)