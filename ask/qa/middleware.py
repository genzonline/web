from django.http import HttpResponse
from .models import Session, User


def CheckSessionMiddleware(get_response):
	def process_request(request):
		try:
			sessionid = request.COOKIE.get('sessionid')
			session = Session.objects.get(
				key = sessionid,
				expires__gt=datetime.now(),
			)
			request.session = session
			request.user = session.user
		except Session.DoesNotExist:
			request.session = None
			request.user = None