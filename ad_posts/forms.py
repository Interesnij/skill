from django import forms


class Form_1(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.auto import Auto
		model=Auto
		exclude = ['creator',]


class Form_2(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.spez_moto import SpecMoto
		model=SpecMoto
		exclude = ['creator',]


class Form_3(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.zap_auto import ZapAuto
		model=ZapAuto
		exclude = ['creator',]


class Form_4(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.realty import Realty
		model=Realty
		exclude = ['creator',]

class Form_5(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.service import Service
		model=Service
		exclude = ['creator',]

class Form_6(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.women import Women
		model=Women
		exclude = ['creator',]

class Form_7(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.man import Man
		model=Man
		exclude = ['creator',]

class Form_8(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.child import Child
		model=Child
		exclude = ['creator',]

class Form_9(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.baby import Baby
		model=Baby
		exclude = ['creator',]

class Form_10(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_posts.models import Ad
		model=Ad
		exclude = ['creator',]

class Form_11(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.phone import PhoneAd
		model=PhoneAd
		exclude = ['creator',]

class Form_12(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.foto_video import FotoVideo
		model=FotoVideo
		exclude = ['creator',]

class Form_13(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.comp import Comp
		model=Comp
		exclude = ['creator',]

class Form_14(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.tv import TV
		model=TV
		exclude = ['creator',]

class Form_15(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.home_tech import HomeTech
		model=HomeTech
		exclude = ['creator',]

class Form_16(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.home_garden import HomeGarden
		model=HomeGarden
		exclude = ['creator',]

class Form_17(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.repair import Repair
		model=Repair
		exclude = ['creator',]

class Form_18(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
	from ad_model.beauty import Beauty
		model=Beauty
		exclude = ['creator',]

class Form_19(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from ad_model.sport import Sport
		model=Sport
		exclude = ['creator',]

class Form_20(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from hobbies.sport import Hobbies
		model=Hobbies
		exclude = ['creator',]

class Form_21(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from hobbies.job import Job
		model=Job
		exclude = ['creator',]

class Form_22(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from hobbies.pets import Pets
		model=Pets
		exclude = ['creator',]

class Form_23(forms.ModelForm):
	description = forms.CharField( label="",widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

	class Meta:
		from hobbies.biznes import Biznes
		model=Biznes
		exclude = ['creator',]
