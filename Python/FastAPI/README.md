
# Project : FastAPI Salary Calculator

This project demonstrates the creation of a basic API using FastAPI. The API performs simple computations based on salary, bonus, and taxes and returns the results in JSON format. 

## Features

The API has the following endpoints:

1. **GET Request**: 
    - This route handles a simple GET request and returns a welcome message.

2. **POST Request to Multiply a Number**:
    - This route takes a number in the request body and returns that number multiplied by 2.

3. **POST Request for Salary Calculation**:
    - This route expects a JSON body containing the fields `salary`, `bonus`, and `taxes`. It will compute the result as:
      ```
      salary + bonus - taxes
      ```
    - If the fields are missing or invalid, the API returns an error message.

### Expected Input for Salary Calculation

```json
{
    "salary": 2500,
    "bonus": 200,
    "taxes": 400
}
```

### Output:

- **Valid Input**: 
  ```json
  {
      "result": 2300
  }
  ```

- **Invalid Input (non-numeric value)**: 
  ```json
  {
      "error": "expected numbers, got strings."
  }
  ```

- **Missing Fields**:
  ```json
  {
      "error": "3 fields expected (salary, bonus, taxes). You forgot: bonus."
  }
  ```

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

You can install the necessary dependencies by running:

```bash
pip install fastapi uvicorn
```

## API Endpoints

1. **GET /**  
   - Returns a welcome message.
   
   Response:
   ```json
   {
       "message": "Welcome to the FastAPI Salary Calculator!"
   }
   ```

2. **POST /multiply-by-two**  
   - Accepts a number and returns it multiplied by 2.
   
   Request (JSON):
   ```json
   {
       "number": 10
   }
   ```
   Response:
   ```json
   {
       "result": 20
   }
   ```

3. **POST /calculate-salary**  
   - Accepts a JSON object with `salary`, `bonus`, and `taxes` and returns the computed result.

   Request (JSON):
   ```json
   {
       "salary": 2500,
       "bonus": 200,
       "taxes": 400
   }
   ```

   Response (valid input):
   ```json
   {
       "result": 2300
   }
   ```

   Response (non-numeric value):
   ```json
   {
       "error": "expected numbers, got strings."
   }
   ```

   Response (missing field):
   ```json
   {
       "error": "3 fields expected (salary, bonus, taxes). You forgot: bonus."
   }
   ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

Once the server is running, you can visit the following URLs:

- **GET Request**: `http://localhost:8000/`
- **POST Request**: `http://localhost:8000/multiply-by-two`
- **POST Salary Calculation**: `http://localhost:8000/calculate-salary`

## Testing the API

To test the API, you can use a browser for GET requests or tools like **curl** or **Postman** for POST requests.

### Using cURL (example):

- For the **GET** request:
  ```bash
  curl http://localhost:8000/
  ```

- For the **POST /multiply-by-two** request:
  ```bash
  curl -X 'POST' \
    'http://localhost:8000/multiply-by-two' \
    -H 'Content-Type: application/json' \
    -d '{"number": 10}'
  ```

- For the **POST /calculate-salary** request:
  ```bash
  curl -X 'POST' \
    'http://localhost:8000/calculate-salary' \
    -H 'Content-Type: application/json' \
    -d '{"salary": 2500, "bonus": 200, "taxes": 400}'
  ```

## Next Steps

- Explore more advanced FastAPI features, such as database connections, authentication, and validation.
- Learn how to deploy this FastAPI app to production using services like Heroku, AWS, or Docker.
- Enhance the API by adding more complex business logic or endpoints.

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial by DataCamp](https://www.datacamp.com/community/tutorials/introduction-fastapi-python)
- [FastAPI - Deploying ML Models as API](https://fastapi.tiangolo.com/tutorial/deployment/)
- [FastAPI Python Database Example](https://fastapi.tiangolo.com/tutorial/sql-databases/)
```

This is the full README in Markdown language for your FastAPI project, ready to be used in your repository or documentation!
