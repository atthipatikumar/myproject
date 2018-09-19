from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from myproject.models.user import Users

class UsersResource(ModelResource):
	class Meta:
		collection_name="data"
		queryset = Users.objects.all()
		resource_name = 'user12'
		authorization = Authorization()