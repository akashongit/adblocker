browser.webRequest.onBeforeRequest.addListener(
  removeheaders,
  {urls: ["<all_urls>"]},
  ["blocking"]
);
// browser.webRequest.onBeforeRequest.removeListener(listener)

function removeheaders(requests)
{
  for 
  console.log("Headers removed!!");
}
