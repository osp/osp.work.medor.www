define([
    'underscore', 
    'backbone',
    'js/models/article'
], function (_, backbone, ArticleModel) {
    'use strict';

    var ArticleCollection = Backbone.Collection.extend({
         url : "/articles",
         model : ArticleModel,
    });

    return ArticleCollection;
});
