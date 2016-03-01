/**
 * Builds the mobile and desktop files for production.
 */

'use strict';

var gulp = require('gulp');
var runSequence = require('run-sequence');

gulp.task('build', function(cb) {
    global.isWatching = false;

    runSequence(
        'clean',
        // 'collectstatic',
        'copy',
        'sprites',
        [
            'sass',
        ],
        'cssmin',
        'uglify',
        cb);
});
