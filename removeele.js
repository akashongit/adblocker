var blocked = true;
// var ele = true;
var border;
document.addEventListener("click", printMousePos);
// browser.runtime.onConnect.addListener(function(){ console.log(" removeele connected");});
browser.runtime.onMessage.addListener(function(message){ if(message.msg == true) {console.log("received from uimenu");blocked = false;} else {filter();}});

function filter(){
  newFilter = prompt("Enter new filter :");
  console.log("New filter added!!  "+newFilter);
  // changed = browser.storage.local.get("changed");
  // browser.storage.local.set({'newfilter':newFilter});
  // browser.storage.local.set({'changed':true});
  var sending = browser.runtime.sendMessage( {changed : true, filter:newFilter} );
  // browser.storage.local.set({store});
}

console.log("removeele Content script loaded!!");
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
