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
      var visits = options.tracking_params.visits;
      var searches = options.tracking_params.searches;
      if (
        visits === 1
        && _.isEmpty(searches)
      ) {
        return {
          "hint_method": "tooltip",
          "el": ".search-input-container",
          "success_event": "content_loaded",
          "hint_options": {
            "title": "Start searching!",
            "placement": "bottom",
            "trigger": "manual",
          }
        };
      }
     },

    domain_completion_hint: function(options) {
      var searches = options.tracking_params.searches;
      var domain_completions = options.tracking_params.domain_completions;

      if (
        // There is a search object, (eg, after keydown)
        options.search_obj
        // There are matching domains
        && options.search_obj.domains_matching_stem.length > 0
        // There have been no successful completions by the user yet.
        && _.isEmpty(domain_completions)
      ) {
        return {
          "hint_method": "inline",
          "el": "[data-view-name='suggestion-panel-container']",
          "hide_event": "search_input",
          "success_event": "domain_completion",
          "hint_options": {
            "title": "<strong>Hint!</strong> <em>TAB</em> to see matching projects.",
          }
        };
      }
     },

  };

  return hint_rules;

});

