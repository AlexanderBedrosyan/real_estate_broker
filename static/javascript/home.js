// Runtime-safe YouTube embed: check oEmbed, only set iframe src when embeddable.
// Falls back to opening YouTube watch page if embedding is blocked.

(function () {
    const DEFAULT_VIDEO_ID = 'KUvOUxkQpGg';

    function buildEmbedSrc(videoId, { autoplay=false, loop=false } = {}) {
        const params = new URLSearchParams();
        if (autoplay) params.set('autoplay', '1');
        params.set('mute', '1');
        if (loop) {
            params.set('loop', '1');
            params.set('playlist', videoId);
        }
        params.set('enablejsapi', '1');
        params.set('playsinline', '1');
        try { params.set('origin', window.location.origin); } catch (e) { /* ignore */ }
        params.set('rel', '0');
        params.set('modestbranding', '1');
        return `https://www.youtube.com/embed/${videoId}?${params.toString()}`;
    }

    async function checkEmbeddable(videoId) {
        const url = 'https://www.youtube.com/oembed?format=json&url=' + encodeURIComponent('https://www.youtube.com/watch?v=' + videoId);
        try {
            const resp = await fetch(url, { method: 'GET', cache: 'no-store' });
            return resp.ok;
        } catch (e) {
            return false;
        }
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

    document.addEventListener('DOMContentLoaded', async function () {
        const miniTvIframe = document.getElementById('mini-tv-video');
        const modalIframe = document.getElementById('modal-video');
        const modalElement = document.getElementById('videoModal');
        const bootstrapModal = modalElement && window.bootstrap ? new bootstrap.Modal(modalElement) : null;

        const videoId = (miniTvIframe && miniTvIframe.dataset.videoId) || (modalIframe && modalIframe.dataset.videoId) || DEFAULT_VIDEO_ID;

        [miniTvIframe, modalIframe].forEach(iframe => {
            if (!iframe) return;
            iframe.setAttribute('allow', 'autoplay; encrypted-media');
            iframe.setAttribute('referrerpolicy', 'no-referrer-when-downgrade');
        });

        const embeddable = await checkEmbeddable(videoId);

        if (embeddable) {
            if (miniTvIframe) {
                miniTvIframe.src = buildEmbedSrc(videoId, { autoplay: true, loop: true });
            }
        } else {
            if (miniTvIframe && miniTvIframe.parentNode) {
                const poster = document.createElement('div');
                poster.className = 'mini-tv-fallback';
                poster.style.cssText = 'width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:transparent;color:#fff;cursor:pointer;padding:10px;';
                poster.innerHTML = '<div style="text-align:center;"><strong>Watch on YouTube</strong><br><small>(video cannot be embedded)</small></div>';
                poster.addEventListener('click', () => {
                    window.open('https://www.youtube.com/watch?v=' + videoId, '_blank', 'noopener');
                });
                miniTvIframe.parentNode.replaceChild(poster, miniTvIframe);
            }
        }

        // openModal: show modal and request fullscreen (user gesture)
        window.openModal = function () {
            if (!embeddable) {
                window.open('https://www.youtube.com/watch?v=' + videoId, '_blank', 'noopener');
                return;
            }

            // pause mini player if possible
            if (!postYouTubeCommand(miniTvIframe, 'pauseVideo')) {
                try { if (miniTvIframe) miniTvIframe.src = ''; } catch (e) {}
            }

            if (modalIframe) {
                modalIframe.src = buildEmbedSrc(videoId, { autoplay: true, loop: false });
            }

            // show bootstrap modal
            bootstrapModal && bootstrapModal.show();

            // Try to request fullscreen on the modal element (user-initiated)
            try {
                if (modalElement && modalElement.requestFullscreen) {
                    modalElement.requestFullscreen().catch(()=>{ /* ignore fullscreen errors */ });
                } else if (modalElement && modalElement.classList) {
                    // fallback: try on modal iframe
                    modalIframe && modalIframe.requestFullscreen && modalIframe.requestFullscreen().catch(()=>{});
                }
            } catch (e) { /* ignore */ }
        };

        if (modalElement && modalIframe) {
            // when modal is hidden: stop video, clear src, exit fullscreen and restore mini
            modalElement.addEventListener('hidden.bs.modal', () => {
                if (!postYouTubeCommand(modalIframe, 'stopVideo')) {
                    try { modalIframe.src = ''; } catch (e) {}
                } else {
                    try { modalIframe.src = ''; } catch (e) {}
                }
                // exit fullscreen if active
                if (document.fullscreenElement) {
                    try { document.exitFullscreen(); } catch (e) { /* ignore */ }
                }
                if (embeddable && miniTvIframe) {
                    try { miniTvIframe.src = buildEmbedSrc(videoId, { autoplay: true, loop: true }); } catch (e) {}
                }
            });

            // ensure modal shown event also tries fullscreen (some browsers require shown event)
            modalElement.addEventListener('shown.bs.modal', () => {
                try {
                    if (!document.fullscreenElement) {
                        if (modalElement.requestFullscreen) modalElement.requestFullscreen().catch(()=>{});
                    }
                } catch (e) {}
            });
        }
    });
})();