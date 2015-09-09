define([
    'underscore', 
    'backbone',
    'text!js/templates/partials/article-item.html'
], function (_, backbone, template) {
    'use strict';

    return Backbone.View.extend({
        tagName: 'li',
        events: { 'click .delete': function() { this.model.destroy(); } },
        template: _.template(template),
        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
        },
        initialize: function() {
            this.listenTo(this.model, 'remove', this.remove);
        },
    });
});
