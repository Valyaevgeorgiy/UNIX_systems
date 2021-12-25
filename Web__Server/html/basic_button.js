arrColor = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];

function mouseOut() {
    for (i = 0; i < 13; i++)
        setTimeout('document.blinkbutton.button.style.background = "#' + arrColor[15 - i] + '0' + arrColor[15 - i] + 'FFF";', i * 50);
}

function mouseOver() {
    for (i = 0; i < 15; i++)
        setTimeout('document.blinkbutton.button.style.background = "#' + arrColor[i] + '0' + arrColor[i] + 'F31";', i * 50);
}