import re
def domain_name(url):
    clean_left_url = clean_left(url)    
    clean_left_right_url = clean_right(clean_left_url)
    return clean_left_right_url
    
def clean_left(url):
    clean_left_url = url
    #http:// first remove the http
    if 'http://' in url:
        split_http = re.split('http://', url)
        clean_left_url = split_http[1]
    #https:// second remove the https
    if 'https://' in url:
        split_https = re.split('https://', url)
        clean_left_url = split_https[1]
    #www. //third remove the www
    if 'www' in url:
        split_www = re.split('www.', url)
        clean_left_url = split_www[1]
    return clean_left_url
    
def clean_right(clean_left_url):
    dot_index = clean_left_url.index('.')
    return clean_left_url[:dot_index]