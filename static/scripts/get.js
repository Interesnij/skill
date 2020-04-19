function on(elSelector,eventName,selector,fn) {var element = document.querySelector(elSelector);element.addEventListener(eventName, function(event) {var possibleTargets = element.querySelectorAll(selector);var target = event.target;for (var i = 0, l = possibleTargets.length; i < l; i++) {var el = target;var p = possibleTargets[i];while(el && el !== element) {if (el === p) {return fn.call(p, event);}el = el.parentNode;}}});};
function new_load(block,link) {
  var request = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  request.open( 'GET', link, true );
  request.onreadystatechange = function () {
    if ( request.readyState == 4 && request.status == 200 ) {
      block.innerHTML = request.responseText;
    }};
  request.send( null );
}

function SelectSubCategory (select) {
  var selectedOption = select.options[select.selectedIndex];
  var pk = selectedOption.value;
  var subcat_block = document.querySelector(".subcat");
  var upload_block = subcat_block.querySelector("#id_category");
  if (pk == ""){
    upload_block.innerHTML = "";
    subcat_block.style.display = "none";
    try{document.querySelector(".special_block").innerHTML = "";
       document.querySelector(".special_block").nextElementSibling.nextElementSibling.style.display = "none";
       document.querySelector(".special_block").nextElementSibling.style.display = "none";}
    catch{console.log("!")}
  }
  else{
    upload_block.innerHTML = "";
    new_load(upload_block, '/search/get_subcat/' + pk);
    subcat_block.style.display = "block";
  }
}
function loadCitySelect (select) {
  var selectedOption = select.options[select.selectedIndex];
  var pk = selectedOption.value;
  var subcat_block = document.querySelector(".city");
  var upload_block = subcat_block.querySelector("#id_city");
  if (pk == ""){
    upload_block.innerHTML = "";
  }
  else{
    upload_block.innerHTML = "";
    new_load(upload_block, '/cities/load/' + pk);
    subcat_block.style.display = "block";
  }
}

function loadAddForm (select) {
  var selectedOption = select.options[select.selectedIndex];
  var pk = selectedOption.value;
  var special_block = document.querySelector(".special_block");
  if (pk == ""){
    special_block.innerHTML = "";
    special_block.nextElementSibling.nextElementSibling.style.display = "none";
    special_block.nextElementSibling.style.display = "none";
    special_block.style.display = "none";}
  else{
    special_block.innerHTML = "";
    new_load(special_block, '/posts/form_special/' + pk);
    special_block.style.display = "block";
    special_block.nextElementSibling.style.display = "block";
    special_block.nextElementSibling.nextElementSibling.style.display = "block"
  }
}

function open_fullscreen(link, block) {
  var link_, elem;
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'GET', link, true );
  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    elem = link_.responseText;
    block.parentElement.style.display = "block";
    block.innerHTML = elem
  }};
  link_.send();
}

on('body', 'click', '.get_russia', function() {
  var loader
  loader = document.getElementById("russia_loader");
  open_fullscreen("/countries/load/1", loader)
});

on('body', 'click', '.russia_fullscreen_hide', function() {
  document.querySelector(".russia_fullscreen").style.display = "none";
  document.getElementById("russia_loader").innerHTML=""
});

on('body', 'click', '.more_search_fields', function(e) {
  e.preventDefault();
  this.nextElementSibling.classList.toggle("show");
});
