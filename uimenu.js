// import "./blocker.js";
/*
Called when the item has been created, or when creation failed due to an error.
We'll just log success/failure here.
*/

// let initialState = browser.storage.local.get("blocking");
// let checkedState = initialState.then(function(result) {
// return result["blocking"];
// });

function onCreated() {
  if (browser.runtime.lastError) {
    console.log(`Error: ${browser.runtime.lastError}`);
  } else {
    console.log("Item created successfully");
  }
}

/*
Called when the item has been removed.
We'll just log success here.
*/
function onRemoved() {
  console.log("Item removed successfully");
}

/*
Called when there was an error.
We'll just log the error here.
*/
function onError(error) {
  console.log(`Error: ${error}`);
}

/*
Create all the context menu items.
*/


let checkedState = false;

browser.menus.create({
  id: "unblock",
  title: "Unblock Ads",
  contexts: ["all"],
  type: "radio",
    // icons: {
    // "16": "icons/paint-blue-16.png",
    // "32": "icons/paint-blue-32.png"
  // },
  checked: checkedState
}, onCreated);

browser.menus.create({
  id: "addfilter",
  title: "Add New Filter",
  contexts: ["all"],
  icons: {
    "16": "icons/paint-blue-16.png",
    "32": "icons/paint-blue-32.png"
  }
}, onCreated);


browser.menus.create({
  id: "remove",
  title: "Remove this Ad",
  contexts: ["all"],
  icons: {
    "16": "icons/paint-green-16.png",
    "32": "icons/paint-green-32.png"
  }
}, onCreated);


// browser.menus.create({
//   id: "tools-menu",
//   title: "Menu",
//   contexts: ["tools_menu"],
// }, onCreated);

/*
Set a colored border on the document in the given tab.
Note that this only work on normal web pages, not special pages
like about:debugging.
*/
var blue = 'document.body.style.border = "5px solid blue"';
var green = 'document.body.style.border = "5px solid green"';

function borderify(tabId, color) {
  browser.tabs.executeScript(tabId, {
    code: color
  });
}

/*
Toggle checkedState, and update the menu item's title
appropriately.
Note that we should not have to maintain checkedState independently like
this, but have to because Firefox does not currently pass the "checked"
property into the event listener.
*/
function updateCheckUncheck() {
  checkedState = !checkedState;
  if (checkedState) {
    browser.menus.update("unblock", {
      checked: true,
    });
  } else {
    browser.menus.update("unblock", {
      checked: false,
    });
  }
}

/*
The click event listener, where we perform the appropriate action given the
ID of the menu item that was clicked.
*/
browser.menus.onClicked.addListener((info, tab) => {
  switch (info.menuItemId) {
    case "unblock":
      // console.log(info.selectionText);
      // console.log("Unblocked option");
      updateCheckUncheck();
      let data = browser.storage.local.get("blocking");
      let blocked = data.then(function(result) {
   console.log(!result["blocking"]);
   return result["blocking"];
 });

//  store = browser.storage.local.get();
//  blocked = store.then(function(result) {
// console.log(result);
// return result;
// });
 // store = Promise.resolve()
      // console.log(store.value);
     // console.log(Object.values(store));
      // store["blocking"] = !store["blocking"];
      // store.then(function(result) {
   // console.log(result);
 // });
      console.log("menu status -> " + checkedState);
      browser.storage.local.set({'blocking':checkedState});
      browser.tabs.reload(tab.id);
      break;
    // case "remove-me":
    //   var removing = browser.menus.remove(info.menuItemId);
    //   removing.then(onRemoved, onError);
    //   break;
    case "remove":
      // borderify(tab.id, blue);
      console.log("Blocked!!");
      // var item = info.mediaType;
      // var curtab = tabs.query({active: true});
      console.log(tab.id);
      // var stat = browser.tabs.connect(
      // tab.id,
      // {name: "remove ads"}

    // );
      // stat.postMessage({b: true});
    // browser.addEventListener('click', function() {
    var sending = browser.tabs.sendMessage( tab.id, {msg : true} );
    // console.log("working");
    // onClick's logic below:
    // document.addEventListener('click', printMousePos);
// });


      // printMousePos();
      // cursorX = 2;
      // cursorY = 3;

      // console.log("x :" + cursorX + "  y :" + cursorY );
      // item = document.caretPositionFromPoint(cursorX ,cursorY );
      // item
      // .style.color = "RED";
      break;

case "addfilter":
    var sending = browser.tabs.sendMessage( tab.id, {msg : false} );
    // var newf = browser.tabs.sendMessage( tab.id, {msg : true} );
break;
    // case "open-sidebar":
    //   console.log("Opening my sidebar");
    //   break;
    // case "tools-menu":
    //   console.log("Clicked the tools menu item");
    //   break;
  }
});

// function removeele(){
//   document.addEventListener("click", function( event ) {
//     // highlight the mouseenter target
//     console.log("entered");
//     event.target.style.color = "purple";});
// }
