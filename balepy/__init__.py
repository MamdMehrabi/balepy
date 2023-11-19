from balepy.main import Client
from balepy.Messages import messages

app = Client('905219034:yV3KyeqlSQDHPLF38vX6t2ychdCLSSAXEsRnngy7')
s = app.polling()
print(s)