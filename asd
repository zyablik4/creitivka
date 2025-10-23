//html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="3.css">
</head>
<body>
    <h1>Поисковые системы</h1>
    <p>Google — это американская транснациональная технологическая корпорация и крупнейшая в мире поисковая система, которая обрабатывает миллиарды запросов ежемесячно. Она была основана Ларри Пейджем и Сергеем Брином в 1998 году. Google предоставляет широкий спектр сервисов, включая почту (Gmail), карты (Google Maps), облачное хранилище (Google Drive), видеохостинг (YouTube) и браузер (Google Chrome). </p>
    Ссылка на Google --->
    <a href="https://www.google.com/?hl=ru"><button>Google</button></a>
    <p>«Яндекс» — это российская IT-компания, которая изначально создала одноимённую поисковую систему, но сейчас владеет множеством интернет-сервисов и продуктов. Среди них «Яндекс.Карты», «Яндекс.Такси» (сейчас — «Яндекс Go»), «Яндекс.Музыка», голосовой помощник «Алиса», а также сервисы для бизнеса, такие как «Яндекс.Метрика» и «Яндекс.Директ». Поисковая система Яндекса ориентирована на русскоязычный сегмент интернета и считается одной из крупнейших в мире. </p>
    Ссылка на Yandex --->
    <a href="https://ya.ru/"><button>Yandex</button></a>
    <p class="sms">Вам смска</p>

</body>
</html>

//css
body{
    background-color: rgb(60, 58, 58);
    color: rgb(255, 255, 255);
    display: inline-block;
    font-family: 'Courier New', Courier, monospace;
    
}
button{
    background-color: rgb(26, 24, 24);
    border-radius: 10px;
    padding: 8px;
    color: wheat;
}
button:hover{
    background-color: rgb(78, 79, 81);
    
}
h1{
    background-color: rgb(33, 32, 32);
    padding: 20px;
    border-radius: 0px 0px 20px 20px;
    margin-top: -10px;
    margin-left: -10px;
}
.sms{
    position: fixed;
    top: 7px;
    right: 10em;
    background: linear-gradient(60deg, rgb(0, 0, 0), rgb(131, 125, 89));
    padding: 7px;
    border-radius: 10px;
}
