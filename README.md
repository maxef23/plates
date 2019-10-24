# Синявино

## Тестовые сервер развернут по url http://3.124.81.206:5000

### Авторизация:

- /login. В запрос входит два параметра: логин и пароль. Сейчас создан тестовый пользователь с логином: admin и паролем: admin. В ответ приходит json с уникальным токеном пользователя. В последующем все запросы к базе должны иметь этот token в качестве аргумента.

##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/login", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("login=admin&password=admin");
```

##### Ответ:

```
{
  "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MTE2MjU1NCwiZXhwIjoxNTcxMTcyNTU0fQ.eyJpZCI6MTF9.lAU7dZkII6g3AY81cWDrFlDNCNc_IPQbCeIMR6UlJkozjC5VkOO0enrBW39sI6hEa5GYuatqFgZgaQN28JDnkg"
}
```





 
### Чтение:
- /get. Если послать с помощью метода GET, то вернется json со всеми строками таблицы Numberplate. Если послать методом POST и прикрепить в тело запроса id номера, то в ответ придет json cо всеми строками у которых id больше или равен данному.


##### Пример 1:
```
var xhttp = new XMLHttpRequest();
xhttp.open("GET", "/get?token=", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send();
```

##### Ответ:
```
[
  {
    "CamID": 44554, 
    "Licplates": "E410YX177", 
    "Timestamp": "2019-10-21 11:07:28", 
    "id": 68
  }, 
  {
    "CamID": 44554, 
    "Licplates": "B883CY47", 
    "Timestamp": "2019-10-21 11:07:28", 
    "id": 69
  }, 
  {
    "CamID": 44554, 
    "Licplates": "B883CY47", 
    "Timestamp": "2019-10-21 11:07:28", 
    "id": 70
  }
]
```


##### Пример 2:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/get?token=", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send('id=100');
```

##### Ответ:
```
[
  {
    "CamID": 44554, 
    "Licplates": "B116PK47", 
    "Timestamp": "2019-10-21 11:07:28", 
    "id": 101
  }, 
  {
    "CamID": 44554, 
    "Licplates": "B116PK47", 
    "Timestamp": "2019-10-21 11:07:28", 
    "id": 102
  }, 
  {
    "CamID": 44554, 
    "Licplates": "O146AA47", 
    "Timestamp": "2019-10-21 11:07:28", 
    "id": 103
  }, 
  {
    "CamID": 44554, 
    "Licplates": "B559CM47", 
    "Timestamp": "2019-10-21 11:07:28", 
    "id": 104
  }
]
```





### Запись:
- /send. Принимает три аргумента CamID, Timestamp, Licplates. Во избежании дублирования номеров, невозможно послать два одинаковых номера подряд с одинаковым CamID.


##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/send?token=", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("CamID=3&Timestamp=0&Licplates=c777cc198");
```

### Удаление:
- /delete. Принимает аргумент id сущности в таблице Numberplate и удаляет его.


##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/delete?token=", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send('id=100');
```


### Статистика по номеру:
- /getstat_by_plate. Принимает аргумент plate госномера машины и возвращает все записи в базе с таким номером.



##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/getstat_by_plate?token=", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send('plate=b999aa198');
```


##### Ответ:
```
[
  {
    "CamID": 4, 
    "Licplates": "b999aa198", 
    "Timestamp": "0", 
    "id": 251
  }, 
  {
    "CamID": 4, 
    "Licplates": "b999aa198", 
    "Timestamp": "1571935890000", 
    "id": 253
  }
]
```


### Подсчет номеров в диапазон времени. Принимает два аргумента begin - начало диапазона и end - конец диапазона в секундах от начала эпохи. Возвращает json с номерами заехавшими/выехавшими в этом временном промежутке.

##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/count_plates?token=", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("begin=1571935880&end=1571935895");
```

##### Ответ:
```
[
  {
    "CamID": 4, 
    "Licplates": "b999aa198", 
    "Timestamp": "1571935890", 
    "id": 253
  }
]

```