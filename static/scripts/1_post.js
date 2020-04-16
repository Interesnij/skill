 on('body', 'click', '.ad_sold', function() {
   item = this.parentElement.parentElement.parentElement.parentElement;
   pk = item.getAttribute("data-pk");
   parent = this.parentElement;
   link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
   link.open( 'GET', "/users/ad_progs/sold/" + pk + "/", true );
   link.onreadystatechange = function () {
   if ( link.readyState == 4 && link.status == 200 ) {
     new_span = document.createElement("span");
     new_span.classList.add("ad_unsold");
     new_span.style.cursor = "pointer";
     new_span.innerHTML = "Продано";
     parent.innerHTML = "";
     parent.append(new_span);
   }};
   link.send( null );
})

on('body', 'click', '.ad_unsold', function() {
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/unsold/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("ad_sold");
    new_span.style.cursor = "pointer";
    new_span.innerHTML = "Не продано";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.ad_remove', function() {
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/delete/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("ad_unremove");
    new_span.style.cursor = "pointer";
    new_span.innerHTML = "Отмена";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.ad_unremove', function() {
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/undelete/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("ad_remove");
    new_span.style.cursor = "pointer";
    new_span.innerHTML = "Удалить";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.ad_active', function() {
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/active/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("ad_unactive");
    new_span.style.cursor = "pointer";
    new_span.innerHTML = "Видно";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})

on('body', 'click', '.ad_unactive', function() {
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/unactive/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("ad_active");
    new_span.style.cursor = "pointer";
    new_span.innerHTML = "Не видно";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})
