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

// =======================================================================================
// ============================================================================================
on('body', 'click', '.user_add_anketa_admin', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/love_progs/add_admin/", "user_remove_anketa_admin", "админ - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_anketa_editor");
    next_target.classList.add("user_add_anketa_editor"); next_target.classList.remove("user_remove_anketa_editor"); next_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_anketa_moderator");
    next_next_target.classList.add("user_add_anketa_moderator"); next_next_target.classList.remove("user_remove_anketa_moderator"); next_next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    next_next_next_target = admin_span.nextElementSibling.nextElementSibling.nextElementSibling.querySelector(".user_remove_anketa_advertiser");
    next_next_next_target.classList.add("user_add_anketa_advertiser"); next_next_next_target.classList.remove("user_remove_anketa_advertiser"); next_next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_anketa_admin', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete_admin/", "user_add_anketa_admin", "сделать админом");
})

on('body', 'click', '.user_add_anketa_editor', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/love_progs/add_editor/", "user_remove_anketa_editor", "редактор - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_anketa_admin");
    prev_target.classList.add("user_add_anketa_admin"); prev_target.classList.remove("user_remove_anketa_admin"); prev_target.innerHTML = "сделать админом";
  }catch{null}
  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_anketa_moderator");
    next_target.classList.add("user_add_anketa_moderator"); next_target.classList.remove("user_remove_anketa_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_anketa_advertiser");
    next_next_target.classList.add("user_add_anketa_advertiser"); next_next_target.classList.remove("user_remove_anketa_advertiser"); next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_anketa_editor', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete_editor/", "user_add_anketa_editor", "сделать редактором");
})

on('body', 'click', '.user_add_anketa_moderator', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/love_progs/add_moderator/", "user_remove_anketa_moderator", "модератор - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_anketa_advertiser");
    next_target.classList.add("user_add_anketa_advertiser"); next_target.classList.remove("user_remove_anketa_advertiser"); next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_anketa_editor");
    prev_target.classList.add("user_add_anketa_editor"); prev_target.classList.remove("user_remove_anketa_editor"); prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_anketa_admin");
    prev_prev_target.classList.add("user_add_anketa_admin"); prev_prev_target.classList.remove("user_remove_anketa_admin"); prev_prev_target.innerHTML = "сделать админом";
  }catch{null}

})
on('body', 'click', '.user_remove_anketa_moderator', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete_moderator/", "user_add_anketa_moderator", "сделать модератор");
})

on('body', 'click', '.user_add_anketa_advertiser', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/love_progs/add_advertiser/", "user_remove_anketa_advertiser", "рекламодатель - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_anketa_moderator");
    prev_target.classList.add("user_add_anketa_moderator"); next_target.classList.remove("user_remove_anketa_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_anketa_editor");
    prev_prev_target.classList.add("user_add_anketa_editor"); prev_prev_target.classList.remove("user_remove_anketa_editor"); prev_prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_prev_target = admin_span.previousElementSibling.previousElementSibling.previousElementSibling.querySelector(".user_remove_anketa_admin");
    prev_prev_prev_target.classList.add("user_add_anketa_admin"); prev_prev_prev_target.classList.remove("user_remove_anketa_admin"); prev_prev_prev_target.innerHTML = "сделать админом";
  }catch{null}
})
on('body', 'click', '.user_remove_anketa_advertiser', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete_advertiser/", "user_add_anketa_advertiser", "сделать рекламодателем");
})

// =======================================================================================
// ============================================================================================

on('body', 'click', '.user_add_admin', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/progs/add_admin/", "user_remove_admin", "админ - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_editor");
    next_target.classList.add("user_add_editor"); next_target.classList.remove("user_remove_editor"); next_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_moderator");
    next_next_target.classList.add("user_add_moderator"); next_next_target.classList.remove("user_remove_moderator"); next_next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    next_next_next_target = admin_span.nextElementSibling.nextElementSibling.nextElementSibling.querySelector(".user_remove_advertiser");
    next_next_next_target.classList.add("user_add_advertiser"); next_next_next_target.classList.remove("user_remove_advertiser"); next_next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_admin', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/delete_admin/", "user_add_admin", "сделать админом");
})

