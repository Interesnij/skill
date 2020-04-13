from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
	template_name = None

	def get(self,request,*args,**kwargs):
		import re

		if request.user.is_authenticated and not request.user.is_deleted:
			self.template_name = "main/page.html"
		elif request.user.is_authenticated and request.user.is_deleted:
			self.template_name = "generic/user_deleted.html"
		elif request.user.is_anonymous:
			self.template_name = "main/anon_page.html"

		MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
		if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
			self.template_name = "mob_" + self.template_name
		return super(MainPageView,self).get(request,*args,**kwargs)


class MainPhoneSend(TemplateView):
	template_name="main/phone_verification.html"
