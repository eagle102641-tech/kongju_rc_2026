function addLog(text) {

    const box = document.getElementById("logBox");

    const time = new Date().toLocaleTimeString();

    box.innerHTML += "<br>" + time + " - " + text;

    box.scrollTop = box.scrollHeight;

}

async function sendCommand(command) {

    addLog(command);

    await fetch("/api/drive", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            command: command
        })
    });

}

const slider = document.getElementById("speedSlider");

slider.oninput = async function () {

    document.getElementById("speedText").innerHTML = this.value + "%";

    addLog("Speed : " + this.value);

    await fetch("/api/speed", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            speed: this.value
        })
    });

}