const totalHeight = document.documentElement.scrollHeight;

document.addEventListener('mousemove', (event) => {
    const cursorLight = document.getElementById('cursor-light');
    cursorLight.style.left = `${event.clientX - cursorLight.offsetWidth / 2}px`;
    cursorLight.style.top = `${Math.min(event.clientY + window.scrollY, totalHeight) - cursorLight.offsetHeight / 2}px`;
    cursorLight.classList.remove('hidden');
});

document.addEventListener('mouseout', () => {
    const cursorLight = document.getElementById('cursor-light');
    cursorLight.classList.add('hidden');
});


function scaleIframes() {
    const containers = document.querySelectorAll('.laptop-frame');
    const iframes = document.querySelectorAll('iframe');
    for(let i =0; i<containers.length; i++){
        const scaleX = containers[i].clientWidth * 0.77/ 1920;
        const scaleY = containers[i].clientHeight * 0.875/ 1240;
        const scale = Math.min(scaleX, scaleY);
        iframes[i].style.transform = `scale(${scale})`;
    }
}

window.addEventListener('resize', scaleIframes);
window.addEventListener('load', scaleIframes);