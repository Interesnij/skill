
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

$('body').on('click', '#image-holder', function() {
 img = $(this);
entrou = false;
 imageLoader = img.prev();
imageLoader.click();
 $(imageLoader).on("change", function() {
  if (!entrou) {imgPath = $(this)[0].value;
    extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();
  if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg")
  {if (typeof FileReader != "undefined") {
    image_holder = $(img);
    image_holder.empty();
    reader = new FileReader();
    reader.onload = function(e) {
      $img = $("<img />", {
        id: "targetImageCrop",
        src: e.target.result,
        class: "thumb-image" }).appendTo(image_holder);
      };
      image_holder.show();
      reader.readAsDataURL($(this)[0].files[0]);
    }
  } else { this.value = null; }
} entrou = true;
setTimeout(function() { entrou = false; }, 1000);
img.prev().prev().show();
console.log("upload comment image 2")});});
