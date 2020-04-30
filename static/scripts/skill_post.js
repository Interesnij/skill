on('body', 'click', '.course_remove', function(e) {
  e.preventDefault();
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/skill_progs/delete/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("course_unremove");
    new_span.innerHTML = "Отмена";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.course_unremove', function(e) {
  e.preventDefault();
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/skill_progs/undelete/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("course_remove");
    new_span.innerHTML = "Удалить";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.course_active', function(e) {
  e.preventDefault();
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/skill_progs/active/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("course_unactive");
    new_span.innerHTML = "Активный";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.course_unactive', function(e) {
  e.preventDefault();
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/skill_progs/unactive/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("course_active");
    new_span.innerHTML = "Черновик";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})
