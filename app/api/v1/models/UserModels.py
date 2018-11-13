import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class Order(object):
	orders = []
	def create_order(self, destination_addr, pickup_addr,recipient_name,recipient_id,item_type,weight,order_status,payment_status,name):
		self.destination_addr = destination_addr
		self.pickup_addr = pickup_addr
		self.recipient_name = recipient_name
		self.recipient_id = recipient_id
		self.item_type = item_type
		self.weight = weight
		self.order_status = order_status
		self.payment_status = payment_status
		self.name = name

		payload  ={
		"order_id": str(uuid.uuid4().int),
		"destination_address":self.destination_addr,
		"pickup_address":self.pickup_addr,
		"recipient_name":self.recipient_name,
		"recipient_id":self.recipient_id,
		"item_type":self.item_type,
		"weight":self.weight,
		"order_status":self.order_status,
		"payment_status":self.payment_status,
		"name":self.name
		}

		Order.orders.append(payload)
		return True
	def get_all(self):
		"""Get all orders
		return: """
		return Order.orders

	def get_one_order(self,order_id):
		"""Gets a specific order with order_id as arguments
		param:order_id
		:return:"""
		
		for item in Order.orders:
			if item["order_id"] == order_id:
				return item

	def get_one_user_orders(self, name):
		for order in Order.orders:
			if order['name'] == name:
				return order
			return "No such order"

	def cancel_order(self, order_id):
		for order in Order.orders:
			if order["order_id"] == order_id:
				order['order_status'] = 'canceled'
				return True

	def get_user_orders(self, name):
		orders = [order for order in Order.orders
                   if order['name'] == name]
		return orders	

class User_model(object):
	fields = []
	def create_user(self, email, username, password, con_password, role):
		self.email = email
		self.username = username 
		self.password = password
		self.con_password = con_password
		self.role = role


		payload={
			"user_id": str(uuid.uuid4().int),
			"email":self.email,
			"username":self.username,
			"password":self.password,
			"con_password":self.con_password,
			"role":self.role
		}
		User_model.fields.append(payload)
		return True

	def login_user(self, email, password, role):
		self.email = email
		self.password = password,
		self.role = role

		payload={
			"user_id":str(uuid.uuid4().int),
			"email":self.email,
			"password":self.password,
			"role":self.role
		}
		User_model.fields.append(payload)
		return True

	
	