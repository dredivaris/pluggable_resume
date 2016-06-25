'use strict';

// requirements
var gulp = require('gulp'),
    browserify = require('gulp-browserify'),
    size = require('gulp-size'),
    clean = require('gulp-clean'),
    sourcemaps = require("gulp-sourcemaps"),
    babel = require("gulp-babel");

gulp.task('transform', function () {
  return gulp.src('./wsgi/static/scripts/jsx/reddit_client.js')
    .pipe(browserify({transform: ['reactify']}))
    .on('error', onError)
    .pipe(babel())
    .pipe(gulp.dest('./wsgi/static/scripts/js'))
    .pipe(size());
});

gulp.task('clean', function () {
  return gulp.src(['./wsgi/static/scripts/js'], {read: false})
    .pipe(clean());
});

gulp.task('default', function() {
  gulp.start('transform');
  gulp.watch('./wsgi/static/scripts/jsx/reddit_client.js', ['transform']);
});

function onError(err) {
  console.log(err);
  this.emit('end');
}