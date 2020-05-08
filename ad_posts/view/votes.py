import json
from users.models import User
from ad_posts.models import Ad
from django.http import HttpResponse
from django.views import View
from common.model.votes import AdVotes


class AdLike(View):
    def get(self, request, **kwargs):
        ad = Ad.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user.pk != request.user.pk and not request.user.is_blocked_with_user_with_id(user_id=user.pk):
            try:
                likedislike = AdVotes.objects.get(parent=ad, user=request.user)
                if likedislike.vote is not AdVotes.LIKE:
                    likedislike.vote = AdVotes.LIKE
                    likedislike.save(update_fields=['vote'])
                    result = True
                else:
                    likedislike.delete()
                    result = False
            except AdVotes.DoesNotExist:
                AdVotes.objects.create(parent=ad, user=request.user, vote=AdVotes.LIKE)
                result = True
                #item.notification_user_like(request.user)
        return HttpResponse(json.dumps({"result": result,
                                        "like_count": str(ad.likes.count),
                                        "dislike_count": str(ad.dislikes.count)}),
                                    content_type="application/json")


class AdDisLike(View):
    def get(self, request, **kwargs):
        ad = Ad.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user.pk != request.user.pk and not request.user.is_blocked_with_user_with_id(user_id=user.pk):
            try:
                likedislike = AdVotes.objects.get(parent=ad, user=request.user)
                if likedislike.vote is not AdVotes.DISLIKE:
                    likedislike.vote = AdVotes.DISLIKE
                    likedislike.save(update_fields=['vote'])
                    result = True
                else:
                    likedislike.delete()
                    result = False
            except AdVotes.DoesNotExist:
                AdVotes.objects.create(parent=ad, user=request.user, vote=AdVotes.DISLIKE)
                result = True
                #item.notification_user_dislike(request.user)
        return HttpResponse(json.dumps({"result": result,
                                        "like_count": str(ad.likes.count),
                                        "dislike_count": str(ad.dislikes.count)}),
                                    content_type="application/json")
