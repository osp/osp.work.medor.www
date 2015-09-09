define([
    'underscore', 
    'backbone',
    'js/models/article',
    'js/collections/article',
    'js/views/article-detail',
    'js/views/article-list',
], function (
    _, 
    backbone, 
    ArticleModel, 
    ArticleCollection, 
    ArticleDetailView, 
    ArticleListView
) {
    'use strict';

    var MainRouter = Backbone.Router.extend({
        routes: {
            "": "articleList", // matches http://example.com/
            "*slug": "articleDetail" // matches http://example.com/#anything-here
        }
    });

    var initialize = function(){
        // Initiate the router
        var app_router = new MainRouter;
        var currentView;

        app_router.on('route:articleList', function(action) {
            currentView && currentView.remove();

            var articleCollection = new ArticleCollection();
            currentView = new ArticleListView({collection: articleCollection});

            articleCollection.fetch();
        })

        app_router.on('route:articleDetail', function(action) {
            currentView && currentView.remove();

            var articleModel = new ArticleModel({_id: action});
            currentView = new ArticleDetailView({model: articleModel});

            articleModel.fetch();
        })

        // Start Backbone history a necessary step for bookmarkable URL's
        Backbone.history.start();
    };

    return {
        initialize: initialize
    };
});
