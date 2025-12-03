const miniTvVideoId = 'KUvOUxkQpGg';

function buildEmbedSrc(videoId, { autoplay=false, loop=false } = {}) {
    const params = new URLSearchParams();
    if (autoplay) params.set('autoplay', '1');
    params.set('mute', '1');
    if (loop) {
        params.set('loop', '1');
        params.set('playlist', videoId);
    }
    params.set('enablejsapi', '1');
    try { params.set('origin', window.location.origin); } catch (e) {}
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

async function checkEmbeddable(videoId) {
    const oembedUrl = 'https://www.youtube.com/oembed?format=json&url=' +
        encodeURIComponent('https://www.youtube.com/watch?v=' + videoId);
    try {
        const resp = await fetch(oembedUrl, { method: 'GET', cache: 'no-store' });
        return resp.ok;
    } catch (e) {
        return false;
    }
}

document.addEventListener("DOMContentLoaded", async function() {
    const modalElement = document.getElementById('videoModal');
    const modalVideoIframe = document.getElementById('modal-video');
    const miniTvIframe = document.getElementById('mini-tv-video');
    const bootstrapModal = modalElement && window.bootstrap ? new bootstrap.Modal(modalElement) : null;

    // ensure allow attributes
    [modalVideoIframe, miniTvIframe].forEach(iframe => {
        if (!iframe) return;
        iframe.setAttribute('allow', 'autoplay; encrypted-media; picture-in-picture');
        iframe.setAttribute('allowfullscreen', '');
    });

    const embeddable = await checkEmbeddable(miniTvVideoId);

    if (embeddable) {
        if (miniTvIframe) {
            miniTvIframe.src = buildEmbedSrc(miniTvVideoId, { autoplay: true, loop: true });
        }
    } else {
        // fallback: remove/replace the mini iframe with a clickable poster/link
        if (miniTvIframe) {
            const poster = document.createElement('div');
            poster.className = 'mini-tv-fallback';
            poster.style.cssText = 'width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:#000;color:#fff;cursor:pointer;';
            poster.innerHTML = '<div style="text-align:center;"><strong>Watch on YouTube</strong><br><small>(video cannot be embedded)</small></div>';
            poster.addEventListener('click', () => {
                window.open('https://www.youtube.com/watch?v=' + miniTvVideoId, '_blank', 'noopener');
            });
            miniTvIframe.parentNode && miniTvIframe.parentNode.replaceChild(poster, miniTvIframe);
        }
        // For modal, fallback to opening watch page in new tab
    }

    if (modalElement && modalVideoIframe) {
        window.openModal = function() {
            if (embeddable) {
                if (!postYouTubeCommand(miniTvIframe, 'pauseVideo')) {
                    try { miniTvIframe.src = ''; } catch (e) {}
                }
                modalVideoIframe.src = buildEmbedSrc(miniTvVideoId, { autoplay: true, loop: false });
                bootstrapModal && bootstrapModal.show();
            } else {
                // open YouTube watch page in new tab since embed is blocked
                window.open('https://www.youtube.com/watch?v=' + miniTvVideoId, '_blank', 'noopener');
            }
        };

        modalElement.addEventListener('hidden.bs.modal', () => {
            if (embeddable) {
                if (!postYouTubeCommand(modalVideoIframe, 'stopVideo')) {
                    try { modalVideoIframe.src = ''; } catch (e) {}
                } else {
                    try { modalVideoIframe.src = ''; } catch (e) {}
                }
                if (!postYouTubeCommand(miniTvIframe, 'playVideo')) {
                    try { miniTvIframe.src = buildEmbedSrc(miniTvVideoId, { autoplay: true, loop: true }); } catch (e) {}
                }
            }
        });
    }
});