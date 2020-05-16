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
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_ad_advertiser");
    next_next_target.classList.add("user_add_ad_advertiser"); next_next_target.classList.remove("user_remove_ad_advertiser"); next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_ad_editor', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/delete_editor/", "user_add_ad_editor", "сделать редактором");
})

on('body', 'click', '.user_add_ad_moderator', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/ad_progs/add_moderator/", "user_remove_ad_moderator", "модератор - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_ad_advertiser");
    next_target.classList.add("user_add_ad_advertiser"); next_target.classList.remove("user_remove_ad_advertiser"); next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_ad_editor");
    prev_target.classList.add("user_add_ad_editor"); prev_target.classList.remove("user_remove_ad_editor"); prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_ad_admin");
    prev_prev_target.classList.add("user_add_ad_admin"); prev_prev_target.classList.remove("user_remove_ad_admin"); prev_prev_target.innerHTML = "сделать админом";
  }catch{null}

})
on('body', 'click', '.user_remove_ad_moderator', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/delete_moderator/", "user_add_ad_moderator", "сделать модератор");
})

on('body', 'click', '.user_add_ad_advertiser', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/ad_progs/add_advertiser/", "user_remove_ad_advertiser", "рекламодатель - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_ad_moderator");
    prev_target.classList.add("user_add_ad_moderator"); next_target.classList.remove("user_remove_ad_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_ad_editor");
    prev_prev_target.classList.add("user_add_ad_editor"); prev_prev_target.classList.remove("user_remove_ad_editor"); prev_prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_prev_target = admin_span.previousElementSibling.previousElementSibling.previousElementSibling.querySelector(".user_remove_ad_admin");
    prev_prev_prev_target.classList.add("user_add_ad_admin"); prev_prev_prev_target.classList.remove("user_remove_ad_admin"); prev_prev_prev_target.innerHTML = "сделать админом";
  }catch{null}
})
on('body', 'click', '.user_remove_ad_advertiser', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/delete_advertiser/", "user_add_ad_advertiser", "сделать рекламодателем");
})
