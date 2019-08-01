from django.shortcuts import render

# Create your views here.
@csrf_exempt
def div(request):
	jsob = {"startNumber": 1000, "length": 10} #defaults
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			#######################
			#Custom Function Below#
			#######################
			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])
			loop = range(length)


			numarray = []

			divno = startNumber
			divisor = 2

			for l in loop:
				numarray.append(divno)
				divno = divno / divisor

			return JsonResponse({"div":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})		
	else:
		return JsonResponse(jsob)