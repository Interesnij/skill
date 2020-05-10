
on('body', 'click', '#image-holder', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_image");
img.click();

img.onchange = function() {
  if (!entrou) {imgPath = img.value;
    extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();
  if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg")
  {if (typeof FileReader != "undefined") {
    ggg.innerHTML = "";
    reader = new FileReader();
    reader.onload = function(e) {
      $img = document.createElement("img");
      $img.id = "targetImageCrop";
      $img.src = e.target.result;
      $img.class = "thumb-image";
      ggg.append($img)
      };
      reader.readAsDataURL($(this)[0].files[0]);
      console.log($(this)[0], $(this)[0].files[0])
    }
  } else { this.value = null; }
} entrou = true;
setTimeout(function() { entrou = false; }, 1000)
}});
