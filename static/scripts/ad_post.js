 on('#ajax', 'click', '.ad_sold', function() {
   item = this.parentElement.parentElement.parentElement.parentElement;
   pk = item.getAttribute("data-pk");
   parent = this.parentElement;
   link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
   link.open( 'GET', "/users/ad_progs/sold/" + pk + "/", true );
   link.onreadystatechange = function () {
   if ( link.readyState == 4 && link.status == 200 ) {
     new_span = document.createElement("span");
     new_span.classList.add("ad_unsold");
     new_span.innerHTML = "Восстановить";
     parent.innerHTML = "";
     parent.append(new_span);
   }};
   link.send( null );
})

on('#ajax', 'click', '.ad_unsold', function() {
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  parent = this.parentElement;
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/users/ad_progs/unsold/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add("ad_sold");
    new_span.innerHTML = "Удалить";
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
})
