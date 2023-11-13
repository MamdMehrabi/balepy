from balepy import Client

token = '814560181:KG3YW2RKX6TJyujoaxNr5Aqp8YCJczk7MHnXEtKA'
app = Client(token)
seen = [u["update_id"] for u in (app.get_updates())["result"]]
while True:
    updates = (app.get_updates()).json()["result"]
    for update in updates:
        pass