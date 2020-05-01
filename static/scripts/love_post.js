on('body', 'click', '.anketa_remove', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/delete/", "anketa_unremove", "Отмена")
})

on('body', 'click', '.anketa_unremove', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/undelete/", "anketa_remove", "Удалить")
})

on('body', 'click', '.anketa_active', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/active/", "anketa_unactive", "Активный")
})

on('body', 'click', '.anketa_unactive', function(e) {
  e.preventDefault();
  send_change(this, "/users/love_progs/unactive/", "anketa_active", "Черновик")
})
