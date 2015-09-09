define([
    'underscore', 
    'backbone',
    'text!js/templates/article-detail.html',
    'scribe',
], function (
    _, 
    backbone,
    articleDetailTemplate,
    Scribe
) {
    'use strict';

    return Backbone.View.extend({
        el: 'main',
        events: {
            'click .save': function(event) {
                this.model.save('body', this.scribe.getHTML());
            }
        },
        render: function() {
            this.$el.html(articleDetailTemplate);

            this.scribe = new Scribe(this.$el.find('.editor').get(0), { allowBlockElements: true });
            this.scribe.setContent(this.model.get('body'));
        },
        initialize: function() {
            this.listenTo(this.model, 'sync', this.render);
            this.listenTo(this.model, 'all', function(event) { console.log(event); });
        }
    });
});
