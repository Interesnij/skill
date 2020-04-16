 on('body', 'click', '.ad_sold', function(e) {
   e.preventDefault;
   item = this.parentElement.parentElement.parentElement.parentElement;
   pk = item.getAttribute("data-pk");
   parent = this.parentElement;
   link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
   link.open( 'GET', "/users/ad_progs/sold/" + pk + "/", true );
   link.onreadystatechange = function () {
   if ( link.readyState == 4 && link.status == 200 ) {
     new_a = document.createElement("a");
     new_a.setAttribute('href', "#");
     new_a.classList.add("ad_unsold");
     new_a.innerHTML = "Активировать";
     parent.innerHTML = "";
     parent.append(new_a);
   }};
   link.send( null );
})

on('body', 'click', '.ad_unsold', function(e) {
  e.preventDefault;
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/unsold/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_a = document.createElement("a");
    new_a.setAttribute('href', "#");
    new_a.classList.add("ad_sold");
    new_a.innerHTML = "Продано";
    parent.innerHTML = "";
    parent.append(new_a);
  }};
  link.send( null );
})

on('body', 'click', '.ad_remove', function(e) {
  e.preventDefault;
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/delete/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_a = document.createElement("a");
    new_a.setAttribute('href', "#");
    new_a.classList.add("ad_unremove");
    new_a.innerHTML = "Восстановить";
    parent.innerHTML = "";
    parent.append(new_a);
  }};
  link.send( null );
})

on('body', 'click', '.ad_unremove', function() {
  e.preventDefault;
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/undelete/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_a = document.createElement("a");
    new_a.setAttribute('href', "#");
    new_a.classList.add("ad_remove");
    new_a.innerHTML = "Удалить";
    parent.innerHTML = "";
    parent.append(new_a);
  }};
  link.send( null );
})
