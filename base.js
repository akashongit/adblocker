var blocking = false;
let ABPFilterParser = require('abp-filter-parser');
var fs = require('fs');
var unique = require('uniq');
let easyListTxt = "||ads.example.com^";
// let easyListTxt = fs.readFileSync(__dirname + "/node_modules/abp-filter-parser/test/data/easylist.txt", "utf-8");
let parsedFilterData = {};
// let urlToCheck = 'http://static.tumblr.com/dhqhfum/WgAn39721/cfh_header_banner_v2.jpg';

let elementHidingRules = fs.readFileSync(__dirname + "/element.txt", "utf-8");
let parsedeleFilterData = {};

// This is the site who's URLs are being checked, not the domain of the URL being checked.
let currentPageDomain = 'slashdot.org';
function blockUrl(requestDetails)
{
  if(blocking == true)
  {
    return {cancel : false}
  }
  // let currentPageDomain = requestDetails.url;
ABPFilterParser.parse(easyListTxt, parsedFilterData);
// ABPFilterParser.parse(someOtherListOfFilters, parsedFilterData);

if (ABPFilterParser.matches(parsedFilterData, requestDetails.url, {
      domain: currentPageDomain,
      elementTypeMaskMap: ABPFilterParser.elementTypes.SCRIPT,
    })) {
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
// browser.webRequest.onBeforeRequest.addListener(
//   blockUrl,
//   {urls: ["<all_urls>"]},
//   ["blocking"]
// );
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
