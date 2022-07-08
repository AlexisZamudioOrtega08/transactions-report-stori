# Welcome to transactions-report-stori

This is an API for simulating a report of transactions.

### The API contains the following group of endpoints:
  - transactions
  - users
  - reports

### In transactions group there are two endpoints availables:
  ```method: POST host/api/v1/transactions```

   The above endpoint requires the following parameters.

  | Body  Parameters| Type        | Description                                         |
  | :-------------  | :---------- | :-------------------------------------------------- |
  | `user_id`       | `int`       | **Required**. Id of the user that made the txn.     |
  | `txn`           | `bool`      | **Required**. Type of txn (1 -> Credit, 0 -> Debit).|
  | `amount`        | `float`     | **Required**. Amount of txn.                        |

  **Body example**
  
    {
        "user_id": 3,
        "txn": 0,
        "amount": 150.78
    }

  ```method: GET host/api/v1/transactions```    

| Query Parameters| Type        | Description                                         |
| :-------------  | :---------- | :-------------------------------------------------- |
| `user_id`       | `int`       | **Not Required**. Id of user, to obtain txns.       |

##### **Note:** If user_id is not provided all txns will be retreived

### In users group there are two endpoints availables:

```method: POST host/api/v1/users```

   The above endpoint requires the following parameters.

  | Body  Parameters| Type        | Description                          |
  | :-------------  | :---------- | :----------------------------------- |
  | `email`         | `str`       | **Required**. Email of the user.     |
  | `first_name`    | `str`       | **Required**. First name os user.    |
  | `last_name`     | `str`       | **Required**. Last name of user.     |

**Body example**
 
    {
      "email": "your_mail@example.com",
      "first_name": "your_name",
      "last_name": "your_last_name"
    }

```method: GET host/api/v1/users```    

| Query Parameters| Type        | Description                     |
| :-------------  | :---------- | :------------------------------ |
| `id`            | `int`       | **Not Required**. Id of user.   |

##### **Note:** If id is not provided all users will be retreived.

### In reports group there is only a single endpoint available:
```method: POST host/api/v1/reports```

| Query Parameters| Type        | Description                     |
| :-------------  | :---------- | :------------------------------ |
| `user_id`       | `int`       | **Required**. Id of user.       |

##### **Note:**  Email and txns information is retreived with thie id.

#### By consuming the above endpoint you will receive a mail like this:
![alt text](https://transactions-report-stori-api-assets.sfo3.digitaloceanspaces.com/img/email.png)


### In oder to run the app you need to follow the next steps:
  - Create a `.env` file in the root directory of the project, you can refer `.env.example` for this.
  - In order to complete the next steps you must need to have installed docker in your local machine.


    * Once docker is installed you can run the following command:
      ```
      docker-compose up -d
      ```



### In case you want to try the API as service, please use the following url as your host:
    http://test.seitech.org/api/v1
    
    e.g
    
      - METHOD GET https://seitech.org/api/v1/users

## Author
- [X] [@alexiszamudio](https://github.com/AlexisZamudioOrtega08)
