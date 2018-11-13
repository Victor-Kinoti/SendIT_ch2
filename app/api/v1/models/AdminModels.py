import uuid
class UserOrders(object):
    orders = [{
        "user_id":str(uuid.uuid4().int),
        "pickup_address":"Nairobi",
        "destination_address":"Meru",
        "order_type":"Parcel",
        "payment_status":"Not Paid",
        "order_status":"Delivered"


    },
    {
        "user_id":str(uuid.uuid4().int),
        "pickup_address":"Naivasha",
        "destination_address":"Thika",
        "order_type":"Envelope",
        "payment_status":"Paid",
        "order_status":"Delivered"


    },
    {
        "user_id":str(uuid.uuid4().int),
        "pickup_address":"Mombasa",
        "destination_address":"Nakuru",
        "order_type":"Parcel",
        "payment_status":"Paid",
        "order_status":"InTransit"


    }]

    def get_all_orders(self):
        return UserOrders.orders

    def get_one_user_order(self, user_id):
        for item in UserOrders.orders:
            if item["user_id"] == user_id:
                return item


    def update_order_status(self, user_id):
        for item in UserOrders.orders:
            if item["user_id"] == user_id:
                item['order_status'] == 'Delivered'
                return True
    
    def update_order_payment(self, user_id):
        for item in UserOrders.orders:
           
            if item["user_id"] == user_id:
                if item['payment_status'] == 'Paid':
                    item['payment_status'] == 'Not Paid'
                else:
                    item['payment_status'] == 'Paid'
                return True
