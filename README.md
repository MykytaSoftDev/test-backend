## Array Task

The source code is in the file `test-backend-arrays.py`.
The ArrayHandler class was created, which contains array processing methods that needed to be integrated in accordance with the task.

1. The `filter_unique_records` method was created, in which the array is processed and returns a new array with unique values.

```py
def filter_unique_records(self):
    unique_dict = {item["id"]: item for item in self.array}
    unique_array = list(unique_dict.values())
    return unique_array
```

2. The `sort_array_by_id` method used for sorting array by id.

```py
def sort_array_by_id(self):
    sorted_array = sorted(self.array, key=lambda x: x["id"])
    return sorted_array
```

3. The `filter_by_id` method used to search for an element by id.

```py
def filter_by_id(self, id):
    filtered_array = [item for item in self.array if item["id"] == id]
    return filtered_array
```

4. The `convert_to_dictionary` method converts the data into a dictionary based on the selected key and value.

```py
def convert_to_dictionary(self, key, value):
    new_dict = {item[key]: item[value] for item in self.array}
    return new_dict
```

## SQL Tasks

-- TASK 1 --

This query selects all department_ids where the respondent's gender is male (gender = true), groups the records by department_id,and then uses the HAVING clause to select only those departments where the minimum score of all men in the department is strictly above 5.

```sql
SELECT department_id
FROM evaluations
WHERE gender = true
GROUP BY department_id
HAVING MIN(value) > 5;
```

-- TASK 2 --

The first thing that came to my mind was the integration of the specialized Elasticsearch engine, it has powerful search and processing capabilities for text data.
Later I came up with another idea: you can use hashing. To do this, you can put an index on a special column with hashed bio.

1. Create a new field bio_hash, which will store the hash value of the bio field.

```sql
ALTER TABLE evaluations
ADD COLUMN bio_hash VARCHAR(64);
```

2. Calculate hash values for each entry in the table

```sql
UPDATE evaluations
SET bio_hash = SHA2(bio, 256);
```

3. Create an index on the bio_hash field

```sql
CREATE INDEX idx_bio_hash ON evaluations (bio_hash);
```

This will significantly speed up the search and make it more efficient through the use of an index.

Then we can search the biography like this:

```sql
SELECT *
FROM evaluations
WHERE bio_hash = SHA2('bio_description', 256);
```

## Architecture Task

I made a Python class equivalent to what was specified in the assignment in PHP code, since you know that I have no experience with PHP, and the condition also indicates that the solution can be provided in Python. The source code is in the file `test-backend-architecture.py`

-- TASK 1 --

1. The `SomeObjectsHandler` class now stores a dictionary of handlers, where the keys are the object names and the values are the corresponding handlers.

```py
def __init__(self):
    self.handlers = {}
```

2. The `register_handler` method adds a handler for a specific object name to the handlers dictionary.

```py
def register_handler(self, object_name, handler):
    self.handlers[object_name] = handler
```

3. The `handle_objects` method checks for the presence of a handler for each object and adds it to the list of handlers if it exists.

```py
def handle_objects(self, objects):
    handlers = []
    for obj in objects:
        object_name = obj.get_object_name()
        if object_name in self.handlers:
            handlers.append(self.handlers[object_name])
    return handlers
```

This way, we can add new handlers for new object types without changing the code of the SomeObjectsHandler class, which is consistent with the OCP principle.

-- TASK 2 --

The main problem is that Http is now tied to the XMLHttpService very tightly. This means that if we want to use another service to send requests instead of XMLHttpService, we will have to change the Http class. This is not very good because we want our classes to be flexible and not depend on a specific implementation.

To solve this problem, we add an HttpServiceInterface that says we should have a request method to send HTTP requests. We will then implement this interface in the XMLHttpService class.

Now, when we create an Http class, we simply tell it to use any object that implements the HttpServiceInterface interface. This means that we can use any implementation of the request service without changing the Http class code. This makes our code more flexible and easier to change, and this approach also complies with the Dependency Inversion Principle (DIP) from the SOLID principles.

```py
class XMLHttpService:
    def request(self, url, method, options):
        # Implementing an HTTP request using XMLHttpService
        pass

class HttpServiceInterface:
    def request(self, url, method, options):
        pass

class Http:
    def __init__(self, http_service: HttpServiceInterface):
        self.service = http_service

    def get(self, url, options):
        self.service.request(url, 'GET', options)

    def post(self, url):
        self.service.request(url, 'POST')
```
