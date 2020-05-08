
 on('body', 'click', '.module_sold', function(e) {
   e.preventDefault();
   send_change(this, "/users/ad_progs/sold/", "module_unsold", "Продано")
})

on('body', 'click', '.module_unsold', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/unsold/", "module_sold", "Не продано")
})

on('body', 'click', '.module_remove', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/delete/", "module_unremove", "Отмена")
})

on('body', 'click', '.module_unremove', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/undelete/", "module_remove", "Удалить")
})

on('body', 'click', '.module_active', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/active/", "module_unactive", "Активное")
})

on('body', 'click', '.module_unactive', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/unactive/", "module_active", "Черновик")
})

on('body', 'click', '.module_unactive', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/unactive/", "module_active", "Черновик")
})

on('body', 'click', '.module_unfavorite', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/unfavorite/", "module_favorite", "Запомнить")
})
on('body', 'click', '.module_favorite', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/favorite/", "module_unfavorite", "Забыть")
})

on('body', 'click', '.ad_like', function() {
  like = this;
  pk = document.getElementById("creator_pk").getAttribute("data-pk");
  uuid = document.querySelector(".page-title").getAttribute("data-uuid");
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/posts/votes/like/" + uuid + "/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    jsonResponse = JSON.parse(link.responseText);
    dislike = document.querySelector(".ad_dislike");
    likes_count = document.querySelector(".likes_count");
    dislikes_count = dislike.querySelector(".dislikes_count");
    likes_count.innerHTML = jsonResponse.like_count;
    dislikes_count.innerHTML = jsonResponse.dislike_count;
    like.classList.toggle("btn_success");
    like.classList.toggle("btn_default");
    dislike.classList.add("btn_default");
    dislike.classList.remove("btn_danger");
  }};
  link.send( null );
})
