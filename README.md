Бот для телеграм, отправляющий пользователю эхо-сообщение. Написан на flask, requests по мотивам заказа на фриланс-бирже, который не удалось получить. :) Запускается в докер-контейнере с помощью [waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/) и выводится &laquo;в мир&raquo; с помощью pyngrok.

В качестве основы использована статья с хабра &laquo;[Простой Telegram-бот на Flask с информированием о погоде](https://habr.com/ru/post/495036/)&raquo;.

Токен бота указывается в качестве переменной окружения `token` в файле `.env`.

Сборка: `docker build -t tgbot`

Запуск: `docker run tgbot`

