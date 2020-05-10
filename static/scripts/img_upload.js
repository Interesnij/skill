$('body').on('click', '#image-holder', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_image");
img.click();
 $(img).on("change", function() {
  if (!entrou) {imgPath = $(this)[0].value;
    extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();
  if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg")
  {if (typeof FileReader != "undefined") {
    ggg.innerHTML = "";
    reader = new FileReader();
    reader.onload = function(e) {
      $img = $("<img />", {
        id: "targetImageCrop",
        src: e.target.result,
        class: "thumb-image" }).appendTo(ggg);
      };
      //ggg.show();
      reader.readAsDataURL($(this)[0].files[0]);
    }
  } else { this.value = null; }
} entrou = true;
setTimeout(function() { entrou = false; }, 1000)});
});
