/*global module:false*/
module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({

    bump: {
      options: {
        files: ['package.json'],
        updateConfigs: [],
        commit: false,
        createTag: false,
        push: false,
      }
    },

    requirejs: {
      compile: {
        options: {
          baseUrl: "app/static/src",
          mainConfigFile: "app/templates/require_config_dev.js",
          dir: "app/static/build/" + grunt.file.readJSON(
            'package.json').version,
          modules: [
            {
              //module names are relative to baseUrl/paths config
              name: 'main'
            }
          ],
          removeCombined: true,
          fileExclusionRegExp: /^\./
        }
      }
    },

    // Task configuration.
    jshint: {

      options: {

        // JS Hint Options
        // See http://www.jshint.com/docs/

        // Enforcing Options
        // =================

        // Disable bitwise operators to prevent mixups of & and &&.
        bitwise: true,

        // Do NOT enforce camelCase as underscored names are preferred.
        camelcase: false,

        // Blocks must always use curlies.
        curly: true,

        // Prohibit == versus ===. == does coercion, which is not always easy
        // to predict.
        eqeqeq: true,

        // Enforce ECMAScript 3 compatibility in order to support IE8.
        es3: true,
        es5: false,

        // Require inherited properties to be filtered out in
        // `for (key in obj)` constructs.
        forin: true,

        // Functions must be wrapped in parens when immediately invoked, ie:
        //
        // (function() {
        //   return true;
        // })()
        immed: true,

        // Indent 2... not enforced. Do what looks good, but 2 is preferred.
        // indent: ???
        latedef: true,

        // Capitalize constructor functions.
        newcap: true,

        // Do not use arguments.caller and arguments.callee.
        // Disallowed in strict mode anyway.
        noarg: true,

        // Disallow use of explicitly undeclared variables.
        undef: true,

        // The only global var should be require's `define`.
        globals: { 'define': false, 'requirejs': false },

        // Warn on unused variables.
        unused: true,

        // Strict mode... I wish.
        // strict: ???

        // Limit max number of statements to prevent monolithic functions.
        maxstatements: 20,

        // Cyclomatic complexity... 10? 15? I prefer 5 when it comes to fns...
        maxcomplexity: 10,

        // Max line length: 80 or gtfo.
        maxlen: 80,

        // Relaxing Options
        // ================

        // Semicolons... just do em for simplicities sake.
        asi: false,

        // Warn when assignments used where comparisons expected.
        boss: false,

        // Don't use `== null` trick, use Underscore instead:
        // _.isNull(my_null) or _.isUndefined(my_undef)
        eqnull: false,

        // Eval is OK in certain scenarios.
        evil: true,

        // Allow expressions where assignments/calls expected.
        expr: true,

        // Don't use variables outside their block scope.
        funcscope: false,

        // This style does not cause any issues on any browsers, and
        // I find it to be much more readable:
        // if (my_bool
        //     && your_bool) {
        laxbreak: true,

        // Comma-first? I like it in SQL for some reason, but not
        // for JS.
        laxcomma: false,

        // No functions inside loops... use function factories instead.
        loopfunc: false,

        // No multiline strings. Use + as leading operator instead.
        multistr: false,

        // Use dot notation consistently...
        sub: false,

        // Environment Options
        // ===================

        // Set environment to a browser.
        browser: true,

        // Allow alert and console
        devel: true
      },

      all: [
        'Gruntfile.js',
        'app/static/*.js'
      ]
    },

    gruntfile: {
      src: 'Gruntfile.js'
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-bump');
  grunt.loadNpmTasks('grunt-contrib-requirejs');

  // Default task.
  grunt.registerTask('default', ['jshint', 'bump', 'requirejs']);

};
