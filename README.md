# plates

#Синявино

## Тестовые сервер развернут по url http://3.124.81.206:5000

### Авторизация:

- /login. В запрос входит два параметра: логин и пароль. Сейчас создан тестовый пользователь с логином: admin и паролем: admin. В ответ приходит json с уникальным токеном пользователя. В последующем все запросы к базе должны иметь этот token в качестве аргумента.

```
{
  "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MTE2MjU1NCwiZXhwIjoxNTcxMTcyNTU0fQ.eyJpZCI6MTF9.lAU7dZkII6g3AY81cWDrFlDNCNc_IPQbCeIMR6UlJkozjC5VkOO0enrBW39sI6hEa5GYuatqFgZgaQN28JDnkg"
}
```
 
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
- /send. Принимает три аргумента CamID, Timestamp, Licplates


##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "http://127.0.0.1:5000/send?token=...", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("CamID=3&Timestamp=0&Licplates=c777cc198");
```

### Удаление:
- /delete. Принимает аргумент id сущности в таблице numberplate и удаляет его


### Статистика по номеру:
- /getstat_by_plate. Принимает аргумент plate госномера машины и возвращает все записи в базе с таким номером.

