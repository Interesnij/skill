on('body', 'click', '#register_ajax', function() {
  form_data = new FormData(document.querySelector("#signup"));
  reg_link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  reg_link.open( 'POST', "/rest-auth/registration/", true );
  reg_link.onreadystatechange = function () {
  if ( reg_link.readyState == 4 && reg_link.status == 200 ) {
    window.location.href = "/phone_send/";
    console.log("vse ok")
    }};
  reg_link.send(form_data);
})
on('body', 'click', '#logg', function() {
  form_data = new FormData(document.querySelector("#login"));
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'POST', "/rest-auth/login/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    window.location.href = "/";
    }};
  link.send(form_data);
});

on('body', 'click', '#phone_send', function() {
  var phone = document.getElementById('phone').value;
  var request = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  request.open( 'GET', "/users/progs/phone_send/" + phone + "/", true );
  request.onreadystatechange = function () {
    if ( request.readyState == 4 && request.status == 200) {
      var div = document.getElementById('jsondata');
      div.innerHTML = request.responseText;
      document.getElementById("phone").setAttribute("disabled", "true");
      document.getElementById("phone_send").setAttribute("disabled", "true");
    }
  };
  request.send( null );
});

on('body', 'click', '#code_send', function(e) {
var phone = document.getElementById('phone').value;
var code = document.getElementById('code').value;
var request = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
request.open( 'GET', "/users/progs/phone_verify/" + phone + "/" + code + "/", true );
request.onreadystatechange = function () {
  if ( request.readyState == 4 && request.status == 200 ) {
    var div = document.getElementById('jsondata2');
    div.innerHTML = request.responseText;
    console.log(request.responseText);
    if (request.responseText.indexOf("ok") != -1){window.location.href = "{% url 'user' pk=request.user.pk %}";}
  }
};
request.send( null );

});

on('body', 'click', '.user_subscribe', function(e) {
  e.preventDefault();
  parent = this.parentElement;
  send_change(this, "/users/progs/subscribe/", "user_unsubscribe", "отписаться");
  try{
    target = parent.nextElementSibling.querySelector(".user_unblock");
    send_change(target, "/users/progs/unblock/", "user_block", "заблокировать");
  }catch{null}
})

on('body', 'click', '.user_unsubscribe', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/unsubscribe/", "user_subscribe", "подписаться");
})

on('body', 'click', '.user_block', function(e) {
  e.preventDefault();
  parent = this.parentElement;
  send_change(this, "/users/progs/block/", "user_unblock", "разблокировать");
  try{
  target = parent.previousElementSibling.querySelector(".user_unsubscribe");
  parent.previousElementSibling.style.opacity="0";
  target.classList.add("user_subscribe");
  target.classList.remove("user_unsubscribe");
  target.innerHTML = "подписаться";
  }catch{parent.previousElementSibling.style.opacity="0"}

})

on('body', 'click', '.user_unblock', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/unblock/", "user_block", "заблокировать");
  this.parentElement.previousElementSibling.style.opacity="1";
})


on('body', 'click', '.user_add_ad_admin', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/ad_progs/add_admin/", "user_remove_ad_admin", "админ - разжаловать");
  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_ad_editor");
    next_target.classList.add("user_add_ad_editor"); next_target.classList.remove("user_remove_ad_editor"); next_target.innerHTML = "сделать редактором";
  }catch{null}

  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_ad_moderator");
    next_next_target.classList.add("user_add_ad_moderator"); next_next_target.classList.remove("user_remove_ad_moderator"); next_next_target.innerHTML = "сделать модератором";
  }catch{null}

  try{
    next_next_next_target = admin_span.nextElementSibling.nextElementSibling.nextElementSibling.querySelector(".user_remove_ad_advertiser");
    next_next_next_target.classList.add("user_add_ad_advertiser"); next_next_next_target.classList.remove("user_remove_ad_advertiser"); next_next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_ad_admin', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/delete_admin/", "user_add_ad_admin", "сделать админом");
})

on('body', 'click', '.user_add_ad_editor', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/ad_progs/add_editor/", "user_remove_ad_editor", "редактор - разжаловать");
  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_ad_admin");
    prev_target.classList.add("user_add_ad_admin"); prev_target.classList.remove("user_remove_ad_admin"); prev_target.innerHTML = "сделать админом";
  }catch{null}

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_ad_moderator");
    next_target.classList.add("user_add_ad_moderator"); next_target.classList.remove("user_remove_ad_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}

  try{
    next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_ad_advertiser");
    next_target.classList.add("user_add_ad_advertiser"); next_target.classList.remove("user_remove_ad_advertiser"); next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_ad_editor', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/delete_editor/", "user_add_ad_editor", "сделать редактором");
})
