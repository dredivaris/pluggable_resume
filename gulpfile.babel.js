'use strict';

// requirements
import gulp from "gulp";
import browserify from "browserify";
import clean from "gulp-clean";
import eslint from "gulp-eslint";
import babelify from "babelify";
import source from "vinyl-source-stream";
import transform from "vinyl-transform";


gulp.task('transform', function () {
  return browserify('./wsgi/static/scripts/src/app.js')
    // .transform('reactify')
    .transform(babelify, {presets: ["es2015", "react"]})
    .bundle()
    .on('error', onError)
    .pipe(source('bundle.js'))
    .pipe(gulp.dest('./wsgi/static/scripts/dist'));
});

gulp.task('clean', function () {
  return gulp.src(['./wsgi/static/scripts/dist'], {read: false})
    .pipe(clean());
});

gulp.task('lint', () => {
  return gulp.src(['./wsgi/static/scripts/src/app.js', 'gulpfile.babel.js'])
    .pipe(eslint())
    .pipe(eslint.format())
});

gulp.task('transpile', ['lint'], () => bundle()); // TODO


gulp.task('default', function () {
  gulp.start('transform');
  gulp.watch('./wsgi/static/scripts/src/*.js', ['transform']);
  gulp.watch('./wsgi/static/scripts/src/**/*.js', ['transform'])
});

function onError(err) {
  console.log(err);
  this.emit('end');
}