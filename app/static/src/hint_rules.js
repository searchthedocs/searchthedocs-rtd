define(function() {

  var hint_rules = {
    // Hint Rules take a hash of user tracking parameters to offer
    // hints to the user based on previous interactions.
    // Parameters:
    // - visits
    // - actions_performed (array)
    //
    // Returns a hash containing the metadata to display the hint.
    // For example:
    //
    search_hint: function(options) {
      var visits = options.visits;
      var searches = options.searches;
      if (
        visits === 1
        && _.isEmpty(searches)
      ) {
        return {
          "hint_method": "tooltip",
          "el": ".search-input-container",
          "remove_event": "content_loaded",
          "hint_options": {
            "title": "Start searching!",
            "placement": "bottom",
            "trigger": "manual",
          }
        };
      }
     },

    domain_completion_hint: function(options) {
      var searches = options.searches;
      var domain_completions = options.domain_completions;
      if (
        !_.isEmpty(searches)
        && _.isEmpty(domain_completions)
      ) {
        return {
          "hint_method": "inline",
          "el": "[data-view-name='suggestion-panel-container']",
          "remove_event": "domain_completion",
          "hint_options": {
            "title": "Hint! You can also tab-complete project filters",
          }
        };
      }
     },

  };

  return hint_rules;

});

