const secHand = document.querySelector(".sec-hand");
const minHand = document.querySelector(".min-hand");
const hrHand = document.querySelector(".hr-hand");

const setDate = () => {
    const now = new Date();
    
    let sec = now.getSeconds();
    const secDegrees = ((sec / 60) * 360) + 90;
    secHand.style.transform = `rotate(${secDegrees}deg)`;

    let min = now.getMinutes();
    const minDegrees = ((min / 60) * 360) + 90;
    minHand.style.transform = `rotate(${minDegrees}deg)`;

    let hr = now.getHours();
    if (hr > 12) hr -= 12;
    const hrDegrees = ((hr / 12) * 360) + 90;
    hrHand.style.transform = `rotate(${hrDegrees}deg)`;

    console.log(hr, min, sec);
}

setInterval(setDate, 1000);