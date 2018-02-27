

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
