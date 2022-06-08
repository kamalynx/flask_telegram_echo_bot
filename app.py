from os import getenv

from flask import Flask
from flask import jsonify
from flask import request
from pyngrok import ngrok
import requests
from waitress import serve


app = Flask(__name__)
app.config['token'] = getenv('token')


def update_telegram_webhook(token: str, url: str):
    """Задать url для вебхука Телеграм бота.

    :param token: токен бота
    :param url: url метода API Телеграм для обновления хука
    """
    request = requests.post(
        f'https://api.telegram.org/bot{token}/setWebhook',
        json={"url": url}
    )
    return request.json()


def send_echo_message(chat_id: int, text: str) -> None:
    """Отправить эхо-сообщение пользователю.

    :param chat_id: уникальный идентификатор чата
    :param text: сообщение, присланное пользователем
    :param method: метод API Телеграм, который будет вызван
    :param token: токен бота
    :param data: словарь, содержащий id чата и сообщение
    """
    method: str = 'sendMessage'
    token: str = app.config.get('token')
    url: str = f'https://api.telegram.org/bot{token}/{method}'
    data: dict = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)


@app.route('/', methods=['GET', 'POST'])
def handle_request_from_bot():
    """Обработать запрос, приходящий от бота."""
    if request.method == 'POST':
        app.logger.info(request.json)
        chat_id: int = request.json['message']['chat']['id']
        message: str = request.json['message']['text']
        send_echo_message(chat_id, message)
    return jsonify({'ok': True})


if __name__ == '__main__':
    http_tunnel = ngrok.connect(8080, bind_tls=True).public_url
    app.logger.info(
        update_telegram_webhook(app.config.get('token'), http_tunnel)
    )
    serve(app, host='0.0.0.0', port=8080)
