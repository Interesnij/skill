
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
      ggg.append($img);

      };
      reader.readAsDataURL(img.files[0]);
    }
  } else { this.value = null; }
} entrou = true;
setTimeout(function() { entrou = false; }, 1000);
ggg.parentElement.nextElementSibling.style.display = "block";
}});

on('body', 'click', '#image-holder1', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_img1");
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
      ggg.append($img);

      };
      reader.readAsDataURL(img.files[0]);
    }
  } else { this.value = null; }
} entrou = true;
setTimeout(function() { entrou = false; }, 1000);
ggg.parentElement.nextElementSibling.style.display = "block";
}});
