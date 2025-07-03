num=0
function stopWatch(){
    let stopwatch=document.getElementById('PP')
    num+=1
    stopwatch.textContent=num
}

function reset(){
    let reset=document.getElementById('btn').textcontent=0

}

function stop(){
    let stop=document.getElementById('btn2')
    stop.clearInterval()
}



function sgh() {
    let img = document.getElementById("photo");
    img.width = img.width*2;
    }
    setInterval(sgh, 5000)