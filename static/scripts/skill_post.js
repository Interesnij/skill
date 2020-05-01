on('body', 'click', '.course_remove', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/delete/", "course_unremove", "Отмена")
})

on('body', 'click', '.course_unremove', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/undelete/", "course_remove", "Удалить")
})

on('body', 'click', '.course_active', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/active/", "course_unactive", "Активный")
})

on('body', 'click', '.course_unactive', function(e) {
  e.preventDefault();
  send_change(this, "/users/skill_progs/unactive/", "course_active", "Черновик")
})
