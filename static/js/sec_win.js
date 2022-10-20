window.addEventListener("keydown", function(event) {
    if (event.key == 'F12') {
        // block F12 (DevTools)
        event.preventDefault();
        event.stopPropagation();
        return false;   
    
    } else if(event.key == 'F5') {
        // block F5 (DevTools)
        event.preventDefault();
        event.stopPropagation();
        return false;

    } else if (event.ctrlKey && event.shiftKey && event.key == 'I') {
        // block Ctrl+Shift+I (DevTools)
        event.preventDefault();
        event.stopPropagation();
        return false;

    } else if (event.ctrlKey && event.shiftKey && event.key == 'J') {
        // block Ctrl+Shift+J (Console)
        event.preventDefault();
        event.stopPropagation();
        return false;
    }else if (event.ctrlKey && event.key == 'u') {
        // block Ctrl+u (Console)
        event.preventDefault();
        event.stopPropagation();
        return false;
    } else if (event.ctrlKey && event.key == 'r') {
        // block Ctrl+r (Console)
        event.preventDefault();
        event.stopPropagation();
        return false;
    }
});

window.oncontextmenu = function(event) {
    // block right-click / context-menu
    event.preventDefault();
    event.stopPropagation();
    return false;
};