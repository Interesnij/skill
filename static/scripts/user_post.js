on('body', 'click', '.user_subscribe', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/subscribe/", "user_unsubscribe", "Отписаться")
})

on('body', 'click', '.user_unsubscribe', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/unsubscribe/", "user_subscribe", "Подписаться")
})

on('body', 'click', '.user_block', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/block/", "user_unblock", "Разблокировать")
})

on('body', 'click', '.user_unblock', function(e) {
  e.preventDefault();
  send_change(this, "/users/progs/unblock/", "user_block", "Заблокировать")
})
