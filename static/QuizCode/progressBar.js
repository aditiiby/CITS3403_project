const progressBar = document.getElementById("InsideBar")

/* this here will check the if there is a result in the DB and if so will add 16.67 otherwise the progress will be 0*/
let CarbonProgress = 16.67
let HeliumProgress = 16.67
let HydrogenProgress = 16.67
let IronProgress = 16.67
let NitrogenProgress = 16.67 
let OxygenProgress = 16.67


progress = (CarbonProgress + HeliumProgress + HydrogenProgress + IronProgress + NitrogenProgress + OxygenProgress).toFixed()

progressBar.innerHTML =  progress + "%"
progressBar.style.width = progress + "%"
