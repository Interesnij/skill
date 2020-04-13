from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
	template_name = None

	def get(self,request,*args,**kwargs):
		self.template_name = request.user.get_template_main(folder="main/", template="page.html", request=request)
		return super(MainPageView,self).get(request,*args,**kwargs)
