var blocked = true;
// var ele = true;
var border;
document.addEventListener("click", printMousePos);
browser.runtime.onConnect.addListener(function(){ console.log("connected");});
browser.runtime.onMessage.addListener(function(message){ if(message.msg == true) {console.log("received");blocked = false;}});

console.log("Content script loaded!!");
function printMousePos(e) {
  if(blocked == false)
  {
    item = e.target;
    item.style.display = "none";
      blocked = true;
    // console.log(item);
    alert("Ads successfully blocked!!");
}
}


// document.addEventListener("hover", function(e){border = e.target.style.border-style; e.target.style.border-style ="dotted";});
// document.addEventListener("hover", function(e){e.target.style.border-style = border;});
