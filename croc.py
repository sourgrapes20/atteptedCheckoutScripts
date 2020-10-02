import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
action: add
updates: approaching
pid: 205434-066-M6W8
qty: 1
sizeLabel: Women
'''




def main():
    with requests.session() as session:
        cart_url = 'https://www.crocs.com/on/demandware.store/Sites-crocs_us-Site/default/Cart-API'

        payload = {
            "action":"add",
            "updates":"approaching",
            "pid":"205434-066-M6W8",
            "qty":"1",
            "sizeLabel":"Women"
        }
        #adds to cart
        response = session.post(cart_url, data=payload)
        print(response.status_code, "cart")


        checkout_url = 'https://www.crocs.com/on/demandware.store/Sites-crocs_us-Site/default/COCheckout-Step'
        response = session.get(checkout_url)
        print(response.status_code, "checkout")
        checkout_html = response.text
        '''
        #csrf_token scraper
        token_string = 'csrf_token","value":"'
        index = checkout_html.index(token_string) + 21
        csrf_token = ""
        while(checkout_html[index] != "="):
            csrf_token = csrf_token + checkout_html[index]
            index = index+1
        
        csrf_token = csrf_token + "="
        checkout_payload = {
            "wfrm_root_browserinfo_colordepth": "24",
            "dwfrm_root_browserinfo_screenheight": "864",
            "dwfrm_root_browserinfo_screenwidth": "1536",
            "dwfrm_root_browserinfo_timezoneoffset": "420",
            "dwfrm_root_browserinfo_javaenabled": "false",
            "csrf_token":str(csrf_token),
            "dwfrm_root_singleshipping_shippingAddress_addressFields_firstName": "Sargune",
            "dwfrm_root_singleshipping_shippingAddress_addressFields_lastName": "Kalsi",
            "dwfrm_root_singleshipping_shippingAddress_addressFields_address1": "17144 NW Mesa View Ln.",
            "dwfrm_root_singleshipping_shippingAddress_addressFields_address2": "",
            "dwfrm_root_singleshipping_shippingAddress_addressFields_zip": "97006",
            "dwfrm_root_singleshipping_shippingAddress_addressFields_city": "BEAVERTON",
            "dwfrm_root_singleshipping_shippingAddress_addressFields_states_state": "OR",
            "dwfrm_root_singleshipping_shippingAddress_addressFields_phone": "(971) 325-7738",
            "dwfrm_root_singleshipping_shippingAddress_email_emailAddress": "sourgrapes20@gmail.com",
            "dwfrm_root_singleshipping_shippingAddress_email_emailAddressConfirm": "sourgrapes20@gmail.com",
            "dwfrm_root_singleshipping_shippingAddress_addressFields_country": "US",
            "dwfrm_root_singleshipping_shippingAddress_addressID":"",
            "donotcountme": "on",
            "dwfrm_root_billing_guestBillingAddressIsTheSameAsShippingAddress": "true",
            "dwfrm_root_billing_billingAddress_addressFields_country":"US",
            "dwfrm_root_billing_billingAddress_addressFields_firstName": "Sargune",
            "dwfrm_root_billing_billingAddress_addressFields_lastName": "Kalsi",
            "dwfrm_root_billing_billingAddress_addressFields_address1": "17144 NW Mesa View Ln.",
            "dwfrm_root_billing_billingAddress_addressFields_address2": "",
            "dwfrm_root_billing_billingAddress_addressFields_zip": "97006",
            "dwfrm_root_billing_billingAddress_addressFields_city": "BEAVERTON",
            "billingstatemockselectcheckout": "",
            "dwfrm_root_billing_billingAddress_addressFields_states_state": "OR",
            "dwfrm_root_billing_billingAddress_addressFields_phone": "(971) 325-7738",
            "dwfrm_root_billing_billingAddress_addressID": "1601340860132",
            "dwfrm_root_singleshipping_shippingMethod_shippingMethodID": "dayton-economy5_6",
            "cardnumber":"",
            "pin":"" ,
            "dwfrm_root_billing_paymentMethods_selectedPaymentMethodID": "AdyenDirect",
            "dwfrm_root_billing_paymentMethods_creditCard_owner_d0wmaghthrjv": "Sargune Kalsi",
            "dwfrm_root_billing_paymentMethods_creditCard_number_d0prfrjtvpqe": "4767 7182 2375 8642",
            "dwfrm_root_billing_paymentMethods_creditCard_type_d0kiyteieaqx": "VISA",
            "dwfrm_root_billing_paymentMethods_creditCard_cardexpire": "05/25",
            "cvvmaskedc38d9": "***",
            "dwfrm_root_billing_paymentMethods_creditCard_cvn_d0ogipjjdwuq": "761",
            "dwfrm_root_billing_paymentMethods_creditCard_month_d0jqcdlhsdtl": "5",
            "dwfrm_root_billing_paymentMethods_creditCard_year_d0umholvikig": "2025",
            "dwfrm_root_submitorder":""
        }

        submit_url = "https://www.crocs.com/on/demandware.store/Sites-crocs_us-Site/default/COCheckout-Step/C1948035565"
        response = session.post(submit_url, data=checkout_payload)
        print(response.status_code, "submit order")
        with open('index.html', 'w', encoding="utf-8") as f:
            f.write(response.text)
        '''
        cookieJar = session.cookies.get_dict()
        print(cookieJar)
        '''
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=selenium") 
        chrome_driver = 'C:/Users/sourg/Desktop/Programming/chromedriver_win32/chromedriver'
        driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
        driver.get('http://google.com')
        driver.add_cookie(cookieJar)
        '''

if __name__ =='__main__':
    main()

