## A1QA course №2
### Task 9
* создать образ 
```bash
docker build -t task_html .
```
* запустить контейнер
```bash
docker run -d -p 5005:8080 --rm task_html
```
* зайти в контейнер
```bash
docker exec -it clever_pascal sh
/usr/local/tomcat/webapps/task # ls
```
Output:

Dockerfile    README.md     css           index.html    index.js      js            terminal.png
