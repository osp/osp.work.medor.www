
function init() {
    window.addEventListener('scroll', function(e){
        var distanceY = window.pageYOffset || document.documentElement.scrollTop,
        shrinkOn = 70,
            menu = document.querySelector(".menu");
        if (distanceY > shrinkOn) {
            classie.add(menu,"smaller");
        } else {
            if (classie.has(menu,"smaller")) {
                classie.remove(menu,"smaller");
            }
        }
    });
}
window.onload = init();
