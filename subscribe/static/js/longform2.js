function remy(target) {          
    // Avoids Capitalized short words (2 to 3 characters) to be alone
    pattern = /(\b[A-Z].{0,2}|, .{0,3}) /g;
    text = target.html();          
    target.html(text.replace(pattern, '$1 ')); // I actually put a non-breaking space charcter after $1! You don’t see it, but it’s there. This is to not have this &nbsp; value pop up in places.
}    


$(function() {
    remy($("main"));

    Modernizr.load({
        test: Modernizr.details,
        yep : '/static/components/details-tag/jquery.details.js',
    });

    $('.jcarousel').jcarousel({});

    $('.jcarousel-control-prev')
    .jcarouselControl({
        target: '-=1',
    });

    $('.jcarousel-control-next')
    .jcarouselControl({
        target: '+=1',
    });

    
    // SCROLL MAGIC !
    var controller = new ScrollMagic({loglevel: 3});

    //var contentIn = TweenMax.to("#cover-content", 0.000001, {left: "0px", autoAlpha: 1});
    //var contentOut = TweenMax.to("#cover-content", 0.000001, {left: "-500px", autoAlpha: 0});
    var detailIn = TweenMax.to("#cover-detail", 0.000001, {left: "0px", autoAlpha: 1});
    var detailOut = TweenMax.to("#cover-detail", 0.000001, {left: "-500px", autoAlpha: 0});
    var coopIn = TweenMax.to("#cover-coop", 0.000001, {left: "0px", autoAlpha: 1});
    var coopOut = TweenMax.to("#cover-coop", 0.000001, {left: "-500px", autoAlpha: 0});
    var budgetIn = TweenMax.to("#cover-budget", 0.000001, {left: "0px", autoAlpha: 1});
    var budgetOut = TweenMax.to("#cover-budget", 0.000001, {left: "-500px", autoAlpha: 0});

    new ScrollScene({triggerElement: "#magazine", duration: 1200, offset: -100, loglevel: 3})
        .setTween(detailIn)
        .addTo(controller);
        //.addIndicators();

    new ScrollScene({triggerElement: "#collaborative-experience", duration: 1200, offset: -300})
        .setTween(detailOut)
        .addTo(controller);
        //.addIndicators();

    new ScrollScene({triggerElement: "#collaborative-experience", duration: 1200, offset: -100})
        .setTween(coopIn)
        .addTo(controller);
        //.addIndicators();

    new ScrollScene({triggerElement: "#accounting", duration: 1200, offset: -300})
        .setTween(coopOut)
        .addTo(controller);
        //.addIndicators();

    new ScrollScene({triggerElement: "#accounting", duration: 1200, offset: -100})
        .setTween(budgetIn)
        .addTo(controller);
        //.addIndicators();

    new ScrollScene({triggerElement: "#status", duration: 1200, offset: -300})
        .setTween(budgetOut)
        .addTo(controller);
        //.addIndicators();
    

    /* The code below is loosely based on https://github.com/renettarenula/anchorific.js 
     * Copyright: Ren Aysha, MIT License. See <http://opensource.org/licenses/MIT>
     * */
    var prev;
    var headers = $($('#menu a').map(function() {return $($(this).attr('href')).get()}));
        
    $( window ).scroll( function( e ) {
        // get all the header on top of the viewport
        current = headers.map( function( e ) {
            if ( ( $( this ).offset().top - $( window ).scrollTop() ) < 1 ) {
                return this;
            }
        });
        // get only the latest header on the viewport
        current = $( current ).eq( current.length - 1 );

        if ( current && current.length ) {
            // get all li tag that contains href of # ( all the parents )
            list = $( '#menu li:has(a[href="#' + current.attr( 'id' ) + '"])' );

            if ( prev !== undefined ) {
                prev.removeClass( 'active' );
            }

            list.addClass( 'active' );
            prev = list;
        }
    });
});
