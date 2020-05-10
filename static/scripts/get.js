
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

document.body.querySelectorAll('.background-image').forEach(box => {
  adres = box.querySelector("img").getAttribute("src");
  box.style.backgroundImage = "url(" + adres +")";
   })

//   $(".change-class").on("click", function(e){
//           e.preventDefault();
//           var parentClass = $( "."+$(this).attr("data-parent-class") );
//           parentClass.removeClass( $(this).attr("data-change-from-class") );
//           parentClass.addClass( $(this).attr("data-change-to-class") );
//           $(this).parent().find(".change-class").removeClass("active");
//           $(this).addClass("active");
//       });

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
    if(box[i].classList.contains("active")){
      box[i].classList.delete("active");
  }};
  _this.classList.add("active");
});
