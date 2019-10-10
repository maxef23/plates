# plates

Запись и чтение из базы госномеров

 
### Чтение:
- /get. В ответ приходит json со всеми строками таблицы Numberplate

##### Пример:
```
/get

[
  {
    "CamID": 1, 
    "Licplates": "H272YM161", 
    "Timestamp": "0", 
    "id": 1
  }, 
  {
    "CamID": 1, 
    "Licplates": "C008BC161", 
    "Timestamp": "0", 
    "id": 2
  }, 
  {
    "CamID": 1, 
    "Licplates": "C008BC161", 
    "Timestamp": "0", 
    "id": 3
  }
]
```


- /get/<int:id>. В ответ приходит json cо строками у которых ID больше или равен id

##### Пример:
```
/get/2

[
  {
    "CamID": 1, 
    "Licplates": "C008BC161", 
    "Timestamp": "0", 
    "id": 2
  }, 
  {
    "CamID": 1, 
    "Licplates": "C008BC161", 
    "Timestamp": "0", 
    "id": 3
  }
]
```

### Запись:
- /send Принимает три аргумента CamID, Timestamp, Licplates


##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "http://127.0.0.1:5000/send", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("CamID=3&Timestamp=0&Licplates=c777cc198");
```