def wsgi_application(environ, start_response):

	# BUSINESS LOGIC #

	query = environ.get('QUERY_STRING').split("&")
	body = ""
	for i in query:
		body += i + "\n"

	##################

	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]

	print(body)

	start_response(status, headers)
	return [bytes(body, 'utf-8')]