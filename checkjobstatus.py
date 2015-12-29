import requests
from BeautifulSoup import BeautifulSoup
URL = 'http://disneycareers.com/en/my-dashboard/'
headers = {'User-Agent': 'Mozilla/5.0','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest'}
payload = {
	'username': 'username',
	'password': 'password',
}

session = requests.session()
r = session.post(URL, data=payload)
page = BeautifulSoup(r.text)
# print page
# print r.cookies

applicationUrl = "http://disneycareers.com/en/dashsvc/?ws=dashboard&t=application"
a = session.get(applicationUrl,headers=headers)
html =  BeautifulSoup(a.text)
for b in html('table')[0]("b"):
	if b != None:
		text = b.text
		text = text.replace("&nbsp", "")
		text = text.replace('\\r\\n', "")
		text = text.replace(';', "")
		text = text.replace('<\/div>', "")
		text = text.replace('<\/b>', "")
		lines =  text.splitlines()
		print lines[0].split("\\t")[0]
