function addLog(text){

    const box=document.getElementById("logBox");

    const time=new Date().toLocaleTimeString();

    box.innerHTML+="<br>"+time+" - "+text;

    box.scrollTop=box.scrollHeight;

}


function sendCommand(command){

    addLog(command);

}


const slider=document.getElementById("speedSlider");

slider.oninput=function(){

    document.getElementById("speedText").innerHTML=this.value+"%";

    addLog("Speed : "+this.value);

}