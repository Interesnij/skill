
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

on('body', 'click', '#image-holder', function() {
img = this;
entrou = false;
var imageLoader = document.querySelector("id_image");
imageLoader.click();
on('body', 'change', imageLoader, function() {
  if (!entrou) {
    imgPath = this.value;
    extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();
    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg")
    {if (typeof FileReader != "undefined") {
      image_holder = this;
      reader = new FileReader();
      reader.onload = function(e) {
        $img = document.createElement("img"),
        $img.id = "targetImageCrop";
        $img.src = e.target.result;
        $img.class = "thumb-image";
        image_holder.append($img);
        image_holder.style.display == "block";
      }
        reader.readAsDataURL(this.files);
    }
     else {this.value = null;}
  } entrou = true;
  setTimeout(function() { entrou = false; }, 1000);
}
});
});
