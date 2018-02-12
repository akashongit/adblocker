let ABPFilterParser = require('abp-filter-parser');
var fs = require('fs');
var unique = require('uniq');
let easyListTxt = "||ads.example.com^";
// let easyListTxt = fs.readFileSync(__dirname + "/node_modules/abp-filter-parser/test/data/easylist.txt", "utf-8");
let parsedFilterData = {};
let urlToCheck = 'http://static.tumblr.com/dhqhfum/WgAn39721/cfh_header_banner_v2.jpg';

// This is the site who's URLs are being checked, not the domain of the URL being checked.
let currentPageDomain = 'slashdot.org';
function blockUrl(requestDetails)
{
ABPFilterParser.parse(easyListTxt, parsedFilterData);
// ABPFilterParser.parse(someOtherListOfFilters, parsedFilterData);

if (ABPFilterParser.matches(parsedFilterData, requestDetails.url, {
      domain: currentPageDomain,
      elementTypeMaskMap: ABPFilterParser.elementTypes.SCRIPT,
    })) {
  console.log("Loading: " + requestDetails.url);
  console.log('You should block this URL!');
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

browser.webRequest.onBeforeRequest.addListener(
  blockUrl,
  {urls: ["<all_urls>"]},
  ["blocking"]
);
