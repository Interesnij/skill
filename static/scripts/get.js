
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

$(".background-image").each(function() {
      $(this).css("background-image", "url("+ $(this).find("img").attr("src") +")" );
    });

document.body.querySelectorAll('.background-image').forEach(
  adres = this.querySelector("img").getAttribute("src");
  this.style.backgroundImage = "url(" + adres +")";
   )}
