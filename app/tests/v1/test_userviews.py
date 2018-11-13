import unittest
import json
from ... import create_app
from ...api.v1.views import UserViews
from ...api.v1.models.UserModels import Order

class ParcelModelCase(unittest.TestCase):
    def setUp(self):
        
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.request_1 = json.dumps({"destination_address":"Nairobi", "pickup_address":"Kisumu", 
        "recipient_name":"keynote", "recipient_id":"316459", "item_type":"parcel", "weight":"65kg", "name":"keynote",
        "payment_status": "Not paid", "order_status":"canceled"})
        self.request_2 = json.dumps({
            "username":"Keynote", "email":"vik@gmail.com", "password":"pass", "con_password":"pass", "role":"admin"
        })
        self.request_3 = json.dumps({
            "username":"Keynote", "email":"vik@gmail.com", "password":"pass", "con_password":"password", "role":"admin"
        })

        self.request_4 = json.dumps({
             "email":"vik@gmail.com", "password":"pass", "con_password":"password", "role":"admin"
        })

        self.request_5 = json.dumps({
            "username":"Keynote", "email":"vik@gmail.com", "con_password":"password", "role":"admin"
        })

        self.request_6 = json.dumps({
            "email":"vik@gmail.com", "password":"password", "role":"admin"
        })
        self.request_7 = json.dumps({
            "username":"Keynote", "password":"pass", "con_password":"pass", "role":"admin"
        })
        self.data_1 = json.dumps({ "user_id":"1", "pickup_address":"Nairobi",\
         "destination_address":"Meru","order_type":"Parcel", "payment_status":"Not Paid", \
         "order_status":"Delivered"

        })
        self.data_2 = json.dumps({"destination_address":"Nairobi","pickup_address":"kisumu",\
        "recipient_name":"Victor","recipient_id":"35526","item_type":"letter"\
        ,"name":"Vik","status":"Delivered"

})

    def test_create_order(self):
        res = self.client.post('/api/v1/parcels', data=self.request_1, content_type='application/json')
        output = json.loads(res.data.decode())
        self.assertEqual(output['Status'], "created", msg="Incomplete credentials not allowed")
        assert res.status_code == 201

    def test_get_all_orders(self):
        res = self.client.get('/api/v1/parcels')

        self.assertTrue(res.status_code, 200)

    def test_cancel_order(self):
        res = self.client.put('/api/v1/parcels/1/cancel', data=self.request_1, content_type='application/json')
        output = json.loads(res.data.decode())
        assert res.status_code == 201
        self.assertEqual(output['Status'], 'order has been canceled')

    def test_register_user(self):
        res = self.client.post("/api/v1/register", data=self.request_2, content_type='application/json')
        output = json.loads(res.data.decode())
        assert res.status_code == 201
        assert res.content_type == 'application/json;charset=utf-8'
        assert output['Status'] == 'User created'

    def test_pass_not_matching(self):
        res = self.client.post("/api/v1/register", data=self.request_3, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['message'] == "Password and confirm password not matching"
        assert res.content_type == 'application/json'
        assert res.status_code == 400

    def test_username_missing(self):
        res = self.client.post("/api/v1/register", data=self.request_4, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['message'] == "Username missing"
        assert res.content_type == 'application/json'
        assert res.status_code == 400
        

    def test_password_missing(self):
        res = self.client.post("/api/v1/register", data=self.request_5, content_type='application/json')
        output = json.loads(res.data.decode())
        assert res.content_type == 'application/json'
        assert output['message'] == "Password missing"
        assert res.status_code == 400

    def test_user_login(self):
        res = self.client.post("/api/v1/login", data=self.request_6, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['Status'] == 'User Logged in'
        assert res.status_code == 201
        assert res.content_type == 'application/json;charset=utf-8'

    def test_email_missing(self):
        res = self.client.post("/api/v1/register", data=self.request_7, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['message'] == "Email missing"
        assert res.content_type == 'application/json'
        assert res.status_code == 400

    def test_payment_status(self):
        res = self.client.put("/api/v1/users/paid/1", data=self.data_1, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['message'] == 'order paid!'
        assert res.status_code == 200

    def test_delivered_status(self):
        res = self.client.put("/api/v1/users/delivered/1", data=self.data_1, content_type='application/json')
        output = json.loads(res.data.decode())
        assert output['message'] == 'order has been delivered!'
        assert res.status_code == 200        


if __name__ == '__main__':
    unittest.main()