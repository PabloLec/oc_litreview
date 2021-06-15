module.exports = function (grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),

    concat: {
      common_js: {
        src: [
          "oc_lit_review/static/assets/jquery/jquery-3.6.0.min.js",
          "oc_lit_review/static/assets/bootstrap/bootstrap.min.js",
        ],
        dest: "oc_lit_review/static/assets/js/common.js",
      },
      common_css: {
        src: [
          "oc_lit_review/static/assets/bootstrap/bootstrap.min.css",
          "oc_lit_review/static/assets/css/style.css",
          "oc_lit_review/static/assets/css/navbar.css",
          "oc_lit_review/static/assets/fontawesome/css/all.css",
        ],
        dest: "oc_lit_review/static/assets/css/common.css",
      },
    },
    uglify: {
      common_js: {
        src: "oc_lit_review/static/assets/js/common.js",
        dest: "oc_lit_review/static/assets/js/min/common.min.js",
      },
      index: {
        src: "oc_lit_review/static/assets/js/index.js",
        dest: "oc_lit_review/static/assets/js/min/index.min.js",
      },
      post_actions: {
        src: "oc_lit_review/static/assets/js/post_actions.js",
        dest: "oc_lit_review/static/assets/js/min/post_actions.min.js",
      },
      star_rating: {
        src: "oc_lit_review/static/assets/js/star_rating.js",
        dest: "oc_lit_review/static/assets/js/min/star_rating.min.js",
      },
      usersearch: {
        src: "oc_lit_review/static/assets/js/usersearch.js",
        dest: "oc_lit_review/static/assets/js/min/usersearch.min.js",
      },
    },
    cssmin: {
      common_css: {
        src: "oc_lit_review/static/assets/css/common.css",
        dest: "oc_lit_review/static/assets/css/min/common.min.css",
      },
      index: {
        src: "oc_lit_review/static/assets/css/index.css",
        dest: "oc_lit_review/static/assets/css/min/index.min.css",
      },
      index_form: {
        src: "oc_lit_review/static/assets/css/index_form.css",
        dest: "oc_lit_review/static/assets/css/min/index_form.min.css",
      },
      posts: {
        src: "oc_lit_review/static/assets/css/posts.css",
        dest: "oc_lit_review/static/assets/css/min/posts.min.css",
      },
      review_forms: {
        src: "oc_lit_review/static/assets/css/review_forms.css",
        dest: "oc_lit_review/static/assets/css/min/review_forms.min.css",
      },
      subscriptions: {
        src: "oc_lit_review/static/assets/css/subscriptions.css",
        dest: "oc_lit_review/static/assets/css/min/subscriptions.min.css",
      },
    },
  });

  grunt.loadNpmTasks("grunt-contrib-concat");
  grunt.loadNpmTasks("grunt-contrib-uglify");
  grunt.loadNpmTasks("grunt-contrib-cssmin");

  grunt.registerTask("default", ["concat", "uglify", "cssmin"]);
};
