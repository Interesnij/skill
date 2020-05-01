on('body', 'click', '.user_subscribe', function(e) {
  e.preventDefault();
  parent = this.parent;
  send_change(this, "/users/progs/subscribe/", "user_unsubscribe", "Отписаться");
  try{
    target = parent.nextElementSibling.querySelector(".user_unblock");
    send_change(target, "/users/progs/unblock/", "user_unsubscribe", "Отписаться")
  }catch{null}
})

on('body', 'click', '.user_unsubscribe', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/unsubscribe/", "user_subscribe", "Подписаться");
})

on('body', 'click', '.user_block', function(e) {
  e.preventDefault();
  parent = this.parent;
  send_change(this, "/users/progs/block/", "user_unblock", "Разблокировать");
  try{
  target = parent.previousElementSibling.querySelector(".user_unsubscribe");
  target.classList.add("user_subscribe");
  target.classList.remove("user_unsubscribe");
  target.innerHTML = "Подписаться";
  }catch{null}
})

on('body', 'click', '.user_unblock', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/unblock/", "user_block", "Заблокировать")
})
