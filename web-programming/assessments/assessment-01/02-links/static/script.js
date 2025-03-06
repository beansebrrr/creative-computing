/**
 * Play / pause functionality
 */

const backgroundVideo = document.querySelector("#background-video");
const playPause = document.querySelector("#play-pause");
const playPauseIcon = playPause.querySelector("img");

playPause.addEventListener("click", () => {
  if (backgroundVideo.paused) {
    backgroundVideo.play();
    playPauseIcon.src = "./static/assets/pause.svg";
  } else {
    backgroundVideo.pause();
    playPauseIcon.src = "./static/assets/play.svg";
  };
});