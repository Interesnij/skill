
$(document).ready(function($) {
    "use strict";

    $("select.change-tab").each(function(){
        var _this = $(this);
        if( $(this).find(".item").attr("data-value") !== "" ){
            changeTab( _this );
        }
    });
    $(".change-tab").on("change", function() {
        changeTab( $(this) );
    });
    $(".box").each(function(){
        if( $(this).find(".background .background-image").length ) {
            $(this).css("background-color","transparent");
        }
    });
