let dstore = {
  blocked : true,
  newfilter : "",
  changefilter : false,
  context : ""
};
let blocking = {"blocking":false};
browser.storage.local.set(dstore);
browser.storage.local.set(blocking);
let ABPFilterParser = require('abp-filter-parser');
var fs = require('fs');
var unique = require('uniq');
var bloomf = require('bloom-filter-js');
// let easyListTxt = "||www.facebook.com^";
let easyListTxt = fs.readFileSync(__dirname + "/easylist.txt", "utf-8");
let parsedFilterData = {};
ABPFilterParser.parse(easyListTxt, parsedFilterData);
console.log(parsedFilterData);
// let urlToCheck = 'http://static.tumblr.com/dhqhfum/WgAn39721/cfh_header_banner_v2.jpg';

// let elementHidingRules = fs.readFileSync(__dirname + "/element.txt", "utf-8");
// let parsedeleFilterData = {};

// This is the site who's URLs are being checked, not the domain of the URL being checked.
let currentPageDomain = 'slashdot.org';
function blockUrl(requestDetails)
{
  // if(requestDetails.type.toLowerCase()=="main_frame")
  // {
  //   console.log("\ndocument");
  //
  // }

  // unblock all ads

  store = browser.storage.local.get("blocking");
  blocked = store.then(function(result) {
console.log("Unblock all ads value :"+result["blocking"]);
return result["blocking"];
});
  if(blocked == true)
  {
    console.log("Url is unblocked");
    return {cancel : false}
  }
  // let currentPageDomain = requestDetails.url;
// ABPFilterParser.parse(someOtherListOfFilters, parsedFilterData);

if (ABPFilterParser.matches(parsedFilterData, requestDetails.url, {
      domain: currentPageDomain,
      elementTypeMaskMap: ABPFilterParser.elementTypes.SCRIPT,
    }))
    {
  console.log("Loading: " + requestDetails.url);
  console.log('URL/Resource blocked!');
  return {redirectUrl : browser.extension.getURL("images/blocked.svg")}
  // return {cancel:true}
} else {
  // console.log("Loading: " + requestDetails.url);
  // console.log('You should NOT block this URL!');
  return {cancel : false}
}

}

function logURL(requestDetails) {
  console.log("Loading: " + requestDetails.url);
}
// if(blocking == true){
browser.webRequest.onBeforeRequest.addListener(
  blockUrl,
  {urls: ["<all_urls>"]},
  ["blocking"]
);

// browser.storage.onChanged.addListener(reboot());

function reboot()
{
  store = browser.storage.local.get();
  if (store.changefilter == true)
  {
    store.changefilter = false;
    var newfil ="";
    ABPFilterParser.parse(store.newfilter, newfil);
    parsedFilterData.add(newfil);
    browser.tabs.reload(tab.id);
    browser.storage.local.set({store});
}
}

// }
browser.webRequest.onBeforeRequest.addListener(
  findcontext,
  {urls: ["<all_urls>"], type: "main_frame"},
);

// function findcontext (requestDetails){
// svm_call = XMLHttpRequest();
// url = "http://127.0.0.1/findtext"
// svm_call.onreadystatechange = function() {
//   if (svm_call.readyState === 4) {
//     console.log(svm_call.response); //Outputs a DOMString by default
//   }
// }
//var formData = new FormData();
// formData.append('url', requestDetails.url);
// svm_call.open('POST', url, false);
// svm_call.send({"url":requestDetails.url});

//  store = browser.storage.local.set({store});
//  // store.context = ml()
// }

// document.addEventListener("DOMContentLoaded", function(event) {
//    console.log("DOM fully loaded and parsed");
//    elementHidingRules.forEach(elementHidingRule => {
//      let parsedFilterData = {};
//      parseFilter(elementHidingRule, parsedFilterData);
//      assert(parsedFilterData.htmlRuleSelector.length > 0);
//      assert(parsedFilterData.isException !== undefined);
//      parsedFilterData.forEach(parsedFilterData => {
//    if(elementHidingRule[0]=='.')
//    {
//    // document.getElementByClass(elementHidingRule).style.display = "block";
//   }
//   else
//   {
//   // document.getElementById(elementHidingRule).style.display = "block";
//   }
//    });
//  });
//
//  });
