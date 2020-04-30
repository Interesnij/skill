on('body', 'click', '.anketa_remove', function(e) {
  e.preventDefault();
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/love_progs/delete/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("anketa_unremove");
    new_span.innerHTML = "Отмена";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.anketa_unremove', function(e) {
  e.preventDefault();
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/love_progs/undelete/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("anketa_remove");
    new_span.innerHTML = "Удалить";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.anketa_active', function(e) {
  e.preventDefault();
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/love_progs/active/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("anketa_unactive");
    new_span.innerHTML = "Активный";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.anketa_unactive', function(e) {
  e.preventDefault();
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/love_progs/unactive/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("anketa_active");
    new_span.innerHTML = "Черновик";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})
