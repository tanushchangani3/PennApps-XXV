window.onload = () => {
    const transition = document.getElementById('page-transition');
    setTimeout(() => {
        transition.style.transition = 'opacity 0.5s ease';
        transition.style.opacity = '0';
    }, 100); // Short delay before the transition effect fades out
};

window.onbeforeunload = () => {
    const transition = document.getElementById('page-transition');
    transition.style.transition = 'opacity 0.5s ease';
    transition.style.opacity = '1';
};
