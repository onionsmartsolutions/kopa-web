from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)

class Sms():
	gateway = None
	def initialize():
		username = "onionapp"
		apikey   = "5c8ce53d0963fda2013f418ede4c0cd7d867206c1646f71a51cb647eb0524692"
		gateway = AfricasTalkingGateway(username, apikey)
	
	def send_message(to,message):
		self.initialize()
		try:
		    results = gateway.sendMessage(to, message)
		except AfricasTalkingGatewayException:
		    print ('Encountered an error while sending')




