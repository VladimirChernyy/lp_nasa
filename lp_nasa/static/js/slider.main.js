$(document).ready(function () {
    lightbox.option({
        resizeDuration: 200,
        wrapAround: true,
        alwaysShowNavOnTouchDevices: true,
    });
    $(".sliders").slick({
        slidesToShow: 5,
        infinite: true,
        slidesToScroll: 1,
        centerMode: true,
        variableWidth: true,
        focusOnSelect: true,
        prevArrow: '<button type="button" class="btn slider-btn slider-prev"><img src="static/img/prev.svg" alt="arrow-left"></button>',
        nextArrow: '<button type="button" class="btn slider-btn slider-next"><img src="static/img/next.svg" alt="arrow-right"></button>',
        asNavFor: '.sliders-two',
        responsive: [
            {
                breakpoint: 600,
                settings: {
                    centerMode: true,
                    slidesToShow: 3,
                    arrows: false
                }
            },
        ],
    })

    $(".sliders-two").slick({
        infinite: true,
        centerMode: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: '.sliders',
        fade: true,
        arrows: false,
    })
});
