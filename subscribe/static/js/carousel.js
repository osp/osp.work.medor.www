$(function() {
    $('.jcarousel').jcarousel({
        //wrap: 'circular'
    });

    $('.jcarousel-control-prev')
    .jcarouselControl({
        target: '-=1',
    });

    $('.jcarousel-control-next')
    .jcarouselControl({
        target: '+=1',
    });
});
