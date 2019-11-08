# Синявино

## Тестовые сервер развернут по url http://3.124.81.206:5000

### Авторизация:

- /login. В запрос входит два параметра: логин и пароль. Сейчас создан тестовый пользователь с логином: admin и паролем: admin. В ответ приходит json с уникальным токеном пользователя. В последующем все запросы к базе должны иметь этот token в качестве аргумента.

##### Пример:
```
  axios({
    method: 'post',
    url: '/login',
    data : {
      login : "admin",
      password : "admin"
    },
    headers: {
        "Content-type" : "application/json",
        'Access-Control-Allow-Origin': '*'
        
      }
  });
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
  axios({
    method: 'get',
    url: '/get' + "?token=" + token,
    headers: {
        "Content-type" : "application/json",
        'Access-Control-Allow-Origin': '*'
        
      }
  });
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
  axios({
    method: 'post',
    url: '/get' + "?token=" + token,
    data : {
      id : 10
    },
    headers: {
        "Content-type" : "application/json",
        'Access-Control-Allow-Origin': '*'
        
      }
  });
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
  axios({
    method: 'post',
    url: '/delete' + "?token=" + token,
    data : {
      id : 5
    },
    headers: {
        "Content-type" : "application/json",
        'Access-Control-Allow-Origin': '*'
        
      }
  });
```


### Статистика по номеру:
- /getstat_by_plate. Принимает аргумент plate госномера машины и возвращает все записи в базе с таким номером.



##### Пример:
```
  axios({
    method: 'post',
    url: '/getstat_by_plate' + "?token=" + token,
    data : {
      plate : "c777cc198"
    },
    headers: {
        "Content-type" : "application/json",
        'Access-Control-Allow-Origin': '*'
        
      }
  });
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


### Подсчет номеров в диапазон времени. 

- /count_plates. Принимает два аргумента begin - начало диапазона и end - конец диапазона в секундах от начала эпохи. Возвращает json с номерами заехавшими/выехавшими в этом временном промежутке.

##### Пример:
```
  axios({
    method: 'post',
    url: '/count_plates' + "?token=" + token,
    data : {
      begin : 1571935875935,
      end : 1571935899998
    },
    headers: {
        "Content-type" : "application/json",
        'Access-Control-Allow-Origin': '*'
        
      }
  });
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