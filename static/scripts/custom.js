
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

    if( $(".owl-carousel").length ){
        var galleryCarousel = $(".gallery-carousel");

        galleryCarousel.owlCarousel({
            loop: false,
            margin: 0,
            nav: true,
            items: 1,
            navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
            autoHeight: true,
            dots: false
        });

        $(".tabs-slider").owlCarousel({
            loop: false,
            margin: 0,
            nav: false,
            items: 1,
            autoHeight: true,
            dots: false,
            mouseDrag: true,
            touchDrag: false,
            pullDrag: false,
            freeDrag: false
        });

        $(".full-width-carousel").owlCarousel({
            loop: true,
            margin: 10,
            nav: true,
            items: 3,
            navText: ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
            autoHeight: false,
            center: true,
            dots: false,
            autoWidth:true,
            responsive: {
                768: {
                    items: 3
                },
                0 : {
                    items: 1,
                    center: false,
                    margin: 0,
                    autoWidth: false
                }
            }
        });

        $(".gallery-carousel-thumbs").owlCarousel({
            loop: false,
            margin: 20,
            nav: false,
            dots: true,
            items: 5,
            URLhashListener: true
        });

        $("a.owl-thumb").on("click", function () {
            $("a.owl-thumb").removeClass("active-thumb");
            $(this).addClass("active-thumb");
        });

        galleryCarousel.on('translated.owl.carousel', function() {
            var hash = $(this).find(".active").find("img").attr("data-hash");
            $(".gallery-carousel-thumbs").find("a[href='#" + hash + "']").trigger("click");
        });
    }
