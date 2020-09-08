## A1QA course №2
### Task 5
### Running tests on Linux


* setting environment variable for path to config before running tests
```bash 
export CONFIG='./t5_userinyerface/resources/configurations.json'
```

* running task 5
```bash 
python3 -m pytest -v -s t5_userinyerface/tests/test_userinyerface.py  
```
