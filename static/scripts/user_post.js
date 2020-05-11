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
