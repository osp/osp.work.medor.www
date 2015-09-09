define("scribe-plugin-toolbar-popover",
  ["exports"],
  function(__exports__) {
    "use strict";
    __exports__["default"] = function(popoverName, popoverLayer) {
        return function(scribe) {
            popoverLayer.style.display = 'none';
            popoverLayer.style.position = 'absolute';
            popoverLayer.style.left = 0;

            popoverLayer.parentNode.addEventListener('mouseleave', function() {
                popoverLayer.style.display = 'none';
            });

            var popover = new scribe.api.Command('popover');

            popover.execute = function() {
                var display = popoverLayer.style.display;

                if (this.queryState()) {
                    popoverLayer.style.display = 'none';
                } else {
                    popoverLayer.style.display = 'block';
                }
            };

            popover.queryState = function() {
                return popoverLayer.style.display !== 'none';
            };

            popover.queryEnabled = function() {
                return popoverLayer.querySelector('button:not([disabled])') !== null;
            };

            scribe.commands['popover' + popoverName] = popover;
        };
    }
  });