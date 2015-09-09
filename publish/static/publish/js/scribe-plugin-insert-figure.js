define(function () {

  /**
   * This plugin adds a command for toggling classes on paragraphs.
   */

  'use strict';

  return function () {
    return function (scribe) {
      function insertFigure() {}

      insertFigure.execute = function () {
        console.log('execute');

        if (this.queryEnabled()) {
          //var selection = new scribe.api.Selection();
          //var parentNode = selection.getContaining(function (node) {
              //return node.nodeName === 'P';
          //});

          //if (this.queryState()) {
            //document.execCommand("insertHTML", false, "</p><figure><img src='http://s2.lemde.fr/image/2015/09/02/312x156/4743562_3_df72_juge-trop-obese-et-trop-complexe-le-code-du_903574334bff8b418c00af196bac15dc.jpg' /><figcaption>Ici la légende</figcaption></figure><p>");
            document.execCommand("insertParagraph", false, "</p><figure><img src='http://s2.lemde.fr/image/2015/09/02/312x156/4743562_3_df72_juge-trop-obese-et-trop-complexe-le-code-du_903574334bff8b418c00af196bac15dc.jpg' /><figcaption>Ici la légende</figcaption></figure>");
          //} else {
            ////
          //}
        }
      };

      insertFigure.queryState = function () {
        /* Returns whether or not the specified command is already applied on
         * current selection */

        console.log('querystate');

        var selection = new scribe.api.Selection();
        var ret = selection.getContaining(function (node) {
          return node.nodeName === 'FIGURE';
        });

        console.log(ret);


        return ret;
      };

      insertFigure.queryEnabled = function () {
        /* Returns whether the execution of the specified command can be
         * successful, using the execCommand method. */

        // The command can be successful if it is happens inside a paragraph
        // The command can not be successful if it is happens inside a figure

        console.log('queryenabled');

        var selection = new scribe.api.Selection();
        var ret = !! selection.getContaining(function (node) {
          return node.nodeName === 'P';
        });

        console.log(ret);

        return ret;
      };

      scribe.commands['insertFigure'] = insertFigure;
    };
  };

});
