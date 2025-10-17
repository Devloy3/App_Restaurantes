import gulp from 'gulp';
import open from 'open';

// Task to open the browser
gulp.task('open-app', function(){
  return open('/home/eloy/git/restaurantes/Web/boot/pages/dashboard.html');
});