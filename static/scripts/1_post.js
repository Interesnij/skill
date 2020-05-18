
 on('body', 'click', '.module_sold', function(e) {
   e.preventDefault();
   send_change(this, "/users/ad_progs/sold/", "module_unsold", "не продано")
})

on('body', 'click', '.module_unsold', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/unsold/", "module_sold", "продано")
})

on('body', 'click', '.module_remove', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/delete/", "module_unremove", "Отмена")
})

on('body', 'click', '.module_unremove', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/undelete/", "module_remove", "Удалить")
})

on('body', 'click', '.module_active', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/active/", "module_unactive", "деактивировать")
})

on('body', 'click', '.module_unactive', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/unactive/", "module_active", "активировать")
})

on('body', 'click', '.module_unactive', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/unactive/", "module_active", "активировать")
})

on('body', 'click', '.module_unfavorite', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/unfavorite/", "module_favorite", "Запомнить")
})
on('body', 'click', '.module_favorite', function(e) {
  e.preventDefault();
  send_change(this, "/users/ad_progs/favorite/", "module_unfavorite", "Забыть")
})

on('body', 'click', '.ad_like', function() {
  like = this;
  pk = document.getElementById("creator_pk").getAttribute("data-pk");
  uuid = document.querySelector(".page-title").getAttribute("data-uuid");
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/posts/votes/like/" + uuid + "/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    jsonResponse = JSON.parse(link.responseText);
    dislike = like.parentElement.nextElementSibling.querySelector(".ad_dislike");
    likes_count = like.querySelector(".likes_count");
    dislikes_count = dislike.querySelector(".dislikes_count");
    likes_count.innerHTML = jsonResponse.like_count;
    dislikes_count.innerHTML = jsonResponse.dislike_count;
    like.classList.toggle("btn_success");
    like.classList.toggle("btn_default");
    dislike.classList.add("btn_default");
    dislike.classList.remove("btn_danger");
  }};
  link.send( null );
})

on('body', 'click', '.ad_dislike', function() {
  dislike = this;
  pk = document.getElementById("creator_pk").getAttribute("data-pk");
  uuid = document.querySelector(".page-title").getAttribute("data-uuid");
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/posts/votes/dislike/" + uuid + "/" + pk + "/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    jsonResponse = JSON.parse(link.responseText);
    like = dislike.parentElement.previousElementSibling.querySelector(".ad_like");
    likes_count = like.querySelector(".likes_count");
    dislikes_count = dislike.querySelector(".dislikes_count");
    likes_count.innerHTML = jsonResponse.like_count;
    dislikes_count.innerHTML = jsonResponse.dislike_count;
    dislike.classList.toggle("btn_danger");
    dislike.classList.toggle("btn_default");
    like.classList.add("btn_default");
    like.classList.remove("btn_success");
  }};
  link.send( null );
})

on('body', 'click', '#create_post', function() {
  form_data = new FormData(document.querySelector("#login"));
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'POST', "/form_special/", true );
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    window.location.href = "/";
    }};
  link.send(form_data);
});


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

on('body', 'click', '#image-holder2', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_img2");
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

on('body', 'click', '#image-holder3', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_img3");
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

on('body', 'click', '#image-holder4', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_img4");
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

on('body', 'click', '#image-holder5', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_img5");
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

on('body', 'click', '#image-holder6', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_img6");
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

on('body', 'click', '#image-holder7', function() {
entrou = false;
ggg = this;
img = this.previousElementSibling.querySelector("#id_img7");
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
