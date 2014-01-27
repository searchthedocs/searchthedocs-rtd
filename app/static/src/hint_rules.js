define(function() {

  var hint_rules = {
    // Hint Rules take a hash of user tracking parameters to offer
    // hints to the user based on previous interactions.
    // Parameters:
    // - visit_number
    // - actions_performed (array)
    //
    // Returns a hash containing the metadata to display the hint.
    // For example:
    //
    incremental_hint: function(options) {
      var visit_number = options.visit_number;
      if (visit_number === 1) {
        return {
          "hint_method": "tooltip",
          "el": ".search-input-container",
          "hint_options": {
            "title": "Incremental search! Start typing...",
            "placement": "bottom",
          }
        };
      }
     },

  };

  return hint_rules;

});

