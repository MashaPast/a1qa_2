## A1QA course №2
### Task 6
### Running tests on Linux


* setting environment variable for path to config before running tests
```bash 
export CONFIG='./t6_rest_api_tasks/resources/configurations.json'
```

* running all tests in task 6
```bash 
python3 -m pytest -v -s t6_rest_api_tasks/tests/test_rest_api.py
```