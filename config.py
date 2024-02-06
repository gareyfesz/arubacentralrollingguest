from passwordgen import password




central_info = {
        "username": "central_username_non_sso",
        "password": "central_password",
        "client_id": "client_id",
        "client_secret": "client_secret",
        "customer_id": "customer_id",
        "base_url": "base_url"
    }

# API path that includes central portal id and visitor id that we are updating


apiPath = "/guest/v1/portals/PORTAL_ID/visitors/VISITOR_ID"


# API data to push to specified central visitor

apiData = {
  "name": "guestusername",
  "user": {
    "phone": "+1XXXXXXXXXX",
    "email": "email@email.local"
  },
  "is_enabled": True,
  "valid_till_no_limit": False,
  "valid_till_days": 7,
  "valid_till_hours": 0,
  "valid_till_minutes": 0,
  "notify": False,
  "notify_to": "email",
  "password": password,
  "status": True,
  "created_at": {},
  "expire_at": {}
}



# email parameters

sender_email = "email@email.local"
recipient_email = "email@email.local"
smtp_server = "127.0.0.1"
smtp_port = "25"
subject = 'password of the week'


# define username
name = "username"
