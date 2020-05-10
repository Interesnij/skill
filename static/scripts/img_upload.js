
  var imageLoader = document.getElementById("id_image");
var entrou = false;

$("body").on('click', '#image-holder', function() {
  $("#id_image").click();
  console.log("click!!!")
});

$("#id_image").on("change", function() {
  if (!entrou) {
    var imgPath = $(this)[0].value;
    var extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();

    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
      if (typeof FileReader != "undefined") {
        var image_holder = $("#image-holder");
        image_holder.empty();

        var reader = new FileReader();
        reader.onload = function(e) {
          $img = $("<img />", {
            id: "targetImageCrop",
            src: e.target.result,
            class: "thumb-image"
          }).appendTo(image_holder);
        };

        image_holder.show();
        reader.readAsDataURL($(this)[0].files[0]);
      }
    } else {
      this.value = null;
    }
  }
  entrou = true;
  setTimeout(function() {
    entrou = false;
  }, 1000);
});
