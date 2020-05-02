

on('body', 'click', '#image-holder', function() {
img = this;
entrou = false;
var imageLoader = document.getElementById("id_image");
imageLoader.click();
on('#ajax', 'change', imageLoader, function() {
  if (!entrou) {
    imgPath = this.value;
    extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();
    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg")
    {if (typeof FileReader != "undefined") {
      image_holder = this;
      image_holder.innerHTML = "";
      reader = new FileReader();
      reader.onload = function(e) {
        $img = document.createElement("img"),
        $img.id = "targetImageCrop";
        $img.src = e.target.result;
        $img.class = "thumb-image";
        image_holder.append($img)
        image_holder.style.display == "none";
      }
        reader.readAsDataURL(this.files);
    }
     else {this.value = null;}
  } entrou = true;
  setTimeout(function() { entrou = false; }, 1000);
  this.previousElementSibling.previousElementSibling.style.display == "block";
}
}});
});
