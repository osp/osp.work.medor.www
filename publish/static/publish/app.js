define([
    'jquery',
    'underscore',
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
    'scribe-plugin-toolbar-popover',
    'scribe-plugin-toogle-class',
    'scribe-plugin-insert-figure'
], function (
    $,
    _,
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
    scribePluginToolbarPopover,
    scribePluginToogleClassCommand,
    scribePluginInsertFigure
) {
    'use strict';

    var initialize = function(){
        this.scribe = new Scribe($('.editor').get(0), { allowBlockElements: true });
        this.scribe.use(scribePluginHeadingCommand(2));
        this.scribe.use(scribePluginHeadingCommand(3));
        this.scribe.use(scribePluginContentCleaner());
        this.scribe.use(scribePluginCurlyQuotes());
        this.scribe.use(scribePluginLinkPromptCommand());

        // Formatters
        //this.scribe.use(scribePluginSanitizer({
            //tags: {
                //p: {},
                //br: {},
                //b: {},
                //strong: {},
                //i: {},
                //strike: {},
                //blockquote: {},
                //code: {},
                //ol: {},
                //ul: {},
                //li: {},
                //a: { href: true },
                //h2: {},
                //u: {},
                //figure: {},
                //figcaption: {},
                //img: {},
            //}
        //}));

        this.scribe.use(scribePluginToogleClassCommand('foo'));
        this.scribe.use(scribePluginToogleClassCommand('bar'));
        this.scribe.use(scribePluginInsertFigure());
        this.scribe.use(scribePluginToolbar(document.querySelector('.toolbar')));
        //window.alex = scribePluginToolbarPopover;
        //this.scribe.use(scribePluginToolbarPopover.default('foo', document.querySelector('.toolbar')));
    }

    return {
        initialize: initialize
    };
});
