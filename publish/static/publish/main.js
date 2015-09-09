// Filename: main.js

// Require.js allows us to configure shortcut alias
// There usage will become more apparent further along in the tutorial.
require.config({
    paths: {
        'scribe': './components/scribe/scribe',
        'scribe-plugin-blockquote-command': './components/scribe-plugin-blockquote-command/scribe-plugin-blockquote-command',
        'scribe-plugin-code-command': './components/scribe-plugin-code-command/scribe-plugin-code-command',
        'scribe-plugin-curly-quotes': './components/scribe-plugin-curly-quotes/scribe-plugin-curly-quotes',
        'scribe-plugin-formatter-plain-text-convert-new-lines-to-html': './components/scribe-plugin-formatter-plain-text-convert-new-lines-to-html/scribe-plugin-formatter-plain-text-convert-new-lines-to-html',
        'scribe-plugin-heading-command': './components/scribe-plugin-heading-command/scribe-plugin-heading-command',
        'scribe-plugin-intelligent-unlink-command': './components/scribe-plugin-intelligent-unlink-command/scribe-plugin-intelligent-unlink-command',
        'scribe-plugin-keyboard-shortcuts': './components/scribe-plugin-keyboard-shortcuts/scribe-plugin-keyboard-shortcuts',
        'scribe-plugin-link-prompt-command': './components/scribe-plugin-link-prompt-command/scribe-plugin-link-prompt-command',
        'scribe-plugin-sanitizer': './components/scribe-plugin-sanitizer/scribe-plugin-sanitizer',
        'scribe-plugin-smart-lists': './components/scribe-plugin-smart-lists/scribe-plugin-smart-lists',
        'scribe-plugin-toolbar': './components/scribe-plugin-toolbar/scribe-plugin-toolbar',
        'scribe-plugin-content-cleaner': './components/scribe-plugin-content-cleaner/scribe-plugin-content-cleaner',
        'scribe-plugin-toolbar-popover': './components/scribe-plugin-toolbar-popover/scribe-plugin-toolbar-popover',
        'jquery': './components/jquery/jquery',
        'underscore': './components/underscore/underscore',
        'backbone': './components/backbone/backbone',
        'text': './components/requirejs-text/text',

        'scribe-plugin-toogle-class': './js/scribe-plugin-toggle-class',
        'scribe-plugin-insert-figure': './js/scribe-plugin-insert-figure'
    }
});

require([
    // Load our app module and pass it to our definition function
    'app',
], function(App){
    // The "app" dependency is passed in as "App"
    App.initialize();
});
