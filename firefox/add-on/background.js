// Connect to the rune-inator python script
var port = browser.runtime.connectNative("rune_inator");

var done = true;

// Receiving messages from the rune-inator python script
port.onMessage.addListener((response) => {
  console.log("Received: " + response);
  if(response == "done")
  {
    console.log("Done!");
    done = true;
    browser.browserAction.setIcon({ path: "icons/Idle.png" });
  }
});

// Called when the extention icon is clicked
browser.browserAction.onClicked.addListener(() => {
  if(done)
  {
    browser.tabs.query({ currentWindow: true, active: true })
      .then((tabs) => {
        var url = tabs[0].url;
        if(url.includes("murderbridge.com") && url.includes("Champion"))
        {
          var elements = url.split("/");
          if(elements.length > 0)
          {
            var champ = elements[elements.length - 1];

            console.log("Calling script for: " + champ);
            done = false;
            port.postMessage(champ);
            browser.browserAction.setIcon({ path: "icons/Working.png" });
          }
        }
      });
  }
});
