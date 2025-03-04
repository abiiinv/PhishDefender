// ==UserScript==
// @name         MailHog Character Overlay
// @match        http://localhost:8025/*
// @grant        none
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';

    const overlayStyle = document.createElement('style');
    overlayStyle.textContent = `
        #character-overlay {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 1000;
            display: none; /* Initially hidden */
        }
    `;
    document.head.appendChild(overlayStyle);

    document.addEventListener('DOMContentLoaded', function() {
        const img = document.createElement('img');
        img.src = 'images/char1.svg';
        img.id = 'character-overlay';
        document.body.appendChild(img);

        // Show the overlay after everything is loaded
        img.style.display = 'block';

        function hideOverlay() {
            img.style.display = 'none';
        }

        document.addEventListener('click', hideOverlay);
        document.addEventListener('keydown', hideOverlay);
    });
})();
