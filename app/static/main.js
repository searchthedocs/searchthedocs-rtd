// Main Module for searchthedocs demo
define(function (require) {
  var _ = require('underscore'),
    $ = require('jquery'),
    SearchTheDocsView = require('searchthedocs/src/searchthedocs');

  var searchthedocs_main = function() {

    window.searchtd = new SearchTheDocsView({
      brand: 'searchthedocs',
      brand_href: '#'
    });

   $('#searchthedocs-container').append(searchtd.render().el);

  };

  return searchthedocs_main;

});

