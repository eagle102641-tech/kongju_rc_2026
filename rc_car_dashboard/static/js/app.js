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
const joystick = nipplejs.create({

    zone: document.getElementById("joystick"),

    mode: "static",

    position: {

        left: "50%",

        top: "50%"

    },

    color: "blue"

});


joystick.on("move", async function(evt,data){

    const x=data.vector.x;

    const y=data.vector.y;

    addLog(
        "x:"+x.toFixed(2)+
        " y:"+y.toFixed(2)
    );

    await fetch("/api/joystick",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            x:x,

            y:y

        })

    });

});


joystick.on("end", async function(){

    await fetch("/api/joystick",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            x:0,

            y:0

        })

    });

});