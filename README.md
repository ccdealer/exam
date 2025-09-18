api/v1/registration/ - POST -  апи регистрации. Обязательные поля отмеченны "***", письмо отправляется на email
    {
    "username": "", ***
    "first_name": "", 
    "last_name": "",
    "email": "", ***
    "password": "" ***
  }
auth/activate/{user.pk}/?code={user.activation_code} - GET - энпоинт активации аккаунта. Ссылка в письме

авторизация с помощью jwt token
api/token - { "email": "Ваш email", "password", "Ваш Password"}

articles - Get - Все статьи
articles/?fersh={любое значение} - возвращает статьи за последние 24 часа
articeles/?q={Ваше значение для поиска по оглавлениям} - поиск по оглавлениям



articles/update - POST - параметры поиска - 
  { "q": "Тема поиска",
    "sources":"источник",
    "language": "Язык" }

  
