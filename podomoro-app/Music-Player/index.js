/*jshint esversion: 6 */
var img = document.querySelector("img");
var music = document.querySelector("audio");
var play = document.getElementById("play");
var artist = document.getElementById("artist");
var title = document.getElementById("title");
var prev = document.getElementById("prev");
var next = document.getElementById("next");
let progress = document.getElementById("progress");
let total_duration = document.getElementById("duration");
let current_time = document.getElementById("current_time");
const progress_div = document.getElementById("progress_div");

var songs = [{
  name: "music-1",
  title: "SUN MERE HUMSAFAR",
  artist: "Akhil Sachdeva",
},
{
  name: "music-2",
  title: "DUNIYA",
  artist: "Abhijit Vaghani, Akhil, Dhvani Bhanushali, Bob",
},
];
var isPlaying = false;

// play function
var playMusic = function(){
  isPlaying = true;
  music.play();
  play.classList.replace("fa-play","fa-pause");
  img.classList.add("anime");
};

// pause function
var pauseMusic =function(){
  isPlaying = false;
  music.pause();
  play.classList.replace("fa-pause","fa-play");
  img.classList.add("anime");
};

play.addEventListener('click',function(){
  if(isPlaying){
    pauseMusic();
  }else{
    playMusic();
  }
});

// change the track
var loadSong = function(songs){
  title.textContent = songs.title;
  artist.textContent = songs.artist;
  music.src = "musics/"+songs.name+".mp3";
  img.src = "images/"+songs.name+".jpg";

};
songIndex = 0;

var nextSong = function(){
  songIndex = (songIndex+1)%songs.length;
  loadSong(songs[songIndex]);
  playMusic();
};

var prevSong = function(){
  songIndex = (songIndex-1+songs.length)%songs.length;
  loadSong(songs[songIndex]);
  playMusic();
};

// progress bar
music.addEventListener('timeupdate',function(event){
  var {currentTime,duration}= event.srcElement;

  let progress_time = (currentTime/duration)*100;
  progress.style.width = `${progress_time}%`;
  // music duration
  let min_duration = Math.floor(duration/60);
  let sec_duration = Math.floor(duration%60);

  let tot_duration = `${min_duration}:${sec_duration}`;
  if(duration){
    total_duration.textContent = `${tot_duration}`;
  }

  // current duration
  let min_currentTime = Math.floor(currentTime/60);
  let sec_currentTime = Math.floor(currentTime%60);
  if(sec_currentTime<10){
    sec_currentTime = `0${sec_currentTime}`;
  }
  let tot_currentTime = `${min_currentTime}:${sec_currentTime}`;
  current_time.textContent = `${tot_currentTime}`;

});

progress_div.addEventListener('click',function(event){
  const {duration} = music;
  let move_progress = (event.offsetX/event.srcElement.clientWidth)*duration;
  music.currentTime = move_progress;
});
music.addEventListener('ended',nextSong());
next.addEventListener('click',nextSong);
prev.addEventListener('click',prevSong);
