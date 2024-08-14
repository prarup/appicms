import frappe
from frappe import auth

@frappe.whitelist( allow_guest=True )
def login(usr, pwd):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()
    except:
        frappe.throw(title='Error',msg='Invalid ID or Password')
        return

    api_generate = generate_keys(frappe.session.user)
    user = frappe.get_doc('User', frappe.session.user)

    frappe.response["auth"] = {
        "success_key":1,
        "message":"Authentication success",
        "sid":frappe.session.sid,
        "api_key":user.api_key,
        "api_secret":api_generate,
		"username": user.name,
		"role": user.type,
		"mapping": user.mapping,
		"partner": user.partner,
		"mobile_no": user.mobile_no
	}





def generate_keys(usr):
    user_details = frappe.get_doc('User', usr)
    api_secret = frappe.generate_hash(length=15)

    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    user_details.api_secret = api_secret

    tokens = "token "
    colon = ":"
    user_details.token = tokens + user_details.api_key + colon + user_details.api_secret


    user_details.save()

    return api_secret
