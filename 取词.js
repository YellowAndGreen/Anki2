function getWord(){     
var word = window.getSelection?    window.getSelection():    document.selection.createRange().text    

}
document.body.addEventListener("click", getWord, false)



s = window.getSelection();
oRange = s.getRangeAt(0); //get the text range
oRect = oRange.getBoundingClientRect();