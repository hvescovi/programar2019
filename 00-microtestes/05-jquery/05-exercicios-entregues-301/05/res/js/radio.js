var sound = new Howl({
      src: ['res/music/music.mp3'],
      loop: true,
    });
var sound2 = new Howl({
      src: ['res/music/music2.mp3'],
      loop: true,
    });
var estatica = new Howl({
  src: ['res/music/estatica.mp3'],
  sprite: {
    estatica: [0, 1000],
  }
});

document.getElementById('volume').addEventListener("input", function(){
  var val = document.getElementById("volume").value;
  Howler.volume(val/10);
});

document.getElementById('music').addEventListener("input", function(){
  var val = document.getElementById("music").value;
  console.log(val);

  sound.stop();
  sound2.stop();
  estatica.stop();

  estatica.play("estatica");
  if (val == 10){
    sound.play();
  }
  if (val == 0){
    sound2.play();
  }

});