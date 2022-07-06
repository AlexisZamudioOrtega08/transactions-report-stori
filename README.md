# Welcome to transactions-report-stori

This is an API for sending a report of transactions to a mail address.

### The API contains one endpoint:
```method: POST host:5000/api/statements```

The above endpoint requieres a query parameter to be parsed.

| Query Parameters| Type        | Description                                     |
| :-------------  | :---------- | :---------------------------------------------- |
| `email`         | `str`       | **Required**. Email of user to receive the mail |


#### Requests example:

  - ```host:5001/api/statements?email=example@email.com```

### In oder to run the app you need to follow the next steps:
  - Create a `.env` file in the root directory of the project, you can refer `.env.example` for this.
  - In order to complete the next steps you must need to have installed docker in your local machine.

    * Once docker is installed you can run the following command:
      ```
      docker compose up
      ```

### If you want to try the demonstration of the application, you can use the following URL:
```method: POST http://first.seitech.org/statements?email=your_mail@example.com```

## Author
- [X] [@alexiszamudio](https://github.com/AlexisZamudioOrtega08)
