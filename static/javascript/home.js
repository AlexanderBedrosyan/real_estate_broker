const miniTvVideoId = 'KUvOUxkQpGg';
const modalVideoIframe = document.getElementById('modal-video');
const modalElement = document.getElementById('videoModal');
const bootstrapModal = new bootstrap.Modal(modalElement);

function openModal() {
    const modalVideoSrc = `https://www.youtube.com/embed/${miniTvVideoId}?autoplay=1`;
    modalVideoIframe.src = modalVideoSrc;

    const miniTvIframe = document.getElementById('mini-tv-video');
    miniTvIframe.src = "";

    bootstrapModal.show();
}

modalElement.addEventListener('hidden.bs.modal', () => {
    modalVideoIframe.src = "";

    const miniTvIframe = document.getElementById('mini-tv-video');
    miniTvIframe.src = `https://www.youtube.com/embed/${miniTvVideoId}?autoplay=1&mute=1&loop=1&playlist=${miniTvVideoId}`;
});


document.addEventListener("DOMContentLoaded", function() {

    const mediaElements = document.querySelectorAll("audio, video");
    mediaElements.forEach(element => {
        element.muted = true;
    });

    const iframeElements = document.querySelectorAll("iframe");
    iframeElements.forEach(iframe => {
        const src = iframe.src;
        if (src.includes("youtube.com/embed")) {
            const mutedSrc = appendMuteToYouTubeURL(src);
            iframe.src = mutedSrc;
        }
    });
});


function appendMuteToYouTubeURL(url) {
    const urlObj = new URL(url);
    urlObj.searchParams.set("mute", "1"); 
    return urlObj.toString();
}