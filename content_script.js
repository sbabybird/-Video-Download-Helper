// Use a WeakSet to keep track of elements that have already been processed.
const processedElements = new WeakSet();

// Using the maximum z-index value to ensure the button is always on top.
const MAX_Z_INDEX = 2147483647;

function createDownloadButton(targetElement) {
    if (processedElements.has(targetElement)) return;

    const button = document.createElement('button');
    button.textContent = '⬇️';
    // Apply styles for the button
    Object.assign(button.style, {
        position: 'absolute',
        top: '15px', // Adjusted for better visibility on various players
        left: '15px',
        zIndex: MAX_Z_INDEX, // Use the max z-index
        backgroundColor: 'rgba(0, 0, 0, 0.7)', // More neutral color
        color: 'white',
        border: '2px solid white', // Add border for better visibility
        borderRadius: '50%',
        width: '40px', // Slightly larger
        height: '40px',
        fontSize: '20px',
        cursor: 'pointer',
        opacity: '0.6',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        boxShadow: '0 2px 5px rgba(0,0,0,0.5)' // Add shadow
    });

    button.addEventListener('mouseover', () => button.style.opacity = '1');
    button.addEventListener('mouseout', () => button.style.opacity = '0.6');

    button.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        let urlToSend = window.location.href; // Default URL
        const hostname = window.location.hostname;

        if (hostname.includes('twitter.com') || hostname.includes('x.com')) {
            const tweetArticle = e.target.closest('article[data-testid="tweet"]');
            if (tweetArticle) {
                // Find the permalink by looking for a link with a time element inside
                const timeElement = tweetArticle.querySelector('time');
                if (timeElement && timeElement.parentElement.tagName === 'A') {
                     urlToSend = timeElement.parentElement.href;
                } else {
                    // Fallback for other link structures
                    const permalinkElement = tweetArticle.querySelector('a[href*="/status/"]');
                     if (permalinkElement && permalinkElement.href) {
                        urlToSend = permalinkElement.href;
                    } else {
                        console.error("VideoDownloader: Could not find tweet permalink. Falling back to page URL.");
                    }
                }
            } else {
                console.error("VideoDownloader: Could not find parent tweet article.");
            }
        }

        console.log(`Sending URL to background: ${urlToSend}`);
        chrome.runtime.sendMessage({ url: urlToSend });
    });

    if (window.getComputedStyle(targetElement).position === 'static') {
        targetElement.style.position = 'relative';
    }
    
    targetElement.appendChild(button);
    processedElements.add(targetElement);
}

function handleTwitter() {
    const videoPlayers = document.querySelectorAll('article[data-testid="tweet"] div[data-testid="videoPlayer"]');
    videoPlayers.forEach(player => {
        createDownloadButton(player);
    });
}

function handlePornhub() {
    // Pornhub's main player container has the ID 'player'
    const playerContainer = document.querySelector('#player');
    if (playerContainer) {
        createDownloadButton(playerContainer);
    }
}

function handleGeneric() {
    const videos = document.querySelectorAll('video');
    videos.forEach(video => {
        // Use the parent element as the container. This works for YouTube.
        const container = video.parentElement;
        if (container) {
            createDownloadButton(container);
        }
    });
}

function runDetector() {
    const hostname = window.location.hostname;
    if (hostname.includes('twitter.com') || hostname.includes('x.com')) {
        handleTwitter();
    } else if (hostname.includes('pornhub.com')) {
        handlePornhub();
    } else {
        handleGeneric();
    }
}

setInterval(runDetector, 1500);

console.log("Video Downloader content script (v3) loaded and running.");