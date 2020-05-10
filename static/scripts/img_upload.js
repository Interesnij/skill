
  var imageLoader = document.getElementById("id_images");
var entrou = false;
$("#image-holder").on("click", function() {
  $("#id_image").click();
});

$("#id_images").on("change", function() {
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


  var imageLoader = document.getElementById("id_img1");
var entrou = false;
$("#image-holder1").on("click", function() {
  $("#id_img1").click();
});

$("#id_img1").on("change", function() {
  if (!entrou) {
    var imgPath = $(this)[0].value;
    var extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();

    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
      if (typeof FileReader != "undefined") {
        var image_holder = $("#image-holder1");
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


  var imageLoader = document.getElementById("id_img2");
var entrou = false;
$("#image-holder2").on("click", function() {
  $("#id_img2").click();
});

$("#id_img2").on("change", function() {
  if (!entrou) {
    var imgPath = $(this)[0].value;
    var extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();

    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
      if (typeof FileReader != "undefined") {
        var image_holder = $("#image-holder2");
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


  var imageLoader = document.getElementById("id_img3");
var entrou = false;
$("#image-holder3").on("click", function() {
  $("#id_img3").click();
});

$("#id_img3").on("change", function() {
  if (!entrou) {
    var imgPath = $(this)[0].value;
    var extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();

    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
      if (typeof FileReader != "undefined") {
        var image_holder = $("#image-holder3");
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


  var imageLoader = document.getElementById("id_img4");
var entrou = false;
$("#image-holder4").on("click", function() {
  $("#id_img4").click();
});

$("#id_img4").on("change", function() {
  if (!entrou) {
    var imgPath = $(this)[0].value;
    var extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();

    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
      if (typeof FileReader != "undefined") {
        var image_holder = $("#image-holder4");
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


  var imageLoader = document.getElementById("id_img5");
var entrou = false;
$("#image-holder5").on("click", function() {
  $("#id_img5").click();
});

$("#id_img5").on("change", function() {
  if (!entrou) {
    var imgPath = $(this)[0].value;
    var extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();

    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
      if (typeof FileReader != "undefined") {
        var image_holder = $("#image-holder5");
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


  var imageLoader = document.getElementById("id_img6");
var entrou = false;
$("#image-holder6").on("click", function() {
  $("#id_img6").click();
});

$("#id_img6").on("change", function() {
  if (!entrou) {
    var imgPath = $(this)[0].value;
    var extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();

    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
      if (typeof FileReader != "undefined") {
        var image_holder = $("#image-holder6");
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


  var imageLoader = document.getElementById("id_img7");
var entrou = false;
$("#image-holder7").on("click", function() {
  $("#id_img7").click();
});

$("#id_img7").on("change", function() {
  if (!entrou) {
    var imgPath = $(this)[0].value;
    var extn = imgPath.substring(imgPath.lastIndexOf(".") + 1).toLowerCase();

    if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
      if (typeof FileReader != "undefined") {
        var image_holder = $("#image-holder7");
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
