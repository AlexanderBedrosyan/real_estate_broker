const miniTvVideoId = 'KUvOUxkQpGg';

document.addEventListener("DOMContentLoaded", function() {
    const modalElement = document.getElementById('videoModal');
    const modalVideoIframe = document.getElementById('modal-video');
    const miniTvIframe = document.getElementById('mini-tv-video');
    const bootstrapModal = modalElement ? new bootstrap.Modal(modalElement) : null;

    function buildMiniLoopSrc() {
        return `https://www.youtube.com/embed/${miniTvVideoId}?autoplay=1&mute=1&loop=1&playlist=${miniTvVideoId}`;
    }

    // Ensure all media elements are muted by default
    const mediaElements = document.querySelectorAll("audio, video");
    mediaElements.forEach(element => {
        element.muted = true;
    });

    // Mute existing YouTube iframes (preserves other params)
    const iframeElements = document.querySelectorAll("iframe");
    iframeElements.forEach(iframe => {
        try {
            const src = iframe.getAttribute('src') || '';
            if (src.includes("youtube.com/embed")) {
                // If this is the mini-tv iframe and has no src, set looping src
                if (iframe.id === 'mini-tv-video' && (!src || src.trim() === "")) {
                    iframe.src = buildMiniLoopSrc();
                } else {
                    iframe.src = appendMuteToYouTubeURL(src);
                }
            }
        } catch (e) {
            // ignore invalid URLs
        }
    });

    if (modalElement && modalVideoIframe) {
        // Expose openModal globally if other code triggers it
        window.openModal = function() {
            modalVideoIframe.src = `https://www.youtube.com/embed/${miniTvVideoId}?autoplay=1&mute=1&loop=1&playlist=${miniTvVideoId}`;
            if (miniTvIframe) {
                miniTvIframe.src = "";
            }
            bootstrapModal && bootstrapModal.show();
        };

        modalElement.addEventListener('hidden.bs.modal', () => {
            modalVideoIframe.src = "";
            if (miniTvIframe) {
                miniTvIframe.src = buildMiniLoopSrc();
            }
        });
    }
});

// keep helper function at module scope
function appendMuteToYouTubeURL(url) {
    try {
        const urlObj = new URL(url);
        urlObj.searchParams.set("mute", "1");
        // if loop param missing for a single-video embed that should loop, playlist must be set externally
        return urlObj.toString();
    } catch (e) {
        return url;
    }
}