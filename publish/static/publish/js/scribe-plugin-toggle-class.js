define(function () {

  /**
   * This plugin adds a command for toggling classes on paragraphs.
   */

  'use strict';

  return function (className) {
    return function (scribe) {
      function toggleClassCommand() {}

      toggleClassCommand.execute = function () {
        if (this.queryEnabled()) {
          var selection = new scribe.api.Selection();
          var parentNode = selection.getContaining(function (node) {
              return node.nodeName === 'P';
          });
          if (this.queryState()) {
            parentNode.classList.remove(className);
          } else {
            parentNode.classList.add(className);
          }
        }
      };

      toggleClassCommand.queryState = function () {
        /* Returns whether or not the specified command is already applied on
         * current selection */

        var selection = new scribe.api.Selection();
        var parentNode = selection.getContaining(function (node) {
          return node.nodeName === 'P';
        });

        return parentNode && parentNode.classList.contains(className);
      };

      toggleClassCommand.queryEnabled = function () {
        /* Returns whether the execution of the specified command can be
         * successful, using the execCommand method. */

        var selection = new scribe.api.Selection();
        return !! selection.getContaining(function (node) {
          return node.nodeName === 'P';
        });
      };

      scribe.commands['toggle-class-' + className] = toggleClassCommand;
    };
  };

});
