define([
    'scribe',
    'scribe-plugin-blockquote-command',
    'scribe-plugin-code-command',
    'scribe-plugin-curly-quotes',
    'scribe-plugin-formatter-plain-text-convert-new-lines-to-html',
    'scribe-plugin-heading-command',
    'scribe-plugin-intelligent-unlink-command',
    'scribe-plugin-keyboard-shortcuts',
    'scribe-plugin-link-prompt-command',
    'scribe-plugin-sanitizer',
    'scribe-plugin-smart-lists',
    'scribe-plugin-toolbar',
    'scribe-plugin-content-cleaner',
    'underscore', 
    'backbone'
], function (
    Scribe,
    scribePluginBlockquoteCommand,
    scribePluginCodeCommand,
    scribePluginCurlyQuotes,
    scribePluginFormatterPlainTextConvertNewLinesToHtml,
    scribePluginHeadingCommand,
    scribePluginIntelligentUnlinkCommand,
    scribePluginKeyboardShortcuts,
    scribePluginLinkPromptCommand,
    scribePluginSanitizer,
    scribePluginSmartLists,
    scribePluginToolbar,
    scribePluginContentCleaner,
    _, 
    backbone
) {
    'use strict';

    var ArticleView = Backbone.View.extend({
        tagName: 'div',
        attributes: { class: 'scribe-editor' },
        events: {'input': function() {console.log('blabla')}},
        render: function() {
            $('body').append(this.$el);
        },
        initialize: function() {
            var scribe = new Scribe(this.el, { allowBlockElements: true });
            scribe.setContent(this.model.get('body'));

            //scribe.on('content-changed', (function(event) {
                //console.log("ok");
                //this.model.set('body', scribe.getHTML());
                //this.model.save();
            //}).bind(this));

            this.render();
        },
    });

    return ArticleView;
});
