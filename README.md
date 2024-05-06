# test assignment

[link](/docs/ТЗ на вакансию SDET 2024.pdf)

## How to run

1. make a local copy of the git repository
```
git clone https://github.com/uxmlen/simbirsoft-assignment.git
```

2. prepare the environments to run the tests
```bash
docker composer up -d
```

3. go inside the project 
```bash
cd simbirsoft-test
```

4. install all dependencies using poetry (requirement.txt is in the project for backwards compatibility)
```bash
poetry install
```

5. run the tests and generate reports for allure
```
pytest -sv --alluredir=results ./tests/
```

6. let's look at the results in allure
```
allure serve results
```

## Stack

- Selenium Grid/Webdriver
- Allure
- Pytest
- Poetry
- Docker Compose
