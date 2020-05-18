
function send_change(a, _link, new_class, html){
  parent = a.parentElement;
  item = a.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', _link + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    new_span = document.createElement("span");
    new_span.classList.add(new_class);
    new_span.innerHTML = html;
    parent.innerHTML = "";
    parent.append(new_span);
  }};
  link.send( null );
}

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
       document.querySelector(".special_block").previousElementSibling.style.display = "none";
       document.querySelector(".special_block").nextElementSibling.style.display = "none";}
    catch{null}
  }
  else{
    console.log(upload_block);
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
    subcat_block.style.display = "none";
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
  var top_forms = special_block.previousElementSibling;
  var bottom_forms = special_block.nextElementSibling;
  if (pk == ""){
    special_block.innerHTML = "";
    special_block.style.display = "none";
    top_forms.style.display = "none";
    bottom_forms.style.display = "none";}
  else{
    special_block.innerHTML = "";
    new_load(special_block, '/posts/form_special/' + pk);
    special_block.style.display = "block";
    top_forms.style.display = "block";
    bottom_forms.style.display = "block"
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

function load_chart() {
  try{
var ctx = document.getElementById('canvas');
var dates = ctx.getAttribute('data-dates').split(",");
var data_1 = ctx.getAttribute('data-data_1').split(",");
var data_2 = ctx.getAttribute('data-data_2').split(",");
var label_1 = ctx.getAttribute('data-label_1');
var label_2 = ctx.getAttribute('data-label_2');

var config = {
type: 'line',
data: {
  labels: dates,
  datasets: [{
    label: label_1,
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    data: data_1,
    fill: false,
  }, {
    label: label_2,
    fill: false,
    backgroundColor: 'rgb(54, 162, 235)',
    borderColor: 'rgb(54, 162, 235)',
    data: data_2,
  }]
},
options: {
  responsive: true,
  title: {display: true,text: ''},
  tooltips: {mode: 'index',intersect: false,},
  hover: {mode: 'nearest',intersect: true},
  scales: {
  xAxes: [{display: true,scaleLabel: {display: true,labelString: ''}}],
  yAxes: [{display: true,scaleLabel: {display: true,labelString: ''}}]
  }
}
};

ctx.getContext('2d');window.myLine = new Chart(ctx, config);
}catch{return}
}
