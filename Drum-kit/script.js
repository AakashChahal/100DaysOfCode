function playSound(e) {
    // console.log(e);
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.querySelector(`.key[data-key="${e.keyCode}"]`);
    // console.log(audio);
    if (!audio) return;
    audio.currentTime = 0;
    audio.play();
    key.classList.add("playing");
};

const keys = document.querySelectorAll('.key');

function removeTransition(e){
    if (e.propertyName !== 'transform') return;
    // console.log(e);
    this.classList.remove("playing");
}; 

keys.forEach(key => key.addEventListener('transitionend', removeTransition));
window.addEventListener('keydown', playSound);