on('body', 'click', '.user_add_editor', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/progs/add_editor/", "user_remove_editor", "редактор - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_admin");
    prev_target.classList.add("user_add_admin"); prev_target.classList.remove("user_remove_admin"); prev_target.innerHTML = "сделать админом";
  }catch{null}
  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_moderator");
    next_target.classList.add("user_add_moderator"); next_target.classList.remove("user_remove_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_advertiser");
    next_next_target.classList.add("user_add_advertiser"); next_next_target.classList.remove("user_remove_advertiser"); next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_editor', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/delete_editor/", "user_add_editor", "сделать редактором");
})

on('body', 'click', '.user_add_moderator', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/progs/add_moderator/", "user_remove_moderator", "модератор - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_advertiser");
    next_target.classList.add("user_add_advertiser"); next_target.classList.remove("user_remove_advertiser"); next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_editor");
    prev_target.classList.add("user_add_editor"); prev_target.classList.remove("user_remove_editor"); prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_admin");
    prev_prev_target.classList.add("user_add_admin"); prev_prev_target.classList.remove("user_remove_admin"); prev_prev_target.innerHTML = "сделать админом";
  }catch{null}

})
on('body', 'click', '.user_remove_moderator', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/delete_moderator/", "user_add_moderator", "сделать модератор");
})

on('body', 'click', '.user_add_advertiser', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/progs/add_advertiser/", "user_remove_advertiser", "рекламодатель - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_moderator");
    prev_target.classList.add("user_add_moderator"); next_target.classList.remove("user_remove_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_editor");
    prev_prev_target.classList.add("user_add_editor"); prev_prev_target.classList.remove("user_remove_editor"); prev_prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_prev_target = admin_span.previousElementSibling.previousElementSibling.previousElementSibling.querySelector(".user_remove_admin");
    prev_prev_prev_target.classList.add("user_add_admin"); prev_prev_prev_target.classList.remove("user_remove_admin"); prev_prev_prev_target.innerHTML = "сделать админом";
  }catch{null}
})
on('body', 'click', '.user_remove_advertiser', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/delete_advertiser/", "user_add_advertiser", "сделать рекламодателем");
})

// =======================================================================================
// ============================================================================================

on('body', 'click', '.user_add_anketa_admin', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/love_progs/add_admin/", "user_remove_anketa_admin", "админ - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_anketa_editor");
    next_target.classList.add("user_add_anketa_editor"); next_target.classList.remove("user_remove_anketa_editor"); next_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_anketa_moderator");
    next_next_target.classList.add("user_add_anketa_moderator"); next_next_target.classList.remove("user_remove_anketa_moderator"); next_next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    next_next_next_target = admin_span.nextElementSibling.nextElementSibling.nextElementSibling.querySelector(".user_remove_anketa_advertiser");
    next_next_next_target.classList.add("user_add_anketa_advertiser"); next_next_next_target.classList.remove("user_remove_anketa_advertiser"); next_next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_anketa_admin', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete_admin/", "user_add_anketa_admin", "сделать админом");
})

on('body', 'click', '.user_add_anketa_editor', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/love_progs/add_editor/", "user_remove_anketa_editor", "редактор - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_anketa_admin");
    prev_target.classList.add("user_add_anketa_admin"); prev_target.classList.remove("user_remove_anketa_admin"); prev_target.innerHTML = "сделать админом";
  }catch{null}
  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_anketa_moderator");
    next_target.classList.add("user_add_anketa_moderator"); next_target.classList.remove("user_remove_anketa_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_anketa_advertiser");
    next_next_target.classList.add("user_add_anketa_advertiser"); next_next_target.classList.remove("user_remove_anketa_advertiser"); next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
})
on('body', 'click', '.user_remove_anketa_editor', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete_editor/", "user_add_anketa_editor", "сделать редактором");
})

