// let dstore = {
//   blocked : true,
//   newfilter : "",
//   changefilter : false,
//   context : ""
// };
unblocked = false

let newfilter = {"newfilter" : ""};
let changed = {"changed":false}
let blocking = {"blocking":false};
browser.storage.local.set(newfilter);
browser.storage.local.set(blocking);
browser.storage.local.set(changed);
let ABPFilterParser = require('abp-filter-parser');
var IDBFiles = require('idb-file-storage')
var fs = require('fs');
var unique = require('uniq');
var bloomf = require('bloom-filter-js');
let userFilter = "";
let context = {
media:"",
entertainment:"",
games:"",
shopping:"",
education:"",
adult:"",
economy:"",
health:"",
kids:"",
sports:""
};

var conIterator = 0;
let parsedContextData = [];
var temp;

// let easyListTxt = "||ads.example.com^";
let easyListTxt = fs.readFileSync(__dirname + "/easylist.txt", "utf-8");
// let userFilter = fs.readFileSync(__dirname + "/userfilter.txt", "utf-8");
let parsedFilterData = {};
let parseduserFilterData = {};

// for(conIterator=0;conIterator<10;conIterator++){
//   ABPFilterParser.parse(userFilter, temp);
//   parsedContextData.push(temp);
// }


ABPFilterParser.parse(easyListTxt, parsedFilterData);
ABPFilterParser.parse(userFilter, parseduserFilterData);
// console.log(parsedFilterData);
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
  if(unblocked == true)
  {
    console.log("Url is unblocked");
    return {cancel : false}
  }
  // let currentPageDomain = requestDetails.url;
// ABPFilterParser.parse(someOtherListOfFilters, parsedFilterData);
matchEasyList = ABPFilterParser.matches(parsedFilterData, requestDetails.url, {
      domain: currentPageDomain,
      elementTypeMaskMap: ABPFilterParser.elementTypes.SCRIPT,
    });
matchuserFilter = ABPFilterParser.matches(parseduserFilterData, requestDetails.url, {
      domain: currentPageDomain,
      elementTypeMaskMap: ABPFilterParser.elementTypes.SCRIPT,
    });
    console.log("EasyList :"+matchEasyList+"\nUser Filter :"+matchuserFilter);
// if (matchEasyList)
if (matchEasyList || matchuserFilter)
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

// browser.storage.onChanged.addListener(reboot);
browser.runtime.onMessage.addListener(reboot)

function get_domain_from_url(url) {
var sourceString = url.replace('http://','').replace('https://','').replace('www.','').split(/[/?#]/)[0];
return sourceString;
}

function reboot(message)
{
  //access newfilter
  // let fdata = browser.storage.local.get("newfilter");
  // let cdata = browser.storage.local.get("changed");
  // let uFilter = fdata.then(function(result) {
  // console.log("new filter "+result["newfilter"]+" accepted!!!");
  // return result["newfilter"];
  // });
  // console.log(uFilter);
//access changed
 // let isChanged = cdata.then(function(result) {
 //  console.log("filter added in blocker "+result["changed"]);
 //  return result["changed"];
 //  });
  // console.log("isChanged "+isChanged);
  if (message.changed)
  {
    // browser.storage.local.set({'newfilter':''});
    // browser.storage.local.set({'changed':false});
    console.log(" Filter change analysed!!!");

    var parsedUrl = get_domain_from_url(message.filter)
    console.log("new filter "+parsedUrl+" accepted ");
    filterRule = "||"+parsedUrl+"^";
    // console.log();
    userFilter = userFilter+filterRule+"\n";
    console.log("content in user filter "+userFilter);
    // console.log(userFilter+"||"+message.filter+"^\n");
    ABPFilterParser.parse(userFilter, parseduserFilterData);
    // browser.tabs.reload(tab.id);



    //appending to file
    // let ufilter = fs.readFileSync(__dirname + "/userfilter.txt", "utf-8");
    // let ufilter = fs.open('mynewfile2.txt', 'w');
//     fs.appendFile(__dirname + "/userfilter.txt", message.filter);
//     store.changefilter = false;
//     var newfil ="";
//     ABPFilterParser.parse(store.newfilter, newfil);
//     parsedFilterData.add(newfil);
//     browser.tabs.reload(tab.id);
//     browser.storage.local.set({store});
// }

  }

}

// listener for context
browser.webRequest.onBeforeRequest.addListener(
  findcontext,
  {urls: ["<all_urls>"], types: ["main_frame"]}
);

function findcontext (requestDetails){
svm_call = new XMLHttpRequest();
url = "http://127.0.0.1:8080/findcontext?&url="+requestDetails.url;
console.log("Ajax call to "+url);
svm_call.onreadystatechange = function() {
  if (svm_call.readyState === 4) {
    let context = JSON.parse(svm_call.response)
    console.log("respone from server "+svm_call.response); //Outputs a DOMString by default
    console.log("the context is "+context['context']);
  }
}
// var formData = new FormData();
// formData.append('url', requestDetails.url);
svm_call.open('GET', url, true);

svm_call.send({"url":requestDetails.url});

 // store = browser.storage.local.set({store});
 // store.context = ml()
}

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
