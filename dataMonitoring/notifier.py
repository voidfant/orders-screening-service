import requests

def sendTelegram(user_ids, data):
    token = "5571330842:AAGKoBnF5XXumwCR5UisQQLs5o0xLwrCfEE"
    url = "https://api.telegram.org/bot"
    chat_id = "256995936"
    url += token
    method = url + "/sendMessage"
    for user_id in user_ids:
        r = requests.post(method, data={
            "chat_id": user_id,
            "text": f"Просим обратить внимание на то, что срок поставки по заказу {data[0]} истек {data[1]}"
            })

    if r.status_code != 200:
        raise Exception("post_text error")


# sendTelegram([469066515, 256995936])