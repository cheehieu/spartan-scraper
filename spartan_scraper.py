import requests

#bibtex_id = '10.1007/s00425-007-0544-9'
#url = "http://www.doi2bib.org/#/doi/{id}".format(id=bibtex_id)
#xhr_url = 'http://www.doi2bib.org/doi2bib'
#
#with requests.Session() as session:
#    session.get(url)
#
#    response = session.get(xhr_url, params={'id': bibtex_id})
#    print(response.content)

url = 'http://isslive.com/displays/spartanDisplay1.html'
xhr_url = ''
id = 'displays-section-toggle2'
url_get = 'http://push1.isslive.com/lightstreamer/ajax_frame.html?phase=64&domain=isslive.com&'

r = requests.get(url_get)
print r.text


