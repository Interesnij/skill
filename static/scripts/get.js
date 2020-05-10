
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
  var parentClass = _this.getAttribute("data-parent-class");
  parentClass.classlist.remove(_this.getAttribute("data-change-from-class"));
  parentClass.classlist.add(_this.getAttribute("data-change-to-class"));
  _this.parentElement.querySelector(".change-class").classlist.remove("active");
  _this.classlist.add("active");
});
