from django.http import Http404, HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings
from myproject.db import query

def users123(request):
	id = request.REQUEST.get('id','')
	age = request.REQUEST.get('age','')
	
	if id != '':
		sql = "SELECT * from number WHERE id= %s"
		param_for_user_details=[id]        
   
	elif age != '':
		sql = "SELECT * from number WHERE age= %s"
		param_for_user_details=[age]
	else:
		sql = "SELECT * from number"
		param_for_user_details=[]
	results = query(sql,*param_for_user_details)     
	final_test_map = []  
	metadata_totalcount=0 
    #result is constructed in the expected format
	for result in results:
		metadata_totalcount=metadata_totalcount+1
		response_map = {}
		response_map['id']=result['id']
		response_map['age']=result['age']                                                                                       
		final_test_map.append(response_map)       
	metadata = {"total_count":metadata_totalcount}
	response = {"metadata":metadata,'data_test':final_test_map} 
	data = json.dumps(response, encoding="ISO-8859-1")    
	http_response = HttpResponse(data,content_type="application/json")
	return http_response