
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
function get_image(){
  document.body.querySelectorAll('.background-image').forEach(box => {
  adres = box.querySelector("img").getAttribute("src");
  box.style.backgroundImage = "url(" + adres +")";
  })
}

on('body', 'click', '.change-class', function(e) {
  e.preventDefault();
  _this = this;

  parentClass = "." + _this.getAttribute("data-parent-class");
  remove_class = _this.getAttribute("data-change-from-class");

  parent = document.body.querySelector(parentClass);
  parent.classList.remove(remove_class);
  parent.classList.add(_this.getAttribute("data-change-to-class"));
  all_tabs = _this.parentElement.querySelectorAll(".change-class");
  for (var i = 0; i < all_tabs.length; i++) {
    if(all_tabs[i].classList.contains("active")){
      all_tabs[i].classList.remove("active");
  }};
  _this.classList.add("active");
});

class Index {
  // класс, работающий с подгрузкой блоков на сайте. Смена основного блока, листание отдельных элементов, и т.д.
  static initLink() {document.body.querySelectorAll('.ajax').forEach( lin => lin.addEventListener('click', Index.push_url) );}
  static push_url(event){
    event.preventDefault();
    var ajax_link, url;
    ajax_link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
    url = this.getAttribute('href');
    if (url != window.location.pathname){
      ajax_link.open( 'GET', url, true );
      ajax_link.onreadystatechange = function () {
        if ( this.readyState == 4 && this.status == 200 ) {
          var rtr, elem_, ajax;
          rtr = document.getElementById('ajax');
          elem_ = document.createElement('span');
          elem_.innerHTML = ajax_link.responseText;
          ajax = elem_.querySelector("#reload_block");
          rtr.innerHTML = ajax.innerHTML;
          document.title = elem_.querySelector('title').innerHTML;
          window.history.pushState({route: url}, "network", url);
          window.scrollTo(0,0);
          Index.initLink();
          get_image();
          load_chart();
        }
      }
      ajax_link.send();
    }
  };
}


Index.initLink();
get_image();
