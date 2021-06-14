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
    },
    cssmin: {
      css: {
        src: "oc_lit_review/static/assets/css/common.css",
        dest: "oc_lit_review/static/assets/css/min/common.min.css",
      },
    },
    watch: {
      scripts: {
        files: ["src/js/*.js", "src/css/*.css"],
        tasks: ["concat", "uglify", "cssmin"],
        options: {
          spawn: false,
        },
      },
    },
  });

  grunt.loadNpmTasks("grunt-contrib-concat");
  grunt.loadNpmTasks("grunt-contrib-uglify");
  grunt.loadNpmTasks("grunt-contrib-cssmin");
  grunt.loadNpmTasks("grunt-contrib-watch");

  grunt.registerTask("default", ["concat", "uglify", "cssmin"]);
};
