import urllib.request
import re

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html_str):
    result = re.findall('[<][!]*[a-zA-Z]+[a-zA-Z0-9]+', html_str)
    result += re.findall('[<][a(?= )||piqbus(?=>)]', html_str)
    #result = re.findall('[/][a-zA-Z0-9]+[>]+', html_str)
    return result
    
def bytestostring(bytes):
    encoding = 'utf-8'
    string = str(bytes, encoding)
    return string

def count_elemets(array):
    array_dict = {}.fromkeys(array,0)
    for a in array:
        array_dict[a] += 1
    return array_dict

def remove_angles(elements_list):
    for i in range(0, len(elements_list)):
        elements_list[i] = elements_list[i][1:]
    return(elements_list)
    
def count_from_html(url):
    parsed_bytes = get_html(url)
    html_text = bytestostring(parsed_bytes)
    html_elements_list = sorted(parse(html_text))
    html_elements_list = remove_angles(html_elements_list)
    html_elements_dict = count_elemets(html_elements_list)
    return html_elements_dict

def main():
    count_from_html('https://pythonworld.ru/osnovy/indeksy-i-srezy.html')
    
    
    
if __name__ == '__main__':
    main()
    