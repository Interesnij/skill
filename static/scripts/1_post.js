
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
