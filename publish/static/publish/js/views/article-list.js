define([
    'underscore', 
    'backbone',
    'js/views/partials/article-item',
    'text!js/templates/article-list.html'
], function (
    _, 
    backbone,
    ArticleItemView,
    articleListTemplate
) {
    'use strict';

    return Backbone.View.extend({
        el: 'main',
        events: {
            'click .add-article': function() {
                this.collection.create({
                    title: 'Super coolos',
                    body: 'Yes'
                });
            },
        },
        template: _.template(articleListTemplate),
        render: function() {
            this.$el.html(articleListTemplate);

            var that = this;
            var $ul = this.$el.find('.articles')

            $ul.empty();

            this.collection.each(function(model) {
                var view = new ArticleItemView({model: model});
                that.$el.append(view.$el);
                view.render();
            }); 
        },
        initialize: function() {
            this.listenTo(this.collection, 'all', function(event) { console.log(event); });
            this.listenTo(this.collection, 'sync', this.render);
        }
    });
});
