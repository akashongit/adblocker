



function redirect(requestDetails) {
  // console.log("opening  " + requestDetails.url);
  // console.log("type  " + requestDetails.type);
  Navigator.doNotTrack = 1;
}

function rewriteHeader(e) {
  if (e.type.toLowerCase() == "image")
  {
    return {requestHeaders: e.requestHeaders, cancel:true};
  }
  // if (e.type.toLowerCase() == "css")
  // {
  //   return {requestHeaders: e.requestHeaders, cancel:true};
  // }

  for (var header of e.requestHeaders) {
    if (header.name.toLowerCase() == "referer") {
      header.value = "";
    }
    // if (header.name.toLowerCase() == "cookie"){
    //   header.value = "";
    // }
  }
  return {requestHeaders: e.requestHeaders};
}

function logCookies(cookies) {
//   for (let cookie of cookies) {
//     var name = cookie.name;
//     console.log(name);
//     browser.cookies.remove({name});
//   }
}

// function responseDetails(responseDetails){
//   var getCookies = browser.cookies.getAll({});
//   console.log("cookies ");
//   getCookies.then(logCookies);
// }

// browser.tabs.query({}).then(tabs => {
//     for (tab of tabs) {
//         browser.cookies.getAll({url: tab.url}).then(cookies => {
//             for (cookie of cookies) {
//                 browser.cookies.remove({
//                     name: cookie.id
//                 });
//             }
//         });
//     }
// });
// }

browser.webRequest.onBeforeRequest.addListener(
  redirect,
  {urls: ["<all_urls>"]},
  ["blocking"]
);

// browser.webRequest.onBeforeSendHeaders.addListener(
//   rewriteUserAgentHeader,
//   {urls: ["<all_urls>"]},
//   ["blocking", "requestHeaders"]
// );
// browser.webRequest.onBeforeSendHeaders.addListener(
//   responseDetails,
//   {urls: ["<all_urls>"]},
//   ["blocking", "requestHeaders"]
// );

// browser.webRequest.onResponseStarted.addListener(
// responseDetails,
// {urls: ["<all_urls>"]},
// {type: ["html"]}
// );
function onSet(result) {
  if (result) {
    console.log("success");
  } else {
    console.log("failure");
  }
}
var trackSetting = browser.privacy.websites.trackingProtectionMode.set({
        value: "always"
      });

var cookieSetting = browser.privacy.websites.cookieConfig.set({
        behavior: "reject_third_party",
        nonPersistentCookies: false
      });

var fingerprintingSetting = browser.privacy.websites.resistFingerprinting.set({
        value: true
      });

// browser.browserAction.onClicked.addListener(() => {
//
//   var getting = browser.privacy.websites.hyperlinkAuditingEnabled.get({});
//   getting.then((got) => {
//     console.log(got.value);
//     if ((got.levelOfControl === "controlled_by_this_extension") ||
//         (got.levelOfControl === "controllable_by_this_extension")) {
//       var setting = browser.privacy.websites.hyperlinkAuditingEnabled.set({
//         value: true
//       });
//       setting.then(onSet);
//     } else {
//       console.log("Not able to set hyperlinkAuditingEnabled");
//     }
//   });
//
// });
