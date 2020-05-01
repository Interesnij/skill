on('body', 'click', '.user_subscribe', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/subscribe/", "user_unsubscribe", "Отписаться");
  try{
    next_block = this.parent.nextElementSibling;
    target = next_block.querySelector(".user_unblock");
    send_change(target, "/users/progs/unblock/", "user_unsubscribe", "Отписаться");
})

on('body', 'click', '.user_unsubscribe', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/unsubscribe/", "user_block", "Заблокировать");
})

on('body', 'click', '.user_block', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/block/", "user_unblock", "Разблокировать");
  previous_block = this.parent.previousElementSibling;
  target = previous_block.querySelector(".user_unsubscribe");
  target.classList.add(".user_subscribe");
  target.classList.remove(".user_unsubscribe");
  target.innerHTML = "Подписаться";
})

on('body', 'click', '.user_unblock', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/unblock/", "user_block", "Заблокировать")
})
