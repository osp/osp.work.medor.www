function remy(target) {          
    // Avoids Capitalized short words (2 to 3 characters) to be alone
    pattern = /(\b[A-Z].{0,2}|, .{0,3}) /g;
    text = target.html();          
    target.html(text.replace(pattern, '$1 ')); // I actually put a non-breaking space charcter after $1! You don’t see it, but it’s there. This is to not have this &nbsp; value pop up in places.
}    


$(function() {
    remy($("main"));

    $("#menu").tocify({
        "selectors": "h2",
        "hashGenerator": "pretty",
        "highlightOffset": 10,
        "extendPage": false,
    });
    
    //if (Modernizr.details) {
        //console.log('support ok');
    //} else {
        //console.log('support not ok');
        //// script to run if local storage is not supported
    //}
    //Modernizr.load({
        //test: Modernizr.details,
        //yep : 'geo.js',
        //nope: 'geo-polyfill.js'
    //});

    //$('a[href^="#"]').click(function(){
        //var the_id = $(this).attr("href");
        //scrollTop = $('[id="' + the_id.substring(1) + '"]').position().top - 180;
        //console.log(scrollTop)
        //$('#main').mCustomScrollbar("scrollTo", scrollTop);
        ////$('#main').animate({
        ////    scrollTop:$('[id="' + the_id.substring(1) + '"]').offset().top,
        ////}, 1500);
        //return false;
    //});

    /*
    $.ajax({
        url: 'http://www.kisskissbankbank.com/fr/projects/the-french-fromage/widget',
        type: 'GET',
        success: function(res) {
            var html = $(res.responseText);
            var data = {
                amount: html.find('.amount strong').text(),
                goal: $.trim(html.find('.goal p').contents().filter(function() { return this.nodeType == 3 })[0].textContent),
                collected: $.trim(html.find('.collected p').contents().filter(function() { return this.nodeType == 3 })[0].textContent),
                timeLeft: html.find('.time-left').text(),
                bankers: html.find('.bankers').text()
            }

            var $elt = $('<dl>');

            for (var prop in obj) {
                $el.append($('<dt>').text(prop));
                $el.append($('<dd>').text(obj[prop]));
            }

            console.log($elt);

            $('header').append($elt);
        }
    });
    */
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

    
    // SCROLL MAGIC !
    var controller = new ScrollMagic();

    var contentIn = TweenMax.to("#cover-content", 0.000001, {left: "0px", autoAlpha: 1});
    var contentOut = TweenMax.to("#cover-content", 0.000001, {left: "-500px", autoAlpha: 0});
    var detailIn = TweenMax.to("#cover-detail", 0.000001, {left: "0px", autoAlpha: 1});
    var detailOut = TweenMax.to("#cover-detail", 0.000001, {left: "-500px", autoAlpha: 0});
    var coopIn = TweenMax.to("#cover-coop", 0.000001, {left: "0px", autoAlpha: 1});
    var coopOut = TweenMax.to("#cover-coop", 0.000001, {left: "-500px", autoAlpha: 0});
    var budgetIn = TweenMax.to("#cover-budget", 0.000001, {left: "0px", autoAlpha: 1});
    var budgetOut = TweenMax.to("#cover-budget", 0.000001, {left: "-500px", autoAlpha: 0});

    new ScrollScene({triggerElement: "#magazine", duration: 1200, offset: -100})
        .setTween(detailIn)
        .addTo(controller)

    new ScrollScene({triggerElement: "#collaborative-experience", duration: 1200, offset: -300})
        .setTween(detailOut)
        .addTo(controller)

    new ScrollScene({triggerElement: "#collaborative-experience", duration: 1200, offset: -100})
        .setTween(coopIn)
        .addTo(controller)

    new ScrollScene({triggerElement: "#accounting", duration: 1200, offset: -300})
        .setTween(coopOut)
        .addTo(controller)

    new ScrollScene({triggerElement: "#accounting", duration: 1200, offset: -100})
        .setTween(budgetIn)
        .addTo(controller)

    new ScrollScene({triggerElement: "#status", duration: 1200, offset: -300})
        .setTween(budgetOut)
        .addTo(controller)

});
