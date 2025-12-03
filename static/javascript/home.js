const miniTvVideoId = 'KUvOUxkQpGg';

function buildEmbedSrc(videoId, { autoplay=false, loop=false } = {}) {
    const params = new URLSearchParams();
    if (autoplay) params.set('autoplay', '1');
    // mute is required for autoplay in many browsers
    params.set('mute', '1');
    if (loop) {
        params.set('loop', '1');
        params.set('playlist', videoId);
    }
    // enable JS API and set origin to avoid player configuration errors
    params.set('enablejsapi', '1');
    try {
        params.set('origin', window.location.origin);
    } catch (e) {
        // ignore if origin isn't available (very rare)
    }
    params.set('rel', '0');
    params.set('modestbranding', '1');
    return `https://www.youtube.com/embed/${videoId}?${params.toString()}`;
}

function postYouTubeCommand(iframe, command) {
    if (!iframe || !iframe.contentWindow) return false;
    try {
        iframe.contentWindow.postMessage(JSON.stringify({
            event: 'command',
            func: command,
            args: []
        }), '*');
        return true;
    } catch (e) {
        return false;
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const modalElement = document.getElementById('videoModal');
    const modalVideoIframe = document.getElementById('modal-video');
    const miniTvIframe = document.getElementById('mini-tv-video');
    const bootstrapModal = modalElement && window.bootstrap ? new bootstrap.Modal(modalElement) : null;

    // Ensure iframes have proper allow attributes (helps autoplay)
    [modalVideoIframe, miniTvIframe].forEach(iframe => {
        if (!iframe) return;
        iframe.setAttribute('allow', 'autoplay; encrypted-media; picture-in-picture');
        iframe.setAttribute('allowfullscreen', '');
    });

    // Initialize mini TV looped player
    if (miniTvIframe) {
        // set looping, muted, autoplay embed with origin+enablejsapi
        miniTvIframe.src = buildEmbedSrc(miniTvVideoId, { autoplay: true, loop: true });
    }

    if (modalElement && modalVideoIframe) {
        // Expose openModal globally for other code
        window.openModal = function() {
            // try to pause mini player via JS API; if not possible, clear its src as fallback
            if (!postYouTubeCommand(miniTvIframe, 'pauseVideo')) {
                try { miniTvIframe.src = ''; } catch (e) { /* ignore */ }
            }

            // set modal player to play (no loop needed)
            modalVideoIframe.src = buildEmbedSrc(miniTvVideoId, { autoplay: true, loop: false });
            bootstrapModal && bootstrapModal.show();
        };

        // When modal closes stop modal player and resume mini player
        modalElement.addEventListener('hidden.bs.modal', () => {
            // stop modal player via JS API if possible
            if (!postYouTubeCommand(modalVideoIframe, 'stopVideo')) {
                try { modalVideoIframe.src = ''; } catch (e) { /* ignore */ }
            } else {
                // also clear src to fully reset iframe
                try { modalVideoIframe.src = ''; } catch (e) { /* ignore */ }
            }

            // try to resume mini player via JS API; fallback to re-assigning src
            if (!postYouTubeCommand(miniTvIframe, 'playVideo')) {
                try { miniTvIframe.src = buildEmbedSrc(miniTvVideoId, { autoplay: true, loop: true }); } catch (e) { /* ignore */ }
            }
        });
    }
});