on('body', 'click', '.user_add_anketa_moderator', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/love_progs/add_moderator/", "user_remove_anketa_moderator", "модератор - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_anketa_advertiser");
    next_target.classList.add("user_add_anketa_advertiser"); next_target.classList.remove("user_remove_anketa_advertiser"); next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_anketa_editor");
    prev_target.classList.add("user_add_anketa_editor"); prev_target.classList.remove("user_remove_anketa_editor"); prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_anketa_admin");
    prev_prev_target.classList.add("user_add_anketa_admin"); prev_prev_target.classList.remove("user_remove_anketa_admin"); prev_prev_target.innerHTML = "сделать админом";
  }catch{null}

})
on('body', 'click', '.user_remove_anketa_moderator', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete_moderator/", "user_add_anketa_moderator", "сделать модератор");
})

on('body', 'click', '.user_add_anketa_advertiser', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/love_progs/add_advertiser/", "user_remove_anketa_advertiser", "рекламодатель - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_anketa_moderator");
    prev_target.classList.add("user_add_anketa_moderator"); next_target.classList.remove("user_remove_anketa_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_anketa_editor");
    prev_prev_target.classList.add("user_add_anketa_editor"); prev_prev_target.classList.remove("user_remove_anketa_editor"); prev_prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_prev_target = admin_span.previousElementSibling.previousElementSibling.previousElementSibling.querySelector(".user_remove_anketa_admin");
    prev_prev_prev_target.classList.add("user_add_anketa_admin"); prev_prev_prev_target.classList.remove("user_remove_anketa_admin"); prev_prev_prev_target.innerHTML = "сделать админом";
  }catch{null}
})
on('body', 'click', '.user_remove_anketa_advertiser', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete_advertiser/", "user_add_anketa_advertiser", "сделать рекламодателем");
})

// =======================================================================================
// ============================================================================================

on('body', 'click', '.user_add_course_admin', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/skill_progs/add_admin/", "user_remove_course_admin", "админ - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_course_editor");
    next_target.classList.add("user_add_course_editor"); next_target.classList.remove("user_remove_course_editor"); next_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_moderator");
    next_next_target.classList.add("user_add_course_moderator"); next_next_target.classList.remove("user_remove_course_moderator"); next_next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    next_next_next_target = admin_span.nextElementSibling.nextElementSibling.nextElementSibling.querySelector(".user_remove_course_advertiser");
    next_next_next_target.classList.add("user_add_course_advertiser"); next_next_next_target.classList.remove("user_remove_course_advertiser"); next_next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
  try{
    next_next_next_next_target = admin_span.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.querySelector(".user_remove_course_teacher");
    next_next_next_next_target.classList.add("user_add_course_teacher"); next_next_next_next_target.classList.remove("user_remove_course_teacher"); next_next_next_next_target.innerHTML = "сделать учителем";
  }catch{null}
})
on('body', 'click', '.user_remove_course_admin', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/delete_admin/", "user_add_course_admin", "сделать админом");
})

on('body', 'click', '.user_add_course_editor', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/skill_progs/add_editor/", "user_remove_course_editor", "редактор - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_course_admin");
    prev_target.classList.add("user_add_course_admin"); prev_target.classList.remove("user_remove_course_admin"); prev_target.innerHTML = "сделать админом";
  }catch{null}
  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_course_moderator");
    next_target.classList.add("user_add_course_moderator"); next_target.classList.remove("user_remove_course_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_course_advertiser");
    next_next_target.classList.add("user_add_course_advertiser"); next_next_target.classList.remove("user_remove_course_advertiser"); next_next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
  try{
    next_next_next_target = admin_span.nextElementSibling.nextElementSibling.nextElementSibling.querySelector(".user_remove_course_teacher");
    next_next_next_target.classList.add("user_add_course_teacher"); next_next_next_target.classList.remove("user_remove_course_teacher"); next_next_next_target.innerHTML = "сделать учителем";
  }catch{null}
})
on('body', 'click', '.user_remove_course_editor', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/delete_editor/", "user_add_course_editor", "сделать редактором");
})

