'use strict';

// requirements
import gulp from "gulp";
import browserify from "gulp-browserify";
import size from "gulp-size";
import clean from "gulp-clean";
import eslint from "gulp-eslint";
import babel from "gulp-babel";

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

gulp.task('lint', () => {
  return gulp.src(['./wsgi/static/scripts/jsx/reddit_client.js', 'gulpfile.babel.js'])
    .pipe(eslint())
    .pipe(eslint.format())
});

gulp.task('transpile', ['lint'], () => bundle());


gulp.task('default', function() {
  gulp.start('transform');
  gulp.watch('./wsgi/static/scripts/jsx/reddit_client.js', ['transform']);
});

function onError(err) {
  console.log(err);
  this.emit('end');
}