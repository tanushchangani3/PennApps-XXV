window.onload = () => {
    const blocks = document.querySelectorAll('.block');
    
    // Trigger the swipe-in animation after a slight delay
    setTimeout(() => {
        blocks.forEach(block => {
            block.style.transform = 'translateX(0)';  // Move blocks from off-screen to visible area
        });
    }, 100);  // Short delay to start the swipe-in animation

    // Wait for the blocks to swipe in, then fade out and disappear
    setTimeout(() => {
        blocks.forEach(block => {
            block.style.transition = 'opacity 0.5s ease';
            block.style.opacity = '0';  // Make the blocks transparent
        });
        
        // After the opacity transition, set display to 'none'
        setTimeout(() => {
            blocks.forEach(block => {
                block.style.display = 'none';
            });
        }, 500);  // Timeout to match opacity transition
    }, 1300);  // Ensure swipe animation completes first (slightly longer than block transition)
};

window.onbeforeunload = () => {
    const blocks = document.querySelectorAll('.block');
    
    // Reset block visibility and position when navigating away
    blocks.forEach(block => {
        block.style.display = 'block';  // Make sure blocks are visible again
        block.style.opacity = '1';      // Reset opacity
        block.style.transform = 'translateX(-100vw)';  // Move blocks off-screen left
    });

    // Trigger the swipe-in animation
    setTimeout(() => {
        blocks.forEach(block => {
            block.style.transform = 'translateX(0)';  // Move blocks back on screen
        });
    }, 100);  // Slight delay for smoother animation
};
