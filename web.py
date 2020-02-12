from bottle import route, run, template, request
from back.parser import count_from_html

dictio = {}

@route('/parser')
def url_form(): 
    return template(
    '''
    <div>
    <form action="/parser" method="post">
            URL: <input name="url" type="text" />
            
            <input value="URL" type="submit" />
        </form>
    <br>
 
    </div>''')


@route('/parser', method='POST')
def get_url():
    url = request.forms.get('url')
    dictio = count_from_html(url)
    return template(
    '''
    <div>
    <form action="/parser" method="post">
            URL: <input name="url" type="text" />
            
            <input value="URL" type="submit" />
        </form>
    <br>
    <p>{{a}}</p>
    </div>''', a = dictio)
    
    
run(host='localhost', port=8080)
