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

  - Download or create the docker image for the app:
    * Docker image is available on: ```https://transactions-report-stori-api-assets.sfo3.digitaloceanspaces.com/docker-images/transactions-stori-report-first.tar```

    * In case you have instaññed docker you can build the image by yourself with the following commands:
      * ```docker image build -t transactions-stori-report-first .``` -> This will create an image of the application.
      * ```docker run -p 5001:5001 -d transactions-stori-report-first``` -> This will run the image and expose port 5001 to work locally.

### If you want to try the demonstration of the application, you can use the following URL:
```method: POST http://first.seitech.org/statements?email=your_mail@example.com```

### Or in case you want to test it locally, you can use the following URL:
```method: POST http://localhost:5001:statements?email=your_mail@example.com```

## Author
- [X] [@alexiszamudio](https://github.com/AlexisZamudioOrtega08)
