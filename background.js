const NATIVE_HOST_NAME = 'com.my_company.video_downloader';

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.url) {
    console.log('Received URL, sending to native host:', message.url);
    chrome.runtime.sendNativeMessage(
      NATIVE_HOST_NAME,
      { url: message.url },
      (response) => {
        if (chrome.runtime.lastError) {
          console.error(`Error communicating with native host: ${chrome.runtime.lastError.message}`);
        } else {
          console.log('Received response from native host:', response);
        }
      }
    );
  }
});