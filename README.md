# plates

Запись и чтение из базы госномеров

 
### Чтение:
- Всех номеров сразу /get 

- Номера по id /get/<int:id>


### Запись:
- /send Принимает три аргумента CamID, Timestamp, Licplates


##### Пример:
```
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "http://127.0.0.1:5000/send", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("CamID=3&Timestamp=0&Licplates=c777cc198");
```