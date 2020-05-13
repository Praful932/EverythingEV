$(window).scroll(function() {
    if ($(window).scrollTop() > 205) {
        $('nav').addClass("sticky");
    } else {
        $('nav').removeClass("sticky");
    }
});

//----------------------------------------------
$(".single-item").slick({
    autoplay: true,
    autoplaySpeed: 2000,
    dots: false
});
$('.responsive').slick({
    dots: false,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 4000,
    speed: 800,
    slidesToShow: 3,
    slidesToScroll: 4,
    responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
                dots: true
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }
    ]
});

//----------------------------------------------------

$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });
    $('.scrollup').click(function() {
        $("html, body").animate({
            scrollTop: 10
        }, 600);
        return false;
    });
});

//--------------------------------------------------
$('.counter').each(function() {
    var $this = $(this),
        countTo = $this.attr('data-count');

    $({ countNum: $this.text() }).animate({
        countNum: countTo
    }, {
        duration: 8000,
        easing: 'linear',
        step: function() {
            $this.text(Math.floor(this.countNum));
        },
        complete: function() {
            $this.text(this.countNum);
            //alert('finished');
        }
    });
});
//---------------------------------------------------
$('.mah').slick({
    dots: false,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 4000,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 4,
    responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 4,
                infinite: true,
                dots: false
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        }
    ]
});
//----------------------------------------------------

$(document).ready(function() {
    $('.nav-icn').on('click', function() {
        $('.navigation').addClass('navigation-show');
        $('.modal-shade').addClass('modal-shade-show');
    })
    $('.modal-shade').on('click', function() {
        $('.navigation').removeClass('navigation-show');
        $('.modal-shade').removeClass('modal-shade-show');
    })
})