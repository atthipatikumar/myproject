from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from myproject.models.user1 import Users1

class UsersResource(ModelResource):
	class Meta:
		collection_name="data"
		queryset = Users1.objects.all()
		resource_name = 'user79'
		authorization = Authorization()