on('body', 'click', '.user_add_course_moderator', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/skill_progs/add_moderator/", "user_remove_course_moderator", "модератор - разжаловать");

  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_course_advertiser");
    next_target.classList.add("user_add_course_advertiser"); next_target.classList.remove("user_remove_course_advertiser"); next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
  try{
    next_next_target = admin_span.nextElementSibling.nextElementSibling.querySelector(".user_remove_course_teacher");
    next_next_target.classList.add("user_add_course_teacher"); next_next_target.classList.remove("user_remove_course_teacher"); next_next_target.innerHTML = "сделать учителем";
  }catch{null}
  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_course_editor");
    prev_target.classList.add("user_add_course_editor"); prev_target.classList.remove("user_remove_course_editor"); prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_course_admin");
    prev_prev_target.classList.add("user_add_course_admin"); prev_prev_target.classList.remove("user_remove_course_admin"); prev_prev_target.innerHTML = "сделать админом";
  }catch{null}

})
on('body', 'click', '.user_remove_course_moderator', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/delete_moderator/", "user_add_course_moderator", "сделать модератор");
})

on('body', 'click', '.user_add_course_advertiser', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/skill_progs/add_advertiser/", "user_remove_course_advertiser", "рекламодатель - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_course_moderator");
    prev_target.classList.add("user_add_course_moderator"); next_target.classList.remove("user_remove_course_moderator"); next_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_course_editor");
    prev_prev_target.classList.add("user_add_course_editor"); prev_prev_target.classList.remove("user_remove_course_editor"); prev_prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_prev_target = admin_span.previousElementSibling.previousElementSibling.previousElementSibling.querySelector(".user_remove_course_admin");
    prev_prev_prev_target.classList.add("user_add_course_admin"); prev_prev_prev_target.classList.remove("user_remove_course_admin"); prev_prev_prev_target.innerHTML = "сделать админом";
  }catch{null}
  try{
    next_target = admin_span.nextElementSibling.querySelector(".user_remove_course_teacher");
    next_target.classList.add("user_add_course_teacher"); next_target.classList.remove("user_remove_course_teacher"); next_target.innerHTML = "сделать учителем";
  }catch{null}
})
on('body', 'click', '.user_remove_course_advertiser', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/delete_advertiser/", "user_add_course_advertiser", "сделать рекламодателем");
})

on('body', 'click', '.user_add_course_teacher', function(e) {
  e.preventDefault();
  admin_span = this.parentElement.parentElement;
  send_change(this, "/users/skill_progs/add_teacher/", "user_remove_course_teacher", "учитель - разжаловать");

  try{
    prev_target = admin_span.previousElementSibling.querySelector(".user_remove_course_advertiser");
    prev_target.classList.add("user_add_course_advertiser"); next_target.classList.remove("user_remove_course_advertiser"); next_target.innerHTML = "сделать рекламодателем";
  }catch{null}
  try{
    prev_prev_target = admin_span.previousElementSibling.previousElementSibling.querySelector(".user_remove_course_moderator");
    prev_prev_target.classList.add("user_add_course_moderator"); prev_prev_target.classList.remove("user_remove_course_moderator"); prev_prev_target.innerHTML = "сделать модератором";
  }catch{null}
  try{
    prev_prev_prev_target = admin_span.previousElementSibling.previousElementSibling.previousElementSibling.querySelector(".user_remove_course_editor");
    prev_prev_prev_target.classList.add("user_add_course_editor"); prev_prev_prev_target.classList.remove("user_remove_course_editor"); prev_prev_prev_target.innerHTML = "сделать редактором";
  }catch{null}
  try{
    prev_prev_prev_prev_target = admin_span.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.querySelector(".user_remove_course_admin");
    prev_prev_prev_prev_target.classList.add("user_add_course_admin"); prev_prev_prev_prev_target.classList.remove("user_remove_course_admin"); prev_prev_prev_prev_target.innerHTML = "сделать админом";
  }catch{null}
})
on('body', 'click', '.user_remove_course_teacher', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/delete_teacher/", "user_add_course_teacher", "сделать учителем");
})

// =======================================================================================
// ============================================================================================
